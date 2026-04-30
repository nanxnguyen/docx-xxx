# ⚡ Q31: Next.js Workflow & Version Comparison - Next.js 14 vs 15 vs 16

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Next.js workflow: File-based routing (App Router) → Rendering strategies (SSR/SSG/ISR) → Data fetching (Server Components) → Build optimization. Version evolution: v14 stable App Router, v15 React 19 + async APIs, v16 cache improvements."**

**🔑 Next.js Workflow - 5 Bước:**

**1. Routing - File-Based (App Router):**

- `app/page.tsx` = homepage `/`
- `app/blog/[slug]/page.tsx` = dynamic route `/blog/my-post`
- `layout.tsx` = shared UI wrapper (persist across pages)
- Route groups `(marketing)` không ảnh hưởng URL

**2. Rendering Strategies:**

- **SSR** (Server-Side Rendering): Render mỗi request, fresh data
- **SSG** (Static Site Generation): Pre-render build time, fast CDN
- **ISR** (Incremental Static Regeneration): SSG + revalidate background
- **CSR** (Client-Side): Fetch data client-side (use client components)

**3. Data Fetching:**

- **Server Components** (default): `async` components fetch trên server
- `fetch()` auto-cached, `revalidate` option cho ISR
- **Client Components** (`'use client'`): dùng React Query, SWR, useEffect

**4. Build & Deploy:**

- `next build` → static HTML + optimized bundles
- Vercel (zero-config), Docker, Node.js server
- Edge Runtime cho ultra-low latency

**5. Performance Optimizations:**

- Automatic code splitting (per route)
- Image optimization (`<Image />`), Font optimization
- Route prefetching (`<Link />`)

**🔑 Version Comparison:**

| **Feature**     | **Next.js 14**                          | **Next.js 15**                                                 | **Next.js 16**                              |
| --------------- | --------------------------------------- | -------------------------------------------------------------- | ------------------------------------------- |
| **React**       | React 18                                | **React 19**                                                   | React 19                                    |
| **App Router**  | Stable                                  | Enhanced                                                       | Optimized                                   |
| **Key Feature** | Turbopack (beta), Server Actions stable | **Async Request APIs** (cookies/headers), Partial Prerendering | **Cache behavior changes**, DX improvements |
| **Breaking**    | -                                       | `cookies()/headers()` giờ **async**                            | Default caching strategies changed          |

**⚠️ Lỗi Thường Gặp:**

- Dùng `'use client'` không cần thiết → mất Server Component benefits (bundle size tăng)
- Fetch data trong Client Components mà không cache → waterfall, chậm
- Quên `revalidate` cho ISR → data stale mãi mãi
- Mix Pages Router và App Router không hiểu middleware scope

**💡 Kiến Thức Senior:**

- **Server vs Client Components**: Server = zero JS to client, Client = interactivity (onClick, useState)
- **Partial Prerendering** (v15): Combine static + dynamic trong cùng route (static shell + dynamic content)
- **Turbopack** (v14+): Rust-based bundler nhanh hơn Webpack (~700x dev mode)
- **Streaming SSR**: `<Suspense>` cho progressive rendering, TTFB nhanh hơn
- **Middleware**: Chạy Edge Runtime, dùng cho auth, redirects, A/B testing

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
// Layout gốc này sẽ bao bọc tất cả các trang trong ứng dụng
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  // children: nội dung của từng trang cụ thể sẽ được truyền vào đây
  return (
    <html lang="vi">
      <body>
        <header>Logo + Menu</header>{' '}
        {/* Header chung cho tất cả pages - luôn hiển thị */}
        {children} {/* Nội dung page cụ thể - thay đổi theo từng trang */}
        <footer>Footer</footer> {/* Footer chung - luôn hiển thị */}
      </body>
    </html>
  );
}

// app/page.tsx - Homepage
// File này tự động tạo route "/" (trang chủ)
export default function HomePage() {
  return <h1>Trang chủ</h1>; // Hiển thị tại route "/" khi user truy cập domain gốc
}

