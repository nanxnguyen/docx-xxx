# ▲ Q26: Next.js - React Framework for Production

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (2-3 phút):**

**"Next.js là framework React với SSR, SSG, routing và tối ưu hóa tích hợp sẵn.**

**📦 Phương Pháp Render Cốt Lõi (4 Loại):**

1. **SSR (Server-Side Rendering - Render Phía Server)**: Render HTML mỗi request → dữ liệu mới, SEO tốt. Dùng `getServerSideProps()`.

   - ✅ Trường hợp: Dashboard, trang cá nhân, dữ liệu thời gian thực.
   - ⚠️ Đánh đổi: TTFB chậm hơn, tải server cao.

2. **SSG (Static Site Generation - Tạo Trang Tĩnh)**: Render HTML lúc build → phục vụ file tĩnh (cực nhanh). Dùng `getStaticProps()`.

   - ✅ Trường hợp: Blog, tài liệu, trang marketing (nội dung ít thay đổi).
   - ✅ Lợi ích: Thân thiện CDN, hiệu năng tốt nhất, SEO tốt.

3. **ISR (Incremental Static Regeneration - Tạo Tĩnh Tăng Dần)**: SSG + tạo lại nền → mẫu stale-while-revalidate.

   - `revalidate: 60` → tạo lại trang mỗi 60s nếu có request.
   - ✅ Tốt nhất cả hai: Tốc độ tĩnh + dữ liệu mới.

4. **CSR (Client-Side Rendering - Render Phía Client)**: Lấy dữ liệu trên client (như SPA). Dùng `useSWR` hoặc React Query.
   - ✅ Trường hợp: Trang riêng tư, dashboard người dùng.
   - ⚠️ Đánh đổi: Không SEO, tải ban đầu chậm hơn.

**🗂️ App Router vs Pages Router:**

- **Pages Router (Cũ):**

  - Routing dựa trên file: `pages/about.tsx` → `/about`.
  - `getServerSideProps`, `getStaticProps` cho lấy dữ liệu.
  - Chỉ Client Components.

- **App Router (Next.js 13+):**
  - Dựa trên thư mục: `app/about/page.tsx` → `/about`.
  - Server Components mặc định → không có JS bundle.
  - Layouts, loading, error states tích hợp sẵn.
  - `async/await` trực tiếp trong components (không cần getServerSideProps).
  - Routing lồng nhau, parallel routes, intercepting routes.

**⚡ Server Components vs Client Components:**

- **Server Components**: Render trên server → không gửi JS tới client → tải nhanh hơn, SEO tốt hơn.

  - Mặc định trong App Router.
  - Không dùng được hooks (useState, useEffect), browser APIs.
  - ✅ Trường hợp: Nội dung tĩnh, lấy dữ liệu, trang SEO.

- **Client Components**: Chỉ thị `'use client'` → render trên client → tương tác được.
  - Dùng được hooks, browser APIs, event handlers.
  - ✅ Trường hợp: Form, giao diện tương tác, state client.

**🎯 Tính Năng Chính:**

- **Routing Dựa Trên File**: Không cần config, tự động chia code theo route.
- **Tối Ưu Hình Ảnh**: Component `<Image>` → tự động resize, lazy load, WebP.
- **API Routes**: `pages/api/` hoặc `app/api/` → serverless functions.
- **Middleware**: Chạy code trước khi request hoàn thành → auth, redirects, rewrites.
- **Chia Code Tự Động**: Chỉ tải JS cho trang hiện tại → tải nhanh hơn.

**⚠️ Lỗi Thường Gặp:**

- **Lấy dữ liệu trong useEffect (CSR) khi có thể dùng SSR/SSG**: Bỏ lỡ lợi ích SEO.
- **Không dùng `next/image`**: Bỏ lỡ tối ưu tự động (resize, lazy load, WebP).
- **Hardcode URLs**: Dùng `next/link` + `next/router` cho SPA navigation.
- **Không tối ưu fonts**: Dùng `next/font` cho tối ưu font tự động.

**💡 Kiến Thức Senior:**

- **Rendering Hỗn Hợp**: Kết hợp SSR + SSG + CSR trong cùng app → chọn phương pháp cho từng trang.
- **Edge Runtime**: Deploy middleware/API routes trên Edge → độ trễ thấp toàn cầu.
- **Streaming SSR**: React 18 + App Router → stream HTML chunks → TTFB nhanh hơn.
- **Partial Prerendering**: Next.js 14+ → vỏ tĩnh + nội dung động streamed.
- **Turbopack**: Next.js 13+ dev server → bundler dựa trên Rust → nhanh hơn Webpack 700 lần.

**🚀 Mẹo Hiệu Năng:**

- **Prefetching**: `<Link>` tự động prefetch khi hover → chuyển trang tức thì.
- **Import Động**: `next/dynamic` để chia code → tải components theo yêu cầu.
- **Caching**: `revalidate` cho ISR, headers `Cache-Control` cho API routes.
- **Phân Tích**: Báo cáo Web Vitals tích hợp → theo dõi hiệu năng người dùng thực.

---

**🎯 Next.js là gì:**

- React framework for production với built-in routing, SSR, SSG, API routes
- Tối ưu performance, SEO, developer experience
- Zero-config, file-based routing, automatic code splitting

#### **📚 PHẦN 1: CORE FEATURES**

##### **1.1. Rendering Methods**

