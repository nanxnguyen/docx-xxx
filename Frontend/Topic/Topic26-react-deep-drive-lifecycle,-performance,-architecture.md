# ⚛️ Topic26: React Deep Dive - Lifecycle, Performance, Architecture

## ⭐ Senior/Staff Summary

React ở level senior/staff không phải về học từng hook, mà về hiểu **state là snapshot, effects là sync mechanism, reconciliation là diffing algorithm, memoization là trade-off (performance vs complexity)**. Fiber architecture cho phép React pause/resume render, tối ưu UX. 

Key insights senior/staff nên biết:
- 🔄 **Render cycle**: Trigger → Render Phase (pausable) → Commit Phase (sync) → Paint. Mỗi phase có ý nghĩa khác.
- 📸 **State as snapshot**: Mỗi render là snapshot độc lập của state tại thời điểm đó, không phải "live binding".
- 🧹 **Effects là sync với external world**: Không phải tính toán. Cleanup pattern là nền tảng.
- 💾 **Memoization là trade-off**: useMemo/useCallback chỉ dùng khi thực sự cần, measure trước.
- 🎯 **Patterns giải quyết vấn đề**: HOC, Render Props, Compound, Custom Hooks - không phải "features".
- ⚡ **React 18 Concurrent**: auto batching, useTransition, useDeferredValue cho UX tốt hơn khi update nặng.
- 🖥️ **Server Components**: render ở server → no JS bundle. Boundary rules, serialization constraints, streaming.

## 🧠 Key Mental Model

### Render Cycle (4 giai đoạn)

```
Trigger (setState, prop change)
  ↓
Render Phase (pausable, no side effects)
  - Component function chạy, tính VDOM mới
  - React có thể pause để browser paint
  - Không được side effects ở đây
  ↓
Commit Phase (sync, finalize updates)
  - DOM update
  - Ref mutations
  - **Effects chạy ở đây** (sau browser paint)
  ↓
Browser Paint
  - Layout calculation
  - Painting to screen
```

**Senior insight**: Hiểu rõ phase này giúp debug hiệu năng và hiểu tại sao useLayoutEffect (runs synchronously) khác useEffect (runs after paint).

### Fiber Architecture

React 16+ dùng **Fiber** thay stack, cho phép render interruptible:
- Fiber là linked list node, mỗi component có một fiber
- Work loop có thể pause sau mỗi unit work (fiber)
- Priority lanes: user input (high) > normal updates > background work

**Tại sao quan trọng**: Concurrent rendering, Suspense, useTransition có thể làm việc vì fiber pausable.

### State as Snapshot

```ts
function Counter() {
  const [count, setCount] = useState(0);
  
  // Lần render này, count LUÔN là 0 (đó là snapshot)
  const handleClick = () => {
    setCount(count + 1); // Chỉ call setState, không thay đổi count ngay
    console.log(count);  // Vẫn in 0
  };
  
  return <button onClick={handleClick}>{count}</button>;
}
```

Mỗi render, closure capture state tại thời điểm đó. Đó là lý do functional update `setCount(prev => prev + 1)` quan trọng.

## 📚 Main Concepts

### 3.1 useState & useReducer

**useState: Primitive state**

```ts
const [count, setCount] = useState(0);

// ✅ Functional update - capture latest state
setCount(prev => prev + 1);

// ⚠️ Stale closure - có thể miss updates
setCount(count + 1);
```

Functional update tránh stale closure. Cần đặc biệt khi:
- Multiple setState calls cùng event handler
- Async callback (setTimeout, fetch)
- Custom event handlers

**Lazy initialization: Performance optimization**

```ts
// ❌ Chạy expensive function mỗi render
const [data, setData] = useState(expensiveComputation());

// ✅ Chỉ chạy 1 lần khi mount
const [data, setData] = useState(() => expensiveComputation());
```

**useReducer: Complex state logic**

Dùng `useReducer` khi:
- State là object với nhiều fields
- Multiple setState cùng event
- Logic phức tạp có dependencies

```ts
type State = { count: number; error: string | null };
type Action = 
  | { type: 'INCREMENT' }
  | { type: 'SET_ERROR'; payload: string };

function reducer(state: State, action: Action): State {
  switch (action.type) {
    case 'INCREMENT': return { ...state, count: state.count + 1 };
    case 'SET_ERROR': return { ...state, error: action.payload };
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, { count: 0, error: null });
  return <button onClick={() => dispatch({ type: 'INCREMENT' })}>{state.count}</button>;
}
```

