# 🗂️ Topic 33: State Management Comparison - Redux Toolkit vs Zustand vs Context API

## 1. ⭐ Senior/Staff Summary

State management trong React không phải là câu hỏi “Redux hay Zustand?”. Câu hỏi đúng là: **state này thuộc loại nào, thay đổi bao lâu một lần, ai cần đọc nó, có cần cache/debug/persist/test/time-travel không?**

Một app React thường có 4 nhóm state:

- **Local UI state**: modal open, input draft, hover, selected row. Dùng `useState`, `useReducer`.
- **URL state**: search params, pagination, filters, active tab. Dùng router/search params để share link và hỗ trợ back/forward.
- **Server state**: data từ backend, có cache/stale/refetch/pagination. Dùng React Query, SWR, RTK Query, Apollo.
- **Global client state**: auth session, cart draft, feature flags, editor state, wizard state. Dùng Redux Toolkit, Zustand, Jotai hoặc store tương tự.

So sánh nhanh:

- ✅ **Redux Toolkit**: hợp app lớn, nhiều developer, workflow phức tạp, cần strict pattern, DevTools tốt, middleware, replay/debug, normalized state.
- ✅ **Zustand**: hợp app nhỏ/vừa, team muốn ít boilerplate, selector đơn giản, store dễ tách slice, performance tốt nếu subscribe đúng.
- ✅ **Context API**: tốt cho dependency injection như theme, i18n, auth client, config ít đổi. Không nên dùng như global store cho state thay đổi liên tục.
- ✅ **Jotai**: hợp atomic state, granular updates, derived/async atoms, UI cần state nhỏ phân tán.
- ✅ **RTK Query / React Query / SWR**: hợp server state. Đừng tự viết loading/error/cache/refetch trong Redux slice nếu data là server cache.

> 💡 Senior mental model: **State nên sống ở nơi gần nhất có thể, nhưng đủ xa để những component cần nó đọc được.** Đưa state lên global quá sớm làm app khó debug, khó test và re-render nhiều hơn cần thiết.

## 2. 🧠 Key Mental Model

### 2.1. Phân loại state trước khi chọn tool

| Loại state | Ví dụ | Tool phù hợp | Vì sao |
|---|---|---|---|
| Local state | Modal open, input value, hover | `useState`, `useReducer` | Chỉ một component/subtree cần |
| URL state | `?page=2&sort=price`, active tab | React Router, Next router/search params | Shareable, back/forward đúng |
| Server state | Users, products, comments | React Query, SWR, RTK Query | Cache, stale, refetch, pagination |
| Global client state | Cart draft, auth status, editor state | Redux Toolkit, Zustand, Jotai | Nhiều nơi cần đọc/ghi |
| Dependency/config | Theme, locale, API client | Context API | Ít đổi, truyền dependency sâu |

### 2.2. Data ownership

```text
Backend sở hữu dữ liệu?
  → Server state: React Query / SWR / RTK Query.

Browser/session sở hữu dữ liệu?
  → Client state: Redux / Zustand / Jotai / local state.

URL cần mô tả màn hình hiện tại?
  → URL state.

Chỉ một component dùng?
  → Local state.
```

### 2.3. Re-render mental model

State update làm component re-render khi component đó subscribe/read state đó:

- `useState`: component chứa state re-render.
- `Context`: mọi consumer đọc context value sẽ re-render khi `value` identity đổi.
- Redux `useSelector`: component re-render nếu selector result đổi theo equality check.
- Zustand selector: component re-render nếu selected slice đổi.
- Jotai atom: component re-render nếu atom đang đọc đổi.

> ⚠️ Performance không nằm ở “library nào nhanh nhất” một cách tuyệt đối. Nó nằm ở **subscription granularity**, reference equality, selector stability và cách chia state.

## 3. 📚 Main Concepts

### 3.1. Redux Toolkit

Redux Toolkit là cách dùng Redux hiện đại. Nó cung cấp `configureStore`, `createSlice`, Immer mặc định cho reducers, DevTools, middleware setup và RTK Query.

**Hợp khi:**

- App lớn, nhiều team cùng sửa state.
- Business workflow phức tạp: cart, checkout, editor, permissions, multi-step flows.
- Cần audit/debug tốt: Redux DevTools, action log, time-travel.
- Cần normalized state, selectors, middleware, persistence.
- Team muốn convention rõ để onboarding.

