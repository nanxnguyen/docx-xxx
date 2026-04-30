# ⚛️ Q48: React 19 Migration Guide - Upgrade từ React 18 sang 19

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"React 19 thêm Actions (async transitions), new hooks (useActionState, useOptimistic, use), ref as prop. Breaking: PropTypes removed, createElement → jsx(), StrictMode 2 renders. Migration: npx codemod + manual fixes."**

**🔑 New Features:**

**1. ⚡ Actions - Async State Transitions (Chuyển Trạng Thái Bất Đồng Bộ):**

- **🔄 Tự động handle** pending/error states trong async operations (tự động xử lý trạng thái đang tải/lỗi)
- 💡 `useTransition` + async functions = Actions (kết hợp useTransition với hàm async)
- 🎯 `useActionState(action, initialState)` - all-in-one hook (thay thế useState + useTransition)
  - ✅ Tự động quản lý: pending state, error state, form reset
  - ✅ Progressive enhancement: Form vẫn submit được khi tắt JavaScript
- 📝 Form Actions: `<form action={serverAction}>` - auto pending/error
  - 💡 Không cần tự quản lý loading/error state nữa!

**2. 🪝 New Hooks (Hooks Mới):**

- **`useActionState`**: 🔄 Combine useState + useTransition + error handling (gộp 3 hooks thành 1)

  - 💡 Thay thế: useState + useTransition + manual error handling
  - ✅ Tự động: pending state, error state, form reset

- **`useOptimistic`**: ⚡ Optimistic UI updates (cập nhật UI lạc quan)

  - 🎯 Show immediately (hiển thị ngay lập tức) → Better UX
  - 🔄 Rollback if fail (tự động quay lại nếu lỗi) → Không cần tự code rollback

- **`use(promise)`**: 📥 Read promises/context in render (đọc promise/context trong render)
  - 💡 Suspense integration (tích hợp với Suspense)
  - ✅ Có thể gọi conditional (khác useContext phải gọi đầu component)

**3. 🎯 Ref Simplification (Đơn Giản Hóa Ref):**

- **`ref` as regular prop** - không cần `forwardRef` wrapper
  - ✅ Trước: Phải dùng `forwardRef` để nhận ref
  - ✅ Giờ: `ref` là prop bình thường như `className`, `onClick`
- 💻 `<Component ref={myRef} />` works directly (hoạt động trực tiếp)
  - ✅ Không cần wrap component trong forwardRef
  - ✅ Code sạch hơn, ít boilerplate
- 🧹 Cleaner component APIs (API component gọn gàng hơn)

**4. ⏳ Improved Suspense (Cải Thiện Suspense):**

- 🔄 Sibling Suspense boundaries không block nhau (các Suspense cùng cấp không chặn nhau)
  - ✅ Trước: 1 Suspense loading → block tất cả siblings
  - ✅ Giờ: Mỗi Suspense độc lập → UX tốt hơn
- 🛡️ Better error boundaries integration (tích hợp Error Boundary tốt hơn)
  - ✅ Error handling mượt mà hơn
  - ✅ Fallback UI hiển thị chính xác hơn

**🔑 Breaking Changes:**

**1. 🗑️ PropTypes Removed (Xóa PropTypes):**

- ⚠️ PropTypes đã bị xóa khỏi React core
- ✅ Dùng **TypeScript** hoặc **Zod** thay vì
  - 💡 TypeScript: Type checking tại compile time (tốt hơn runtime)
  - 💡 Zod: Runtime validation với TypeScript integration
- 🔧 Codemod tự động: `npx codemod react/19/remove-prop-types`
  - ✅ Tool tự động xóa PropTypes và migrate sang TypeScript

**2. 🔄 StrictMode Double Render (Render 2 Lần):**

- ⚠️ Luôn render 2 lần trong dev (even production builds)
  - 💡 Component function chạy 2 lần để detect side effects
  - ✅ Effects (useEffect) chỉ chạy 1 lần (khác React 18)
- 🎯 Để detect side effects (phát hiện side effects)
  - ✅ Giúp tìm bugs sớm hơn
  - ✅ Không ảnh hưởng performance production (chỉ dev mode)

**3. 🔧 createElement → jsx() (Thay Đổi Nội Bộ):**

- ⚙️ Internal change (thay đổi nội bộ), build tools auto-handle (tự động xử lý)
  - 💡 React 19 dùng `jsx()` thay vì `createElement()` bên trong
  - ✅ Build tools (Vite, Webpack) tự động transform
- 📝 Update Babel/SWC config nếu custom setup (cập nhật nếu có cấu hình tùy chỉnh)
  - ✅ Babel: `runtime: "automatic"`
  - ✅ TypeScript: `"jsx": "react-jsx"`

**4. 🔄 Context Changes (Thay Đổi Context):**

- ⚠️ `<Context.Provider>` deprecated → dùng `<Context>` directly
  - ✅ Trước: `<ThemeContext.Provider value="dark">`
  - ✅ Giờ: `<ThemeContext value="dark">` (ngắn gọn hơn)
- ⚠️ `Context.Consumer` deprecated → dùng `useContext` hook
  - ✅ Trước: `<Context.Consumer>{value => ...}</Context.Consumer>`
  - ✅ Giờ: `const value = useContext(Context)` (đơn giản hơn)

**⚠️ Lỗi Thường Gặp:**

- Dùng PropTypes → runtime error, migrate sang TypeScript
- Rely on single render trong StrictMode → side effects leak
- Forget `use()` chỉ call trong render (không trong conditions/loops)
- `useOptimistic` không rollback on error → phải manual handle

**💡 Kiến Thức Senior:**

- **Migration strategy**: Codemod → fix errors → incremental adoption (không cần rewrite all)
- **Server Components**: React 19 stable support (Next.js App Router)
- **Compiler (React Forget)**: Auto-memoization (experimental, beta 2024)
- **Actions vs Mutations**: Actions = client transitions, Server Actions = server mutations

**⚡ Quick Summary:**

> React 19 = Actions + useActionState + useOptimistic + ref as prop + no forwardRef. Breaking changes: React.createElement → jsx(), StrictMode 2 renders, PropTypes removed. Migration: npx codemod + manual fixes.

**💡 Ghi Nhớ:**

- 🎯 **Actions**: Async transitions tự động handle pending/error/optimistic updates
- 🔧 **New Hooks**: useActionState, useOptimistic, use (read promises/context)
- 🚀 **Ref Simplification**: ref as prop, no forwardRef needed
- ⚠️ **Breaking**: PropTypes removed, StrictMode double render, createElement → jsx()

---

## **1. React 19 - Tính Năng Mới**

### **1.1. Actions - Async State Updates**

**Vấn đề trước đây:**

```typescript
// ❌ React 18 - Manual pending/error handling (Xử lý thủ công)
function UpdateName() {
  const [name, setName] = useState(''); // Tên người dùng
  const [error, setError] = useState(null); // Lỗi (phải tự quản lý)
  const [isPending, setIsPending] = useState(false); // Trạng thái loading (phải tự quản lý)

  const handleSubmit = async () => {
    setIsPending(true); // 👉 Bật loading thủ công
    setError(null); // 👉 Reset lỗi thủ công

    try {
      const response = await updateName(name); // Gọi API
      if (response.error) {
        setError(response.error); // 👉 Set lỗi thủ công
      } else {
        redirect('/success'); // Chuyển trang khi thành công
      }
    } catch (err) {
      setError(err.message); // 👉 Bắt lỗi thủ công
    } finally {
      setIsPending(false); // 👉 Tắt loading thủ công
    }
  };

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button onClick={handleSubmit} disabled={isPending}>
        {isPending ? 'Updating...' : 'Update'}
      </button>
      {error && <p className="error">{error}</p>}
    </div>
  );
}
```

**✅ React 19 - Actions tự động:**

```typescript
// ✅ React 19 - useTransition tự động xử lý pending
function UpdateName() {
  const [name, setName] = useState(''); // Tên người dùng
  const [error, setError] = useState(null); // Chỉ cần quản lý lỗi
  const [isPending, startTransition] = useTransition(); // ⚡ isPending tự động!

  const handleSubmit = () => {
    // 🎯 Wrap async function trong startTransition → Tạo Action
    // 💡 React tự động quản lý isPending state
    startTransition(async () => {
      // 🔐 Gọi API update tên
      const error = await updateName(name);

      if (error) {
        // ❌ Có lỗi → set error state
        setError(error);
        return;
      }

      // ✅ Thành công → chuyển trang
      redirect('/success');
    });
    // ⚡ isPending tự động = true khi bắt đầu, false khi kết thúc!
    // 💡 Không cần setIsPending(true/false) nữa!
  };

  return (
    <div>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button onClick={handleSubmit} disabled={isPending}>
        Update
      </button>
      {error && <p>{error}</p>}
    </div>
  );
}

/**
 * ✅ Actions tự động:
 * - Set isPending = true khi bắt đầu
 * - Set isPending = false khi kết thúc
 * - Không cần try/catch cho pending state
 * - Tự động revert optimistic updates khi error
 */
```