**Decision: useState vs useReducer**

| Situation | Dùng |
|-----------|------|
| Single primitive value (string, number, boolean) | useState |
| Object với 2-3 fields, simple logic | useState với immutable spread |
| Many fields, complex logic, multiple related updates | useReducer |
| Need to pass dispatch context | useReducer |

### 3.2 useEffect & useLayoutEffect

**useEffect: Async side effects**

```ts
useEffect(() => {
  // Run AFTER render + paint
  const unsubscribe = subscribe(onData);
  
  // Cleanup: run BEFORE next effect or unmount
  return () => unsubscribe();
}, [dependencies]);
```

Dependency array:
- `undefined`: run mỗi render (⚠️ rare)
- `[]`: run 1 lần sau mount
- `[deps]`: run khi deps thay đổi

**Common pattern: fetch data**

```ts
function useData(url: string) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;

    (async () => {
      const response = await fetch(url);
      const json = await response.json();
      
      if (!cancelled) {
        setData(json);
        setLoading(false);
      }
    })();

    return () => {
      cancelled = true; // Ignore result if component unmounted
    };
  }, [url]);

  return { data, loading };
}
```

**useLayoutEffect: Synchronous, before paint**

```ts
// ❌ Jank: độ cao component thay đổi sau paint
useEffect(() => {
  setHeight(ref.current.clientHeight);
}, []);

// ✅ Smooth: measure -> update -> paint cùng lúc
useLayoutEffect(() => {
  setHeight(ref.current.clientHeight);
}, []);
```

Dùng `useLayoutEffect` chỉ khi đo DOM (measurements, animation setup). 99% cases dùng `useEffect`.

### 3.3 useRef & useMemo & useCallback

**useRef: Mutable value, no re-render**

```ts
// DOM access
function TextInput() {
  const inputRef = useRef<HTMLInputElement>(null);
  
  const focus = () => inputRef.current?.focus();
  
  return (
    <>
      <input ref={inputRef} />
      <button onClick={focus}>Focus</button>
    </>
  );
}

// Mutable value across renders
function Timer() {
  const intervalIdRef = useRef<number | null>(null);
  
  const start = () => {
    intervalIdRef.current = setInterval(() => {}, 1000);
  };
  
  const stop = () => {
    if (intervalIdRef.current) clearInterval(intervalIdRef.current);
  };
  
  return <>{/* */}</>;
}
```

**useMemo: Cache expensive computation**

```ts
// ❌ Compute filter mỗi render
const filtered = items.filter(item => item.visible);

// ✅ Cache nếu items không đổi
const filtered = useMemo(
  () => items.filter(item => item.visible),
  [items]
);
```

⚠️ **Pitfall**: Lạm dụng useMemo
- Dependency array dependencies cũng là cost
- 90% cases, React fast enough
- Measure trước optimize

**useCallback: Cache function reference**

```ts
// ❌ Hàm mới mỗi render -> List component re-render
function Parent({ items }) {
  const handleDelete = (id) => {
    setItems(items.filter(item => item.id !== id));
  };
  
  return <List items={items} onDelete={handleDelete} />;
}

// ✅ Cache function -> List skipped re-render (with React.memo)
function Parent({ items }) {
  const handleDelete = useCallback(
    (id) => {
      setItems(items.filter(item => item.id !== id));
    },
    [items]
  );
  
  return <List items={items} onDelete={handleDelete} />;
}

const List = React.memo(({ items, onDelete }) => {
  return items.map(item => (
    <Item key={item.id} item={item} onDelete={onDelete} />
  ));
});
```

**Decision table: Khi nào memoize**

| Situation | useMemo/useCallback? | Lý do |
|-----------|---------------------|-------|
| Simple array filter/map | Không | React fast, dependency tracking cost |
| Heavy computation (1000+ items, complex calc) | Có | Measurable perf gain |
| Pass function to memoized child | Có | useCallback -> React.memo skips |
| Object/array dependency | Cần cẩn thận | Dependency cũng có thể thay đổi mỗi render |

### 3.4 useContext & Context Pattern

**useContext: Broadcast state**

```ts
const UserContext = React.createContext<User | null>(null);

function App() {
  const [user, setUser] = useState<User | null>(null);
  
  return (
    <UserContext.Provider value={user}>
      <Profile />
    </UserContext.Provider>
  );
}

function Profile() {
  const user = useContext(UserContext);
  return <div>{user?.name}</div>;
}
```

