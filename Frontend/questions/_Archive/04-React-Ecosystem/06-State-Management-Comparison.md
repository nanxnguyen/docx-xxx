# 🗂️ Q57: So Sánh State Management - Redux vs Zustand vs Context API

## **⭐ PHIÊN BẢN TRẢ LỜI 1 PHÚT (Cho Phỏng Vấn Nhanh)**

**"State management chia làm 4 loại: Server state (React Query/SWR), Global state (Redux/Zustand/Jotai), Local state (useState), URL state (Router). 

Chọn tool dựa vào độ phức tạp: **Redux Toolkit** cho app lớn cần DevTools, time-travel debugging, strict patterns. **Zustand** cho app nhỏ/vừa cần minimal boilerplate, bundle 1KB. **Context API** chỉ dùng dependency injection, KHÔNG dùng làm state manager (re-render toàn tree). **Jotai** cho atomic updates, React Suspense.

Lỗi hay gặp: Dùng Redux cho server state (nên dùng React Query), Context API cho global state (performance issue), không normalize Redux state (nested updates khó).

Đã từng migrate project từ Redux sang Zustand, giảm bundle 12KB → 1KB, code ngắn hơn 60%, team onboard nhanh hơn. Key lesson: Không có silver bullet, chọn tool phù hợp với team size, app complexity."**

---

## **📋 TÓM TẮT CHO SENIOR/STAFF (3-4 phút)**

### **🎯 Câu Trả Lời Đầy Đủ:**

**"State management là pattern tổ chức data flow trong React app. Critical decision vì ảnh hưởng bundle size, performance, developer experience, maintainability."**

**🔑 Bảng So Sánh Chi Tiết:**

| **Khía Cạnh** | **Redux Toolkit** | **Zustand** |  **Context API** |
|---------------|-------------------|-------------|-----------|-----------------|
| **Triết lý** | Centralized store, predictable | Simple hooks-based | Atomic state | Dependency injection |
| **Bundle size** | ~12KB | **~1KB ⭐** | **~3KB** | 0KB (built-in) |
| **Boilerplate** | Medium | **Minimal ⭐** | **Minimal** | Low |
| **Performance** | Good (manual optimization) | **Excellent ⭐** | **Excellent ⭐** | Poor (re-render tree) |
| **DevTools** | **Best-in-class ⭐** | Good | Good | No |
| **Learning curve** | Steep | **Gentle ⭐** | Medium | Easy |
| **Use case** | Large apps, complex logic | Small-medium apps | Granular updates | Theme, i18n, auth |

**🎯 KHI NÀO DÙNG GÌ?**

**1. Redux Toolkit - "Pháo Đài Vững Chãi":**
```typescript
// ✅ DÙNG KHI:
- App lớn (100+ components, 10+ developers)
- Cần time-travel debugging (replay bugs)
- Cần strict patterns (onboarding team lớn)
- Complex workflows (multi-step forms, undo/redo)
- Middleware ecosystem (logging, analytics, persistence)

// ❌ KHÔNG DÙNG KHI:
- App nhỏ (MVP, prototype) → overkill
- Bundle size critical (mobile-first) → quá nặng
- Team nhỏ, move fast → quá nhiều boilerplate
```

**2. Zustand - "Dao Thụy Sĩ":**
```typescript
// ✅ DÙNG KHI:
- App nhỏ/vừa (< 50 components)
- Cần minimal boilerplate + fast iteration
- Bundle size quan trọng (1KB vs 12KB Redux)
- Performance critical (automatic selective subscriptions)
- Team nhỏ, cần onboard nhanh

// ❌ KHÔNG DÙNG KHI:
- Cần time-travel debugging phức tạp
- Cần strict patterns cho team lớn
- Cần middleware ecosystem như Redux Saga
```

**4. Context API - "MÂM CƠM CHUNG" (KHÔNG phải State Manager!):**
```typescript
// ✅ CHỈ DÙNG CHO:
- Dependency injection (theme, i18n, auth instance)
- Props drilling shallow (2-3 levels)
- Static/rarely-changing values

// ❌ TUYỆT ĐỐI KHÔNG DÙNG CHO:
- Global state thường xuyên thay đổi
- State phức tạp → re-render toàn tree → performance disaster
```

---

**⚠️ LỖI PHỔ BIẾN & CÁCH FIX:**

**1. Dùng Redux cho Server State:**
```typescript
// ❌ SAI: Dùng Redux để cache API data
const usersSlice = createSlice({
  name: 'users',
  initialState: { data: [], loading: false },
  reducers: {
    fetchUsersStart: (state) => { state.loading = true },
    fetchUsersSuccess: (state, action) => { state.data = action.payload },
  },
});

// ✅ ĐÚNG: Dùng React Query/SWR (cache, refetch, optimistic updates tự động)
const { data: users, isLoading } = useQuery({
  queryKey: ['users'], // 🔑 Key để identify query (cache key)
  queryFn: fetchUsers, // 📡 Hàm fetch data
  staleTime: 5 * 60 * 1000, // ⏱️ Cache time: Data được coi là fresh trong 5 phút
});
```

**2. Context API cho Global State:**
```typescript
// ❌ SAI: Context + useState → re-render toàn tree
const AppContext = createContext();

function App() {
  const [state, setState] = useState({ user: null, cart: [], theme: 'light' });
  // 💥 Mỗi lần setState → TOÀN BỘ tree re-render! (performance disaster)
  
  return <AppContext.Provider value={state}>...</AppContext.Provider>;
}

// ✅ ĐÚNG: Dùng Zustand → selective subscriptions
const useStore = create((set) => ({
  user: null,
  cart: [],
  theme: 'light',
  setUser: (user) => set({ user }), // 🎯 Chỉ update user field
}));

// 🎯 Chỉ component dùng `user` mới re-render (không re-render khi cart/theme thay đổi)
const user = useStore((state) => state.user);
```

**3. Không Normalize Redux State:**
```typescript
// ❌ SAI: Nested objects → updates khó
const state = {
  posts: [
    { id: 1, author: { id: 10, name: 'John' }, comments: [...] },
    { id: 2, author: { id: 10, name: 'John' }, comments: [...] },
  ],
};

// 😱 Update author.name → phải loop qua tất cả posts (O(n) complexity)

// ✅ ĐÚNG: Normalized state với Entity Adapter
const postsAdapter = createEntityAdapter();
const state = {
  // 📊 Flat structure: dễ update, không duplicate
  posts: { ids: [1, 2], entities: { 1: {...}, 2: {...} } },
  users: { ids: [10], entities: { 10: { id: 10, name: 'John' } } },
};

// 🚀 Update user.name → O(1) lookup (tìm thẳng theo ID)
```

**4. Zustand Không Dùng Immer:**
```typescript
// ❌ SAI: Mutate state trực tiếp (bug khó debug)
const useStore = create((set) => ({
  users: [],
  addUser: (user) => set((state) => {
    state.users.push(user); // 🐛 MUTATE! Bug tiềm ẩn (thay đổi object gốc)
    return state;
  }),
}));

// ✅ ĐÚNG: Dùng Immer middleware hoặc immutable updates
const useStore = create(immer((set) => ({
  users: [],
  addUser: (user) => set((state) => {
    state.users.push(user); // ✅ Immer handle immutability (tự động tạo copy)
  }),
})));

// 🔄 Hoặc không Immer - manual immutable update
addUser: (user) => set((state) => ({
  users: [...state.users, user], // ✅ Immutable (tạo array mới)
}))
```

---

**💡 KIẾN THỨC SENIOR/STAFF:**