**Không hợp khi:**

- App nhỏ/prototype.
- Chỉ cần vài global flags.
- Server state là phần lớn nhu cầu nhưng lại không dùng RTK Query/React Query.
- Team bị chậm vì boilerplate mà không có lợi ích debug/process tương ứng.

```ts
import { configureStore, createSlice, PayloadAction } from '@reduxjs/toolkit';

type CartItem = {
  id: string;
  quantity: number;
};

type CartState = {
  items: CartItem[];
};

const initialState: CartState = {
  items: [],
};

const cartSlice = createSlice({
  name: 'cart',
  initialState,
  reducers: {
    addItem(state, action: PayloadAction<CartItem>) {
      const existing = state.items.find((item) => item.id === action.payload.id);

      if (existing) {
        existing.quantity += action.payload.quantity;
      } else {
        state.items.push(action.payload);
      }
    },
    removeItem(state, action: PayloadAction<string>) {
      state.items = state.items.filter((item) => item.id !== action.payload);
    },
  },
});

export const { addItem, removeItem } = cartSlice.actions;

export const store = configureStore({
  reducer: {
    cart: cartSlice.reducer,
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;
```

### 3.2. RTK Query

RTK Query là data fetching/cache layer trong Redux Toolkit. Nó giải quyết server state: loading, error, cache, invalidation, polling, refetch và optimistic update.

```ts
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

type User = {
  id: string;
  name: string;
};

export const usersApi = createApi({
  reducerPath: 'usersApi',
  baseQuery: fetchBaseQuery({ baseUrl: '/api' }),
  tagTypes: ['User'],
  endpoints: (builder) => ({
    getUsers: builder.query<User[], void>({
      query: () => '/users',
      providesTags: ['User'],
    }),
    updateUser: builder.mutation<User, Partial<User> & { id: string }>({
      query: ({ id, ...patch }) => ({
        url: `/users/${id}`,
        method: 'PATCH',
        body: patch,
      }),
      invalidatesTags: ['User'],
    }),
  }),
});

export const { useGetUsersQuery, useUpdateUserMutation } = usersApi;
```

> ✅ Rule: Nếu state đến từ API và cần cache/refetch, hãy dùng React Query/SWR/RTK Query thay vì tự tạo `loading/data/error` slice thủ công.

### 3.3. Normalized state và selectors

Redux mạnh khi state được normalize:

```ts
import { createEntityAdapter, createSlice } from '@reduxjs/toolkit';

type Product = {
  id: string;
  name: string;
  price: number;
};

const productsAdapter = createEntityAdapter<Product>();

const productsSlice = createSlice({
  name: 'products',
  initialState: productsAdapter.getInitialState(),
  reducers: {
    productAdded: productsAdapter.addOne,
    productsReceived: productsAdapter.setAll,
    productUpdated: productsAdapter.updateOne,
  },
});
```

Normalized state giúp:

- update theo ID nhanh hơn
- tránh duplicate nested data
- selectors dễ memoize
- UI list/detail dùng chung source of truth

### 3.4. Reselect và derived data

Derived data nên nằm trong selector, không lưu duplicate trong state.

```ts
import { createSelector } from '@reduxjs/toolkit';
import type { RootState } from './store';

const selectCartItems = (state: RootState) => state.cart.items;
const selectProducts = (state: RootState) => state.products.entities;

export const selectCartTotal = createSelector(
  [selectCartItems, selectProducts],
  (items, products) =>
    items.reduce((total, item) => {
      const product = products[item.id];
      return total + (product?.price ?? 0) * item.quantity;
    }, 0)
);
```

**Pitfall:** nếu selector luôn return object/array mới mà không memoize, component có thể re-render liên tục.

### 3.5. Redux middleware

Middleware nằm giữa `dispatch(action)` và reducer. Nó dùng cho logging, analytics, async orchestration, persistence hoặc side effects.

```text
UI dispatch(action)
  ↓
middleware: logging / analytics / thunk / saga / listener
  ↓
reducer update state
  ↓
subscribers re-render
```

Redux Toolkit đã setup `redux-thunk` và dev checks mặc định. Với logic reactive phức tạp, có thể dùng `createListenerMiddleware`.