// app/blog/[slug]/page.tsx - Dynamic Route (Route động)
// [slug] là dynamic segment - có thể là bất kỳ giá trị nào
// Ví dụ: /blog/my-post → slug = "my-post", /blog/hello-world → slug = "hello-world"
export default async function BlogPost({
  params,
}: {
  params: { slug: string };
}) {
  // params.slug = "my-post" khi URL là /blog/my-post
  // async function: component này chạy trên server, có thể fetch data trực tiếp
  const post = await getPostBySlug(params.slug); // Fetch data từ database - chạy trên server

  return (
    <article>
      <h1>{post.title}</h1> {/* Hiển thị tiêu đề bài viết */}
      <p>{post.content}</p> {/* Hiển thị nội dung bài viết */}
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
// export const dynamic: báo cho Next.js biết cách render trang này
export const dynamic = 'force-dynamic'; // Next.js 14+ - Bắt buộc render mỗi request (không cache)

export default async function DashboardPage() {
  // ⚡ Code này chạy MỖI REQUEST - mỗi lần user truy cập đều chạy lại
  // async function: cho phép dùng await để fetch data
  const user = await getCurrentUser(); // Fetch user từ session - lấy thông tin user hiện tại
  const notifications = await getNotifications(user.id); // Fetch notifications mới nhất - lấy thông báo

  return (
    <div>
      <h1>Xin chào, {user.name}!</h1> {/* Hiển thị tên user */}
      <p>Bạn có {notifications.length} thông báo mới</p> {/* Hiển thị số lượng thông báo */}
    </div>
  );
  // 📊 Timeline: Request → Server render → Send HTML → Client hydrate
  // Mỗi request đều render lại trên server, đảm bảo data luôn mới nhất
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
// SSG: Static Site Generation - Tạo HTML tĩnh lúc build, không render mỗi request
export default async function BlogPost({
  params,
}: {
  params: { slug: string };
}) {
  // ⚡ Code này chạy LÚC BUILD (npm run build) - chỉ chạy 1 lần khi build
  // Sau khi build xong, HTML đã được tạo sẵn, serve trực tiếp (rất nhanh)
  const post = await getPostBySlug(params.slug); // Query database - chỉ chạy lúc build

  return (
    <article>
      <h1>{post.title}</h1> {/* Tiêu đề bài viết */}
      <p>{post.content}</p> {/* Nội dung bài viết */}
    </article>
  );
  // 📊 Timeline: Build time → Generate HTML → Deploy → Serve tĩnh
  // HTML được tạo sẵn, không cần render lại mỗi request
}

// Tạo list các pages cần build
// Function này báo cho Next.js biết cần tạo bao nhiêu trang tĩnh
export async function generateStaticParams() {
  const posts = await getAllPosts(); // Lấy tất cả bài viết từ database

  // Trả về mảng các params - Next.js sẽ tạo HTML cho mỗi slug
  return posts.map((post) => ({
    slug: post.slug, // Next.js sẽ generate /blog/post-1, /blog/post-2... cho mỗi slug
  }));
  // Ví dụ: có 10 bài viết → Next.js tạo 10 file HTML tĩnh lúc build
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
// ISR: Incremental Static Regeneration - Kết hợp SSG + tự động cập nhật
export const revalidate = 60; // Revalidate mỗi 60 giây - sau 60s sẽ tạo HTML mới ở background

export default async function ProductPage({
  params,
}: {
  params: { id: string };
}) {
  // ⚡ Code này:
  // - Lúc build: Generate HTML tĩnh (giống SSG)
  // - Runtime: Serve static HTML (nhanh như SSG)
  // - Sau 60s: Regenerate HTML mới ở background (tự động cập nhật data)
  const product = await getProduct(params.id); // Lấy thông tin sản phẩm

  return (
    <div>
      <h1>{product.name}</h1> {/* Tên sản phẩm */}
      <p>Giá: {product.price} VNĐ</p> {/* Giá sản phẩm */}
      <p>Còn lại: {product.stock} sản phẩm</p> {/* Số lượng tồn kho */}
    </div>
  );
  // 📊 Timeline:
  // Request 1 (0s): Serve static HTML (old data) - trả HTML đã tạo sẵn
  // Request 2 (61s): Serve static HTML + Trigger regen background - vẫn trả HTML cũ, nhưng bắt đầu tạo HTML mới
  // Request 3 (62s): Serve NEW HTML (updated data) - trả HTML mới đã được cập nhật
}
```

---

### **1.4. Data Fetching (Lấy Dữ Liệu)**

**Server Components (Mặc định trong App Router):**

```typescript
// app/blog/page.tsx - Server Component
// Server Component: mặc định trong App Router, chạy trên server
export default async function BlogPage() {
  // ✅ Fetch TRỰC TIẾP trên server - không cần API route
  // async function: cho phép dùng await để fetch data
  const posts = await db.posts.findMany(); // Query database - truy vấn database trực tiếp
  // 👉 Không cần useEffect, không cần useState - chỉ cần async/await
  // 👉 Code này chạy trên SERVER, không gửi xuống client - bảo mật hơn
  // 👉 Database credentials KHÔNG lộ ra client - thông tin nhạy cảm an toàn

  return (
    <div>
      <h1>Danh sách bài viết</h1>
      {/* Duyệt qua mảng posts và render từng bài viết */}
      {posts.map((post) => (
        <article key={post.id}>
          {' '}
          {/* key: React cần để track các item */}
          <h2>{post.title}</h2> {/* Tiêu đề bài viết */}
          <p>{post.excerpt}</p> {/* Đoạn trích dẫn */}
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
'use client'; // 👉 Bắt buộc khai báo 'use client' ở đầu file - báo cho Next.js biết đây là Client Component

import { useState } from 'react'; // useState chỉ dùng được trong Client Component

export default function LikeButton({ postId }: { postId: string }) {
  // useState: quản lý state trên client (browser)
  const [likes, setLikes] = useState(0); // State lưu số lượt like, mặc định = 0
  const [isLiked, setIsLiked] = useState(false); // State kiểm tra user đã like chưa, mặc định = false

  // Hàm xử lý khi user click nút like
  const handleLike = async () => {
    // 🌐 Call API từ client - gửi request lên server
    const response = await fetch(`/api/posts/${postId}/like`, {
      method: 'POST',
    }); // POST request để like bài viết
    const data = await response.json(); // Parse JSON response

    setLikes(data.likes); // Cập nhật số lượt like mới
    setIsLiked(true); // Đánh dấu user đã like
  };

  return (
    <button onClick={handleLike} disabled={isLiked}>
      {/* onClick: event handler chỉ có trong Client Component */}
      {/* disabled: vô hiệu hóa nút nếu đã like */}
      {isLiked ? `❤️ ${likes}` : `🤍 ${likes}`}{' '}
      {/* Hiển thị icon và số lượt like */}
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
// Server Action: function chạy trên server, không cần tạo API route riêng
export default function LoginPage() {
  // ✅ Server Action - function chạy trên server
  // async function: có thể dùng await để xử lý bất đồng bộ
  async function loginAction(formData: FormData) {
    'use server'; // 👉 Đánh dấu đây là Server Action - bắt buộc phải có

    // FormData: object chứa dữ liệu từ form
    const email = formData.get('email'); // Lấy giá trị email từ form
    const password = formData.get('password'); // Lấy giá trị password từ form

    // Authenticate user trực tiếp trên server - không cần API route
    const user = await authenticate(email, password); // Xác thực user

    if (user) {
      redirect('/dashboard'); // Chuyển trang nếu đăng nhập thành công
    } else {
      return { error: 'Sai email hoặc mật khẩu' }; // Trả về lỗi nếu đăng nhập thất bại
    }
  }

  return (
    <form action={loginAction}>
      {' '}
      {/* Form gọi Server Action - action prop trỏ đến Server Action */}
      <input name="email" type="email" placeholder="Email" />{' '}
      {/* Input email */}
      <input name="password" type="password" placeholder="Mật khẩu" /> {/* Input password */}
      <button type="submit">Đăng nhập</button> {/* Nút submit form */}
    </form>
  );
  // 👉 Không cần API route /api/login - Server Action thay thế
  // 👉 Form vẫn work khi JavaScript bị tắt (progressive enhancement) - tăng tính khả dụng
}

// 2️⃣ Turbopack Dev Server
// next.config.js - File cấu hình Next.js
module.exports = {
  experimental: {
    // experimental: các tính năng thử nghiệm, có thể thay đổi trong tương lai
    turbo: true, // ✅ Enable Turbopack (beta) - bật Turbopack thay vì Webpack
    // Turbopack: bundler mới viết bằng Rust, nhanh hơn Webpack rất nhiều
  },
};

// 3️⃣ Metadata API
// app/blog/[slug]/page.tsx
// generateMetadata: function đặc biệt để tạo metadata cho SEO
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug); // Lấy thông tin bài viết

  return {
    title: post.title, // <title>...</title> - tiêu đề trang (hiển thị trên tab browser)
    description: post.excerpt, // <meta name="description"> - mô tả trang (dùng cho SEO)
    openGraph: {
      // OpenGraph: metadata cho Facebook, Twitter khi share link
      images: [post.coverImage], // <meta property="og:image"> - ảnh hiển thị khi share
    },
  };
  // Metadata này giúp SEO tốt hơn và hiển thị đẹp khi share link
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
// Breaking Change: thay đổi lớn, code cũ sẽ không hoạt động
// ❌ Next.js 14: params, cookies, headers là synchronous (đồng bộ)
export default function Page({ params }) {
  const { id } = params; // Sync - lấy trực tiếp, không cần await
  const cookieStore = cookies(); // Sync - gọi trực tiếp, không cần await
}

// ✅ Next.js 15: params, cookies, headers là asynchronous (bất đồng bộ)
export default async function Page({ params }) {
  // async function: bắt buộc phải có vì cần await
  const { id } = await params; // 👉 Phải await params - đợi params được resolve
  const cookieStore = await cookies(); // 👉 Phải await cookies - đợi cookies được resolve
  const headersList = await headers(); // 👉 Phải await headers - đợi headers được resolve

  // Sau khi await xong, mới có thể dùng các giá trị
  const token = cookieStore.get('token'); // Lấy token từ cookies
  const userAgent = headersList.get('user-agent'); // Lấy user-agent từ headers

  return <div>User ID: {id}</div>;
  {
    /* Hiển thị user ID */
  }
}

/**
 * 💡 Tại sao async?
 * - Chuẩn bị cho Partial Prerendering (PPR)
 * - Tránh block rendering khi đợi params/cookies
 * - Consistent với Server Components async nature
 */

// 2️⃣ Caching Changes (Breaking Change!)
// Caching: lưu trữ response để không phải fetch lại mỗi lần
// ❌ Next.js 14: fetch() cached by default - tự động cache
const data = await fetch('https://api.example.com/data');
// 👉 Response được cache vĩnh viễn - lần sau dùng lại data cũ, không fetch mới

// ✅ Next.js 15: fetch() NOT cached by default - không tự động cache
const data = await fetch('https://api.example.com/data');
// 👉 Mỗi request đều fetch mới - luôn lấy data mới nhất từ API

// Muốn cache trong Next.js 15: phải tự khai báo
const data = await fetch('https://api.example.com/data', {
  cache: 'force-cache', // 👉 Opt-in caching - bắt buộc cache, dùng data cũ nếu có
});

// Hoặc dùng revalidate: cache nhưng tự động cập nhật sau một khoảng thời gian
const data = await fetch('https://api.example.com/data', {
  next: { revalidate: 60 }, // Cache 60 giây - sau 60s sẽ fetch lại data mới
  // ISR: Incremental Static Regeneration - cập nhật dần dần
});

// 3️⃣ React 19 Features
// use() hook: hook mới trong React 19, đọc Promise/Context trong render
import { use } from 'react';

export default function Comments({ commentsPromise }) {
  // ✅ use() hook - Read promise trong render
  // commentsPromise: một Promise chứa danh sách comments
  const comments = use(commentsPromise); // use() sẽ đợi Promise resolve và trả về data
  // Không cần useEffect hay useState, chỉ cần use() hook

  return comments.map((c) => <p key={c.id}>{c.text}</p>); // Render danh sách comments
  // map(): duyệt qua mảng và render từng comment
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
      ttl: 3600, // Default TTL
    },
  },
};

// Manual cache control
import { revalidateTag } from 'next/cache';

// Fetch with tag
const data = await fetch('https://api.example.com/products', {
  next: {
    tags: ['products'], // Tag để invalidate sau
    revalidate: 3600,
  },
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
// Optimal: tối ưu - kết hợp Server và Client Components hiệu quả
export default async function ProductPage({ params }) {
  // async function: Server Component, có thể fetch data
  const { id } = await params; // Lấy product ID từ URL params

  // ✅ Fetch song song (faster) - fetch nhiều API cùng lúc
  // Promise.all(): đợi tất cả Promise resolve, nhanh hơn fetch tuần tự
  const [product, reviews, recommendations] = await Promise.all([
    getProduct(id), // Fetch thông tin sản phẩm
    getReviews(id), // Fetch đánh giá
    getRecommendations(id), // Fetch sản phẩm gợi ý
  ]);
  // Destructuring: lấy 3 giá trị từ mảng kết quả

  return (
    <div>
      {/* Server Component - No JS sent to client - không gửi JS xuống browser */}
      <ProductInfo product={product} /> {/* Component tĩnh, render trên server */}
      {/* Client Component - Only this part interactive - chỉ phần này interactive */}
      <AddToCartButton productId={id} /> {/* Component có onClick, useState */}
      {/* Streaming - Show fallback while loading - hiển thị skeleton trong lúc đợi */}
      <Suspense fallback={<ReviewsSkeleton />}>
        {/* Suspense: cho phép stream component này */}
        <Reviews data={reviews} /> {/* Component này có thể stream */}
      </Suspense>
    </div>
  );
  // Kết hợp Server Component (nhanh, SEO tốt) và Client Component (interactive)
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
// Hydration: quá trình React "kích hoạt" HTML tĩnh thành interactive app
// 1️⃣ Server render (SSR) - Render trên server trước
export default function Counter() {
  // useState: quản lý state, nhưng lúc này chưa hoạt động (chưa hydrate)
  const [count, setCount] = useState(0); // State ban đầu = 0

  return (
    <div>
      <p>Count: {count}</p> {/* Hiển thị số đếm */}
      <button onClick={() => setCount(count + 1)}>
        {/* onClick: chưa hoạt động lúc này, phải đợi hydration */}
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
// Hydration mismatch: HTML từ server khác với HTML React render trên client
export default function RandomNumber() {
  // Server render: <p>42</p> - server tạo số ngẫu nhiên = 42
  // Client hydration: <p>87</p>  ← Số khác nhau! - client tạo số ngẫu nhiên = 87
  const randomNum = Math.random() * 100; // ⚠️ Server và client khác nhau
  // Math.random() tạo số khác nhau mỗi lần chạy → server và client khác nhau

  return <p>{randomNum}</p>; // React phát hiện mismatch → warning/error
}

// Console Error:
/**
 * ⚠️ Warning: Text content did not match.
 * Server: "42" Client: "87"
 */

// ✅ FIX 1: Chỉ render trên client (useEffect)
('use client'); // Bắt buộc phải có vì dùng useState và useEffect

import { useState, useEffect } from 'react';

export default function RandomNumber() {
  // useState: quản lý state, null ban đầu (server và client đều render null)
  const [randomNum, setRandomNum] = useState<number | null>(null);

  // useEffect: chỉ chạy trên client, sau khi component đã mount (sau hydration)
  useEffect(() => {
    // ✅ Code này CHỈ chạy trên client (sau hydration)
    // []: dependency array rỗng = chỉ chạy 1 lần sau khi mount
    setRandomNum(Math.random() * 100); // Tạo số ngẫu nhiên trên client
  }, []);

  // Kiểm tra nếu chưa có số ngẫu nhiên (lúc server render và lần đầu client render)
  if (randomNum === null) {
    return <p>Đang tạo số ngẫu nhiên...</p>; // Server render + First client render - giống nhau
  }

  return <p>{randomNum}</p>; // Chỉ hiển thị sau hydration - khi useEffect đã chạy
}

// ✅ FIX 2: Suppress hydration warning (cho timestamp, user-specific data)
// suppressHydrationWarning: bỏ qua cảnh báo mismatch cho element này
('use client'); // Cần vì dùng Date (có thể khác nhau giữa server và client)

export default function CurrentTime() {
  const now = new Date().toLocaleString(); // Lấy thời gian hiện tại - server và client khác nhau

  return (
    <time suppressHydrationWarning>
      {/* suppressHydrationWarning: báo cho React biết bỏ qua mismatch */}
      {now} {/* ✅ Next.js bỏ qua mismatch cho element này - không warning */}
    </time>
  );
  // Dùng khi biết chắc server và client sẽ khác nhau (time, user-specific data)
}

// ❌ WRONG: Dùng localStorage trước hydration
// localStorage: chỉ có trong browser, không có trên server
('use client');

export default function UserPreference() {
  // ⚠️ Server không có localStorage → crash hoặc mismatch
  // Server render: localStorage không tồn tại → lỗi hoặc dùng giá trị mặc định
  // Client render: localStorage có → lấy giá trị từ storage
  const theme = localStorage.getItem('theme') || 'light'; // ⚠️ Server sẽ lỗi hoặc mismatch

  return <div className={theme}>Content</div>; // Server và client khác nhau → mismatch
}

// ✅ FIX 3: Check browser environment
// Dùng useEffect để đảm bảo chỉ chạy trên client
('use client');

import { useState, useEffect } from 'react';

export default function UserPreference() {
  // useState: state ban đầu = 'light' (server và client đều render 'light')
  const [theme, setTheme] = useState('light'); // Default value - giống nhau trên server và client

  // useEffect: chỉ chạy trên client, sau khi component mount
  useEffect(() => {
    // ✅ Chỉ chạy trên client - localStorage chỉ có trong browser
    const savedTheme = localStorage.getItem('theme') || 'light'; // Lấy theme từ localStorage
    setTheme(savedTheme); // Cập nhật theme sau khi lấy được từ localStorage
  }, []); // []: chỉ chạy 1 lần sau mount

  return <div className={theme}>Content</div>; // Server render 'light', client cập nhật sau
  // Server và client lần đầu render giống nhau → không mismatch
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
// Selective Hydration: React ưu tiên hydrate phần user đang tương tác
// Suspense: cho phép render fallback trong khi đợi component sẵn sàng
export default function BlogPost() {
  return (
    <div>
      {/* ✅ Header hydrate ngay (không có Suspense) - hydrate trước */}
      <Header /> {/* Component này hydrate ngay lập tức */}
      <article>
        <h1>Tiêu đề bài viết</h1> {/* Nội dung tĩnh, hydrate ngay */}
        <p>Nội dung chính...</p> {/* Nội dung tĩnh, hydrate ngay */}
        {/* ⚡ Comments hydrate sau (wrapped trong Suspense) - hydrate sau */}
        <Suspense fallback={<CommentsSkeleton />}>
          {/* Suspense: đợi Comments sẵn sàng, hiển thị skeleton trong lúc đợi */}
          <Comments /> {/* Component này hydrate sau, có thể stream */}
        </Suspense>
        {/* ⚡ Sidebar hydrate sau - hydrate sau */}
        <Suspense fallback={<SidebarSkeleton />}>
          {/* Suspense: đợi Sidebar sẵn sàng, hiển thị skeleton trong lúc đợi */}
          <Sidebar /> {/* Component này hydrate sau */}
        </Suspense>
      </article>
    </div>
  );
  // React sẽ hydrate Header trước, Comments và Sidebar sau
  // Nếu user click vào Comments, React sẽ ưu tiên hydrate Comments trước Sidebar
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
// dynamic: import component động, chỉ load khi cần
import dynamic from 'next/dynamic';

// ✅ Component này chỉ hydrate khi visible hoặc khi user tương tác
// dynamic(() => import(...)): code splitting - chỉ load code khi cần
const HeavyChart = dynamic(() => import('@/components/HeavyChart'), {
  // import(): dynamic import - chỉ load module khi component được render
  loading: () => <p>Đang tải biểu đồ...</p>, // Hiển thị trong lúc đợi load
  ssr: false, // ❌ Không render trên server (chỉ client) - chỉ chạy trên browser
  // ssr: false → không SEO, nhưng giảm bundle size ban đầu
});

export default function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1> {/* Render ngay */}
      {/* ⚡ Chart chỉ load khi scroll đến hoặc khi component được render */}
      <HeavyChart />{' '}
      {/* Component này chỉ load khi cần, giảm bundle size ban đầu */}
    </div>
  );
  // HeavyChart chỉ được load khi Dashboard render, không load ngay từ đầu
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
// Server Component: mặc định, không cần 'use client'
export default function NewPostPage() {
  // ✅ Server Action - function này chạy trên server
  // async function: có thể dùng await
  async function createPost(formData: FormData) {
    'use server'; // 👉 Đánh dấu Server Action - bắt buộc phải có

    // FormData: object chứa dữ liệu từ form
    const title = formData.get('title'); // Lấy title từ form
    const content = formData.get('content'); // Lấy content từ form

    // ✅ Access database trực tiếp (không cần API route)
    // db.posts.create(): tạo record mới trong database
    const post = await db.posts.create({
      data: { title, content }, // Dữ liệu để tạo post mới
    });

    // ✅ Redirect sau khi tạo xong - chuyển đến trang chi tiết post
    redirect(`/posts/${post.id}`); // redirect: function của Next.js
  }

  return (
    <form action={createPost}>
      {' '}
      {/* Form gọi Server Action - action prop trỏ đến Server Action */}
      <input name="title" placeholder="Tiêu đề" /> {/* Input title */}
      <textarea name="content" placeholder="Nội dung" /> {/* Textarea content */}
      <button type="submit">Tạo bài viết</button> {/* Nút submit */}
    </form>
  );
  // Khi user submit form, Next.js sẽ gọi createPost() trên server
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
('use server'); // 👉 Toàn bộ file này là Server Actions

export async function createPost(formData: FormData) {
  const title = formData.get('title') as string;
  const content = formData.get('content') as string;

  const post = await db.posts.create({
    data: { title, content },
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
('use client');

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
'use client'; // 👉 Bắt buộc ở đầu file - báo cho Next.js biết đây là Client Component

import { useState } from 'react'; // useState chỉ dùng được trong Client Component

export default function Counter() {
  // useState: quản lý state trên client (browser)
  // [count, setCount]: destructuring - count là giá trị, setCount là hàm để cập nhật
  const [count, setCount] = useState(0); // ✅ useState chỉ dùng được trong Client Component
  // 0: giá trị khởi tạo ban đầu

  return (
    <div>
      <p>Count: {count}</p> {/* Hiển thị số đếm hiện tại */}
      <button onClick={() => setCount(count + 1)}>
        {/* onClick: event handler chỉ có trong Client Component */}
        {/* () => setCount(count + 1): arrow function tăng count lên 1 */}
        Tăng {/* ✅ onClick chỉ có trong Client Component */}
      </button>
    </div>
  );
  // Component này chỉ hoạt động trên client, không render trên server
}

// Example 2: Browser APIs
// Browser APIs: các API chỉ có trong browser, không có trên server
('use client'); // Bắt buộc vì dùng browser APIs

import { useEffect, useState } from 'react';

export default function UserLocation() {
  // useState: quản lý state, null ban đầu (chưa có vị trí)
  const [location, setLocation] = useState<string | null>(null);
  // <string | null>: TypeScript type - có thể là string hoặc null

  // useEffect: chỉ chạy trên client, sau khi component mount
  useEffect(() => {
    // ✅ navigator.geolocation chỉ có trong browser - không có trên server
    if (navigator.geolocation) {
      // Kiểm tra browser có hỗ trợ geolocation không
      navigator.geolocation.getCurrentPosition((position) => {
        // getCurrentPosition: lấy vị trí hiện tại của user
        // position: object chứa thông tin vị trí
        setLocation(
          `${position.coords.latitude}, ${position.coords.longitude}`
        );
        // Cập nhật location với tọa độ latitude và longitude
      });
    }
  }, []); // []: chỉ chạy 1 lần sau mount

  return <p>Vị trí: {location || 'Đang lấy...'}</p>;
  // Hiển thị vị trí nếu có, hoặc "Đang lấy..." nếu chưa có
}

// Example 3: Third-party library (Chart.js)
('use client');

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
// Vấn đề: toàn bộ page là Client Component → bundle size lớn, không tối ưu
'use client'; // ⚠️ Toàn bộ page là Client Component

export default async function ProductPage({ params }) {
  // ⚠️ async function trong Client Component - không nên làm vậy
  const product = await getProduct(params.id); // ⚠️ Fetch trên client (slow, không an toàn)
  // Vấn đề: fetch trên client → chậm hơn, credentials có thể lộ

  const [quantity, setQuantity] = useState(1); // useState: cần Client Component

  return (
    <div>
      <h1>{product.name}</h1> {/* Hiển thị tên sản phẩm */}
      <p>{product.description}</p> {/* Hiển thị mô tả */}

      <input
        type="number"
        value={quantity} {/* Controlled input - giá trị từ state */}
        onChange={e => setQuantity(Number(e.target.value))} {/* Cập nhật state khi user nhập */}
      />
      <button>Thêm vào giỏ</button> {/* Nút thêm vào giỏ */}
    </div>
  );
  // ⚠️ Toàn bộ code này gửi xuống client → bundle size lớn
}

/**
 * ⚠️ Vấn đề:
 * - Toàn bộ page code gửi xuống client (large bundle)
 * - Fetch data từ client (slow, latency cao)
 * - Database credentials có thể lộ
 */

// ✅ RIGHT: Split thành Server + Client Components
// Tách thành Server Component (fetch data) + Client Component (interactive)
// app/products/[id]/page.tsx (Server Component - DEFAULT)
import AddToCartButton from '@/components/AddToCartButton'; // Import Client Component

export default async function ProductPage({ params }) {
  // ✅ Fetch trên server (fast, secure) - Server Component mặc định
  // async function: cho phép fetch data trên server
  const product = await getProduct(params.id); // Fetch trên server → nhanh, an toàn

  return (
    <div>
      {/* ✅ Static content - Server Component - không gửi JS xuống client */}
      <h1>{product.name}</h1> {/* Render trên server, gửi HTML xuống */}
      <p>{product.description}</p> {/* Render trên server */}
      <img src={product.image} alt={product.name} /> {/* Render trên server */}

      {/* ✅ Interactive part - Client Component - chỉ phần này interactive */}
      <AddToCartButton productId={product.id} price={product.price} />
      {/* Component này có 'use client', có useState, onClick */}
    </div>
  );
  // ✅ Chỉ AddToCartButton gửi JS xuống client, phần còn lại là HTML thuần
}

// components/AddToCartButton.tsx (Client Component)
'use client'; // 👉 Chỉ component này là Client - boundary nhỏ nhất

import { useState } from 'react'; // useState chỉ dùng được trong Client Component

export default function AddToCartButton({ productId, price }) {
  // Props: nhận productId và price từ Server Component
  const [quantity, setQuantity] = useState(1); // State quản lý số lượng, mặc định = 1

  // Hàm xử lý khi user click "Thêm vào giỏ"
  const handleAddToCart = async () => {
    // Gửi request lên API để thêm vào giỏ hàng
    await fetch('/api/cart', {
      method: 'POST', // POST request
      body: JSON.stringify({ productId, quantity }) // Gửi productId và quantity
    });
    alert('Đã thêm vào giỏ!'); // Thông báo thành công
  };

  return (
    <div>
      <input
        type="number"
        value={quantity} {/* Controlled input - giá trị từ state */}
        onChange={e => setQuantity(Number(e.target.value))} {/* Cập nhật quantity khi user nhập */}
      />
      <button onClick={handleAddToCart}>
        {/* onClick: event handler chỉ có trong Client Component */}
        Thêm vào giỏ - {price * quantity} VNĐ {/* Hiển thị tổng tiền */}
      </button>
    </div>
  );
  // ✅ Chỉ component này gửi JS xuống client, rất nhỏ gọn
}

/**
 * ✅ Ưu điểm:
 * - ProductPage: Server Component (0 client JS)
 * - AddToCartButton: Client Component (minimal JS)
 * - Fetch data trên server (fast, secure)
 * - Chỉ interactive part hydrate
 */

// ⚡ Advanced: Pass Server Component as children
// Pattern: Client Component có thể nhận Server Component làm children
// components/ClientWrapper.tsx (Client Component)
'use client'; // Client Component vì có useState và onClick

import { useState } from 'react';

export default function ClientWrapper({ children }) {
  // children: prop đặc biệt trong React, chứa nội dung bên trong component
  const [isOpen, setIsOpen] = useState(false); // State quản lý trạng thái mở/đóng

  return (
    <div>
      <button onClick={() => setIsOpen(!isOpen)}>
        {/* onClick: toggle isOpen - đổi từ true sang false và ngược lại */}
        {isOpen ? 'Đóng' : 'Mở'} {/* Hiển thị text tùy theo isOpen */}
      </button>

      {isOpen && children} {/* ✅ children là Server Component */}
      {/* Conditional rendering: chỉ render children khi isOpen = true */}
      {/* Magic: children có thể là Server Component, vẫn render trên server */}
    </div>
  );
  // ✅ ClientWrapper là Client (có interactivity), children là Server (fetch data)
}

// app/page.tsx (Server Component)
import ClientWrapper from '@/components/ClientWrapper'; // Import Client Component

export default async function Page() {
  // async function: Server Component, có thể fetch data
  const data = await fetchData(); // ✅ Fetch trên server - nhanh, an toàn

  return (
    <ClientWrapper>
      {/* ClientWrapper: Client Component (có useState, onClick) */}
      {/* ✅ Component này vẫn là Server Component - fetch trên server */}
      <ExpensiveServerComponent data={data} />
      {/* ExpensiveServerComponent: Server Component, nhận data từ server */}
      {/* Magic: Server Component làm children của Client Component vẫn render trên server */}
    </ClientWrapper>
  );
  // ✅ Best of both worlds: Client interactivity + Server data fetching
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
// Lazy load: chỉ load code khi cần, giảm bundle size ban đầu
import dynamic from 'next/dynamic'; // Import function để lazy load component

// ✅ Chart chỉ load khi cần - code splitting
// dynamic(() => import(...)): chỉ import module khi component được render
const SalesChart = dynamic(() => import('@/components/SalesChart'), {
  // import(): dynamic import - chỉ load khi cần
  loading: () => <p>Đang tải biểu đồ...</p>, // Hiển thị trong lúc đợi load
  ssr: false, // Client-only (không render trên server) - chỉ chạy trên browser
  // ssr: false → không SEO, nhưng giảm bundle size ban đầu
});

export default async function DashboardPage() {
  // async function: Server Component
  const stats = await getStats(); // ✅ Server fetch - lấy data trên server

  return (
    <div>
      {/* ✅ Server Component - 0 client JS - render trên server */}
      <h1>Dashboard</h1> {/* Render ngay */}
      <p>Doanh thu: {stats.revenue} VNĐ</p> {/* Hiển thị doanh thu */}
      <p>Đơn hàng: {stats.orders}</p> {/* Hiển thị số đơn hàng */}
      {/* ⚡ Lazy load chart - chỉ load khi scroll đến hoặc khi component render */}
      <SalesChart data={stats.chartData} />
      {/* Component này chỉ load khi cần, không load ngay từ đầu */}
    </div>
  );
  // ✅ Stats hiển thị ngay, Chart load sau → faster initial load
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
// Hybrid: kết hợp Server Components (static) và Client Components (interactive)
export default async function BlogPost({ params }) {
  // async function: Server Component, fetch data trên server
  const post = await getPost(params.slug); // ✅ Server fetch - lấy bài viết
  const relatedPosts = await getRelatedPosts(post.id); // ✅ Server fetch - lấy bài viết liên quan

  return (
    <article>
      {/* ✅ Server Component - Static content - render trên server, không gửi JS */}
      <h1>{post.title}</h1> {/* Tiêu đề bài viết */}
      <time>{post.publishedAt}</time> {/* Ngày đăng */}
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
      {/* dangerouslySetInnerHTML: render HTML từ string (cẩn thận với XSS) */}

      {/* ❌ Client Component - Like button (interactive) - có useState, onClick */}
      <LikeButton postId={post.id} initialLikes={post.likes} />
      {/* Component này có 'use client', gửi JS xuống client */}

      {/* ✅ Server Component - Related posts - render trên server */}
      <aside>
        <h2>Bài viết liên quan</h2>
        {/* map(): duyệt qua mảng và render từng bài viết */}
        {relatedPosts.map(p => (
          <a key={p.id} href={`/blog/${p.slug}`}>{p.title}</a>
          {/* key: React cần để track các item trong list */}
        ))}
      </aside>

      {/* ❌ Client Component - Comments (interactive + real-time) - có real-time updates */}
      <CommentsSection postId={post.id} />
      {/* Component này có 'use client', có thể có WebSocket/SSE cho real-time */}
    </article>
  );
  // ✅ Kết hợp tối ưu: Server Components cho content, Client Components cho interactivity
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

---

## 🔍 Giải thích Next.js Workflow & Version Comparison (mức Senior/Tech Lead, tiếng Việt)

### 1. Trả lời nhanh kiểu phỏng vấn (4–5 phút)

> **“Về workflow, với Next.js (App Router) mình đi theo pipeline: định nghĩa route/layout → chọn chiến lược render (SSR/SSG/ISR/CSR) cho từng trang → quyết định data fetching ở Server Components hay Client Components → cấu hình cache/revalidate → build & deploy (thường lên Vercel/Edge). Về version: 14 ổn định App Router + Server Actions + Turbopack dev; 15 chuyển các request APIs (cookies/headers/params) sang async và đổi default caching; 16 tập trung hoàn thiện Partial Prerendering, Turbopack build và caching ở mức hệ thống.”**

Ý là bạn không chỉ thuộc API, mà hiểu **dòng chảy từ request → render → data → cache → deploy**, và **cách các version thay đổi behavior** đó.

---

### 2. Next.js workflow – nói theo góc nhìn kiến trúc

**Bước 1 – Routing & Layout (thiết kế cây UI):**

- Dùng **App Router** (`app/`) với `layout.tsx`, `page.tsx`, route groups `(marketing)`, `(dashboard)`…
- Ở level kiến trúc, mình quyết định:
  - Layout nào dùng chung (header/footer/sidebar) và được **persist** khi chuyển route.
  - Chia app theo **feature segments** (marketing vs authenticated dashboard) để tách concerns.

**Bước 2 – Chọn chiến lược render per-route:**

- Với mỗi route, mình hỏi:
  - Trang này **SEO-critical** không?
  - Dữ liệu **thay đổi tần suất** thế nào (giây, phút, giờ, ngày)?
  - Có phụ thuộc **session/user hiện tại** không?
- Từ đó chọn:
  - **SSG** cho content tĩnh (blog/docs/landing) → build time + CDN.
  - **ISR** cho content bán-động (product, listing) → `revalidate`.
  - **SSR** cho trang phụ thuộc session, data real-time hoặc khó cache.
  - **CSR** cho trang private/dashboard, không cần SEO.

**Bước 3 – Data fetching & component boundary:**

- Default: **Server Components** cho phần hiển thị, data fetching gần DB/API.
- Chỉ đánh dấu `'use client'` ở những nơi cần:
  - `useState/useEffect`, event handlers, browser APIs, lib thuần client (charts, maps…).
- Tư duy: **island architecture** – page là server-rendered shell, gắn các "interactive island" nhỏ.

**Bước 4 – Cache, revalidate, streaming:**

- Quyết định **cache mode** cho từng loại request:
  - Config/danh mục: `force-cache`/`revalidate` dài.
  - Dữ liệu kinh doanh: `revalidate` ngắn hoặc `no-store`.
- Với App Router:
  - `fetch(..., { cache: 'force-cache' })`, `next: { revalidate: N, tags: [...] }`.
  - Dùng `revalidatePath`, `revalidateTag` trong Server Actions/route handlers sau mutation.
- Dùng **Suspense + streaming SSR** cho trang lớn: shell trả ngay, phần nặng được stream dần (reviews, charts…).

**Bước 5 – Build & Deploy:**

- `next build` sinh static assets + server bundle (hoặc edge bundle).
- Thường deploy lên **Vercel** để tận dụng:
  - Edge Runtime, serverless functions.
  - Built-in image/font optimization.
  - Analytics, logs, ISR infra.
- Hoặc Docker/Node server on-prem nếu yêu cầu hạ tầng riêng.

Khi phỏng vấn, bạn có thể mô tả như vậy để thể hiện **tư duy pipeline** từ code → runtime.

---

### 3. So sánh Next.js 14 vs 15 vs 16 – nói ngắn, tập trung behavior

**Next.js 14 – "App Router trưởng thành, Server Actions dùng được"**

- Điểm chính:
  - App Router đủ ổn để dùng production.
  - **Server Actions** stable → form/mutation không cần API routes riêng.
  - **Turbopack dev**: tăng tốc experience dev, nhưng build prod vẫn dùng Webpack.
  - Partial Prerendering mới ở mức preview.
- Góc nhìn kiến trúc:
  - Đây là version hợp lý để **bắt đầu migrate từ Pages → App Router**.
  - Có thể áp dụng Server Components + Actions với ít rủi ro.

**Next.js 15 – "Async request APIs, caching đổi default" (nơi hay dính bẫy)**

- Breaking chính:
  - `cookies()`, `headers()`, `params`… chuyển sang **async** trong App Router.
  - `fetch()` **không còn cache by default**; muốn cache phải **opt-in** (`cache: 'force-cache'` hoặc `revalidate`).
- Tác động thực tế:
  - Phải **sửa function signatures** sang async/await, đặc biệt trong layout/page.
  - Phải **rà lại tất cả các chỗ fetch** để không vô tình mất cache (tăng load backend, giảm performance).
- Thêm vào đó: support tốt hơn cho **React 19/Compiler**, error messages dễ debug hydration.

**Next.js 16 (dự kiến) – "Production Turbopack + PPR stable"**

- Mục tiêu chính:
  - **Turbopack cho build production**: build nhanh, tree-shaking tốt hơn, DX/CI cải thiện.
  - **Partial Prerendering stable**: shell tĩnh + vùng nội dung động stream → cải thiện TTFB nhưng vẫn flexible.
  - Caching/Edge Runtime mature hơn, phù hợp hệ thống lớn.
- Góc nhìn chiến lược:
  - 16 là bước củng cố idea: **ít JS client hơn, nhiều việc trên server hơn, streaming & cache mạnh hơn**.

Khi trả lời, bạn có thể gói gọn: **14: ổn định App Router + Actions, 15: thay đổi APIs & cache behavior, 16: hoàn thiện PPR/Turbopack & caching.**

---

### 4. Những lỗi & quyết định kiến trúc mà Senior/Lead cần nêu

- **Lạm dụng `'use client'`**:

  - Khiến toàn bộ subtree thành Client Component → bundle phình to, hydration chậm.
  - Cách sửa: đẩy logic render/data lên Server, chỉ để interactive island là client.

- **Không để ý cache/revalidate khi lên Next 15+**:

  - `fetch` default no-cache → backend ăn traffic nhiều, mất lợi ích ISR.
  - Cần có quy ước trong team: loại data nào cache bao lâu, tag/invalidation thế nào.

- **Mix Pages Router & App Router không rõ ranh giới**:

  - Middleware, headers, cookies có behavior khác nhau.
  - Quyết định rõ: hoặc giữ Pages cho legacy, hoặc dần chuyển toàn bộ sang App Router.

- **Không tận dụng streaming/Suspense** cho trang phức tạp:
  - Đợi đủ mọi data rồi mới trả HTML → TTFB chậm, UX kém.
  - Pattern tốt hơn: shell + skeleton trả trước, phần nặng stream dần.

Nếu bạn nêu được **các lỗi này + cách tổ chức team để tránh** (coding guideline, lint rule, review checklist), đó là điểm cộng lớn ở vai trò Lead.

---

### 5. Câu chốt để kết bài trả lời

> "Khi thiết kế với Next.js, mình luôn bắt đầu từ **flow tổng thể**: route/layout tree → chọn chiến lược render per-page → boundary Server/Client Components → chiến lược cache & revalidation → cuối cùng mới đến build & deploy. Về phiên bản, từ 14 đến 16 là hành trình đẩy mạnh App Router + Server Components, chuyển từ 'SPA with SSR' sang **server-centric, streaming-first framework**, nơi client chỉ nhận lượng JS tối thiểu cần thiết để tương tác. Vai trò của mình là **định nghĩa các guideline** để cả team dùng đúng SSR/SSG/ISR, cache và 'use client', tránh bẫy khi upgrade version."
