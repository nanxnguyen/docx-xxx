# ⚡ Q41: Next.js Workflow & Version Comparison - Next.js 14 vs 15 vs 16


**⚡ Quick Summary:**
> Next.js 14 = App Router stable + Server Actions + Turbopack. Next.js 15 = React 19 + Async Request APIs + Partial Prerendering. Next.js 16 = Cache cải tiến + Improved DX. Workflow: Page/Layout → Rendering (SSR/SSG/ISR) → Data Fetching → Deployment.

**💡 Ghi Nhớ:**
- 📁 **Next.js 14**: App Router production-ready, Server Actions, Turbopack dev (beta)
- 🚀 **Next.js 15**: React 19, Async Request APIs (cookies/headers), Partial Prerendering
- ⚡ **Next.js 16**: Cache behavior changes, Better DX, Performance improvements
- 🎯 **Workflow**: Routing → Rendering Strategy → Data Fetching → Build → Deploy

---

## **1. Next.js Workflow - Luồng Hoạt Động**

### **1.1. Overall Architecture (Kiến Trúc Tổng Quan)**

```
📊 Next.js Request Flow:

Browser Request (/) 
    ↓
Next.js Router (App Router hoặc Pages Router)
    ↓
Layout Wrapper (app/layout.tsx - Shared UI)
    ↓
Page Component (app/page.tsx)
    ↓
Rendering Strategy (SSR/SSG/ISR)
    ↓
Data Fetching (fetch, DB query...)
    ↓
React Server Component (RSC) - Render trên server
    ↓
Send HTML + RSC Payload đến client
    ↓
Hydration - React "kích hoạt" interactivity
    ↓
Client-side Navigation (Fast, no full reload)
```

---

### **1.2. File-Based Routing (Routing Dựa Trên File)**

**App Router (Next.js 13+):**

```typescript
📁 Project Structure:

app/
  ├── layout.tsx         // 🌐 Root layout (bọc tất cả pages)
  ├── page.tsx           // 🏠 Homepage (/)
  ├── about/
  │   └── page.tsx       // 📄 About page (/about)
  ├── blog/
  │   ├── page.tsx       // 📝 Blog list (/blog)
  │   └── [slug]/
  │       └── page.tsx   // 📰 Blog post (/blog/my-post)
  └── api/
      └── users/
          └── route.ts   // 🔌 API endpoint (/api/users)
```

**Giải thích:**

```typescript
// app/layout.tsx - Root Layout (Bọc tất cả pages)
export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="vi">
      <body>
        <header>Logo + Menu</header> {/* Header chung cho tất cả pages */}
        {children} {/* Nội dung page cụ thể */}
        <footer>Footer</footer> {/* Footer chung */}
      </body>
    </html>
  );
}

// app/page.tsx - Homepage
export default function HomePage() {
  return <h1>Trang chủ</h1>; // Hiển thị tại route "/"
}

// app/blog/[slug]/page.tsx - Dynamic Route (Route động)
export default async function BlogPost({ params }: { params: { slug: string } }) {
  // params.slug = "my-post" khi URL là /blog/my-post
  const post = await getPostBySlug(params.slug); // Fetch data từ database
  
  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
}
```

---

### **1.3. Rendering Strategies (Chiến Lược Render)**

**3 strategies chính:**

```typescript
/**
 * 1️⃣ SSR (Server-Side Rendering) - Render mỗi request
 * 
 * 🎯 Khi nào dùng:
 * - Data thay đổi liên tục (real-time)
 * - Cần personalization (user-specific data)
 * - SEO quan trọng + data dynamic
 * 
 * ⚡ Performance:
 * - TTFB: Chậm hơn (vì render mỗi request)
 * - SEO: ✅ Tốt (HTML đầy đủ)
 * - Cache: ❌ Khó cache server-side
 */

// SSR Example - Force dynamic rendering
export const dynamic = 'force-dynamic'; // Next.js 14+

export default async function DashboardPage() {
  // ⚡ Code này chạy MỖI REQUEST
  const user = await getCurrentUser(); // Fetch user từ session
  const notifications = await getNotifications(user.id); // Fetch notifications mới nhất
  
  return (
    <div>
      <h1>Xin chào, {user.name}!</h1>
      <p>Bạn có {notifications.length} thông báo mới</p>
    </div>
  );
  // 📊 Timeline: Request → Server render → Send HTML → Client hydrate
}

/**
 * 2️⃣ SSG (Static Site Generation) - Pre-render lúc build
 * 
 * 🎯 Khi nào dùng:
 * - Data ít thay đổi (blog, docs)
 * - Landing pages, marketing pages
 * - Performance tối đa (CDN cache)
 * 
 * ⚡ Performance:
 * - TTFB: ✅ Cực nhanh (serve HTML tĩnh)
 * - SEO: ✅ Tốt nhất
 * - Cache: ✅ Cache dễ dàng (CDN)
 */

// SSG Example - Generate at build time
export default async function BlogPost({ params }: { params: { slug: string } }) {
  // ⚡ Code này chạy LÚC BUILD (npm run build)
  const post = await getPostBySlug(params.slug); // Query database
  
  return (
    <article>
      <h1>{post.title}</h1>
      <p>{post.content}</p>
    </article>
  );
  // 📊 Timeline: Build time → Generate HTML → Deploy → Serve tĩnh
}

// Tạo list các pages cần build
export async function generateStaticParams() {
  const posts = await getAllPosts(); // Lấy tất cả bài viết
  
  return posts.map(post => ({
    slug: post.slug // Next.js sẽ generate /blog/post-1, /blog/post-2...
  }));
}

/**
 * 3️⃣ ISR (Incremental Static Regeneration) - Hybrid approach
 * 
 * 🎯 Khi nào dùng:
 * - Data thay đổi định kỳ (vài phút/giờ)
 * - E-commerce (product pages)
 * - News sites (articles)
 * 
 * ⚡ Performance:
 * - TTFB: ✅ Nhanh (serve static, regen background)
 * - SEO: ✅ Tốt
 * - Cache: ✅ CDN cache + auto-revalidate
 */

// ISR Example - Revalidate every 60 seconds
export const revalidate = 60; // Revalidate mỗi 60 giây

export default async function ProductPage({ params }: { params: { id: string } }) {
  // ⚡ Code này:
  // - Lúc build: Generate HTML tĩnh
  // - Runtime: Serve static
  // - Sau 60s: Regenerate HTML mới ở background
  const product = await getProduct(params.id);
  
  return (
    <div>
      <h1>{product.name}</h1>
      <p>Giá: {product.price} VNĐ</p>
      <p>Còn lại: {product.stock} sản phẩm</p>
    </div>
  );
  // 📊 Timeline:
  // Request 1 (0s): Serve static HTML (old data)
  // Request 2 (61s): Serve static HTML + Trigger regen background
  // Request 3 (62s): Serve NEW HTML (updated data)
}
```