**1. Phân Loại State Rõ Ràng:**
```typescript
const STATE_CATEGORIES = {
  // 🌐 Server State: Data từ backend
  serverState: {
    tool: 'React Query / SWR / Apollo', // 🛠️ Công cụ chuyên dụng
    examples: ['User profile', 'Products', 'Comments'], // 📋 Ví dụ
    why: 'Auto cache, refetch, optimistic updates, pagination', // 💡 Lý do
  },
  
  // 🌍 Global Client State: Shared across app
  globalClientState: {
    tool: 'Zustand / Redux / Jotai', // 🛠️ Quản lý state global
    examples: ['Theme', 'Auth status', 'Shopping cart'], // 📋 State dùng chung
    why: 'Cross-component communication', // 💡 Giao tiếp giữa components
  },
  
  // 📍 Local State: Component-specific
  localState: {
    tool: 'useState / useReducer', // 🛠️ React hooks built-in
    examples: ['Form inputs', 'Modal open', 'Hover state'], // 📋 State riêng
    why: 'Không cần share → keep local', // 💡 Giữ trong component
  },
  
  // 🔗 URL State: Synced with navigation
  urlState: {
    tool: 'React Router / Next.js router', // 🛠️ Router libraries
    examples: ['Search params', 'Filters', 'Active tab'], // 📋 State trong URL
    why: 'Shareable links, browser back/forward', // 💡 Chia sẻ được link
  },
};
  urlState: {
    tool: 'React Router / Next.js router',
    examples: ['Search params', 'Filters', 'Active tab'],
    why: 'Shareable links, browser back/forward',
  },
};
```

**2. Redux Toolkit Query (RTK Query):**
```typescript
// 📡 Built-in data fetching (alternative to React Query)
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const api = createApi({
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }), // ⚙️ Base config cho API
  endpoints: (builder) => ({
    getUsers: builder.query<User[], void>({
      query: () => 'users', // 🔗 Endpoint URL
    }),
  }),
});

// 🎣 Auto-generated hooks - tự động tạo hooks
const { data, isLoading, error } = api.useGetUsersQuery();
// ✅ Cache, refetch, polling, optimistic updates tự động
```

**3. Jotai với React Suspense:**
```typescript
// ⚛️ Async atom + Suspense boundary
const userAtom = atom(async () => {
  const res = await fetch('/api/user'); // 📡 Fetch data
  return res.json();
});

function UserProfile() {
  const user = useAtomValue(userAtom); // 💧 Suspend while loading (tự động suspend)
  return <div>{user.name}</div>;
}

function App() {
  return (
    <Suspense fallback={<Spinner />}> {/* 🔄 Hiển thị loading */}
      <UserProfile />
    </Suspense>
  );
}
// ✅ No loading state needed, Suspense handles it (không cần useState loading)
```

**4. Zustand Middleware Stack:**
```typescript
const useStore = create(
  devtools(           // 1️⃣ Layer 1: Redux DevTools (debug)
    persist(          // 2️⃣ Layer 2: LocalStorage persistence (lưu state)
      subscribeWithSelector( // 3️⃣ Layer 3: Selective subscriptions (chọn lọc re-render)
        immer((set) => ({ // 4️⃣ Layer 4: Immutable updates (update an toàn)
          count: 0,
          increment: () => set((s) => { s.count++ }),
        }))
      ),
      { name: 'app-store' } // 💾 Tên key trong localStorage
    ),
    { name: 'AppStore' } // 🔧 Tên hiển thị trong DevTools
  )
);
```

---

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)  
> **Thời gian trả lời:** 12-15 phút

---

## 📋 **Mục Lục**

