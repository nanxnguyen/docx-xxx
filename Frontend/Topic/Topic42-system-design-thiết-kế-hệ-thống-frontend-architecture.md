# 🏗️ Topic42: System Design - Frontend Architecture

> Mục tiêu: biết cách thiết kế một hệ thống frontend production-ready: dễ scale team, scale traffic, debug được production, kiểm soát performance, bảo mật, deployment và tradeoff kiến trúc.

---

## ⭐ Senior/Staff Summary

Frontend system design không chỉ là chọn React, Next.js hay Vite. Đây là bài toán thiết kế toàn bộ frontend platform để đáp ứng:

- ✅ **Scalability**: scale traffic, scale team, scale repo, scale deployment.
- ✅ **Performance**: fast initial load, Core Web Vitals tốt, bundle hợp lý, cache tốt.
- ✅ **Reliability**: error boundary, retry, fallback, graceful degradation.
- ✅ **Maintainability**: feature ownership rõ, module boundary rõ, coding standards.
- ✅ **Security**: auth, token handling, CSP, XSS, dependency risk, env var leak.
- ✅ **Observability**: logs, metrics, tracing, RUM, alerting.
- ✅ **Delivery**: CI/CD, preview deploy, rollback, feature flags.

Một kiến trúc frontend production thường có các lớp:

```txt
Browser / Client
→ CDN / Edge
→ Frontend App: React / Next.js / Microfrontend / SPA
→ API Layer: BFF / GraphQL / REST Gateway
→ Server State Cache: React Query / SWR / Apollo
→ Client State: Zustand / Redux / Context / URL state
→ Observability: Sentry / Datadog / OpenTelemetry / Web Vitals
```

Key tradeoff:

- **Modular monolith** trước, microfrontend sau khi team/deploy thật sự cần.
- **Monorepo** tốt cho shared code và ownership, nhưng cần tooling/cache/CI tốt.
- **BFF** tốt khi frontend cần API đúng shape, nhưng thêm một layer vận hành.
- **GraphQL** tốt cho flexible querying, nhưng cần schema governance/cache/error handling.
- **SSR/Streaming/ISR** tốt cho SEO/perceived performance, nhưng tăng complexity.
- **Feature flags** giúp rollout an toàn, nhưng phải có lifecycle cleanup.

> 💡 Senior key: **Architecture tốt là architecture tiến hóa theo pain point thật, không phải architecture nhiều công nghệ nhất.**

---

## 🧠 Key Mental Model

### 1. Frontend system design là thiết kế constraints

Khi nhận đề bài system design frontend, đừng nhảy ngay vào folder structure. Hãy hỏi:

- Người dùng là ai, traffic bao nhiêu?
- App cần SEO hay chỉ internal dashboard?
- Critical flows là gì: login, checkout, editor, search, payment?
- SLA/SLO cần đạt: uptime, latency, error rate?
- Team size và ownership thế nào?
- Deploy frequency có độc lập giữa teams không?
- Data realtime hay eventual consistency?
- Offline support có cần không?
- Security/compliance có nhạy cảm không?

Ví dụ:

- Landing page marketing:
  - ưu tiên SEO, performance, CDN, SSG/ISR.

- Admin dashboard:
  - ưu tiên auth, RBAC, data table, caching, observability.

- E-commerce homepage:
  - ưu tiên CDN, personalization, image optimization, A/B testing, Core Web Vitals.

- Google Docs clone:
  - ưu tiên realtime collaboration, conflict resolution, offline recovery, latency.

---

### 2. Scale frontend có 4 loại

- **Scale traffic**
  - CDN, edge caching, code splitting, SSR/SSG/ISR, image optimization.

- **Scale team**
  - module boundary, monorepo, design system, ownership, lint rules, ADR.

- **Scale deployment**
  - CI/CD, preview deploy, feature flags, canary, rollback, microfrontend khi cần.

- **Scale debugging**
  - source maps, release id, RUM, logs, traces, error boundaries, dashboards.

> ⚠️ Nhiều người chỉ nói performance. Senior phải nói cả team ownership, release safety và production debugging.

---

## 📚 Main Concepts

### 1. Architecture styles

#### ✅ Modular Monolith

Một app frontend lớn nhưng chia feature rõ trong cùng repo/build/deploy.

Phù hợp khi:

- team nhỏ/vừa
- domain chưa quá phân mảnh
- deploy cùng lúc vẫn ổn
- muốn giảm operational complexity

Ví dụ structure:

```txt
src/
├─ app/
├─ features/
│  ├─ auth/
│  ├─ checkout/
│  ├─ catalog/
│  └─ profile/
├─ shared/
│  ├─ ui/
│  ├─ api/
│  ├─ hooks/
│  └─ utils/
└─ routes/
```

✅ Đây thường là starting point tốt nhất.

---

#### ✅ Monorepo

Một repo chứa nhiều apps/libs/packages.

Phù hợp khi:

- nhiều apps share design system, utils, API clients
- cần enforce dependency boundary
- nhiều team cùng làm nhưng muốn shared tooling
- cần task cache/incremental build

Ví dụ:

```txt
apps/
├─ web/              # React/Vite app
├─ admin/            # Admin dashboard
├─ mobile/           # React Native
└─ landing/          # Next.js marketing

packages/
├─ ui/               # Design system
├─ api-client/       # Typed API client
├─ auth/             # Auth SDK
├─ eslint-config/
└─ tsconfig/
```

Tooling:

- Nx: mạnh về dependency graph, affected commands, enforce boundaries.
- Turborepo: đơn giản, fast task cache, hợp Next.js/pnpm workspace.
- pnpm workspace: package manager/workspace foundation tốt.

⚠️ Monorepo không tự động giải quyết architecture. Nếu không có boundary, nó chỉ là một folder lớn.

---

#### ✅ Microfrontend

Microfrontend chia frontend thành các app/module có thể deploy độc lập.

Phù hợp khi:

- nhiều team sở hữu domain độc lập
- release cadence khác nhau
- app rất lớn, build/deploy chung gây bottleneck
- cần migrate legacy từng phần
- nhiều tech stack phải coexist

Không phù hợp khi:

- team nhỏ
- app chưa đủ lớn
- chỉ dùng vì “nghe hiện đại”
- chưa có observability/versioning/dependency governance tốt

Tradeoffs:

- ✅ independent deploy
- ✅ ownership rõ
- ✅ migrate legacy dễ hơn
- ⚠️ runtime integration phức tạp
- ⚠️ bundle duplication
- ⚠️ shared dependency version mismatch
- ⚠️ routing/auth/state/monitoring khó hơn

---

### 2. Module Federation

Webpack Module Federation cho phép app expose/consume module runtime.

Remote app:

```js
const { ModuleFederationPlugin } = require('webpack').container;

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'checkout',
      filename: 'remoteEntry.js',
      exposes: {
        './CheckoutApp': './src/CheckoutApp',
      },
      shared: {
        react: { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true, requiredVersion: '^18.0.0' },
      },
    }),
  ],
};
```

Host app:

```js
new ModuleFederationPlugin({
  name: 'shell',
  remotes: {
    checkout: 'checkout@https://cdn.example.com/checkout/remoteEntry.js',
  },
});
```

Usage:

```tsx
import { lazy, Suspense } from 'react';

const CheckoutApp = lazy(() => import('checkout/CheckoutApp'));

export function CheckoutRoute() {
  return (
    <Suspense fallback={<div>Loading checkout...</div>}>
      <CheckoutApp />
    </Suspense>
  );
}
```

Production checklist:

- shared dependency version policy
- fallback khi remote fail
- Sentry release theo remote
- CSP allowlist cho remote URL
- rollback/canary theo remote
- contract test giữa shell và remote

---

### 3. Microfrontend communication

Communication nên giữ loose coupling.

Các cách phổ biến:

- **URL/route**
  - Tốt cho navigation, filters, selected tab.
  - Dễ bookmark/share.

- **Custom events**
  - Tốt cho event nhẹ giữa apps.
  - Cần typed event contract.

- **Shared store**
  - Chỉ dùng cho state cross-cutting thật sự như auth/theme.
  - Cẩn thận coupling.

- **API/backend**
  - Tốt nhất cho domain data.
  - Tránh frontend remote phụ thuộc trực tiếp vào internal state của nhau.

Typed event bus:

```ts
type AppEvents = {
  'cart:item-added': { productId: string; quantity: number };
  'auth:logout': undefined;
};

export function emitEvent<TName extends keyof AppEvents>(
  name: TName,
  payload: AppEvents[TName]
) {
  window.dispatchEvent(new CustomEvent(name, { detail: payload }));
}

export function listenEvent<TName extends keyof AppEvents>(
  name: TName,
  handler: (payload: AppEvents[TName]) => void
) {
  const listener = (event: Event) => {
    handler((event as CustomEvent<AppEvents[TName]>).detail);
  };

  window.addEventListener(name, listener);

  return () => window.removeEventListener(name, listener);
}
```