---

### **1.4. Data Fetching (Lấy Dữ Liệu)**

**Server Components (Mặc định trong App Router):**

```typescript
// app/blog/page.tsx - Server Component
export default async function BlogPage() {
  // ✅ Fetch TRỰC TIẾP trên server
  const posts = await db.posts.findMany(); // Query database
  // 👉 Không cần useEffect, không cần useState
  // 👉 Code này chạy trên SERVER, không gửi xuống client
  // 👉 Database credentials KHÔNG lộ ra client
  
  return (
    <div>
      <h1>Danh sách bài viết</h1>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  );
}

/**
 * ✅ Ưu điểm Server Component:
 * - Fetch data gần database (low latency)
 * - Không tốn bundle size client (code không gửi xuống browser)
 * - Bảo mật hơn (secrets không lộ)
 * - SEO tốt (HTML đầy đủ)
 */
```

**Client Components (Khi cần interactivity):**

```typescript
// app/components/LikeButton.tsx - Client Component
'use client'; // 👉 Bắt buộc khai báo 'use client' ở đầu file

import { useState } from 'react';

export default function LikeButton({ postId }: { postId: string }) {
  const [likes, setLikes] = useState(0);
  const [isLiked, setIsLiked] = useState(false);

  const handleLike = async () => {
    // 🌐 Call API từ client
    const response = await fetch(`/api/posts/${postId}/like`, { method: 'POST' });
    const data = await response.json();
    
    setLikes(data.likes);
    setIsLiked(true);
  };

  return (
    <button onClick={handleLike} disabled={isLiked}>
      {isLiked ? `❤️ ${likes}` : `🤍 ${likes}`}
    </button>
  );
}

/**
 * ⚠️ Khi nào dùng Client Component:
 * - Cần useState, useEffect, event handlers (onClick, onChange...)
 * - Cần browser APIs (localStorage, window, document...)
 * - Cần third-party libraries (charts, maps...)
 * 
 * 📊 Server vs Client Components:
 * 
 * Server Component:
 * - ✅ Fetch data trực tiếp
 * - ✅ Access database
 * - ✅ Zero client JS
 * - ❌ Không có interactivity
 * 
 * Client Component:
 * - ✅ Interactive (onClick, useState...)
 * - ✅ Browser APIs
 * - ❌ Tốn bundle size
 * - ❌ Không fetch trực tiếp DB
 */
```

---

## **2. So Sánh Next.js 14 vs 15 vs 16**

### **2.1. Next.js 14 (Tháng 10/2023)**

**🎯 Tính năng chính:**

```typescript
/**
 * ✅ Next.js 14 Highlights:
 * 
 * 1️⃣ Turbopack (Dev Server):
 * - Fast Refresh nhanh hơn 53%
 * - Cold start nhanh hơn 94%
 * - Thay thế Webpack (beta)
 * 
 * 2️⃣ Server Actions (Stable):
 * - Form submission không cần API route
 * - Progressive enhancement (work without JS)
 * 
 * 3️⃣ Partial Prerendering (Preview):
 * - Static + Dynamic trong cùng 1 page
 * - Stream dynamic parts
 */

// 1️⃣ Server Actions - Submit form trực tiếp
// app/login/page.tsx
export default function LoginPage() {
  // ✅ Server Action - function chạy trên server
  async function loginAction(formData: FormData) {
    'use server'; // 👉 Đánh dấu đây là Server Action
    
    const email = formData.get('email');
    const password = formData.get('password');
    
    // Authenticate user trực tiếp trên server
    const user = await authenticate(email, password);
    
    if (user) {
      redirect('/dashboard'); // Chuyển trang
    } else {
      return { error: 'Sai email hoặc mật khẩu' };
    }
  }

  return (
    <form action={loginAction}> {/* Form gọi Server Action */}
      <input name="email" type="email" placeholder="Email" />
      <input name="password" type="password" placeholder="Mật khẩu" />
      <button type="submit">Đăng nhập</button>
    </form>
  );
  // 👉 Không cần API route /api/login
  // 👉 Form vẫn work khi JavaScript bị tắt (progressive enhancement)
}

// 2️⃣ Turbopack Dev Server
// next.config.js
module.exports = {
  experimental: {
    turbo: true // ✅ Enable Turbopack (beta)
  }
};

// 3️⃣ Metadata API
// app/blog/[slug]/page.tsx
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug);
  
  return {
    title: post.title, // <title>...</title>
    description: post.excerpt, // <meta name="description">
    openGraph: {
      images: [post.coverImage], // <meta property="og:image">
    }
  };
}
```

