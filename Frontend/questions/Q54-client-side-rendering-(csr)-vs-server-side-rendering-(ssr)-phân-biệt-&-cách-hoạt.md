# 🖥️ Q54: Client-Side Rendering (CSR) vs Server-Side Rendering (SSR) - Phân Biệt & Cách Hoạt Động Chi Tiết




**Trả lời:**

#### **🎯 Khái Niệm Cốt Lõi**

**CSR (Client-Side Rendering):**
- Server gửi **HTML rỗng** (chỉ có `<div id="root"></div>`) + **JavaScript bundle** (500KB-2MB)
- Browser **download JS → parse → execute → render** → hiển thị nội dung
- Giống như: Mua IKEA furniture (phải tự lắp ráp ở nhà)
- Rendering engine: Browser (Chrome V8, Firefox SpiderMonkey)

**SSR (Server-Side Rendering):**
- Server **render sẵn HTML đầy đủ** (có nội dung) rồi gửi về browser
- Browser **hiển thị ngay** HTML → sau đó download JS để tương tác
- Giống như: Mua furniture đã lắp ráp sẵn (chỉ cần đặt vào nhà)
- Rendering engine: Node.js server (React renderToString)


#### **✅ Ưu Điểm CSR (Client-Side Rendering)**

**1. Navigation Cực Nhanh (Fast SPA Navigation)**
```
User clicks link:
- CSR: 0ms (chỉ thay đổi DOM, không reload page)
- SSR: 500-1000ms (phải request server, đợi render)
→ Trải nghiệm mượt mà như native app
```

**2. Rich Interactions (Tương Tác Phong Phú)**
```typescript
// CSR: Dễ dàng làm real-time features
- Live chat, notifications
- Drag & drop, animations
- Real-time data updates
- Complex state management
→ Full JavaScript power trên browser
```

**3. Server Load Thấp (Less Server Load)**
```
- Server chỉ serve static files (HTML, JS, CSS)
- Không cần render cho mỗi request
- Dễ cache với CDN
- Cost thấp (chỉ cần CDN, không cần powerful server)
```

**4. Dễ Deploy & Scale**
```
- Deploy lên CDN (Vercel, Netlify, CloudFront)
- Không cần server-side logic
- Auto-scale với CDN
→ Chi phí thấp, dễ maintain
```

---

#### **❌ Nhược Điểm CSR**

**1. Initial Load Chậm (Slow First Load)**
```
Timeline:
[0s] User clicks link
[0-1s] Download HTML (5KB) - nhanh
[1-3s] Download JS bundle (500KB-2MB) - CHẬM
[3-4s] Parse & Execute JS - CHẬM
[4-5s] Fetch API data - CHẬM
[5s] User sees content - QUÁ LÂU!

→ User thấy blank screen trong 3-5 giây
→ Bounce rate cao (user rời trang)
```

**2. SEO Nghèo Nàn (Poor SEO)**
```html
<!-- Google bot sees: -->
<html>
  <body>
    <div id="root"></div>  <!-- EMPTY! -->
    <script src="bundle.js"></script>
  </body>
</html>

→ Google không thấy nội dung
→ Không index được
→ SEO ranking thấp
```

**3. Blank Screen Problem**
```
User experience:
[0-3s] White/blank screen (nothing to see)
[3-5s] Loading spinner (still waiting...)
[5s+] Content appears (finally!)

→ User frustrated
→ Think website is broken
→ Leave before content loads
```

**4. Phụ Thuộc JavaScript**
```
- User disable JS → website không chạy
- JS error → website crash
- Slow device → website lag
→ Không graceful degradation
```

---

#### **✅ Ưu Điểm SSR (Server-Side Rendering)**

**1. Initial Load Cực Nhanh (Fast Time to Content)**
```
Timeline:
[0s] User clicks link
[0.5s] Server renders HTML (nhanh vì server mạnh)
[0.5s] Browser receives full HTML
[0.5s] User SEES content immediately!
[1-2s] JS hydrates in background
[2s] Fully interactive

→ User thấy nội dung trong 0.5-1 giây
→ First impression tốt
```