---

### 4. API layer: REST, BFF, GraphQL

#### REST direct

Frontend gọi services/API gateway trực tiếp.

Phù hợp:

- API đã đúng shape frontend cần
- app nhỏ/vừa
- backend contracts ổn định

Rủi ro:

- over-fetch/under-fetch
- nhiều round trips
- frontend biết quá nhiều service internals

---

#### BFF - Backend for Frontend

BFF là backend layer thiết kế riêng cho nhu cầu frontend.

Phù hợp khi:

- frontend cần aggregate nhiều services
- cần transform data đúng view model
- cần security/session logic gần frontend
- mobile/web cần response shape khác nhau

Example:

```ts
import express from 'express';

const router = express.Router();

router.get('/dashboard', async (req, res) => {
  try {
    const [user, orders, recommendations] = await Promise.all([
      userService.getCurrentUser(req),
      orderService.getRecentOrders(req),
      recommendationService.getForUser(req),
    ]);

    res.json({
      user: {
        id: user.id,
        name: user.name,
      },
      recentOrders: orders.slice(0, 5),
      recommendations,
    });
  } catch (error) {
    res.status(500).json({
      code: 'DASHBOARD_LOAD_FAILED',
      message: 'Cannot load dashboard',
    });
  }
});
```

✅ BFF giảm complexity trong client.

⚠️ BFF thêm một service cần deploy, monitor, scale và own contract.

---

#### GraphQL

GraphQL cho client query đúng data cần.

Phù hợp khi:

- nhiều client có nhu cầu data khác nhau
- domain graph phức tạp
- muốn typed schema
- muốn giảm over-fetching

Rủi ro:

- caching phức tạp hơn REST/CDN
- N+1 query nếu resolver yếu
- schema governance cần chặt
- error partial data cần xử lý rõ

Query example:

```graphql
query Dashboard($userId: ID!) {
  user(id: $userId) {
    id
    name
    permissions
  }
  orders(userId: $userId, limit: 5) {
    id
    total
    status
  }
}
```

React usage:

```tsx
function Dashboard({ userId }: { userId: string }) {
  const { data, loading, error } = useQuery(GET_DASHBOARD, {
    variables: { userId },
  });

  if (loading) return <Skeleton />;
  if (error) return <ErrorState error={error} />;

  return <DashboardView data={data} />;
}
```

---

### 5. State management architecture

State nên chia theo ownership:

- **Server State**
  - API data, cache, loading/error, stale/refetch.
  - Tool: React Query, SWR, Apollo, RTK Query.

- **Global Client State**
  - Auth snapshot, theme, global UI, selected organization.
  - Tool: Zustand, Redux Toolkit, Jotai.

- **Local State**
  - Form input, modal local, tab local.
  - Tool: `useState`, `useReducer`.

- **URL State**
  - filter, sort, pagination, selected tab.
  - Tool: router/search params.

Layered example:

```tsx
function OrdersPage() {
  const [searchParams, setSearchParams] = useSearchParams();
  const page = Number(searchParams.get('page') ?? 1);

  const selectedOrgId = useAppStore((state) => state.selectedOrgId);

  const ordersQuery = useQuery({
    queryKey: ['orders', selectedOrgId, page],
    queryFn: () => fetchOrders({ orgId: selectedOrgId, page }),
    staleTime: 60_000,
  });

  const [selectedOrderId, setSelectedOrderId] = useState<string | null>(null);

  if (ordersQuery.isLoading) return <OrdersSkeleton />;
  if (ordersQuery.isError) return <ErrorState />;

  return (
    <OrdersTable
      orders={ordersQuery.data.items}
      selectedOrderId={selectedOrderId}
      onSelectOrder={setSelectedOrderId}
      onPageChange={(nextPage) => setSearchParams({ page: String(nextPage) })}
    />
  );
}
```

✅ Key: không nhét mọi thứ vào Redux/Zustand.

---

### 6. Rendering architecture: CSR, SSR, SSG, ISR, Streaming

Chọn rendering theo page type:

- **CSR**
  - Tốt cho dashboard/internal app.
  - SEO không phải trọng tâm.
  - Deploy đơn giản.

- **SSR**
  - Tốt cho SEO/dynamic content.
  - TTFB có thể tăng nếu server/data chậm.
  - Cần cache và error handling tốt.

- **SSG**
  - Tốt cho static marketing/docs/blog.
  - Performance tốt, CDN cache dễ.
  - Không phù hợp data thay đổi từng user.