---

### **1.2. useActionState - Form Handling**

```typescript
// ✅ React 19 - useActionState (thay thế useFormState)
function ChangeName() {
  // 🎯 useActionState: All-in-one hook cho form handling
  // 📦 Returns: [state, action, isPending]
  // 💡 Thay thế: useState + useTransition + manual error handling
  const [error, submitAction, isPending] = useActionState(
    // ⚡ Action function - nhận previousState và formData
    // 📝 previousState: State trước đó (có thể dùng để update)
    // 📝 formData: FormData object từ form submit
    async (previousState, formData) => {
      // 📥 Lấy giá trị từ form (tự động từ FormData)
      const name = formData.get('name');

      // 🔐 Gọi API update tên
      const error = await updateName(name);

      if (error) {
        // ❌ Return error → error state được cập nhật tự động
        return error;
      }

      // ✅ Thành công → chuyển trang
      redirect('/success');

      // 🧹 Return null → error = null (clear error state)
      return null;
    },
    null // 🎯 Initial state (error ban đầu = null)
  );

  return (
    <form action={submitAction}>
      <input type="text" name="name" />
      <button type="submit" disabled={isPending}>
        Update
      </button>
      {error && <p>{error}</p>}
    </form>
  );
}

/**
 * ✅ useActionState features:
 * - Wraps async function as Action
 * - Returns [state, action, isPending]
 * - Auto-resets form after success
 * - Supports progressive enhancement (works without JS)
 */
```

**Form Actions với useFormStatus:**

```typescript
// Component con có thể đọc form status từ parent form
import { useFormStatus } from 'react-dom';

function SubmitButton() {
  // ⚡ useFormStatus: Đọc form status từ parent <form>
  // 💡 Tự động biết form đang submit hay không (không cần props!)
  // 🎯 Chỉ dùng được trong component con của <form>
  const { pending } = useFormStatus(); // pending = true khi form đang submit

  return (
    <button type="submit" disabled={pending}>
      {/* 💬 Hiển thị text động dựa trên pending state */}
      {pending ? 'Đang gửi...' : 'Gửi'}
    </button>
  );
}

// Parent form
function MyForm() {
  return (
    <form action={submitAction}>
      {' '}
      {/* submitAction từ useActionState */}
      <input name="email" placeholder="Email của bạn" />
      <SubmitButton /> {/* ⚡ Tự động có pending state mà không cần props! */}
    </form>
  );
}
```

---

### **1.3. useOptimistic - Optimistic Updates**

```typescript
function ChangeName({ currentName, onUpdateName }) {
  // 🎯 useOptimistic: Optimistic UI updates (cập nhật UI lạc quan)
  // 📦 Returns: [optimisticState, setOptimisticState]
  // 💡 optimisticState = giá trị hiển thị ngay (có thể chưa confirm từ server)
  const [optimisticName, setOptimisticName] = useOptimistic(currentName);

  const submitAction = async (formData) => {
    // 📥 Lấy tên mới từ form
    const newName = formData.get('name');

    // ⚡ Set optimistic state NGAY LẬP TỨC (UI update instant!)
    // 🎯 UI hiển thị "Nguyễn Văn B" ngay lập tức → Better UX!
    setOptimisticName(newName);

    // 🌐 Call API (mất 2-3 giây...)
    // ⏳ User thấy UI đã update → không phải đợi
    const updatedName = await updateName(newName);

    // ✅ Update real state sau khi API thành công
    onUpdateName(updatedName);

    // 🔄 optimisticName tự động sync với currentName
    // 💡 Nếu API fail → React tự động revert về currentName
  };

  return (
    <form action={submitAction}>
      <p>Your name is: {optimisticName}</p>
      <input
        type="text"
        name="name"
        disabled={currentName !== optimisticName}
      />
    </form>
  );
}

/**
 * 🎯 useOptimistic workflow:
 *
 * 1. User clicks "Update"
 * 2. setOptimisticName('New Name') → UI shows "New Name" ngay
 * 3. API call starts (network delay...)
 * 4. API success → onUpdateName() updates real state
 * 5. optimisticName auto reverts to currentName
 *
 * ❌ Nếu API fails:
 * - React tự động revert optimisticName về currentName
 * - Không cần manual rollback!
 */
```

---

### **1.4. New API: use() - Read Promises & Context**

**Read Promises:**

```typescript
import { use, Suspense } from 'react';

function Comments({ commentsPromise }) {
  // 🎯 use(): Đọc promise trong render (tích hợp với Suspense)
  // ✅ use() suspends cho đến khi promise resolve
  // 💡 Khác với useEffect: use() chạy trong render, không phải effect
  const comments = use(commentsPromise);

  // 📊 Flow hoạt động:
  // 1️⃣ Promise chưa xong → Component "suspend" → Hiển thị fallback từ Suspense
  // 2️⃣ Promise xong → Component render với data
  // 3️⃣ Promise reject → Throw error → Error Boundary catch

  return comments.map((comment) => (
    <p key={comment.id}>{comment.text}</p> // 📝 Render danh sách comments
  ));
}

function Page({ commentsPromise }) {
  return (
    <Suspense fallback={<div>Đang tải bình luận...</div>}>
      {' '}
      {/* Hiển thị khi loading */}
      <Comments commentsPromise={commentsPromise} /> {/* Pass promise vào */}
    </Suspense>
  );
}

/**
 * ⚠️ IMPORTANT:
 * - Promise PHẢI được tạo BÊN NGOÀI component (cache)
 * - KHÔNG tạo promise trong render:
 *
 * ❌ BAD:
 * const promise = fetch('/api/comments'); // Recreate mỗi render!
 * const data = use(promise);
 *
 * ✅ GOOD:
 * const promise = useMemo(() => fetch('/api/comments'), []);
 * const data = use(promise);
 */
```

**Read Context conditionally:**

```typescript
import { use } from 'react';
import ThemeContext from './ThemeContext';

function Heading({ children }) {
  // 🚪 Early return (thoát sớm nếu không có children)
  if (children == null) {
    return null;
  }

  // ✅ use() CÓ THỂ gọi sau early return (khác useContext)
  // 💡 useContext: Phải gọi ở đầu component (Rules of Hooks)
  // 💡 use(): Linh hoạt hơn - gọi được ở bất cứ đâu trong component
  const theme = use(ThemeContext); // 📖 Đọc theme từ Context

  // 🎨 Dùng màu từ theme để style
  return <h1 style={{ color: theme.color }}>{children}</h1>;
}

/**
 * ❌ useContext KHÔNG được gọi conditional:
 *
 * if (children == null) return null;
 * const theme = useContext(ThemeContext); // ❌ ERROR
 *
 * ✅ use() CÓ THỂ gọi conditional:
 *
 * if (children == null) return null;
 * const theme = use(ThemeContext); // ✅ OK
 */
```

---

### **1.5. ref as Prop - No forwardRef**

**❌ React 18:**

```typescript
import { forwardRef } from 'react';

const MyInput = forwardRef(({ placeholder }, ref) => {
  return <input placeholder={placeholder} ref={ref} />;
});

// Usage
<MyInput ref={inputRef} placeholder="Enter name" />;
```

**✅ React 19:**

```typescript
// ✅ React 19: ref là prop bình thường, không cần forwardRef
// 💡 Trước: Phải dùng forwardRef wrapper
// 💡 Giờ: ref là prop như className, onClick...
function MyInput({ placeholder, ref }) {
  // 📦 ref giờ là prop như bình thường
  // 🎯 Không cần forwardRef wrapper nữa!
  return <input placeholder={placeholder} ref={ref} />; // 🔗 Truyền ref vào input
}

// 💻 Usage (cách dùng giống React 18)
<MyInput ref={inputRef} placeholder="Nhập tên" />;
// ✅ Truyền ref như prop bình thường
// ✅ Không cần forwardRef wrapper

/**
 * ✅ Advantages:
 * - Đơn giản hơn, less boilerplate
 * - Consistent với các props khác
 * - Tree shaking tốt hơn (không bundle forwardRef nếu không dùng)
 *
 * ⚠️ Migration:
 * - React 19 có codemod tự động: npx codemod react/19/replace-forward-ref
 */
```

**Ref cleanup:**

