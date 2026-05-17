# 🧱 Topic40: Microfrontend, Monorepo & Module Federation

## ⭐ Senior/Staff Summary

> **Microfrontend không phải là "chia nhỏ frontend cho vui". Nó là tradeoff kiến trúc để nhiều team deploy độc lập, nhưng đổi lại là complexity ở runtime, versioning, communication, observability và governance.**

- 🧱 **Microfrontend (MFE)**: chia frontend lớn thành nhiều app nhỏ theo domain/team ownership.
- 🏠 **Shell/Host**: app container chịu trách nhiệm layout, routing cấp cao, auth context, loading remote apps.
- 📦 **Remote app**: MFE được build/deploy riêng, expose page/component/module cho shell dùng.
- 🔌 **Module Federation**: runtime code sharing, shell load remote module qua `remoteEntry.js` thay vì build chung.
- 🔄 **Shared dependencies**: share React/UI libs để tránh duplicate bundle và lỗi nhiều instance React.
- 🧩 **Multi-framework**: React/Vue/Angular/Svelte có thể cùng tồn tại, nhưng cần wrapper hoặc Web Components.
- 📡 **Communication**: ưu tiên contract rõ; chọn props/callback, custom events, event bus, shared state tùy coupling.
- 🧭 **Routing**: shell-based routing dễ kiểm soát; distributed routing tăng autonomy nhưng khó debug/version.
- 🎨 **Styling isolation**: CSS Modules, namespace, CSS-in-JS, Shadow DOM/Web Components.
- 📚 **Monorepo**: 1 repo nhiều apps/libs, dùng Nx/Turborepo/pnpm workspaces để share code, cache build, enforce boundaries.
- ⚠️ **Không nên dùng MFE** nếu team nhỏ, app đơn giản, domain coupling cao, hoặc chưa có CI/CD/observability đủ tốt.

## 🧠 Key Mental Model

### 1. Tách theo domain, không tách theo component nhỏ

Microfrontend hợp khi boundary đủ rõ:

- ✅ `catalog`, `cart`, `checkout`, `profile`, `admin`.
- ❌ `Button`, `Modal`, `Table`, `Header` thành remote app riêng.

💡 **Rule thực tế**: nếu 2 phần release cùng nhau, dùng chung state sâu, và luôn phải test cùng nhau, chúng chưa thật sự là microfrontend boundary tốt.

### 2. Monorepo và Microfrontend là 2 khái niệm khác nhau

| Khái niệm | Giải thích | Có thể dùng độc lập không? |
|---|---|---|
| `Microfrontend` | Kiến trúc runtime/deployment chia app thành nhiều frontend độc lập | Có |
| `Monorepo` | Cách tổ chức source code nhiều apps/libs trong 1 repo | Có |
| `Module Federation` | Cơ chế load/share module runtime giữa host và remotes | Có |

Bạn có thể có:

- MFE + multi-repo.
- MFE + monorepo.
- Monorepo nhưng vẫn là monolith frontend.

### 3. Senior question trước khi chọn MFE

- Team có cần deploy độc lập thật không?
- Domain ownership có rõ không?
- Có contract API/event/version rõ chưa?
- Có monitoring theo từng remote không?
- Có fallback khi remote fail không?
- Có policy shared dependency không?
- Có design system đủ ổn để UX không bị chắp vá không?

## 📚 Main Concepts

### 🧱 Microfrontend là gì?

Microfrontend chia app lớn thành nhiều frontend nhỏ, mỗi phần có thể:

- Do một team sở hữu.
- Build/test/deploy riêng.
- Có release cadence riêng.
- Có thể dùng tech stack riêng, nếu governance cho phép.

Ví dụ e-commerce:

```text
Shell App
├── Catalog MFE      -> Team Catalog, React
├── Cart MFE         -> Team Cart, Vue
├── Checkout MFE     -> Team Payments, React
├── Profile MFE      -> Team Identity, Angular
└── Admin MFE        -> Team Ops, React
```

### ✅ Khi nào nên dùng Microfrontend?

- Tổ chức có nhiều team frontend làm song song.
- Domain business độc lập tương đối rõ.
- Independent deployment là yêu cầu thật.
- Legacy migration từng phần: Angular -> React, old app -> new stack.
- Cần A/B testing/canary theo từng vertical.
- App quá lớn khiến build/test/deploy monolith thành bottleneck.

### ❌ Khi nào không nên dùng?

- Team nhỏ dưới 5-8 dev.
- App chưa đủ lớn hoặc domain chưa rõ.
- Feature coupling cao, thay đổi một chỗ kéo theo toàn bộ app.
- Chưa có CI/CD, automated test, monitoring, error boundary tốt.
- Chỉ muốn "dùng công nghệ mới" mà không có pain point tổ chức.

### 🔌 Module Federation

Module Federation cho phép app A expose module, app B consume module ở runtime.

**Remote expose module:**

```js
// dashboard/webpack.config.js
new ModuleFederationPlugin({
  name: "dashboard",
  filename: "remoteEntry.js",
  exposes: {
    "./DashboardPage": "./src/pages/DashboardPage",
    "./widgets/RevenueCard": "./src/widgets/RevenueCard",
  },
  shared: {
    react: { singleton: true, requiredVersion: "^18.0.0" },
    "react-dom": { singleton: true, requiredVersion: "^18.0.0" },
  },
});
```

**Shell consume remote:**

```js
// shell/webpack.config.js
new ModuleFederationPlugin({
  name: "shell",
  remotes: {
    dashboard: "dashboard@https://cdn.example.com/dashboard/remoteEntry.js",
  },
  shared: {
    react: { singleton: true, requiredVersion: "^18.0.0" },
    "react-dom": { singleton: true, requiredVersion: "^18.0.0" },
  },
});
```

**React lazy load remote:**

```tsx
import * as React from "react";

const DashboardPage = React.lazy(() => import("dashboard/DashboardPage"));

export function AppRoutes() {
  return (
    <React.Suspense fallback={<div>Loading dashboard...</div>}>
      <DashboardPage />
    </React.Suspense>
  );
}
```

💡 Webpack 5 có Module Federation native. Vite thường dùng plugin federation/Rspack ecosystem tùy stack.

### 🔄 Shared dependencies

Shared dependency giúp tránh:

- Duplicate React/ReactDOM.
- Bundle phình lớn.
- Context/hooks lỗi do có nhiều React instance.
- UI library bị load nhiều version.

```js
shared: {
  react: {
    singleton: true,
    requiredVersion: "^18.0.0",
  },
  "react-dom": {
    singleton: true,
    requiredVersion: "^18.0.0",
  },
}
```

⚠️ `singleton` không có nghĩa là mọi thứ tự động an toàn. Team vẫn cần:

- Align version.
- Contract compatibility.
- Test shell + remote.
- Fallback khi remote chưa tương thích.