**Performance trap**: Context value thay đổi -> tất cả consumer re-render

```ts
// ❌ Object inline -> mỗi render là value mới -> children re-render
<UserContext.Provider value={{ user, setUser }}>

// ✅ UseMemo -> cache value
const contextValue = useMemo(() => ({ user, setUser }), [user, setUser]);
<UserContext.Provider value={contextValue}>
```

**Pattern: Tách value context và dispatch context**

```ts
const UserValueContext = React.createContext<User | null>(null);
const UserActionContext = React.createContext<{ setUser: (u: User) => void } | null>(null);

function App() {
  const [user, setUser] = useState<User | null>(null);
  
  const value = useMemo(() => user, [user]);
  const actions = useMemo(() => ({ setUser }), []);
  
  return (
    <UserValueContext.Provider value={value}>
      <UserActionContext.Provider value={actions}>
        {/* Nếu setUser thay đổi (hiếm), chỉ action consumers re-render */}
        {/* Nếu user thay đổi, value consumers re-render */}
      </UserActionContext.Provider>
    </UserValueContext.Provider>
  );
}
```

**Khi nào dùng Context vs state management library (Zustand, Redux)?**

- Context: small app, infrequent updates, component tree không sâu
- Zustand/Redux: large app, frequent updates, nhiều unrelated components consume state

### 3.5 Custom Hooks

**Rules of hooks**:
1. Chỉ gọi hooks ở top level của component hoặc custom hook
2. Tên custom hook phải bắt đầu với `use`

**Pattern: Extract, Compose, Test**

```ts
// Extract logic vào hook
function useFetch(url: string) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<Error | null>(null);

  useEffect(() => {
    let cancelled = false;

    (async () => {
      try {
        const response = await fetch(url);
        const json = await response.json();
        if (!cancelled) {
          setData(json);
          setError(null);
        }
      } catch (e) {
        if (!cancelled) setError(e as Error);
      } finally {
        if (!cancelled) setLoading(false);
      }
    })();

    return () => {
      cancelled = true;
    };
  }, [url]);

  return { data, loading, error };
}

// Use in component
function App() {
  const { data, loading, error } = useFetch('https://api.example.com/data');
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  return <div>{JSON.stringify(data)}</div>;
}
```

**Common custom hooks** (production ready):

- `useLocalStorage(key, initial)` - persist state ở localStorage
- `useDebounce(value, delay)` - debounce value updates
- `useIntersectionObserver(ref)` - lazy load, infinite scroll
- `useAsync(fn, deps)` - handle async operations

### 3.6 React Reconciliation & Fiber

**Reconciliation**: How React updates DOM efficiently

React không update mỗi property trên mỗi DOM node. Thay vào đó:
1. Compare old VDOM vs new VDOM (diffing algorithm)
2. Identify minimal DOM updates
3. Batch DOM operations

**Why key prop matters**:

```ts
// ❌ Key = index
items.map((item, index) => <Item key={index} data={item} />)

// Nếu list reorder/insert:
// React cũng reorder DOM nodes
// State trong Item component KHÔNG reset (wrong!)
// Input value, animation state bị sai

// ✅ Key = unique id
items.map(item => <Item key={item.id} data={item} />)

// React track Item by id
// State reset khi item remove, preserved khi reorder
```

**Fiber**: Render unit trong React

Thay stack, React 16+ dùng linked list (Fiber) cho pausable rendering:
- Mỗi component là fiber node
- Work loop xử lý 1 fiber → check time budget → pause nếu cần paint
- Priority lanes: user input (high) vs batch updates (normal)

**Implication**: Concurrent rendering, Suspense, useTransition hoạt động vì fiber pausable.

### 3.7 Performance Optimization

**React.memo: Skip re-render khi props không đổi**

```ts
// ❌ Re-render mỗi khi parent render
function Item({ id, name }) {
  return <div>{name}</div>;
}

// ✅ Skip nếu props cùa
const Item = React.memo(({ id, name }) => {
  return <div>{name}</div>;
});

// Parent thay đổi, Item không re-render nếu { id, name } cùa
```

Chỉ dùng `React.memo` khi:
- Component re-render thường xuyên
- Re-render cost cao (heavy computation)
- Props thường không đổi