1. [State Management Overview](#1-state-management-overview)
2. [Redux Toolkit](#2-redux-toolkit)
3. [Zustand](#3-zustand)
4. [Jotai](#4-jotai)
5. [Comparison Table](#5-comparison-table)
6. [Migration Strategies](#6-migration-strategies)
7. [Advanced Patterns](#7-advanced-patterns)

---

## 1. State Management Overview

### **1.1. State Categories**

```typescript
// ===================================================
// 🏗️ **STATE CATEGORIZATION**
// ===================================================

const STATE_TYPES = {
  // ✅ Server State (cached from API)
  serverState: {
    description: 'Data fetched from backend',
    examples: ['User profile', 'Product list', 'Comments'],
    bestTools: ['React Query', 'SWR', 'Apollo Client'],
  },
  
  // ✅ Global Client State (shared across app)
  globalClientState: {
    description: 'Application-wide state',
    examples: ['Theme', 'Auth status', 'Language'],
    bestTools: ['Zustand', 'Jotai', 'Redux Toolkit'],
  },
  
  // ✅ Local Component State
  localState: {
    description: 'Component-specific state',
    examples: ['Form inputs', 'Modal open/close', 'Hover state'],
    bestTools: ['useState', 'useReducer'],
  },
  
  // ✅ URL State (browser navigation)
  urlState: {
    description: 'State synced with URL',
    examples: ['Search params', 'Filters', 'Pagination'],
    bestTools: ['React Router', 'Next.js router'],
  },
};

// ===================================================
// 🎯 **DECISION TREE**
// ===================================================

function chooseStateManager(requirements: Requirements) {
  // ✅ Need DevTools & time-travel debugging?
  if (requirements.needsDevTools && requirements.complexWorkflow) {
    return 'Redux Toolkit';
  }
  
  // ✅ Need minimal boilerplate & simplicity?
  if (requirements.preferSimplicity && requirements.smallToMediumApp) {
    return 'Zustand';
  }
  
  // ✅ Need atomic updates & derived state?
  if (requirements.needsAtomicUpdates && requirements.reactSuspense) {
    return 'Jotai';
  }
  
  // ✅ Server state caching?
  if (requirements.isServerState) {
    return 'React Query or SWR';
  }
  
  return 'useState/useContext';
}
```

---

## 2. Redux Toolkit

### **2.1. Redux Toolkit Setup**

```typescript
// ===================================================
// 🔴 **REDUX TOOLKIT** (Modern Redux)
// ===================================================

import { createSlice, configureStore, PayloadAction } from '@reduxjs/toolkit';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';

// ✅ Define slice (tạo slice - 1 phần của store)
interface CounterState {
  value: number;
  status: 'idle' | 'loading' | 'succeeded' | 'failed';
}

const initialState: CounterState = {
  value: 0,
  status: 'idle',
};

const counterSlice = createSlice({
  name: 'counter', // 🏷️ Tên slice
  initialState, // 📊 State khởi tạo
  reducers: { // 🔧 Các actions để update state
    increment: (state) => {
      state.value += 1; // ✅ Immer allows direct mutation (có thể mutate trực tiếp)
    },
    
    decrement: (state) => {
      state.value -= 1;
    },
    
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload; // 📦 Nhận payload (data) từ action
    },
    
    reset: (state) => {
      state.value = 0; // 🔄 Reset về 0
    },
  },
});

export const { increment, decrement, incrementByAmount, reset } = counterSlice.actions;

// ===================================================
// 🏪 **CONFIGURE STORE** - Tạo Redux store
// ===================================================

export const store = configureStore({
  reducer: { // 🎯 Combine reducers (ghép các slices lại)
    counter: counterSlice.reducer,
    user: userSlice.reducer,
    cart: cartSlice.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: { // ⚠️ Check serializable (data phải JSON-able)
        ignoredActions: ['user/login'], // 🚫 Bỏ qua check cho action này
      },
    }),
  devTools: process.env.NODE_ENV !== 'production', // 🔧 Enable DevTools trong dev mode
});

export type RootState = ReturnType<typeof store.getState>; // 📊 Type cho toàn bộ state
export type AppDispatch = typeof store.dispatch; // 🎯 Type cho dispatch function

// ✅ Typed hooks - Custom hooks với TypeScript types
export const useAppDispatch: () => AppDispatch = useDispatch;
export const useAppSelector: TypedUseSelectorHook<RootState> = useSelector;

// ===================================================
// 📡 **ASYNC THUNKS** (API calls)
// ===================================================

import { createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUserById = createAsyncThunk(
  'user/fetchById', // 🏷️ Tên action
  async (userId: string, { rejectWithValue }) => { // 📡 Async function
    try {
      const response = await fetch(`/api/users/${userId}`);
      return await response.json(); // ✅ Return data khi thành công
    } catch (error) {
      return rejectWithValue('Failed to fetch user'); // ❌ Return error khi thất bại
    }
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    data: null,
    loading: false,
    error: null,
  },
  reducers: {},
  extraReducers: (builder) => { // 🔧 Handle async actions
    builder
      .addCase(fetchUserById.pending, (state) => {
        state.loading = true; // ⏳ Bắt đầu loading
      })
      .addCase(fetchUserById.fulfilled, (state, action) => {
        state.loading = false; // ✅ Kết thúc loading
        state.data = action.payload; // 📦 Lưu data
      })
      .addCase(fetchUserById.rejected, (state, action) => {
        state.loading = false; // ❌ Kết thúc loading
        state.error = action.payload as string; // 💥 Lưu error
      });
  },
});

// ===================================================
// 🎯 **USAGE IN COMPONENT** - Sử dụng trong component
// ===================================================

function Counter() {
  const count = useAppSelector((state) => state.counter.value); // 📊 Lấy state
  const dispatch = useAppDispatch(); // 🎯 Lấy dispatch function
  
  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => dispatch(increment())}>+</button> {/* 🔼 Tăng */}
      <button onClick={() => dispatch(decrement())}>-</button> {/* 🔽 Giảm */}
      <button onClick={() => dispatch(incrementByAmount(5))}>+5</button> {/* ➕ Tăng 5 */}
    </div>
  );
}
```

---

## 3. Zustand

### **3.1. Zustand Store**

```typescript
// ===================================================
// 🐻 **ZUSTAND** (Minimal & Fast)
// ===================================================

import { create } from 'zustand';
import { devtools, persist } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

// ✅ Define store - Tạo Zustand store
interface CounterStore {
  count: number; // 📊 State
  increment: () => void; // 🔧 Actions
  decrement: () => void;
  incrementByAmount: (amount: number) => void;
  reset: () => void;
}

export const useCounterStore = create<CounterStore>()(
  devtools( // 🔧 Layer 1: DevTools (debug với Redux DevTools)
    immer((set) => ({ // 💧 Layer 2: Immer (immutable updates tự động)
      count: 0, // 📊 Initial state
      
      increment: () =>
        set((state) => {
          state.count += 1; // ✅ Direct mutation (Immer handle)
        }),
      
      decrement: () =>
        set((state) => {
          state.count -= 1; // 🔽 Giảm
        }),
      
      incrementByAmount: (amount) =>
        set((state) => {
          state.count += amount; // ➕ Tăng theo amount
        }),
      
      reset: () =>
        set((state) => {
          state.count = 0; // 🔄 Reset về 0
        }),
    }))
  )
);

// ===================================================
// 💾 **PERSISTENT STORE** (LocalStorage)
// ===================================================

interface AuthStore {
  user: User | null;
  token: string | null;
  login: (user: User, token: string) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthStore>()(
  persist(
    (set) => ({
      user: null,
      token: null,
      
      login: (user, token) =>
        set({ user, token }),
      
      logout: () =>
        set({ user: null, token: null }),
    }),
    {
      name: 'auth-storage', // localStorage key
      partialize: (state) => ({ token: state.token }), // Only persist token
    }
  )
);

// ===================================================
// 📡 **ASYNC ACTIONS**
// ===================================================

interface UserStore {
  users: User[];
  loading: boolean;
  error: string | null;
  fetchUsers: () => Promise<void>;
}

export const useUserStore = create<UserStore>()((set, get) => ({
  users: [],
  loading: false,
  error: null,
  
  fetchUsers: async () => {
    set({ loading: true, error: null }); // ⏳ Bắt đầu loading
    
    try {
      const response = await fetch('/api/users'); // 📡 Gọi API
      const users = await response.json(); // 📦 Parse JSON
      set({ users, loading: false }); // ✅ Lưu data, tắt loading
    } catch (error) {
      set({ error: 'Failed to fetch users', loading: false }); // ❌ Lưu error
    }
  },
}));

// ===================================================
// 🎯 **USAGE IN COMPONENT** - Sử dụng trong component
// ===================================================

function Counter() {
  // ✅ Subscribe to specific state (auto-rerenders) - Chỉ subscribe field cụ thể
  const count = useCounterStore((state) => state.count); // 📊 Chỉ re-render khi count thay đổi
  const increment = useCounterStore((state) => state.increment); // 🔧 Lấy action
  
  // ⚠️ Or destructure (less optimal - subscribes to all) - Kém tối ưu hơn
  // const { count, increment } = useCounterStore(); // 💥 Re-render khi BẤT KỲ field nào đổi
  
  return (
    <div>
      <h1>{count}</h1>
      <button onClick={increment}>+</button>
    </div>
  );
}

// ===================================================
// 🔄 **COMPUTED VALUES** (Selectors) - Giá trị tính toán
// ===================================================

const useCartStore = create<CartStore>((set, get) => ({
  items: [], // 🛒 Danh sách items
  
  total: () => { // 💰 Tính tổng tiền
    return get().items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  },
  
  addItem: (item) =>
    set((state) => ({
      items: [...state.items, item], // ➕ Thêm item mới
    })),
}));

function CartTotal() {
  const total = useCartStore((state) => state.total()); // 💰 Lấy total
  return <div>Total: ${total}</div>;
}
```

---

## 4. Jotai

### **4.1. Jotai Atoms**

```typescript
// ===================================================
// ⚛️ **JOTAI** (Atomic State Management) - Quản lý state nguyên tử
// ===================================================

import { atom, useAtom, useAtomValue, useSetAtom } from 'jotai';
import { atomWithStorage } from 'jotai/utils';

// ✅ Primitive atom - Atom đơn giản
export const countAtom = atom(0); // 📊 State = 0

// ✅ Derived atom (computed) - Atom tính toán từ atom khác
export const doubleCountAtom = atom((get) => get(countAtom) * 2); // 🔢 = count * 2

// ✅ Write-only atom (action) - Atom chỉ ghi (không đọc)
export const incrementAtom = atom(
  null, // ⛔ no read - không cho phép đọc
  (get, set) => {
    set(countAtom, get(countAtom) + 1); // 🔼 Tăng countAtom lên 1
  }
);

// ✅ Read-write atom - Atom vừa đọc vừa ghi
export const counterAtom = atom(
  (get) => get(countAtom), // 📖 read - đọc giá trị
  (get, set, amount: number) => {
    set(countAtom, get(countAtom) + amount); // ✍️ write - ghi giá trị mới
  }
);

// ===================================================
// 💾 **PERSISTENT ATOM** (LocalStorage) - Lưu vào localStorage
// ===================================================

export const themeAtom = atomWithStorage<'light' | 'dark'>(
  'theme', // 🔑 LocalStorage key
  'light' // 🌟 Default value
);

// ===================================================
// 📡 **ASYNC ATOM**
// ===================================================

export const userIdAtom = atom<string | null>(null);

export const userAtom = atom(async (get) => {
  const userId = get(userIdAtom);
  if (!userId) return null;
  
  const response = await fetch(`/api/users/${userId}`);
  return response.json();
});

// ===================================================
// 🎯 **USAGE IN COMPONENT**
// ===================================================

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  const doubleCount = useAtomValue(doubleCountAtom);
  const increment = useSetAtom(incrementAtom);
  
  return (
    <div>
      <h1>Count: {count}</h1>
      <h2>Double: {doubleCount}</h2>
      <button onClick={() => setCount((c) => c + 1)}>+</button>
      <button onClick={increment}>Increment Action</button>
    </div>
  );
}

// ===================================================
// 🔄 **ATOM FAMILY** (Dynamic atoms)
// ===================================================

import { atomFamily } from 'jotai/utils';

const todoAtomFamily = atomFamily((id: string) =>
  atom({
    id,
    title: '',
    completed: false,
  })
);

function TodoItem({ id }: { id: string }) {
  const [todo, setTodo] = useAtom(todoAtomFamily(id));
  
  return (
    <div>
      <input
        value={todo.title}
        onChange={(e) => setTodo({ ...todo, title: e.target.value })}
      />
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={(e) => setTodo({ ...todo, completed: e.target.checked })}
      />
    </div>
  );
}
```

---

## 5. Comparison Table

```typescript
// ===================================================
// 📊 **COMPREHENSIVE COMPARISON**
// ===================================================

const STATE_MANAGER_COMPARISON = {
  // ===== Redux Toolkit =====
  reduxToolkit: {
    bundleSize: '~12 KB (with React-Redux)',
    boilerplate: 'Medium (slices are simpler than old Redux)',
    learningCurve: 'Steep (concepts: actions, reducers, middleware)',
    devTools: '✅ Excellent (time-travel debugging)',
    typescript: '✅ Great (built-in types)',
    performance: '✅ Good (selector memoization with Reselect)',
    ecosystem: '✅ Huge (middleware, DevTools, tutorials)',
    
    bestFor: [
      'Large apps with complex state logic',
      'Need time-travel debugging',
      'Team familiar with Redux',
      'Strict unidirectional data flow required',
    ],
    
    codeExample: `
      // Verbose but predictable
      const slice = createSlice({
        name: 'counter',
        initialState: { value: 0 },
        reducers: {
          increment: (state) => { state.value += 1 },
        },
      });
    `,
  },
  
  // ===== Zustand =====
  zustand: {
    bundleSize: '~1 KB (tiny!)',
    boilerplate: 'Minimal (one store definition)',
    learningCurve: 'Gentle (simple hooks)',
    devTools: '✅ Good (via middleware)',
    typescript: '✅ Excellent (full inference)',
    performance: '✅ Excellent (selective subscriptions)',
    ecosystem: 'Growing (middleware for persist, immer, devtools)',
    
    bestFor: [
      'Small to medium apps',
      'Need minimal boilerplate',
      'Bundle size is critical',
      'Want simple API',
    ],
    
    codeExample: `
      // Concise and intuitive
      const useStore = create((set) => ({
        count: 0,
        increment: () => set((s) => ({ count: s.count + 1 })),
      }));
    `,
  },
  
  // ===== Jotai =====
  jotai: {
    bundleSize: '~3 KB',
    boilerplate: 'Minimal (atom definitions)',
    learningCurve: 'Medium (atomic model is different)',
    devTools: '✅ Good (via plugin)',
    typescript: '✅ Excellent (type inference)',
    performance: '✅ Excellent (atomic updates)',
    ecosystem: 'Growing (utilities for async, storage, etc)',
    
    bestFor: [
      'Need granular reactivity',
      'Derived state is common',
      'React Suspense integration',
      'Bottom-up state composition',
    ],
    
    codeExample: `
      // Atomic and composable
      const countAtom = atom(0);
      const doubleAtom = atom((get) => get(countAtom) * 2);
    `,
  },
};

// ===================================================
// 🎯 **PERFORMANCE COMPARISON**
// ===================================================

const PERFORMANCE_METRICS = {
  rerenderOptimization: {
    redux: 'Manual (useSelector + memoization)',
    zustand: 'Automatic (subscribe to slices)',
    jotai: 'Automatic (atomic subscriptions)',
  },
  
  bundleSize: {
    redux: '12 KB',
    zustand: '1 KB ⭐',
    jotai: '3 KB',
  },
  
  reactSuspense: {
    redux: '❌ Not built-in',
    zustand: '⚠️ Manual implementation',
    jotai: '✅ Native support ⭐',
  },
  
  devTools: {
    redux: '✅ Best-in-class ⭐',
    zustand: '✅ Good (middleware)',
    jotai: '✅ Good (plugin)',
  },
};
```

---

## 6. Migration Strategies

### **6.1. Redux → Zustand Migration**

```typescript
// ===================================================
// 🔄 **MIGRATION: REDUX → ZUSTAND**
// ===================================================

// ❌ Redux Toolkit (BEFORE)
const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => { state.value += 1 },
    decrement: (state) => { state.value -= 1 },
  },
});

// ✅ Zustand (AFTER)
const useCounterStore = create<CounterStore>((set) => ({
  value: 0,
  increment: () => set((state) => ({ value: state.value + 1 })),
  decrement: () => set((state) => ({ value: state.value - 1 })),
}));

// Component changes:
// BEFORE: const count = useSelector((state) => state.counter.value);
// AFTER:  const count = useCounterStore((state) => state.value);
```

---

## 7. Advanced Patterns

### **7.1. Undo/Redo Pattern**

```typescript
// ===================================================
// ↩️ **UNDO/REDO** (Zustand)
// ===================================================

interface HistoryStore<T> {
  past: T[];
  present: T;
  future: T[];
  set: (newPresent: T) => void;
  undo: () => void;
  redo: () => void;
  canUndo: boolean;
  canRedo: boolean;
}

function createHistoryStore<T>(initialState: T) {
  return create<HistoryStore<T>>((set, get) => ({
    past: [],
    present: initialState,
    future: [],
    
    set: (newPresent) => {
      const { present, past } = get();
      set({
        past: [...past, present],
        present: newPresent,
        future: [],
      });
    },
    
    undo: () => {
      const { past, present, future } = get();
      if (past.length === 0) return;
      
      const previous = past[past.length - 1];
      set({
        past: past.slice(0, -1),
        present: previous,
        future: [present, ...future],
      });
    },
    
    redo: () => {
      const { past, present, future } = get();
      if (future.length === 0) return;
      
      const next = future[0];
      set({
        past: [...past, present],
        present: next,
        future: future.slice(1),
      });
    },
    
    canUndo: get().past.length > 0,
    canRedo: get().future.length > 0,
  }));
}

// Usage
const useCanvasStore = createHistoryStore<CanvasState>({ shapes: [] });

function Canvas() {
  const { present, undo, redo, canUndo, canRedo } = useCanvasStore();
  
  return (
    <div>
      <button onClick={undo} disabled={!canUndo}>Undo</button>
      <button onClick={redo} disabled={!canRedo}>Redo</button>
    </div>
  );
}
```

---

## 8. Redux Deep Dive - Advanced Patterns

### **8.1. Redux Middleware Architecture**

```typescript
// ===================================================
// 🔌 **CUSTOM MIDDLEWARE** - Logging & Analytics
// ===================================================

import { Middleware } from '@reduxjs/toolkit';

// ✅ Logger Middleware
const loggerMiddleware: Middleware = (store) => (next) => (action) => {
  console.group(action.type);
  console.log('⏰ Dispatching:', action);
  console.log('📊 Previous State:', store.getState());
  
  const result = next(action);
  
  console.log('📈 Next State:', store.getState());
  console.groupEnd();
  
  return result;
};

// ===================================================
// 📡 **API MIDDLEWARE** - Centralized API calls
// ===================================================

interface ApiAction {
  type: string;
  endpoint: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  body?: any;
  onSuccess?: string;
  onError?: string;
}

const apiMiddleware: Middleware = (store) => (next) => async (action: any) => {
  // Only process API actions
  if (!action.endpoint) {
    return next(action);
  }

  const { endpoint, method, body, onSuccess, onError } = action as ApiAction;

  try {
    const response = await fetch(endpoint, {
      method,
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${store.getState().auth.token}`,
      },
      body: body ? JSON.stringify(body) : undefined,
    });

    const data = await response.json();

    if (!response.ok) throw new Error(data.message);

    // Dispatch success action
    if (onSuccess) {
      store.dispatch({ type: onSuccess, payload: data });
    }

    return data;
  } catch (error) {
    // Dispatch error action
    if (onError) {
      store.dispatch({ type: onError, payload: error.message });
    }

    throw error;
  }
};

// Usage
dispatch({
  type: 'API_REQUEST',
  endpoint: '/api/users',
  method: 'GET',
  onSuccess: 'users/fetchSuccess',
  onError: 'users/fetchError',
});

// ===================================================
// ⏱️ **DEBOUNCE MIDDLEWARE** - Throttle actions
// ===================================================

const debounceMiddleware: Middleware = (store) => {
  const timers: Record<string, NodeJS.Timeout> = {};

  return (next) => (action: any) => {
    const { meta } = action;

    if (!meta?.debounce) {
      return next(action);
    }

    const { delay = 300, key = action.type } = meta.debounce;

    // Clear existing timer
    if (timers[key]) {
      clearTimeout(timers[key]);
    }

    // Set new timer
    return new Promise((resolve) => {
      timers[key] = setTimeout(() => {
        resolve(next(action));
        delete timers[key];
      }, delay);
    });
  };
};

// Usage
dispatch({
  type: 'search/setQuery',
  payload: 'react',
  meta: { debounce: { delay: 500, key: 'search' } },
});

// ===================================================
// 🔄 **RETRY MIDDLEWARE** - Auto retry failed actions
// ===================================================

const retryMiddleware: Middleware = (store) => (next) => async (action: any) => {
  const { meta } = action;

  if (!meta?.retry) {
    return next(action);
  }

  const { maxAttempts = 3, delay = 1000 } = meta.retry;

  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await next(action);
    } catch (error) {
      if (attempt === maxAttempts) {
        throw error;
      }

      // Wait before retry (exponential backoff)
      await new Promise((resolve) =>
        setTimeout(resolve, delay * Math.pow(2, attempt - 1))
      );

      console.log(`🔄 Retry attempt ${attempt}/${maxAttempts}`);
    }
  }
};

