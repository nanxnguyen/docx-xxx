# ⚛️ Topic 34: React 19 Migration Guide - Upgrade từ React 18 sang React 19

## 1. ⭐ Senior/Staff Summary

React 19 không chỉ là bản nâng cấp API. Nó thay đổi cách React xử lý **async UI**, **form submission**, **optimistic update**, **ref**, **document metadata**, **resource loading**, **error reporting** và một số API legacy đã bị loại bỏ.

Điểm quan trọng khi migrate từ React 18 sang React 19:

- ✅ **Nâng React 18.3 trước** nếu dự án lớn, vì React 18.3 gần giống 18.2 nhưng thêm warning cho các API sẽ lỗi khi lên React 19.
- ✅ **Chạy official codemod**, sau đó review thủ công. Codemod giúp nhanh, nhưng không thay senior judgment.
- ✅ **Bật new JSX transform** (`react-jsx` / automatic runtime). React 19 yêu cầu transform mới để hỗ trợ `ref` as prop và tối ưu JSX.
- ✅ **Kiểm tra legacy API**: `ReactDOM.render`, `ReactDOM.hydrate`, `unmountComponentAtNode`, `findDOMNode`, string refs, legacy context, `react-dom/test-utils`.
- ✅ **Cập nhật TypeScript types** vì React 19 có thay đổi đáng kể ở `ref`, `useReducer`, JSX namespace và form/action typing.
- ✅ **Adopt feature mới theo nhu cầu**, không rewrite toàn bộ app: dùng Actions cho mutation/form phức tạp, `useOptimistic` cho UX cần phản hồi tức thì, `use()` chủ yếu khi framework/runtime hỗ trợ Suspense tốt.

> 💡 Mental model: **React 19 làm mutation async trở thành first-class citizen**. Trước đây form/mutation thường là `useState + loading + error + try/catch + rollback`; React 19 đưa những pattern này vào core API để UI async nhất quán hơn.

## 2. 🧠 Key Mental Model

### 2.1. React 18 vs React 19 trong một bảng

| Mảng | React 18 | React 19 |
|---|---|---|
| Form async | Tự quản lý `isLoading`, `error`, submit handler | `<form action>`, `useActionState`, `useFormStatus` |
| Mutation UX | Tự code optimistic + rollback | `useOptimistic` hỗ trợ state optimistic |
| Promise trong render | Chủ yếu qua framework/Suspense patterns | `use(promise)` cho Suspense-aware rendering |
| Ref custom component | Thường cần `forwardRef` | Function component có thể nhận `ref` như prop |
| Metadata | Thường dùng framework hoặc `react-helmet` | Có thể render `<title>`, `<meta>`, `<link>` trong component |
| Resource loading | Manual preload/preconnect hoặc framework | `preload`, `preinit`, `preconnect`, `prefetchDNS` từ `react-dom` |
| Legacy APIs | Nhiều API cũ còn warning | Nhiều API cũ bị remove hoặc deprecated mạnh hơn |
| Error reporting | Render error có thể bị log/rethrow trùng | Có `onCaughtError`, `onUncaughtError` ở root |

### 2.2. Migration đúng cách

```text
React 18.2
  ↓
React 18.3 để thấy warning sớm
  ↓
Branch migration riêng
  ↓
Upgrade react/react-dom/@types
  ↓
Run React 19 codemods
  ↓
Fix TypeScript + tests + console warnings
  ↓
Manual QA: forms, auth, routing, hydration, SSR
  ↓
Deploy staging/canary
```

### 2.3. Không nên hiểu React 19 như một yêu cầu rewrite

React 19 cho phép code gọn hơn, nhưng migration tốt thường là:

- **Phase 1**: làm app chạy ổn trên React 19.
- **Phase 2**: thay legacy API và fix warning.
- **Phase 3**: adopt Actions / `useActionState` / `useOptimistic` ở những flow có lợi rõ ràng.
- **Phase 4**: tối ưu SSR, metadata, resource loading, testing và observability.

## 3. 📚 Main Concepts

### 3.1. ✅ Actions - async transition cho mutation

**Actions** là pattern cho async state transition. Một Action thường là async function được gọi trong context mà React hiểu được, ví dụ:

- `startTransition(async () => { ... })`
- `<form action={actionFn}>`
- `useActionState(actionFn, initialState)`

React dùng Action để quản lý pending state, optimistic state và thứ tự cập nhật UI tốt hơn.

#### Trước React 19

```tsx
import { useState } from 'react';

async function updateProfile(name: string) {
  const response = await fetch('/api/profile', {
    method: 'POST',
    body: JSON.stringify({ name }),
  });

  if (!response.ok) {
    throw new Error('Update failed');
  }
}

export function ProfileForm() {
  const [name, setName] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isPending, setIsPending] = useState(false);

  async function handleSubmit() {
    setIsPending(true);
    setError(null);

    try {
      await updateProfile(name);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Unknown error');
    } finally {
      setIsPending(false);
    }
  }

  return (
    <section>
      <input value={name} onChange={(event) => setName(event.target.value)} />
      <button disabled={isPending} onClick={handleSubmit}>
        {isPending ? 'Saving...' : 'Save'}
      </button>
      {error && <p role="alert">{error}</p>}
    </section>
  );
}
```