```ts
import { createListenerMiddleware } from '@reduxjs/toolkit';
import { addItem } from './cartSlice';

export const listenerMiddleware = createListenerMiddleware();

listenerMiddleware.startListening({
  actionCreator: addItem,
  effect: async (action) => {
    await fetch('/api/analytics/cart-add', {
      method: 'POST',
      body: JSON.stringify(action.payload),
    });
  },
});
```

### 3.6. Redux persist và hydration

Persist state hữu ích cho cart, draft, preferences. Nhưng không nên persist mọi thứ.

**Nên persist:**

- theme
- cart draft
- local preferences
- non-sensitive wizard draft

**Không nên persist:**

- access token nhạy cảm nếu threat model không cho phép
- server cache lớn
- permission data stale
- UI state tạm như modal open

SSR/hydration cần cẩn thận vì server không có `localStorage`. Với Next.js, persist store thường phải chạy ở client boundary.

### 3.7. Zustand

Zustand là store nhỏ, hook-based, ít boilerplate. Store không bị ràng buộc chặt với React component tree như Context.

**Hợp khi:**

- App nhỏ/vừa.
- Global client state không quá ceremony.
- Team muốn selector đơn giản và actions gần state.
- Cần persist/devtools/immer nhưng không muốn Redux structure.
- UI state hoặc domain state vừa phải: cart, filters, editor panels, auth view state.

**Không hợp khi:**

- Team lớn cần strict convention/action log chuẩn.
- Workflow phức tạp cần audit replay/time-travel sâu.
- Cần ecosystem middleware như Redux Saga.
- Store bắt đầu phình to nhưng không chia slice rõ.

```ts
import { create } from 'zustand';

type CartStore = {
  items: Array<{ id: string; quantity: number }>;
  addItem: (id: string) => void;
  removeItem: (id: string) => void;
};

export const useCartStore = create<CartStore>((set) => ({
  items: [],
  addItem: (id) =>
    set((state) => {
      const existing = state.items.find((item) => item.id === id);

      if (existing) {
        return {
          items: state.items.map((item) =>
            item.id === id ? { ...item, quantity: item.quantity + 1 } : item
          ),
        };
      }

      return { items: [...state.items, { id, quantity: 1 }] };
    }),
  removeItem: (id) =>
    set((state) => ({
      items: state.items.filter((item) => item.id !== id),
    })),
}));
```

Component chỉ subscribe slice cần dùng:

```tsx
function CartCount() {
  const count = useCartStore((state) =>
    state.items.reduce((total, item) => total + item.quantity, 0)
  );

  return <span>{count}</span>;
}
```

### 3.8. Zustand middleware composition

Zustand có middleware như `devtools`, `persist`, `immer`, `subscribeWithSelector`.

```ts
import { create } from 'zustand';
import { devtools, persist, subscribeWithSelector } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

type CounterStore = {
  count: number;
  increment: () => void;
};

export const useCounterStore = create<CounterStore>()(
  devtools(
    persist(
      subscribeWithSelector(
        immer((set) => ({
          count: 0,
          increment: () =>
            set((state) => {
              state.count += 1;
            }),
        }))
      ),
      { name: 'counter-store' }
    ),
    { name: 'CounterStore' }
  )
);
```

**Rule:** Nếu dùng Immer middleware thì mutate draft được. Nếu không dùng Immer, phải immutable update thủ công.

### 3.9. Zustand slices pattern

Khi store lớn, chia slice để maintain tốt hơn.

```ts
import { create, StateCreator } from 'zustand';

type AuthSlice = {
  userId: string | null;
  setUserId: (userId: string | null) => void;
};

type CartSlice = {
  cartCount: number;
  incrementCart: () => void;
};

type AppStore = AuthSlice & CartSlice;

const createAuthSlice: StateCreator<AppStore, [], [], AuthSlice> = (set) => ({
  userId: null,
  setUserId: (userId) => set({ userId }),
});

const createCartSlice: StateCreator<AppStore, [], [], CartSlice> = (set) => ({
  cartCount: 0,
  incrementCart: () => set((state) => ({ cartCount: state.cartCount + 1 })),
});

export const useAppStore = create<AppStore>()((...args) => ({
  ...createAuthSlice(...args),
  ...createCartSlice(...args),
}));
```

### 3.10. Zustand async actions và error handling

Zustand không ép async pattern. Action có thể `async`, nhưng cần state rõ cho loading/error.