// ===================================================
// 📊 **ANALYTICS MIDDLEWARE** - Track user actions
// ===================================================

const analyticsMiddleware: Middleware = (store) => (next) => (action) => {
  const result = next(action);

  // Track specific actions
  const trackedActions = ['user/login', 'cart/addItem', 'order/submit'];

  if (trackedActions.includes(action.type)) {
    // Send to analytics service
    analytics.track(action.type, {
      userId: store.getState().user?.id,
      timestamp: Date.now(),
      payload: action.payload,
    });
  }

  return result;
};

// ===================================================
// 🔧 **CONFIGURE STORE với Custom Middleware**
// ===================================================

export const store = configureStore({
  reducer: rootReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        // Ignore these action types
        ignoredActions: ['persist/PERSIST'],
        // Ignore these field paths in all actions
        ignoredActionPaths: ['meta.arg', 'payload.timestamp'],
        // Ignore these paths in the state
        ignoredPaths: ['items.dates'],
      },
      thunk: {
        extraArgument: { api, analytics }, // ✅ Inject dependencies
      },
    })
      .prepend(loggerMiddleware)
      .concat(apiMiddleware, debounceMiddleware, retryMiddleware, analyticsMiddleware),
});
```

---

### **8.2. Advanced Selectors with Reselect**

```typescript
// ===================================================
// 🎯 **MEMOIZED SELECTORS** - Optimize re-renders
// ===================================================