#### React 19 với `useTransition`

```tsx
import { useState, useTransition } from 'react';

export function ProfileForm() {
  const [name, setName] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isPending, startTransition] = useTransition();

  function handleSubmit() {
    startTransition(async () => {
      setError(null);

      try {
        await updateProfile(name);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Unknown error');
      }
    });
  }

  return (
    <section>
      <input value={name} onChange={(event) => setName(event.target.value)} />
      <button disabled={isPending} onClick={handleSubmit}>
        {isPending ? 'Saving...' : 'Save'}
      </button>
      {error && <p role="alert">{error}</p>}
    </section>
  );
}
```

**Điểm cần nhớ:**

- Action không thay thế toàn bộ data library.
- Action hợp nhất cho mutation/form UX.
- Với app có cache phức tạp, vẫn cần React Query, SWR, Relay hoặc framework cache.

### 3.2. ✅ `useActionState` - form state + action result + pending

`useActionState` nhận một Action và trả về:

```tsx
const [state, formAction, isPending] = useActionState(action, initialState);
```

Nó phù hợp khi form cần:

- pending state
- validation result
- error message
- state trả về từ server/API
- progressive enhancement khi framework hỗ trợ form action tốt

```tsx
import { useActionState } from 'react';

type FormState = {
  ok: boolean;
  message: string;
};

async function submitEmail(
  _previousState: FormState,
  formData: FormData
): Promise<FormState> {
  const email = String(formData.get('email') ?? '');

  if (!email.includes('@')) {
    return { ok: false, message: 'Email không hợp lệ' };
  }

  const response = await fetch('/api/newsletter', {
    method: 'POST',
    body: JSON.stringify({ email }),
  });

  if (!response.ok) {
    return { ok: false, message: 'Không thể đăng ký lúc này' };
  }

  return { ok: true, message: 'Đã đăng ký thành công' };
}

export function NewsletterForm() {
  const [state, action, isPending] = useActionState(submitEmail, {
    ok: false,
    message: '',
  });

  return (
    <form action={action}>
      <input name="email" type="email" autoComplete="email" />
      <button disabled={isPending}>
        {isPending ? 'Đang gửi...' : 'Đăng ký'}
      </button>
      {state.message && (
        <p role={state.ok ? 'status' : 'alert'}>{state.message}</p>
      )}
    </form>
  );
}
```

> ⚠️ React Canary từng có `useFormState` từ `react-dom`. React 19 dùng `useActionState` từ `react`.

### 3.3. ✅ `useFormStatus` - pending state cho submit button con

`useFormStatus` nằm trong `react-dom`, dùng để đọc trạng thái của form cha gần nhất. Nó rất hữu ích khi tách `SubmitButton` thành component riêng.

```tsx
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  const { pending } = useFormStatus();

  return (
    <button disabled={pending} type="submit">
      {pending ? 'Saving...' : 'Save'}
    </button>
  );
}

export function SettingsForm({ action }: { action: (formData: FormData) => void }) {
  return (
    <form action={action}>
      <input name="displayName" />
      <SubmitButton />
    </form>
  );
}
```

**Pitfall phổ biến:** gọi `useFormStatus` ngay trong component render `<form>` sẽ không đọc đúng form đó. Hook này nên nằm ở child component bên trong form.

### 3.4. ✅ `useOptimistic` - optimistic UI có kiểm soát

`useOptimistic` giúp hiển thị state tạm thời trong khi mutation đang chạy.

```tsx
import { useOptimistic } from 'react';

type Comment = {
  id: string;
  text: string;
  pending?: boolean;
};

async function createComment(text: string): Promise<Comment> {
  const response = await fetch('/api/comments', {
    method: 'POST',
    body: JSON.stringify({ text }),
  });

  if (!response.ok) {
    throw new Error('Cannot create comment');
  }

  return response.json();
}

export function CommentList({ comments }: { comments: Comment[] }) {
  const [optimisticComments, addOptimisticComment] = useOptimistic(
    comments,
    (currentComments, text: string) => [
      { id: crypto.randomUUID(), text, pending: true },
      ...currentComments,
    ]
  );

  async function action(formData: FormData) {
    const text = String(formData.get('text') ?? '').trim();

    if (!text) return;

    addOptimisticComment(text);
    await createComment(text);
  }

  return (
    <>
      <form action={action}>
        <input name="text" />
        <button type="submit">Comment</button>
      </form>

      <ul>
        {optimisticComments.map((comment) => (
          <li key={comment.id}>
            {comment.text}
            {comment.pending && <small> Đang gửi...</small>}
          </li>
        ))}
      </ul>
    </>
  );
}
```

**Senior note:**

- Optimistic UI tốt cho like, comment, add-to-cart, toggle trạng thái.
- Không nên optimistic cho giao dịch tiền, thanh toán, phân quyền, dữ liệu pháp lý.
- Vẫn cần strategy khi request fail: show error, refetch, rollback hoặc reconcile với server response.

### 3.5. ✅ `use()` - đọc Promise hoặc Context trong render

`use()` cho phép component đọc Promise hoặc Context trong render path. Khi đọc Promise chưa resolved, React có thể suspend và để `Suspense` xử lý fallback.