```ts
type ProfileStore = {
  profile: { id: string; name: string } | null;
  loading: boolean;
  error: string | null;
  fetchProfile: () => Promise<void>;
};

export const useProfileStore = create<ProfileStore>((set) => ({
  profile: null,
  loading: false,
  error: null,
  fetchProfile: async () => {
    set({ loading: true, error: null });

    try {
      const response = await fetch('/api/profile');

      if (!response.ok) {
        throw new Error('Cannot load profile');
      }

      set({ profile: await response.json(), loading: false });
    } catch (error) {
      set({
        error: error instanceof Error ? error.message : 'Unknown error',
        loading: false,
      });
    }
  },
}));
```

> ⚠️ Nếu data là server cache cần stale/refetch/pagination, dùng React Query/SWR/RTK Query thay vì tự build cache bằng Zustand.

### 3.11. Context API

Context giúp truyền data sâu mà không prop drilling. Nó không được thiết kế như high-frequency global state manager.

**Hợp khi:**

- theme
- locale/i18n
- feature flags ít đổi
- auth client/session snapshot ít đổi
- dependency injection: API client, logger, config

**Không hợp khi:**

- cart update liên tục
- form state lớn
- table filters thay đổi từng keystroke
- websocket event stream
- state nhiều consumer đọc nhiều phần khác nhau

```tsx
import { createContext, useContext } from 'react';

type Theme = 'light' | 'dark';

const ThemeContext = createContext<Theme>('light');

export function ThemeProvider({
  theme,
  children,
}: {
  theme: Theme;
  children: React.ReactNode;
}) {
  return <ThemeContext.Provider value={theme}>{children}</ThemeContext.Provider>;
}

export function useTheme() {
  return useContext(ThemeContext);
}
```

Nếu context value là object, memoize value hoặc tách context theo concern:

```tsx
const AuthStateContext = createContext<{ userId: string | null } | null>(null);
const AuthActionsContext = createContext<{ logout: () => void } | null>(null);
```

### 3.12. Jotai

Jotai dùng atomic state: mỗi atom là một đơn vị state nhỏ. Component chỉ re-render khi atom nó đọc thay đổi.

**Hợp khi:**

- state nhỏ, phân tán
- derived atoms
- async atoms + Suspense
- granular updates
- UI/editor cần nhiều state độc lập

```tsx
import { atom, useAtom, useAtomValue } from 'jotai';

const countAtom = atom(0);
const doubledAtom = atom((get) => get(countAtom) * 2);

function Counter() {
  const [count, setCount] = useAtom(countAtom);
  const doubled = useAtomValue(doubledAtom);

  return (
    <button onClick={() => setCount((value) => value + 1)}>
      {count} / {doubled}
    </button>
  );
}
```

Async atom:

```tsx
import { Suspense } from 'react';
import { atom, useAtomValue } from 'jotai';

const userAtom = atom(async () => {
  const response = await fetch('/api/me');
  return response.json() as Promise<{ name: string }>;
});

function UserProfile() {
  const user = useAtomValue(userAtom);
  return <p>{user.name}</p>;
}

export function App() {
  return (
    <Suspense fallback={<p>Loading...</p>}>
      <UserProfile />
    </Suspense>
  );
}
```

### 3.13. Comparison table

| Tiêu chí | Redux Toolkit | Zustand | Context API | Jotai |
|---|---|---|---|---|
| Primary use | Global client state phức tạp | Global client state nhẹ/vừa | Dependency injection | Atomic state |
| Boilerplate | Medium | Low | Low | Low/Medium |
| Debugging | Rất mạnh | Tốt với devtools | Hạn chế | Tốt |
| Performance | Tốt nếu selector đúng | Tốt nếu selector đúng | Dễ re-render rộng | Granular |
| Team convention | Rất tốt | Cần tự đặt convention | Không đủ cho app lớn | Cần hiểu atom model |
| Server state | RTK Query | Không phải trọng tâm | Không phù hợp | Có async atom, nhưng cache app-level cần cân nhắc |
| Best for | Enterprise, complex flows | Small/mid apps, fast iteration | Theme/i18n/config | Fine-grained UI state |

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Sai: dùng Redux slice cho server cache đơn giản

```ts
// ❌ Không nên nếu chỉ để fetch/cache users.
const usersSlice = createSlice({
  name: 'users',
  initialState: { data: [], loading: false, error: null },
  reducers: {
    fetchStart(state) {
      state.loading = true;
    },
    fetchSuccess(state, action) {
      state.data = action.payload;
      state.loading = false;
    },
  },
});
```