import { createSelector, createEntityAdapter } from '@reduxjs/toolkit';

// ✅ Entity Adapter (normalized state)
const usersAdapter = createEntityAdapter<User>({
  selectId: (user) => user.id,
  sortComparer: (a, b) => a.name.localeCompare(b.name),
});

const usersSlice = createSlice({
  name: 'users',
  initialState: usersAdapter.getInitialState({
    loading: false,
    error: null,
  }),
  reducers: {
    addUser: usersAdapter.addOne,
    updateUser: usersAdapter.updateOne,
    removeUser: usersAdapter.removeOne,
    setUsers: usersAdapter.setAll,
  },
});

// ✅ Basic selectors từ adapter
export const {
  selectAll: selectAllUsers,
  selectById: selectUserById,
  selectIds: selectUserIds,
  selectEntities: selectUserEntities,
  selectTotal: selectTotalUsers,
} = usersAdapter.getSelectors((state: RootState) => state.users);

// ===================================================
// 🔍 **COMPLEX MEMOIZED SELECTORS**
// ===================================================

// Selector 1: Get active users
export const selectActiveUsers = createSelector(
  [selectAllUsers],
  (users) => users.filter((user) => user.status === 'active')
);

// Selector 2: Get users by role
export const selectUsersByRole = createSelector(
  [selectAllUsers, (_state: RootState, role: string) => role],
  (users, role) => users.filter((user) => user.role === role)
);

// Selector 3: Get user statistics (expensive computation)
export const selectUserStats = createSelector(
  [selectAllUsers],
  (users) => {
    console.log('⚡ Computing user stats...'); // Only logs when users change

    return {
      total: users.length,
      active: users.filter((u) => u.status === 'active').length,
      inactive: users.filter((u) => u.status === 'inactive').length,
      byRole: users.reduce((acc, user) => {
        acc[user.role] = (acc[user.role] || 0) + 1;
        return acc;
      }, {} as Record<string, number>),
    };
  }
);

// ===================================================
// 🔗 **CHAINED SELECTORS** - Compose selectors
// ===================================================

// Base selectors
const selectCartItems = (state: RootState) => state.cart.items;
const selectProducts = (state: RootState) => state.products.entities;

// Derived selector: Get cart items with product details
export const selectCartWithProducts = createSelector(
  [selectCartItems, selectProducts],
  (cartItems, products) => {
    return cartItems.map((item) => ({
      ...item,
      product: products[item.productId],
    }));
  }
);

// Derived selector: Calculate cart total
export const selectCartTotal = createSelector(
  [selectCartWithProducts],
  (items) => {
    return items.reduce(
      (total, item) => total + item.product.price * item.quantity,
      0
    );
  }
);

// Derived selector: Calculate tax
export const selectCartTax = createSelector(
  [selectCartTotal, (state: RootState) => state.settings.taxRate],
  (total, taxRate) => total * taxRate
);

// Derived selector: Calculate grand total
export const selectCartGrandTotal = createSelector(
  [selectCartTotal, selectCartTax],
  (subtotal, tax) => subtotal + tax
);

// ===================================================
// 📊 **PARAMETERIZED SELECTORS** - Factory pattern
// ===================================================

// ✅ Create selector factory
const makeSelectUserPosts = () =>
  createSelector(
    [
      (state: RootState) => state.posts.entities,
      (_state: RootState, userId: string) => userId,
    ],
    (posts, userId) => {
      return Object.values(posts).filter((post) => post?.userId === userId);
    }
  );

// Usage in component
function UserPosts({ userId }: { userId: string }) {
  // ✅ Create selector instance per component
  const selectUserPosts = useMemo(makeSelectUserPosts, []);
  const posts = useAppSelector((state) => selectUserPosts(state, userId));

  return <PostList posts={posts} />;
}

// ===================================================
// 🎯 **STRUCTURED SELECTORS** - Combine multiple selectors
// ===================================================

import { createStructuredSelector } from 'reselect';

const selectDashboardData = createStructuredSelector({
  users: selectAllUsers,
  stats: selectUserStats,
  cart: selectCartWithProducts,
  total: selectCartTotal,
});

// Usage
function Dashboard() {
  const data = useAppSelector(selectDashboardData);
  // data = { users, stats, cart, total }

  return (
    <div>
      <UserList users={data.users} />
      <Stats stats={data.stats} />
      <Cart items={data.cart} total={data.total} />
    </div>
  );
}
```

---

### **8.3. Redux Persist & Hydration**

```typescript
// ===================================================
// 💾 **REDUX PERSIST** - Save state to storage
// ===================================================

import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage'; // localStorage
import { PersistGate } from 'redux-persist/integration/react';