**Code splitting + Suspense**:

```ts
const HeavyComponent = React.lazy(() => import('./HeavyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyComponent />
    </Suspense>
  );
}
```

**Virtualization: Cho danh sách dài**

```ts
import { FixedSizeList } from 'react-window';

function LargeList({ items }) {
  const Row = ({ index, style }) => (
    <div style={style}>{items[index]}</div>
  );

  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={35}
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
}
```

### 3.8 Advanced Patterns

**HOC (Higher-Order Component)**:

```ts
function withAuth(Component: React.ComponentType) {
  return function AuthComponent(props: any) {
    const user = useAuth();
    
    if (!user) return <Redirect to="/login" />;
    
    return <Component {...props} user={user} />;
  };
}

const ProtectedPage = withAuth(Page);
```

**Render Props**:

```ts
interface DataProviderProps {
  children: (data: Data) => React.ReactNode;
}

function DataProvider({ children }: DataProviderProps) {
  const [data, setData] = useState(null);
  
  return children(data);
}

function App() {
  return (
    <DataProvider>
      {data => <PageContent data={data} />}
    </DataProvider>
  );
}
```

**Compound Components: Context-based composition**

```ts
function Tabs() {
  const [active, setActive] = useState(0);
  
  return (
    <TabContext.Provider value={{ active, setActive }}>
      <div>{/* Tabs.Tab will use context */}</div>
    </TabContext.Provider>
  );
}

Tabs.Tab = function Tab({ label, children }) {
  const { active, setActive } = useContext(TabContext);
  return (
    <button onClick={() => setActive(label)}>
      {label}
    </button>
  );
};
```

### 3.9 React 18+ Concurrent Features

**Auto batching**: Multiple setState -> 1 render

```ts
// React 17: 2 renders (setTimeout không batch)
// React 18: 1 render (auto batch)
setTimeout(() => {
  setCount(c => c + 1);
  setName('alice');
}, 1000);
```

**useTransition: Mark update as non-urgent**

```ts
const [isPending, startTransition] = useTransition();

function handleSearch(input) {
  // Urgent: update input immediately
  setInput(input);
  
  // Non-urgent: search results can wait
  startTransition(() => {
    setResults(search(input));
  });
}

return (
  <>
    <input value={input} onChange={(e) => handleSearch(e.target.value)} />
    {isPending && <div>Searching...</div>}
    {results.map(r => <Result key={r.id} result={r} />)}
  </>
);
```

**useDeferredValue: Delay expensive re-render**

```ts
const [input, setInput] = useState('');
const deferredInput = useDeferredValue(input);

function handleChange(e) {
  setInput(e.target.value); // Urgent
  // deferredInput updates after, only if no higher priority work
}

return (
  <>
    <input onChange={handleChange} />
    <SearchResults query={deferredInput} />
  </>
);
```

### 3.10 Server Components (RSC)

Server components render ở server, return stream của component nodes:

```ts
// app.js (Server Component)
async function Blog() {
  const posts = await db.getPosts();
  
  return (
    <div>
      {posts.map(post => (
        <ServerPost key={post.id} post={post} />
      ))}
    </div>
  );
}

// Cannot serialize:
// - Functions (event handlers) -> move to client component
// - Classes
// - Symbols
```

**Client component boundary**: Mark interactive parts

```ts
// app.js (Server)
import { Counter } from './counter.js'; // 'use client'

export default function Page() {
  return (
    <div>
      {/* Server rendered */}
      <h1>Title</h1>
      
      {/* Client rendered (no JS for server part) */}
      <Counter />
    </div>
  );
}
```

## 🧪 Practical TypeScript Examples

### ✅ 1. Data table với sort/filter & useReducer

