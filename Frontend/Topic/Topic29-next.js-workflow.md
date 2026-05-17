# ▲ Topic 29: Next.js Workflow - App Router, Rendering, Data Fetching, Caching & Production Architecture

## 1. ⭐ Senior/Staff Summary

Next.js là React framework cho production: routing, rendering, data fetching, caching, image/font optimization, API/Route Handlers, middleware, metadata/SEO, streaming và deployment workflow. Ở mức senior/staff, điểm quan trọng không phải “Next.js có SSR”, mà là **biết chọn rendering/caching boundary đúng cho từng route**.

Các key cần nắm:

- 🧱 **Rendering modes:** SSR, SSG, ISR, CSR, Streaming SSR, Partial Prerendering/Cache Components.
- 🗂️ **Routing:** Pages Router cũ vs App Router mới, layouts, pages, loading, error, route handlers, dynamic routes.
- 🧩 **Server vs Client Components:** server-first by default, chỉ dùng client boundary khi cần interactivity/browser APIs.
- 🔌 **Data fetching:** fetch trong Server Components, client fetching với SWR/TanStack Query, parallel vs sequential, streaming với Suspense.
- 🗄️ **Caching:** static shell, data cache, route cache, router cache, `revalidatePath`, `revalidateTag`, `use cache`/Cache Components.
- 🔎 **SEO:** Metadata API, canonical, Open Graph, sitemap, robots, structured data.
- ⚡ **Performance:** image/font optimization, dynamic import, route prefetch, bundle boundaries, edge/server runtime tradeoffs.
- 💧 **Hydration:** mismatch, `use client` overuse, browser-only APIs, server/client data drift.
- 🧭 **Version awareness:** Next 13 App Router/RSC, Next 14 stabilization/PPR experiments, Next 15 caching changes, Next 16 Cache Components.

> 🔥 Senior point: Next.js performance tốt đến từ **ít client JS hơn**, **cache đúng dữ liệu public**, **stream đúng phần dynamic**, và **không biến mọi component thành Client Component**.

## 2. 🧠 Key Mental Model or Key Points

```txt
Request
  -> Middleware? redirects/rewrites/auth hints
  -> Route segment tree: layout/page/loading/error
  -> Server Components fetch data/render RSC payload
  -> HTML/RSC stream to browser
  -> Client Components hydrate where needed
  -> Router Cache speeds client navigation
```

Mental models:

- **App Router is server-first:** `app/page.tsx` và `layout.tsx` mặc định là Server Components.
- **Server Component không gửi JS component đó xuống client:** tốt cho content/data-heavy UI.
- **Client Component là boundary:** chỉ thêm `'use client'` khi cần state, effects, event handlers, browser APIs.
- **Rendering mode là per-route/per-segment decision:** không chọn SSR/CSR cho toàn app một cách máy móc.
- **Caching là explicit architecture decision:** dữ liệu public cache được; dữ liệu user/account/payment thường `no-store`.
- **HTML visible khác fully interactive:** SSR/streaming giúp thấy content sớm nhưng Client Components vẫn cần hydration.
- **Route Handlers không phải backend đầy đủ:** tốt cho BFF/light API, nhưng domain backend lớn vẫn nên tách service rõ ràng.

## 3. 📚 Main Concepts

### 3.1. 🧱 Rendering Methods: SSR, SSG, ISR, CSR

| Mode | Render khi nào? | Dùng cho | Tradeoff |
|---|---|---|---|
| SSR | Mỗi request | Dynamic SEO page, personalized nhẹ | TTFB/server load cao hơn |
| SSG | Build time | Docs, blog, marketing | Data stale đến lần build sau |
| ISR | Static + revalidate | Product/category/news public | Có thể stale trong thời gian ngắn |
| CSR | Client sau khi JS chạy | Dashboard sau login, app tương tác nhiều | SEO/initial content yếu hơn |
| Streaming SSR | Server gửi HTML từng phần | Page có data chậm từng vùng | Cần loading boundary tốt |

App thực tế thường hybrid:

```txt
/                    -> SSG
/blog/[slug]         -> SSG/ISR
/products/[id]       -> ISR hoặc SSR theo freshness
/search              -> SSR
/dashboard           -> CSR hoặc SSR shell + client data
/checkout            -> dynamic, private, no-store
```

### 3.2. 🗂️ Pages Router vs App Router

| Tiêu chí | Pages Router | App Router |
|---|---|---|
| Folder | `pages/` | `app/` |
| Data fetching | `getServerSideProps`, `getStaticProps` | async Server Components, `fetch`, Server Actions |
| Component model | Client-rendered React pages | Server Components mặc định |
| Layout | `_app`, custom layout patterns | nested `layout.tsx` |
| Loading/error | tự implement nhiều hơn | `loading.tsx`, `error.tsx`, `not-found.tsx` |
| API | `pages/api/*` | `app/api/*/route.ts` |
| Streaming/Suspense | hạn chế hơn | first-class |

App Router file conventions:

```txt
app/
  layout.tsx
  page.tsx
  loading.tsx
  error.tsx
  not-found.tsx
  products/
    [id]/
      page.tsx
  api/
    health/
      route.ts
```

### 3.3. 🧩 Server Components vs Client Components

Server Component phù hợp cho:

- Fetch data từ DB/API nội bộ.
- Render content/SEO.
- Dùng secret/server-only code.
- Giảm client bundle.
- Static hoặc cached UI.

Client Component cần khi:

- `useState`, `useEffect`, `useReducer`.
- Event handlers: `onClick`, `onChange`.
- Browser APIs: `window`, `localStorage`, geolocation.
- Interactive widgets: form, modal, dropdown, carousel.

Example:

```tsx
// app/products/[id]/page.tsx - Server Component
import { AddToCartButton } from "./AddToCartButton";

export default async function ProductPage({ params }: { params: { id: string } }) {
  const product = await getProduct(params.id);

  return (
    <main>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <AddToCartButton productId={product.id} />
    </main>
  );
}
```

```tsx
// AddToCartButton.tsx - Client Component
"use client";

export function AddToCartButton({ productId }: { productId: string }) {
  const [pending, setPending] = React.useState(false);

  return (
    <button disabled={pending} onClick={() => addToCart(productId, setPending)}>
      Add to cart
    </button>
  );
}
```

> ⚠️ Khi một file có `'use client'`, các imports bên dưới boundary đó cũng vào client graph nếu được dùng bởi component đó. Đừng đặt `'use client'` ở layout/root nếu không cần.

### 3.4. 🔌 Data Fetching Patterns

Server Component fetching:

```tsx
export default async function Page() {
  const [products, categories] = await Promise.all([
    getProducts(),
    getCategories(),
  ]);

  return <ProductGrid products={products} categories={categories} />;
}
```

Avoid sequential waterfall:

```tsx
// ❌ chậm nếu không cần phụ thuộc nhau
const user = await getUser();
const orders = await getOrders();

// ✅ song song
const [user, orders] = await Promise.all([getUser(), getOrders()]);
```

Client fetching:

```tsx
"use client";

function PortfolioWidget() {
  const { data, isLoading } = useQuery({
    queryKey: ["portfolio"],
    queryFn: fetchPortfolio,
    refetchInterval: 10_000,
  });

  if (isLoading) return <Skeleton />;
  return <Portfolio data={data} />;
}
```

Decision:

- Server fetch cho SEO/content initial.
- Client fetch cho realtime, user interaction, polling, highly personalized widgets.
- Server Action cho mutation gần form/action boundary.
- Route Handler/BFF khi cần endpoint cho client hoặc integrate third-party safely.

### 3.5. 🗄️ Caching và Revalidation

Next.js caching model đã thay đổi qua các version, nên cần nói chính xác theo context. Trong docs App Router hiện tại, `fetch` không tự cache mặc định; bạn cache rõ bằng option hoặc API tương ứng.

Patterns:

```tsx
// Cache data
await fetch("https://api.example.com/products", {
  cache: "force-cache",
});

// Revalidate theo thời gian
await fetch("https://api.example.com/products", {
  next: { revalidate: 60 },
});

// Luôn fresh, không cache shared data
await fetch("https://api.example.com/account", {
  cache: "no-store",
});
```