**📊 Performance:**

```typescript
/**
 * Next.js 14 Benchmark:
 * 
 * Dev Server (Turbopack):
 * - Cold start: 700ms → 53ms (94% faster)
 * - Fast Refresh: 200ms → 100ms (53% faster)
 * 
 * Production Build:
 * - Server Components: Zero client JS
 * - Image Optimization: Auto WebP/AVIF
 * - Font Optimization: Auto self-host fonts
 */
```

---

### **2.2. Next.js 15 (Tháng 10/2024)**

**🚀 Breaking Changes & New Features:**

```typescript
/**
 * ✅ Next.js 15 Highlights:
 * 
 * 1️⃣ React 19 Support:
 * - use() hook
 * - useOptimistic
 * - useActionState
 * 
 * 2️⃣ Async Request APIs:
 * - cookies() async
 * - headers() async
 * - params async
 * 
 * 3️⃣ Caching Changes:
 * - fetch() no longer cached by default
 * - GET route handlers no longer cached
 */

// 1️⃣ Async Request APIs (Breaking Change!)
// ❌ Next.js 14:
export default function Page({ params }) {
  const { id } = params; // Sync
  const cookieStore = cookies(); // Sync
}

// ✅ Next.js 15:
export default async function Page({ params }) {
  const { id } = await params; // 👉 Phải await params
  const cookieStore = await cookies(); // 👉 Phải await cookies
  const headersList = await headers(); // 👉 Phải await headers
  
  const token = cookieStore.get('token');
  const userAgent = headersList.get('user-agent');
  
  return <div>User ID: {id}</div>;
}

/**
 * 💡 Tại sao async?
 * - Chuẩn bị cho Partial Prerendering (PPR)
 * - Tránh block rendering khi đợi params/cookies
 * - Consistent với Server Components async nature
 */

// 2️⃣ Caching Changes (Breaking Change!)
// ❌ Next.js 14: fetch() cached by default
const data = await fetch('https://api.example.com/data');
// 👉 Response được cache vĩnh viễn

// ✅ Next.js 15: fetch() NOT cached by default
const data = await fetch('https://api.example.com/data');
// 👉 Mỗi request đều fetch mới

// Muốn cache trong Next.js 15:
const data = await fetch('https://api.example.com/data', {
  cache: 'force-cache' // 👉 Opt-in caching
});

// Hoặc dùng revalidate:
const data = await fetch('https://api.example.com/data', {
  next: { revalidate: 60 } // Cache 60 giây
});

// 3️⃣ React 19 Features
import { use } from 'react';

export default function Comments({ commentsPromise }) {
  // ✅ use() hook - Read promise trong render
  const comments = use(commentsPromise);
  
  return comments.map(c => <p key={c.id}>{c.text}</p>);
}

// 4️⃣ Improved Error Messages
// Next.js 15 có error messages rõ ràng hơn:
/**
 * ❌ Next.js 14:
 * Error: Invalid hook call
 * 
 * ✅ Next.js 15:
 * Error: You're calling useState in a Server Component.
 * Add 'use client' at the top of this file to convert it to a Client Component.
 * 
 * File: app/components/Counter.tsx
 * Line: 5
 */
```

**📊 Migration Checklist (14 → 15):**

```typescript
/**
 * ✅ Migration Checklist:
 * 
 * 1. Update params to async:
 *    - await params trong page/layout
 *    - await searchParams trong page
 * 
 * 2. Update cookies/headers to async:
 *    - await cookies()
 *    - await headers()
 * 
 * 3. Review fetch() calls:
 *    - Thêm { cache: 'force-cache' } nếu cần cache
 *    - Thêm { next: { revalidate: X } } cho ISR
 * 
 * 4. Update to React 19:
 *    - npm install react@19 react-dom@19
 *    - Check breaking changes (PropTypes removed, StrictMode changes)
 * 
 * 5. Test thoroughly:
 *    - Test forms (Server Actions)
 *    - Test data fetching (cache behavior)
 *    - Test dynamic routes (params)
 */
```

---

### **2.3. Next.js 16 (Dự kiến 2025)**

**⚡ Expected Features (Dựa trên roadmap):**

```typescript
/**
 * 🔮 Next.js 16 Expected Features:
 * 
 * 1️⃣ Partial Prerendering (Stable):
 * - Mix static + dynamic trong cùng page
 * - Streaming dynamic parts
 * - Faster TTFB
 * 
 * 2️⃣ Improved Caching:
 * - Better cache invalidation
 * - Granular cache control
 * - Cache warming
 * 
 * 3️⃣ Turbopack (Stable):
 * - Replace Webpack hoàn toàn
 * - Faster builds
 * - Better tree-shaking
 * 
 * 4️⃣ Better Developer Experience:
 * - Improved error overlay
 * - Better TypeScript support
 * - Faster Hot Module Replacement (HMR)
 */

// 1️⃣ Partial Prerendering (PPR) Example
export default async function ProductPage({ params }) {
  const { id } = await params;
  
  // ✅ Static part - Pre-render at build time
  const product = await getProduct(id);
  
  return (
    <div>
      {/* Static content */}
      <h1>{product.name}</h1>
      <img src={product.image} alt={product.name} />
      
      {/* Dynamic part - Stream on request */}
      <Suspense fallback={<p>Đang tải...</p>}>
        <ProductReviews productId={id} />
        <RecommendedProducts userId={getCurrentUserId()} />
      </Suspense>
    </div>
  );
}

/**
 * 📊 PPR Timeline:
 * 
 * Traditional SSR:
 * Request → Wait for ALL data → Send HTML (slow TTFB)
 * 
 * PPR:
 * Request → Send static HTML ngay → Stream dynamic parts
 * - TTFB: Instant (static shell)
 * - Dynamic parts: Stream khi ready
 * - User sees content nhanh hơn
 */

// 2️⃣ Improved Cache API (Potential)
// next.config.js
module.exports = {
  experimental: {
    cache: {
      type: 'redis', // Redis cache thay vì filesystem
      url: process.env.REDIS_URL,
      ttl: 3600 // Default TTL
    }
  }
};

// Manual cache control
import { revalidateTag } from 'next/cache';

// Fetch with tag
const data = await fetch('https://api.example.com/products', {
  next: { 
    tags: ['products'], // Tag để invalidate sau
    revalidate: 3600 
  }
});

// Invalidate khi có update
async function updateProduct(id: string, data: any) {
  await db.products.update(id, data);
  
  // ✅ Invalidate cache theo tag
  revalidateTag('products'); // Tất cả fetch có tag 'products' sẽ bị invalidate
}
```