```tsx
import { Suspense, use } from 'react';

type Product = {
  id: string;
  name: string;
  price: number;
};

function ProductDetails({ productPromise }: { productPromise: Promise<Product> }) {
  const product = use(productPromise);

  return (
    <article>
      <h2>{product.name}</h2>
      <p>{product.price.toLocaleString('vi-VN')}đ</p>
    </article>
  );
}

export function ProductPage({ productPromise }: { productPromise: Promise<Product> }) {
  return (
    <Suspense fallback={<p>Đang tải sản phẩm...</p>}>
      <ProductDetails productPromise={productPromise} />
    </Suspense>
  );
}
```

Khác với Hooks thông thường, `use()` có thể được gọi trong điều kiện hoặc vòng lặp. Tuy nhiên, nó vẫn phải nằm trong render của component/hook và cần hiểu rõ Suspense behavior.

```tsx
import { createContext, use } from 'react';

const ThemeContext = createContext<'light' | 'dark'>('light');

function Label({ compact }: { compact: boolean }) {
  if (compact) {
    return <span>Compact</span>;
  }

  const theme = use(ThemeContext);
  return <span data-theme={theme}>Full label</span>;
}
```

### 3.6. ✅ `ref` as prop - giảm phụ thuộc vào `forwardRef`

Trong React 19, function component có thể nhận `ref` như prop.

```tsx
import type { ComponentProps, Ref } from 'react';

type InputProps = ComponentProps<'input'> & {
  ref?: Ref<HTMLInputElement>;
};

function TextInput({ ref, ...props }: InputProps) {
  return <input ref={ref} {...props} />;
}
```

Trước React 19:

```tsx
import { forwardRef } from 'react';

const TextInput = forwardRef<HTMLInputElement, React.ComponentProps<'input'>>(
  function TextInput(props, ref) {
    return <input ref={ref} {...props} />;
  }
);
```

**Migration note:**

- Component mới có thể dùng `ref` prop.
- Không cần migrate mọi `forwardRef` ngay lập tức nếu code đang ổn.
- `forwardRef` chưa phải lúc nào cũng biến mất khỏi ecosystem, vì library types và backward compatibility cần thời gian.
- `element.ref` bị deprecated; dùng `element.props.ref`.

### 3.7. ✅ Context as provider

React 19 cho phép render context object trực tiếp như provider:

```tsx
import { createContext, useContext } from 'react';

const AuthContext = createContext<{ userId: string | null }>({ userId: null });

export function AuthProvider({ children }: { children: React.ReactNode }) {
  return <AuthContext value={{ userId: 'u_123' }}>{children}</AuthContext>;
}

export function UserBadge() {
  const auth = useContext(AuthContext);
  return <span>{auth.userId ?? 'Guest'}</span>;
}
```

Cách cũ vẫn quen thuộc:

```tsx
return (
  <AuthContext.Provider value={{ userId: 'u_123' }}>
    {children}
  </AuthContext.Provider>
);
```

**Production note:** migration này nên làm bằng codemod hoặc từng vùng code. Đừng trộn quá nhiều style trong cùng một module nếu team chưa thống nhất convention.

### 3.8. ✅ Document Metadata

React 19 hỗ trợ render metadata trong component và tự hoist vào `<head>`:

```tsx
type BlogPost = {
  title: string;
  description: string;
  tags: string[];
};

export function BlogPostPage({ post }: { post: BlogPost }) {
  return (
    <article>
      <title>{post.title}</title>
      <meta name="description" content={post.description} />
      <meta name="keywords" content={post.tags.join(',')} />

      <h1>{post.title}</h1>
      <p>{post.description}</p>
    </article>
  );
}
```

Điều này hữu ích cho client-only app, streaming SSR và Server Components. Tuy nhiên:

- Framework như Next.js vẫn có metadata API riêng mạnh hơn cho route-based metadata.
- App lớn vẫn cần policy về title override, canonical URL, Open Graph, robots, i18n SEO.
- Không nên thay toàn bộ metadata solution nếu framework hiện tại đã quản lý tốt.

### 3.9. ✅ Stylesheets, async scripts và resource preloading

React 19 hỗ trợ tốt hơn cho tài nguyên nằm sâu trong component tree.

```tsx
export function ChartWidget() {
  return (
    <section>
      <link rel="stylesheet" href="/charts.css" precedence="default" />
      <h2>Revenue</h2>
      <div id="chart" />
    </section>
  );
}
```

Async script có thể được render ở nơi component cần, React sẽ deduplicate:

```tsx
export function PaymentWidget() {
  return (
    <section>
      <script async src="https://example.com/payment-sdk.js" />
      <button>Pay</button>
    </section>
  );
}
```

Resource hint APIs từ `react-dom`:

```tsx
import { preconnect, prefetchDNS, preinit, preload } from 'react-dom';

export function ProductPageShell() {
  preconnect('https://cdn.example.com');
  prefetchDNS('https://analytics.example.com');
  preload('/fonts/inter.woff2', { as: 'font' });
  preinit('/checkout.js', { as: 'script' });

  return <main>...</main>;
}
```

**Khi dùng:**