Revalidate:

```ts
import { revalidatePath, revalidateTag } from "next/cache";

revalidatePath("/products");
revalidateTag("products");
```

Cache Components / Next 16 direction:

```ts
// next.config.ts
const nextConfig = {
  cacheComponents: true,
};

export default nextConfig;
```

Với Cache Components, bạn explicit cache bằng `use cache`, `cacheTag`, `cacheLife` ở scope phù hợp. Ý tưởng là mix static shell, cached content và dynamic content trong cùng route.

> 🔒 Cẩn thận: Account, order, payment, portfolio, admin data thường không được public cache. Dùng `no-store`, private cache hoặc user-scoped cache rõ ràng.

### 3.6. 🌊 Streaming SSR và Suspense

Streaming giúp server gửi shell trước, data chậm stream sau.

```tsx
import { Suspense } from "react";

export default function ProductPage() {
  return (
    <>
      <ProductHeader />
      <Suspense fallback={<ReviewsSkeleton />}>
        <Reviews />
      </Suspense>
    </>
  );
}
```

Good loading state:

- Có skeleton đúng kích thước để tránh CLS.
- Không spinner toàn page nếu chỉ một vùng chậm.
- Error boundary theo segment/widget.
- Không stream dữ liệu private vào cached shell sai cách.

### 3.7. ⚙️ Server Actions và Route Handlers

Server Actions dùng cho mutation từ form/component boundary.

```tsx
// app/actions.ts
"use server";

export async function updateProfile(formData: FormData) {
  const name = String(formData.get("name") ?? "");
  await saveProfile({ name });
}
```

```tsx
import { updateProfile } from "./actions";

export function ProfileForm() {
  return (
    <form action={updateProfile}>
      <input name="name" />
      <button type="submit">Save</button>
    </form>
  );
}
```

Route Handler:

```ts
// app/api/health/route.ts
export async function GET() {
  return Response.json({ ok: true });
}
```

Use Route Handlers for:

- Webhooks.
- BFF endpoints.
- Health checks.
- Third-party API proxy with server-side secrets.

Security notes:

- Validate input server-side.
- Check auth/session.
- Add CSRF/rate limit for sensitive mutations.
- Never expose secrets to Client Components.

### 3.8. 🛡️ Middleware và Edge Runtime

Middleware chạy trước route handler/page response, phù hợp cho:

- Redirects/rewrites.
- Locale routing.
- Lightweight auth checks.
- A/B routing.
- Header manipulation.

Không phù hợp cho:

- Heavy DB query.
- Large body parsing.
- Complex business logic.
- Long-running tasks.

Edge Runtime:

- Latency thấp gần user.
- Runtime APIs hạn chế hơn Node.
- Cold start/region/data access cần cân nhắc.

### 3.9. 🔎 SEO và Metadata

Metadata API:

```tsx
export async function generateMetadata({ params }: { params: { id: string } }) {
  const product = await getProduct(params.id);

  return {
    title: product.name,
    description: product.summary,
    openGraph: {
      title: product.name,
      images: [product.imageUrl],
    },
  };
}
```

SEO checklist:

- Unique `title`/`description`.
- Canonical URL.
- Open Graph/Twitter cards.
- Sitemap và robots.
- Structured data khi phù hợp.
- Content có trong HTML cho public SEO page.
- Avoid hydration-only content cho nội dung cần crawl.

### 3.10. 🖼️ Image, Font và Bundle Optimization

`next/image` giúp resize, lazy load, responsive sizes, format optimization.

```tsx
import Image from "next/image";

<Image
  src={product.imageUrl}
  alt={product.name}
  width={800}
  height={600}
  sizes="(min-width: 1024px) 33vw, 100vw"
  priority={isHeroImage}
/>;
```

`next/font` giúp giảm layout shift và tránh external font request runtime tùy cấu hình.

Dynamic import:

```tsx
import dynamic from "next/dynamic";

const Chart = dynamic(() => import("./Chart"), {
  loading: () => <ChartSkeleton />,
  ssr: false,
});
```

