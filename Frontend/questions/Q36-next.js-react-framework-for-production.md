# ▲ Q36: Next.js - React Framework for Production




**🎯 Next.js là gì:**
- React framework for production với built-in routing, SSR, SSG, API routes
- Tối ưu performance, SEO, developer experience
- Zero-config, file-based routing, automatic code splitting

#### **📚 PHẦN 1: CORE FEATURES**

##### **1.1. Rendering Methods**

```typescript
// ══════════════════════════════════════════════════════════
// 1. SSR - Server-Side Rendering (mỗi request)
// ══════════════════════════════════════════════════════════
// Chạy trên server MỖI request → Fresh data, tốt cho SEO
export async function getServerSideProps(context) {
  const res = await fetch('https://api.example.com/data');
  const data = await res.json();
  
  return {
    props: { data }, // Passed to page component
  };
}

function Page({ data }) {
  return <div>{data.title}</div>;
}

// ✅ Khi nào dùng: Data thay đổi thường xuyên, cần real-time
// ⚠️ Nhược điểm: Slower TTFB (Time To First Byte), server load cao

// ══════════════════════════════════════════════════════════
// 2. SSG - Static Site Generation (build time)
// ══════════════════════════════════════════════════════════
// Generate HTML tại BUILD TIME → Serve static files (cực nhanh)
export async function getStaticProps() {
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();
  
  return {
    props: { posts },
    revalidate: 60, // ISR: Re-generate mỗi 60s nếu có request
  };
}

// Dynamic routes với SSG
export async function getStaticPaths() {
  const res = await fetch('https://api.example.com/posts');
  const posts = await res.json();
  
  const paths = posts.map(post => ({
    params: { id: post.id.toString() },
  }));
  
  return {
    paths, // Pre-render những paths này
    fallback: 'blocking', // 'blocking' | true | false
  };
}

// ✅ Khi nào dùng: Blog, docs, marketing pages (static content)
// ✅ Ưu điểm: Cực nhanh, CDN-friendly, tốt cho SEO

// ══════════════════════════════════════════════════════════
// 3. ISR - Incremental Static Regeneration
// ══════════════════════════════════════════════════════════
export async function getStaticProps() {
  const data = await fetchData();
  
  return {
    props: { data },
    revalidate: 10, // Re-generate page mỗi 10s (stale-while-revalidate)
  };
}

// Flow:
// 1. Request → Serve stale page (instant)
// 2. Background: Re-generate new page
// 3. Next request → Serve fresh page
// ✅ Best of both worlds: Static speed + Fresh data

// ══════════════════════════════════════════════════════════
// 4. CSR - Client-Side Rendering
// ══════════════════════════════════════════════════════════
import useSWR from 'swr';

function Profile() {
  const { data, error } = useSWR('/api/user', fetcher);
  
  if (error) return <div>Failed to load</div>;
  if (!data) return <div>Loading...</div>;
  
  return <div>Hello {data.name}</div>;
}

// ✅ Khi nào dùng: Private pages, dashboards, user-specific data
// ⚠️ Nhược điểm: Không tốt cho SEO, slower initial load
```

**📊 So sánh Rendering Methods:**

| Method | Build Time | Request Time | SEO | Speed | Use Case |
|--------|-----------|--------------|-----|-------|----------|
| **SSG** | Generate HTML | Serve static | ⭐⭐⭐ | ⭐⭐⭐ | Blog, docs |
| **ISR** | Generate HTML | Serve static + revalidate | ⭐⭐⭐ | ⭐⭐⭐ | E-commerce |
| **SSR** | - | Generate HTML | ⭐⭐⭐ | ⭐⭐ | Real-time data |
| **CSR** | - | Fetch on client | ⭐ | ⭐ | Dashboards |

---

##### **1.2. File-Based Routing**