**2. SEO Xuất Sắc (SEO-Friendly)**
```html
<!-- Google bot sees: -->
<html>
  <body>
    <div id="root">
      <h1>Welcome to My Site</h1>
      <p>Full content here...</p>
      <article>Blog post content...</article>
      <!-- FULL CONTENT! -->
    </div>
  </body>
</html>

→ Google index đầy đủ nội dung
→ Better ranking
→ Social media previews work (Open Graph)
```

**3. Better Performance (Đặc biệt cho slow devices)**
```
- Server render nhanh (powerful CPU)
- User device không cần làm việc nặng
- Suitable for low-end phones
- Ít JS → less battery drain
```

**4. Không Blank Screen**
```
User experience:
[0.5s] Content appears immediately!
[1-2s] Page becomes interactive

→ Progressive enhancement
→ Even if JS fails, HTML still works
→ Better perceived performance
```

---

#### **❌ Nhược Điểm SSR**

**1. Server Load Cao (High Server Cost)**
```
CSR:
- Server: "Here's HTML + JS" (1 lần, cache được)
- Cost: $5/month (CDN)

SSR:
- Server: "Let me render this page..." (mỗi request)
- Server: Parse React → Fetch data → Render HTML
- Cost: $50-500/month (cần server mạnh)

→ 10-100x chi phí hơn CSR
```

**2. Navigation Chậm Hơn (Slower Navigation)**
```
User clicks internal link:

CSR:
- Instant (0ms) - chỉ update DOM
- Smooth transition

SSR:
- Request server (50-200ms network)
- Server render (50-100ms)
- Download HTML (50-200ms)
- Total: 500-1000ms
→ Có thể thấy "flash" khi chuyển trang
```

**3. Complexity Cao (Complex Setup)**
```typescript
// CSR: Simple
ReactDOM.render(<App />, root);

// SSR: Complex
- Server setup (Express, Next.js)
- Hydration issues (client-server mismatch)
- Data fetching strategies
- Cache invalidation
- State management across server-client
→ Nhiều bugs tiềm ẩn, khó debug
```

**4. TTFB Cao Hơn (Time to First Byte)**
```
CSR:
- TTFB: 50ms (serve static file)

SSR:
- TTFB: 200-500ms (render + fetch data)
→ User đợi lâu hơn trước khi thấy gì đó
(nhưng khi thấy thì đã có full content)
```

**5. Hydration Issues**
```typescript
// Server renders: <div>Count: 0</div>
// Client state:   <div>Count: 1</div>
// → Mismatch! Warning!

// Common issues:
- Date.now() khác nhau server vs client
- Random values
- Browser-only APIs (window, localStorage)
→ Requires careful coding
```

---

#### **📊 So Sánh Trực Quan**

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER EXPERIENCE COMPARISON                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  CSR (Client-Side Rendering):                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 0s ▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░  ← Blank screen          │  │
│  │ 1s ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░  ← Downloading JS         │  │
│  │ 2s ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░  ← Parsing JS             │  │
│  │ 3s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░  ← Fetching data          │  │
│  │ 4s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░  ← Rendering               │  │
│  │ 5s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ✅ Content visible!      │  │
│  │                                                            │  │
│  │ First Content: 5 seconds                                  │  │
│  │ User sees: Blank → Loading → Content                     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
│  SSR (Server-Side Rendering):                                   │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ 0s ▓░░░░░░░░░░░░░░░░░░░░░░░░░░  ← Server rendering      │  │
│  │ 0.5s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ✅ Content visible!      │  │
│  │ 1s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ← Hydrating JS            │  │
│  │ 2s ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ✅ Interactive!           │  │
│  │                                                            │  │
│  │ First Content: 0.5 seconds                                │  │
│  │ Interactive: 2 seconds                                    │  │
│  │ User sees: Content immediately → Becomes interactive     │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

#### **🎯 Khi Nào Dùng Gì?**

**Dùng CSR khi:**
```
✅ Internal tools / Admin dashboard
   → Không cần SEO, user đã login
   → Example: Google Analytics, Jira, Notion

✅ Highly interactive apps
   → Real-time updates, complex interactions
   → Example: Figma, Trello, Games

✅ Budget thấp
   → Chỉ cần CDN, không cần server mạnh
   → Startup với limited resources
```