```ts
interface TableState {
  items: Item[];
  sort: { field: keyof Item; asc: boolean } | null;
  filter: string;
}

type TableAction = 
  | { type: 'SET_ITEMS'; payload: Item[] }
  | { type: 'SORT'; field: keyof Item }
  | { type: 'FILTER'; query: string };

function tableReducer(state: TableState, action: TableAction): TableState {
  switch (action.type) {
    case 'SET_ITEMS':
      return { ...state, items: action.payload };
    case 'SORT': {
      const isSameField = state.sort?.field === action.field;
      return {
        ...state,
        sort: { field: action.field, asc: isSameField ? !state.sort.asc : true }
      };
    }
    case 'FILTER':
      return { ...state, filter: action.query };
  }
}

function useTable(initialItems: Item[]) {
  const [state, dispatch] = useReducer(tableReducer, {
    items: initialItems,
    sort: null,
    filter: ''
  });

  const filtered = useMemo(
    () => state.items.filter(item =>
      item.name.toLowerCase().includes(state.filter.toLowerCase())
    ),
    [state.items, state.filter]
  );

  const sorted = useMemo(
    () => state.sort
      ? [...filtered].sort((a, b) => {
          const aVal = a[state.sort.field];
          const bVal = b[state.sort.field];
          const cmp = aVal < bVal ? -1 : 1;
          return state.sort.asc ? cmp : -cmp;
        })
      : filtered,
    [filtered, state.sort]
  );

  return {
    items: sorted,
    dispatch,
    sort: state.sort,
    filter: state.filter
  };
}
```

### ✅ 2. Custom hook: useLocalStorage

```ts
function useLocalStorage<T>(key: string, initial: T) {
  const [state, setState] = useState<T>(() => {
    const stored = localStorage.getItem(key);
    return stored ? JSON.parse(stored) : initial;
  });

  const setValue = useCallback((value: T | ((prev: T) => T)) => {
    setState(prev => {
      const next = typeof value === 'function' ? (value as Function)(prev) : value;
      localStorage.setItem(key, JSON.stringify(next));
      return next;
    });
  }, [key]);

  return [state, setValue] as const;
}

// Usage
function Settings() {
  const [theme, setTheme] = useLocalStorage<'light' | 'dark'>('theme', 'light');

  return (
    <button onClick={() => setTheme(t => t === 'light' ? 'dark' : 'light')}>
      Current: {theme}
    </button>
  );
}
```

### ✅ 3. Compound component + useContext

```ts
interface TabContextType {
  active: string;
  setActive: (id: string) => void;
}

const TabContext = React.createContext<TabContextType | null>(null);

function Tabs({ children, defaultActive }: { children: React.ReactNode; defaultActive: string }) {
  const [active, setActive] = useState(defaultActive);

  return (
    <TabContext.Provider value={{ active, setActive }}>
      <div role="tablist" style={{ display: 'flex', gap: '1rem' }}>
        {children}
      </div>
    </TabContext.Provider>
  );
}

Tabs.Tab = function Tab({ id, label }: { id: string; label: string }) {
  const ctx = useContext(TabContext);
  if (!ctx) throw new Error('Tab must be inside Tabs');

  return (
    <button
      role="tab"
      aria-selected={ctx.active === id}
      onClick={() => ctx.setActive(id)}
      style={{ fontWeight: ctx.active === id ? 'bold' : 'normal' }}
    >
      {label}
    </button>
  );
};

Tabs.Panel = function Panel({ id, children }: { id: string; children: React.ReactNode }) {
  const ctx = useContext(TabContext);
  if (!ctx) throw new Error('Panel must be inside Tabs');

  return ctx.active === id ? <div role="tabpanel">{children}</div> : null;
};

// Usage
<Tabs defaultActive="about">
  <Tabs.Tab id="about" label="About" />
  <Tabs.Tab id="contact" label="Contact" />
  <Tabs.Panel id="about">
    <p>About content</p>
  </Tabs.Panel>
  <Tabs.Panel id="contact">
    <p>Contact content</p>
  </Tabs.Panel>
</Tabs>
```

## ⚛️ Production Notes / React Implications

- **Error Boundaries**: Bắt error trong render phase, không async errors. Dùng cho layout fallback.
- **Hydration mismatch**: Client initial render khác server output. Debug bằng compare HTML.
- **StrictMode dev behavior**: Effects chạy 2 lần intentionally để bắt side effect problems.
- **Memory leaks**: useEffect không cleanup listener/timer/subscription = leak.
- **useCallback dependencies**: Function mới nếu dependency thay đổi = memo không effective.

## ⚠️ Common Pitfalls

- ❌ Stale closure: setState callback bị closure cũ
- ❌ Infinite loop: useEffect setState mà không đủ dependencies
- ❌ Over-memoize: useMemo/useCallback cho mọi thứ
- ❌ Missing cleanup: event listener/subscription không remove
- ❌ Key = index: dynamic list bị sai state
- ❌ Context performance: value object inline -> all consumers re-render
- ❌ useLayoutEffect mà không cần đo DOM
- ❌ Dependencies array quên include variable
- ❌ Fetch race condition: không track cancelled
- ❌ Mutate state: `state.prop = value` thay setState