Use `ssr: false` chỉ khi component phụ thuộc browser-only APIs hoặc quá interactive; đừng dùng để né bug SSR mà không hiểu nguyên nhân.

### 3.11. 💧 Hydration và Hydration Mismatch

Hydration mismatch xảy ra khi HTML server khác render đầu tiên trên client.

Nguyên nhân:

- `Date.now()`, `Math.random()` trong render.
- Đọc `window`, `localStorage`, `navigator` trong render server.
- Locale/timezone khác.
- Feature flag server/client khác.
- Data server/client drift.

Fix:

- Render deterministic output.
- Dùng `useEffect` cho browser-only logic.
- Đưa theme/locale/auth từ cookie/header vào server render nếu ảnh hưởng UI đầu tiên.
- Tách Client Component nhỏ, không biến cả page thành client.

### 3.12. 🧭 Next.js 14 vs 15 vs 16 - điểm senior cần biết

| Version | Điểm cần nhớ |
|---|---|
| Next 13 | App Router, Server Components, layouts, streaming bắt đầu phổ biến |
| Next 14 | App Router ổn định hơn, Partial Prerendering thử nghiệm, Server Actions phát triển |
| Next 15 | Caching semantics thay đổi theo hướng explicit hơn; cần đọc migration guide khi upgrade |
| Next 16 | Cache Components/`cacheComponents` gom PPR/useCache/dynamicIO theo hướng explicit cached/dynamic boundaries |

> ⚠️ Đừng trả lời version theo trí nhớ cũ. Với Next.js, caching/version behavior thay đổi nhanh; khi migration production phải đọc official release notes và migration guide.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Route architecture cho app e-commerce

```txt
/                         -> SSG static shell
/products/[slug]          -> ISR 60s + product tag revalidation
/search                   -> SSR, short cache by query
/account                  -> dynamic no-store, auth required
/checkout                 -> dynamic no-store, auth + CSRF
/admin                    -> dynamic, role-based access
/api/webhooks/payment     -> Route Handler, signature verification
```

### 4.2. ✅ Server Component fetch + Client Component interaction

```tsx
// app/products/[id]/page.tsx
export default async function Page({ params }: { params: { id: string } }) {
  const product = await fetchProduct(params.id);

  return (
    <>
      <ProductDetails product={product} />
      <AddToCart productId={product.id} />
    </>
  );
}
```

```tsx
// AddToCart.tsx
"use client";

export function AddToCart({ productId }: { productId: string }) {
  const [pending, setPending] = React.useState(false);

  return (
    <button disabled={pending} onClick={() => addToCart(productId, setPending)}>
      Add to cart
    </button>
  );
}
```

### 4.3. ✅ Cache tags sau mutation

```ts
"use server";

import { revalidateTag } from "next/cache";

export async function updateProductPrice(productId: string, price: number) {
  await db.product.update({ where: { id: productId }, data: { price } });
  revalidateTag(`product:${productId}`);
  revalidateTag("products");
}
```

### 4.4. ✅ Avoid hydration mismatch với theme

```tsx
"use client";

export function ClientThemeLabel() {
  const [theme, setTheme] = React.useState<string | null>(null);

  React.useEffect(() => {
    setTheme(window.localStorage.getItem("theme") ?? "light");
  }, []);

  return <span>{theme ?? "..."}</span>;
}
```

Nếu theme ảnh hưởng toàn layout, tốt hơn là đọc từ cookie trên server để render đúng ngay từ đầu.

### 4.5. ✅ Middleware auth redirect nhẹ

```ts
import { NextRequest, NextResponse } from "next/server";

export function middleware(request: NextRequest) {
  const session = request.cookies.get("session");

  if (!session && request.nextUrl.pathname.startsWith("/account")) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/account/:path*"],
};
```

> Middleware check chỉ là lớp sớm. API/server page vẫn phải verify session thật.

## 5. 🏭 Production Notes / React Implications