### 🧩 Multi-framework

Multi-framework có thể hữu ích khi:

- Legacy app đang ở Angular/Vue, shell mới ở React.
- Team migrate từng phần.
- Một domain có framework đặc thù.

Nhưng chi phí tăng:

- Bundle size lớn hơn.
- Design consistency khó hơn.
- Routing/state/test phức tạp hơn.
- Hiring/onboarding khó hơn.

**Cách integrate phổ biến:**

- Module Federation + wrapper.
- Web Components/custom elements.
- Iframe nếu cần isolation rất mạnh.

```tsx
// React shell mount một Vue widget thông qua wrapper contract.
type MountVueWidget = (el: HTMLElement, props: { userId: string }) => () => void;

export function VueProfileWrapper({
  mount,
  userId,
}: {
  mount: MountVueWidget;
  userId: string;
}) {
  const ref = React.useRef<HTMLDivElement | null>(null);

  React.useEffect(() => {
    if (!ref.current) return;
    return mount(ref.current, { userId });
  }, [mount, userId]);

  return <div ref={ref} />;
}
```

### 📡 Communication Patterns

#### 1. Props/Callbacks

Dùng khi shell render remote như child component.

```tsx
<CheckoutPage
  user={user}
  locale="vi-VN"
  onCheckoutSuccess={(orderId) => navigate(`/orders/${orderId}`)}
/>
```

✅ Dễ hiểu, type-safe.

⚠️ Coupling cao, remote phụ thuộc shell contract.

#### 2. Custom Events / Event Bus

Dùng khi apps không muốn import trực tiếp nhau.

```typescript
type AppEvent =
  | { type: "cart:item-added"; payload: { sku: string; quantity: number } }
  | { type: "auth:logout"; payload: { reason: "manual" | "expired" } };

export function publish(event: AppEvent) {
  window.dispatchEvent(new CustomEvent(event.type, { detail: event.payload }));
}

export function subscribe<T>(
  type: AppEvent["type"],
  handler: (payload: T) => void
) {
  const listener = (event: Event) => {
    handler((event as CustomEvent<T>).detail);
  };

  window.addEventListener(type, listener);
  return () => window.removeEventListener(type, listener);
}
```

✅ Loose coupling, hợp với notification/auth/cart events.

⚠️ Dễ thành "event spaghetti" nếu không có schema/version/logging.

#### 3. Shared State

Dùng cho state global thật sự như auth session, theme, cart summary.

```typescript
import { create } from "zustand";

type SessionState = {
  userId: string | null;
  setUserId: (userId: string | null) => void;
};

export const useSessionStore = create<SessionState>((set) => ({
  userId: null,
  setUserId: (userId) => set({ userId }),
}));
```

✅ Dễ sync UI cross-MFE.

⚠️ Coupling cao, versioning khó, nhiều remote cùng mutate dễ bug.

#### 4. Backend/API as source of truth

Với data business lớn, đừng cố sync hết qua frontend event bus. Để backend/API là source of truth, frontend chỉ invalidate/refetch.

### 🧭 Routing Strategies

#### Shell-based routing

Shell biết route top-level và load remote theo route.

```tsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/catalog/*" element={<CatalogRemote />} />
  <Route path="/checkout/*" element={<CheckoutRemote />} />
</Routes>
```

✅ Centralized, dễ analytics/auth guard/layout.

⚠️ Shell phải biết route contract của remote.

#### Distributed routing

Shell chỉ route prefix, remote tự quản lý route con.

```tsx
<Route path="/dashboard/*" element={<DashboardRemote />} />
```

✅ Remote tự chủ hơn.

⚠️ Deep link, navigation, 404, breadcrumb, permission khó đồng bộ hơn.

### 🎨 Styling Isolation

| Pattern | Nên dùng khi | Tradeoff |
|---|---|---|
| CSS Modules | Default cho scoped CSS | Ít runtime, dễ dùng |
| CSS-in-JS | Dynamic styling/theme phức tạp | Runtime/cache/SSR cần quản lý |
| Prefix/namespace | Legacy CSS hoặc đơn giản | Discipline cao, dễ leak nếu quên |
| Shadow DOM | Web Components, isolation mạnh | Theming, portal, global style khó hơn |

💡 Dù dùng pattern nào, design system/shared tokens vẫn rất quan trọng để UX không bị mỗi MFE một kiểu.

### 📚 Monorepo

Monorepo là 1 repo chứa nhiều apps/packages:

```text
repo/
├── apps/
│   ├── shell/
│   ├── catalog/
│   ├── checkout/
│   └── profile/
├── libs/
│   ├── shared-ui/
│   ├── shared-auth/
│   ├── shared-types/
│   └── shared-communication/
├── package.json
├── pnpm-workspace.yaml
├── nx.json hoặc turbo.json
└── tsconfig.base.json
```

### 🛠️ Nx vs Turborepo vs Lerna vs pnpm Workspaces

| Tool | Điểm mạnh | Nên dùng khi |
|---|---|---|
| Nx | Dependency graph, generators, affected builds, cache, MF support tốt | Enterprise, Angular/React lớn, cần governance |
| Turborepo | Task runner nhanh, cache đơn giản, framework-agnostic | React/Vue/Next monorepo cần build nhanh |
| pnpm Workspaces | Package linking, disk efficient | Nền tảng package manager cho monorepo |
| Lerna | Publishing packages legacy | Dự án cũ; thường thay bằng pnpm/Turbo/Changesets |

💡 Stack phổ biến:

- Enterprise Angular/React lớn: `Nx`.
- React/Next/Vite nhiều app: `pnpm + Turborepo`.
- Package publishing: `pnpm + Changesets`.

## 🧱 Detailed Architecture Patterns

### 🔥 Monolith pain points mà Microfrontend giải quyết

**Deployment bottleneck:**

- Một team sửa bug nhỏ nhưng phải build/test/deploy cả app.
- QA phải regression nhiều domain không liên quan.
- Rollback một feature có thể rollback luôn toàn bộ release.
- Release train chậm làm team phụ thuộc nhau.

**Team conflict:**

- Nhiều team sửa chung `package.json`, `webpack.config`, `tsconfig`.
- Team A muốn React 18, Team B còn legacy React 17.
- Team C muốn migrate Redux sang Zustand, Team D vẫn cần Redux middleware.
- Code ownership mờ: không rõ ai chịu trách nhiệm domain nào.

**Scale codebase:**

- App lớn build chậm, test chậm, local dev nặng.
- Shared folder thành nơi chứa mọi thứ.
- Component/domain coupling tăng dần, khó refactor.

**Microfrontend giúp bằng cách:**

- Tách ownership theo domain.
- Cho phép deploy remote độc lập.
- Giảm conflict vì mỗi team có app/package riêng.
- Cho phép migrate legacy từng phần.
- Cho phép canary/A-B testing theo domain.