```typescript
// ✅ React 19 - Return cleanup function (Hàm dọn dẹp)
// 💡 Mới trong React 19: ref callback có thể return cleanup function
<input
  ref={(ref) => {
    // 🎯 Khi component mount → ref callback được gọi với DOM element
    console.log('Ref được tạo:', ref);

    // 💡 Ví dụ: Thêm event listener, focus input, setup observers...
    ref?.focus(); // 🎯 Focus vào input khi mount

    // ✅ Return cleanup function (mới trong React 19)
    // 🧹 Khi component unmount → cleanup function được gọi
    return () => {
      console.log('Dọn dẹp ref:', ref);
      // 💡 Ví dụ: Remove event listener, clear timers, disconnect observers...
      // ⚠️ Quan trọng: Tránh memory leaks!
    };
  }}
/>

/**
 * Lifecycle:
 * 1. Component mount → ref callback called với DOM element
 * 2. Component unmount → cleanup function called
 *
 * ❌ React 18:
 * - Unmount → ref callback called với null
 * - Không có cleanup function
 */
```

---

### **1.6. Context as Provider**

**❌ React 18:**

```typescript
const ThemeContext = createContext('light');

function App({ children }) {
  return <ThemeContext.Provider value="dark">{children}</ThemeContext.Provider>;
}
```

**✅ React 19:**

```typescript
const ThemeContext = createContext('light'); // Default value = 'light'

function App({ children }) {
  // ✅ React 19: Render <Context> trực tiếp thay vì <Context.Provider>
  // 💡 Ngắn gọn hơn, dễ đọc hơn
  return (
    <ThemeContext value="dark">
      {/* 🎨 Cung cấp value = 'dark' cho tất cả children */}
      {children}
      {/* 📖 Các component con có thể đọc theme = 'dark' bằng useContext */}
    </ThemeContext>
    // 📊 So sánh:
    // ❌ React 18: <ThemeContext.Provider value="dark">
    // ✅ React 19: <ThemeContext value="dark"> (ngắn gọn hơn)
  );
}

/**
 * ⚠️ Migration:
 * - <Context.Provider> vẫn work trong React 19
 * - Sẽ deprecated trong future versions
 * - Codemod: npx codemod react/19/replace-context-provider
 */
```

---

### **1.7. Document Metadata**

**❌ React 18:**

```typescript
import { Helmet } from 'react-helmet';

function BlogPost({ post }) {
  return (
    <>
      <Helmet>
        <title>{post.title}</title>
        <meta name="description" content={post.excerpt} />
      </Helmet>
      <article>{post.content}</article>
    </>
  );
}
```

**✅ React 19:**

```typescript
// ✅ React 19: Native support - không cần react-helmet
// 💡 React tự động hoist metadata tags lên <head>
function BlogPost({ post }) {
  return (
    <article>
      {/* 📄 Metadata tags - React tự động đưa lên <head> */}
      {/* 🎯 Title hiển thị trên tab browser */}
      <title>{post.title}</title>
      {/* 🔍 Mô tả cho SEO (Google, Facebook...) */}
      <meta name="description" content={post.excerpt} />
      {/* 🏷️ Keywords cho SEO */}
      <meta name="keywords" content={post.tags.join(', ')} />
      {/* 🔗 URL chính thức (tránh duplicate content) */}
      <link rel="canonical" href={`https://example.com/blog/${post.slug}`} />
      {/* 📝 Nội dung bài viết */}
      <h1>{post.title}</h1> {/* Tiêu đề bài viết */}
      <p>{post.content}</p> {/* Nội dung */}
    </article>
  );
}

/**
 * ✅ React tự động hoist <title>, <meta>, <link> lên <head>
 *
 * 🎯 Works with:
 * - Client-only apps
 * - SSR (Server-Side Rendering)
 * - Server Components
 *
 * ⚠️ Note:
 * - react-helmet vẫn hữu ích cho advanced cases (overriding, precedence)
 */
```

---

### **1.8. Stylesheet Support**

```typescript
function ComponentA() {
  return (
    <div>
      {/* 📦 Component tự quản lý CSS của mình */}
      {/* 🎨 CSS theme - precedence="default" (load sau) */}
      <link rel="stylesheet" href="/styles/theme.css" precedence="default" />

      {/* ⚡ CSS quan trọng - precedence="high" (load trước) */}
      {/* 💡 Critical CSS load trước → tránh FOUC (Flash of Unstyled Content) */}
      <link rel="stylesheet" href="/styles/critical.css" precedence="high" />

      <p className="theme-text">Nội dung A</p>
    </div>
  );
}

function ComponentB() {
  return (
    <div>
      {/* 👇 Component khác cũng có CSS riêng */}
      <link
        rel="stylesheet"
        href="/styles/layout.css"
        precedence="default"
      /> {/* CSS layout */}
      <p className="layout-text">Nội dung B</p>
      {/* ⚡ React tự động de-duplicate nếu cùng href */}
    </div>
  );
}

/**
 * ✅ React handles:
 * - De-duplication (same href chỉ load 1 lần)
 * - Ordering theo precedence (high → default → low)
 * - Suspense integration (wait for CSS load trước khi render)
 *
 * 📊 Precedence order:
 * precedence="high"    → Load trước
 * precedence="default" → Load sau
 * precedence="low"     → Load cuối
 *
 * 🎯 Use cases:
 * - Component-scoped styles
 * - Code splitting styles với components
 * - Avoid FOUC (Flash of Unstyled Content)
 */
```

---

## **2. Breaking Changes & Migration**

### **2.1. Removed: PropTypes**

**❌ React 18:**

```typescript
import PropTypes from 'prop-types';

function MyComponent({ name, age }) {
  return (
    <div>
      {name} - {age}
    </div>
  );
}

MyComponent.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number,
};
```

**✅ React 19 - Use TypeScript:**

```typescript
interface MyComponentProps {
  name: string;
  age?: number;
}

function MyComponent({ name, age }: MyComponentProps) {
  return (
    <div>
      {name} - {age}
    </div>
  );
}

/**
 * ⚠️ PropTypes REMOVED trong React 19:
 * - prop-types package vẫn có thể cài riêng
 * - Khuyến nghị: Migrate sang TypeScript
 *
 * 🔧 Migration:
 * npx codemod react/19/remove-prop-types
 */
```

---

### **2.2. StrictMode Double Rendering**

**❌ React 18:**

```typescript
// StrictMode render 2 lần trong DEV mode
<React.StrictMode>
  <App />
</React.StrictMode>

// Console logs:
// Render 1
// Render 2 (duplicate for detecting side effects)
```

**✅ React 19:**

```typescript
// StrictMode vẫn render 2 lần NHƯNG:
// - Chỉ re-run component function, KHÔNG re-run effects
// - useEffect, useLayoutEffect chỉ chạy 1 lần
// - Giảm confusion khi debug

<React.StrictMode>
  <App />
</React.StrictMode>

/**
 * 🎯 React 19 StrictMode changes:
 *
 * ✅ Render function: 2 lần (same)
 * ✅ useEffect: 1 lần (changed!)
 * ✅ useLayoutEffect: 1 lần (changed!)
 * ✅ useState initializer: 2 lần (same)
 * ✅ useMemo: 2 lần (same)
 */
```

---

### **2.3. React.createElement → jsx()**

**⚠️ Internal Change:**

```typescript
/**
 * React 19 internally:
 * - createElement() → jsx() runtime
 * - Affects bundler config (Babel, TypeScript)
 *
 * ❌ Old transform (React 17):
 * import React from 'react';
 * React.createElement('div', null, 'Hello');
 *
 * ✅ New transform (React 19):
 * import { jsx } from 'react/jsx-runtime';
 * jsx('div', { children: 'Hello' });
 *
 * 🔧 Migration:
 * - Update tsconfig.json: "jsx": "react-jsx"
 * - Update Babel: @babel/preset-react with runtime: "automatic"
 */
```

**tsconfig.json:**

```json
{
  "compilerOptions": {
    "jsx": "react-jsx", // ✅ React 19
    // "jsx": "react",  // ❌ Old (React 17)
    "target": "ES2015",
    "module": "ESNext"
  }
}
```

**Babel config:**

```json
{
  "presets": [
    [
      "@babel/preset-react",
      {
        "runtime": "automatic" // ✅ React 19
      }
    ]
  ]
}
```

---

### **2.4. useDeferredValue Initial Value**

**✅ React 19:**

```typescript
function Search({ query }) {
  // ✅ useDeferredValue(value, initialValue)
  // 👉 Lần render đầu: deferredQuery = '' (initialValue)
  // 👉 Lần render sau: deferredQuery = query (giá trị thật)
  const deferredQuery = useDeferredValue(query, ''); // Defer query updates

  return <Results query={deferredQuery} />;
  {
    /* Hiển thị kết quả */
  }
  // 📊 Timeline:
  // T0: query = 'React' → deferredQuery = '' → Hiển thị kết quả rỗng ngay
  // T1: Re-render → deferredQuery = 'React' → Hiển thị kết quả search 'React'
}