- **ISR**
  - Static + revalidate theo thời gian.
  - Tốt cho e-commerce/catalog/news.

- **Streaming SSR**
  - Gửi HTML từng phần, cải thiện perceived performance.
  - Cần thiết kế Suspense boundary tốt.

- **Islands Architecture**
  - Static HTML là chính, chỉ hydrate component cần tương tác.
  - Tốt cho content-heavy site.

---

### 7. Performance architecture

Các lớp performance:

- **Network**
  - CDN, compression, HTTP/2/3, preconnect, preload/prefetch.

- **Bundle**
  - code splitting, tree-shaking, vendor splitting, bundle budget.

- **Rendering**
  - memoization đúng chỗ, virtualization, avoid layout shift, avoid long tasks.

- **Data**
  - caching, pagination, infinite query, request dedupe, optimistic update.

- **Media**
  - responsive images, lazy load, AVIF/WebP, image CDN.

Performance checklist:

- LCP target rõ
- CLS tránh layout shift
- INP giảm main-thread blocking
- bundle analyzer trong CI
- Core Web Vitals RUM, không chỉ Lighthouse local

---

### 8. CDN & Edge

CDN giúp cache static assets gần user.

Static asset strategy:

```txt
index.html                 → no-cache
assets/main.[hash].js      → public, max-age=31536000, immutable
assets/vendor.[hash].js    → public, max-age=31536000, immutable
images/products/[hash].webp → public, max-age=31536000, immutable
```

Edge functions phù hợp cho:

- geo routing
- A/B testing
- redirects
- auth/session lightweight checks
- personalization nhẹ
- cache key normalization

Không nên dùng edge cho:

- business transaction phức tạp
- long-running job
- logic cần database connection nặng
- secrets/governance chưa rõ

---

### 9. Resilience: Error Boundary, retry, circuit breaker

Error Boundary:

```tsx
import { Component, ErrorInfo, ReactNode } from 'react';

type Props = {
  children: ReactNode;
  fallback?: ReactNode;
};

type State = {
  hasError: boolean;
  error: Error | null;
};

export class ErrorBoundary extends Component<Props, State> {
  state: State = {
    hasError: false,
    error: null,
  };

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    Sentry.captureException(error, {
      extra: {
        componentStack: errorInfo.componentStack,
      },
    });
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ?? <div>Something went wrong.</div>;
    }

    return this.props.children;
  }
}
```

Retry với backoff:

```ts
async function retry<T>(
  fn: () => Promise<T>,
  maxAttempts = 3,
  delayMs = 300
): Promise<T> {
  let lastError: unknown;

  for (let attempt = 1; attempt <= maxAttempts; attempt += 1) {
    try {
      return await fn();
    } catch (error) {
      lastError = error;

      if (attempt === maxAttempts) break;

      await new Promise((resolve) =>
        setTimeout(resolve, delayMs * 2 ** (attempt - 1))
      );
    }
  }

  throw lastError;
}
```

Circuit breaker dùng khi service liên tục fail:

```ts
type CircuitState = 'CLOSED' | 'OPEN' | 'HALF_OPEN';

class CircuitBreaker {
  private state: CircuitState = 'CLOSED';
  private failures = 0;
  private lastFailureAt = 0;

  constructor(
    private readonly failureThreshold = 3,
    private readonly resetTimeoutMs = 10_000
  ) {}

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    if (this.state === 'OPEN') {
      const canRetry = Date.now() - this.lastFailureAt > this.resetTimeoutMs;

      if (!canRetry) {
        throw new Error('Circuit is open');
      }

      this.state = 'HALF_OPEN';
    }

    try {
      const result = await fn();
      this.state = 'CLOSED';
      this.failures = 0;
      return result;
    } catch (error) {
      this.failures += 1;
      this.lastFailureAt = Date.now();

      if (this.failures >= this.failureThreshold) {
        this.state = 'OPEN';
      }

      throw error;
    }
  }
}
```

---

### 10. Feature flags

Feature flags giúp rollout an toàn:

- gradual rollout
- A/B testing
- canary release
- kill switch
- permission-based feature
- environment-based config
- remote config với LaunchDarkly, ConfigCat, Unleash hoặc internal flag service

Simple provider:

```tsx
import { createContext, ReactNode, useContext } from 'react';

type FeatureFlags = {
  newCheckout: boolean;
  realtimeEditor: boolean;
};

const FeatureFlagContext = createContext<FeatureFlags>({
  newCheckout: false,
  realtimeEditor: false,
});

export function FeatureFlagsProvider({
  flags,
  children,
}: {
  flags: FeatureFlags;
  children: ReactNode;
}) {
  return (
    <FeatureFlagContext.Provider value={flags}>
      {children}
    </FeatureFlagContext.Provider>
  );
}

export function useFeatureFlag(name: keyof FeatureFlags) {
  return useContext(FeatureFlagContext)[name];
}
```

Usage:

```tsx
function CheckoutEntry() {
  const enabled = useFeatureFlag('newCheckout');

  return enabled ? <NewCheckout /> : <LegacyCheckout />;
}
```

⚠️ Feature flag debt:

- flag không cleanup
- logic phân nhánh quá nhiều
- test matrix phình
- flag config không audit được

Remote config production notes:

- flag cần owner và expiry date
- flag changes cần audit log
- fallback default phải an toàn khi service lỗi
- không đưa secret/business rule nhạy cảm vào client flag
- cache flag ngắn hạn để tránh blocking app startup
- critical kill switch nên có đường rollback rõ

---

### 11. Observability

Frontend observability gồm:

- **Error tracking**
  - Sentry, Bugsnag.
  - error rate, stack trace, release, user/session context.

- **RUM - Real User Monitoring**
  - Core Web Vitals, page load, route transition, INP.

- **Logs**
  - structured client logs cho critical flows.

- **Tracing**
  - frontend span nối với backend trace qua request id/trace id.

- **Synthetic monitoring**
  - scripted checks từ nhiều region.

Example:

```ts
performance.mark('checkout:start');

await submitOrder(order);

performance.mark('checkout:submitted');
performance.measure('checkout-submit', 'checkout:start', 'checkout:submitted');
```

Alert nên theo:

- error rate tăng
- API latency tăng
- checkout conversion drop
- LCP/INP vượt threshold
- remote microfrontend load fail

---

### 12. Security architecture

Frontend security cần thiết kế từ đầu:

- XSS prevention: escape output, sanitize HTML, CSP.
- Auth token: tránh lưu token nhạy cảm bừa bãi trong localStorage.
- CSRF: nếu dùng cookie auth, cần SameSite/CSRF protection.
- Env vars: chỉ expose biến public đúng prefix.
- Dependency: lockfile, audit, SCA.
- Source maps: private upload, không public nếu source nhạy cảm.
- Third-party script: SRI, CSP allowlist.
- RBAC: frontend chỉ hide UI; backend vẫn phải enforce permission.

> ⚠️ Frontend authorization chỉ là UX guard, không phải security boundary cuối.

---

### 13. Production-ready project checklist

Một frontend project từ zero đến production-ready nên có:

- Foundation:
  - TypeScript strict
  - package manager ổn định
  - env config rõ local/staging/prod
  - path alias hợp lý

- Architecture:
  - feature-based structure
  - shared UI/utils/API/types
  - import boundary
  - ADR cho quyết định lớn

- Code quality:
  - ESLint, Prettier
  - Husky/lint-staged nếu phù hợp
  - schema validation bằng Zod/Yup

- Testing:
  - unit tests cho logic
  - component tests cho UI quan trọng
  - E2E tests cho critical flows
  - contract tests cho API/microfrontend

- Performance:
  - lazy loading/code splitting
  - image optimization
  - CDN caching
  - performance budget
  - Web Vitals RUM

- CI/CD:
  - lint, type-check, test, build
  - preview deploy
  - security/dependency check
  - rollback strategy

- Monitoring:
  - Sentry/Datadog/New Relic
  - release tracking
  - source map upload
  - dashboard/alert

---

### 14. Real-world system design questions

#### Design Shopee-like homepage - 10M DAU

Requirements thường gặp:

- traffic lớn, spike theo campaign
- SEO tốt cho landing/category
- personalization theo user/region
- A/B testing banner/layout
- image-heavy, cần LCP tốt
- 99.9% uptime hoặc cao hơn

Architecture gợi ý:

```txt
User
→ CDN / Edge cache
→ Next.js / SSR + ISR for public content
→ BFF / GraphQL gateway
→ Product / Promotion / Recommendation services
→ Observability: RUM, Sentry, tracing, business metrics
```

Key decisions:

- **Rendering**
  - SSG/ISR cho category/static campaign.
  - SSR/edge personalization cho phần dynamic nhẹ.
  - CSR cho widget cá nhân hóa không critical SEO.