⚠️ Nhưng MFE không tự động làm code tốt hơn. Nếu boundary sai, nó chỉ biến monolith thành distributed monolith khó debug hơn.

### 🏠 Shell App responsibilities

Shell không nên chứa business logic của mọi domain. Shell nên chịu trách nhiệm các concern ngang:

- App layout: header, sidebar, top-level layout.
- Top-level routing.
- Auth/session bootstrap.
- Locale/timezone/theme.
- Remote loading/fallback.
- Error boundary cho từng remote.
- Observability metadata.
- Feature flag/canary quyết định remote version.
- Shared design system provider nếu cần.

```tsx
export function ShellApp() {
  return (
    <SessionProvider>
      <ThemeProvider>
        <AppLayout>
          <RemoteErrorBoundary fallback={<RemoteUnavailable name="catalog" />}>
            <React.Suspense fallback={<RouteSkeleton />}>
              <AppRoutes />
            </React.Suspense>
          </RemoteErrorBoundary>
        </AppLayout>
      </ThemeProvider>
    </SessionProvider>
  );
}
```

### 📦 Remote App responsibilities

Remote nên sở hữu domain của nó:

- Route/page/component trong domain.
- Data fetching liên quan domain.
- UI state local.
- Domain-specific validation.
- Error state và empty state.
- Tests riêng.
- Release notes/version riêng.

Remote không nên:

- Tự thay đổi shell layout global nếu không có contract.
- Đọc/ghi global state tùy tiện.
- Import code từ remote khác trực tiếp.
- Phụ thuộc implementation detail của shell.

### 🔌 Module Federation deep dive

#### `exposes`

Remote expose public API của nó. Hãy expose ít nhưng ổn định.

```js
exposes: {
  "./CatalogPage": "./src/pages/CatalogPage",
  "./ProductCard": "./src/components/ProductCard",
  "./routes": "./src/routes",
}
```

✅ Nên expose:

- Page-level entry.
- Stable widgets.
- Route config nếu shell cần.
- Public mount function cho multi-framework.

❌ Tránh expose:

- Internal hooks chưa ổn định.
- Deep component private.
- Utility nhỏ nên đưa vào shared package.

#### `remotes`

Shell map remote name với URL.

```js
remotes: {
  catalog: "catalog@https://cdn.example.com/catalog/remoteEntry.js",
  checkout: "checkout@https://cdn.example.com/checkout/remoteEntry.js",
}
```

Production thường không hardcode trực tiếp trong code. Dùng manifest để đổi version/canary/rollback:

```json
{
  "catalog": {
    "version": "1.12.3",
    "remoteEntry": "https://cdn.example.com/catalog/1.12.3/remoteEntry.js"
  },
  "checkout": {
    "version": "2.4.0",
    "remoteEntry": "https://cdn.example.com/checkout/2.4.0/remoteEntry.js"
  }
}
```

#### `shared`

Shared dependency là nơi hay gây bug nhất.

```js
shared: {
  react: {
    singleton: true,
    requiredVersion: "^18.2.0",
  },
  "react-dom": {
    singleton: true,
    requiredVersion: "^18.2.0",
  },
  "@company/design-system": {
    singleton: true,
    requiredVersion: "^3.0.0",
  },
}
```

**`singleton: true`:**

- Đảm bảo runtime dùng một instance cho lib quan trọng.
- Cần cho React, ReactDOM, design system provider, shared store nếu thật sự dùng.

**`requiredVersion`:**

- Giúp kiểm soát compatibility.
- Nếu range quá rộng, dễ nhận version không test.
- Nếu quá hẹp, deploy remote có thể fail khi shell chưa upgrade.

**`eager`:**

- Load dependency ngay thay vì lazy.
- Dùng cẩn thận vì có thể tăng initial bundle.
- Không nên bật theo thói quen.

### 🔄 Remote loading lifecycle

```text
1. User vào /catalog
2. Shell match route /catalog/*
3. Shell đọc manifest để biết remoteEntry URL
4. Browser tải remoteEntry.js
5. Module Federation resolve shared dependencies
6. Shell lazy import CatalogPage
7. React Suspense render fallback trong lúc tải
8. Remote render page
9. Error Boundary bắt lỗi nếu remote crash
10. Observability log mfeName + mfeVersion
```

Senior cần biết flow này để debug:

- Remote không tải được: kiểm tra CDN, CORS, manifest, cache.
- React hook error: có thể duplicate React.
- UI trắng: thiếu Error Boundary/fallback.
- Remote cũ chạy với shell mới: version contract mismatch.

### 🧩 Module Federation vs iframe vs package composition

| Pattern | Ưu điểm | Nhược điểm | Nên dùng |
|---|---|---|---|
| Module Federation | Runtime composition, share deps, UX liền mạch | Coupling runtime, config phức tạp | Same trust boundary, cần independent deploy |
| iframe | Isolation mạnh, CSS/JS tách biệt | UX kém hơn, communication khó, routing phức tạp | Third-party, payment, legacy rất tách biệt |
| Package composition | Đơn giản, type-safe, build-time | Không deploy độc lập | Team chưa cần runtime MFE |
| Web Components | Framework-agnostic, Shadow DOM | Tooling/theming/SSR khó hơn | Widget đa framework, embedded component |

## 🧩 Multi-Framework Integration Details

### ⚛️ React shell + Vue remote

Không nên giả định React import trực tiếp Vue component như React component thường. Nên có mount contract rõ:

```typescript
// profile/public-api.ts
export type ProfileMountProps = {
  userId: string;
  locale: string;
};

export function mountProfile(
  element: HTMLElement,
  props: ProfileMountProps
): () => void {
  const app = createVueProfileApp(props);
  app.mount(element);

  return () => app.unmount();
}
```

```tsx
// shell/ProfileRemote.tsx
export function ProfileRemote({
  mountProfile,
  userId,
}: {
  mountProfile: (
    element: HTMLElement,
    props: { userId: string; locale: string }
  ) => () => void;
  userId: string;
}) {
  const ref = React.useRef<HTMLDivElement | null>(null);

  React.useEffect(() => {
    if (!ref.current) return;

    return mountProfile(ref.current, {
      userId,
      locale: "vi-VN",
    });
  }, [mountProfile, userId]);

  return <div ref={ref} />;
}
```

### 🧱 Web Components approach

Web Components giúp framework-agnostic hơn:

```typescript
class ProfileWidget extends HTMLElement {
  connectedCallback() {
    const userId = this.getAttribute("user-id");
    this.innerHTML = `<profile-root data-user-id="${userId}"></profile-root>`;
  }
}

customElements.define("profile-widget", ProfileWidget);
```

React dùng:

```tsx
export function ProfileSlot({ userId }: { userId: string }) {
  return <profile-widget user-id={userId} />;
}
```

⚠️ Tradeoff:

- TypeScript JSX cần khai báo custom element.
- Styling/theming qua Shadow DOM cần design token strategy.
- Event emit phải chuẩn hóa.

### 🧱 Multi-framework governance

Nếu cho phép nhiều framework, cần policy:

- Framework nào được support chính thức?
- Ai maintain tooling/build/test?
- Design system có wrapper cho từng framework không?
- Bundle budget cho mỗi remote là bao nhiêu?
- Migration plan khi một framework bị bỏ support?

Không có governance, multi-framework dễ biến thành "mỗi team một kiểu", UX và maintenance rất tệ.

## 📡 Communication Pattern Deep Dive

### 1. Props/Callbacks

Phù hợp khi:

- Shell là parent rõ ràng.
- Remote cần data nhỏ từ shell.
- Callback ít, contract ổn định.

```tsx
<CartRemote
  userId={session.userId}
  currency="VND"
  onCartChanged={(summary) => {
    setCartSummary(summary);
  }}
/>
```

Không phù hợp khi:

- Nhiều remote cần listen cùng event.
- Remote không có quan hệ parent-child.
- Contract thay đổi thường xuyên.

### 2. Custom Events

Phù hợp cho event cross-domain:

- `auth:expired`
- `cart:updated`
- `notification:show`
- `checkout:completed`

```typescript
type CheckoutCompletedEvent = {
  orderId: string;
  total: number;
};

window.dispatchEvent(
  new CustomEvent<CheckoutCompletedEvent>("checkout:completed", {
    detail: { orderId: "ord_123", total: 450000 },
  })
);
```

Listener phải cleanup:

```typescript
React.useEffect(() => {
  const listener = (event: Event) => {
    const payload = (event as CustomEvent<CheckoutCompletedEvent>).detail;
    console.log(payload.orderId);
  };

  window.addEventListener("checkout:completed", listener);
  return () => window.removeEventListener("checkout:completed", listener);
}, []);
```

### 3. Event Bus / PubSub

Khi event nhiều hơn, dùng event bus có type và logging:

```typescript
type EventMap = {
  "auth:logout": { reason: "manual" | "expired" };
  "cart:item-added": { sku: string; quantity: number };
  "notification:show": { message: string; level: "success" | "error" };
};

class TypedEventBus {
  emit<K extends keyof EventMap>(type: K, payload: EventMap[K]) {
    window.dispatchEvent(new CustomEvent(type, { detail: payload }));
  }

  on<K extends keyof EventMap>(
    type: K,
    handler: (payload: EventMap[K]) => void
  ) {
    const listener = (event: Event) => {
      handler((event as CustomEvent<EventMap[K]>).detail);
    };

    window.addEventListener(type, listener);
    return () => window.removeEventListener(type, listener);
  }
}
```

Senior rule:

- Event phải có owner.
- Payload phải có schema/version.
- Event quan trọng phải log được.
- Không dùng event bus thay cho API/domain model.

### 4. Shared Store

Shared store chỉ nên nhỏ:

- Session/user summary.
- Theme/locale.
- Cart count/summary.
- Notification queue.

Không nên dùng shared store cho toàn bộ business state của mọi remote.

```typescript
type GlobalShellState = {
  user: { id: string; name: string } | null;
  theme: "light" | "dark";
  cartCount: number;
};
```

Nếu store chứa quá nhiều thứ, remote coupling tăng và mất lợi ích independent deployment.

### 5. Backend as source of truth

Với order, payment, inventory, permission, pricing:

- Backend/API là source of truth.
- Remote dùng React Query/SWR/cache riêng.
- Cross-MFE event chỉ invalidate/refetch.

```typescript
eventBus.on("cart:item-added", () => {
  queryClient.invalidateQueries({ queryKey: ["cart-summary"] });
});
```

## 🧭 Routing Strategy Deep Dive

### Shell-based routing

Shell quản lý route map top-level:

```tsx
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/catalog/*" element={<CatalogRemote />} />
  <Route path="/cart/*" element={<CartRemote />} />
  <Route path="/checkout/*" element={<CheckoutRemote />} />
</Routes>
```

Ưu điểm:

- Dễ auth guard.
- Dễ analytics page view.
- Dễ layout consistency.
- Dễ kiểm soát navigation flow.

Nhược điểm:

- Shell phải biết nhiều route contract.
- Mỗi khi remote thêm route lớn, có thể phải update shell.

### Distributed routing

Remote tự quản lý route con:

```tsx
// Shell
<Route path="/catalog/*" element={<CatalogRemote />} />;

// Catalog remote
<Routes>
  <Route path="/" element={<ProductList />} />
  <Route path="/:productId" element={<ProductDetail />} />
  <Route path="/:productId/reviews" element={<ProductReviews />} />
</Routes>;
```

Ưu điểm:

- Remote autonomy cao.
- Shell ít biết implementation detail.
- Team domain tự thêm route con.

Nhược điểm:

- Breadcrumb/title/analytics/permission khó đồng bộ.
- Deep link cần config deployment tốt.
- 404 nested route phải rõ owner.

### Routing contract nên có

```typescript
type RemoteRouteContract = {
  basePath: string;
  owner: string;
  requiresAuth: boolean;
  permissions?: string[];
  title?: string;
};
```

## 🎨 Styling Isolation Deep Dive

### CSS Modules

```css
.button {
  background: var(--color-primary);
  border-radius: var(--radius-sm);
}
```

```tsx
import styles from "./Button.module.css";

export function Button() {
  return <button className={styles.button}>Save</button>;
}
```

Tốt cho:

- Scoped class.
- Ít runtime.
- Dễ debug.

### CSS-in-JS

Tốt cho:

- Theme runtime.
- Dynamic styling.
- Component library.

Lưu ý:

- SSR extraction.
- Runtime overhead.
- Style order giữa shell/remote.

### Shadow DOM

Tốt cho:

- Web Components.
- Isolation mạnh.
- Embedded widget.

Tradeoff:

- Global theme khó truyền vào.
- Modal/tooltip/portal có thể phức tạp.
- Accessibility vẫn phải test kỹ.

### Prefix/Namespace

Legacy friendly:

```css
.catalog-mfe .product-card {
  ...
}
```

Lưu ý:

- Dễ quên prefix.
- Không cô lập thật sự.
- Chỉ phù hợp khi team discipline tốt.

## 📚 Monorepo Setup & Governance

### Cấu trúc repo nên có

```text
repo/
├── apps/
│   ├── shell/
│   ├── catalog/
│   ├── cart/
│   ├── checkout/
│   └── profile/
├── libs/
│   ├── design-system/
│   ├── shared-auth/
│   ├── shared-api-client/
│   ├── shared-communication/
│   ├── domain-product/
│   ├── domain-order/
│   └── shared-test-utils/
├── tools/
├── package.json
├── pnpm-workspace.yaml
├── nx.json hoặc turbo.json
└── tsconfig.base.json
```