```typescript
// pages/index.tsx → /
// pages/about.tsx → /about
// pages/blog/[slug].tsx → /blog/:slug (dynamic)
// pages/blog/[...slug].tsx → /blog/* (catch-all)
// pages/api/hello.ts → /api/hello (API route)

// Dynamic route example
// pages/posts/[id].tsx
import { useRouter } from 'next/router';

function Post() {
  const router = useRouter();
  const { id } = router.query; // Get dynamic param
  
  return <div>Post: {id}</div>;
}

// Catch-all route: pages/docs/[...slug].tsx
// Matches: /docs/a, /docs/a/b, /docs/a/b/c
function Docs() {
  const router = useRouter();
  const { slug } = router.query; // slug = ['a', 'b', 'c']
  
  return <div>Path: {slug?.join('/')}</div>;
}

// Programmatic navigation
const router = useRouter();
router.push('/about'); // Client-side navigation
router.push({ pathname: '/post/[id]', query: { id: '1' } });
router.replace('/login'); // Replace history
router.back(); // Go back
```

---

##### **1.3. API Routes**

```typescript
// pages/api/user.ts
import type { NextApiRequest, NextApiResponse } from 'next';

type Data = {
  name: string;
};

export default function handler(
  req: NextApiRequest,
  res: NextApiResponse<Data>
) {
  // Method-based routing
  if (req.method === 'POST') {
    // Handle POST
    const { name } = req.body;
    res.status(200).json({ name });
  } else {
    // Handle GET
    res.status(200).json({ name: 'John Doe' });
  }
}

// Dynamic API route: pages/api/posts/[id].ts
export default function handler(req, res) {
  const { id } = req.query;
  res.status(200).json({ post: id });
}

// ✅ Use cases: Backend logic, database queries, authentication
```

---

##### **1.4. Image Optimization**

```typescript
import Image from 'next/image';

// Automatic optimization, lazy loading, responsive
function Avatar() {
  return (
    <Image
      src="/me.png"
      alt="Picture"
      width={500}
      height={500}
      priority // Load eagerly (above fold)
      placeholder="blur" // Blur placeholder while loading
      blurDataURL="data:image/..." // Custom blur
    />
  );
}

// External images
<Image
  src="https://example.com/photo.jpg"
  alt="Photo"
  width={800}
  height={600}
  loader={({ src, width, quality }) => {
    return `${src}?w=${width}&q=${quality || 75}`;
  }}
/>

// ✅ Benefits:
// - Auto WebP/AVIF conversion
// - Lazy loading (viewport intersection)
// - Responsive images (srcset)
// - Prevent layout shift (width/height required)
```

---

#### **📚 PHẦN 2: ADVANCED FEATURES**

##### **2.1. Middleware (Next.js 12+)**

```typescript
// middleware.ts (root level)
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

// Chạy TRƯỚC request đến page/API
export function middleware(request: NextRequest) {
  // Authentication
  const token = request.cookies.get('token');
  
  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    return NextResponse.redirect(new URL('/login', request.url));
  }
  
  // A/B Testing
  const bucket = request.cookies.get('bucket') || Math.random() > 0.5 ? 'a' : 'b';
  const response = NextResponse.next();
  response.cookies.set('bucket', bucket);
  
  // Rewrite (thay đổi URL nội bộ)
  if (request.nextUrl.pathname === '/old-blog') {
    return NextResponse.rewrite(new URL('/blog', request.url));
  }
  
  return response;
}

// Chỉ chạy cho specific paths
export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'],
};
```

---

##### **2.2. App Router (Next.js 13+ - New)**

```typescript
// app/layout.tsx - Root layout
export default function RootLayout({ children }) {
  return (
    <html>
      <body>{children}</body>
    </html>
  );
}

// app/page.tsx - Home page (Server Component mặc định)
async function getData() {
  const res = await fetch('https://api.example.com/data');
  return res.json();
}

export default async function Page() {
  const data = await getData(); // Async component!
  return <div>{data.title}</div>;
}

// app/dashboard/layout.tsx - Nested layout
export default function DashboardLayout({ children }) {
  return (
    <div>
      <Sidebar />
      {children}
    </div>
  );
}

// Client component (when needed)
'use client'; // Directive

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
}
```

---

##### **2.3. Data Fetching (App Router)**

```typescript
// Fetch with caching
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'force-cache', // SSG-like (default)
  });
  return res.json();
}

// Revalidate every 10s (ISR)
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 10 },
  });
  return res.json();
}

// No caching (SSR-like)
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'no-store',
  });
  return res.json();
}

// Parallel data fetching
export default async function Page() {
  const [user, posts] = await Promise.all([
    fetch('/api/user').then(r => r.json()),
    fetch('/api/posts').then(r => r.json()),
  ]);
  
  return <div>{user.name} - {posts.length} posts</div>;
}
```