**Dùng SSR khi:**
```
✅ Public-facing websites
   → Cần SEO, social sharing
   → Example: Blog, News, E-commerce

✅ Landing pages / Marketing
   → First impression matters
   → Better conversion rate

✅ Content-heavy sites
   → Nhiều text, ít interaction
   → Example: Documentation, Wikipedia
```

**Dùng SSG (Hybrid) khi:**
```
✅ Static content with occasional updates
   → Blog posts, product pages
   → Example: Next.js with ISR

✅ Best of both worlds
   → Fast như CSR (served from CDN)
   → SEO-friendly như SSR
   → Cost-effective
```

---

#### **💡 Key Takeaways**

**CSR (Client-Side):**
- 🚀 Navigation nhanh, tương tác mượt
- 💰 Chi phí thấp, dễ deploy
- ❌ Initial load chậm (3-5s), SEO kém
- 🎯 **Dùng cho**: Internal tools, SPAs, interactive apps

**SSR (Server-Side):**
- ⚡ Initial load nhanh (0.5-1s), SEO tốt
- ✅ Không blank screen, better UX
- ❌ Server cost cao, navigation chậm hơn
- 🎯 **Dùng cho**: Public sites, marketing, e-commerce

**Modern Approach:**
- **Mix cả 3**: SSG (static pages) + SSR (dynamic) + CSR (interactive)
- **Framework**: Next.js, Remix, Nuxt.js hỗ trợ cả 3
- **Measure**: Dùng Lighthouse, Web Vitals để optimize

---

#### **📊 Sơ Đồ So Sánh CSR vs SSR**

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CSR vs SSR COMPARISON                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  CLIENT-SIDE RENDERING (CSR)                                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ 1. Browser Request → Server                                   │ │
│  │    GET https://example.com                                    │ │
│  │                                                                │ │
│  │ 2. Server Response (Minimal HTML)                             │ │
│  │    <!DOCTYPE html>                                            │ │
│  │    <html><head>...</head>                                     │ │
│  │    <body>                                                     │ │
│  │      <div id="root"></div>  ← Empty!                         │ │
│  │      <script src="/bundle.js"></script>                      │ │
│  │    </body></html>                                            │ │
│  │                                                                │ │
│  │ 3. Browser Downloads JS Bundle (Large!)                       │ │
│  │    bundle.js (500KB - 2MB)                                    │ │
│  │    ⏱️  Parsing + Execution time                               │ │
│  │                                                                │ │
│  │ 4. JavaScript Runs & Renders UI                               │ │
│  │    React.render(<App />, root)                               │ │
│  │    → API calls                                                │ │
│  │    → Fetch data                                               │ │
│  │    → Render components                                        │ │
│  │                                                                │ │
│  │ 5. User Sees Content                                          │ │
│  │    ⏱️  Total: 3-5 seconds                                     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  SERVER-SIDE RENDERING (SSR)                                       │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ 1. Browser Request → Server                                   │ │
│  │    GET https://example.com                                    │ │
│  │                                                                │ │
│  │ 2. Server Renders Full HTML                                   │ │
│  │    - Execute React on server                                  │ │
│  │    - Fetch data from database                                 │ │
│  │    - Generate complete HTML                                   │ │
│  │    ⏱️  Server processing time                                 │ │
│  │                                                                │ │
│  │ 3. Server Response (Full HTML)                                │ │
│  │    <!DOCTYPE html>                                            │ │
│  │    <html><head>...</head>                                     │ │
│  │    <body>                                                     │ │
│  │      <div id="root">                                          │ │
│  │        <h1>Welcome!</h1>                                      │ │
│  │        <p>Fully rendered content...</p>  ← Complete!         │ │
│  │      </div>                                                   │ │
│  │      <script src="/bundle.js"></script>                      │ │
│  │    </body></html>                                            │ │
│  │                                                                │ │
│  │ 4. Browser Shows Content Immediately                          │ │
│  │    ⏱️  User sees content: 0.5-1 second                        │ │
│  │                                                                │ │
│  │ 5. JavaScript Hydrates (Makes Interactive)                    │ │
│  │    React.hydrate(<App />, root)                              │ │
│  │    → Attach event listeners                                   │ │
│  │    → Make interactive                                         │ │
│  │    ⏱️  Total interactive: 2-3 seconds                         │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