---

## **3. Bảng So Sánh Chi Tiết**

```typescript
/**
 * ┌─────────────────────┬────────────────┬────────────────┬────────────────┐
 * │ Feature             │ Next.js 14     │ Next.js 15     │ Next.js 16     │
 * ├─────────────────────┼────────────────┼────────────────┼────────────────┤
 * │ React Version       │ 18.x           │ 19.x           │ 19.x+          │
 * │ App Router          │ ✅ Stable      │ ✅ Stable      │ ✅ Stable      │
 * │ Server Actions      │ ✅ Stable      │ ✅ Stable      │ ✅ Stable      │
 * │ Turbopack           │ ⚠️ Beta        │ ⚠️ Beta        │ ✅ Stable      │
 * │ Partial Prerender   │ ⚠️ Preview     │ ⚠️ Experimental│ ✅ Stable      │
 * │ params              │ Sync           │ Async          │ Async          │
 * │ cookies/headers     │ Sync           │ Async          │ Async          │
 * │ fetch() cache       │ Default ON     │ Default OFF    │ Default OFF    │
 * │ GET route cache     │ Default ON     │ Default OFF    │ Improved       │
 * │ Error Messages      │ Good           │ Better         │ Best           │
 * │ TypeScript          │ Good           │ Better         │ Best           │
 * │ Build Performance   │ Fast           │ Faster         │ Fastest        │
 * └─────────────────────┴────────────────┴────────────────┴────────────────┘
 * 
 * 🎯 Khi nào upgrade?
 * 
 * Next.js 14 → 15:
 * - ✅ Nếu muốn React 19 features (use, useOptimistic...)
 * - ✅ Nếu cần better error messages
 * - ⚠️ Phải migrate params/cookies/headers sang async
 * - ⚠️ Phải review fetch() caching behavior
 * 
 * Next.js 15 → 16:
 * - ✅ Nếu cần PPR (performance boost)
 * - ✅ Nếu cần Turbopack stable (faster builds)
 * - ✅ Nếu cần better caching control
 * - ⚠️ Đợi stable release trước
 */
```

---

## **4. Best Practices**

```typescript
/**
 * ✅ Next.js Best Practices:
 * 
 * 1️⃣ Routing:
 * - Dùng App Router (không phải Pages Router)
 * - Tổ chức folders theo features (app/blog, app/products...)
 * - Dùng route groups (app/(marketing), app/(dashboard))
 * 
 * 2️⃣ Components:
 * - Default Server Components (async, fetch trực tiếp)
 * - Chỉ dùng Client Components khi cần (useState, onClick...)
 * - Đặt 'use client' càng sát component interactive càng tốt
 * 
 * 3️⃣ Data Fetching:
 * - Fetch song song: Promise.all([fetch1, fetch2])
 * - Dùng Suspense cho streaming
 * - Cache với revalidate cho ISR
 * 
 * 4️⃣ Performance:
 * - Dùng Image component (next/image)
 * - Dùng Font optimization (next/font)
 * - Lazy load Client Components
 * - Enable Turbopack trong dev
 * 
 * 5️⃣ SEO:
 * - generateMetadata cho dynamic pages
 * - generateStaticParams cho SSG
 * - Sitemap + robots.txt
 */

// Example: Optimal Page Structure
export default async function ProductPage({ params }) {
  const { id } = await params;
  
  // ✅ Fetch song song (faster)
  const [product, reviews, recommendations] = await Promise.all([
    getProduct(id),
    getReviews(id),
    getRecommendations(id)
  ]);
  
  return (
    <div>
      {/* Server Component - No JS sent to client */}
      <ProductInfo product={product} />
      
      {/* Client Component - Only this part interactive */}
      <AddToCartButton productId={id} />
      
      {/* Streaming - Show fallback while loading */}
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews data={reviews} />
      </Suspense>
    </div>
  );
}
```

---

---

## **5. Hydration - Kích Hoạt Tương Tác**

### **5.1. Hydration Là Gì?**