```typescript
// ══════════════════════════════════════════════════════════
// 1. 🖥️ SSR - Server-Side Rendering (Render Phía Server - mỗi request)
// ══════════════════════════════════════════════════════════
// Chạy trên server MỖI request → Fresh data, tốt cho SEO
// 💡 SSR: Server render HTML mỗi request → Gửi HTML đầy đủ cho client
// 💡 Flow: Request → Server fetch data → Server render HTML → Gửi HTML → Client hydrate

export async function getServerSideProps(context) {
  // 💡 getServerSideProps: Function chạy trên server MỖI request
  // 💡 context: Object chứa request info (params, query, req, res...)
  // 💡 async: Có thể fetch data async

  const res = await fetch('https://api.example.com/data'); // 📡 Fetch data từ API
  // 💡 fetch: Gọi API để lấy data
  // 💡 await: Đợi response từ API

  const data = await res.json(); // 📦 Parse JSON response
  // 💡 res.json(): Convert response thành JavaScript object

  return {
    props: { data }, // 📤 Passed to page component
    // 💡 props: Data được truyền vào page component như props
    // 💡 Page component nhận props.data
  };
}

function Page({ data }) {
  // 💡 Page: Component nhận data từ getServerSideProps
  // 💡 data: Props từ getServerSideProps

  return <div>{data.title}</div>; // 📝 Render data
  // 💡 HTML được render trên server → Gửi xuống client đã có nội dung
  // 💡 SEO tốt: Search engine thấy nội dung ngay trong HTML
}

// ✅ Khi nào dùng: Data thay đổi thường xuyên, cần real-time
// 💡 Use cases: Dashboard, trang cá nhân, dữ liệu thời gian thực
// 💡 VD: Trang profile user → Data thay đổi theo user → Cần SSR

// ⚠️ Nhược điểm: Slower TTFB (Time To First Byte), server load cao
// 💡 TTFB: Thời gian từ request đến khi nhận byte đầu tiên
// 💡 SSR: Phải chờ server render → TTFB chậm hơn SSG
// 💡 Server load: Mỗi request đều render → Tốn CPU, memory

// ══════════════════════════════════════════════════════════
// 2. 📦 SSG - Static Site Generation (Tạo Trang Tĩnh - build time)
// ══════════════════════════════════════════════════════════
// Generate HTML tại BUILD TIME → Serve static files (cực nhanh)
// 💡 SSG: Render HTML lúc build → Lưu HTML tĩnh → Serve file tĩnh
// 💡 Flow: Build time → Fetch data → Render HTML → Lưu file → Deploy → Serve static
// 💡 Request: Chỉ serve file tĩnh → Cực nhanh (CDN), không tốn server CPU

export async function getStaticProps() {
  // 💡 getStaticProps: Function chạy CHỈ LÚC BUILD TIME
  // 💡 Không chạy mỗi request → Chỉ chạy khi build
  // 💡 Data được "đóng băng" tại thời điểm build

  const res = await fetch('https://api.example.com/posts'); // 📡 Fetch data lúc build
  // 💡 Fetch data từ API lúc build
  // 💡 Data này sẽ được dùng cho tất cả requests sau đó

  const posts = await res.json(); // 📦 Parse JSON

  return {
    props: { posts }, // 📤 Data cho page component
    revalidate: 60, // ⏰ ISR: Re-generate mỗi 60s nếu có request
    // 💡 revalidate: ISR (Incremental Static Regeneration)
    // 💡 60: Sau 60 giây, request tiếp theo sẽ trigger rebuild nền
    // 💡 Request hiện tại: Serve page cũ (stale) → Nhanh
    // 💡 Background: Rebuild page mới → Request sau: Serve page mới
  };
}

// 🔀 Dynamic routes với SSG (Routes động với SSG)
export async function getStaticPaths() {
  // 💡 getStaticPaths: Chỉ định các paths nào được pre-render
  // 💡 Cần cho dynamic routes: [id].tsx, [slug].tsx...
  // 💡 Next.js cần biết: Pre-render paths nào?

  const res = await fetch('https://api.example.com/posts'); // 📡 Fetch danh sách posts
  const posts = await res.json();

  const paths = posts.map((post) => ({
    params: { id: post.id.toString() }, // 🔑 Tạo params cho mỗi post
    // 💡 params: Object chứa dynamic route params
    // 💡 VD: { id: '1' } → Pre-render /posts/1
    // 💡 VD: { id: '2' } → Pre-render /posts/2
  }));

  return {
    paths, // 📋 Pre-render những paths này
    // 💡 paths: Array các paths sẽ được pre-render lúc build
    // 💡 VD: [{ params: { id: '1' } }, { params: { id: '2' } }]

    fallback: 'blocking', // 🔄 'blocking' | true | false
    // 💡 fallback: Xử lý paths không được pre-render
    // 💡 'blocking': Path mới → Server render on-demand → Block request
    // 💡 true: Path mới → Show loading → Render sau
    // 💡 false: Path mới → 404
  };
}

// ✅ Khi nào dùng: Blog, docs, marketing pages (static content)
// 💡 Use cases: Nội dung ít thay đổi, không cần real-time
// 💡 VD: Blog posts, documentation, landing pages, product catalogs

// ✅ Ưu điểm: Cực nhanh, CDN-friendly, tốt cho SEO
// 💡 Cực nhanh: Serve file tĩnh → Không tốn server CPU
// 💡 CDN-friendly: File tĩnh dễ cache trên CDN → Phục vụ từ edge
// 💡 SEO tốt: HTML đầy đủ ngay từ đầu → Search engine index dễ

// ══════════════════════════════════════════════════════════
// 3. 🔄 ISR - Incremental Static Regeneration (Tạo Tĩnh Tăng Dần)
// ══════════════════════════════════════════════════════════
// 💡 ISR: SSG + Revalidate → Kết hợp tốc độ tĩnh + dữ liệu mới
// 💡 Stale-while-revalidate pattern: Serve page cũ ngay → Rebuild nền → Serve page mới sau

export async function getStaticProps() {
  const data = await fetchData(); // 📡 Fetch data

  return {
    props: { data },
    revalidate: 10, // ⏰ Re-generate page mỗi 10s (stale-while-revalidate)
    // 💡 revalidate: Thời gian (giây) để trigger rebuild
    // 💡 10: Sau 10 giây, request tiếp theo sẽ trigger rebuild nền
    // 💡 Request hiện tại: Serve page cũ (stale) → Nhanh như SSG
    // 💡 Background: Rebuild page mới với data mới
    // 💡 Request sau: Serve page mới (fresh) → Data mới
  };
}

// 🔄 Flow (Quy trình hoạt động):
// 1. 📥 Request → Serve stale page (instant) - Nhanh như SSG
//    // 💡 Request đến → Serve page đã build sẵn (có thể cũ)
//    // 💡 Không cần chờ → Trả về ngay → TTFB nhanh
//
// 2. 🔄 Background: Re-generate new page - Rebuild nền
//    // 💡 Sau khi serve page cũ → Trigger rebuild nền
//    // 💡 Fetch data mới → Render HTML mới → Lưu lại
//    // 💡 Không block request hiện tại → User không chờ
//
// 3. 📤 Next request → Serve fresh page - Trang mới
//    // 💡 Request tiếp theo → Serve page mới đã rebuild
//    // 💡 Data mới → User thấy nội dung cập nhật
//
// ✅ Best of both worlds: Static speed + Fresh data
// 💡 Tốc độ: Nhanh như SSG (serve file tĩnh)
// 💡 Data: Mới như SSR (revalidate định kỳ)
// 💡 Use cases: E-commerce, blog với comments, content cập nhật thường xuyên

// ══════════════════════════════════════════════════════════
// 4. 💻 CSR - Client-Side Rendering (Render Phía Client)
// ══════════════════════════════════════════════════════════
// 💡 CSR: Render hoàn toàn trên client → Giống SPA truyền thống
// 💡 Flow: Server gửi HTML rỗng + JS → Client tải JS → Client fetch data → Client render

import useSWR from 'swr'; // 📦 useSWR: Hook để fetch data trên client

function Profile() {
  // 💡 Profile: Component render trên client
  // 💡 Không có getServerSideProps/getStaticProps → CSR

  const { data, error } = useSWR('/api/user', fetcher);
  // 💡 useSWR: Hook fetch data trên client
  // 💡 '/api/user': API endpoint để fetch user data
  // 💡 fetcher: Function để fetch data
  // 💡 data: Data từ API (null khi đang loading)
  // 💡 error: Error nếu fetch fail

  if (error) return <div>Failed to load</div>; // ❌ Hiển thị lỗi
  // 💡 error: Có lỗi khi fetch → Hiển thị error message

  if (!data) return <div>Loading...</div>; // ⏳ Hiển thị loading
  // 💡 !data: Chưa có data (đang loading) → Hiển thị loading state

  return <div>Hello {data.name}</div>; // ✅ Hiển thị data
  // 💡 data: Đã có data → Render nội dung
}

// ✅ Khi nào dùng: Private pages, dashboards, user-specific data
// 💡 Use cases: Trang không cần SEO, data riêng tư, dashboard
// 💡 VD: User dashboard, admin panel, private content

// ⚠️ Nhược điểm: Không tốt cho SEO, slower initial load
// 💡 SEO: HTML ban đầu rỗng → Search engine không thấy nội dung
// 💡 Initial load: Phải tải JS → Fetch data → Render → Chậm hơn SSR/SSG
```

**📊 So sánh Rendering Methods:**

| Method  | Build Time    | Request Time              | SEO    | Speed  | Use Case       |
| ------- | ------------- | ------------------------- | ------ | ------ | -------------- |
| **SSG** | Generate HTML | Serve static              | ⭐⭐⭐ | ⭐⭐⭐ | Blog, docs     |
| **ISR** | Generate HTML | Serve static + revalidate | ⭐⭐⭐ | ⭐⭐⭐ | E-commerce     |
| **SSR** | -             | Generate HTML             | ⭐⭐⭐ | ⭐⭐   | Real-time data |
| **CSR** | -             | Fetch on client           | ⭐     | ⭐     | Dashboards     |

---

##### **1.2. File-Based Routing (Routing Dựa Trên File)**

```typescript
// 📁 File-Based Routing: Cấu trúc file = cấu trúc routes
// 💡 Next.js tự động tạo routes dựa trên file structure
// 💡 Không cần config routing → Zero-config, convention over configuration

// 📄 pages/index.tsx → / (Home page)
// 💡 index.tsx: File đặc biệt → Route root (/)

// 📄 pages/about.tsx → /about
// 💡 about.tsx: File name = route path

// 📄 pages/blog/[slug].tsx → /blog/:slug (dynamic route)
// 💡 [slug]: Dynamic segment → Match bất kỳ giá trị nào
// 💡 VD: /blog/my-post, /blog/another-post

// 📄 pages/blog/[...slug].tsx → /blog/* (catch-all route)
// 💡 [...slug]: Catch-all → Match tất cả paths sau /blog/
// 💡 VD: /blog/a, /blog/a/b, /blog/a/b/c

// 📄 pages/api/hello.ts → /api/hello (API route)
// 💡 api/: API routes → Serverless functions
// 💡 Không render UI → Chỉ xử lý HTTP requests

// 🔀 Dynamic route example (Ví dụ route động)
// pages/posts/[id].tsx
import { useRouter } from 'next/router'; // 📦 Hook để access router

function Post() {
  const router = useRouter(); // 🔧 Lấy router object
  // 💡 useRouter: Hook để access routing info

  const { id } = router.query; // 🔑 Get dynamic param
  // 💡 router.query: Object chứa query params và dynamic params
  // 💡 { id }: Lấy giá trị của [id] từ URL
  // 💡 VD: /posts/123 → { id: '123' }

  return <div>Post: {id}</div>; // 📝 Render với dynamic param
}

// 🔀 Catch-all route: pages/docs/[...slug].tsx
// Matches: /docs/a, /docs/a/b, /docs/a/b/c
// 💡 [...slug]: Catch-all → Match nhiều segments
function Docs() {
  const router = useRouter();
  const { slug } = router.query; // 📋 slug = ['a', 'b', 'c']
  // 💡 slug: Array chứa tất cả segments
  // 💡 VD: /docs/a/b/c → slug = ['a', 'b', 'c']
  // 💡 VD: /docs/intro → slug = ['intro']

  return <div>Path: {slug?.join('/')}</div>; // 📝 Join array thành path
  // 💡 slug?.join('/'): Convert array thành string
  // 💡 VD: ['a', 'b', 'c'] → 'a/b/c'
}

// 🧭 Programmatic navigation (Điều hướng bằng code)
const router = useRouter();

router.push('/about'); // ➡️ Client-side navigation
// 💡 push: Navigate đến route mới (thêm vào history)
// 💡 Client-side: Không reload page → SPA navigation

router.push({ pathname: '/post/[id]', query: { id: '1' } });
// 💡 push với object: Navigate với dynamic route
// 💡 pathname: Route pattern với [id]
// 💡 query: Values cho dynamic params
// 💡 → Navigate đến /post/1

router.replace('/login'); // 🔄 Replace history
// 💡 replace: Navigate nhưng replace history entry
// 💡 Không thêm vào history → User không back được
// 💡 Use case: Redirect sau login → Không muốn user back về login page

router.back(); // ⬅️ Go back
// 💡 back: Quay lại trang trước (giống browser back button)
```

---

##### **1.3. API Routes (Routes API)**