- `preconnect`: cần kết nối sớm tới origin quan trọng.
- `prefetchDNS`: chỉ resolve DNS, nhẹ hơn `preconnect`.
- `preload`: resource cần sớm trong current navigation.
- `preinit`: script/style cần load và init sớm.

### 3.10. ✅ Improved Suspense và hydration tolerance

React 19 cải thiện behavior quanh Suspense, hydration và third-party scripts/extensions:

- Hydration ít bị ảnh hưởng hơn bởi tag bất ngờ trong `<head>` hoặc `<body>` do extension/script chèn vào.
- Error reporting bớt trùng lặp hơn.
- Stylesheets có thể phối hợp tốt hơn với Suspense/streaming để tránh reveal UI trước khi CSS cần thiết load xong.

Điều này không có nghĩa là bỏ qua hydration mismatch. Các lỗi sau vẫn cần fix:

- render `Date.now()` hoặc `Math.random()` trực tiếp trong SSR markup
- đọc `localStorage` trong render server/client không nhất quán
- format locale/timezone khác nhau server và client
- branch theo `window` trong render path

### 3.11. ⚠️ Breaking changes quan trọng

| Breaking change | Trước đây | React 19 | Cách xử lý |
|---|---|---|---|
| New JSX Transform required | Có thể dùng classic transform | React 19 yêu cầu transform mới cho feature/tối ưu mới | `tsconfig.jsx = react-jsx`, Babel/SWC automatic runtime |
| Render errors | Có thể rethrow/log trùng | Không rethrow như trước; root có error callbacks | Cập nhật monitoring |
| Function `propTypes` | Runtime check trong dev | Bị ignore cho function component | Dùng TypeScript/Zod |
| Function `defaultProps` | Hoạt động | Bị remove cho function component | Dùng default parameters |
| Legacy context | `contextTypes`, `getChildContext` | Removed | Dùng `createContext` |
| String refs | `"myRef"` | Removed | Dùng callback ref hoặc `createRef` |
| Module pattern factories | Return object có `render` | Removed | Dùng function component |
| `React.createFactory` | Tạo element factory | Removed | Dùng JSX |
| `react-dom/test-utils` | Nhiều helper cũ | Removed, chỉ còn hướng migrate `act` | Import `act` từ `react`, dùng Testing Library |
| `ReactDOM.render` | Legacy root | Removed | `createRoot` |
| `ReactDOM.hydrate` | Legacy hydrate | Removed | `hydrateRoot` |
| `unmountComponentAtNode` | Unmount root cũ | Removed | `root.unmount()` |
| `findDOMNode` | Escape hatch DOM | Removed | Dùng explicit ref |
| UMD builds | Có thể load UMD script | Removed | Dùng ESM CDN hoặc bundler |
| `react-test-renderer` | Snapshot/render tree tests | Deprecated | Prefer React Testing Library |

### 3.12. TypeScript changes cần để ý

#### `useReducer` typing

React 19 cải thiện inference cho `useReducer`, nhưng cách truyền generic cũ có thể lỗi.

```tsx
import { useReducer } from 'react';

type State = { count: number };
type Action = { type: 'increment' } | { type: 'decrement' };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'increment':
      return { count: state.count + 1 };
    case 'decrement':
      return { count: state.count - 1 };
  }
}

export function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0 });

  return (
    <button onClick={() => dispatch({ type: 'increment' })}>
      {state.count}
    </button>
  );
}
```

#### JSX namespace

Nếu project/library khai báo global `JSX` types, cần kiểm tra lại vì React 19 có thay đổi về typing quanh JSX namespace. Library nội bộ nên chạy TypeScript check kỹ sau khi upgrade `@types/react`.

### 3.13. React Server Components và Server Actions

React 19 ổn định phần React Server Components dành cho framework/library, nhưng app không tự nhiên có RSC chỉ vì nâng React.

| Khái niệm | Ý nghĩa |
|---|---|
| Server Components | Component render trước ở môi trường server/build, không ship JS client không cần thiết |
| Server Actions | Async function chạy ở server và có thể được gọi từ client qua framework hỗ trợ |
| `"use server"` | Directive cho Server Action, không phải marker cho Server Component |
| `"use client"` | Directive của framework để đánh dấu boundary client component |

**Senior note:** Nếu dùng Next.js App Router, React 19 feature sẽ đi cùng framework constraints. Nếu dùng Vite SPA thuần, bạn vẫn có Actions/form hooks client-side, nhưng không tự có Server Actions/RSC như full-stack framework.

### 3.14. React Compiler không phải “mặc định có trong React 19”

React Compiler là hướng tối ưu tự động memoization, nhưng không nên xem nó là phần migration mặc định của React 19 app.

Khi phỏng vấn hoặc review migration, nói rõ:

- React 19 cung cấp API/runtime mới.
- React Compiler là tool/compiler riêng, cần cấu hình và maturity check.
- Không dùng compiler để che lỗi render architecture, state quá rộng hoặc component boundary sai.

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Install và codemod

```bash
# Khuyến nghị cho dự án lớn: nâng lên React 18.3 trước để thấy warning migration.
npm install --save-exact react@18.3.1 react-dom@18.3.1

# Sau khi xử lý warning chính, nâng lên React 19.
npm install --save-exact react@^19.0.0 react-dom@^19.0.0
npm install --save-dev --save-exact @types/react@^19.0.0 @types/react-dom@^19.0.0

# Chạy recipe migration chính thức.
npx codemod@latest react/19/migration-recipe
```