### 4.2. Đúng hơn: React Query hoặc RTK Query cho server state

```tsx
import { useQuery } from '@tanstack/react-query';

function UsersTable() {
  const { data = [], isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: fetchUsers,
    staleTime: 5 * 60 * 1000,
  });

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Cannot load users</p>;

  return <Table rows={data} />;
}
```

### 4.3. Sai: Context chứa object state thay đổi liên tục

```tsx
// ❌ Mỗi lần cart đổi, mọi consumer của AppContext có thể re-render.
const AppContext = createContext<{
  user: User | null;
  cart: CartItem[];
  theme: 'light' | 'dark';
} | null>(null);

function AppProvider({ children }: { children: React.ReactNode }) {
  const [state, setState] = useState({
    user: null,
    cart: [],
    theme: 'light' as const,
  });

  return <AppContext.Provider value={state}>{children}</AppContext.Provider>;
}
```

### 4.4. Đúng hơn: tách state theo ownership

```tsx
const ThemeContext = createContext<'light' | 'dark'>('light');
const useCartStore = create<CartStore>((set) => ({
  items: [],
  addItem: (id) => set((state) => ({ items: [...state.items, { id, quantity: 1 }] })),
}));

function CartBadge() {
  const count = useCartStore((state) => state.items.length);
  return <span>{count}</span>;
}
```

### 4.5. Undo/redo pattern với Redux

```ts
type HistoryState<T> = {
  past: T[];
  present: T;
  future: T[];
};

function undoable<T>(reducer: (state: T, action: unknown) => T) {
  return (state: HistoryState<T>, action: { type: string }) => {
    if (action.type === 'UNDO') {
      const previous = state.past.at(-1);
      if (!previous) return state;

      return {
        past: state.past.slice(0, -1),
        present: previous,
        future: [state.present, ...state.future],
      };
    }

    if (action.type === 'REDO') {
      const next = state.future[0];
      if (!next) return state;

      return {
        past: [...state.past, state.present],
        present: next,
        future: state.future.slice(1),
      };
    }

    const newPresent = reducer(state.present, action);

    if (newPresent === state.present) return state;

    return {
      past: [...state.past, state.present],
      present: newPresent,
      future: [],
    };
  };
}
```

### 4.6. Testing Redux slice

```ts
import { addItem, removeItem } from './cartSlice';
import cartReducer from './cartSlice';

test('adds item to cart', () => {
  const state = cartReducer(undefined, addItem({ id: 'p1', quantity: 1 }));

  expect(state.items).toEqual([{ id: 'p1', quantity: 1 }]);
});

test('removes item from cart', () => {
  const state = cartReducer(
    { items: [{ id: 'p1', quantity: 1 }] },
    removeItem('p1')
  );

  expect(state.items).toEqual([]);
});
```

### 4.7. Testing Zustand store

```ts
import { useCartStore } from './cartStore';

beforeEach(() => {
  useCartStore.setState({ items: [] });
});

test('adds item', () => {
  useCartStore.getState().addItem('p1');

  expect(useCartStore.getState().items).toEqual([{ id: 'p1', quantity: 1 }]);
});
```

## 5. 🏗️ Production Notes / React Implications

### 5.1. Performance

Performance phụ thuộc vào cách subscribe:

- Redux: dùng selector nhỏ, memoized selectors cho derived data.
- Zustand: dùng selector, tránh `useStore()` lấy cả store trong component lớn.
- Context: tách context theo concern, memoize `value`, tránh high-frequency updates.
- Jotai: chia atom hợp lý, tránh atom quá lớn.

```tsx
// ❌ Component re-render khi bất kỳ field nào trong store đổi.
const store = useAppStore();

// ✅ Chỉ re-render khi userId đổi.
const userId = useAppStore((state) => state.userId);
```

### 5.2. Reference equality và immutability

React/Redux/Zustand đều dựa nhiều vào reference equality để biết state có đổi không.

```ts
// ❌ Mutate trực tiếp nếu không có Immer.
set((state) => {
  state.items.push(item);
  return state;
});

// ✅ Immutable update.
set((state) => ({
  items: [...state.items, item],
}));
```

Redux Toolkit reducers dùng Immer mặc định, nên có thể viết mutation-style trong reducer. Zustand chỉ làm được vậy nếu thêm `immer` middleware.

### 5.3. SSR và hydration