```typescript
// 📡 API Routes: Serverless functions trong Next.js
// 💡 pages/api/ hoặc app/api/ → Tự động tạo API endpoints
// 💡 Không cần server riêng → Full-stack trong 1 app

// pages/api/user.ts
import type { NextApiRequest, NextApiResponse } from 'next';
// 💡 NextApiRequest: Type cho request object
// 💡 NextApiResponse: Type cho response object

type Data = {
  name: string; // 📦 Type cho response data
};

export default function handler(
  req: NextApiRequest, // 📥 Request object
  // 💡 req: Chứa request info (method, body, query, headers...)

  res: NextApiResponse<Data> // 📤 Response object
  // 💡 res: Dùng để gửi response (json, status, headers...)
) {
  // 🔀 Method-based routing (Routing dựa trên HTTP method)
  if (req.method === 'POST') {
    // ✅ Handle POST request
    const { name } = req.body; // 📦 Lấy data từ request body
    // 💡 req.body: Data từ client gửi lên (JSON, form data...)

    res.status(200).json({ name }); // 📤 Trả JSON response
    // 💡 status(200): Set HTTP status code (200 = OK)
    // 💡 json(): Gửi JSON response
  } else {
    // ✅ Handle GET request (hoặc methods khác)
    res.status(200).json({ name: 'John Doe' }); // 📤 Trả default data
  }
}

// 🔀 Dynamic API route: pages/api/posts/[id].ts
// 💡 [id]: Dynamic segment trong API route
// 💡 VD: /api/posts/123 → id = '123'
export default function handler(req, res) {
  const { id } = req.query; // 🔑 Get dynamic param từ query
  // 💡 req.query: Object chứa query params và dynamic params
  // 💡 { id }: Lấy giá trị của [id] từ URL

  res.status(200).json({ post: id }); // 📤 Trả response với id
}

// ✅ Use cases: Backend logic, database queries, authentication
// 💡 Backend logic: Xử lý business logic, validation...
// 💡 Database queries: Query database, CRUD operations
// 💡 Authentication: Login, register, token refresh...
// 💡 Webhooks: Nhận webhooks từ third-party services
// 💡 Proxy: Proxy requests đến external APIs
```

---

##### **1.4. Image Optimization**

```typescript
import Image from 'next/image'; // 📦 Next.js Image component
// 💡 Image: Component tối ưu hình ảnh tự động
// 💡 Thay thế <img> tag → Tự động optimize, lazy load, responsive

// 🖼️ Automatic optimization, lazy loading, responsive
function Avatar() {
  return (
    <Image
      src="/me.png" // 📁 Image path (local hoặc external)
      // 💡 src: Path đến image (từ public/ hoặc external URL)

      alt="Picture" // 📝 Alt text cho accessibility
      // 💡 alt: Mô tả image cho screen readers và SEO
      // 💡 ⚠️ Required: Luôn phải có alt text

      width={500} // 📏 Width của image (pixels)
      height={500} // 📏 Height của image (pixels)
      // 💡 width/height: Required để prevent layout shift
      // 💡 Next.js dùng để reserve space → Không bị jump khi load

      priority // ⚡ Load eagerly (above fold)
      // 💡 priority: Tải image ngay (không lazy load)
      // 💡 Dùng cho images above fold (hero, logo...) → LCP tốt hơn

      placeholder="blur" // 🌫️ Blur placeholder while loading
      // 💡 placeholder: Hiển thị placeholder khi đang load
      // 💡 'blur': Hiển thị blur version của image

      blurDataURL="data:image/..." // 🎨 Custom blur data URL
      // 💡 blurDataURL: Base64 encoded tiny image cho blur effect
      // 💡 Next.js tự generate nếu không có
    />
  );
}

// 🌐 External images (Hình ảnh từ domain khác)
<Image
  src="https://example.com/photo.jpg" // 🌐 External URL
  alt="Photo"
  width={800}
  height={600}
  loader={({ src, width, quality }) => {
    // 🔧 Custom loader cho external images
    // 💡 loader: Function để transform image URL
    // 💡 src: Original image URL
    // 💡 width: Desired width
    // 💡 quality: Image quality (1-100)

    return `${src}?w=${width}&q=${quality || 75}`;
    // 💡 Transform URL với query params
    // 💡 VD: https://example.com/photo.jpg?w=800&q=75
    // 💡 External service sẽ resize/optimize image
  }}
/>;
// 💡 ⚠️ Lưu ý: Cần config domains trong next.config.js cho external images

// ✅ Benefits (Lợi ích):
// - 🎨 Auto WebP/AVIF conversion
//    // 💡 Tự động convert sang format hiện đại (WebP, AVIF)
//    // 💡 Giảm kích thước file 30-50% → Load nhanh hơn
//
// - ⏳ Lazy loading (viewport intersection)
//    // 💡 Chỉ load image khi vào viewport
//    // 💡 Giảm initial page load → Faster FCP, LCP
//
// - 📱 Responsive images (srcset)
//    // 💡 Tự động tạo srcset với nhiều sizes
//    // 💡 Browser chọn size phù hợp với screen → Tối ưu bandwidth
//
// - 🎯 Prevent layout shift (width/height required)
//    // 💡 Reserve space trước khi load → Không bị jump
//    // 💡 Tốt cho CLS (Cumulative Layout Shift) score
```

---

#### **📚 PHẦN 2: ADVANCED FEATURES**

##### **2.1. Middleware (Next.js 12+)**

```typescript
// 🔧 middleware.ts (root level - File ở root của project)
// 💡 Middleware: Code chạy TRƯỚC request đến page/API
// 💡 Chạy trên Edge Runtime → Nhanh, gần user (low latency)
// 💡 Use cases: Auth, redirects, rewrites, A/B testing, logging...

import { NextResponse } from 'next/server'; // 📦 Response utilities
import type { NextRequest } from 'next/server'; // 📦 Request type

// 🔧 Chạy TRƯỚC request đến page/API
export function middleware(request: NextRequest) {
  // 💡 middleware: Function chạy cho mỗi request (nếu match matcher)
  // 💡 request: Request object chứa URL, cookies, headers...

  // 🔐 Authentication (Xác thực)
  const token = request.cookies.get('token'); // 🍪 Lấy token từ cookie
  // 💡 request.cookies: Access cookies từ request
  // 💡 get('token'): Lấy cookie có tên 'token'

  if (!token && request.nextUrl.pathname.startsWith('/dashboard')) {
    // 💡 !token: Không có token (chưa login)
    // 💡 pathname.startsWith('/dashboard'): Đang truy cập dashboard
    // 💡 → Chưa login + truy cập protected route → Redirect login

    return NextResponse.redirect(new URL('/login', request.url));
    // 💡 redirect: Redirect user đến /login
    // 💡 new URL('/login', request.url): Tạo absolute URL
    // 💡 User không thể truy cập dashboard nếu chưa login
  }

  // 🧪 A/B Testing (Thử nghiệm A/B)
  const bucket =
    request.cookies.get('bucket') || Math.random() > 0.5 ? 'a' : 'b';
  // 💡 bucket: Xác định user thuộc variant nào (A hoặc B)
  // 💡 request.cookies.get('bucket'): Lấy bucket từ cookie (nếu có)
  // 💡 || Math.random() > 0.5 ? 'a' : 'b': Random nếu chưa có
  // 💡 → User được assign vào variant A hoặc B

  const response = NextResponse.next(); // ➡️ Tiếp tục request
  // 💡 next(): Cho phép request tiếp tục đến page/API
  // 💡 response: Response object để modify

  response.cookies.set('bucket', bucket); // 🍪 Set bucket vào cookie
  // 💡 cookies.set(): Set cookie trong response
  // 💡 User sẽ có cookie 'bucket' → Lần sau vẫn variant đó
  // 💡 → Consistent A/B testing

  // 🔄 Rewrite (thay đổi URL nội bộ - không redirect)
  if (request.nextUrl.pathname === '/old-blog') {
    // 💡 pathname === '/old-blog': User truy cập /old-blog
    // 💡 Rewrite: Serve content từ /blog nhưng URL vẫn /old-blog

    return NextResponse.rewrite(new URL('/blog', request.url));
    // 💡 rewrite: Serve content từ /blog nhưng không đổi URL
    // 💡 User thấy URL /old-blog nhưng nhận content từ /blog
    // 💡 Khác redirect: URL không đổi, chỉ content đổi
    // 💡 Use case: Migration, URL aliases, internal routing
  }

  return response; // ➡️ Trả response (cho phép request tiếp tục)
}

// 🎯 Chỉ chạy cho specific paths (Giới hạn paths middleware chạy)
export const config = {
  matcher: ['/dashboard/:path*', '/api/:path*'], // 🎯 Path patterns
  // 💡 matcher: Array các path patterns middleware sẽ chạy
  // 💡 '/dashboard/:path*': Match /dashboard và tất cả sub-paths
  // 💡 VD: /dashboard, /dashboard/settings, /dashboard/users...
  // 💡 '/api/:path*': Match tất cả API routes
  // 💡 VD: /api/users, /api/posts/123...
  // 💡 ⚠️ Không match → Middleware không chạy → Performance tốt hơn
};
// 💡 Best practice: Chỉ match paths cần middleware → Giảm overhead
```

---

##### **2.2. App Router (Next.js 13+ - New - Router Mới)**