```typescript
/**
 * 💧 Hydration (Thủy hóa):
 * 
 * Quá trình React "kích hoạt" HTML tĩnh từ server thành interactive React app.
 * 
 * 📊 Timeline:
 * 
 * 1️⃣ Server Render (SSR/SSG):
 *    - Server tạo HTML tĩnh: <button>Click me</button>
 *    - HTML không có event handlers
 *    - Gửi HTML + React payload xuống client
 * 
 * 2️⃣ Client Download:
 *    - Browser nhận HTML (hiển thị ngay - Fast FCP)
 *    - Download JavaScript bundles
 *    - Parse và execute React code
 * 
 * 3️⃣ Hydration Process:
 *    - React "đọc" HTML hiện có trên page
 *    - Attach event handlers: onClick, onChange...
 *    - Khởi tạo state: useState, useContext...
 *    - Component trở nên interactive (có thể click, type...)
 * 
 * ⚡ Kết quả:
 *    - HTML tĩnh → Interactive React app
 *    - User thấy UI ngay (HTML) nhưng phải đợi để tương tác (JS)
 */

// Example: Hydration Process
// 1️⃣ Server render (SSR)
export default function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Tăng
      </button>
    </div>
  );
}

/**
 * Server gửi HTML tĩnh:
 * <div>
 *   <p>Count: 0</p>
 *   <button>Tăng</button>  <!-- ❌ Không có onClick handler -->
 * </div>
 * 
 * 2️⃣ Client hydration:
 * - React parse component code
 * - useState(0) khởi tạo state
 * - onClick handler được attach vào button
 * 
 * 3️⃣ Sau hydration:
 * <button onclick="...">Tăng</button>  <!-- ✅ Có onClick handler, có thể click -->
 */
```

---

### **5.2. Hydration Mismatch - Lỗi Phổ Biến**

```typescript
/**
 * ⚠️ Hydration Mismatch:
 * 
 * Xảy ra khi HTML từ server KHÁC với HTML mà React render lần đầu trên client.
 * 
 * 🔴 Nguyên nhân phổ biến:
 * 1. Random data (Math.random(), Date.now())
 * 2. Browser-only APIs (window, document, localStorage)
 * 3. User-specific data không consistent
 * 4. CSS-in-JS libraries (styled-components)
 */

// ❌ WRONG: Hydration mismatch
export default function RandomNumber() {
  // Server render: <p>42</p>
  // Client hydration: <p>87</p>  ← Số khác nhau!
  const randomNum = Math.random() * 100; // ⚠️ Server và client khác nhau
  
  return <p>{randomNum}</p>;
}

// Console Error:
/**
 * ⚠️ Warning: Text content did not match. 
 * Server: "42" Client: "87"
 */

// ✅ FIX 1: Chỉ render trên client (useEffect)
'use client';

import { useState, useEffect } from 'react';

export default function RandomNumber() {
  const [randomNum, setRandomNum] = useState<number | null>(null);
  
  useEffect(() => {
    // ✅ Code này CHỈ chạy trên client (sau hydration)
    setRandomNum(Math.random() * 100);
  }, []);
  
  if (randomNum === null) {
    return <p>Đang tạo số ngẫu nhiên...</p>; // Server render + First client render
  }
  
  return <p>{randomNum}</p>; // Chỉ hiển thị sau hydration
}

// ✅ FIX 2: Suppress hydration warning (cho timestamp, user-specific data)
'use client';

export default function CurrentTime() {
  const now = new Date().toLocaleString();
  
  return (
    <time suppressHydrationWarning>
      {now} {/* ✅ Next.js bỏ qua mismatch cho element này */}
    </time>
  );
}

// ❌ WRONG: Dùng localStorage trước hydration
'use client';

export default function UserPreference() {
  // ⚠️ Server không có localStorage → crash hoặc mismatch
  const theme = localStorage.getItem('theme') || 'light';
  
  return <div className={theme}>Content</div>;
}

// ✅ FIX 3: Check browser environment
'use client';

import { useState, useEffect } from 'react';

export default function UserPreference() {
  const [theme, setTheme] = useState('light'); // Default value
  
  useEffect(() => {
    // ✅ Chỉ chạy trên client
    const savedTheme = localStorage.getItem('theme') || 'light';
    setTheme(savedTheme);
  }, []);
  
  return <div className={theme}>Content</div>;
}

/**
 * 💡 Quy tắc vàng tránh Hydration Mismatch:
 * 
 * 1. ✅ Đảm bảo server và client render GIỐNG NHAU lần đầu
 * 2. ✅ Dùng useEffect cho browser-only logic
 * 3. ✅ Dùng suppressHydrationWarning cho time/date
 * 4. ✅ Lazy load components có browser APIs
 * 5. ❌ Không dùng Math.random(), Date.now() trực tiếp trong JSX
 * 6. ❌ Không dùng window, localStorage trước hydration
 */
```

---

### **5.3. Progressive Hydration & Selective Hydration**

```typescript
/**
 * ⚡ Selective Hydration (React 18+):
 * 
 * React tự động ưu tiên hydrate các phần user đang tương tác.
 * Không cần đợi toàn bộ page hydrate xong.
 */

// Example: Selective Hydration với Suspense
export default function BlogPost() {
  return (
    <div>
      {/* ✅ Header hydrate ngay (không có Suspense) */}
      <Header />
      
      <article>
        <h1>Tiêu đề bài viết</h1>
        <p>Nội dung chính...</p>
        
        {/* ⚡ Comments hydrate sau (wrapped trong Suspense) */}
        <Suspense fallback={<CommentsSkeleton />}>
          <Comments />
        </Suspense>
        
        {/* ⚡ Sidebar hydrate sau */}
        <Suspense fallback={<SidebarSkeleton />}>
          <Sidebar />
        </Suspense>
      </article>
    </div>
  );
}

/**
 * 📊 Hydration Timeline:
 * 
 * Traditional Hydration (React 17):
 * 0s: HTML displayed
 * 3s: JS downloaded
 * 4s: Entire page hydrated  ← User phải đợi 4s mới tương tác được
 * 
 * Selective Hydration (React 18):
 * 0s: HTML displayed
 * 3s: JS downloaded
 * 3.1s: Header hydrated      ← User có thể click menu ngay
 * 3.5s: Article hydrated
 * 4s: Comments hydrated (lazy)
 * 4.5s: Sidebar hydrated (lazy)
 * 
 * 💡 Nếu user click Comments lúc 3.2s:
 * → React ưu tiên hydrate Comments trước Sidebar
 */

// ⚡ Lazy Hydration với next/dynamic
import dynamic from 'next/dynamic';

// ✅ Component này chỉ hydrate khi visible hoặc khi user tương tác
const HeavyChart = dynamic(() => import('@/components/HeavyChart'), {
  loading: () => <p>Đang tải biểu đồ...</p>,
  ssr: false // ❌ Không render trên server (chỉ client)
});

export default function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      
      {/* ⚡ Chart chỉ load khi scroll đến */}
      <HeavyChart />
    </div>
  );
}

/**
 * 💡 Khi nào dùng Lazy Hydration:
 * 
 * ✅ Heavy components (charts, maps, editors)
 * ✅ Below-the-fold content (nội dung phải scroll mới thấy)
 * ✅ Third-party widgets (chat, analytics)
 * ✅ Mobile optimization (tiết kiệm JS bundle)
 * 
 * ⚠️ Trade-offs:
 * - ✅ Faster initial hydration
 * - ✅ Less JS to parse
 * - ❌ Delay khi user tương tác (nếu chưa load)
 * - ❌ No SEO cho ssr: false
 */
```