Codemod recipe thường bao gồm:

- `replace-reactdom-render`
- `replace-string-ref`
- `replace-act-import`
- `replace-use-form-state`
- `prop-types-typescript`

> ⚠️ Official recipe không bao phủ mọi TypeScript edge case. Sau codemod vẫn phải chạy `tsc`, tests và QA thủ công.

### 4.2. Update JSX transform

`tsconfig.json`:

```json
{
  "compilerOptions": {
    "jsx": "react-jsx"
  }
}
```

Babel:

```json
{
  "presets": [
    ["@babel/preset-react", { "runtime": "automatic" }]
  ]
}
```

### 4.3. `ReactDOM.render` sang `createRoot`

```tsx
// Before
import { render } from 'react-dom';
import { App } from './App';

render(<App />, document.getElementById('root'));
```

```tsx
// After
import { createRoot } from 'react-dom/client';
import { App } from './App';

const container = document.getElementById('root');

if (!container) {
  throw new Error('Root container not found');
}

createRoot(container).render(<App />);
```

### 4.4. `hydrate` sang `hydrateRoot`

```tsx
import { hydrateRoot } from 'react-dom/client';
import { App } from './App';

const container = document.getElementById('root');

if (!container) {
  throw new Error('Root container not found');
}

hydrateRoot(container, <App />);
```

### 4.5. Root error callbacks cho monitoring

```tsx
import { createRoot } from 'react-dom/client';
import { App } from './App';
import { reportError } from './observability';

createRoot(document.getElementById('root')!, {
  onCaughtError(error, errorInfo) {
    reportError(error, {
      type: 'react-caught-error',
      componentStack: errorInfo.componentStack,
    });
  },
  onUncaughtError(error, errorInfo) {
    reportError(error, {
      type: 'react-uncaught-error',
      componentStack: errorInfo.componentStack,
    });
  },
}).render(<App />);
```

### 4.6. `defaultProps` sang default parameter

```tsx
// Before
type ButtonProps = {
  variant?: 'primary' | 'secondary';
};

function Button({ variant }: ButtonProps) {
  return <button data-variant={variant}>Save</button>;
}

Button.defaultProps = {
  variant: 'primary',
};
```

```tsx
// After
type ButtonProps = {
  variant?: 'primary' | 'secondary';
};

function Button({ variant = 'primary' }: ButtonProps) {
  return <button data-variant={variant}>Save</button>;
}
```

### 4.7. `findDOMNode` sang explicit ref

```tsx
// Before
import { findDOMNode } from 'react-dom';

class LegacyInput extends React.Component {
  focus() {
    const node = findDOMNode(this) as HTMLInputElement | null;
    node?.focus();
  }

  render() {
    return <input />;
  }
}
```

```tsx
// After
import { createRef } from 'react';

class LegacyInput extends React.Component {
  private inputRef = createRef<HTMLInputElement>();

  focus() {
    this.inputRef.current?.focus();
  }

  render() {
    return <input ref={this.inputRef} />;
  }
}
```

### 4.8. React Query + React 19 Actions

React Query vẫn mạnh cho server-state cache, retry, invalidation, pagination, background refetch. React 19 Actions mạnh cho form/mutation UX. Hai thứ có thể phối hợp.

```tsx
import { useActionState } from 'react';
import { useQueryClient } from '@tanstack/react-query';

type ActionState = {
  ok: boolean;
  message: string;
};

export function RenameProjectForm({ projectId }: { projectId: string }) {
  const queryClient = useQueryClient();

  const [state, action, isPending] = useActionState(
    async (_previousState: ActionState, formData: FormData) => {
      const name = String(formData.get('name') ?? '').trim();

      if (!name) {
        return { ok: false, message: 'Tên project là bắt buộc' };
      }

      const response = await fetch(`/api/projects/${projectId}`, {
        method: 'PATCH',
        body: JSON.stringify({ name }),
      });

      if (!response.ok) {
        return { ok: false, message: 'Không thể đổi tên project' };
      }

      await queryClient.invalidateQueries({ queryKey: ['project', projectId] });
      await queryClient.invalidateQueries({ queryKey: ['projects'] });

      return { ok: true, message: 'Đã cập nhật project' };
    },
    { ok: false, message: '' }
  );

  return (
    <form action={action}>
      <input name="name" />
      <button disabled={isPending}>{isPending ? 'Saving...' : 'Save'}</button>
      {state.message && (
        <p role={state.ok ? 'status' : 'alert'}>{state.message}</p>
      )}
    </form>
  );
}
```

### 4.9. E-commerce cart với optimistic UI