/**
 * 🎯 Workflow:
 *
 * 1. First render:
 *    - deferredQuery = '' (initialValue)
 *    - Shows empty results instantly
 *
 * 2. Background re-render:
 *    - deferredQuery = query (actual value)
 *    - Updates results with real query
 *
 * ✅ Advantages:
 * - Avoid blank screen during initial load
 * - Show placeholder/skeleton immediately
 */
```

---

## **3. Migration Guide - Step by Step**

### **📋 CÁCH 1: Migration Tự Động Bằng Tool (Khuyến Nghị)**

**Bước 1: 💾 Backup code hiện tại**

```bash
# 📝 Commit tất cả changes trước khi migrate
# ⚠️ Quan trọng: Backup trước khi thay đổi!
git add .
git commit -m "chore: backup before React 19 migration"

# 🌿 Tạo branch mới để migrate (an toàn hơn)
# 💡 Nếu có lỗi → có thể quay lại main branch
git checkout -b feature/react-19-migration
```

---

**Bước 2: 🤖 Chạy React 19 Upgrade Script (Official Tool)**

```bash
# 🎯 CÁCH DỄ NHẤT: Dùng official upgrade script
# 💡 Tool tự động migrate code → tiết kiệm thời gian!
npx react-codemod@latest upgrade

# 📋 Tool sẽ hỏi các câu hỏi:
# ? Which React version are you upgrading to?
# → Chọn: 19

# ? Select transforms to apply:
# → Chọn ALL (chọn tất cả để migrate đầy đủ):
#   ✅ replace-reactdom-render (React 18 → 19)
#   ✅ replace-forward-ref (Remove forwardRef)
#   ✅ replace-context-provider (Context.Provider → Context)
#   ✅ remove-prop-types (Remove PropTypes)

# ? Select files/directories to transform:
# → Nhập: src (hoặc đường dẫn đến code của bạn)
# 💡 Có thể chọn: src, apps, libs... (tùy cấu trúc project)
```

**Output mẫu:**

```bash
🔍 Scanning files...
Found 127 files to transform

🔧 Applying transforms...
✅ replace-reactdom-render: 3 files modified
✅ replace-forward-ref: 15 files modified
✅ replace-context-provider: 8 files modified
✅ remove-prop-types: 42 files modified

📊 Summary:
- 68 files modified
- 59 files unchanged
- 0 errors

⚠️  Please review changes before committing!
```

---

**Bước 3: 📦 Update Dependencies (Cập Nhật Thư Viện)**

```bash
# 🗑️ Xóa node_modules và package-lock.json
# 💡 Để đảm bảo cài đặt sạch, không conflict với version cũ
rm -rf node_modules package-lock.json

# ⚛️ Update React packages lên version 19
npm install react@19 react-dom@19

# 📝 Update TypeScript types cho React 19
# 💡 Quan trọng: Phải update types để TypeScript hiểu React 19 APIs
npm install --save-dev @types/react@19 @types/react-dom@19

# 🧪 Update testing libraries
# 💡 Đảm bảo testing library tương thích với React 19
npm install --save-dev @testing-library/react@latest

# 🔄 Reinstall tất cả packages
# 💡 Cài lại tất cả dependencies với version mới
npm install
```

---

**Bước 4: Update Config Files**

**tsconfig.json:**

```json
{
  "compilerOptions": {
    "jsx": "react-jsx", // ✅ Bắt buộc cho React 19
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true
  }
}
```

**vite.config.ts (nếu dùng Vite):**

```typescript
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [
    react({
      // ✅ React 19 sử dụng automatic JSX runtime
      jsxRuntime: 'automatic',
    }),
  ],
});
```

**babel.config.js (nếu dùng Babel):**

```javascript
module.exports = {
  presets: [
    [
      '@babel/preset-react',
      {
        runtime: 'automatic', // ✅ React 19 requirement
      },
    ],
  ],
};
```

---

**Bước 5: Review Changes Tự Động**

```bash
# Xem tất cả files đã thay đổi
git diff

# Một số thay đổi phổ biến:
```

**forwardRef removed:**

```typescript
// ❌ BEFORE (React 18):
const MyInput = forwardRef(({ placeholder }, ref) => {
  return <input placeholder={placeholder} ref={ref} />;
});

// ✅ AFTER (React 19 - tự động):
function MyInput({ placeholder, ref }) {
  return <input placeholder={placeholder} ref={ref} />;
}
```

**Context.Provider simplified:**

```typescript
// ❌ BEFORE:
<ThemeContext.Provider value="dark">
  {children}
</ThemeContext.Provider>

// ✅ AFTER (tự động):
<ThemeContext value="dark">
  {children}
</ThemeContext>
```

**PropTypes removed:**

```typescript
// ❌ BEFORE:
import PropTypes from 'prop-types';
MyComponent.propTypes = {
  name: PropTypes.string,
};

// ✅ AFTER (tự động xóa):
// (Nếu có TypeScript, tool giữ nguyên interface)
```

---

**Bước 6: Fix Manual Changes**

```bash
# Chạy TypeScript check
npm run tsc --noEmit

# Nếu có lỗi, fix thủ công:
```

**Common issues:**

```typescript
// ❌ Error: ref type mismatch
function MyComponent({ ref, ...props }: Props) {
  //                    ^^^ Type error

// ✅ Fix: Add ref type
import { Ref } from 'react';

function MyComponent({ ref, ...props }: Props & { ref?: Ref<HTMLInputElement> }) {
  return <input ref={ref} {...props} />;
}
```

---

**Bước 7: Run Tests**

```bash
# Chạy tất cả tests
npm test

# Nếu có test fails:
# - Update snapshots: npm test -- -u
# - Fix component logic nếu cần
```

---

**Bước 8: Test App Locally**

```bash
# Start dev server
npm run dev

# ✅ Checklist test thủ công:
# - [ ] Forms submit correctly
# - [ ] Context providers work
# - [ ] Refs work in custom components
# - [ ] No console errors
# - [ ] Performance seems normal
```

---

**Bước 9: Commit Changes**

```bash
# Review tất cả changes một lần nữa
git diff

# Add và commit
git add .
git commit -m "feat: migrate to React 19

- Run react-codemod upgrade script
- Update dependencies to React 19
- Update TypeScript types
- Update tsconfig.json jsx setting
- Fix type errors
- All tests passing"

# Push branch
git push origin feature/react-19-migration
```

---

**Bước 10: Create PR & Deploy**

```bash
# Tạo Pull Request trên GitHub/GitLab
# ✅ PR Checklist:
# - [ ] All tests passing
# - [ ] No TypeScript errors
# - [ ] No console errors in browser
# - [ ] Reviewed codemod changes
# - [ ] Updated package.json
# - [ ] Updated tsconfig.json

# Sau khi PR approved → Merge
git checkout main
git merge feature/react-19-migration

# Deploy lên staging trước
npm run deploy:staging

# Test trên staging → OK → Deploy production
npm run deploy:production
```

---

### **📋 CÁCH 2: Migration Thủ Công (Không Dùng Tool)**

<details>
<summary><strong>👉 Click để xem chi tiết (dùng khi tool không work)</strong></summary>

### **3.1. Install React 19**

```bash
# NPM
npm install react@19 react-dom@19

# Yarn
yarn add react@19 react-dom@19

# PNPM
pnpm add react@19 react-dom@19
```

---

### **3.2. Update TypeScript Types**

```bash
npm install --save-dev @types/react@19 @types/react-dom@19
```

**tsconfig.json:**

```json
{
  "compilerOptions": {
    "jsx": "react-jsx", // ✅ Update
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "target": "ES2020",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true
  }
}
```

---

### **3.3. Run Codemods Riêng Lẻ**

```bash
# Install codemod CLI
npx codemod@latest

# Replace forwardRef
npx codemod react/19/replace-forward-ref

# Replace Context.Provider
npx codemod react/19/replace-context-provider

# Remove PropTypes
npx codemod react/19/remove-prop-types

# Replace ReactDOM.render (if not migrated to React 18)
npx codemod react/19/replace-reactdom-render
```

**Manual review sau khi chạy codemods:**

```typescript
// ❌ Codemod có thể tạo code như này:
function MyComponent({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}

// ✅ Review và simplify:
function MyComponent({ ref, ...props }) {
  return <input ref={ref} {...props} />;
}
```

</details>

---

### **3.4. Update Form Handling**

**❌ Old (React 18):**

```typescript
function ContactForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      await submitForm({ name, email });
      alert('Success!');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <input value={email} onChange={(e) => setEmail(e.target.value)} />
      <button disabled={loading}>Submit</button>
      {error && <p>{error}</p>}
    </form>
  );
}
```

**✅ New (React 19):**

```typescript
function ContactForm() {
  // 👉 useActionState tự động quản lý form state
  const [error, submitAction, isPending] = useActionState(
    async (prevState, formData) => {
      // 👇 Lấy data từ form
      const data = {
        name: formData.get('name'), // Tên người dùng
        email: formData.get('email'), // Email người dùng
      };

      try {
        await submitForm(data); // Gửi form lên server
        return null; // ✅ Thành công → error = null
      } catch (err) {
        return err.message; // ❌ Lỗi → error = message
      }
    },
    null // Initial error = null
  );

  return (
    <form action={submitAction}>
      {' '}
      {/* submitAction tự động handle submit */}
      <input name="name" placeholder="Tên của bạn" />
      <input name="email" placeholder="Email của bạn" />
      <button disabled={isPending}>Gửi</button> {/* isPending tự động */}
      {error && <p className="error">{error}</p>} {/* Hiển thị lỗi nếu có */}
    </form>
  );
}