### Dependency boundaries

```text
apps/*                 -> can import libs/*
libs/design-system     -> cannot import apps/*
libs/domain-product    -> cannot import apps/catalog
libs/shared-auth       -> should not import domain-specific libs
libs/shared-utils      -> should stay framework-light
```

Nếu dùng Nx:

```json
{
  "depConstraints": [
    {
      "sourceTag": "type:app",
      "onlyDependOnLibsWithTags": ["type:ui", "type:domain", "type:shared"]
    },
    {
      "sourceTag": "type:shared",
      "onlyDependOnLibsWithTags": ["type:shared"]
    }
  ]
}
```

### Affected builds

Monorepo hiệu quả khi chỉ build/test phần bị ảnh hưởng:

```text
Change libs/design-system/Button
-> affected: shell, catalog, checkout, profile

Change apps/catalog/ProductList
-> affected: catalog only

Change libs/domain-order
-> affected: checkout, order-history
```

CI nên chạy:

- Lint affected projects.
- Test affected projects.
- Build affected apps/libs.
- E2E critical flows nếu shared lib quan trọng đổi.

## 🛠️ Monorepo Tooling Deep Dive

### Nx

Nx mạnh ở governance và dependency graph:

- Project graph.
- Affected commands.
- Local/remote cache.
- Generators.
- Module boundaries.
- Integrated plugins.
- Module Federation support tốt, đặc biệt Angular/React enterprise.

```bash
nx graph
nx affected -t lint test build
nx g @nx/react:app shell
nx g @nx/react:lib design-system
```

Nên dùng Nx khi:

- Repo lớn, nhiều team.
- Cần enforce architecture.
- Muốn code generation chuẩn hóa.
- Cần affected build/test nghiêm túc.

Tradeoff:

- Config nhiều hơn.
- Tooling opinionated hơn.
- Onboarding cần thời gian.

### Turborepo

Turborepo tập trung vào task orchestration và cache:

```json
{
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["^build"]
    },
    "lint": {}
  }
}
```

Nên dùng Turbo khi:

- React/Next/Vite monorepo.
- Muốn setup nhẹ.
- Cần cache build nhanh.
- Architecture boundaries có thể enforce bằng ESLint/TS riêng.

Tradeoff:

- Ít governance hơn Nx.
- Không giàu generator bằng Nx.
- Dependency graph/affected semantics đơn giản hơn.

### pnpm Workspaces

pnpm giúp link packages nội bộ và tiết kiệm disk:

```yaml
packages:
  - "apps/*"
  - "libs/*"
```

```json
{
  "dependencies": {
    "@company/design-system": "workspace:*",
    "@company/shared-auth": "workspace:*"
  }
}
```

Nên dùng pnpm gần như mặc định cho monorepo JS/TS hiện đại.

### Lerna

Lerna từng phổ biến cho multi-package publishing. Hiện nay thường thay bằng:

- pnpm workspaces.
- Turborepo/Nx.
- Changesets cho versioning/publishing.

Chỉ nên giữ Lerna nếu repo legacy đã dùng ổn.

### Caching strategies

**Local cache:**

- Dev A build một task.
- Chạy lại cùng input -> lấy cache.
- Giảm thời gian local feedback.

**Remote cache:**

- CI build một task.
- Dev/CI khác reuse output.
- Rất mạnh với team lớn.

Input cache nên gồm:

- Source files.
- Lockfile.
- Config files.
- Environment relevant.
- Build command.

Không nên cache mù nếu build phụ thuộc env ẩn.

### Task orchestration

Nếu `shell` phụ thuộc `shared-ui`, build order phải là:

```text
shared-ui -> catalog -> shell
shared-auth -> shell
```

Tool tốt sẽ tự hiểu graph, thay vì dev viết script thủ công.

## 🚀 Real-World Scenarios

### Scenario 1: E-commerce nhiều team

**Context:** Catalog, cart, checkout, profile do các team khác nhau sở hữu.

**Architecture:**

```text
Shell
├── catalog remote
├── cart remote
├── checkout remote
└── profile remote
```

**Key decisions:**

- Shell quản lý auth/session/layout.
- Catalog tự deploy filter/search/product detail.
- Checkout có Error Boundary và rollback riêng vì business critical.
- Cart summary dùng shared store nhỏ hoặc event `cart:updated`.
- Product/order data vẫn qua backend API.

**Tradeoff senior:**

- Catalog có thể deploy nhanh hơn.
- Checkout cần test contract kỹ hơn.
- Design system phải enforce để UX thống nhất.

### Scenario 2: Legacy Angular -> React migration

**Context:** App cũ Angular lớn, team muốn migrate sang React nhưng không thể rewrite một lần.

**Approach:**

- Shell mới hoặc shell hiện tại load remote theo route.
- Angular legacy giữ domain chưa migrate.
- React remote viết domain mới.
- Shared auth và design tokens thống nhất.
- Migrate từng domain: profile -> dashboard -> checkout.

**Tradeoff:**

- Tốc độ migrate an toàn hơn.
- Tạm thời bundle có cả Angular và React.
- Routing và shared auth phải thiết kế kỹ.

### Scenario 3: Internal platform với Nx monorepo

**Context:** Công ty có 20 apps admin/internal, nhiều shared libs.

**Approach:**

- Nx monorepo.
- Apps trong `apps/*`.
- Shared UI/auth/api/types trong `libs/*`.
- Module boundaries bằng tags.
- Remote cache trong CI.
- Affected build/test.

**Outcome:**

- Build nhanh hơn.
- Consistency tooling tốt hơn.
- Ownership rõ hơn qua CODEOWNERS.

### Scenario 4: Third-party payment iframe

**Context:** Checkout cần nhúng payment provider.

**Decision:**

- Không dùng Module Federation cho third-party untrusted code.
- Dùng iframe để isolation.
- Giao tiếp qua `postMessage` với origin check.

```typescript
window.addEventListener("message", (event) => {
  if (event.origin !== "https://payment.example.com") return;

  if (event.data.type === "payment:completed") {
    confirmPayment(event.data.paymentId);
  }
});
```

**Tradeoff:**

- Isolation/security tốt hơn.
- UX và integration khó hơn.

## 🧪 Practical TypeScript/JavaScript Examples

### ✅ 1. Remote manifest thay vì hardcode URL

Hardcode remote URL làm deploy/rollback khó.

```typescript
type RemoteManifest = {
  dashboard: {
    url: string;
    version: string;
  };
  checkout: {
    url: string;
    version: string;
  };
};

async function loadRemoteManifest(): Promise<RemoteManifest> {
  const response = await fetch("/mfe-manifest.json", {
    cache: "no-store",
  });

  if (!response.ok) {
    throw new Error("Cannot load MFE manifest");
  }

  return response.json();
}
```