// ✅ Persist config
const persistConfig = {
  key: 'root',
  storage,
  whitelist: ['auth', 'settings'], // Only persist these reducers
  blacklist: ['ui', 'temp'], // Don't persist these
  version: 1,
  migrate: async (state: any) => {
    // Migration logic for version updates
    if (state?._persist?.version < 1) {
      // Migrate from old schema to new
      return {
        ...state,
        settings: {
          ...state.settings,
          newField: 'default',
        },
      };
    }
    return state;
  },
};

// ✅ Create persisted reducer
const persistedReducer = persistReducer(persistConfig, rootReducer);

export const store = configureStore({
  reducer: persistedReducer,
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST', 'persist/REHYDRATE'],
      },
    }),
});

export const persistor = persistStore(store);

// ===================================================
// 🎯 **APP SETUP với Persist**
// ===================================================

import { Provider } from 'react-redux';

function App() {
  return (
    <Provider store={store}>
      <PersistGate loading={<Spinner />} persistor={persistor}>
        <Router />
      </PersistGate>
    </Provider>
  );
}

// ===================================================
// 🔄 **SELECTIVE PERSIST** - Per-slice config
// ===================================================

import { createTransform } from 'redux-persist';

// Transform to persist only specific fields
const userTransform = createTransform(
  // Transform state on its way to storage
  (inboundState: any) => ({
    token: inboundState.token,
    userId: inboundState.userId,
    // Don't persist sensitive data
  }),
  // Transform state on its way back from storage
  (outboundState: any) => ({
    ...outboundState,
    profile: null, // Will be refetched
  }),
  { whitelist: ['auth'] }
);

const persistConfig = {
  key: 'root',
  storage,
  transforms: [userTransform],
};

// ===================================================
// 🧹 **PURGE PERSISTED STATE** - Clear storage
// ===================================================

import { PURGE } from 'redux-persist';

function LogoutButton() {
  const dispatch = useAppDispatch();

  const handleLogout = () => {
    // Clear persisted state
    dispatch({ type: PURGE, result: () => null });

    // Or manually
    persistor.purge();
  };

  return <button onClick={handleLogout}>Logout</button>;
}
```

---

### **8.4. Redux Testing Strategies**

```typescript
// ===================================================
// 🧪 **TESTING REDUCERS**
// ===================================================

import { counterSlice, increment, decrement } from './counterSlice';

describe('counterSlice', () => {
  const initialState = { value: 0 };

  it('should return initial state', () => {
    expect(counterSlice.reducer(undefined, { type: 'unknown' })).toEqual(
      initialState
    );
  });

  it('should increment', () => {
    const actual = counterSlice.reducer(initialState, increment());
    expect(actual.value).toBe(1);
  });

  it('should decrement', () => {
    const actual = counterSlice.reducer({ value: 1 }, decrement());
    expect(actual.value).toBe(0);
  });
});

// ===================================================
// 🧪 **TESTING ASYNC THUNKS**
// ===================================================

import { fetchUserById } from './userSlice';
import { server } from '../mocks/server'; // MSW
import { rest } from 'msw';

describe('fetchUserById', () => {
  it('should fetch user successfully', async () => {
    const mockUser = { id: '1', name: 'John' };

    server.use(
      rest.get('/api/users/1', (req, res, ctx) => {
        return res(ctx.json(mockUser));
      })
    );

    const dispatch = jest.fn();
    const thunk = fetchUserById('1');

    await thunk(dispatch, () => ({}), undefined);

    const { calls } = dispatch.mock;
    expect(calls[0][0].type).toBe('user/fetchById/pending');
    expect(calls[1][0].type).toBe('user/fetchById/fulfilled');
    expect(calls[1][0].payload).toEqual(mockUser);
  });

  it('should handle error', async () => {
    server.use(
      rest.get('/api/users/1', (req, res, ctx) => {
        return res(ctx.status(500), ctx.json({ error: 'Server error' }));
      })
    );

    const dispatch = jest.fn();
    const thunk = fetchUserById('1');

    await thunk(dispatch, () => ({}), undefined);

    const { calls } = dispatch.mock;
    expect(calls[1][0].type).toBe('user/fetchById/rejected');
  });
});

// ===================================================
// 🧪 **TESTING SELECTORS**
// ===================================================

import { selectUserStats } from './userSelectors';

describe('selectUserStats', () => {
  it('should compute stats correctly', () => {
    const state = {
      users: {
        ids: ['1', '2', '3'],
        entities: {
          '1': { id: '1', status: 'active', role: 'admin' },
          '2': { id: '2', status: 'active', role: 'user' },
          '3': { id: '3', status: 'inactive', role: 'user' },
        },
      },
    };

    const stats = selectUserStats(state as any);

    expect(stats).toEqual({
      total: 3,
      active: 2,
      inactive: 1,
      byRole: { admin: 1, user: 2 },
    });
  });
});

// ===================================================
// 🧪 **INTEGRATION TESTS** - with React Testing Library
// ===================================================

import { renderWithProviders } from '../test-utils';
import { screen, fireEvent } from '@testing-library/react';

// Test utility
export function renderWithProviders(
  ui: React.ReactElement,
  {
    preloadedState = {},
    store = configureStore({ reducer: rootReducer, preloadedState }),
    ...renderOptions
  } = {}
) {
  function Wrapper({ children }: { children: React.ReactNode }) {
    return <Provider store={store}>{children}</Provider>;
  }

  return { store, ...render(ui, { wrapper: Wrapper, ...renderOptions }) };
}

describe('Counter Component', () => {
  it('should increment counter', () => {
    renderWithProviders(<Counter />);

    const incrementButton = screen.getByText('+');
    fireEvent.click(incrementButton);

    expect(screen.getByText('1')).toBeInTheDocument();
  });
});
```

---

## 9. Zustand Deep Dive - Advanced Patterns

### **9.1. Zustand Middleware Composition**

```typescript
// ===================================================
// 🐻 **ZUSTAND MIDDLEWARE** - Advanced patterns
// ===================================================