/**
 * ✅ Benefits:
 * - Less code (no useState for loading/error)
 * - Auto form reset
 * - Progressive enhancement (works without JS)
 * - Better UX với isPending state
 */
```

---

### **3.5. Remove react-helmet (Optional)**

**❌ Old:**

```typescript
import { Helmet } from 'react-helmet';

function Page() {
  return (
    <>
      <Helmet>
        <title>My Page</title>
        <meta name="description" content="..." />
      </Helmet>
      <div>Content</div>
    </>
  );
}
```

**✅ New:**

```typescript
function Page() {
  return (
    <div>
      <title>My Page</title>
      <meta name="description" content="..." />
      <div>Content</div>
    </div>
  );
}

// Uninstall
npm uninstall react-helmet
```

---

## **4. Performance Optimizations**

### **4.1. Server Components (RSC)**

**✅ React 19 stable support:**

```typescript
// app/page.tsx (Server Component - Chạy trên server)
async function BlogPost({ params }) {
  // ✅ Fetch data TRỰC TIẾP từ DATABASE trên SERVER
  const post = await db.posts.findById(params.id); // Query database
  // 👉 Không cần useEffect, không cần useState
  // 👉 Code này chạy trên server, KHÔNG gửi xuống client
  // 👉 Client chỉ nhận HTML đã render sẵn

  return (
    <article>
      <title>{post.title}</title> {/* SEO-friendly */}
      <h1>{post.title}</h1> {/* Tiêu đề bài viết */}
      <p>{post.content}</p> {/* Nội dung bài viết */}
    </article>
    // ⚡ HTML này được render sẵn trên server → Tốc độ cực nhanh!
  );
}

/**
 * ✅ Benefits:
 * - Zero client JS for data fetching
 * - Direct database access
 * - Faster initial load
 * - SEO-friendly
 *
 * 🎯 Use with:
 * - Next.js 14+ (App Router)
 * - Remix (experimental)
 */
```

---

### **4.2. Preload Resources**

```typescript
import { preload, preinit, prefetchDNS } from 'react-dom';

function App() {
  // ✅ Preload font - Tải trước font để tránh chữ nhấp nháy
  preload('/fonts/roboto.woff2', { as: 'font', type: 'font/woff2' });
  // 👉 Browser tải font NGAY khi parse HTML (không đợi CSS)

  // ✅ Preinit script - Tải VÀ chạy script ngay lập tức
  preinit('/analytics.js', { as: 'script' });
  // 👉 Script được tải + execute sớm nhất có thể

  // ✅ Prefetch DNS - Resolve DNS trước để tiết kiệm thời gian
  prefetchDNS('https://api.example.com');
  // 👉 DNS lookup trước → Khi fetch API sẽ nhanh hơn

  return <div>App</div>;
}

/**
 * ✅ Result HTML:
 * <head>
 *   <link rel="preload" href="/fonts/roboto.woff2" as="font" type="font/woff2" />
 *   <script async src="/analytics.js"></script>
 *   <link rel="dns-prefetch" href="https://api.example.com" />
 * </head>
 *
 * 🎯 Performance gains:
 * - Fonts load earlier (avoid FOIT)
 * - Scripts execute ASAP
 * - DNS resolved trước khi fetch
 */
```

---

### **4.3. Suspense Improvements**

**Pre-warming:**

```typescript
<Suspense fallback={<Spinner />}>
  <LazyComponent />
</Suspense>

/**
 * ✅ React 19 pre-warming:
 * - Khi LazyComponent suspend, React "pre-warms" cây con
 * - Chuẩn bị render trước khi data arrives
 * - Faster transition từ fallback → content
 *
 * 📊 Before (React 18):
 * Data arrives → Start render → Paint (slower)
 *
 * 📊 After (React 19):
 * Data arrives → Already prepared → Paint (faster)
 */
```

---

## **5. Compatibility & Testing**

### **5.1. React 19 + React 18 Libraries**

```typescript
/**
 * ✅ React 19 backward compatible với React 18 libraries
 *
 * Libraries vẫn work:
 * - react-router-dom v6
 * - redux, zustand
 * - react-query (TanStack Query)
 * - formik, react-hook-form
 * - material-ui, chakra-ui
 *
 * ⚠️ Check compatibility:
 * https://react.dev/blog/2024/04/25/react-19-upgrade-guide#libraries
 */
```

---

### **5.2. Testing Updates**

**React Testing Library:**

```bash
# Update to latest version
npm install --save-dev @testing-library/react@latest

# React 19 compatible version: v14+
```

**Update tests:**

```typescript
// ✅ React 19 - No changes needed for most tests
import { render, screen } from '@testing-library/react';

test('renders button', () => {
  render(<button>Click me</button>);
  expect(screen.getByRole('button')).toHaveTextContent('Click me');
});

// ✅ Test Actions
test('form submission', async () => {
  const mockSubmit = jest.fn();

  render(<MyForm onSubmit={mockSubmit} />);

  await userEvent.type(screen.getByRole('textbox'), 'John');
  await userEvent.click(screen.getByRole('button', { name: /submit/i }));

  expect(mockSubmit).toHaveBeenCalledWith({ name: 'John' });
});
```

---

## **6. Migration Checklist**

```typescript
/**
 * ✅ MIGRATION CHECKLIST:
 *
 * 📦 Dependencies:
 * - [ ] Update react@19 react-dom@19
 * - [ ] Update @types/react@19 @types/react-dom@19
 * - [ ] Update testing libraries
 *
 * 🔧 Config:
 * - [ ] tsconfig.json: "jsx": "react-jsx"
 * - [ ] Babel: runtime: "automatic"
 * - [ ] ESLint: update react version
 *
 * 🤖 Codemods:
 * - [ ] npx codemod react/19/replace-forward-ref
 * - [ ] npx codemod react/19/replace-context-provider
 * - [ ] npx codemod react/19/remove-prop-types
 *
 * 📝 Manual Updates:
 * - [ ] Replace PropTypes với TypeScript
 * - [ ] Migrate forms sang useActionState
 * - [ ] Update ref callbacks (return cleanup)
 * - [ ] Review StrictMode behavior
 *
 * 🧪 Testing:
 * - [ ] Run test suite
 * - [ ] Test forms với Actions
 * - [ ] Test Suspense boundaries
 * - [ ] Visual regression testing
 *
 * 📊 Performance:
 * - [ ] Add preload() cho critical resources
 * - [ ] Consider Server Components (Next.js 14+)
 * - [ ] Profile với React DevTools Profiler
 */
```

---

## **7. Common Issues & Solutions**

### **Issue 1: forwardRef TypeScript errors**

```typescript
// ❌ Error: Type 'ForwardRefExoticComponent' is not assignable
const MyComponent = forwardRef<HTMLInputElement, Props>((props, ref) => {
  return <input ref={ref} {...props} />;
});

// ✅ Solution: Remove forwardRef
function MyComponent({
  ref,
  ...props
}: Props & { ref?: Ref<HTMLInputElement> }) {
  return <input ref={ref} {...props} />;
}
```

---

### **Issue 2: StrictMode console spam**

```typescript
// ❌ React 18: useEffect runs 2 times in DEV
useEffect(() => {
  console.log('Effect'); // Logs 2 times
}, []);

// ✅ React 19: useEffect runs 1 time in DEV
useEffect(() => {
  console.log('Effect'); // Logs 1 time
}, []);
```

---

### **Issue 3: PropTypes removed**

```typescript
// ❌ Error: Module not found: 'prop-types'
import PropTypes from 'prop-types';

MyComponent.propTypes = {
  name: PropTypes.string
};

// ✅ Solution 1: Install prop-types separately
npm install prop-types