```typescript
// 📁 app/layout.tsx - Root layout (Layout gốc)
// 💡 layout.tsx: Component wrap tất cả pages trong segment
// 💡 Root layout: Wrap toàn bộ app → HTML structure chung
export default function RootLayout({ children }) {
  // 💡 children: Pages/components được render bên trong layout
  // 💡 Layout không re-render khi navigate → Giữ state, performance tốt

  return (
    <html>
      <body>{children}</body>
      {/* 💡 children: Pages sẽ được render ở đây */}
    </html>
  );
}

// 📄 app/page.tsx - Home page (Server Component mặc định)
// 💡 page.tsx: Component render cho route
// 💡 app/page.tsx → Route / (home page)
// 💡 Mặc định là Server Component → Không cần 'use client'

async function getData() {
  // 💡 getData: Function fetch data (có thể async)
  // 💡 Chạy trên server → Có thể access database, secrets...

  const res = await fetch('https://api.example.com/data'); // 📡 Fetch data
  return res.json(); // 📦 Parse JSON
}

export default async function Page() {
  // 💡 async: Component có thể là async trong App Router!
  // 💡 Không cần getServerSideProps → Đơn giản hơn

  const data = await getData(); // ⚡ Async component!
  // 💡 await: Đợi data fetch xong → Render với data
  // 💡 Chạy trên server → Data có sẵn khi HTML gửi xuống

  return <div>{data.title}</div>; // 📝 Render với data
  // 💡 HTML đã có data → SEO tốt, không cần client-side fetch
}

// 📁 app/dashboard/layout.tsx - Nested layout (Layout lồng nhau)
// 💡 Nested layout: Layout chỉ cho segment /dashboard
// 💡 Layout hierarchy: Root layout → Dashboard layout → Page
export default function DashboardLayout({ children }) {
  return (
    <div>
      <Sidebar /> {/* 📋 Sidebar hiển thị cho tất cả /dashboard/* pages */}
      {children} {/* 📄 Pages trong /dashboard/* */}
      {/* 💡 Layout được share → Sidebar không re-render khi navigate */}
    </div>
  );
}

// 💻 Client component (when needed - Khi cần interactivity)
('use client'); // 🔧 Directive để khai báo Client Component
// 💡 'use client': Phải đặt ở đầu file
// 💡 Component này sẽ render trên client → Có interactivity
// 💡 Có thể dùng hooks, event handlers, browser APIs

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0); // 📊 State (chỉ Client Component)
  // 💡 useState: Hook chỉ dùng được trong Client Component
  // 💡 Server Component không có state → Không dùng được

  return (
    <button onClick={() => setCount(count + 1)}>
      {/* 💡 onClick: Event handler chỉ dùng được trong Client Component */}
      {count}
    </button>
  );
}
// 💡 Best practice: Chỉ dùng 'use client' khi thật sự cần interactivity
// 💡 Giữ nhiều components là Server Component → Giảm JS bundle
```

---

##### **2.3. Data Fetching (App Router)**

```typescript
// 📦 Fetch with caching (Fetch với cache - SSG-like)
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'force-cache', // 💾 SSG-like (default trong Next.js 14)
    // 💡 force-cache: Cache response vĩnh viễn (không expire)
    // 💡 Giống SSG: Data được cache lúc build → Serve từ cache
    // 💡 ⚠️ Next.js 15: Default là 'no-store' → Phải opt-in caching
  });
  return res.json();
}
// 💡 Use case: Data ít thay đổi, static content
// 💡 Performance: Cực nhanh (serve từ cache)

// 🔄 Revalidate every 10s (ISR - Tạo lại mỗi 10s)
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    next: { revalidate: 10 }, // ⏰ ISR: Revalidate mỗi 10 giây
    // 💡 revalidate: Thời gian (giây) để cache hợp lệ
    // 💡 10: Sau 10 giây, request tiếp theo sẽ fetch data mới
    // 💡 Request hiện tại: Serve từ cache (stale) → Nhanh
    // 💡 Background: Fetch data mới → Update cache
    // 💡 Request sau: Serve data mới (fresh)
  });
  return res.json();
}
// 💡 Use case: Data thay đổi thường xuyên nhưng không cần real-time
// 💡 Best of both: Tốc độ cache + Data mới định kỳ

// 🔄 No caching (SSR-like - Không cache, luôn fresh)
async function getData() {
  const res = await fetch('https://api.example.com/data', {
    cache: 'no-store', // 🚫 Không cache, luôn fetch mới
    // 💡 no-store: Không cache response → Mỗi request fetch mới
    // 💡 Giống SSR: Data luôn fresh, nhưng chậm hơn
    // 💡 ⚠️ Next.js 15: Đây là default behavior
  });
  return res.json();
}
// 💡 Use case: Data real-time, user-specific, sensitive data
// 💡 Trade-off: Data mới nhưng chậm hơn (phải fetch mỗi request)

// ⚡ Parallel data fetching (Lấy dữ liệu song song)
export default async function Page() {
  // 💡 Promise.all: Fetch nhiều data song song → Nhanh hơn sequential
  const [user, posts] = await Promise.all([
    // 💡 Promise.all: Chờ TẤT CẢ promises hoàn thành
    // 💡 Fetch song song → Tổng thời gian = max của các requests

    fetch('/api/user').then((r) => r.json()), // 👤 Fetch user data
    fetch('/api/posts').then((r) => r.json()), // 📝 Fetch posts data
    // 💡 Cả 2 requests chạy song song → Không chờ nhau
  ]);
  // 💡 Total time: max(200ms, 300ms) = 300ms (song song)
  // 💡 Sequential: 200ms + 300ms = 500ms (tuần tự)
  // 💡 → Parallel nhanh hơn 40%!

  return (
    <div>
      {user.name} - {posts.length} posts
    </div>
  ); // 📝 Render với data
}
// 💡 Best practice: Fetch parallel khi có thể → Giảm loading time
// 💡 User experience: Page load nhanh hơn → Better UX
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
  const product = await fetch(`/api/products/${params.id}`).then((r) =>
    r.json()
  );

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
/>;

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
('use server');

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
  const filtered = items.filter((item) => item.active);
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

| Feature              | Next.js 14 | Next.js 15                | Next.js 16 (Expected) |
| -------------------- | ---------- | ------------------------- | --------------------- |
| **React Version**    | 18         | 19 RC                     | 19 Stable             |
| **Turbopack Dev**    | Beta       | ✅ Stable                 | ✅ Stable             |
| **Turbopack Build**  | ❌         | ❌                        | ✅ Stable             |
| **Server Actions**   | ✅ Stable  | ✅ Stable                 | ✅ Enhanced           |
| **PPR**              | Preview    | Experimental              | ✅ Stable             |
| **Request APIs**     | Sync       | ⚠️ Async (breaking)       | Async                 |
| **Caching**          | Default ON | ⚠️ Default OFF (breaking) | Opt-in                |
| **React Compiler**   | ❌         | Experimental              | ✅ Default            |
| **Hydration Errors** | Basic      | ✅ Improved               | Enhanced              |
| **Edge Runtime**     | Basic      | Improved                  | ✅ Mature             |

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

## **🔬 PHẦN 7: SERVER COMPONENTS DEEP DIVE**

### **7.1. Server vs Client Components - Phân Biệt Chi Tiết**

```typescript
// ===================================================
// 🖥️ SERVER COMPONENTS (Default trong App Router)
// ===================================================

/**
 * 🎯 Server Components là gì?
 *
 * - Render HOÀN TOÀN trên server
 * - Không gửi JavaScript xuống client
 * - Không có interactivity (no onClick, useState, useEffect)
 * - Có thể fetch data trực tiếp (async/await)
 * - Reduce bundle size (không ship React code cho component này)
 */

// ✅ Server Component (default - Mặc định trong App Router)
// app/products/page.tsx
async function ProductsPage() {
  // 💡 async: Server Component có thể là async function
  // 💡 Không cần 'use client' → Mặc định là Server Component

  // ✅ Fetch data directly (no useEffect needed!)
  const products = await fetch('https://api.example.com/products').then((r) =>
    r.json()
  );
  // 💡 Fetch trực tiếp trong component → Không cần useEffect
  // 💡 Chạy trên server → Có thể access database, secrets...
  // 💡 Data có sẵn khi HTML gửi xuống → SEO tốt

  return (
    <div>
      <h1>Products</h1>
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
        // 💡 ProductCard: Có thể là Server hoặc Client Component
        // 💡 Server Component có thể render Client Component
      ))}
    </div>
  );
  // 💡 HTML được render trên server → Gửi xuống client đã có nội dung
  // 💡 Không có JS cho component này → Bundle size nhỏ hơn
}

// ===================================================
// 💻 CLIENT COMPONENTS (Opt-in với 'use client')
// ===================================================

/**
 * 🎯 Client Components là gì?
 *
 * - Render trên server (SSR) + hydrate trên client
 * - CÓ interactivity (onClick, useState, useEffect)
 * - Gửi JavaScript xuống client
 * - Giống React traditional components
 */

// ✅ Client Component (needs 'use client' directive - Cần directive 'use client')
// components/AddToCartButton.tsx
('use client'); // 🔧 Directive phải đặt ở đầu file
// 💡 'use client': Khai báo component này là Client Component
// 💡 Component này sẽ render trên client → Có interactivity

import { useState } from 'react'; // 📦 Hook chỉ dùng được trong Client Component

export function AddToCartButton({ productId }: { productId: string }) {
  const [loading, setLoading] = useState(false); // 📊 State (chỉ Client Component)
  // 💡 useState: Hook để quản lý state
  // 💡 loading: State để track loading status

  const handleClick = async () => {
    // 💡 handleClick: Event handler (chỉ Client Component)
    setLoading(true); // ⏳ Set loading = true
    await addToCart(productId); // 📡 Call API để add to cart
    setLoading(false); // ✅ Set loading = false
  };

  return (
    <button onClick={handleClick} disabled={loading}>
      {/* 💡 onClick: Event handler chỉ dùng được trong Client Component */}
      {/* 💡 disabled: Disable button khi đang loading */}
      {loading ? 'Adding...' : 'Add to Cart'}{' '}
      {/* 📝 Hiển thị text theo state */}
    </button>
  );
  // 💡 Component này có JS → Gửi xuống client → Bundle size tăng
  // 💡 Trade-off: Cần interactivity → Phải có JS
}