#### **🔥 CSR (Client-Side Rendering) - Cách Hoạt Động Chi Tiết**

**Timeline:**

```
User clicks link
      ↓
[1] Browser → Server: GET /page
      ↓
[2] Server → Browser: Minimal HTML + <script src="bundle.js">
      ↓                 (5-50 KB)
      ↓
[3] Browser downloads bundle.js
      ↓                 (500KB - 2MB)
      ↓                 ⏱️  1-3 seconds
      ↓
[4] Browser parses & executes JS
      ↓                 ⏱️  0.5-1 second
      ↓
[5] React renders virtual DOM
      ↓
[6] React makes API calls
      ↓                 ⏱️  0.5-2 seconds
      ↓
[7] Data arrives → Re-render
      ↓
[8] User sees content
      ↓                 ⏱️  Total: 3-5 seconds
```

**Code Example (React CSR):**

```typescript
// ============================================
// CSR Example - React App
// ============================================

// index.html - Minimal HTML (chỉ có div rỗng)
// <!DOCTYPE html>
// <html>
// <head>
//   <title>My App</title>
// </head>
// <body>
//   <div id="root"></div>  ← EMPTY!
//   <script src="/bundle.js"></script>
// </body>
// </html>

// main.tsx - Entry point
import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Render app on client
const root = ReactDOM.createRoot(document.getElementById('root')!);
root.render(<App />);

// App.tsx - Main component
import { useState, useEffect } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

function App() {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);

  // Fetch data on client
  useEffect(() => {
    fetch('https://api.example.com/users')
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>; // User sees loading state
  }

  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

// ============================================
// What happens in browser:
// ============================================
// 1. Download HTML (5KB) - instant
// 2. Download bundle.js (500KB) - 1-2 seconds
// 3. Parse & execute JS - 0.5 seconds
// 4. React renders <div>Loading...</div>
// 5. Fetch API - 0.5-1 second
// 6. Re-render with data
// Total: 3-5 seconds until user sees content
```

---

#### **🚀 SSR (Server-Side Rendering) - Cách Hoạt Động Chi Tiết**

**Timeline:**

```
User clicks link
      ↓
[1] Browser → Server: GET /page
      ↓
[2] Server executes React
      ↓
[3] Server fetches data from DB
      ↓                 ⏱️  0.1-0.5 seconds
      ↓
[4] Server renders HTML
      ↓                 ⏱️  0.1-0.3 seconds
      ↓
[5] Server → Browser: Full HTML
      ↓                 (50-200 KB)
      ↓
[6] Browser displays HTML immediately
      ↓                 ⏱️  User sees content: 0.5-1 second
      ↓
[7] Browser downloads JS bundle
      ↓                 (background)
      ↓
[8] Hydration - Make interactive
      ↓                 ⏱️  0.5-1 second
      ↓
[9] Fully interactive
      ↓                 ⏱️  Total interactive: 2-3 seconds
```

**Code Example (Next.js SSR):**