---

#### **📚 PHẦN 3: SEO OPTIMIZATION**

##### **3.1. Metadata & SEO**

```typescript
// pages/index.tsx (Pages Router)
import Head from 'next/head';

export default function Home() {
  return (
    <>
      <Head>
        <title>My Page Title</title>
        <meta name="description" content="Page description" />
        <meta property="og:title" content="OG Title" />
        <meta property="og:description" content="OG Description" />
        <meta property="og:image" content="https://example.com/og.jpg" />
        <meta name="twitter:card" content="summary_large_image" />
        <link rel="canonical" href="https://example.com" />
      </Head>
      <h1>Home</h1>
    </>
  );
}

// app/page.tsx (App Router) - Metadata API
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'My Page Title',
  description: 'Page description',
  openGraph: {
    title: 'OG Title',
    description: 'OG Description',
    images: [{ url: 'https://example.com/og.jpg' }],
  },
  twitter: {
    card: 'summary_large_image',
  },
};

// Dynamic metadata
export async function generateMetadata({ params }): Promise<Metadata> {
  const product = await fetch(`/api/products/${params.id}`).then(r => r.json());
  
  return {
    title: product.name,
    description: product.description,
    openGraph: {
      images: [product.image],
    },
  };
}
```

---

##### **3.2. SEO Best Practices**

```typescript
// 1. Sitemap Generation (pages/api/sitemap.xml.ts)
export default function Sitemap() {
  // Generate sitemap XML
}

// 2. robots.txt (public/robots.txt)
// User-agent: *
// Allow: /
// Sitemap: https://example.com/sitemap.xml

// 3. Structured Data (JSON-LD)
<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{
    __html: JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: 'Article Title',
      author: { '@type': 'Person', name: 'Author' },
    }),
  }}
/>

// 4. Image Alt Text
<Image src="/photo.jpg" alt="Descriptive alt text" width={500} height={500} />

// 5. Semantic HTML
<article>
  <h1>Title</h1>
  <p>Content</p>
</article>

// 6. Internal Linking
import Link from 'next/link';
<Link href="/about">About</Link> // Prefetch on hover
```

---

#### **📚 PHẦN 4: ƯU & NHƯỢC ĐIỂM**

**✅ Ưu điểm:**

1. **SEO Excellent**: SSR/SSG → Search engines index easily
2. **Performance**: Automatic code splitting, image optimization, font optimization
3. **Developer Experience**: Hot reload, TypeScript support, zero config
4. **Flexibility**: SSG, SSR, ISR, CSR - chọn per page
5. **Built-in Features**: Routing, API routes, image optimization, i18n
6. **Production Ready**: Vercel deployment, edge functions, analytics

**⚠️ Nhược điểm:**

1. **Learning Curve**: Nhiều concepts (SSR, SSG, ISR, hydration)
2. **Opinionated**: File-based routing, specific structure
3. **Build Time**: SSG với nhiều pages → long build time
4. **Server Costs**: SSR requires server (không thể pure static hosting)
5. **Vendor Lock-in**: Best với Vercel, other platforms cần config thêm
6. **Bundle Size**: Framework overhead (though optimized)

---

#### **📚 PHẦN 5: PERFORMANCE OPTIMIZATION**

```typescript
// 1. Dynamic Imports (Code Splitting)
import dynamic from 'next/dynamic';

const DynamicComponent = dynamic(() => import('../components/Heavy'), {
  loading: () => <p>Loading...</p>,
  ssr: false, // Disable SSR for this component
});

// 2. Font Optimization
import { Inter } from 'next/font/google';

const inter = Inter({ subsets: ['latin'] });

export default function App({ Component, pageProps }) {
  return (
    <main className={inter.className}>
      <Component {...pageProps} />
    </main>
  );
}

// 3. Script Optimization
import Script from 'next/script';

<Script
  src="https://analytics.com/script.js"
  strategy="lazyOnload" // afterInteractive | beforeInteractive | lazyOnload
/>

// 4. Streaming (App Router)
import { Suspense } from 'react';

export default function Page() {
  return (
    <Suspense fallback={<Loading />}>
      <SlowComponent />
    </Suspense>
  );
}
```