Với SSR/Next.js:

- Không tạo singleton store chứa request-specific data trên server.
- Persist state từ `localStorage` chỉ hydrate ở client.
- Server state nên preload/dehydrate bằng data library nếu cần.
- Auth/session nên rõ ranh giới server/client.
- Tránh mismatch nếu UI render khác trước và sau persist hydration.

### 5.4. Security

State client không phải security boundary:

- Không tin `role`, `permission`, `price`, `discount` trong client store.
- Không persist access token bừa bãi.
- Không lưu PII nhạy cảm vào Redux DevTools/logs.
- Không gửi toàn bộ global state lên API.
- Server phải validate permission và business rules.

### 5.5. Observability và debugging

Redux mạnh ở action log và DevTools. Zustand có devtools middleware nhưng cần action naming/convention tốt hơn nếu store lớn. Với production debugging, nên track:

- action/mutation quan trọng
- failed persistence
- hydration mismatch
- stale server state
- store size tăng bất thường
- expensive selectors

### 5.6. Maintainability

State global nên có ownership:

- domain slice/store rõ: `auth`, `cart`, `editor`, `notifications`
- API payload type tách khỏi UI state type
- selectors/actions export có convention
- tests cho reducer/store critical
- migration plan nếu store quá lớn

## 6. ⚠️ Common Pitfalls

### 6.1. Dùng Redux/Zustand cho server state

Nếu cần cache, stale time, refetch on focus, retry, pagination, optimistic update, hãy dùng React Query/SWR/RTK Query. Redux/Zustand chỉ nên giữ client state thật sự.

### 6.2. Dùng Context như global store high-frequency

Context update làm consumer re-render theo context value. Với state thay đổi liên tục, hãy dùng store có selector hoặc tách context cực nhỏ.

### 6.3. Không normalize state phức tạp

Nested state sâu gây update khó, duplicate data, selector phức tạp. Với entity có ID, normalize.

### 6.4. Derived state bị lưu duplicate

Ví dụ lưu cả `items` và `total` trong state, rồi quên update `total`. Hãy tính bằng selector nếu có thể.

### 6.5. Zustand mutate trực tiếp khi không dùng Immer

Zustand không tự dùng Immer. Nếu mutate object/array và return cùng reference, UI có thể không update đúng.

### 6.6. Selector return object mới mỗi render

```tsx
// ⚠️ Có thể re-render thường xuyên vì object mới.
const data = useStore((state) => ({
  user: state.user,
  cart: state.cart,
}));
```

Dùng selector nhỏ, shallow equality hoặc tách subscription.

### 6.7. Persist quá nhiều

Persist toàn store làm state stale, tăng storage, có nguy cơ leak data và gây hydration bug. Chỉ persist phần thật sự cần.

### 6.8. Store thành global dumping ground

Không phải state nào cũng đưa vào store. Local state nên ở local, URL state nên ở URL, server state nên ở cache layer.

### 6.9. Không reset store khi logout

Logout phải clear client state nhạy cảm: profile, cart private, permissions, drafts tùy policy.

### 6.10. Không test state transitions

State management bug thường nằm ở transition: add/remove/update/reset/error. Test reducer/store actions trực tiếp rẻ và hiệu quả.

## 7. ✅ Decision Guide / Checklist

### 7.1. Chọn tool theo tình huống

| Tình huống | Nên chọn |
|---|---|
| App lớn, nhiều team, cần convention mạnh | Redux Toolkit |
| Cần server cache trong Redux ecosystem | RTK Query |
| App nhỏ/vừa, muốn ít boilerplate | Zustand |
| Custom editor/UI state nhiều phần nhỏ | Zustand hoặc Jotai |
| Atomic/derived state granular | Jotai |
| Theme/locale/config ít đổi | Context API |
| API data có cache/refetch/retry | React Query/SWR/RTK Query |
| Search/filter/pagination cần share link | URL state |
| State chỉ dùng trong một component | `useState` / `useReducer` |

### 7.2. Checklist trước khi đưa state lên global

- [ ] State này có thật sự được nhiều subtree dùng không?
- [ ] Có thể đưa vào URL không?
- [ ] Có phải server state không?
- [ ] Có cần persist không?
- [ ] Có chứa dữ liệu nhạy cảm không?
- [ ] Update frequency cao không?
- [ ] Component có thể subscribe slice nhỏ không?
- [ ] Có cần DevTools/action log/time-travel không?
- [ ] Có cần normalized entity state không?
- [ ] Có test cho transition quan trọng không?