```typescript
// ============================================
// SSR Example - Next.js
// ============================================

// pages/users.tsx - SSR page
import { GetServerSideProps } from 'next';

interface User {
  id: number;
  name: string;
  email: string;
}

interface Props {
  users: User[];
}

// This function runs on SERVER for every request
export const getServerSideProps: GetServerSideProps<Props> = async () => {
  // Fetch data on server
  const res = await fetch('https://api.example.com/users');
  const users = await res.json();

  // Pass data to component as props
  return {
    props: {
      users, // This data is already available!
    },
  };
};

// Component renders on server
function UsersPage({ users }: Props) {
  // No loading state needed - data is already here!
  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.name} - {user.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default UsersPage;

// ============================================
// What happens:
// ============================================
// 1. User requests /users
// 2. Next.js server:
//    - Runs getServerSideProps()
//    - Fetches data from API
//    - Renders component to HTML string
//    - Sends full HTML to browser
// 3. Browser displays HTML immediately (0.5-1s)
// 4. JavaScript hydrates in background
// 5. Page becomes interactive (2-3s total)

// ============================================
// HTML sent to browser (Full content!):
// ============================================
// <!DOCTYPE html>
// <html>
// <head>
//   <title>My App</title>
// </head>
// <body>
//   <div id="__next">
//     <div>
//       <h1>Users</h1>
//       <ul>
//         <li>John Doe - john@example.com</li>
//         <li>Jane Smith - jane@example.com</li>
//         <!-- Full content already rendered! -->
//       </ul>
//     </div>
//   </div>
//   <script src="/_next/static/bundle.js"></script>
// </body>
// </html>
```

---

#### **📊 So Sánh Chi Tiết CSR vs SSR**

```
┌──────────────────────┬──────────────────────────┬──────────────────────────┐
│ Tiêu Chí             │ CSR (Client-Side)        │ SSR (Server-Side)        │
├──────────────────────┼──────────────────────────┼──────────────────────────┤
│ Initial Load         │ ❌ 3-5 seconds           │ ✅ 0.5-1 second          │
│ Time to Interactive  │ ✅ 3-5 seconds           │ ⚠️  2-3 seconds          │
│ SEO                  │ ❌ Poor (empty HTML)     │ ✅ Excellent (full HTML) │
│ Server Load          │ ✅ Low (serve static)    │ ❌ High (render per req) │
│ Complexity           │ ✅ Simple                │ ❌ Complex               │
│ Navigation Speed     │ ✅ Instant               │ ⚠️  Slower (re-render)   │
│ Bundle Size          │ ❌ Large (500KB-2MB)     │ ⚠️  Medium (same JS)     │
│ Blank Screen         │ ❌ Yes (before hydrate)  │ ✅ No (HTML ready)       │
│ API Calls            │ ❌ Client (slow)         │ ✅ Server (fast)         │
│ Caching              │ ✅ Easy (CDN)            │ ⚠️  Complex (per-user)   │
│ Cost                 │ ✅ Low (CDN only)        │ ❌ High (servers)        │
│ User Experience      │ ⚠️  Initial: Poor        │ ✅ Initial: Great        │
│                      │ ✅ After load: Great     │ ⚠️  Navigation: OK       │
└──────────────────────┴──────────────────────────┴──────────────────────────┘
```

---

#### **🎯 Use Cases - Khi Nào Dùng CSR vs SSR?**

**✅ Dùng CSR khi:**

```typescript
// 1. Admin Dashboard / Internal Tools
// - Không cần SEO
// - User đã logged in
// - Rich interactions
// - Example: Analytics dashboard, CRM

// 2. SPAs with Auth
// - Dashboard, Settings
// - User profile pages
// - Tools, calculators

// 3. Highly Interactive Apps
// - Drawing apps
// - Games
// - Real-time collaboration tools

// Example:
const AdminDashboard = () => {
  return (
    <div>
      <Chart data={realtimeData} /> {/* Real-time updates */}
      <DataGrid onEdit={handleEdit} /> {/* Complex interactions */}
    </div>
  );
};
```

**✅ Dùng SSR khi:**

```typescript
// 1. Public Content / Marketing
// - Landing pages
// - Blogs, News
// - E-commerce product pages
// - Example: Company website, Blog

// 2. SEO-Critical Pages
// - Product listings
// - Article pages
// - Search result pages

// 3. Dynamic Content
// - Personalized homepages
// - Location-based content
// - User-specific dashboards

// Example:
export const getServerSideProps = async (context) => {
  // Fetch based on user location
  const { country } = context.req.geo;
  const products = await fetchProductsByCountry(country);

  return { props: { products } };
};

const ProductPage = ({ products }) => {
  return (
    <div>
      <h1>Products in Your Region</h1>
      {products.map((p) => (
        <ProductCard key={p.id} {...p} />
      ))}
    </div>
  );
};
```