```tsx
import { useOptimistic } from 'react';
import { useQueryClient } from '@tanstack/react-query';

type CartItem = {
  sku: string;
  name: string;
  quantity: number;
};

async function addToCart(sku: string) {
  const response = await fetch('/api/cart/items', {
    method: 'POST',
    body: JSON.stringify({ sku }),
  });

  if (!response.ok) {
    throw new Error('Cannot add item');
  }
}

export function AddToCartButton({
  sku,
  initialCart,
}: {
  sku: string;
  initialCart: CartItem[];
}) {
  const queryClient = useQueryClient();
  const [optimisticCart, addOptimistic] = useOptimistic(
    initialCart,
    (cart, itemSku: string) =>
      cart.map((item) =>
        item.sku === itemSku ? { ...item, quantity: item.quantity + 1 } : item
      )
  );

  async function action() {
    addOptimistic(sku);

    try {
      await addToCart(sku);
      await queryClient.invalidateQueries({ queryKey: ['cart'] });
    } catch {
      await queryClient.invalidateQueries({ queryKey: ['cart'] });
    }
  }

  const quantity = optimisticCart.find((item) => item.sku === sku)?.quantity ?? 0;

  return (
    <form action={action}>
      <button type="submit">Add to cart ({quantity})</button>
    </form>
  );
}
```

**Note:** Khi fail, example trên refetch lại cart để reconcile với server. Với flow nhạy cảm, nên show error rõ ràng thay vì im lặng.

### 4.10. Test update: import `act` từ `react`

```tsx
// Before
import { act } from 'react-dom/test-utils';
```

```tsx
// After
import { act } from 'react';
```

Với component tests, ưu tiên test theo hành vi người dùng bằng Testing Library:

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('submits newsletter form', async () => {
  render(<NewsletterForm />);

  await userEvent.type(screen.getByRole('textbox'), 'team@example.com');
  await userEvent.click(screen.getByRole('button', { name: /đăng ký/i }));

  expect(await screen.findByRole('status')).toHaveTextContent('thành công');
});
```

## 5. 🏗️ Production Notes / React Implications

### 5.1. Migration strategy cho production app

| Giai đoạn | Việc cần làm | Lý do |
|---|---|---|
| Inventory | Tìm legacy API bằng `rg` | Biết blast radius trước khi sửa |
| Dependency audit | Check React peer deps của UI libs, router, testing, state libs | Lib dùng internals có thể block upgrade |
| React 18.3 | Nâng tạm để thấy warnings | Giảm bất ngờ khi lên 19 |
| Codemod | Chạy official recipe | Giảm thao tác thủ công |
| TypeScript | Chạy `tsc --noEmit` | Bắt lỗi type từ `ref`, JSX, reducer |
| Tests | Unit/integration/e2e | Bắt regression form, routing, auth |
| Manual QA | Form, modal, focus, SSR/hydration, dashboard flow | Các lỗi UI async khó bắt bằng unit test |
| Staging/canary | Deploy nhỏ trước | Giảm rủi ro production |

### 5.2. Dependency audit nên kiểm tra gì?

```bash
rg "ReactDOM.render|ReactDOM.hydrate|findDOMNode|unmountComponentAtNode" .
rg "react-dom/test-utils|react-test-renderer|contextTypes|getChildContext" .
rg "propTypes|defaultProps|string ref|ref=\"" src
rg "SECRET_INTERNALS|__SECRET_INTERNALS" .
```

Kiểm tra thêm:

- `@testing-library/react` version tương thích React 19.
- UI libraries có hỗ trợ React 19 peer dependency.
- Router/framework version tương thích.
- State/data libs có test với React 19.
- Custom Babel/SWC/Vite/Webpack config có JSX automatic runtime.

### 5.3. Forms: Actions không thay thế validation strategy

React 19 giúp form submit gọn hơn, nhưng production form vẫn cần:

- client validation cho UX nhanh
- server validation là nguồn sự thật
- accessible error message (`role="alert"`, `aria-describedby`)
- disable duplicate submit hoặc idempotency key
- error mapping theo field
- analytics/observability cho failed submit

### 5.4. Error reporting thay đổi

Nếu monitoring đang rely vào render error bị rethrow, React 19 có thể làm metric thay đổi. Nên wire root callbacks:

- `onCaughtError` cho lỗi đã vào Error Boundary
- `onUncaughtError` cho lỗi chưa được Error Boundary bắt

Khi dùng framework, kiểm tra framework có expose root options hay có reporting layer riêng không.

### 5.5. SSR/hydration

React 19 dễ chịu hơn với third-party script/extension, nhưng SSR app vẫn phải tránh mismatch:

- Không render dữ liệu browser-only trực tiếp trên server.
- Không tạo ID random trong render nếu server/client không đồng bộ.
- Dùng `useId` cho ID cần stable.
- Đặt Suspense boundary hợp lý quanh phần data async.
- Test production build, không chỉ dev mode.

### 5.6. React Query, SWR, Relay vẫn có chỗ đứng

React 19 Actions không thay thế server-state management.

| Nhu cầu | Dùng React 19 Action | Dùng React Query/SWR/Relay |
|---|---|---|
| Submit form đơn giản | ✅ Rất hợp | Có thể không cần |
| Pending/error form state | ✅ Rất hợp | Hợp nếu đã có mutation layer |
| Cache list/detail | Không đủ | ✅ Rất hợp |
| Pagination/infinite query | Không phải mục tiêu chính | ✅ Rất hợp |
| Retry/backoff/background sync | Không phải mục tiêu chính | ✅ Rất hợp |
| Optimistic mutation có cache | Cần phối hợp | ✅ Rất hợp |

### 5.7. Accessibility khi đổi form

Khi refactor sang Actions:

- Button submit phải có text rõ ràng khi pending.
- Error phải được screen reader đọc (`role="alert"`).
- Success message nên dùng `role="status"`.
- Focus nên được đưa tới lỗi đầu tiên khi validation fail phức tạp.
- Không chỉ đổi màu để biểu thị error.

## 6. ⚠️ Common Pitfalls

### 6.1. Nghĩ PropTypes gây runtime error trong React 19

Sai. Với function component, `propTypes` bị bỏ check/ignore, nên nguy hiểm hơn ở chỗ lỗi có thể im lặng. Migration nên chuyển sang TypeScript hoặc runtime schema như Zod ở API boundary.

```tsx
import { z } from 'zod';