✅ Manifest giúp:

- Rollback remote bằng config.
- Canary theo user/region.
- Kiểm soát version compatibility.

### ✅ 2. Error Boundary cho remote app

Remote crash không nên làm shell trắng màn hình.

```tsx
import * as React from "react";

type RemoteErrorBoundaryState = {
  hasError: boolean;
};

export class RemoteErrorBoundary extends React.Component<
  React.PropsWithChildren<{ fallback?: React.ReactNode }>,
  RemoteErrorBoundaryState
> {
  state = { hasError: false };

  static getDerivedStateFromError() {
    return { hasError: true };
  }

  componentDidCatch(error: Error, info: React.ErrorInfo) {
    console.error("Remote crashed", { error, info });
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ?? <div>Không tải được module.</div>;
    }

    return this.props.children;
  }
}
```

### ✅ 3. Typed event contract

```typescript
type MfeEvents = {
  "cart:updated": { itemCount: number };
  "auth:expired": { redirectTo: string };
  "notification:show": { message: string; level: "info" | "error" };
};

export function emit<K extends keyof MfeEvents>(
  type: K,
  payload: MfeEvents[K]
) {
  window.dispatchEvent(new CustomEvent(type, { detail: payload }));
}

export function on<K extends keyof MfeEvents>(
  type: K,
  handler: (payload: MfeEvents[K]) => void
) {
  const listener = (event: Event) => {
    handler((event as CustomEvent<MfeEvents[K]>).detail);
  };

  window.addEventListener(type, listener);
  return () => window.removeEventListener(type, listener);
}
```

### ✅ 4. Monorepo boundaries

```text
apps/checkout     -> can import libs/shared-ui, libs/shared-auth, libs/domain-order
apps/catalog      -> can import libs/shared-ui, libs/domain-product
libs/shared-ui    -> cannot import apps/*
libs/domain-order -> cannot import apps/checkout
```

✅ Enforce bằng Nx module boundaries, ESLint rules, TS path aliases, CODEOWNERS.

## ⚛️ Production Notes / React Implications

### 🚀 Performance

- Lazy load remote theo route.
- Preload remote khi hover/nav intent.
- Share React/ReactDOM/UI libs có kiểm soát.
- Tránh remote nhỏ quá nhiều làm tăng network waterfall.
- Theo dõi bundle duplication bằng analyzer.
- Có fallback skeleton để remote load chậm không làm layout jump.

### 🧯 Resilience

- Remote app phải có Error Boundary riêng.
- Shell cần fallback nếu `remoteEntry.js` fail.
- Manifest/CDN cache cần strategy rõ: `remoteEntry` thường không cache quá lâu; assets hashed có thể cache lâu.
- Deploy remote phải có rollback độc lập.
- Contract breaking change phải có versioning.

### 🔐 Security

- Remote code là code chạy trong cùng origin/runtime của shell; coi như trusted code.
- Không load remote từ domain không kiểm soát.
- Dùng CSP/SRI khi phù hợp với deployment model.
- Auth token/session ownership cần rõ: shell quản lý session, remote gọi API qua shared API client hoặc backend gateway.
- Không để remote tự ý đọc/ghi global state nhạy cảm nếu không có contract.

### 📊 Observability

Log/error phải có metadata:

- `mfeName`
- `mfeVersion`
- `route`
- `remoteEntryUrl`
- `shellVersion`

Không có metadata này, debug production gần như mù vì không biết lỗi đến từ remote nào.

### 🧪 Testing Strategy

- Unit test từng remote.
- Contract test cho event payload, exposed modules, shared API.
- Integration test shell + selected remote versions.
- E2E critical flow: login, catalog, cart, checkout.
- Visual regression cho design system.
- Smoke test sau deploy remote.

### 🧭 SSR / Next.js

MFE + SSR khó hơn SPA:

- Remote loading phải tương thích server/client.
- Hydration mismatch dễ xảy ra nếu remote render khác shell.
- Module Federation trong SSR cần setup riêng theo framework/runtime.
- Với Next.js, cân nhắc route-level ownership hoặc package-based composition trước khi runtime MFE.

## 🧩 Appendix: Design System, Scalable FE Structure & State Management

Phần gốc của file có thêm nhiều key về design system, structure, patterns và state management. Các ý này liên quan trực tiếp đến MFE vì nếu thiếu governance, nhiều MFE sẽ tạo UX/codebase rời rạc.

### 🎨 Design System

Design system nên chứa:

- Design tokens: color, spacing, typography, radius, shadow.
- Shared UI components: Button, Input, Modal, Table.
- Accessibility rules.
- Versioning/changelog.
- Visual regression tests.

Trong MFE, design system nên là package/shared lib có version rõ, không copy component giữa apps.

#### Design tokens

Tokens là ngôn ngữ chung giữa design và code:

```typescript
export const tokens = {
  color: {
    primary: "#2563eb",
    danger: "#dc2626",
    text: "#111827",
  },
  spacing: {
    xs: "4px",
    sm: "8px",
    md: "16px",
    lg: "24px",
  },
  radius: {
    sm: "4px",
    md: "8px",
  },
};
```

Trong MFE, tokens giúp:

- Catalog và checkout không tự chọn spacing/color khác nhau.
- Multi-framework vẫn giữ visual consistency.
- Upgrade theme có đường đi rõ.

#### Shared UI package

```text
libs/design-system/
├── src/
│   ├── Button/
│   ├── Input/
│   ├── Modal/
│   ├── Table/
│   ├── tokens/
│   └── index.ts
└── package.json
```

Rule senior:

- Component public API phải ổn định.
- Breaking change cần changelog/migration guide.
- Có Storybook hoặc docs.
- Có visual regression test.
- Không nhét business logic vào design system.

#### Design system trong multi-framework

Nếu remote có React/Vue/Angular:

- Option 1: design tokens shared, component implementation riêng từng framework.
- Option 2: Web Components cho component cơ bản.
- Option 3: React-only design system và hạn chế multi-framework.

Tradeoff:

- Wrapper nhiều framework tăng maintenance.
- Web Components isolate tốt nhưng theming/SSR/tooling có thể khó.
- Một framework chính giúp DX tốt hơn.

### 🏗️ Scalable FE Structure

```text
src/
├── app/                 # app bootstrap, providers, router
├── features/            # business features: auth, orders, products
├── entities/            # domain models/types
├── shared/              # UI, utils, hooks, api client
└── pages/               # route-level composition
```

Key senior:

- Tách domain logic khỏi UI.
- Không để `shared/` thành thùng rác.
- API boundary rõ.
- Feature ownership rõ.
- Có lint/import rules để tránh dependency ngược.