---

#### **📚 PHẦN 6: NEXT.JS 14 vs 15 vs 16 - SỰ KHÁC BIỆT**

##### **6.1. Next.js 14 (October 2023)**

**🎯 Key Features:**

```typescript
// 1. Turbopack (Beta) - Faster dev server
// next.config.js
module.exports = {
  experimental: {
    turbo: {}, // Opt-in Turbopack (5000+ tests passing)
  },
};

// 2. Server Actions (Stable)
// app/actions.ts
'use server';

export async function createPost(formData: FormData) {
  const title = formData.get('title');
  await db.posts.create({ title });
  revalidatePath('/posts');
}

// app/page.tsx
export default function Page() {
  return (
    <form action={createPost}>
      <input name="title" />
      <button type="submit">Create</button>
    </form>
  );
}

// 3. Partial Prerendering (Preview) - Hybrid SSR + Static
// Combines static shell + dynamic content
export const experimental_ppr = true; // Per-route

// 4. Metadata Improvements
export const metadata = {
  metadataBase: new URL('https://example.com'),
  alternates: {
    canonical: '/',
    languages: { 'en-US': '/en-US', 'vi-VN': '/vi-VN' },
  },
};
```

**📊 Next.js 14 Highlights:**
- ✅ Turbopack dev mode (53% faster)
- ✅ Server Actions stable
- ✅ Partial Prerendering preview
- ✅ Improved `next/image`

---

##### **6.2. Next.js 15 (October 2024)**

**🎯 Key Features:**

```typescript
// 1. React 19 Support
// - React Compiler (automatic memoization)
// - New hooks: useFormStatus, useOptimistic
// - Server Components improvements

// 2. Async Request APIs (Breaking Change)
// Before (Next 14): Synchronous
import { cookies, headers } from 'next/headers';
const cookieStore = cookies();

// After (Next 15): Async
const cookieStore = await cookies();
const headersList = await headers();

// 3. Caching Behavior Changes
// Next 14: fetch() cached by default
// Next 15: fetch() NOT cached by default (opt-in caching)

// Opt-in caching
fetch('https://api.example.com', { cache: 'force-cache' });

// 4. Turbopack Dev (Stable)
// No longer experimental, default in development
// next.config.js - Auto-enabled

// 5. Hydration Error Improvements
// Better error messages with source code context
// Automatic suggestions for common issues

// 6. Static Route Indicator
// Dev overlay shows which routes are static/dynamic
// <NextIndicator /> shows route type

// 7. Form Submissions
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();
  return <button disabled={pending}>Submit</button>;
}
```

**📊 Next.js 15 Highlights:**
- ✅ React 19 RC support
- ✅ Async request APIs (breaking)
- ✅ Caching opt-in (breaking)
- ✅ Turbopack stable in dev
- ✅ Better hydration errors
- ⚠️ Breaking changes from 14

---

##### **6.3. Next.js 16 (Expected Q1 2025)**

**🎯 Expected Features (Based on Roadmap):**

```typescript
// 1. Turbopack Build (Production)
// Currently dev-only, production builds will use Turbopack
// Faster builds, less memory usage

// 2. Partial Prerendering (Stable)
// pages/product/[id].tsx
export const experimental_ppr = true;

export default async function Product({ params }) {
  // Static shell renders immediately
  return (
    <div>
      <h1>Product {params.id}</h1>
      
      {/* Dynamic content loads after */}
      <Suspense fallback={<Skeleton />}>
        <ProductDetails id={params.id} />
      </Suspense>
      
      <Suspense fallback={<Skeleton />}>
        <Reviews id={params.id} />
      </Suspense>
    </div>
  );
}

// 3. Enhanced React Compiler Integration
// Auto-optimize components without manual memo/useCallback
function Component({ items }) {
  // Automatically optimized by React Compiler
  const filtered = items.filter(item => item.active);
  return <List items={filtered} />;
}

// 4. Improved Streaming
// Better support for streaming SSR
// Selective hydration improvements

// 5. Edge Runtime Enhancements
// More Node.js APIs available in Edge Runtime
// Better compatibility with existing packages
```

**📊 Next.js 16 Expected Features:**
- ✅ Turbopack production builds
- ✅ PPR stable (game-changer for performance)
- ✅ React Compiler default
- ✅ Better streaming & hydration
- ✅ Edge Runtime maturity