---

#### **⚡ Hybrid Approach - Static Site Generation (SSG)**

Next.js còn có SSG (Static Site Generation) - best of both worlds:

```typescript
// ============================================
// SSG Example - Next.js
// ============================================

// Build time: Generate static HTML
export const getStaticProps: GetStaticProps = async () => {
  // This runs at BUILD TIME, not per request
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();

  return {
    props: { posts },
    revalidate: 60, // Re-generate every 60 seconds (ISR)
  };
};

// Component
const BlogPage = ({ posts }) => {
  return (
    <div>
      <h1>Blog Posts</h1>
      {posts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  );
};

// ============================================
// Benefits:
// ============================================
// ✅ Fast as CSR (served from CDN)
// ✅ SEO-friendly like SSR
// ✅ No server rendering cost
// ✅ ISR (Incremental Static Regeneration)

// Timeline:
// [Build] Generate HTML → Deploy to CDN
//    ↓
// [Request] CDN → Browser (instant!)
//    ↓
// [Background] Re-validate every 60s
```

---

#### **📋 Best Practices**

**1. CSR Optimization:**

```typescript
// ✅ Code splitting
import { lazy, Suspense } from 'react';

const HeavyComponent = lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<Loading />}>
      <HeavyComponent />
    </Suspense>
  );
}

// ✅ Preload critical data
<link rel="preload" href="/api/users" as="fetch" crossOrigin="anonymous" />

// ✅ Service Worker caching
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('/sw.js');
}
```

**2. SSR Optimization:**

```typescript
// ✅ Cache rendered pages
import { NextResponse } from 'next/server';

export async function middleware(request) {
  const response = NextResponse.next();
  response.headers.set('Cache-Control', 'public, max-age=60, stale-while-revalidate=120');
  return response;
}

// ✅ Streaming SSR (React 18)
import { renderToReadableStream } from 'react-dom/server';

const stream = await renderToReadableStream(<App />);
return new Response(stream);

// ✅ Selective hydration
<div suppressHydrationWarning>{serverOnlyContent}</div>
```

**3. Hybrid Strategy:**

```typescript
// ✅ Mix CSR + SSR + SSG
// - SSG: Static pages (blog, docs)
// - SSR: Dynamic pages (user profile)
// - CSR: Interactive parts (comments, likes)

// pages/post/[id].tsx
export const getStaticProps = async ({ params }) => {
  const post = await fetchPost(params.id); // SSG
  return { props: { post } };
};

const PostPage = ({ post }) => {
  return (
    <div>
      {/* SSG content */}
      <article>{post.content}</article>

      {/* CSR interactive part */}
      <Comments postId={post.id} />
      <LikeButton postId={post.id} />
    </div>
  );
};
```

---

#### **🔍 Debugging & Measuring**

```typescript
// 1. Measure Time to First Byte (TTFB)
performance.getEntriesByType('navigation')[0].responseStart;

// 2. Measure First Contentful Paint (FCP)
new PerformanceObserver((list) => {
  for (const entry of list.getEntries()) {
    console.log('FCP:', entry.startTime);
  }
}).observe({ entryTypes: ['paint'] });

// 3. Detect SSR vs CSR
const isSSR = typeof window === 'undefined';
console.log('Rendering on:', isSSR ? 'Server' : 'Client');

// 4. Chrome DevTools
// - Network tab: Check HTML size (SSR = large, CSR = small)
// - Performance tab: Check rendering timeline
// - Lighthouse: Run audit for SSR vs CSR
```

---

#### **❌ Common Mistakes**