// ===================================================
// 🔀 COMPOSITION: Server + Client Components (Kết hợp Server + Client)
// ===================================================

// ✅ Server Component (parent - Component cha)
async function ProductPage({ productId }: { productId: string }) {
  // 💡 ProductPage: Server Component → Fetch data trực tiếp
  const product = await fetchProduct(productId); // 📡 Fetch data trên server
  // 💡 fetchProduct: Function chạy trên server → Access database, secrets...

  return (
    <div>
      {/* 🖥️ Server-rendered content (Nội dung render trên server) */}
      <h1>{product.name}</h1> {/* 📝 Render từ server → SEO tốt */}
      <p>{product.description}</p> {/* 📝 Render từ server → HTML đầy đủ */}
      {/* 💻 Client-only interactivity (Tương tác chỉ trên client) */}
      <AddToCartButton productId={productId} />
      {/* 💡 AddToCartButton: Client Component → Có onClick, useState */}
      {/* 💡 Server Component có thể render Client Component */}
      {/* 💡 Props được serialize → Truyền từ server xuống client */}
    </div>
  );
  // 💡 Best practice: Server Component fetch data → Client Component handle interaction
  // 💡 → Giảm JS bundle (chỉ button có JS, không phải toàn bộ page)
}

// ===================================================
// 📊 COMPARISON TABLE
// ===================================================

/**
┌──────────────────────┬───────────────────┬───────────────────┐
│ Feature              │ Server Component  │ Client Component  │
├──────────────────────┼───────────────────┼───────────────────┤
│ JavaScript to client │ ❌ No             │ ✅ Yes            │
│ useState/useEffect   │ ❌ No             │ ✅ Yes            │
│ onClick/onChange     │ ❌ No             │ ✅ Yes            │
│ Async/await          │ ✅ Yes            │ ❌ No (useEffect) │
│ Access backend       │ ✅ Direct         │ ❌ Via API        │
│ Access secrets       │ ✅ Safe           │ ❌ Exposed        │
│ Bundle size          │ ✅ 0 KB           │ ⚠️ Adds KB        │
│ SEO                  │ ✅ Perfect        │ ⚠️ Needs SSR      │
└──────────────────────┴───────────────────┴───────────────────┘
*/
```

---

### **7.2. Data Fetching Patterns**

```typescript
// ===================================================
// 🎯 PATTERN 1: Sequential Fetching (Waterfall - Lấy Dữ Liệu Tuần Tự)
// ===================================================

// ❌ BAD: Slow (total time = sum of all requests - Tổng thời gian = tổng các requests)
async function SlowPage() {
  // 💡 Sequential: Fetch lần lượt → Chậm (tổng thời gian = tổng các requests)

  const user = await fetchUser(); // ⏱️ 200ms
  // 💡 await: Đợi fetchUser hoàn thành → Mất 200ms

  const posts = await fetchPosts(user.id); // ⏱️ 300ms
  // 💡 Phải đợi user xong mới fetch posts → Mất thêm 300ms
  // 💡 Phụ thuộc: Cần user.id từ request trước

  const comments = await fetchComments(posts[0].id); // ⏱️ 200ms
  // 💡 Phải đợi posts xong mới fetch comments → Mất thêm 200ms
  // 💡 Phụ thuộc: Cần posts[0].id từ request trước

  // Total: 700ms (sequential) - Tổng: 700ms (tuần tự)
  // 💡 200ms + 300ms + 200ms = 700ms
  // 💡 ⚠️ Chậm: Phải chờ từng request hoàn thành

  return <div>...</div>;
}

// ===================================================
// ✅ PATTERN 2: Parallel Fetching (Lấy Dữ Liệu Song Song)
// ===================================================

// ✅ GOOD: Fast (total time = max of all requests - Tổng thời gian = max của các requests)
async function FastPage() {
  // 💡 Parallel: Fetch song song → Nhanh (tổng thời gian = max của các requests)

  // ⚡ Start all requests in parallel (Bắt đầu tất cả requests song song)
  const [user, posts, comments] = await Promise.all([
    // 💡 Promise.all: Chờ TẤT CẢ promises hoàn thành
    // 💡 Tất cả requests chạy song song → Không chờ nhau

    fetchUser(), // ⏱️ 200ms (chạy song song)
    fetchPosts(), // ⏱️ 300ms (chạy song song)
    fetchComments(), // ⏱️ 200ms (chạy song song)
    // 💡 Cả 3 requests chạy cùng lúc → Không phụ thuộc nhau
  ]);
  // Total: 300ms (parallel) - Tổng: 300ms (song song)
  // 💡 max(200ms, 300ms, 200ms) = 300ms
  // 💡 ✅ Nhanh hơn 57% so với sequential (700ms → 300ms)

  return <div>...</div>;
}
// 💡 Best practice: Fetch parallel khi có thể → Giảm loading time đáng kể
// 💡 Trade-off: Cần đảm bảo requests không phụ thuộc nhau

// ===================================================
// ✅ PATTERN 3: Streaming with Suspense (Streaming với Suspense)
// ===================================================

// app/dashboard/page.tsx
import { Suspense } from 'react'; // 📦 Suspense: React component cho streaming

export default function DashboardPage() {
  return (
    <div>
      {/* ⚡ Show immediately (Hiển thị ngay lập tức) */}
      <Header />
      // 💡 Header: Render ngay → Gửi xuống client đầu tiên // 💡 User thấy
      header ngay → Perceived performance tốt
      {/* 🌊 Stream in when ready (Stream khi sẵn sàng) */}
      <Suspense fallback={<UserSkeleton />}>
        {/* 💡 Suspense: Boundary cho async components */}
        {/* 💡 fallback: Hiển thị khi component đang load */}
        {/* 💡 UserSkeleton: Loading state (skeleton UI) */}
        <UserInfo /> {/* ⏳ async component */}
        // 💡 UserInfo: Async Server Component → Fetch data // 💡 Khi fetch xong
        → Stream HTML xuống client // 💡 Thay thế UserSkeleton → Progressive
        loading
      </Suspense>
      <Suspense fallback={<StatsSkeleton />}>
        {/* 💡 Suspense riêng cho Stats → Không block UserInfo */}
        <Stats /> {/* ⏳ async component */}
        // 💡 Stats: Async Server Component → Fetch data song song với UserInfo
        // 💡 Không chờ UserInfo → Fetch parallel → Nhanh hơn
      </Suspense>
    </div>
  );
}

// ⏳ Async Server Component (Component async)
async function UserInfo() {
  const user = await fetchUser(); // ⏱️ Slow query (2 seconds)
  // 💡 fetchUser: Query chậm (2 giây)
  // 💡 await: Đợi data → Render sau

  return <div>{user.name}</div>; // 📝 Render với data
  // 💡 HTML được stream xuống client khi ready
}

async function Stats() {
  const stats = await fetchStats(); // ⏱️ Slow query (1 second)
  // 💡 fetchStats: Query chậm (1 giây)
  // 💡 Chạy song song với UserInfo → Không chờ nhau

  return <div>{stats.count}</div>; // 📝 Render với data
}

/**
 * 🎯 Rendering Flow (Quy trình render):
 *
 * 1. 📤 Header renders immediately (100ms)
 *    // 💡 Header render ngay → Gửi HTML shell xuống client
 *    // 💡 User thấy header → TTFB nhanh (100ms)
 *
 * 2. ⏳ UserSkeleton + StatsSkeleton show
 *    // 💡 Skeletons hiển thị → User thấy loading states
 *    // 💡 Better UX: User biết đang load, không phải blank screen
 *
 * 3. 🔄 UserInfo starts fetching (doesn't block Stats)
 *    // 💡 UserInfo bắt đầu fetch → Không block Stats
 *    // 💡 Stats cũng fetch song song → Parallel fetching
 *
 * 4. 🔄 Stats starts fetching (parallel with UserInfo)
 *    // 💡 Stats fetch song song với UserInfo
 *    // 💡 Total time: max(2s, 1s) = 2s (không phải 3s sequential)
 *
 * 5. 📤 Whichever finishes first streams to client
 *    // 💡 Stats xong trước (1s) → Stream HTML xuống client
 *    // 💡 User thấy Stats → StatsSkeleton được thay thế
 *
 * 6. 📤 Both eventually replace skeletons
 *    // 💡 UserInfo xong sau (2s) → Stream HTML xuống client
 *    // 💡 User thấy UserInfo → UserSkeleton được thay thế
 *
 * ✅ User sees something immediately (Header + Skeletons)
 *    // 💡 User thấy content ngay → Perceived performance tốt
 *    // 💡 TTFB: 100ms (vs 2000ms traditional SSR)
 *
 * ✅ Progressive loading (better UX than spinner)
 *    // 💡 Progressive: Từng phần load → Better UX
 *    // 💡 Không phải chờ tất cả → User thấy content sớm hơn
 */

// ===================================================
// 🎯 PATTERN 4: Preload Pattern (Performance - Pattern Tối Ưu Hiệu Năng)
// ===================================================

// lib/data.ts
import { cache } from 'react'; // 📦 cache: React function để deduplicate requests

// ✅ Deduplicate requests across components (Loại bỏ requests trùng lặp)
export const getUser = cache(async (id: string) => {
  // 💡 cache(): Wrap function để React tự động deduplicate
  // 💡 Nếu gọi getUser() nhiều lần với cùng id trong 1 render → Chỉ fetch 1 lần
  // 💡 React cache kết quả trong render cycle → Giảm network requests

  return fetch(`/api/users/${id}`).then((r) => r.json());
  // 💡 Fetch user data từ API
});