- **Performance**
  - image CDN, responsive images, AVIF/WebP
  - priority image cho hero
  - code splitting theo widget
  - skeleton cho recommendation/promotion
  - cache static assets dài hạn bằng content hash

- **Reliability**
  - fallback banner/default layout khi recommendation fail
  - circuit breaker cho service yếu
  - feature flags để tắt widget lỗi

- **Observability**
  - Core Web Vitals theo region/device
  - click/impression tracking
  - API error rate theo widget

---

#### Design Google Docs-like realtime editor

Requirements thường gặp:

- nhiều user edit cùng document
- low latency
- offline/reconnect
- conflict resolution
- autosave
- presence/cursor
- permission model rõ

Architecture gợi ý:

```txt
React Editor
→ Local document state
→ WebSocket/WebRTC channel
→ Collaboration service
→ CRDT/OT engine
→ Persistence + version history
→ Presence service
```

Key decisions:

- **Realtime protocol**
  - WebSocket phổ biến cho client-server realtime.
  - WebRTC có thể dùng cho peer-to-peer nhưng phức tạp hơn.

- **Conflict resolution**
  - OT hoặc CRDT để merge concurrent edits.
  - Không tự merge string thủ công trong production editor.

- **Offline**
  - local queue operations
  - replay khi reconnect
  - version check để tránh overwrite

- **UX**
  - show saving/saved/offline state
  - presence cursor
  - conflict/fallback messaging
  - keyboard accessibility trong editor

- **Observability**
  - reconnect rate
  - operation latency
  - dropped messages
  - save failure rate

---

## 🧪 Practical TypeScript/JavaScript Examples

### Example 1: API client boundary

```ts
type ApiError = {
  code: string;
  message: string;
  status: number;
};

async function request<T>(url: string, init?: RequestInit): Promise<T> {
  const response = await fetch(url, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...init?.headers,
    },
  });

  if (!response.ok) {
    const error = (await response.json().catch(() => null)) as Partial<ApiError> | null;

    throw {
      code: error?.code ?? 'UNKNOWN_ERROR',
      message: error?.message ?? 'Request failed',
      status: response.status,
    } satisfies ApiError;
  }

  return response.json() as Promise<T>;
}
```

✅ API boundary giúp normalize error, timeout, retry, auth, tracing.

---

### Example 2: Route-level architecture

```tsx
const ProductPage = lazy(() => import('./features/product/ProductPage'));
const CheckoutPage = lazy(() => import('./features/checkout/CheckoutPage'));
const AccountPage = lazy(() => import('./features/account/AccountPage'));

export function AppRoutes() {
  return (
    <ErrorBoundary>
      <Suspense fallback={<PageSkeleton />}>
        <Routes>
          <Route path="/products/:id" element={<ProductPage />} />
          <Route path="/checkout" element={<CheckoutPage />} />
          <Route path="/account" element={<AccountPage />} />
        </Routes>
      </Suspense>
    </ErrorBoundary>
  );
}
```

✅ Route-level split giảm initial bundle.

⚠️ Cần handle chunk load failure khi deploy.

---

### Example 3: Feature boundary trong monorepo

```ts
// packages/auth/src/index.ts
export type Session = {
  userId: string;
  orgId: string;
  permissions: string[];
};

export function can(session: Session, permission: string) {
  return session.permissions.includes(permission);
}
```

Consumer:

```ts
import { can } from '@acme/auth';

if (can(session, 'orders:read')) {
  renderOrders();
}
```

✅ Shared domain logic nằm ở package rõ owner, không copy giữa apps.

---

## ⚛️ Production Notes / React Implications

### React rendering implications

Architecture ảnh hưởng React rendering:

- Global store quá lớn → re-render rộng.
- Context value đổi thường xuyên → consumer re-render.
- Server state tự quản lý bằng Redux/Zustand → cache/refetch/error phức tạp.
- Không memoize list/table lớn → INP xấu.
- Không virtualize table lớn → main thread nghẽn.
- Hydration mismatch trong SSR → bug khó debug.

Guideline:

- co-locate state gần nơi dùng
- dùng React Query/SWR cho server state
- Zustand/Redux cho client state thật sự global
- split context theo responsibility
- dùng virtualization cho list lớn
- đo bằng React Profiler/RUM thay vì đoán

---

### SSR/Hydration

SSR giúp SEO/perceived performance, nhưng thêm rủi ro:

- server/client render khác nhau
- browser-only API chạy trên server
- auth/session data leak giữa request nếu dùng singleton store
- cache key sai làm user thấy data người khác