// ✅ Solution 2: Migrate to TypeScript
interface Props {
  name: string;
}

function MyComponent({ name }: Props) {
  // ...
}
```

---

## **8. React 19 + React Query Best Practices**

### **8.1. Tổng Quan: Khi Nào Dùng React Query vs Actions**

```typescript
/**
 * 🎯 STRATEGY GUIDE:
 *
 * ✅ React Query (TanStack Query) - Dùng khi:
 * - Cần cache management phức tạp (stale time, cache invalidation)
 * - Data fetching với retry logic, polling
 * - Background refetching, prefetching
 * - Sync data across components
 * - Optimistic updates với rollback tự động
 *
 * ✅ React 19 Actions - Dùng khi:
 * - Form submissions đơn giản
 * - Progressive enhancement (no JS support)
 * - Server Actions trong Next.js
 * - Không cần cache phức tạp
 *
 * 🔥 COMBINE CẢ HAI - Best of both worlds:
 * - React Query: Data fetching + caching
 * - Actions: Form handling + optimistic updates
 */
```

---

### **8.2. Pattern 1: useMutation + useActionState**

**❌ Anti-pattern - Duplicate logic:**

```typescript
// ❌ BAD: Logic bị duplicate giữa React Query và form handling
function UpdateProfileForm() {
  const [name, setName] = useState('');
  const [isPending, setIsPending] = useState(false);
  const [error, setError] = useState(null);

  // React Query mutation
  const mutation = useMutation({
    mutationFn: updateProfile,
    onSuccess: () => queryClient.invalidateQueries(['profile']),
  });

  // Manual form handling (duplicate với mutation)
  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsPending(true);
    setError(null);

    try {
      await mutation.mutateAsync({ name });
    } catch (err) {
      setError(err.message);
    } finally {
      setIsPending(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} />
      <button disabled={isPending || mutation.isPending}>Update</button>
      {(error || mutation.error) && <p>{error || mutation.error.message}</p>}
    </form>
  );
}
```

**✅ Best Practice - Kết hợp useMutation + Actions:**

```typescript
import { useActionState } from 'react';
import { useMutation, useQueryClient } from '@tanstack/react-query';

function UpdateProfileForm() {
  const queryClient = useQueryClient();

  // 🎯 React Query mutation - Handle cache invalidation
  const mutation = useMutation({
    mutationFn: updateProfile,
    onSuccess: () => {
      // ✅ Invalidate cache để refetch data mới
      queryClient.invalidateQueries({ queryKey: ['profile'] });
    },
  });

  // 🎯 React 19 Action - Handle form state
  const [error, submitAction, isPending] = useActionState(
    async (prevState, formData) => {
      const name = formData.get('name');

      try {
        // ⚡ Dùng mutation từ React Query
        await mutation.mutateAsync({ name });
        return null; // Success
      } catch (err) {
        return err.message; // Error
      }
    },
    null
  );

  return (
    <form action={submitAction}>
      <input name="name" required />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Đang cập nhật...' : 'Cập nhật'}
      </button>
      {error && <p className="error">{error}</p>}
    </form>
  );
}

/**
 * ✅ Benefits:
 * - React Query: Cache management, invalidation
 * - Actions: Form state management (pending, error)
 * - Không duplicate logic
 * - Progressive enhancement support
 */
```

---

### **8.3. Pattern 2: Optimistic Updates - useOptimistic + React Query**

**✅ Best Practice - Kết hợp useOptimistic với React Query:**

```typescript
import { useOptimistic } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';

function TodoList() {
  const queryClient = useQueryClient();

  // 📊 Fetch todos với React Query
  const { data: todos = [] } = useQuery({
    queryKey: ['todos'],
    queryFn: fetchTodos,
  });

  // 🎯 useOptimistic - React 19 optimistic state
  const [optimisticTodos, setOptimisticTodos] = useOptimistic(todos);

  // 🔄 React Query mutation
  const addTodoMutation = useMutation({
    mutationFn: addTodo,
    onMutate: async (newTodo) => {
      // ⚡ Set optimistic state NGAY LẬP TỨC
      // 💡 UI update instant → Better UX
      setOptimisticTodos((current) => [...current, { ...newTodo, id: 'temp' }]);

      // 🛡️ Cancel ongoing queries để tránh overwrite
      await queryClient.cancelQueries({ queryKey: ['todos'] });

      // 📸 Snapshot previous value for rollback
      const previousTodos = queryClient.getQueryData(['todos']);
      return { previousTodos };
    },
    onError: (err, variables, context) => {
      // ❌ API failed → React Query tự động rollback
      // 💡 useOptimistic cũng tự động revert về todos gốc
      queryClient.setQueryData(['todos'], context.previousTodos);
    },
    onSuccess: () => {
      // ✅ API success → Invalidate để fetch data mới
      queryClient.invalidateQueries({ queryKey: ['todos'] });
    },
  });

  const handleAddTodo = async (formData) => {
    const text = formData.get('text');
    await addTodoMutation.mutateAsync({ text });
  };

  return (
    <div>
      <form action={handleAddTodo}>
        <input name="text" placeholder="Thêm todo..." />
        <button type="submit">Thêm</button>
      </form>

      <ul>
        {optimisticTodos.map((todo) => (
          <li
            key={todo.id}
            style={{ opacity: todo.id === 'temp' ? 0.5 : 1 }}
          >
            {todo.text}
          </li>
        ))}
      </ul>
    </div>
  );
}

/**
 * ✅ Double safety:
 * - useOptimistic: UI rollback tự động
 * - React Query: Cache rollback với onError
 *
 * 🎯 Best of both:
 * - Instant UI feedback
 * - Automatic error recovery
 * - Cache consistency
 */
```

---

### **8.4. Pattern 3: Server Actions + React Query (Next.js 14+)**

**✅ Server Actions với React Query cache:**

```typescript
// app/actions.ts (Server Action)
'use server';

export async function updateUserAction(formData: FormData) {
  const name = formData.get('name') as string;
  const user = await db.users.update({ name });

  // ✅ Revalidate Next.js cache
  revalidatePath('/profile');

  return user;
}

// app/profile/page.tsx (Client Component)
'use client';

import { useActionState } from 'react';
import { useQueryClient } from '@tanstack/react-query';
import { updateUserAction } from './actions';

function ProfileForm({ initialData }) {
  const queryClient = useQueryClient();

  const [error, submitAction, isPending] = useActionState(
    async (prevState, formData) => {
      try {
        // 🔐 Call Server Action
        const updatedUser = await updateUserAction(formData);

        // ✅ Update React Query cache
        queryClient.setQueryData(['user'], updatedUser);

        return null;
      } catch (err) {
        return err.message;
      }
    },
    null
  );

  return (
    <form action={submitAction}>
      <input name="name" defaultValue={initialData.name} />
      <button disabled={isPending}>Cập nhật</button>
      {error && <p>{error}</p>}
    </form>
  );
}

/**
 * 🎯 Workflow:
 * 1. User submits form → Server Action executes
 * 2. revalidatePath() → Next.js cache cleared
 * 3. setQueryData() → React Query cache updated
 * 4. UI rerenders với data mới
 *
 * ✅ Benefits:
 * - Type-safe server mutations
 * - Zero client JS for data fetching
 * - React Query cache sync
 */
```

---

### **8.5. Pattern 4: Prefetching với use() + React Query**

**✅ Streaming data với use() và React Query:**

```typescript
import { use, Suspense } from 'react';
import { useQuery } from '@tanstack/react-query';