---

## **6. "use server" vs "use client" - Chiến Lược Tối Ưu**

### **6.1. Quy Tắc Vàng**

```typescript
/**
 * 🎯 Default Strategy: Server Components
 * 
 * ✅ Mọi component MẶC ĐỊNH là Server Component (trong App Router)
 * ✅ Chỉ dùng "use client" khi THẬT SỰ cần
 * ✅ Đặt "use client" boundary càng sát component interactive càng tốt
 * 
 * 📊 Decision Tree:
 * 
 * Component cần gì?
 *   ├─ Fetch data từ database? → ✅ Server Component
 *   ├─ Access environment variables (secrets)? → ✅ Server Component
 *   ├─ Use useState/useEffect? → ❌ Client Component
 *   ├─ Event handlers (onClick, onChange)? → ❌ Client Component
 *   ├─ Browser APIs (localStorage, window)? → ❌ Client Component
 *   └─ Third-party libraries (charts, editor)? → ❌ Client Component
 */
```

---

### **6.2. "use server" - Server Actions**

```typescript
/**
 * 🖥️ "use server":
 * 
 * Đánh dấu function chạy trên SERVER (không gửi code xuống client).
 * Dùng cho: Form submission, Data mutation, Authentication.
 * 
 * 💡 Ưu điểm:
 * - ✅ Code không lộ ra client (bảo mật)
 * - ✅ Access database trực tiếp
 * - ✅ Không tốn client bundle size
 * - ✅ Progressive enhancement (work without JS)
 * 
 * ⚠️ Nhược điểm:
 * - ❌ Không thể dùng browser APIs
 * - ❌ Phải serialize data (JSON)
 */

// Example 1: Server Action trong Server Component
// app/posts/new/page.tsx
export default function NewPostPage() {
  // ✅ Server Action - function này chạy trên server
  async function createPost(formData: FormData) {
    'use server'; // 👉 Đánh dấu Server Action
    
    const title = formData.get('title');
    const content = formData.get('content');
    
    // ✅ Access database trực tiếp (không cần API route)
    const post = await db.posts.create({
      data: { title, content }
    });
    
    // ✅ Redirect sau khi tạo xong
    redirect(`/posts/${post.id}`);
  }
  
  return (
    <form action={createPost}> {/* Form gọi Server Action */}
      <input name="title" placeholder="Tiêu đề" />
      <textarea name="content" placeholder="Nội dung" />
      <button type="submit">Tạo bài viết</button>
    </form>
  );
}

/**
 * 📊 Flow:
 * 1. User submit form
 * 2. Next.js gửi FormData lên server (POST request)
 * 3. createPost() chạy trên server
 * 4. Insert vào database
 * 5. Redirect về /posts/123
 * 
 * 👉 Không cần tạo API route /api/posts
 * 👉 Database credentials không lộ ra client
 */

// Example 2: Server Action trong separate file
// app/actions/posts.ts
'use server'; // 👉 Toàn bộ file này là Server Actions

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string;
  const content = formData.get('content') as string;
  
  const post = await db.posts.create({
    data: { title, content }
  });
  
  revalidatePath('/posts'); // ✅ Invalidate cache
  return { success: true, postId: post.id };
}

export async function deletePost(postId: string) {
  await db.posts.delete({ where: { id: postId } });
  revalidatePath('/posts');
}

// app/posts/new/page.tsx
import { createPost } from '@/app/actions/posts';

export default function NewPostPage() {
  return <form action={createPost}>...</form>;
}

// Example 3: Gọi Server Action từ Client Component
'use client';

import { createPost } from '@/app/actions/posts';
import { useState } from 'react';

export default function NewPostForm() {
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  async function handleSubmit(formData: FormData) {
    setIsSubmitting(true);
    
    // ✅ Gọi Server Action từ client
    const result = await createPost(formData);
    
    if (result.success) {
      alert('Tạo bài viết thành công!');
    }
    
    setIsSubmitting(false);
  }
  
  return (
    <form action={handleSubmit}>
      <input name="title" placeholder="Tiêu đề" />
      <textarea name="content" placeholder="Nội dung" />
      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Đang tạo...' : 'Tạo bài viết'}
      </button>
    </form>
  );
}

/**
 * 💡 Khi nào dùng "use server":
 * 
 * ✅ Form submissions (login, register, create, update, delete)
 * ✅ Data mutations (write to database)
 * ✅ Authentication (check credentials)
 * ✅ File uploads (xử lý file trên server)
 * ✅ Send emails, call external APIs với secrets
 * 
 * ❌ KHÔNG dùng cho:
 * - Fetch data để hiển thị (dùng Server Component thay vì)
 * - Client-side validation (dùng Client Component)
 * - Real-time features (dùng WebSocket/SSE)
 */
```