Checklist:

- không dùng `window`/`document` trong server render
- tạo store per request
- cache theo user/session khi cần
- serialize state an toàn
- test hydration warning trong CI nếu có thể

---

### Accessibility

System design cũng ảnh hưởng accessibility:

- route change cần focus management
- modal/toast cần trap focus/announce
- loading/error/empty state cần semantic rõ
- realtime collaboration cần announce thay đổi quan trọng
- performance lag ảnh hưởng keyboard/screen reader users

---

## ⚠️ Common Pitfalls

### ❌ 1. Over-engineering microfrontend quá sớm

Microfrontend giải quyết team/deploy scale, không phải default cho mọi app.

✅ Bắt đầu bằng modular monolith nếu pain point chưa rõ.

---

### ❌ 2. Monorepo không có boundary

Không enforce import boundary thì monorepo dễ thành spaghetti.

✅ Dùng Nx tags, ESLint boundaries, package ownership.

---

### ❌ 3. Một global store chứa mọi thứ

Server state, local form state, URL state, modal state đều nhét vào Redux/Zustand làm app khó maintain.

✅ Chia state theo ownership.

---

### ❌ 4. Không có error boundary

Một component crash có thể làm trắng cả app.

✅ Đặt error boundary theo route/section critical.

---

### ❌ 5. Không có observability

Không có Sentry/RUM/logs thì production incident chỉ dựa vào user report.

✅ Gắn release id, source maps, Web Vitals, API error tracking.

---

### ❌ 6. Cache sai

- cache HTML quá lâu
- cache API personalized ở CDN không đúng key
- không invalidate stale data

✅ Thiết kế cache theo data sensitivity và freshness requirement.

---

### ❌ 7. Feature flags không cleanup

Flag sống mãi làm code phân nhánh và test matrix phình.

✅ Mỗi flag cần owner, expiry, cleanup task.

---

### ❌ 8. Frontend tự tin quá mức về security

Ẩn button không phải permission enforcement.

✅ Backend phải enforce authorization.

---

## ✅ Decision Guide / Checklist

### Chọn architecture

- Team nhỏ/vừa, một product chính:
  - ✅ Modular monolith

- Nhiều apps share code, cần consistent tooling:
  - ✅ Monorepo

- Nhiều team deploy độc lập, app rất lớn:
  - ✅ Microfrontend

- SEO/content-heavy:
  - ✅ SSG/ISR/SSR/Islands

- Dashboard internal:
  - ✅ CSR + strong API caching + observability

- Realtime collaboration:
  - ✅ WebSocket/WebRTC/CRDT/OT + offline/reconnect strategy

---

### System design interview checklist

- ✅ Clarify requirements: users, traffic, SEO, realtime, offline, SLA.
- ✅ Pick rendering strategy: CSR/SSR/SSG/ISR/Streaming/Islands.
- ✅ Define architecture style: modular monolith/monorepo/microfrontend.
- ✅ Define API layer: REST/BFF/GraphQL.
- ✅ Define state layers: server/global/local/URL.
- ✅ Define performance plan: CDN, code splitting, image optimization, Web Vitals.
- ✅ Define reliability: error boundary, retry, fallback, circuit breaker.
- ✅ Define security: auth, XSS, CSRF, CSP, env vars.
- ✅ Define observability: Sentry, RUM, logs, traces, alerts.
- ✅ Define delivery: CI/CD, feature flags, preview, rollback.
- ✅ Explain tradeoffs and evolution path.

---

## 🗣️ Short Interview Answer

Em nghĩ frontend system design trước hết là bài toán tradeoff. Em sẽ bắt đầu bằng cách clarify yêu cầu: app cần SEO không, traffic bao nhiêu, team size thế nào, có realtime/offline không, SLA và critical flows là gì. Sau đó em mới chọn rendering strategy như CSR, SSR, SSG, ISR hoặc streaming.

Về architecture, em thường bắt đầu bằng modular monolith có boundary rõ. Nếu có nhiều apps share code hoặc nhiều team thì em cân nhắc monorepo với Nx/Turborepo. Microfrontend chỉ nên dùng khi thật sự cần independent deployment và ownership theo domain, vì nó thêm complexity về shared dependency, routing, auth, observability và runtime failure.