// 🎯 Component đọc promise với use()
function UserProfile({ userPromise }) {
  // ⚡ use() suspends component cho đến khi promise resolve
  const userData = use(userPromise);

  // 📊 React Query caching cho subsequent requests
  const { data: posts } = useQuery({
    queryKey: ['posts', userData.id],
    queryFn: () => fetchUserPosts(userData.id),
    // ✅ initialData từ use() để avoid loading state
    initialData: userData.posts,
  });

  return (
    <div>
      <h1>{userData.name}</h1>
      <ul>
        {posts.map((post) => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  );
}

// Parent component
function ProfilePage({ userId }) {
  // 🚀 Prefetch user data (start fetching ASAP)
  const userPromise = useMemo(
    () => fetchUser(userId), // Promise được tạo 1 lần
    [userId]
  );

  return (
    <Suspense fallback={<ProfileSkeleton />}>
      <UserProfile userPromise={userPromise} />
    </Suspense>
  );
}

/**
 * ✅ Benefits:
 * - Prefetching starts before component renders
 * - React Query cache subsequent requests
 * - Suspense integration for loading states
 * - Faster perceived performance
 *
 * 🎯 Use case:
 * - Route transitions (prefetch next page data)
 * - Hover prefetching (preload on hover)
 * - Parallel data fetching
 */
```

---

### **8.6. Pattern 5: Background Sync với React Query**

**✅ Infinite stale time + background refetch:**

```typescript
import { useQuery } from '@tanstack/react-query';

function UserDashboard() {
  // 🎯 React Query với background sync
  const { data: user } = useQuery({
    queryKey: ['user'],
    queryFn: fetchUser,

    // ⚡ Cache settings
    staleTime: 5 * 60 * 1000, // 5 phút - Data fresh trong 5 phút
    gcTime: 10 * 60 * 1000, // 10 phút - Cache memory retention

    // 🔄 Background refetch
    refetchOnWindowFocus: true, // Refetch khi user quay lại tab
    refetchInterval: 60 * 1000, // Poll every 1 minute

    // ✅ Optimistic updates
    placeholderData: (previousData) => previousData, // Giữ old data khi refetch
  });

  // 🎯 Mutation với optimistic update
  const mutation = useMutation({
    mutationFn: updateUser,
    onMutate: async (newData) => {
      // Cancel ongoing queries
      await queryClient.cancelQueries({ queryKey: ['user'] });

      // Snapshot previous
      const previous = queryClient.getQueryData(['user']);

      // ⚡ Optimistically update
      queryClient.setQueryData(['user'], (old) => ({ ...old, ...newData }));

      return { previous };
    },
    onError: (err, variables, context) => {
      // Rollback on error
      queryClient.setQueryData(['user'], context.previous);
    },
    onSettled: () => {
      // Always refetch after mutation
      queryClient.invalidateQueries({ queryKey: ['user'] });
    },
  });

  return (
    <div>
      <h1>{user?.name}</h1>
      {/* Form với React 19 Actions */}
      <UpdateForm mutation={mutation} />
    </div>
  );
}

/**
 * ✅ Best practices:
 * - staleTime = 5 min → Reduce unnecessary requests
 * - refetchOnWindowFocus → Always fresh when user returns
 * - placeholderData → Prevent UI flicker
 * - Optimistic updates → Instant feedback
 */
```

---

### **8.7. Pattern 6: Error Handling - Error Boundary + React Query**

**✅ Centralized error handling:**

```typescript
import { QueryErrorResetBoundary } from '@tanstack/react-query';
import { ErrorBoundary } from 'react-error-boundary';

function App() {
  return (
    <QueryErrorResetBoundary>
      {({ reset }) => (
        <ErrorBoundary
          onReset={reset}
          fallbackRender={({ error, resetErrorBoundary }) => (
            <div>
              <h1>Có lỗi xảy ra!</h1>
              <p>{error.message}</p>
              <button onClick={resetErrorBoundary}>Thử lại</button>
            </div>
          )}
        >
          <Dashboard />
        </ErrorBoundary>
      )}
    </QueryErrorResetBoundary>
  );
}

// Component với use() + error handling
function Dashboard() {
  const { data, error, isError } = useQuery({
    queryKey: ['dashboard'],
    queryFn: fetchDashboard,
    // ⚡ Throw errors to Error Boundary
    throwOnError: true,
    retry: 3,
    retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
  });

  if (isError) throw error; // Throw to ErrorBoundary

  return <div>{/* Dashboard UI */}</div>;
}

/**
 * ✅ Benefits:
 * - Centralized error UI
 * - Reset button clears React Query errors
 * - Automatic retry with exponential backoff
 * - Works with Suspense + use()
 */
```

---

### **8.8. Migration Guide: React Query v4 → v5 + React 19**

**Step-by-step migration:**

```bash
# 1. Update dependencies
npm install @tanstack/react-query@latest react@19 react-dom@19

# 2. Update TypeScript types
npm install --save-dev @types/react@19 @types/react-dom@19
```

**Breaking changes:**

```typescript
// ❌ React Query v4
import { useQuery } from 'react-query';

const { data } = useQuery('todos', fetchTodos, {
  cacheTime: 5 * 60 * 1000,
});

// ✅ React Query v5 + React 19
import { useQuery } from '@tanstack/react-query';

const { data } = useQuery({
  queryKey: ['todos'], // ⚠️ Must be array
  queryFn: fetchTodos,
  gcTime: 5 * 60 * 1000, // ⚠️ cacheTime → gcTime
});

/**
 * 🔧 v5 Breaking changes:
 * - cacheTime → gcTime
 * - Query keys must be arrays
 * - Package name: react-query → @tanstack/react-query
 * - onSuccess/onError removed from useQuery (use onSettled)
 */
```

---

### **8.9. Performance Checklist**

```typescript
/**
 * ✅ REACT 19 + REACT QUERY PERFORMANCE CHECKLIST:
 *
 * 📊 Data Fetching:
 * - [ ] Use staleTime để reduce unnecessary requests (5-10 min default)
 * - [ ] Enable refetchOnWindowFocus cho real-time data
 * - [ ] Use placeholderData để prevent UI flicker
 * - [ ] Prefetch với use() cho faster page loads
 *
 * 🚀 Mutations:
 * - [ ] Optimistic updates với useOptimistic + React Query
 * - [ ] Cancel ongoing queries trong onMutate
 * - [ ] Invalidate queries sau mutation success
 * - [ ] Rollback on error với onError
 *
 * 💾 Caching:
 * - [ ] Set appropriate gcTime (10 min default)
 * - [ ] Use queryClient.setQueryData cho manual cache updates
 * - [ ] Prefetch critical data với queryClient.prefetchQuery
 * - [ ] Remove unused cache với queryClient.removeQueries
 *
 * 🎯 Forms:
 * - [ ] Use useActionState cho form handling
 * - [ ] Combine với useMutation cho cache management
 * - [ ] Progressive enhancement với Server Actions
 * - [ ] Form validation trước khi call mutation
 *
 * 🛡️ Error Handling:
 * - [ ] Error Boundary + QueryErrorResetBoundary
 * - [ ] Retry logic với exponential backoff
 * - [ ] Toast notifications cho user feedback
 * - [ ] Log errors sang monitoring service (Sentry)
 *
 * 📈 Monitoring:
 * - [ ] React Query DevTools trong development
 * - [ ] Track mutation success/error rates
 * - [ ] Monitor cache hit rates
 * - [ ] Profile với React DevTools Profiler
 */
```

---

### **8.10. Common Anti-Patterns to Avoid**

```typescript
// ❌ ANTI-PATTERN 1: Creating promises in render
function BadComponent() {
  // ❌ Promise recreated every render!
  const data = use(fetch('/api/data'));
  return <div>{data}</div>;
}

// ✅ CORRECT: Memoize promise
function GoodComponent() {
  const promise = useMemo(() => fetch('/api/data'), []);
  const data = use(promise);
  return <div>{data}</div>;
}

// ❌ ANTI-PATTERN 2: Duplicate state management
function BadForm() {
  const [data, setData] = useState(null);
  const { data: queryData } = useQuery(['data'], fetchData);

  // ❌ Duplicate state!
  useEffect(() => {
    setData(queryData);
  }, [queryData]);
}

// ✅ CORRECT: Single source of truth
function GoodForm() {
  // ✅ React Query as single source
  const { data } = useQuery({ queryKey: ['data'], queryFn: fetchData });
  return <div>{data}</div>;
}

// ❌ ANTI-PATTERN 3: Not canceling queries before optimistic update
const mutation = useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    // ❌ Missing cancelQueries → race condition!
    queryClient.setQueryData(['todos'], (old) => [...old, newTodo]);
  },
});

// ✅ CORRECT: Cancel queries first
const mutation = useMutation({
  mutationFn: updateTodo,
  onMutate: async (newTodo) => {
    // ✅ Cancel ongoing queries
    await queryClient.cancelQueries({ queryKey: ['todos'] });
    const previous = queryClient.getQueryData(['todos']);
    queryClient.setQueryData(['todos'], (old) => [...old, newTodo]);
    return { previous };
  },
});

/**
 * ⚠️ Common mistakes:
 * - Not memoizing promises with use()
 * - Duplicate state (React Query + useState)
 * - Missing cancelQueries → race conditions
 * - Not handling rollback on error
 * - Fetching in useEffect instead of React Query
 */
```

---

### **8.11. Real-World Example: E-commerce Cart**

```typescript
import { useActionState, useOptimistic } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';