// app/users/[id]/page.tsx
async function UserPage({ params }: { params: { id: string } }) {
  const user = await getUser(params.id); // 📡 Fetch user (lần 1)
  // 💡 getUser(params.id): Gọi function → Fetch từ API
  // 💡 Kết quả được cache trong render cycle

  return (
    <div>
      <UserProfile userId={params.id} /> {/* 📄 Component con */}
      <UserPosts userId={params.id} /> {/* 📄 Component con */}
    </div>
  );
}

// components/UserProfile.tsx
async function UserProfile({ userId }: { userId: string }) {
  const user = await getUser(userId); // 📡 Same request, cached!
  // 💡 getUser(userId): Gọi với cùng id
  // 💡 React check cache → Đã có kết quả từ lần gọi trước
  // 💡 → Không fetch lại → Dùng cache → Nhanh, không tốn network

  return <div>{user.name}</div>; // 📝 Render với cached data
}

// components/UserPosts.tsx
async function UserPosts({ userId }: { userId: string }) {
  const user = await getUser(userId); // 📡 Same request, cached!
  // 💡 getUser(userId): Gọi với cùng id
  // 💡 React check cache → Đã có kết quả → Dùng cache

  const posts = await getPosts(userId); // 📡 Fetch posts (request khác)
  // 💡 getPosts: Request khác → Không bị cache (chưa wrap với cache)

  return <PostList posts={posts} />; // 📝 Render với data
}

/**
 * ✅ getUser() called 3 times but only 1 network request!
 *    // 💡 getUser() được gọi 3 lần (UserPage, UserProfile, UserPosts)
 *    // 💡 Nhưng chỉ có 1 network request → React deduplicate tự động
 *    // 💡 Lần 1: Fetch từ API → Cache kết quả
 *    // 💡 Lần 2, 3: Dùng cache → Không fetch lại
 *
 * React automatically deduplicates during render
 *    // 💡 React tự động deduplicate requests trong cùng render cycle
 *    // 💡 cache(): Giúp React biết function nào cần deduplicate
 *    // 💡 → Giảm network overhead → Performance tốt hơn
 */
// 💡 Best practice: Dùng cache() cho data fetching functions
// 💡 → Tự động deduplicate → Không cần manual memoization
```

---

### **7.3. Streaming SSR - Progressive Rendering**

```typescript
// ===================================================
// 🌊 STREAMING SSR - Gửi HTML từng phần
// ===================================================

/**
 * 🖥️ Traditional SSR (SSR Truyền Thống):
 * ┌─────────────────────────────────────────────────┐
 * │  Server waits for ALL data                     │
 * │  // 💡 Server phải chờ TẤT CẢ data fetch xong
 * │  → Generates complete HTML                     │
 * │  // 💡 Sau đó mới generate HTML đầy đủ
 * │  → Sends to browser (1 chunk)                  │
 * │  // 💡 Gửi toàn bộ HTML trong 1 lần
 * │  → Browser shows everything                    │
 * │  // 💡 Browser nhận HTML đầy đủ → Hiển thị tất cả
 * └─────────────────────────────────────────────────┘
 * Total time: 3 seconds (all or nothing - Tất cả hoặc không gì cả)
 * // 💡 Phải chờ 3 giây → User thấy blank screen → UX kém
 * // 💡 TTFB: 3 giây (chậm)
 *
 * 🌊 Streaming SSR (SSR Streaming):
 * ┌─────────────────────────────────────────────────┐
 * │  Server sends HTML shell immediately (100ms)   │
 * │  // 💡 Server gửi HTML shell ngay (100ms)
 * │  // 💡 Shell: Structure cơ bản (header, skeleton...)
 * │  → Browser shows shell + loading states        │
 * │  // 💡 Browser hiển thị shell + skeletons ngay
 * │  // 💡 User thấy content ngay → Perceived performance tốt
 * │  → Server streams data as ready                │
 * │  // 💡 Server stream HTML từng phần khi data sẵn sàng
 * │  // 💡 Không chờ tất cả → Stream progressive
 * │  → Browser updates incrementally               │
 * │  // 💡 Browser update từng phần → Progressive enhancement
 * └─────────────────────────────────────────────────┘
 * Time to First Byte: 100ms (fast! - Nhanh!)
 * // 💡 TTFB: 100ms (vs 3000ms traditional) → Nhanh hơn 30 lần!
 *
 * Time to Full Page: 3 seconds (same, but UX better - Cùng thời gian nhưng UX tốt hơn)
 * // 💡 Tổng thời gian vẫn 3 giây (fetch data)
 * // 💡 Nhưng UX tốt hơn: User thấy content sớm → Perceived performance tốt
 */

// app/products/[id]/page.tsx
import { Suspense } from 'react'; // 📦 Suspense: React component cho streaming

export default function ProductPage({ params }: { params: { id: string } }) {
  return (
    <div>
      {/* ⚡ Sent immediately (shell - Gửi ngay lập tức) */}
      <Navigation /> {/* 📋 Navigation render ngay → Gửi xuống client đầu tiên */}
      <Breadcrumb productId={params.id} /> {/* 🍞 Breadcrumb render ngay */}
      // 💡 Navigation + Breadcrumb: Render ngay → Không cần fetch data // 💡 → Gửi
      xuống client ngay → User thấy structure sớm
      {/* 🌊 Suspense boundary = streaming point (Điểm streaming) */}
      <Suspense fallback={<ProductSkeleton />}>
        {/* 💡 Suspense: Boundary cho async component */}
        {/* 💡 fallback: Hiển thị skeleton khi đang load */}
        {/* 💡 ProductSkeleton: Loading state cho product */}
        <ProductDetails productId={params.id} /> {/* ⏳ Async component */}
        // 💡 ProductDetails: Async Server Component → Fetch data // 💡 Khi
        fetch xong → Stream HTML xuống client // 💡 Thay thế ProductSkeleton →
        Progressive loading
      </Suspense>
      <Suspense fallback={<ReviewsSkeleton />}>
        {/* 💡 Suspense riêng cho Reviews → Không block ProductDetails */}
        <ProductReviews productId={params.id} /> {/* ⏳ Async component */}
        // 💡 ProductReviews: Async Server Component → Fetch data song song //
        💡 Không chờ ProductDetails → Fetch parallel → Nhanh hơn
      </Suspense>
      {/* ⚡ Sent immediately (footer - Gửi ngay lập tức) */}
      <Footer /> {/* 📋 Footer render ngay */}
      // 💡 Footer: Render ngay → Gửi xuống client ngay
    </div>
  );
}

// ⏳ Slow async component (Component async chậm)
async function ProductDetails({ productId }: { productId: string }) {
  const product = await fetchProduct(productId); // ⏱️ 2 seconds
  // 💡 fetchProduct: Query chậm (2 giây)
  // 💡 await: Đợi data → Render sau
  // 💡 Chạy song song với ProductReviews → Không block

  return <div>{product.name}</div>; // 📝 Render với data
  // 💡 HTML được stream xuống client khi ready
  // 💡 Thay thế ProductSkeleton → User thấy product name
}

async function ProductReviews({ productId }: { productId: string }) {
  const reviews = await fetchReviews(productId); // ⏱️ 1 second
  // 💡 fetchReviews: Query chậm (1 giây)
  // 💡 Chạy song song với ProductDetails → Không chờ nhau

  return <ReviewList reviews={reviews} />; // 📝 Render với data
  // 💡 HTML được stream xuống client khi ready
  // 💡 Thay thế ReviewsSkeleton → User thấy reviews
}

/**
 * 🎯 Timeline (Dòng thời gian):
 *
 * 0ms:   📤 Send HTML shell (Navigation, Breadcrumb, Footer, Skeletons)
 *        // 💡 Server gửi HTML shell ngay → TTFB nhanh
 *        // 💡 Shell: Structure cơ bản + Skeletons
 *
 * 100ms: 👁️ User sees page structure
 *        // 💡 Browser nhận shell → Hiển thị ngay
 *        // 💡 User thấy navigation, breadcrumb, skeletons
 *        // 💡 → Perceived performance tốt (không phải blank screen)
 *
 * 1000ms: 📤 Reviews finish → stream to client → replace skeleton
 *         // 💡 ProductReviews xong trước (1 giây)
 *         // 💡 Server stream HTML xuống client
 *         // 💡 Browser thay thế ReviewsSkeleton → User thấy reviews
 *
 * 2000ms: 📤 Product finishes → stream to client → replace skeleton
 *         // 💡 ProductDetails xong sau (2 giây)
 *         // 💡 Server stream HTML xuống client
 *         // 💡 Browser thay thế ProductSkeleton → User thấy product
 *
 * ✅ Time to First Byte: 100ms (vs 2000ms traditional SSR)
 *    // 💡 TTFB: 100ms (vs 2000ms traditional) → Nhanh hơn 20 lần!
 *    // 💡 User thấy content sớm → Better UX
 *
 * ✅ User sees something immediately
 *    // 💡 User thấy page structure ngay → Không phải chờ
 *    // 💡 Skeletons → User biết đang load → Better UX
 *
 * ✅ Progressive enhancement
 *    // 💡 Progressive: Từng phần load → User thấy content sớm
 *    // 💡 Không phải chờ tất cả → Better perceived performance
 */
```

---

### **7.4. Server Actions - Backend Functions in Components**

```typescript
// ===================================================
// ⚡ SERVER ACTIONS - RPC-like Backend Functions
// ===================================================