Em sẽ tách state theo ownership: server state dùng React Query/SWR/Apollo, global client state dùng Zustand/Redux khi cần, local state để gần component, URL state đưa lên router. API layer thì tùy bài toán: REST direct cho case đơn giản, BFF khi cần aggregate/transform data, GraphQL khi nhiều client cần query linh hoạt. Điểm em thấy quan trọng là phải có performance plan, CDN/cache, error boundaries, feature flags, CI/CD, monitoring và rollback. Architecture tốt không phải là nhiều công nghệ nhất, mà là dễ scale, dễ debug và tiến hóa được theo nhu cầu thật của team.

---

## 🧠 Ghi nhớ nhanh

- ✅ Frontend system design là tradeoff giữa scalability, performance, reliability, maintainability.
- ✅ Bắt đầu bằng requirements, không bắt đầu bằng tool.
- ✅ Modular monolith là default tốt cho nhiều team.
- ✅ Monorepo cần boundary và task cache.
- ✅ Microfrontend chỉ nên dùng khi có nhu cầu independent deploy/ownership thật.
- ✅ BFF giúp frontend nhận data đúng shape nhưng thêm vận hành.
- ✅ GraphQL mạnh nhưng cần schema governance và caching strategy.
- ✅ State phải chia server/global/local/URL.
- ✅ SSR/Streaming/ISR tốt nhưng tăng complexity.
- ✅ CDN/cache cần phân biệt HTML và hashed assets.
- ✅ Error boundary, retry, circuit breaker giúp resilience.
- ✅ Feature flags cần owner và cleanup.
- ✅ Observability là yêu cầu kiến trúc, không phải việc thêm sau cùng.
- ✅ Frontend security phải phối hợp backend, không chỉ hide UI.

---

## 📖 Giải thích các thuật ngữ trong topic

- **Frontend System Design**
  - Thiết kế kiến trúc frontend để đáp ứng performance, scale, reliability, maintainability và delivery.

- **Modular Monolith**
  - Một app deploy chung nhưng chia module/feature boundary rõ.

- **Monorepo**
  - Một repo chứa nhiều apps/packages dùng chung tooling và dependency graph.

- **Microfrontend**
  - Chia frontend thành nhiều app/module độc lập có thể deploy riêng.

- **Module Federation**
  - Webpack feature cho phép các build độc lập expose/consume module runtime.

- **BFF**
  - Backend for Frontend, API layer thiết kế riêng cho nhu cầu frontend.

- **GraphQL**
  - Query language/API runtime cho phép client lấy đúng data cần qua typed schema.

- **Server State**
  - Data đến từ server/API, cần cache/refetch/loading/error handling.

- **Global Client State**
  - State client cần share nhiều nơi, như theme/auth snapshot/global UI.

- **URL State**
  - State nằm trong URL như filter, sort, pagination, selected tab.

- **CSR**
  - Client-Side Rendering, browser render UI chủ yếu bằng JavaScript.

- **SSR**
  - Server-Side Rendering, server render HTML trước rồi client hydrate.

- **SSG**
  - Static Site Generation, build HTML tĩnh trước khi deploy.

- **ISR**
  - Incremental Static Regeneration, static page được revalidate theo thời gian.

- **Streaming SSR**
  - Server gửi HTML từng phần để cải thiện perceived performance.

- **Islands Architecture**
  - Static HTML là chính, chỉ hydrate các “island” cần tương tác.

- **Hydration**
  - Quá trình React gắn event/state vào HTML đã render từ server.

- **CDN**
  - Content Delivery Network, cache static assets gần user.

- **Edge Function**
  - Function chạy gần user ở edge location, phù hợp logic nhẹ như redirect, A/B test.

- **Core Web Vitals**
  - Bộ metrics UX/performance như LCP, CLS, INP.

- **Error Boundary**
  - React component bắt lỗi render ở subtree và hiển thị fallback UI.

- **Retry**
  - Thử lại request/action khi lỗi tạm thời.

- **Circuit Breaker**
  - Pattern ngắt gọi service khi service fail liên tục để tránh cascade failure.

- **Feature Flag**
  - Cờ bật/tắt feature runtime để rollout/canary/A-B test/kill switch.

- **RUM**
  - Real User Monitoring, đo performance/error từ user thật.

- **Synthetic Monitoring**
  - Kiểm tra tự động theo kịch bản từ môi trường giả lập/region cố định.

- **OpenTelemetry**
  - Chuẩn instrumentation cho metrics/logs/traces.

- **ADR**
  - Architecture Decision Record, tài liệu ghi lại quyết định kiến trúc và lý do.

- **SLA/SLO**
  - Cam kết/mục tiêu chất lượng dịch vụ như uptime, latency, error rate.