### 7.3. Redux checklist

- [ ] Dùng Redux Toolkit, không viết plain Redux ceremony cũ.
- [ ] Dùng RTK Query cho server state nếu ở Redux ecosystem.
- [ ] Normalize entity state lớn.
- [ ] Dùng memoized selectors cho derived data.
- [ ] Không persist toàn store.
- [ ] Không log dữ liệu nhạy cảm vào DevTools.
- [ ] Reducer/action naming rõ theo domain.

### 7.4. Zustand checklist

- [ ] Component dùng selector, không lấy cả store.
- [ ] Immutable update hoặc dùng Immer middleware.
- [ ] Store lớn được chia slices.
- [ ] Async actions có loading/error rõ.
- [ ] Persist partial state, có version/migration nếu cần.
- [ ] Reset store khi logout nếu chứa user data.
- [ ] Test actions trực tiếp bằng `getState()` / `setState()`.

### 7.5. Context checklist

- [ ] Context value ít đổi.
- [ ] Tách state/actions context nếu cần.
- [ ] Memoize object/function value.
- [ ] Không đặt form/table/editor state thay đổi liên tục vào một context lớn.
- [ ] Có custom hook để consumer dùng đúng provider.

## 8. 🎤 Short Interview Answer

Theo em, trước khi chọn Redux, Zustand hay Context, em sẽ phân loại state trước. Nếu là server state như users/products/comments thì em không đưa vào Redux slice thủ công, mà dùng React Query, SWR hoặc RTK Query vì các tool đó xử lý cache, stale, retry và refetch tốt hơn.

Với global client state, Redux Toolkit hợp app lớn cần convention, DevTools, action log, middleware và normalized state. Zustand hợp app nhỏ đến vừa, cần ít boilerplate, store đơn giản và selector theo slice. Context API thì em chủ yếu dùng cho dependency injection như theme, locale, auth client hoặc config ít đổi, chứ không dùng như state manager cho data thay đổi liên tục vì dễ làm nhiều consumer re-render.

Điểm quan trọng trong production là giữ state gần nơi dùng nhất, không biến global store thành chỗ chứa mọi thứ. Em cũng chú ý selector granularity, immutability, persist policy, SSR hydration, reset state khi logout và test các state transition quan trọng.

## 9. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| State management | Cách tổ chức, đọc, ghi và đồng bộ state trong app |
| Local state | State chỉ cần trong một component/subtree |
| Global state | State nhiều vùng trong app cần dùng |
| Server state | Data do backend sở hữu, frontend cache lại |
| URL state | State nằm trong URL/search params |
| Redux Toolkit | Bộ công cụ Redux hiện đại với `configureStore`, `createSlice`, Immer |
| RTK Query | Data fetching/cache layer trong Redux Toolkit |
| Zustand | State library nhỏ, hook-based, selector-friendly |
| Context API | React API truyền data sâu qua component tree |
| Jotai | Atomic state management library cho React |
| Atom | Đơn vị state nhỏ trong Jotai |
| Selector | Hàm chọn một phần state cho component |
| Memoization | Cache kết quả tính toán khi input chưa đổi |
| Reselect | Library/helper tạo memoized selectors cho Redux |
| Middleware | Lớp xử lý nằm giữa dispatch và reducer |
| DevTools | Công cụ xem action/state để debug |
| Time-travel debugging | Quay lại các state trước bằng action log |
| Normalized state | Lưu entity dạng flat theo ID thay vì nested sâu |
| Entity adapter | Helper của Redux Toolkit để quản lý normalized entity |
| Immer | Library cho phép viết mutation-style nhưng tạo immutable update |
| Persist | Lưu một phần state vào storage |
| Hydration | Đồng bộ state client với HTML/state ban đầu từ server |
| Reference equality | So sánh object/array theo reference, không deep compare |
| Structural sharing | Giữ reference cũ cho phần state không đổi để tối ưu render |

## 10. 📚 Nguồn chính thức đã đối chiếu

- Redux Toolkit docs: <https://redux-toolkit.js.org/introduction/getting-started>
- Zustand docs: <https://zustand.docs.pmnd.rs/>
- React Context docs: <https://react.dev/learn/passing-data-deeply-with-context>
- Jotai docs: <https://jotai.org/>