/**
 * ⚡ Server Actions = Functions that run on server, callable from client components
 *    // 💡 Server Actions: Functions chạy trên server, có thể gọi từ client
 *    // 💡 Giống RPC (Remote Procedure Call) → Gọi function như local function
 *    // 💡 Type-safe, không cần API routes → Đơn giản hơn
 *
 * ✅ No need for API routes
 *    // 💡 Không cần tạo API routes (pages/api/ hoặc app/api/)
 *    // 💡 Server Actions thay thế → Ít code hơn, type-safe hơn
 *
 * ✅ Type-safe (TypeScript inference)
 *    // 💡 TypeScript tự động infer types → Type-safe end-to-end
 *    // 💡 Client và Server share types → Không cần manual typing
 *
 * ✅ Progressive enhancement (works without JS)
 *    // 💡 Form vẫn hoạt động khi JS disabled → Progressive enhancement
 *    // 💡 Server Actions work với native form submission
 */

// app/actions.ts
'use server'; // 🔧 Directive để khai báo Server Actions
// 💡 'use server': Phải đặt ở đầu file hoặc function
// 💡 Next.js biết function này chạy trên server → Generate RPC endpoint

import { revalidatePath } from 'next/cache'; // 📦 Function để invalidate cache

export async function createPost(formData: FormData) {
  // 💡 createPost: Server Action → Chạy trên server
  // 💡 formData: FormData từ form submission
  // 💡 async: Có thể async (fetch, database...)

  const title = formData.get('title') as string; // 📝 Lấy title từ form
  const content = formData.get('content') as string; // 📝 Lấy content từ form
  // 💡 formData.get(): Lấy value từ form field
  // 💡 as string: Type assertion (FormData.get() trả về string | null)

  // ✅ Direct database access (server-only code - Truy cập database trực tiếp)
  await db.posts.create({ data: { title, content } });
  // 💡 db.posts.create(): Truy cập database trực tiếp
  // 💡 Chạy trên server → Có thể access database, secrets...
  // 💡 Không cần API route → Đơn giản hơn

  // ✅ Revalidate cache (Làm mới cache)
  revalidatePath('/posts');
  // 💡 revalidatePath: Invalidate cache cho path '/posts'
  // 💡 Sau khi tạo post → Cache cũ không còn hợp lệ
  // 💡 Next request → Fetch data mới → User thấy post mới

  return { success: true }; // 📤 Trả kết quả
  // 💡 Return value được serialize → Gửi về client
  // 💡 Type-safe: TypeScript biết return type
}

// components/PostForm.tsx
('use client'); // 🔧 Client Component (cần interactivity)

import { createPost } from '@/app/actions'; // 📦 Import Server Action
// 💡 Import Server Action như import function bình thường
// 💡 Next.js tự động generate RPC endpoint → Type-safe

import { useFormStatus } from 'react-dom'; // 📦 Hook để track form status

export function PostForm() {
  async function handleSubmit(formData: FormData) {
    // 💡 handleSubmit: Form submit handler
    // 💡 formData: FormData từ form (tự động pass vào)

    const result = await createPost(formData); // ⚡ Gọi Server Action
    // 💡 createPost: Server Action → Chạy trên server
    // 💡 await: Đợi Server Action hoàn thành
    // 💡 Type-safe: TypeScript biết result type

    if (result.success) {
      alert('Post created!'); // ✅ Hiển thị thông báo
    }
  }

  return (
    <form action={handleSubmit}>
      {/* 💡 action={handleSubmit}: Form action handler */}
      {/* 💡 Progressive enhancement: Form vẫn work khi JS disabled */}
      <input name="title" required /> {/* 📝 Input field */}
      <textarea name="content" required /> {/* 📝 Textarea field */}
      <SubmitButton /> {/* 🔘 Submit button */}
    </form>
  );
}

function SubmitButton() {
  const { pending } = useFormStatus(); // 📊 Hook để track form status
  // 💡 useFormStatus: Hook để biết form đang submit không
  // 💡 pending: true khi form đang submit, false khi xong

  return (
    <button type="submit" disabled={pending}>
      {/* 💡 disabled={pending}: Disable button khi đang submit */}
      {pending ? 'Creating...' : 'Create Post'} {/* 📝 Hiển thị text theo status */}
    </button>
  );
}
// 💡 Best practice: Dùng useFormStatus để show loading state
// 💡 → Better UX: User biết form đang submit

// ===================================================
// 🎯 SERVER ACTIONS PATTERNS (Các Pattern Server Actions)
// ===================================================

// 🎨 Pattern 1: Optimistic UI (UI Lạc Quan - Update UI trước khi server confirm)
('use client'); // 🔧 Client Component (cần interactivity)

import { useOptimistic } from 'react'; // 📦 Hook cho optimistic updates
import { likePost } from './actions'; // 📦 Server Action

export function LikeButton({ postId, initialLikes }) {
  // 💡 LikeButton: Button để like post
  // 💡 postId: ID của post
  // 💡 initialLikes: Số likes ban đầu

  const [optimisticLikes, setOptimisticLikes] = useOptimistic(initialLikes);
  // 💡 useOptimistic: Hook để quản lý optimistic state
  // 💡 optimisticLikes: State hiển thị (có thể khác với server)
  // 💡 setOptimisticLikes: Function để update optimistic state
  // 💡 initialLikes: Giá trị ban đầu (từ server)

  async function handleLike() {
    // 💡 handleLike: Handler khi user click like

    // ⚡ Update UI immediately (optimistic - Cập nhật UI ngay lập tức)
    setOptimisticLikes((likes) => likes + 1);
    // 💡 Update UI ngay → User thấy likes tăng ngay
    // 💡 Optimistic: Giả định action sẽ thành công
    // 💡 → Better UX: User không phải chờ server response

    // 📡 Call server action (Gọi Server Action)
    await likePost(postId);
    // 💡 likePost: Server Action → Update database
    // 💡 Nếu fail → React tự động revert optimistic update
    // 💡 Nếu success → Optimistic update đúng → UI đã update sẵn
  }

  return <button onClick={handleLike}>❤️ {optimisticLikes}</button>;
  // 💡 Hiển thị optimisticLikes → User thấy số likes tăng ngay
  // 💡 Nếu server fail → React revert → User thấy số likes cũ
}

// 🔄 Pattern 2: Revalidation after mutation (Làm mới cache sau khi thay đổi)
('use server'); // 🔧 Server Action