```typescript
// ❌ MISTAKE 1: Using window/document in SSR
function MyComponent() {
  const width = window.innerWidth; // ❌ Error: window is not defined
  return <div style={{ width }}></div>;
}

// ✅ FIX: Check environment
function MyComponent() {
  const [width, setWidth] = useState(0);

  useEffect(() => {
    if (typeof window !== 'undefined') {
      setWidth(window.innerWidth);
    }
  }, []);

  return <div style={{ width }}></div>;
}

// ❌ MISTAKE 2: Fetching data in useEffect for SSR
export default function Page() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/data').then(/* ... */); // ❌ Runs on client!
  }, []);

  return <div>{data?.title}</div>;
}

// ✅ FIX: Use getServerSideProps
export const getServerSideProps = async () => {
  const data = await fetch('/api/data').then((r) => r.json());
  return { props: { data } };
};

export default function Page({ data }) {
  return <div>{data.title}</div>; // ✅ Data already available
}

// ❌ MISTAKE 3: Over-using SSR
// Don't SSR everything - mix strategies!

// ✅ GOOD: Strategic mix
// - SSG: Blog posts, docs (static)
// - SSR: User dashboard (dynamic)
// - CSR: Admin panel (no SEO needed)
```

---

#### **📊 Real-world Performance Comparison**

```typescript
// Example: E-commerce Product Page

// CSR (Create React App):
// - Initial Load: 3.5 seconds
// - Time to Interactive: 3.5 seconds
// - Lighthouse Score: 40/100
// - SEO: ❌ Poor (Google sees empty HTML)

// SSR (Next.js):
// - Initial Load: 1.2 seconds
// - Time to Interactive: 2.8 seconds
// - Lighthouse Score: 85/100
// - SEO: ✅ Excellent (Google sees full content)

// SSG (Next.js ISR):
// - Initial Load: 0.5 seconds (CDN)
// - Time to Interactive: 1.8 seconds
// - Lighthouse Score: 95/100
// - SEO: ✅ Excellent + fast delivery
```

---

#### **🎯 Decision Tree**

```
Start
  ↓
SEO needed?
  ├─ No → CSR (React, Vue, Angular SPA)
  │
  └─ Yes → Content changes frequently?
           ├─ No → SSG (Next.js, Gatsby)
           │        - Blog, docs, marketing
           │
           └─ Yes → Per-user content?
                    ├─ No → SSR with cache
                    │        - News, products
                    │
                    └─ Yes → SSR + ISR
                             - User dashboards
                             - Personalized pages
```

---

#### **💡 Summary**

**CSR (Client-Side Rendering):**

- ✅ Best for: SPAs, admin tools, internal apps
- ✅ Pros: Simple, fast navigation, low server cost
- ❌ Cons: Slow initial load, poor SEO, blank screen

**SSR (Server-Side Rendering):**

- ✅ Best for: Public pages, SEO-critical, e-commerce
- ✅ Pros: Fast initial load, SEO-friendly, no blank screen
- ❌ Cons: High server cost, complex, slower navigation

**SSG (Static Site Generation):**

- ✅ Best for: Blogs, docs, marketing pages
- ✅ Pros: Fastest, SEO-friendly, low cost (CDN)
- ❌ Cons: Stale data (solved with ISR)

**Modern Approach:**

```typescript
// Mix all three strategies!
// - SSG for static pages (blog, docs)
// - SSR for dynamic pages (user profile, search)
// - CSR for interactive parts (comments, likes)

// Example: E-commerce site
// - Homepage: SSG (revalidate hourly)
// - Product page: SSR (real-time inventory)
// - Cart: CSR (no SEO needed)
// - Checkout: SSR (security + UX)
```

**Key Takeaway:**

- There's NO "best" approach - choose based on requirements
- Modern frameworks (Next.js, Remix) support all strategies
- Measure with real data: TTFB, FCP, TTI, Lighthouse
- SEO + Performance = SSR/SSG
- Interactivity + Simple = CSR


```
💧 Hydration là quá trình Server render ra HTML → Browser hiển thị ngay → Sau đó React “gắn” event listeners vào HTML → UI trở nên tương tác được.

"Hydration là bước React biến HTML do SSR hoặc SSG render sẵn thành UI có thể tương tác, bằng cách attach event listeners và khôi phục state.

HTML từ server ngay lập tức giúp cải thiện SEO và First Contentful Paint, còn hydration giúp UI hoạt động như SPA. Thách thức lớn nhất là tránh hydration mismatch và tối ưu cost hydration trong các trang lớn bằng techniques như partial/lazy hydration.
```