---

### **6.3. "use client" - Client Components**

```typescript
/**
 * 💻 "use client":
 * 
 * Đánh dấu component chạy trên CLIENT (browser).
 * Code component này sẽ được gửi xuống browser dưới dạng JavaScript bundle.
 * 
 * 💡 Ưu điểm:
 * - ✅ Interactive (useState, useEffect, onClick...)
 * - ✅ Access browser APIs (localStorage, window, navigator...)
 * - ✅ Third-party client libraries (charts, maps, editors...)
 * - ✅ CSS-in-JS (styled-components, emotion...)
 * 
 * ⚠️ Nhược điểm:
 * - ❌ Tốn client bundle size (code gửi xuống browser)
 * - ❌ Không thể access database trực tiếp
 * - ❌ Secrets có thể lộ ra browser (nếu không cẩn thận)
 * - ❌ SEO kém hơn (nếu data fetch từ client)
 */

// Example 1: Basic Client Component
'use client'; // 👉 Bắt buộc ở đầu file

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0); // ✅ useState chỉ dùng được trong Client Component
  
  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Tăng {/* ✅ onClick chỉ có trong Client Component */}
      </button>
    </div>
  );
}

// Example 2: Browser APIs
'use client';

import { useEffect, useState } from 'react';

export default function UserLocation() {
  const [location, setLocation] = useState<string | null>(null);
  
  useEffect(() => {
    // ✅ navigator.geolocation chỉ có trong browser
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(position => {
        setLocation(`${position.coords.latitude}, ${position.coords.longitude}`);
      });
    }
  }, []);
  
  return <p>Vị trí: {location || 'Đang lấy...'}</p>;
}

// Example 3: Third-party library (Chart.js)
'use client';

import { Line } from 'react-chartjs-2'; // ❌ Chart.js cần browser (Canvas API)

export default function SalesChart({ data }) {
  return (
    <div>
      <h2>Biểu đồ doanh thu</h2>
      <Line data={data} /> {/* ✅ Render chart trên client */}
    </div>
  );
}

/**
 * 💡 Khi nào dùng "use client":
 * 
 * ✅ useState, useEffect, useReducer, useContext
 * ✅ Event handlers (onClick, onChange, onSubmit...)
 * ✅ Browser APIs (localStorage, sessionStorage, window, document...)
 * ✅ Third-party client libraries:
 *    - Charts (Chart.js, Recharts)
 *    - Maps (Leaflet, Mapbox)
 *    - Editors (TinyMCE, Draft.js)
 *    - Animation (Framer Motion)
 * ✅ CSS-in-JS (styled-components, emotion)
 * ✅ Client-side routing (useRouter, usePathname)
 * 
 * ❌ KHÔNG dùng khi:
 * - Chỉ cần render static content
 * - Fetch data từ database (dùng Server Component)
 * - SEO quan trọng (dùng Server Component)
 */
```

---

### **6.4. Chiến Lược Tối Ưu - Component Composition**

```typescript
/**
 * 🎯 Strategy: Đặt "use client" boundary càng nhỏ càng tốt
 * 
 * ❌ WRONG: Entire page là Client Component
 * ✅ RIGHT: Chỉ phần interactive là Client Component
 */

// ❌ WRONG: Entire page là Client Component
'use client';

export default async function ProductPage({ params }) {
  const product = await getProduct(params.id); // ⚠️ Fetch trên client (slow, không an toàn)
  const [quantity, setQuantity] = useState(1);
  
  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      
      <input 
        type="number" 
        value={quantity}
        onChange={e => setQuantity(Number(e.target.value))}
      />
      <button>Thêm vào giỏ</button>
    </div>
  );
}

/**
 * ⚠️ Vấn đề:
 * - Toàn bộ page code gửi xuống client (large bundle)
 * - Fetch data từ client (slow, latency cao)
 * - Database credentials có thể lộ
 */

// ✅ RIGHT: Split thành Server + Client Components
// app/products/[id]/page.tsx (Server Component - DEFAULT)
import AddToCartButton from '@/components/AddToCartButton';

export default async function ProductPage({ params }) {
  // ✅ Fetch trên server (fast, secure)
  const product = await getProduct(params.id);
  
  return (
    <div>
      {/* ✅ Static content - Server Component */}
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <img src={product.image} alt={product.name} />
      
      {/* ✅ Interactive part - Client Component */}
      <AddToCartButton productId={product.id} price={product.price} />
    </div>
  );
}

// components/AddToCartButton.tsx (Client Component)
'use client'; // 👉 Chỉ component này là Client

import { useState } from 'react';

export default function AddToCartButton({ productId, price }) {
  const [quantity, setQuantity] = useState(1);
  
  const handleAddToCart = async () => {
    await fetch('/api/cart', {
      method: 'POST',
      body: JSON.stringify({ productId, quantity })
    });
    alert('Đã thêm vào giỏ!');
  };
  
  return (
    <div>
      <input 
        type="number" 
        value={quantity}
        onChange={e => setQuantity(Number(e.target.value))}
      />
      <button onClick={handleAddToCart}>
        Thêm vào giỏ - {price * quantity} VNĐ
      </button>
    </div>
  );
}

/**
 * ✅ Ưu điểm:
 * - ProductPage: Server Component (0 client JS)
 * - AddToCartButton: Client Component (minimal JS)
 * - Fetch data trên server (fast, secure)
 * - Chỉ interactive part hydrate
 */

// ⚡ Advanced: Pass Server Component as children
// components/ClientWrapper.tsx (Client Component)
'use client';

import { useState } from 'react';

export default function ClientWrapper({ children }) {
  const [isOpen, setIsOpen] = useState(false);
  
  return (
    <div>
      <button onClick={() => setIsOpen(!isOpen)}>
        {isOpen ? 'Đóng' : 'Mở'}
      </button>
      
      {isOpen && children} {/* ✅ children là Server Component */}
    </div>
  );
}

// app/page.tsx (Server Component)
import ClientWrapper from '@/components/ClientWrapper';

export default async function Page() {
  const data = await fetchData(); // ✅ Fetch trên server
  
  return (
    <ClientWrapper>
      {/* ✅ Component này vẫn là Server Component */}
      <ExpensiveServerComponent data={data} />
    </ClientWrapper>
  );
}

/**
 * 💡 Magic:
 * - ClientWrapper là Client Component (có useState, onClick)
 * - ExpensiveServerComponent là Server Component (fetch trên server)
 * - Best of both worlds!
 */
```