import { create } from 'zustand';
import { devtools, persist, subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

// ===================================================
// 📊 **FULL MIDDLEWARE STACK**
// ===================================================

interface TodoStore {
  todos: Todo[];
  filter: 'all' | 'active' | 'completed';
  addTodo: (text: string) => void;
  toggleTodo: (id: string) => void;
  removeTodo: (id: string) => void;
  setFilter: (filter: 'all' | 'active' | 'completed') => void;
}

export const useTodoStore = create<TodoStore>()(
  // ✅ Layer 1: DevTools (outermost)
  devtools(
    // ✅ Layer 2: Persist
    persist(
      // ✅ Layer 3: Subscribe with selector
      subscribeWithSelector(
        // ✅ Layer 4: Immer (innermost)
        immer((set) => ({
          todos: [],
          filter: 'all',

          addTodo: (text) =>
            set((state) => {
              state.todos.push({
                id: crypto.randomUUID(),
                text,
                completed: false,
              });
            }),

          toggleTodo: (id) =>
            set((state) => {
              const todo = state.todos.find((t) => t.id === id);
              if (todo) {
                todo.completed = !todo.completed;
              }
            }),

          removeTodo: (id) =>
            set((state) => {
              state.todos = state.todos.filter((t) => t.id !== id);
            }),

          setFilter: (filter) =>
            set({ filter }),
        }))
      ),
      {
        name: 'todo-storage',
        partialize: (state) => ({ todos: state.todos }), // Only persist todos
      }
    ),
    { name: 'TodoStore' }
  )
);

// ===================================================
// 🔔 **SUBSCRIBE TO SPECIFIC CHANGES**
// ===================================================

// Subscribe to filter changes only
useTodoStore.subscribe(
  (state) => state.filter,
  (filter, prevFilter) => {
    console.log('Filter changed:', prevFilter, '→', filter);
    analytics.track('filter_changed', { filter });
  }
);

// Subscribe to todos count
useTodoStore.subscribe(
  (state) => state.todos.length,
  (count, prevCount) => {
    console.log('Todo count:', prevCount, '→', count);
  }
);

// ===================================================
// 🎯 **CUSTOM MIDDLEWARE** - Logger
// ===================================================

const logger = (config) => (set, get, api) => {
  return config(
    (...args) => {
      console.log('📝 Before:', get());
      set(...args);
      console.log('📊 After:', get());
    },
    get,
    api
  );
};

const useStore = create(
  logger((set) => ({
    count: 0,
    increment: () => set((state) => ({ count: state.count + 1 })),
  }))
);

// ===================================================
// ⏱️ **TIME-TRAVEL MIDDLEWARE**
// ===================================================

const timeTravel = (config) => (set, get, api) => {
  const history = [];
  const maxHistory = 50;

  return config(
    (...args) => {
      // Save current state to history
      history.push(get());
      if (history.length > maxHistory) {
        history.shift();
      }

      set(...args);
    },
    get,
    {
      ...api,
      undo: () => {
        if (history.length > 0) {
          const prevState = history.pop();
          set(prevState, true); // Replace state
        }
      },
      getHistory: () => history,
    }
  );
};

// ===================================================
// 🔄 **RESET MIDDLEWARE** - Reset to initial state
// ===================================================

const resetters = new Set<() => void>();

const resetMiddleware = (config) => (set, get, api) => {
  const initialState = config(set, get, api);

  resetters.add(() => set(initialState));

  return {
    ...initialState,
    reset: () => set(initialState),
  };
};

export const resetAllStores = () => {
  resetters.forEach((reset) => reset());
};
```

---

### **9.2. Zustand Slices Pattern**

```typescript
// ===================================================
// 🍰 **SLICES PATTERN** - Modular store composition
// ===================================================

// ✅ Slice 1: Auth
interface AuthSlice {
  user: User | null;
  token: string | null;
  login: (user: User, token: string) => void;
  logout: () => void;
}

const createAuthSlice = (set): AuthSlice => ({
  user: null,
  token: null,
  login: (user, token) => set({ user, token }),
  logout: () => set({ user: null, token: null }),
});

// ✅ Slice 2: UI
interface UISlice {
  sidebarOpen: boolean;
  theme: 'light' | 'dark';
  toggleSidebar: () => void;
  setTheme: (theme: 'light' | 'dark') => void;
}

const createUISlice = (set): UISlice => ({
  sidebarOpen: true,
  theme: 'light',
  toggleSidebar: () =>
    set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setTheme: (theme) => set({ theme }),
});

// ✅ Slice 3: Notifications
interface NotificationSlice {
  notifications: Notification[];
  addNotification: (notification: Notification) => void;
  removeNotification: (id: string) => void;
}

const createNotificationSlice = (set, get): NotificationSlice => ({
  notifications: [],
  addNotification: (notification) =>
    set((state) => ({
      notifications: [...state.notifications, notification],
    })),
  removeNotification: (id) =>
    set((state) => ({
      notifications: state.notifications.filter((n) => n.id !== id),
    })),
});

// ===================================================
// 🔗 **COMBINE SLICES**
// ===================================================

type Store = AuthSlice & UISlice & NotificationSlice;

export const useAppStore = create<Store>()(
  devtools(
    persist(
      immer((set, get, api) => ({
        ...createAuthSlice(set),
        ...createUISlice(set),
        ...createNotificationSlice(set, get),
      })),
      {
        name: 'app-storage',
        partialize: (state) => ({
          theme: state.theme,
          sidebarOpen: state.sidebarOpen,
        }),
      }
    )
  )
);

// ===================================================
// 🎯 **SLICE-SPECIFIC HOOKS** - Optimize re-renders
// ===================================================

// Only subscribe to auth slice
export const useAuth = () =>
  useAppStore((state) => ({
    user: state.user,
    token: state.token,
    login: state.login,
    logout: state.logout,
  }));

// Only subscribe to UI slice
export const useUI = () =>
  useAppStore((state) => ({
    sidebarOpen: state.sidebarOpen,
    theme: state.theme,
    toggleSidebar: state.toggleSidebar,
    setTheme: state.setTheme,
  }));

// Usage
function Sidebar() {
  const { sidebarOpen, toggleSidebar } = useUI();
  // ✅ Only re-renders when sidebarOpen or theme changes

  return <aside className={sidebarOpen ? 'open' : 'closed'} />;
}
```

---

### **9.3. Zustand Async Actions & Error Handling**

```typescript
// ===================================================
// 📡 **ASYNC ACTIONS** - Best practices
// ===================================================

interface UserStore {
  users: User[];
  loading: boolean;
  error: string | null;
  
  fetchUsers: () => Promise<void>;
  createUser: (user: CreateUserDTO) => Promise<User>;
  updateUser: (id: string, updates: Partial<User>) => Promise<void>;
  deleteUser: (id: string) => Promise<void>;
}

export const useUserStore = create<UserStore>()((set, get) => ({
  users: [],
  loading: false,
  error: null,

  // ===================================================
  // ✅ FETCH with loading & error states
  // ===================================================
  fetchUsers: async () => {
    set({ loading: true, error: null });

    try {
      const response = await fetch('/api/users');
      if (!response.ok) throw new Error('Failed to fetch users');

      const users = await response.json();
      set({ users, loading: false });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Unknown error',
        loading: false,
      });
    }
  },

  // ===================================================
  // ✅ CREATE with optimistic update
  // ===================================================
  createUser: async (userData) => {
    const tempUser: User = {
      id: `temp-${Date.now()}`,
      ...userData,
      createdAt: new Date().toISOString(),
    };

    // Optimistic update
    set((state) => ({
      users: [...state.users, tempUser],
    }));

    try {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(userData),
      });

      if (!response.ok) throw new Error('Failed to create user');

      const newUser = await response.json();

      // Replace temp user with real user
      set((state) => ({
        users: state.users.map((u) => (u.id === tempUser.id ? newUser : u)),
      }));

      return newUser;
    } catch (error) {
      // Rollback on error
      set((state) => ({
        users: state.users.filter((u) => u.id !== tempUser.id),
        error: error instanceof Error ? error.message : 'Unknown error',
      }));

      throw error;
    }
  },

  // ===================================================
  // ✅ UPDATE with optimistic update
  // ===================================================
  updateUser: async (id, updates) => {
    // Save previous state for rollback
    const previousUsers = get().users;

    // Optimistic update
    set((state) => ({
      users: state.users.map((u) =>
        u.id === id ? { ...u, ...updates } : u
      ),
    }));

    try {
      const response = await fetch(`/api/users/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates),
      });

      if (!response.ok) throw new Error('Failed to update user');

      const updatedUser = await response.json();

      set((state) => ({
        users: state.users.map((u) => (u.id === id ? updatedUser : u)),
      }));
    } catch (error) {
      // Rollback on error
      set({ users: previousUsers, error: error.message });
      throw error;
    }
  },

  // ===================================================
  // ✅ DELETE with optimistic update
  // ===================================================
  deleteUser: async (id) => {
    const previousUsers = get().users;

    // Optimistic delete
    set((state) => ({
      users: state.users.filter((u) => u.id !== id),
    }));

    try {
      const response = await fetch(`/api/users/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) throw new Error('Failed to delete user');
    } catch (error) {
      // Rollback on error
      set({ users: previousUsers, error: error.message });
      throw error;
    }
  },
}));

// ===================================================
// 🎯 **USAGE IN COMPONENT**
// ===================================================