function ShoppingCart() {
  const queryClient = useQueryClient();

  // 📊 Fetch cart data
  const { data: cart = [] } = useQuery({
    queryKey: ['cart'],
    queryFn: fetchCart,
    staleTime: 2 * 60 * 1000, // 2 minutes
  });

  // 🎯 Optimistic cart state
  const [optimisticCart, setOptimisticCart] = useOptimistic(cart);

  // ➕ Add to cart mutation
  const addMutation = useMutation({
    mutationFn: addToCart,
    onMutate: async (item) => {
      // ⚡ Optimistic update
      setOptimisticCart((current) => [...current, item]);

      await queryClient.cancelQueries({ queryKey: ['cart'] });
      const previous = queryClient.getQueryData(['cart']);

      queryClient.setQueryData(['cart'], (old = []) => [...old, item]);

      return { previous };
    },
    onError: (err, item, context) => {
      // ❌ Rollback
      queryClient.setQueryData(['cart'], context.previous);
      toast.error('Không thể thêm vào giỏ hàng');
    },
    onSuccess: () => {
      // ✅ Invalidate related queries
      queryClient.invalidateQueries({ queryKey: ['cart'] });
      queryClient.invalidateQueries({ queryKey: ['cart-count'] });
      toast.success('Đã thêm vào giỏ hàng');
    },
  });

  // 🗑️ Remove from cart mutation
  const removeMutation = useMutation({
    mutationFn: removeFromCart,
    onMutate: async (itemId) => {
      setOptimisticCart((current) => current.filter((i) => i.id !== itemId));

      await queryClient.cancelQueries({ queryKey: ['cart'] });
      const previous = queryClient.getQueryData(['cart']);

      queryClient.setQueryData(['cart'], (old = []) =>
        old.filter((i) => i.id !== itemId)
      );

      return { previous };
    },
    onError: (err, itemId, context) => {
      queryClient.setQueryData(['cart'], context.previous);
      toast.error('Không thể xóa sản phẩm');
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['cart'] });
      queryClient.invalidateQueries({ queryKey: ['cart-count'] });
    },
  });

  // 🛒 Checkout action
  const [checkoutError, checkoutAction, isCheckingOut] = useActionState(
    async (prevState, formData) => {
      try {
        const shippingInfo = {
          address: formData.get('address'),
          phone: formData.get('phone'),
        };

        await checkout({ cart, shippingInfo });

        // ✅ Clear cart sau checkout
        queryClient.setQueryData(['cart'], []);
        queryClient.invalidateQueries({ queryKey: ['orders'] });

        toast.success('Đặt hàng thành công!');
        return null;
      } catch (err) {
        return err.message;
      }
    },
    null
  );

  return (
    <div>
      <h2>Giỏ hàng ({optimisticCart.length})</h2>

      {optimisticCart.map((item) => (
        <div key={item.id} className="cart-item">
          <h3>{item.name}</h3>
          <p>{item.price.toLocaleString('vi-VN')} ₫</p>
          <button
            onClick={() => removeMutation.mutate(item.id)}
            disabled={removeMutation.isPending}
          >
            Xóa
          </button>
        </div>
      ))}

      <form action={checkoutAction}>
        <input name="address" placeholder="Địa chỉ giao hàng" required />
        <input name="phone" placeholder="Số điện thoại" required />
        <button type="submit" disabled={isCheckingOut || cart.length === 0}>
          {isCheckingOut ? 'Đang xử lý...' : 'Đặt hàng'}
        </button>
        {checkoutError && <p className="error">{checkoutError}</p>}
      </form>
    </div>
  );
}

/**
 * ✅ Features demonstrated:
 * - Optimistic updates (instant UI feedback)
 * - Multiple mutations (add, remove, checkout)
 * - Cache invalidation strategy
 * - Error handling với rollback
 * - Toast notifications
 * - Form handling với Actions
 */
```

---

## **9. Resources**

```typescript
/**
 * 📚 Official Docs:
 * - React 19 Release: https://react.dev/blog/2024/12/05/react-19
 * - Upgrade Guide: https://react.dev/blog/2024/04/25/react-19-upgrade-guide
 * - Actions: https://react.dev/reference/react/useActionState
 * - Server Components: https://react.dev/reference/rsc/server-components
 * - TanStack Query v5: https://tanstack.com/query/latest
 * - React Query + Next.js: https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr
 *
 * 🛠️ Tools:
 * - Codemods: npx codemod@latest
 * - React DevTools: https://react.dev/learn/react-developer-tools
 * - React Query DevTools: @tanstack/react-query-devtools
 *
 * 🎯 Migration Timeline:
 * - Week 1: Update dependencies, run codemods
 * - Week 2: Manual fixes, TypeScript migration
 * - Week 3: Testing, form migrations
 * - Week 4: Performance optimizations, deploy
 */
```

---

**💡 Remember:**

> "React 19 = Less boilerplate + Better DX + Faster apps. Migration effort: Medium. Worth it: 100%!" 🚀

# 🧠 **MINDMAP – React 19 (Tóm gọn toàn bộ trong 1 trang)**

```
React 19
│
├── 1) Actions (Async State & Form)
│     ├── useActionState
│     ├── useFormStatus
│     ├── Progressive enhancement (no JS vẫn submit được)
│     ├── Auto: pending, error, reset form
│     └── Replace: manual loading/error logic
│
├── 2) useOptimistic
│     ├── Optimistic UI ngay lập tức
│     ├── Auto rollback khi error
│     └── Không cần tự viết rollback logic
│
├── 3) New Hook: use()
│     ├── Read promise (suspend)
│     ├── Read context ANYWHERE (not like useContext)
│     ├── Conditional OK
│     └── Enable streaming + Suspense
│
├── 4) New Ref Model
│     ├── ref là prop → không cần forwardRef
│     ├── ref callback return cleanup
│     └── Đơn giản hoá ref lifecycle
│
├── 5) New Context API
│     ├── <Context value="...">
│     ├── <Context.Provider> dần deprecated
│     └── Dễ đọc, ít boilerplate
│
├── 6) Metadata (title, meta, link)
│     ├── Đặt trong component
│     ├── React auto-hoist lên <head>
│     └── Không cần react-helmet
│
├── 7) Stylesheet
│     ├── <link rel="stylesheet" precedence="...">
│     ├── De-duplicate
│     ├── Coordinate với Suspense
│     └── Tránh FOUC
│
├── 8) SSR/Streaming
│     ├── Fast Refresh tốt hơn
│     ├── Pre-warm Suspense
│     └── Hỗ trợ Server Components tốt hơn
│
├── 9) Breaking Changes
│     ├── remove PropTypes
│     ├── forwardRef optional
│     ├── createElement → jsx()
│     └── StrictMode: effects chạy đúng 1 lần
│
└── 10) Migration
       ├── npx react-codemod upgrade
       ├── update tsconfig ("jsx": "react-jsx")
       ├── update dependencies
       └── Manual fix ref, context, propTypes
```

---

# 🎤 **Q&A – Bộ câu trả lời React 19 chuẩn Senior (ngắn – sắc – đúng trọng tâm)**

## **Q1. React 19 khác React 18 ở điểm gì?**

**Senior Answer:**

> “React 19 tập trung vào DX: loại bỏ boilerplate, thống nhất mô hình async thông qua Actions, hỗ trợ optimistic UI gốc, ref/context đơn giản hơn, metadata/styling built-in và tăng khả năng streaming cho SSR. Đây là bản làm React ‘nhẹ đầu’ hơn rất nhiều.”

---

## **Q2. Actions là gì và tại sao quan trọng?**

**Senior Answer:**

> “Actions là cách React chuẩn hóa xử lý async (đặc biệt form). Không cần tự quản lý pending/error/reset. Nó giúp UI có progressive enhancement — form submit được cả khi tắt JS. Đây là bước quan trọng đồng bộ hóa Client Actions và Server Actions.”

---

## **Q3. useOptimistic giải quyết vấn đề gì?**

**Senior Answer:**

> “Nó cho phép UI hiển thị kết quả ngay lập tức trước khi server trả lời, và tự rollback nếu có lỗi. Trước đây phải tự code rollback khá phức tạp.”

---

## **Q4. use() khác gì useContext?**

**Senior Answer:**

> “use() cho phép đọc promise + context ở bất kỳ chỗ nào, kể cả trong branches. Đây là nền tảng giúp React 19 hỗ trợ Streaming + Suspense ở mức tốt hơn.”

---

## **Q5. Vì sao React 19 bỏ forwardRef?**

**Senior Answer:**

> “Ref trở thành một prop bình thường — điều này làm cho component API nhất quán hơn với tất cả props khác và dễ tree-shake hơn.”

---

## **Q6. Metadata trong React 19 hoạt động thế nào?**

**Senior Answer:**

> “Chỉ cần đặt `<title>`, `<meta>`, `<link>` trong component, React sẽ tự hoist lên `<head>`. Không cần react-helmet nữa.”

---

## **Q7. Migration khó không?**

**Senior Answer:**

> “Tương đối nhẹ. 80% có thể dùng codemod để migrate: forwardRef → ref as prop, Provider → Context, remove PropTypes. Chỉ cần update tsconfig và review một số ref callback.”

--