## ✅ Decision Guide / Checklist

**Chọn hook nào:**

| Use case | Hook | Lý do |
|----------|------|-------|
| Single value | useState | Simple |
| Multiple related state | useReducer | Logic clearer |
| Side effects, setup/cleanup | useEffect | Sync external state |
| Measure DOM | useLayoutEffect | Before paint |
| Cache value | useMemo | Expensive computation |
| Cache function ref | useCallback | Pass to memoized child |
| Access DOM/store value | useRef | Mutable, no re-render |
| Consume context | useContext | Share without drilling |

**Khi nào optimize:**

| Situation | Action |
|-----------|--------|
| Component re-render quá thường | Profile trước optimize |
| Heavy component không change props | React.memo |
| Long list | Virtualization |
| Expensive computation | useMemo sau profile |
| Pass function to memo child | useCallback |

## 🗣️ Short Interview Answer

Em nghĩ React ở level senior là hiểu **render cycle**: Trigger → Render Phase (pausable, không side effects) → Commit Phase (DOM update, effects run) → Paint. State là snapshot, mỗi render là closure độc lập của state tại thời điểm đó, vì vậy `setCount(prev => prev + 1)` tránh stale closure.

Về effects, chúng là cách sync external state (API call, listener, subscription) với React. Cleanup pattern là nền tảng để prevent leaks. useLayoutEffect chỉ dùng khi cần đo DOM, 99% dùng useEffect.

Memoization là trade-off. useMemo/useCallback chỉ dùng khi thực sự cần (measure trước), vì dependency tracking cũng có cost. React.memo giúp skip re-render nếu props shallow equal, nhưng mỗi component khác nhau.

Patterns (HOC, Render Props, Compound, Custom Hooks) không phải features, mà giải pháp cho composition. Custom hooks để reuse logic, testing dễ hơn.

React 18+ concurrent features (auto batching, useTransition, useDeferredValue) giúp UX khi update nặng, browser vẫn responsive vì render pausable.

Server Components phía server, no JS bundle, serialization constraints (không function). Boundary rõ giữa server/client.

Các vấn đề production: memory leaks từ missing cleanup, hydration mismatch, context performance trap, stale closure. Kỳ skill senior là debug những vấn đề này, không chỉ code features.

## 📚 Ghi nhớ nhanh

- **Render phases**: Trigger → Render (pausable) → Commit (sync) → Paint
- **State snapshot**: Mỗi render closure khác nhau, dùng functional update
- **useEffect**: Async after paint, dùng cleanup, dependencies kiểm soát run
- **useLayoutEffect**: Sync before paint, chỉ dùng đo DOM
- **useMemo/useCallback**: Trade-off, measure trước optimize
- **React.memo**: Skip re-render nếu props cùa, shallow comparison
- **Key prop**: Unique id, không index, giúp React track items
- **Fiber**: Linked list, pausable, nền tảng concurrent features
- **Context**: Broadcast, performance trap nếu value thay đổi
- **Custom hooks**: Extract logic, reuse, testing

## 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích |
|-----------|-----------|
| **Fiber** | Linked list structure React dùng cho pausable rendering |
| **Reconciliation** | Diffing algorithm để find minimal DOM updates |
| **Virtual DOM** | In-memory representation của DOM |
| **Render phase** | Tính VDOM, pausable, no side effects |
| **Commit phase** | Update DOM, run effects, sync |
| **Concurrent rendering** | Render có thể interrupt để browser paint |
| **Batching** | Gộp multiple setState → 1 render |
| **Hydration** | Client attach JS handlers vào server HTML |
| **Suspense** | Declarative loading state, works với lazy/RSC |
| **useTransition** | Mark update as non-urgent, isPending tracking |
| **useDeferredValue** | Delay expensive value update |
| **Server Components** | Render ở server, no JS bundle |
| **Client boundary** | Mark interactive parts dùng JS |
| **Stale closure** | Closure capture biến cũ |
| **Reference equality** | Object/function cùa hay khác |
| **Shallow comparison** | So sánh top-level, không nested |
| **Memoization** | Cache result để avoid recompute |
| **Memory leak** | Object không được GC vì còn reference |
| **Error boundary** | Component catch error trong render |
| **Controlled component** | Value control bởi React state |