function UserList() {
  const { users, loading, error, fetchUsers, deleteUser } = useUserStore();

  useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  const handleDelete = async (id: string) => {
    try {
      await deleteUser(id);
      toast.success('User deleted');
    } catch (error) {
      toast.error('Failed to delete user');
    }
  };

  if (loading) return <Spinner />;
  if (error) return <Error message={error} />;

  return (
    <div>
      {users.map((user) => (
        <UserCard key={user.id} user={user} onDelete={() => handleDelete(user.id)} />
      ))}
    </div>
  );
}
```

---

### **9.4. Zustand Performance Optimization**

```typescript
// ===================================================
// ⚡ **PERFORMANCE OPTIMIZATION**
// ===================================================

// ❌ BAD: Re-renders on any state change
function BadComponent() {
  const store = useAppStore(); // Subscribe to entire store
  return <div>{store.count}</div>;
}

// ✅ GOOD: Only re-renders when count changes
function GoodComponent() {
  const count = useAppStore((state) => state.count);
  return <div>{count}</div>;
}

// ===================================================
// 🎯 **SHALLOW COMPARISON** - For objects
// ===================================================

import { shallow } from 'zustand/shallow';

// ❌ BAD: New object reference every render
function BadMultiSelect() {
  const { count, user } = useAppStore((state) => ({
    count: state.count,
    user: state.user,
  }));
  // Re-renders on ANY state change!
}

// ✅ GOOD: Shallow comparison
function GoodMultiSelect() {
  const { count, user } = useAppStore(
    (state) => ({
      count: state.count,
      user: state.user,
    }),
    shallow // Only re-render if count or user changes
  );
}

// ===================================================
// 📊 **COMPUTED VALUES** - Memoization
// ===================================================

interface CartStore {
  items: CartItem[];
  taxRate: number;
  
  // ✅ Computed getter (runs on every access)
  getTotal: () => number;
  getTax: () => number;
  getGrandTotal: () => number;
}

export const useCartStore = create<CartStore>()((set, get) => ({
  items: [],
  taxRate: 0.1,

  getTotal: () => {
    return get().items.reduce((sum, item) => sum + item.price * item.quantity, 0);
  },

  getTax: () => {
    return get().getTotal() * get().taxRate;
  },

  getGrandTotal: () => {
    return get().getTotal() + get().getTax();
  },
}));

// Usage with useMemo to prevent recalculation
function CartSummary() {
  const getTotal = useCartStore((state) => state.getTotal);
  const total = useMemo(() => getTotal(), [getTotal]);

  return <div>Total: ${total}</div>;
}

// ===================================================
// 🔍 **CUSTOM EQUALITY FUNCTION**
// ===================================================

function UserProfile() {
  const user = useAppStore(
    (state) => state.user,
    (a, b) => a?.id === b?.id // Only re-render if user ID changes
  );

  return <div>{user?.name}</div>;
}
```

---

### **9.5. Zustand Testing**

```typescript
// ===================================================
// 🧪 **TESTING ZUSTAND STORES**
// ===================================================

import { act, renderHook } from '@testing-library/react';
import { useCounterStore } from './counterStore';

describe('useCounterStore', () => {
  beforeEach(() => {
    // Reset store before each test
    useCounterStore.setState({ count: 0 });
  });

  it('should increment count', () => {
    const { result } = renderHook(() => useCounterStore());

    act(() => {
      result.current.increment();
    });

    expect(result.current.count).toBe(1);
  });

  it('should decrement count', () => {
    const { result } = renderHook(() => useCounterStore());

    act(() => {
      useCounterStore.setState({ count: 5 });
      result.current.decrement();
    });

    expect(result.current.count).toBe(4);
  });

  it('should reset count', () => {
    const { result } = renderHook(() => useCounterStore());

    act(() => {
      useCounterStore.setState({ count: 10 });
      result.current.reset();
    });

    expect(result.current.count).toBe(0);
  });
});

// ===================================================
// 🧪 **TESTING ASYNC ACTIONS**
// ===================================================

describe('useUserStore async actions', () => {
  beforeEach(() => {
    useUserStore.setState({ users: [], loading: false, error: null });
  });

  it('should fetch users', async () => {
    const mockUsers = [
      { id: '1', name: 'User 1' },
      { id: '2', name: 'User 2' },
    ];

    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: true,
        json: () => Promise.resolve(mockUsers),
      })
    ) as jest.Mock;

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.fetchUsers();
    });

    expect(result.current.users).toEqual(mockUsers);
    expect(result.current.loading).toBe(false);
    expect(result.current.error).toBeNull();
  });

  it('should handle fetch error', async () => {
    global.fetch = jest.fn(() =>
      Promise.resolve({
        ok: false,
      })
    ) as jest.Mock;

    const { result } = renderHook(() => useUserStore());

    await act(async () => {
      await result.current.fetchUsers();
    });

    expect(result.current.users).toEqual([]);
    expect(result.current.error).toBe('Failed to fetch users');
  });
});

// ===================================================
// 🧪 **MOCK STORE FOR COMPONENT TESTS**
// ===================================================

// Create mock store
const createMockStore = (initialState = {}) => {
  return create(() => ({
    count: 0,
    increment: jest.fn(),
    ...initialState,
  }));
};

// Test component
describe('Counter component', () => {
  it('should render count', () => {
    const mockStore = createMockStore({ count: 5 });

    render(<Counter />);

    expect(screen.getByText('5')).toBeInTheDocument();
  });
});
```

---

## **🎯 Redux vs Zustand - When to Use What**

```typescript
// ===================================================
// 📊 **DECISION MATRIX**
// ===================================================

const WHEN_TO_USE_REDUX = [
  '✅ Large enterprise applications',
  '✅ Need Redux DevTools time-travel debugging',
  '✅ Complex state logic with multiple reducers',
  '✅ Team already familiar with Redux',
  '✅ Need middleware ecosystem (sagas, observables)',
  '✅ Strict unidirectional data flow required',
  '✅ Need to replay user sessions for debugging',
];

const WHEN_TO_USE_ZUSTAND = [
  '✅ Small to medium applications',
  '✅ Bundle size is critical (<1KB vs 12KB)',
  '✅ Want minimal boilerplate',
  '✅ Need simple API that team can learn quickly',
  '✅ Performance is priority (selective subscriptions)',
  '✅ Don\'t need complex middleware',
  '✅ Want flexibility without constraints',
];

// ===================================================
// 🏆 **PERFORMANCE COMPARISON**
// ===================================================

const PERFORMANCE_COMPARISON = {
  bundleSize: {
    redux: '~12 KB (Redux Toolkit + React-Redux)',
    zustand: '~1 KB ⭐ (12x smaller!)',
  },
  
  boilerplate: {
    redux: 'Medium (slices, actions, reducers)',
    zustand: 'Minimal ⭐ (just create store)',
  },
  
  rerenderOptimization: {
    redux: 'Manual (useSelector + memoization)',
    zustand: 'Automatic ⭐ (subscribe to slices)',
  },
  
  devTools: {
    redux: '✅ Best-in-class ⭐',
    zustand: '✅ Good (via middleware)',
  },
  
  learningCurve: {
    redux: 'Steep (many concepts)',
    zustand: 'Gentle ⭐ (simple hooks)',
  },
  
  middleware: {
    redux: '✅ Rich ecosystem ⭐',
    zustand: '✅ Good (persist, immer, devtools)',
  },
};
```

---

**🎯 Key Takeaways:**

### **Redux Deep Dive:**
1. **Middleware** enables centralized side effects (API, logging, analytics)
2. **Reselect** optimizes expensive computations with memoization
3. **Entity Adapter** normalizes state for O(1) lookups
4. **Redux Persist** saves state to storage automatically
5. **Testing** is straightforward with pure functions

### **Zustand Deep Dive:**
1. **Middleware composition** creates powerful store behaviors
2. **Slices pattern** organizes large stores modularly
3. **Optimistic updates** improve perceived performance
4. **Selective subscriptions** prevent unnecessary re-renders
5. **Minimal API** reduces cognitive load

### **Choose Based On:**
- **Redux** → Large apps, need DevTools, complex workflows
- **Zustand** → Small/medium apps, bundle size critical, want simplicity