---

### **6.5. Performance Comparison**

```typescript
/**
 * 📊 Bundle Size Comparison:
 * 
 * Scenario: Product page với chart
 * 
 * ❌ All Client Component:
 * ├─ React: 45 KB
 * ├─ Product page: 10 KB
 * ├─ Chart.js: 200 KB
 * └─ Total: 255 KB → User download 255 KB JS
 * 
 * ✅ Server + Client Components:
 * ├─ Product info: 0 KB (Server Component, HTML only)
 * ├─ Add to cart button: 5 KB (Small Client Component)
 * ├─ Chart (lazy loaded): 200 KB (only when needed)
 * └─ Total initial: 50 KB → User download 50 KB JS
 * 
 * 🚀 Performance gain: 80% reduction!
 */

// Example: Lazy load heavy Client Component
import dynamic from 'next/dynamic';

// ✅ Chart chỉ load khi cần
const SalesChart = dynamic(() => import('@/components/SalesChart'), {
  loading: () => <p>Đang tải biểu đồ...</p>,
  ssr: false // Client-only (không render trên server)
});

export default async function DashboardPage() {
  const stats = await getStats(); // ✅ Server fetch
  
  return (
    <div>
      {/* ✅ Server Component - 0 client JS */}
      <h1>Dashboard</h1>
      <p>Doanh thu: {stats.revenue} VNĐ</p>
      <p>Đơn hàng: {stats.orders}</p>
      
      {/* ⚡ Lazy load chart - chỉ load khi scroll đến */}
      <SalesChart data={stats.chartData} />
    </div>
  );
}

/**
 * 📊 Loading Timeline:
 * 0s: HTML displayed (stats hiển thị ngay)
 * 1s: User scrolls down
 * 1.5s: Chart JS downloaded
 * 2s: Chart rendered
 * 
 * 👉 Stats đã hiển thị từ 0s, không phải đợi Chart load!
 */
```

---

### **6.6. Decision Flowchart**

```typescript
/**
 * 🎯 Quyết định "use server" vs "use client":
 * 
 * START
 *   ↓
 * Component cần interactive? (useState, onClick...)
 *   ├─ NO → ✅ Server Component (default)
 *   │        - Fetch data trên server
 *   │        - 0 client JS
 *   │        - Better SEO
 *   │
 *   └─ YES → Cần browser APIs? (localStorage, window...)
 *            ├─ YES → ❌ Client Component ("use client")
 *            │         - useState, useEffect
 *            │         - Event handlers
 *            │
 *            └─ NO → Cần submit form?
 *                    ├─ YES → ✅ Server Action ("use server")
 *                    │         - Form submission
 *                    │         - Data mutation
 *                    │
 *                    └─ NO → Third-party library?
 *                            ├─ Browser-only → ❌ Client ("use client")
 *                            │                  - Charts, maps, editors
 *                            │
 *                            └─ Universal → ✅ Server Component
 *                                           - Markdown parser
 *                                           - Date formatter
 * 
 * 💡 Golden Rules:
 * 1. Default to Server Components
 * 2. Add "use client" only when needed
 * 3. Keep "use client" boundary small
 * 4. Pass Server Components as children to Client Components
 * 5. Lazy load heavy Client Components
 */

// Example: Hybrid page
export default async function BlogPost({ params }) {
  const post = await getPost(params.slug); // ✅ Server fetch
  const relatedPosts = await getRelatedPosts(post.id); // ✅ Server fetch
  
  return (
    <article>
      {/* ✅ Server Component - Static content */}
      <h1>{post.title}</h1>
      <time>{post.publishedAt}</time>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
      
      {/* ❌ Client Component - Like button (interactive) */}
      <LikeButton postId={post.id} initialLikes={post.likes} />
      
      {/* ✅ Server Component - Related posts */}
      <aside>
        <h2>Bài viết liên quan</h2>
        {relatedPosts.map(p => (
          <a key={p.id} href={`/blog/${p.slug}`}>{p.title}</a>
        ))}
      </aside>
      
      {/* ❌ Client Component - Comments (interactive + real-time) */}
      <CommentsSection postId={post.id} />
    </article>
  );
}

/**
 * 📊 Bundle Breakdown:
 * - BlogPost page: 0 KB (Server Component)
 * - LikeButton: 3 KB (Small Client Component)
 * - CommentsSection: 15 KB (Client Component with real-time)
 * - Total initial: 18 KB
 * 
 * ✅ Compare to all-client approach: 50 KB+
 * 🚀 64% bundle reduction!
 */
```

---

**💡 Remember:**
> "Default Server Components. Add 'use client' chỉ khi cần interactive. Keep client boundary nhỏ nhất. Hydration = HTML tĩnh → Interactive React app!" 🚀