- **Keep server/client boundary small:** Đặt `'use client'` càng thấp càng tốt.
- **Cache by data sensitivity:** Public content cache được; user/payment/account data không public cache.
- **Avoid waterfalls:** Fetch song song, preload data khi hợp lý, dùng Suspense boundary.
- **Hydration cost matters:** Client Components quá rộng làm JS bundle và INP xấu.
- **Route Handlers are server code:** validate input, auth, rate limit, không leak secret.
- **Middleware is not business layer:** dùng cho routing/auth hint nhẹ, không query nặng.
- **SEO needs real HTML:** Public SEO content không nên chỉ render sau `useEffect`.
- **Images/fonts affect Web Vitals:** dùng `next/image`, `next/font`, dimensions, priority đúng.
- **Observability:** log server errors, cache hit/miss, route latency, Web Vitals.
- **Migration:** Next version/caching behavior thay đổi; upgrade cần test route rendering/caching rõ.

## 6. ⚠️ Common Pitfalls

- ❌ Thêm `'use client'` vào page/layout quá cao, làm mất lợi ích Server Components.
- ❌ Fetch data trong `useEffect` cho page public cần SEO.
- ❌ Cache nhầm dữ liệu private như account/order/payment.
- ❌ Không hiểu `fetch` cache/revalidate semantics theo version đang dùng.
- ❌ Dùng `ssr: false` để che hydration bug.
- ❌ Đọc `window/localStorage` trong Server Component.
- ❌ Sequential data fetching gây waterfall.
- ❌ Middleware làm logic nặng hoặc query DB phức tạp.
- ❌ Route Handler thiếu validation/auth/rate limit.
- ❌ Không dùng `next/image` cho ảnh lớn/LCP.
- ❌ Metadata duplicate hoặc thiếu canonical/Open Graph.
- ❌ Không test hydration mismatch trước production.

## 7. ✅ Decision Guide or Checklist

### Chọn rendering/data strategy nào?

| Nhu cầu | Chọn | Trả lời ngắn |
|---|---|---|
| Blog/docs/landing ít đổi | SSG | Nhanh, cache CDN tốt |
| Product/category public đổi định kỳ | ISR/revalidate | Gần static speed, dữ liệu cập nhật định kỳ |
| Search/public personalized nhẹ | SSR | Data theo request, SEO tốt |
| Dashboard sau login | CSR hoặc dynamic SSR shell | SEO ít quan trọng, data theo user |
| Checkout/payment/account | Dynamic `no-store` | Tránh cache private data |
| Widget interactive | Client Component nhỏ | Chỉ hydrate phần cần tương tác |
| Data chậm một vùng | Suspense + Streaming | Shell hiện trước, vùng chậm stream sau |
| Mutation form | Server Action hoặc Route Handler | Validate/auth server-side |
| Public asset/image | `next/image`, CDN cache | Tối ưu LCP/bandwidth |

### Checklist trước khi merge Next.js route

| Câu hỏi | Trả lời ngắn |
|---|---|
| Route này public hay private? | Public có thể cache/SEO; private cần auth/no-store. |
| Data cần fresh cỡ nào? | Realtime dùng dynamic; chấp nhận stale thì ISR/cache. |
| Có đặt `'use client'` quá cao không? | Đưa xuống component nhỏ nhất cần interactivity. |
| Có browser API trong server render không? | Chuyển vào Client Component/`useEffect` hoặc lấy từ request. |
| Fetch có waterfall không? | Dùng `Promise.all` hoặc preload khi không phụ thuộc nhau. |
| Cache có leak dữ liệu user không? | Kiểm tra `no-store`, private cache, user-scoped cache. |
| Metadata/OG/canonical đủ chưa? | Cần cho public SEO/social page. |
| Ảnh LCP đã tối ưu chưa? | `next/image`, size đúng, priority/fetch priority hợp lý. |
| Route Handler có validation/auth chưa? | Không tin input client. |
| Hydration mismatch có test chưa? | Test Date/random/locale/theme/feature flag. |

## 8. 🗣️ Short Interview Answer

Theo em, Next.js là React framework giúp mình chọn rendering và caching theo từng route thay vì tự build toàn bộ hạ tầng SSR/SSG. Với page public cần SEO như product/blog, em ưu tiên SSG/ISR/SSR tùy độ fresh của data. Với dashboard sau login hoặc widget realtime, em có thể dùng CSR hoặc Client Component nhỏ vì SEO không phải mục tiêu chính.