const UserSchema = z.object({
  id: z.string(),
  name: z.string(),
});

async function fetchUser() {
  const response = await fetch('/api/me');
  return UserSchema.parse(await response.json());
}
```

### 6.2. Dùng `useOptimistic` cho mọi mutation

Không phải mutation nào cũng nên optimistic. Ví dụ payment, permission, banking transfer nên ưu tiên confirmed state.

### 6.3. Bỏ qua duplicate submit

`isPending` giúp disable button, nhưng production API vẫn nên idempotent. User có thể double click, retry, back/forward hoặc submit từ nhiều tab.

### 6.4. Chạy codemod rồi merge ngay

Codemod có thể đổi đúng syntax nhưng sai intention. Cần review những vùng:

- forwarded refs ở component library
- context provider public API
- tests dùng implementation details
- old class components
- custom JSX factory/runtime config

### 6.5. Dùng `use()` mà không có Suspense boundary

Nếu Promise suspend mà không có boundary hợp lý, UX loading sẽ xấu hoặc error khó debug.

### 6.6. Nhầm `"use server"` là Server Component marker

`"use server"` dùng cho Server Actions. Server Components không có directive riêng. Framework quyết định server/client boundary.

### 6.7. Dùng metadata native thay toàn bộ framework metadata

React 19 metadata native hữu ích, nhưng route-level metadata, canonical, Open Graph và i18n SEO thường framework xử lý tốt hơn.

### 6.8. Không update tests

`react-dom/test-utils` và `react-test-renderer` là vùng rủi ro lớn. Test nên chuyển dần sang user behavior thay vì snapshot tree quá chi tiết.

### 6.9. Không kiểm tra third-party dependency dùng React internals

Lib dùng `SECRET_INTERNALS` hoặc assumptions về Fiber internals có thể vỡ khi nâng React. Đây là rủi ro production hơn là lỗi syntax.

### 6.10. Đổi `forwardRef` hàng loạt trong library public API

Nếu package được nhiều app dùng, migration `ref` as prop cần cân nhắc versioning. Public types thay đổi có thể ảnh hưởng consumer đang ở React 18.

## 7. ✅ Decision Guide / Checklist

### 7.1. Khi nào nên migrate lên React 19?

| Tình huống | Khuyến nghị |
|---|---|
| App mới, stack hiện đại | Nên dùng React 19 |
| App React 18 ít legacy API | Migrate khá thẳng |
| App dùng nhiều class/legacy context/findDOMNode | Audit kỹ trước |
| Design system dùng `forwardRef` nhiều | Migrate từng bước, giữ compatibility |
| App SSR/Next/Remix lớn | Check framework version trước |
| Test suite phụ thuộc `react-test-renderer` | Plan refactor tests |
| Có nhiều dependency cũ | Kiểm tra peer dependency và issue tracker |

### 7.2. Checklist trước khi upgrade

- [ ] Tạo branch riêng.
- [ ] Commit sạch trước khi chạy codemod.
- [ ] Nâng thử React 18.3 và xử lý warnings chính.
- [ ] Audit legacy APIs bằng `rg`.
- [ ] Kiểm tra framework/router/test libs hỗ trợ React 19.
- [ ] Bật new JSX transform.
- [ ] Cập nhật `react`, `react-dom`, `@types/react`, `@types/react-dom`.
- [ ] Chạy `npx codemod@latest react/19/migration-recipe`.
- [ ] Chạy TypeScript check.
- [ ] Chạy unit/integration/e2e tests.
- [ ] QA form submit, auth, modal/focus, routing, SSR/hydration.
- [ ] Kiểm tra console warning/error trong production build.
- [ ] Deploy staging/canary trước production full rollout.

### 7.3. Checklist code review migration

- [ ] Không còn `ReactDOM.render` / `ReactDOM.hydrate`.
- [ ] Không còn `findDOMNode`.
- [ ] Không còn string refs.
- [ ] Không còn legacy context (`contextTypes`, `getChildContext`).
- [ ] Function component không dựa vào `defaultProps`.
- [ ] `propTypes` đã được thay bằng TypeScript hoặc runtime schema phù hợp.
- [ ] `act` import từ `react`.
- [ ] Form Actions có accessible error/success state.
- [ ] Optimistic UI có failure strategy.
- [ ] Root error reporting đã được kiểm tra.
- [ ] SSR/hydration không có mismatch mới.

### 7.4. Chọn API React 19 nào?

| Nhu cầu | API nên dùng | Lưu ý |
|---|---|---|
| Form submit trả về message/error | `useActionState` | Tốt cho form local/route mutation |
| Submit button nằm component con | `useFormStatus` | Hook phải ở trong form descendant |
| UI phản hồi ngay trước khi server confirm | `useOptimistic` | Cần rollback/reconcile |
| Promise render với Suspense | `use()` | Cần boundary tốt và framework support |
| Custom input expose DOM node | `ref` as prop | Check library compatibility |
| Route/page title đơn giản | metadata tags | Framework metadata vẫn có thể tốt hơn |
| Preload font/script/style | `preload`, `preinit`, `preconnect` | Dùng có chủ đích, tránh spam hints |

## 8. 🎤 Short Interview Answer

Theo em, React 19 đáng chú ý nhất ở chỗ nó đưa async mutation và form handling thành pattern chính thức hơn. Trước đây trong React 18, mỗi form thường tự quản lý `loading`, `error`, `try/catch`, optimistic state và rollback. React 19 có Actions, `useActionState`, `useFormStatus` và `useOptimistic`, nên code form/mutation có thể ngắn hơn và nhất quán hơn.

Khi migrate, em không rewrite app ngay. Em sẽ nâng lên React 18.3 trước để thấy warning, audit legacy API như `ReactDOM.render`, `findDOMNode`, string refs, legacy context, `propTypes/defaultProps`, rồi mới nâng `react`, `react-dom`, `@types/react` lên 19 và chạy official codemod. Sau đó em chạy TypeScript, tests, kiểm tra form/auth/routing/hydration và deploy staging hoặc canary.

Điểm senior cần để ý là React 19 không thay thế data fetching/cache library như React Query. Actions hợp cho mutation/form UX, còn cache, retry, invalidation, pagination vẫn cần data layer. Ngoài ra phải update error reporting vì React 19 thay đổi cách report render errors, và không nên optimistic UI cho flow nhạy cảm như payment hoặc permission.

## 9. 🧾 Ghi nhớ nhanh

- **React 19 = async UI tốt hơn**, không phải rewrite toàn bộ app.
- **Upgrade an toàn**: React 18.3 → React 19 → codemod → TypeScript/tests → staging.
- **Actions**: async transition cho mutation.
- **`useActionState`**: action result + pending + form integration.
- **`useFormStatus`**: trạng thái form cho submit button con.
- **`useOptimistic`**: optimistic UI, cần rollback/reconcile.
- **`use()`**: đọc Promise/Context trong render, phối hợp với Suspense.
- **`ref` as prop**: giảm nhu cầu `forwardRef` cho component mới.
- **PropTypes/defaultProps function component**: không còn là strategy tốt; dùng TypeScript/default parameter.
- **Legacy ReactDOM APIs**: chuyển sang `createRoot`, `hydrateRoot`, `root.unmount`.
- **Testing**: import `act` từ `react`, giảm phụ thuộc `react-test-renderer`.
- **RSC/Server Actions**: cần framework hỗ trợ, không tự có trong SPA chỉ vì nâng React.

## 10. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| Action | Async function được React hiểu như một state transition/mutation |
| `useActionState` | Hook quản lý state trả về từ Action và pending state |
| `useFormStatus` | Hook đọc trạng thái submit của form cha gần nhất |
| `useOptimistic` | Hook tạo state tạm thời trong khi mutation chưa hoàn tất |
| `use()` | API đọc Promise hoặc Context trong render, có thể suspend |
| Suspense | Cơ chế cho UI hiển thị fallback khi data/component chưa sẵn sàng |
| Optimistic UI | UI giả định mutation thành công trước khi server xác nhận |
| Reconcile | Đồng bộ lại UI/cache với dữ liệu thật từ server |
| Hydration | Quá trình React gắn event/state vào HTML đã render từ server |
| Hydration mismatch | Khi HTML server và render client không khớp |
| `forwardRef` | API cũ để truyền ref qua function component |
| `ref` as prop | React 19 cho phép function component nhận `ref` như prop |
| Legacy Context | Context API cũ dùng `contextTypes` và `getChildContext` |
| New JSX Transform | JSX runtime mới không cần import React chỉ để dùng JSX |
| `createRoot` | API tạo root cho client rendering từ React 18+ |
| `hydrateRoot` | API hydrate HTML SSR từ React 18+ |
| `findDOMNode` | API cũ lấy DOM node từ component instance, đã bị remove |
| UMD build | Dạng bundle script global cũ, React 19 không còn phát hành UMD |
| React Server Components | Component render ở server/build environment để giảm JS client |
| Server Actions | Function chạy ở server, được framework expose cho client gọi |
| React Query | Library quản lý server-state cache, mutations, retry, invalidation |
| Error Boundary | Component bắt lỗi render bên dưới tree để show fallback UI |

## 11. 📚 Nguồn chính thức đã đối chiếu

- React 19 Upgrade Guide: <https://react.dev/blog/2024/04/25/react-19-upgrade-guide>
- React 19 Release: <https://react.dev/blog/2024/12/05/react-19>
- `useActionState`: <https://react.dev/reference/react/useActionState>