#### Feature-based structure

```text
features/auth/
├── api/
│   └── authApi.ts
├── components/
│   └── LoginForm.tsx
├── hooks/
│   └── useLogin.ts
├── model/
│   ├── auth.types.ts
│   └── authStore.ts
└── index.ts
```

Ưu điểm:

- Dễ tìm code theo domain.
- Dễ giao ownership cho team.
- Dễ tách thành remote/lib nếu domain lớn.

#### Layered boundaries

```text
app -> pages -> features -> entities -> shared
```

Rule:

- `shared` không import `features`.
- `entities` không biết UI page.
- `features` có thể dùng `entities/shared`.
- `pages` compose features.
- `app` bootstrap providers/router.

#### API boundary

```typescript
// features/orders/api/orderApi.ts
export async function fetchOrders(userId: string) {
  const response = await fetch(`/api/users/${userId}/orders`);

  if (!response.ok) {
    throw new Error("Cannot fetch orders");
  }

  return response.json() as Promise<Order[]>;
}
```

Senior point:

- UI không gọi fetch rải rác.
- API client centralize auth/error handling.
- DTO -> ViewModel mapping rõ.
- Test dễ hơn.

### 🧠 Frontend design patterns

- Container/Presentational: tách data fetching khỏi UI.
- Compound Components: component API linh hoạt.
- Controlled/Uncontrolled: form/input predictable.
- Custom Hooks: reuse behavior, test logic riêng.
- Singleton: dùng cẩn thận cho API client/event bus/auth manager.
- Error Boundary: cô lập lỗi render.

#### Container / Presentational

```tsx
function OrdersContainer() {
  const { data, isLoading } = useOrders();
  return <OrdersTable orders={data ?? []} loading={isLoading} />;
}

function OrdersTable({
  orders,
  loading,
}: {
  orders: Order[];
  loading: boolean;
}) {
  if (loading) return <div>Loading...</div>;
  return <table>{/* render rows */}</table>;
}
```

Dùng khi muốn UI dễ test và data fetching không lẫn vào markup.

#### Compound Components

```tsx
<Tabs defaultValue="overview">
  <Tabs.List>
    <Tabs.Tab value="overview">Overview</Tabs.Tab>
    <Tabs.Tab value="settings">Settings</Tabs.Tab>
  </Tabs.List>
  <Tabs.Panel value="overview">...</Tabs.Panel>
  <Tabs.Panel value="settings">...</Tabs.Panel>
</Tabs>
```

Hợp cho design system component có nhiều sub-parts.

#### Controlled vs Uncontrolled

```tsx
function ControlledInput() {
  const [value, setValue] = React.useState("");
  return <input value={value} onChange={(e) => setValue(e.target.value)} />;
}

function UncontrolledInput() {
  const ref = React.useRef<HTMLInputElement | null>(null);
  return <input ref={ref} defaultValue="" />;
}
```

Rule:

- Form cần validation/live state -> controlled.
- Input đơn giản hoặc performance-sensitive -> uncontrolled có thể hợp.

#### Custom Hooks

```typescript
function useOrderSummary(orderId: string) {
  return useQuery({
    queryKey: ["order-summary", orderId],
    queryFn: () => fetchOrderSummary(orderId),
  });
}
```

Custom hook giúp reuse behavior, không reuse UI quá sớm.

#### Singleton

Singleton hợp cho:

- API client.
- Event bus.
- Logger.
- Feature flag client.

Nhưng trong MFE phải cẩn thận vì nhiều bundle có thể tạo nhiều singleton nếu shared config sai.

### 🗃️ State Management: Context vs Zustand vs Redux

| Tool | Nên dùng khi | Lưu ý |
|---|---|---|
| Context API | Theme, locale, auth status ít đổi | Dễ gây re-render nếu value thay đổi thường xuyên |
| Zustand | App vừa/lớn, store đơn giản, performance tốt | Ít boilerplate, hợp cart/user/ui state |
| Redux Toolkit | App enterprise, workflow phức tạp, middleware/debug mạnh | Boilerplate hơn, hợp trading/CRM/admin lớn |

Trong Microfrontend:

- Tránh share quá nhiều mutable state.
- Prefer event/API contract cho cross-domain communication.
- Shared state chỉ nên dùng cho state thật sự global: session, theme, cart summary.

#### Context API

Context là built-in React, hợp cho state ít thay đổi:

```tsx
const ThemeContext = React.createContext<{
  theme: "light" | "dark";
  toggleTheme: () => void;
} | null>(null);

export function ThemeProvider({ children }: React.PropsWithChildren) {
  const [theme, setTheme] = React.useState<"light" | "dark">("light");

  const value = React.useMemo(
    () => ({
      theme,
      toggleTheme: () =>
        setTheme((current) => (current === "light" ? "dark" : "light")),
    }),
    [theme]
  );

  return (
    <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>
  );
}
```

Pitfall:

- Context value đổi làm consumers re-render.
- Không hợp cho high-frequency state như typing, realtime price, cart item quantity update liên tục.

#### Zustand

Zustand gọn, hiệu quả cho app vừa/lớn:

```typescript
import { create } from "zustand";

type CartState = {
  items: Array<{ sku: string; quantity: number }>;
  addItem: (sku: string) => void;
  removeItem: (sku: string) => void;
};

export const useCartStore = create<CartState>((set) => ({
  items: [],
  addItem: (sku) =>
    set((state) => ({
      items: [...state.items, { sku, quantity: 1 }],
    })),
  removeItem: (sku) =>
    set((state) => ({
      items: state.items.filter((item) => item.sku !== sku),
    })),
}));
```

Ưu điểm:

- Ít boilerplate.
- Selector tốt, re-render ít hơn Context nếu dùng đúng.
- Dễ dùng cho cart, UI state, user preferences.

Lưu ý trong MFE:

- Nếu shared store là package singleton, phải đảm bảo không bị bundle thành nhiều bản.
- Không dùng shared Zustand store để mọi remote mutate toàn bộ state business.

#### Redux Toolkit

Redux hợp khi state phức tạp, team lớn, workflow cần trace:

```typescript
import { createSlice, configureStore } from "@reduxjs/toolkit";

const ordersSlice = createSlice({
  name: "orders",
  initialState: {
    items: [] as Order[],
    loading: false,
  },
  reducers: {
    orderAdded(state, action) {
      state.items.push(action.payload);
    },
  },
});

export const store = configureStore({
  reducer: {
    orders: ordersSlice.reducer,
  },
});
```

Ưu điểm:

- DevTools mạnh.
- Middleware ecosystem.
- Predictable state transitions.
- Hợp trading/CRM/admin rất lớn.

Tradeoff:

- Nhiều structure hơn Zustand.
- Không nên dùng chỉ vì "enterprise" nếu app không cần.

