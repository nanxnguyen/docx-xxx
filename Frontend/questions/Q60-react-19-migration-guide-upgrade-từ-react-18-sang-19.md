# ⚛️ Q60: React 19 Migration Guide - Upgrade từ React 18 sang 19


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
    startTransition(async () => { // 👉 Wrap async function trong startTransition
      const error = await updateName(name); // Gọi API
      if (error) {
        setError(error); // Chỉ cần set lỗi
        return;
      }
      redirect('/success'); // Chuyển trang khi thành công
    });
    // ⚡ isPending tự động = true khi bắt đầu, false khi kết thúc!
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
  // 👉 [error, submitAction, isPending] = useActionState(action, initialState)
  const [error, submitAction, isPending] = useActionState(
    // 👇 Action function - nhận previousState và formData
    async (previousState, formData) => {
      const name = formData.get('name'); // Lấy giá trị từ form
      const error = await updateName(name); // Gọi API update tên
      
      if (error) {
        return error; // 👉 Return error → error state được cập nhật
      }
      
      redirect('/success'); // Chuyển trang khi thành công
      return null; // 👉 Return null → error = null
    },
    null // Initial state (error ban đầu = null)
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
  // ⚡ useFormStatus tự động đọc pending state từ parent <form>
  const { pending } = useFormStatus(); // pending = true khi form đang submit

  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Đang gửi...' : 'Gửi'} {/* Hiển thị text động */}
    </button>
  );
}