export async function updateProduct(id: string, data: ProductData) {
  // 💡 updateProduct: Server Action để update product
  // 💡 id: Product ID
  // 💡 data: Data mới để update

  await db.products.update({ where: { id }, data }); // 💾 Update database
  // 💡 db.products.update(): Update product trong database
  // 💡 Sau khi update → Cache cũ không còn hợp lệ

  // 🔄 Revalidate specific paths (Làm mới cache cho paths cụ thể)
  revalidatePath(`/products/${id}`); // 🔄 Invalidate product detail page
  // 💡 revalidatePath: Invalidate cache cho path cụ thể
  // 💡 `/products/${id}`: Product detail page → Fetch data mới

  revalidatePath('/products'); // 🔄 Invalidate products list page
  // 💡 '/products': Products list page → Fetch data mới
  // 💡 Product list có thể hiển thị product đã update

  // 🔖 Or revalidate by tag (Hoặc làm mới theo tag)
  revalidateTag('products'); // 🔖 Invalidate tất cả cache có tag 'products'
  // 💡 revalidateTag: Invalidate cache theo tag
  // 💡 'products': Tag được set khi fetch (next: { tags: ['products'] })
  // 💡 → Tất cả cache có tag 'products' đều bị invalidate
  // 💡 → Flexible: Invalidate nhiều paths cùng lúc
}
// 💡 Best practice: Revalidate cache sau mutation → User thấy data mới
// 💡 → Không cần hard refresh → Better UX
```

---

#### **🎯 TÓM TẮT Q26 - NEXT.JS COMPREHENSIVE (Updated)**

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

**🆕 Server Components Deep Dive:**

- **Server vs Client**: Server = no JS to client, Client = 'use client' directive
- **Data Fetching**: Sequential vs Parallel vs Streaming patterns
- **Streaming SSR**: Progressive rendering với Suspense, better TTFB
- **Server Actions**: Type-safe backend functions, no API routes needed
- **React Cache**: Automatic request deduplication

**💡 Key Takeaways:**

- Server Components reduce bundle size (no JavaScript shipped)
- Streaming SSR improves perceived performance (100ms TTFB)
- Server Actions enable full-stack TypeScript without API layer
- Next.js 15 changes: opt-in caching, async request APIs
- PPR (Next 16) = static shell + dynamic streaming

---

## 🔍 Giải thích chi tiết bằng tiếng Việt (mức Senior/Tech Lead)

### 1. Trả lời ngắn gọn kiểu phỏng vấn (2–3 phút)

> **“Next.js là React framework cho production, giải quyết toàn bộ vòng đời từ routing, data fetching, rendering (SSR/SSG/ISR/CSR), tới tối ưu hiệu năng (image, font, caching) và SEO. Với App Router + Server Components, Next.js đẩy nhiều logic về server, giảm JS trên client, hỗ trợ streaming và partial prerendering.”**

Khi phỏng vấn Senior/Tech Lead, bạn nên:

- Không chỉ liệt kê feature, mà **gắn với bài toán kiến trúc**: SEO, performance, DX, chi phí vận hành.
- Biết **khi nào dùng SSR/SSG/ISR/CSR**, và **tại sao**.
- Hiểu **App Router, Server Components, Server Actions** tác động thế nào tới kiến trúc frontend/backend.

---

### 2. Bức tranh tổng thể: Next.js giải quyết vấn đề gì?

Nếu chỉ dùng React thuần (CRA/Vite SPA), bạn sẽ phải tự giải quyết:

- Routing (React Router, file-based routing tự setup).
- SSR/SEO (tự cấu hình Node/Express + hydration).
- Code splitting, image optimization, font optimization, bundling.
- API gateway/backend hoặc BFF layer.

**Next.js** gom tất cả vào một framework:

- **File-based routing** → mỗi file là một route, dễ tổ chức.
- **Nhiều chiến lược render per-page**: SSR, SSG, ISR, CSR.
- **Tích hợp sẵn**: API routes, middleware, image/font optimization.
- **App Router + Server Components**: đưa data fetching, logic render sang server, giảm JS ship xuống client.

Kết quả:

- **SEO tốt** (HTML có nội dung ngay từ server).
- **Hiệu năng tốt** (ít JS, streaming, cache tốt).
- **Developer Experience cao** (code ít boilerplate, conventions mạnh).

---

### 3. Hiểu sâu 4 phương pháp render (SSR/SSG/ISR/CSR)

Bạn nên trả lời kiểu "trade-off" thay vì chỉ định nghĩa:

#### 3.1 SSR – Server-Side Rendering

- **Cách hoạt động:**
  - Mỗi request: server chạy React → tạo HTML → gửi cho client.
  - Client sau đó hydrate (gắn JS vào HTML) để có interactivity.
- **Ưu điểm:**
  - Dữ liệu **luôn mới** theo từng request (phù hợp dashboard, trang cá nhân).
  - SEO tốt vì HTML đã có nội dung.
- **Nhược điểm/Trade-off:**
  - Mỗi request đều tốn chi phí render → **tăng TTFB, tăng tải server**.
  - Cần server runtime (không chỉ file tĩnh trên CDN).
- **Khi dùng:**
  - Trang phụ thuộc mạnh vào **session hiện tại** (user-specific) mà không muốn fetch trên client.
  - Dữ liệu thay đổi liên tục, không muốn cache lâu (real-time-ish).

#### 3.2 SSG – Static Site Generation

- **Cách hoạt động:**
  - HTML được build sẵn **lúc build time**.
  - Deploy lên CDN → mỗi request chỉ là trả file tĩnh.
- **Ưu điểm:**
  - Cực nhanh (CDN, không compute per-request).
  - SEO tốt, cost rẻ (ít server compute).
- **Nhược điểm:**
  - Dữ liệu "đông cứng" tại thời điểm build. Muốn cập nhật phải rebuild lại.
  - Với số lượng page cực lớn (e-commerce, multi-locale) → build time rất lâu.
- **Khi dùng:**
  - Blog, docs, marketing, landing pages – nội dung ít đổi.
  - Kết hợp với **CSR** để load phần động (ví dụ: section reviews load sau).

#### 3.3 ISR – Incremental Static Regeneration

- ISR là **SSG + revalidate** → giống chiến lược cache `stale-while-revalidate`:
  - Request 1: nếu chưa có, server generate HTML, cache lại.
  - Các request sau: nhận **bản cached** (rất nhanh).
  - Sau `revalidate` seconds, request tiếp theo sẽ kích hoạt **rebuild nền**.
- **Ý nghĩa kiến trúc:**
  - Đem lại **cảm giác tĩnh** (nhanh, rẻ) nhưng vẫn có thể **cập nhật định kỳ**.
  - Phù hợp e-commerce, listing, content cập nhật mỗi vài phút/giờ.

#### 3.4 CSR – Client-Side Rendering

- HTML ban đầu gần như rỗng (hoặc shell), JS tải về rồi **tự fetch data** và render.
- **Ưu điểm:**
  - Rất linh hoạt phía client; data fetching tự quản, không phụ thuộc server render.
  - Dùng tốt cho **trang private**, dashboard nội bộ (SEO không phải ưu tiên).
- **Nhược điểm:**
  - SEO kém nếu không có SSR/SSG.
  - TTFB có thể nhanh, nhưng **Time To Interactive** lâu do phải tải JS.

**Câu nói Senior-friendly:**

> "Next.js cho phép mình **chọn chiến lược render phù hợp từng trang**, không cố nhét tất cả vào SSR hay CSR. Điều này quan trọng ở quy mô lớn, vì mỗi trang có profile khác nhau: marketing cần SEO/TTFB, dashboard cần data realtime, blog cần chi phí vận hành thấp."

---

### 4. App Router & Server Components – Khác biệt tư duy so với Pages Router

#### 4.1 Pages Router (cũ)

- Mỗi file trong `pages/` là 1 route.
- Data fetching thông qua `getServerSideProps`, `getStaticProps`, `getInitialProps`.
- Mọi component **mặc định là Client Component** → hầu hết logic chạy client, server chủ yếu render HTML ban đầu.

#### 4.2 App Router (mới, Next 13+)

- Cấu trúc theo thư mục `app/`, hỗ trợ:
  - Nested layouts, loading, error, parallel routes,…
  - `page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx` per segment.
- **Mặc định là Server Components**:
  - Component chạy trên server, có thể `async/await` trực tiếp, không cần `getServerSideProps`.
  - Không ship JS xuống client cho các phần không cần interactivity.
- Khi cần interactivity → thêm `'use client'` lên đầu file để khai báo Client Component.

**Tác động kiến trúc:**

- Có thể **đưa data fetching và business logic lên server**, để client chủ yếu lo UI interaction.
- Giảm **bundle size** đáng kể cho các trang nhiều nội dung tĩnh.
- Dễ phân chia **boundary** giữa phần "pure UI" và phần "interactive widget".

---

### 5. Server Components vs Client Components – Giải thích kiểu Lead

**Server Component:**

- Chạy **chỉ trên server**:
  - Không có `useState`, `useEffect`, không event handler (`onClick`).
  - Có thể gọi DB trực tiếp, gọi internal API, đọc secret,… an toàn.
- Khi render xong, Next.js chỉ gửi **HTML + payload tối thiểu**, không gửi logic JS tương ứng.

**Client Component:**

- Khai báo `'use client'`.
- Giống React truyền thống:
  - Dùng hook, event handler, browser APIs.
  - Component được ship JS xuống client để hydrate và chạy.

**Cách nói Senior:**

> "Mình cố gắng giữ **nhiều component nhất có thể là Server Component**, chỉ đẩy những phần thật sự cần interaction thành Client Component. Điều này giúp **giảm JS** gửi xuống, giảm chi phí hydrate, cải thiện **First Load JS** và **memory footprint** trên máy người dùng."

Ví dụ pattern:

- `ProductPage` (Server): fetch product, render nội dung tĩnh.
- `AddToCartButton` (Client): chỉ là 1 nút với state và gọi Server Action/API.

---

### 6. Data fetching & caching – Góc nhìn kiến trúc

Với App Router:

- `fetch` trên server có **cơ chế cache tích hợp** (phụ thuộc version Next.js), có thể:
  - `cache: 'force-cache'` (SSG-like).
  - `next: { revalidate: 10 }` (ISR-like).
  - `cache: 'no-store'` (SSR-like, luôn fresh).
- Có `cache()` để **dedupe** nhiều lần gọi cùng 1 hàm data.

Senior nên nói thêm về:

- **Chiến lược cache** cho từng loại data (config, danh mục, user session,…).
- **Invalidation**:
  - Dùng `revalidatePath`, `revalidateTag` (Server Actions/route handlers) sau khi mutate dữ liệu.
- **Streaming + Suspense**:
  - Thay vì chờ tất cả data xong mới render, dùng streaming để gửi shell + skeleton trước, rồi stream phần nặng sau.

---

### 7. Next.js qua các version (14/15/16) – những điểm Senior cần biết

- **Next.js 14:**

  - Server Actions stable, App Router mature.
  - Turbopack dev mode (nhanh hơn Webpack đáng kể).
  - Partial Prerendering ở mức preview.

- **Next.js 15:**

  - Cập nhật lên React 19 (RC), hỗ trợ React Compiler.
  - **Breaking change** về request APIs (`cookies`, `headers` trở thành async) và **caching mặc định** (không cache trừ khi opt-in).
  - Turbopack dev mode trở nên ổn định.

- **Next.js 16 (dự kiến):**
  - Turbopack cho production build.
  - Partial Prerendering stable → shell tĩnh, nội dung động stream.
  - React Compiler **bật mặc định**, giảm need cho `useMemo`/`useCallback` thủ công.

Khi trả lời phỏng vấn, bạn không cần thuộc từng release note, nhưng nên thể hiện:

- Bạn **nhận thức được breaking changes** (ví dụ caching behavior từ 14 → 15).
- Bạn hiểu **xu hướng**: đưa nhiều hơn về server (Server Components, Actions, PPR), giảm JS client, tăng streaming.

---

### 8. Kết luận – Câu chốt để ghi điểm Senior/Lead

Bạn có thể kết lại câu trả lời kiểu:

> "Ở vai trò Senior/Tech Lead, khi dùng Next.js mình không chỉ nghĩ ở mức 'framework React hỗ trợ SSR', mà coi nó như **application runtime** cho cả frontend lẫn một phần backend (API routes, Server Actions). Mình thiết kế app theo hướng:
>
> - Chia nhỏ theo route, chọn **chiến lược render phù hợp** từng page (SSR/SSG/ISR/CSR).
> - Tách **Server Components** cho phần hiển thị và data fetching, chỉ dùng **Client Components** cho interaction.
> - Xây **chiến lược caching & revalidation rõ ràng**, tận dụng ISR, revalidatePath/Tag, streaming, PPR.
> - Tận dụng các tối ưu built-in (image/font, middleware, edge) để cân bằng giữa **SEO, UX và chi phí vận hành**."

Điểm quan trọng là: **bạn nói được trade-off và decision-making**, chứ không chỉ liệt kê API của Next.js.