#### Decision nhanh cho state

- Theme/locale/auth status ít đổi -> Context.
- Cart/user profile/notification/UI state -> Zustand.
- Trading/realtime complex workflows/audit/debug lớn -> Redux Toolkit.
- Server state/API cache -> React Query/SWR, không nhét hết vào global client store.

## ⚠️ Common Pitfalls

- ❌ Dùng MFE cho team nhỏ/app nhỏ, tạo complexity không cần thiết.
- ❌ Tách theo UI component thay vì business domain.
- ❌ Không có version compatibility giữa shell và remote.
- ❌ Load remote fail làm toàn app trắng màn hình.
- ❌ Duplicate React hoặc nhiều version shared libs.
- ❌ Shared state quá lớn làm các MFE coupled như monolith.
- ❌ Event bus không schema, không logging, không cleanup listener.
- ❌ CSS leak giữa apps.
- ❌ Multi-framework không có design system, UX rời rạc.
- ❌ Monorepo không enforce boundaries, cuối cùng thành distributed monolith.
- ❌ Không có observability theo `mfeName/version`.
- ❌ CI build/test tất cả mọi thứ, không dùng affected build/cache.

## ✅ Decision Guide / Checklist

**Có nên dùng Microfrontend không?**

- Có nhiều team độc lập không?
- Có cần deploy độc lập thật không?
- Domain boundary có rõ không?
- Có automated test đủ tin cậy không?
- Có monitoring/error tracking theo remote không?
- Có design system/shared contracts không?

**Chọn integration pattern:**

- Cùng framework, cần runtime composition -> Module Federation.
- Khác framework nhẹ -> wrapper/Web Components.
- Cần isolation rất mạnh -> iframe, chấp nhận UX/integration kém hơn.
- Chỉ cần share code nội bộ -> monorepo packages, chưa cần MFE.

**Communication:**

- Parent-child gần nhau -> props/callback.
- Cross-domain event -> typed event bus/custom events.
- Global UI/session state -> shared store nhỏ.
- Business data -> backend/API source of truth.

**Monorepo tooling:**

- Enterprise/generator/boundary mạnh -> Nx.
- Build nhanh, setup nhẹ -> Turborepo + pnpm.
- Package manager/linking -> pnpm workspaces.
- Publishing packages -> Changesets.

## 🗣️ Short Interview Answer

Em nghĩ Microfrontend phù hợp khi vấn đề chính là scale team và independent deployment, không phải chỉ là scale code. Kiến trúc thường có shell app làm host, các remote app theo domain như catalog, cart, checkout, profile. Module Federation giúp shell load remote module ở runtime qua `remoteEntry`, đồng thời share dependency như React để tránh duplicate và lỗi nhiều React instance.

Theo em, phần khó nhất không phải cấu hình Webpack/Vite, mà là boundary và governance: route ownership, communication contract, shared state, version compatibility, fallback khi remote fail, styling isolation, observability và CI/CD. Nếu team nhỏ hoặc domain coupling cao, em thường chọn modular monolith hoặc monorepo trước, vì Microfrontend có overhead lớn.

Với Monorepo, em dùng Nx hoặc Turborepo/pnpm để share libs, enforce boundaries, cache build và chỉ build affected projects. Còn communication giữa MFEs thì em ưu tiên props/callback cho quan hệ cha con, event bus typed cho event cross-domain, shared store rất nhỏ cho session/theme/cart summary, và để backend/API làm source of truth cho business data.

## 🧠 Ghi nhớ nhanh

- **Microfrontend** = scale team + independent deployment, không phải default architecture.
- **Boundary theo domain**, không theo component nhỏ.
- **Shell** quản lý layout, auth/session, top-level routing, remote loading, fallback.
- **Remote** sở hữu domain/page/widget riêng và deploy độc lập.
- **Module Federation** = runtime composition qua `remoteEntry.js`.
- **Shared dependencies** phải kiểm soát React/ReactDOM/design system để tránh duplicate.
- **Communication** nên có contract: props/callback, typed event bus, shared store nhỏ, backend source of truth.
- **Routing** chọn shell-based nếu cần control, distributed nếu remote cần autonomy.
- **Styling isolation** cần CSS Modules/CSS-in-JS/Shadow DOM/prefix + design system.
- **Monorepo** giúp share libs, enforce boundaries, affected build/test, remote cache.
- **Nx** mạnh về governance, **Turborepo** nhẹ và nhanh, **pnpm workspaces** là nền tảng package linking.
- **Không có observability/version/fallback** thì MFE rất khó vận hành production.

## 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| Microfrontend | Kiến trúc chia frontend lớn thành nhiều app/domain nhỏ, có thể deploy độc lập |
| Monorepo | Một repository chứa nhiều apps/libs/packages |
| Shell / Host | App container load và compose các remote apps |
| Remote App | App con expose module/page/component cho shell dùng |
| Module Federation | Cơ chế runtime load/share module giữa nhiều build độc lập |
| `remoteEntry.js` | Entry file chứa metadata/runtime để host biết cách tải remote module |
| Exposes | Config remote public module cho app khác import |
| Remotes | Config host biết remote nào cần load từ URL nào |
| Shared Dependencies | Các dependencies được share giữa shell/remotes để tránh duplicate |
| Singleton | Config đảm bảo chỉ dùng một instance của dependency quan trọng |
| Multi-framework | Nhiều framework cùng tồn tại, ví dụ React shell load Vue/Angular remote |
| Web Components | Chuẩn browser tạo custom elements có thể dùng cross-framework |
| Shadow DOM | DOM/CSS isolation cho Web Components |
| Event Bus | Cơ chế publish/subscribe event giữa apps |
| Custom Event | Browser event tự định nghĩa qua `CustomEvent` |
| Shared State | Store dùng chung giữa nhiều phần app, ví dụ Zustand/Redux |
| Shell-based Routing | Shell quản lý route map chính và load remote theo route |
| Distributed Routing | Remote tự quản lý route con bên trong base path |
| Design System | Bộ tokens, components, guidelines giúp UI nhất quán |
| Affected Build | Chỉ build/test project bị ảnh hưởng bởi thay đổi |
| Remote Cache | Cache build/test output dùng chung giữa CI/devs |
| Task Orchestration | Chạy task theo dependency graph đúng thứ tự |
| CODEOWNERS | File định nghĩa team/person chịu trách nhiệm review vùng code |
| Error Boundary | React boundary bắt lỗi render để không crash toàn app |
| Contract Test | Test đảm bảo contract giữa shell/remote/event/API không bị phá |
| Canary Release | Release một version cho một nhóm user nhỏ trước khi rollout rộng |
| Rollback | Quay về version trước khi release lỗi |
| Distributed Monolith | Hệ thống bị tách deployment nhưng coupling vẫn cao như monolith |