---

##### **6.4. Comparison Table: Next.js 14 vs 15 vs 16**

| Feature | Next.js 14 | Next.js 15 | Next.js 16 (Expected) |
|---------|-----------|-----------|---------------------|
| **React Version** | 18 | 19 RC | 19 Stable |
| **Turbopack Dev** | Beta | ✅ Stable | ✅ Stable |
| **Turbopack Build** | ❌ | ❌ | ✅ Stable |
| **Server Actions** | ✅ Stable | ✅ Stable | ✅ Enhanced |
| **PPR** | Preview | Experimental | ✅ Stable |
| **Request APIs** | Sync | ⚠️ Async (breaking) | Async |
| **Caching** | Default ON | ⚠️ Default OFF (breaking) | Opt-in |
| **React Compiler** | ❌ | Experimental | ✅ Default |
| **Hydration Errors** | Basic | ✅ Improved | Enhanced |
| **Edge Runtime** | Basic | Improved | ✅ Mature |

---

##### **6.5. Migration Guide: 14 → 15 → 16**

```typescript
// ══════════════════════════════════════════════════════════
// NEXT 14 → 15 (Breaking Changes)
// ══════════════════════════════════════════════════════════

// 1. Update async request APIs
// Before (14)
import { cookies } from 'next/headers';
const cookieStore = cookies();

// After (15)
const cookieStore = await cookies();

// 2. Update caching behavior
// Before (14) - cached by default
fetch('https://api.example.com');

// After (15) - opt-in caching
fetch('https://api.example.com', { cache: 'force-cache' });

// 3. Update next.config.js
// Remove experimental turbo flag (now default)
module.exports = {
  // experimental: { turbo: {} }, // Remove this
};

// ══════════════════════════════════════════════════════════
// NEXT 15 → 16 (Expected Changes)
// ══════════════════════════════════════════════════════════

// 1. Enable PPR for production
export const experimental_ppr = true; // Becomes stable

// 2. Remove manual optimizations (React Compiler handles)
// Before (15)
const memoized = useMemo(() => compute(data), [data]);
const callback = useCallback(() => handleClick(), []);

// After (16) - Compiler auto-optimizes
const memoized = compute(data); // Auto-memoized
const callback = () => handleClick(); // Auto-memoized

// 3. Turbopack production builds
// package.json
{
  "scripts": {
    "build": "next build" // Uses Turbopack automatically
  }
}
```

---

##### **6.6. Khi nào nên upgrade?**

**📌 Next.js 14:**
- ✅ Production-ready, stable
- ✅ Good for existing projects
- ✅ Server Actions stable
- ⚠️ Will need migration to 15 eventually

**📌 Next.js 15:**
- ✅ Latest stable (as of Oct 2024)
- ✅ React 19 RC support
- ✅ Better DX (Turbopack, hydration errors)
- ⚠️ Breaking changes from 14
- ⚠️ Caching behavior changes need attention

**📌 Next.js 16:**
- 🔮 Not released yet (Q1 2025)
- ✅ Wait for: PPR stable, Turbopack build, React Compiler
- ⚠️ Early adoption may have bugs

**💡 Recommendation:**
- **New projects**: Next.js 15 (latest stable)
- **Existing projects**: Stay on 14 until 15.1+ (bug fixes)
- **Enterprise**: Wait for 15.2+ or LTS versions

---

#### **🎯 TÓM TẮT Q40 - NEXT.JS**

**✅ Core Features:**
- **Rendering**: SSR, SSG, ISR, CSR - chọn per page
- **Routing**: File-based, dynamic routes, API routes
- **Optimization**: Image, font, script automatic optimization
- **SEO**: Built-in metadata API, sitemap, structured data

**💡 SEO Techniques:**
1. SSR/SSG cho better indexing
2. Metadata API (title, description, OG tags)
3. Structured data (JSON-LD)
4. Image optimization với alt text
5. Sitemap & robots.txt
6. Internal linking với Link component

**🚀 Khi nào dùng Next.js:**
- Cần SEO (blog, e-commerce, marketing)
- Performance-critical apps
- Full-stack React apps (API routes)
- Static sites với dynamic features

---