Điểm quan trọng trong App Router là Server Components mặc định. Em sẽ fetch data và render phần static/content ở server để giảm client JS, chỉ dùng `'use client'` cho phần cần state, effects, event handlers hoặc browser APIs. Về caching, em không cache theo cảm tính: public data có thể dùng `force-cache`, `revalidate`, tag/path revalidation; user/account/payment thì dynamic hoặc `no-store`.

Khi thiết kế production Next.js app, em chú ý hydration mismatch, streaming/Suspense boundary, metadata SEO, image/font optimization, route handlers có auth/validation, middleware chỉ làm logic nhẹ, và đo Web Vitals/server latency. Với Next version mới, đặc biệt caching và Cache Components, em luôn đọc migration docs vì behavior thay đổi khá nhanh.

## 9. 🧾 Ghi nhớ nhanh

- App Router mặc định Server Components.
- `'use client'` tạo client boundary; đặt càng thấp càng tốt.
- Server Component không dùng hooks/browser APIs.
- Client Component dùng cho interactivity.
- SSR render mỗi request; SSG build time; ISR static + revalidate; CSR render ở browser.
- Streaming gửi HTML từng phần qua Suspense boundary.
- Public data có thể cache; private user data phải cẩn thận `no-store`.
- `fetch` caching semantics phụ thuộc version/config; đừng đoán.
- `next/image` và `next/font` ảnh hưởng LCP/CLS.
- Hydration mismatch thường do Date/random/window/localStorage/data drift.
- Middleware không thay thế authorization ở server/API.
- Route Handlers cần validation, auth, rate limit.

## 10. 📖 Giải thích các thuật ngữ trong topic

- `Next.js`: React framework cho routing, rendering, caching và production optimizations.
- `Pages Router`: Router cũ dựa trên thư mục `pages/`.
- `App Router`: Router mới dựa trên thư mục `app/`, hỗ trợ Server Components/layouts/streaming.
- `Server Component`: Component render trên server, không gửi JS component đó xuống client.
- `Client Component`: Component chạy/hydrate trên client, dùng được hooks/events/browser APIs.
- `SSR`: Server-Side Rendering, render HTML mỗi request.
- `SSG`: Static Site Generation, render HTML lúc build.
- `ISR`: Incremental Static Regeneration, static page có revalidate.
- `CSR`: Client-Side Rendering, render UI sau khi JS chạy trong browser.
- `Hydration`: Client JS gắn interactivity vào HTML server-rendered.
- `Streaming SSR`: Gửi HTML/RSC payload từng phần thay vì chờ xong tất cả.
- `Suspense`: React boundary cho loading/streaming async UI.
- `Route Handler`: Endpoint server trong `app/api/*/route.ts`.
- `Server Action`: Function server dùng cho mutation/form/action.
- `Middleware`: Code chạy trước route response để redirect/rewrite/header/auth hint.
- `Edge Runtime`: Runtime gần user hơn nhưng API hạn chế hơn Node.js.
- `Metadata API`: API khai báo/generate SEO metadata.
- `Data Cache`: Cache kết quả data fetching phía server.
- `Router Cache`: Cache RSC payload cho client-side navigation.
- `Revalidation`: Làm mới cache theo thời gian, path hoặc tag.
- `Cache Components`: Next 16 opt-in model cho cached/dynamic component boundaries.
- `PPR`: Partial Prerendering, static shell + dynamic streamed content.

## 11. 📚 Nguồn chính thức đã đối chiếu

- Next.js App Router docs: <https://nextjs.org/docs/app>
- Server and Client Components: <https://nextjs.org/docs/app/building-your-application/rendering/server-components>
- Fetching Data: <https://nextjs.org/docs/app/getting-started/fetching-data>
- Caching and Revalidating: <https://nextjs.org/docs/app/building-your-application/data-fetching/caching>
- Cache Components / `cacheComponents`: <https://nextjs.org/docs/app/getting-started/cache-components>