// Parent form
function MyForm() {
  return (
    <form action={submitAction}> {/* submitAction từ useActionState */}
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
  // 👉 useOptimistic(currentState) → [optimisticState, setOptimisticState]
  const [optimisticName, setOptimisticName] = useOptimistic(currentName);

  const submitAction = async (formData) => {
    const newName = formData.get('name'); // Lấy tên mới từ form
    
    // ⚡ Set optimistic state NGAY LẬP TỨC (UI update instant!)
    setOptimisticName(newName); // UI hiển thị "Nguyễn Văn B" ngay
    
    // 🌐 Call API (mất 2-3 giây...)
    const updatedName = await updateName(newName); // Backend xử lý...
    
    // ✅ Update real state sau khi API thành công
    onUpdateName(updatedName); // Cập nhật state thật
    // 👉 optimisticName tự động revert về currentName (React tự động sync)
  };

  return (
    <form action={submitAction}>
      <p>Your name is: {optimisticName}</p>
      <input type="text" name="name" disabled={currentName !== optimisticName} />
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
  // ✅ use() suspends cho đến khi promise resolve
  const comments = use(commentsPromise); // Đợi promise hoàn thành
  // 👉 Nếu promise chưa xong → Component "suspend" → Hiển thị fallback
  // 👉 Khi promise xong → Component render với data
  
  return comments.map(comment => (
    <p key={comment.id}>{comment.text}</p> // Render danh sách comments
  ));
}

function Page({ commentsPromise }) {
  return (
    <Suspense fallback={<div>Đang tải bình luận...</div>}> {/* Hiển thị khi loading */}
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
  if (children == null) {
    return null; // 👉 Early return (thoát sớm nếu không có children)
  }
  
  // ✅ use() CÓ THỂ gọi sau early return (khác useContext)
  const theme = use(ThemeContext); // Đọc theme từ Context
  // 👉 useContext KHÔNG được phép ở đây (phải gọi trước if)
  // 👉 use() linh hoạt hơn - gọi được ở bất cứ đâu trong component
  
  return <h1 style={{ color: theme.color }}>{children}</h1>; // Dùng màu từ theme
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
<MyInput ref={inputRef} placeholder="Enter name" />
```

**✅ React 19:**

```typescript
// ✅ ref là prop bình thường, không cần forwardRef
function MyInput({ placeholder, ref }) {
  // 👉 ref giờ là prop như bình thường (name, className, onClick...)
  return <input placeholder={placeholder} ref={ref} />; // Truyền ref vào input
}

// Usage (cách dùng giống React 18)
<MyInput ref={inputRef} placeholder="Nhập tên" /> {/* Truyền ref như prop */}

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
<input
  ref={(ref) => {
    console.log('Ref được tạo:', ref); // Khi component mount
    // 👉 Ví dụ: Thêm event listener, focus input, v.v.
    ref?.focus(); // Focus vào input khi mount
    
    // ✅ Return cleanup function (mới trong React 19)
    return () => {
      console.log('Dọn dẹp ref:', ref); // Khi component unmount
      // 👉 Ví dụ: Remove event listener, clear timers, v.v.
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
  return (
    <ThemeContext.Provider value="dark">
      {children}
    </ThemeContext.Provider>
  );
}
```

**✅ React 19:**

```typescript
const ThemeContext = createContext('light'); // Default value = 'light'

function App({ children }) {
  // ✅ Render <Context> trực tiếp thay vì <Context.Provider>
  return (
    <ThemeContext value="dark"> {/* Cung cấp value = 'dark' */}
      {children} {/* Các component con có thể đọc theme = 'dark' */}
    </ThemeContext>
    // 👉 React 18: <ThemeContext.Provider value="dark">
    // 👉 React 19: <ThemeContext value="dark"> (ngắn gọn hơn)
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
// ✅ Native support - không cần react-helmet
function BlogPost({ post }) {
  return (
    <article>
      {/* 👇 Metadata tags - React tự động đưa lên <head> */}
      <title>{post.title}</title> {/* Title hiển thị trên tab browser */}
      <meta name="description" content={post.excerpt} /> {/* Mô tả cho SEO */}
      <meta name="keywords" content={post.tags.join(', ')} /> {/* Keywords cho SEO */}
      <link rel="canonical" href={`https://example.com/blog/${post.slug}`} /> {/* URL chính thức */}
      
      {/* 👇 Nội dung bài viết */}
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
      {/* 👇 Component tự quản lý CSS của mình */}
      <link rel="stylesheet" href="/styles/theme.css" precedence="default" /> {/* CSS theme */}
      <link rel="stylesheet" href="/styles/critical.css" precedence="high" /> {/* CSS quan trọng - load trước */}
      <p className="theme-text">Nội dung A</p>
    </div>
  );
}

function ComponentB() {
  return (
    <div>
      {/* 👇 Component khác cũng có CSS riêng */}
      <link rel="stylesheet" href="/styles/layout.css" precedence="default" /> {/* CSS layout */}
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
  return <div>{name} - {age}</div>;
}

MyComponent.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number
};
```

**✅ React 19 - Use TypeScript:**

```typescript
interface MyComponentProps {
  name: string;
  age?: number;
}

function MyComponent({ name, age }: MyComponentProps) {
  return <div>{name} - {age}</div>;
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
  
  return <Results query={deferredQuery} />; {/* Hiển thị kết quả */}
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

**Bước 1: Backup code hiện tại**

```bash
# Commit tất cả changes trước khi migrate
git add .
git commit -m "chore: backup before React 19 migration"

# Tạo branch mới để migrate (an toàn hơn)
git checkout -b feature/react-19-migration
```

---

**Bước 2: Chạy React 19 Upgrade Script (Official Tool)**

```bash
# 🎯 CÁCH DỄ NHẤT: Dùng official upgrade script
npx react-codemod@latest upgrade

# Tool sẽ hỏi:
# ? Which React version are you upgrading to? 
# → Chọn: 19

# ? Select transforms to apply:
# → Chọn ALL (chọn tất cả):
#   ✅ replace-reactdom-render (React 18 → 19)
#   ✅ replace-forward-ref (Remove forwardRef)
#   ✅ replace-context-provider (Context.Provider → Context)
#   ✅ remove-prop-types (Remove PropTypes)

# ? Select files/directories to transform:
# → Nhập: src (hoặc đường dẫn đến code của bạn)
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

**Bước 3: Update Dependencies**

```bash
# Xóa node_modules và package-lock.json
rm -rf node_modules package-lock.json

# Update React packages
npm install react@19 react-dom@19

# Update TypeScript types
npm install --save-dev @types/react@19 @types/react-dom@19

# Update testing libraries
npm install --save-dev @testing-library/react@latest

# Reinstall tất cả packages
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
      jsxRuntime: 'automatic'
    })
  ]
});
```

**babel.config.js (nếu dùng Babel):**

```javascript
module.exports = {
  presets: [
    [
      '@babel/preset-react',
      {
        runtime: 'automatic' // ✅ React 19 requirement
      }
    ]
  ]
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
  name: PropTypes.string
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
        email: formData.get('email') // Email người dùng
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
    <form action={submitAction}> {/* submitAction tự động handle submit */}
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
function MyComponent({ ref, ...props }: Props & { ref?: Ref<HTMLInputElement> }) {
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

## **8. Resources**

```typescript
/**
 * 📚 Official Docs:
 * - React 19 Release: https://react.dev/blog/2024/12/05/react-19
 * - Upgrade Guide: https://react.dev/blog/2024/04/25/react-19-upgrade-guide
 * - Actions: https://react.dev/reference/react/useActionState
 * - Server Components: https://react.dev/reference/rsc/server-components
 * 
 * 🛠️ Tools:
 * - Codemods: npx codemod@latest
 * - React DevTools: https://react.dev/learn/react-developer-tools
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
