# 🔄 Q17: React Query (TanStack Query) - Data Fetching, Caching & State Management

## **📚 Giới Thiệu**

**React Query (TanStack Query)** là thư viện quản lý server state mạnh mẽ nhất cho React.

**❓ Tại sao cần React Query?**

```typescript
// ❌ TRƯỚC KHI CÓ REACT QUERY: Quản lý state thủ công
function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    setLoading(true);
    fetch('/api/users')
      .then((res) => res.json())
      .then((data) => {
        setUsers(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err);
        setLoading(false);
      });
  }, []);

  // Vấn đề:
  // ❌ Không cache → gọi API mỗi khi component mount
  // ❌ Không refetch tự động khi data cũ
  // ❌ Không handle race conditions
  // ❌ Phải tự quản lý loading, error, data
  // ❌ Không optimistic updates
  // ❌ Không background refetch
  // ❌ Code dài dòng, lặp lại nhiều lần
}

// ✅ SAU KHI CÓ REACT QUERY: Gọn gàng, mạnh mẽ
function UserList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => fetch('/api/users').then((res) => res.json()),
  });

  // ✅ Auto caching
  // ✅ Auto refetch khi window focus
  // ✅ Auto retry khi failed
  // ✅ Handle race conditions
  // ✅ Background refetch
  // ✅ Optimistic updates
  // ✅ Code ngắn gọn, dễ đọc
}
```

**🎯 React Query giải quyết:**

- ✅ **Caching**: Cache data, không gọi lại API không cần thiết
- ✅ **Background Updates**: Tự động refetch khi data cũ
- ✅ **Deduplication**: Nhiều components cùng query → chỉ 1 request
- ✅ **Pagination & Infinite Scroll**: Built-in support
- ✅ **Optimistic Updates**: Update UI trước, sync sau
- ✅ **Offline Support**: Hoạt động khi mất mạng
- ✅ **DevTools**: Debug dễ dàng

---

## **📦 Installation & Setup**

```bash
# Install React Query
npm install @tanstack/react-query

# Install DevTools (optional)
npm install @tanstack/react-query-devtools
```

**🔧 Setup QueryClient:**

```typescript
// =====================================
// src/main.tsx - Setup QueryClient
// =====================================

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import App from './App';

// ✅ Create QueryClient với default options
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      // ⏱️ Cache time: Thời gian data được lưu trong cache (5 phút)
      staleTime: 5 * 60 * 1000, // 5 minutes

      // 🔄 Refetch khi window focus (user quay lại tab)
      refetchOnWindowFocus: true,

      // 🔄 Refetch khi reconnect (sau khi mất mạng)
      refetchOnReconnect: true,

      // 🔄 Refetch khi component mount
      refetchOnMount: true,

      // 🔁 Số lần retry khi request failed
      retry: 3,

      // ⏳ Retry delay (exponential backoff)
      retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),

      // 🗑️ Garbage collection time: Xóa cache sau 10 phút không dùng
      gcTime: 10 * 60 * 1000, // 10 minutes (formerly cacheTime)
    },
    mutations: {
      // 🔁 Retry mutations (thường không retry)
      retry: 0,
    },
  },
});

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <App />

      {/* ✅ DevTools: Chỉ hiện ở development */}
      <ReactQueryDevtools initialIsOpen={false} position="bottom-right" />
    </QueryClientProvider>
  </StrictMode>
);
```

---

## **🔍 USEQUERY - Fetching Data**

### **📌 Basic Usage**

```typescript
// =====================================
// USEQUERY - CƠ BẢN
// =====================================

import { useQuery } from '@tanstack/react-query';

function UserProfile({ userId }: { userId: string }) {
  // ✅ useQuery nhận object với queryKey và queryFn
  const {
    data, // ✅ Data trả về (undefined khi loading lần đầu)
    isLoading, // ✅ true khi loading lần đầu (chưa có cache)
    isFetching, // ✅ true khi đang fetch (kể cả background refetch)
    isError, // ✅ true khi có error
    error, // ✅ Error object
    isSuccess, // ✅ true khi fetch thành công
    refetch, // ✅ Function để refetch manually
    dataUpdatedAt, // ✅ Timestamp lần cuối data được update
  } = useQuery({
    // 🔑 queryKey: Array dùng để identify query (cũng là dependency)
    queryKey: ['user', userId],

    // 📡 queryFn: Function fetch data (phải return Promise)
    queryFn: async () => {
      const response = await fetch(`/api/users/${userId}`);
      if (!response.ok) throw new Error('Failed to fetch user');
      return response.json();
    },

    // ⏱️ Stale time: Thời gian data được coi là "fresh"
    // Nếu data < staleTime → không refetch
    staleTime: 5 * 60 * 1000, // 5 phút

    // 🗑️ GC time: Thời gian giữ data trong cache khi không dùng
    gcTime: 10 * 60 * 1000, // 10 phút

    // 🔄 Refetch options
    refetchOnWindowFocus: true, // Refetch khi user quay lại tab
    refetchOnReconnect: true, // Refetch khi reconnect internet
    refetchOnMount: true, // Refetch khi component mount

    // 🔁 Retry options
    retry: 3, // Retry 3 lần nếu failed
    retryDelay: 1000, // Delay 1s giữa các lần retry

    // ✅ Enabled: Chỉ fetch khi condition = true
    enabled: !!userId, // Chỉ fetch khi có userId
  });

  if (isLoading) return <div>Loading...</div>;
  if (isError) return <div>Error: {error.message}</div>;

  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.email}</p>
      <button onClick={() => refetch()}>Refresh</button>
    </div>
  );
}

// 🔑 QUERYKEY RULES:
/*
1. Query key là ARRAY: ['users', userId, { status: 'active' }]
2. Query key giống nhau → cùng 1 cache
3. Query key thay đổi → fetch lại data
4. Query key là dependency của queryFn

VD:
- ['users'] → Fetch tất cả users
- ['users', '123'] → Fetch user id 123
- ['users', '123', 'posts'] → Fetch posts của user 123
- ['users', { status: 'active' }] → Fetch active users
*/
```

### **📌 Query States**

```typescript
// =====================================
// QUERY STATES (Trạng thái của Query)
// =====================================

/*
┌─────────────────────────────────────────────────────────────────┐
│  QUERY STATUS                                                    │
├─────────────────────────────────────────────────────────────────┤
│  status: 'pending'   → Chưa có data (loading lần đầu)           │
│  status: 'error'     → Có error                                 │
│  status: 'success'   → Có data                                  │
├─────────────────────────────────────────────────────────────────┤
│  FETCH STATUS                                                    │
├─────────────────────────────────────────────────────────────────┤
│  fetchStatus: 'idle'      → Không fetch                         │
│  fetchStatus: 'fetching'  → Đang fetch                          │
│  fetchStatus: 'paused'    → Fetch bị pause (offline)            │
└─────────────────────────────────────────────────────────────────┘
*/

function DataComponent() {
  const query = useQuery({ queryKey: ['data'], queryFn: fetchData });

  // ✅ Các boolean helpers (derived states)
  const {
    isLoading, // status === 'pending'
    isError, // status === 'error'
    isSuccess, // status === 'success'

    isFetching, // fetchStatus === 'fetching'
    isPaused, // fetchStatus === 'paused'

    // ✅ Combined states
    isLoadingError, // isLoading + isError
    isRefetchError, // isError + data exists (refetch failed nhưng có cache)

    // ✅ Data states
    data, // Data trả về
    error, // Error object
    status, // 'pending' | 'error' | 'success'
    fetchStatus, // 'idle' | 'fetching' | 'paused'
  } = query;

  // 📊 STATE DIAGRAM:
  /*
  Initial → pending (isLoading = true)
           ↓
         fetching
           ↓
    ┌──────┴──────┐
    ↓             ↓
  success       error
  (data)        (error)
    │             │
    └──→ refetch ←┘
         ↓
       fetching (isRefetching = true)
         ↓
    ┌────┴────┐
    ↓         ↓
  success   error (isRefetchError = true, vẫn còn data cũ)
  */

  // ✅ Render based on states
  if (isLoading) return <Spinner />;
  if (isError) return <ErrorMessage error={error} />;

  // ✅ Background refetch indicator
  return (
    <div>
      {isFetching && <RefreshIndicator />}
      <DataDisplay data={data} />
    </div>
  );
}
```

### **📌 Dependent Queries (Sequential Queries)**

```typescript
// =====================================
// DEPENDENT QUERIES - Query phụ thuộc vào query khác
// =====================================

function UserPostsPage({ userId }: { userId: string }) {
  // 1️⃣ Fetch user first
  const { data: user } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  // 2️⃣ Fetch user's posts (chỉ khi đã có user)
  const { data: posts } = useQuery({
    queryKey: ['posts', user?.id],
    queryFn: () => fetchUserPosts(user!.id),
    enabled: !!user, // ✅ Chỉ fetch khi có user
  });

  // 3️⃣ Fetch post comments (chỉ khi đã có posts)
  const { data: comments } = useQuery({
    queryKey: ['comments', posts?.[0]?.id],
    queryFn: () => fetchPostComments(posts![0].id),
    enabled: !!posts && posts.length > 0, // ✅ Chỉ fetch khi có posts
  });

  return (
    <div>
      <h1>{user?.name}</h1>
      <PostList posts={posts} comments={comments} />
    </div>
  );
}

// 🎯 Use Case: Multi-step wizard
function CheckoutFlow() {
  const [step, setStep] = useState(1);

  // Step 1: Fetch cart
  const { data: cart } = useQuery({
    queryKey: ['cart'],
    queryFn: fetchCart,
    enabled: step >= 1,
  });

  // Step 2: Fetch shipping options (sau khi có cart)
  const { data: shippingOptions } = useQuery({
    queryKey: ['shipping', cart?.id],
    queryFn: () => fetchShipping(cart!.id),
    enabled: step >= 2 && !!cart,
  });

  // Step 3: Fetch payment methods (sau khi có shipping)
  const { data: paymentMethods } = useQuery({
    queryKey: ['payment', shippingOptions?.selected],
    queryFn: () => fetchPaymentMethods(shippingOptions!.selected),
    enabled: step >= 3 && !!shippingOptions,
  });

  return (
    <WizardSteps
      cart={cart}
      shipping={shippingOptions}
      payment={paymentMethods}
    />
  );
}
```

### **📌 Parallel Queries (Fetch nhiều data cùng lúc)**

```typescript
// =====================================
// PARALLEL QUERIES - Fetch song song
// =====================================

// ✅ Cách 1: Multiple useQuery
function Dashboard() {
  const users = useQuery({ queryKey: ['users'], queryFn: fetchUsers });
  const posts = useQuery({ queryKey: ['posts'], queryFn: fetchPosts });
  const comments = useQuery({ queryKey: ['comments'], queryFn: fetchComments });

  // ✅ Check loading state
  const isLoading = users.isLoading || posts.isLoading || comments.isLoading;

  if (isLoading) return <Spinner />;

  return (
    <div>
      <Users data={users.data} />
      <Posts data={posts.data} />
      <Comments data={comments.data} />
    </div>
  );
}

// ✅ Cách 2: useQueries (Dynamic queries)
import { useQueries } from '@tanstack/react-query';

function MultiUserProfile({ userIds }: { userIds: string[] }) {
  // ✅ useQueries: Fetch multiple queries với dynamic keys
  const userQueries = useQueries({
    queries: userIds.map((id) => ({
      queryKey: ['user', id],
      queryFn: () => fetchUser(id),
      staleTime: 5 * 60 * 1000,
    })),
  });

  // ✅ Check if all queries loaded
  const isLoading = userQueries.some((query) => query.isLoading);
  const isError = userQueries.some((query) => query.isError);

  // ✅ Get all data
  const users = userQueries.map((query) => query.data).filter(Boolean);

  if (isLoading) return <Spinner />;
  if (isError) return <Error />;

  return (
    <div>
      {users.map((user) => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}

// ✅ Cách 3: useQueries với combine (advanced)
function CombinedData() {
  const { data, isLoading } = useQueries({
    queries: [
      { queryKey: ['users'], queryFn: fetchUsers },
      { queryKey: ['posts'], queryFn: fetchPosts },
    ],
    combine: (results) => {
      // ✅ Combine results
      return {
        data: {
          users: results[0].data,
          posts: results[1].data,
        },
        isLoading: results.some((result) => result.isLoading),
      };
    },
  });

  return <Dashboard data={data} />;
}
```

---

## **✏️ USEMUTATION - Modifying Data (POST/PUT/DELETE)**

### **📌 Basic Mutation**

```typescript
// =====================================
// USEMUTATION - CẬP NHẬT DATA
// =====================================

import { useMutation, useQueryClient } from '@tanstack/react-query';

function CreateUserForm() {
  const queryClient = useQueryClient();

  // ✅ useMutation: Thực hiện POST/PUT/DELETE
  const mutation = useMutation({
    // 📡 mutationFn: Function thực hiện mutation
    mutationFn: async (newUser: User) => {
      const response = await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newUser),
      });
      if (!response.ok) throw new Error('Failed to create user');
      return response.json();
    },

    // ✅ onMutate: Chạy TRƯỚC khi mutation (optimistic update)
    onMutate: async (newUser) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: ['users'] });

      // Snapshot previous value
      const previousUsers = queryClient.getQueryData(['users']);

      // Optimistically update
      queryClient.setQueryData(['users'], (old: User[]) => [...old, newUser]);

      // Return context với previous data (để rollback nếu fail)
      return { previousUsers };
    },

    // ✅ onSuccess: Chạy khi mutation thành công
    onSuccess: (data, variables, context) => {
      console.log('✅ Created user:', data);

      // ✅ Invalidate queries để refetch
      queryClient.invalidateQueries({ queryKey: ['users'] });

      // ✅ Hoặc set data manually
      // queryClient.setQueryData(['user', data.id], data);
    },

    // ❌ onError: Chạy khi mutation failed
    onError: (error, variables, context) => {
      console.error('❌ Error:', error);

      // ✅ Rollback optimistic update
      if (context?.previousUsers) {
        queryClient.setQueryData(['users'], context.previousUsers);
      }
    },

    // 🏁 onSettled: Chạy sau khi mutation hoàn tất (dù success hay error)
    onSettled: () => {
      // Refetch để đảm bảo data sync
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);

    // ✅ Trigger mutation
    mutation.mutate({
      name: formData.get('name') as string,
      email: formData.get('email') as string,
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="name" placeholder="Name" />
      <input name="email" placeholder="Email" />

      <button
        type="submit"
        disabled={mutation.isPending} // ✅ Disable khi đang submit
      >
        {mutation.isPending ? 'Creating...' : 'Create User'}
      </button>

      {mutation.isError && (
        <div className="error">Error: {mutation.error.message}</div>
      )}

      {mutation.isSuccess && (
        <div className="success">User created successfully!</div>
      )}
    </form>
  );
}

// 📊 MUTATION STATES:
/*
status: 'idle'    → Chưa chạy
status: 'pending' → Đang chạy (isPending = true)
status: 'error'   → Failed (isError = true)
status: 'success' → Thành công (isSuccess = true)
*/
```

### **📌 Mutation với Optimistic Updates (Update trước, sync sau)**

```typescript
// =====================================
// OPTIMISTIC UPDATES - Cập nhật UI trước, sync sau
// =====================================

function TodoList() {
  const queryClient = useQueryClient();

  // ✅ Update todo mutation với optimistic update
  const updateTodoMutation = useMutation({
    mutationFn: async (updatedTodo: Todo) => {
      const response = await fetch(`/api/todos/${updatedTodo.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updatedTodo),
      });
      return response.json();
    },

    // ✅ onMutate: Update UI ngay lập tức (optimistic)
    onMutate: async (updatedTodo) => {
      // 1. Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: ['todos'] });

      // 2. Snapshot previous value (để rollback nếu fail)
      const previousTodos = queryClient.getQueryData<Todo[]>(['todos']);

      // 3. Optimistically update UI
      queryClient.setQueryData<Todo[]>(['todos'], (old) =>
        old
          ? old.map((todo) => (todo.id === updatedTodo.id ? updatedTodo : todo))
          : []
      );

      // 4. Return context (previousTodos để rollback)
      return { previousTodos };
    },

    // ❌ onError: Rollback nếu mutation failed
    onError: (err, updatedTodo, context) => {
      // Rollback về data cũ
      if (context?.previousTodos) {
        queryClient.setQueryData(['todos'], context.previousTodos);
      }

      // Show error toast
      toast.error('Failed to update todo');
    },

    // ✅ onSuccess: Invalidate queries để refetch (ensure sync)
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ['todos'] });
    },
  });

  // ✅ Toggle todo completed
  const handleToggle = (todo: Todo) => {
    updateTodoMutation.mutate({
      ...todo,
      completed: !todo.completed,
    });
  };

  return (
    <div>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          onToggle={() => handleToggle(todo)}
        />
      ))}
    </div>
  );
}

// 🎯 FLOW:
/*
1. User click checkbox
2. onMutate: UI update ngay lập tức (checkbox checked) ✅
3. mutationFn: Gửi request lên server 📡
4. onSuccess: Server trả về success → invalidate query → refetch ✅
   hoặc
   onError: Server trả về error → rollback UI về trạng thái cũ ❌
*/
```

### **📌 Delete Mutation với Optimistic Update**

```typescript
// =====================================
// DELETE MUTATION - Xóa data
// =====================================

function UserList() {
  const queryClient = useQueryClient();

  const deleteUserMutation = useMutation({
    mutationFn: async (userId: string) => {
      const response = await fetch(`/api/users/${userId}`, {
        method: 'DELETE',
      });
      if (!response.ok) throw new Error('Failed to delete user');
      return userId;
    },

    // ✅ Optimistic delete: Xóa UI trước
    onMutate: async (userId) => {
      await queryClient.cancelQueries({ queryKey: ['users'] });

      const previousUsers = queryClient.getQueryData<User[]>(['users']);

      // Remove user from UI ngay lập tức
      queryClient.setQueryData<User[]>(['users'], (old) =>
        old ? old.filter((user) => user.id !== userId) : []
      );

      return { previousUsers };
    },

    onError: (err, userId, context) => {
      // Rollback nếu delete failed
      if (context?.previousUsers) {
        queryClient.setQueryData(['users'], context.previousUsers);
      }
      toast.error('Failed to delete user');
    },

    onSuccess: (userId) => {
      toast.success('User deleted successfully');

      // Remove individual user query
      queryClient.removeQueries({ queryKey: ['user', userId] });
    },

    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  const handleDelete = (userId: string) => {
    if (confirm('Are you sure?')) {
      deleteUserMutation.mutate(userId);
    }
  };

  return (
    <div>
      {users.map((user) => (
        <UserCard
          key={user.id}
          user={user}
          onDelete={() => handleDelete(user.id)}
        />
      ))}
    </div>
  );
}
```

---

## **📄 PAGINATION & INFINITE SCROLL**

### **📌 Pagination với useQuery**

```typescript
// =====================================
// PAGINATION - Phân trang
// =====================================

function UserListWithPagination() {
  const [page, setPage] = useState(1);
  const pageSize = 10;

  // ✅ Query với page parameter
  const { data, isLoading, isPlaceholderData } = useQuery({
    queryKey: ['users', page],
    queryFn: () => fetchUsers({ page, pageSize }),

    // ✅ placeholderData: Giữ data cũ khi fetch page mới (UX tốt hơn)
    placeholderData: (previousData) => previousData,

    staleTime: 5000, // 5s
  });

  // ✅ Prefetch next page (UX optimization)
  const queryClient = useQueryClient();

  useEffect(() => {
    if (!isPlaceholderData && data?.hasMore) {
      // Prefetch page tiếp theo
      queryClient.prefetchQuery({
        queryKey: ['users', page + 1],
        queryFn: () => fetchUsers({ page: page + 1, pageSize }),
      });
    }
  }, [data, isPlaceholderData, page, queryClient]);

  return (
    <div>
      {isLoading ? <Spinner /> : <UserList users={data.users} />}

      <div className="pagination">
        <button
          onClick={() => setPage((prev) => Math.max(prev - 1, 1))}
          disabled={page === 1}
        >
          Previous
        </button>

        <span>Page {page}</span>

        <button
          onClick={() => setPage((prev) => prev + 1)}
          disabled={isPlaceholderData || !data?.hasMore}
        >
          Next
        </button>
      </div>

      {/* ✅ Loading indicator khi fetch next page */}
      {isPlaceholderData && <div>Loading next page...</div>}
    </div>
  );
}

// 📡 API Response format
interface PaginatedResponse<T> {
  data: T[];
  page: number;
  pageSize: number;
  total: number;
  hasMore: boolean;
}

async function fetchUsers({
  page,
  pageSize,
}: {
  page: number;
  pageSize: number;
}) {
  const response = await fetch(`/api/users?page=${page}&pageSize=${pageSize}`);
  return response.json() as Promise<PaginatedResponse<User>>;
}
```

### **📌 Infinite Scroll với useInfiniteQuery**

```typescript
// =====================================
// INFINITE SCROLL - Load more khi scroll
// =====================================

import { useInfiniteQuery } from '@tanstack/react-query';
import { useInView } from 'react-intersection-observer';

function InfiniteUserList() {
  // ✅ useInfiniteQuery: Built-in support cho infinite scroll
  const {
    data,
    isLoading,
    isError,
    error,
    fetchNextPage, // ✅ Function để load more
    hasNextPage, // ✅ Còn page tiếp theo không?
    isFetchingNextPage, // ✅ Đang load more?
  } = useInfiniteQuery({
    queryKey: ['users', 'infinite'],

    // ✅ queryFn nhận pageParam
    queryFn: async ({ pageParam = 1 }) => {
      const response = await fetch(`/api/users?page=${pageParam}&pageSize=10`);
      return response.json();
    },

    // ✅ getNextPageParam: Determine next page number
    getNextPageParam: (lastPage, allPages) => {
      // Nếu còn data → return page tiếp theo
      return lastPage.hasMore ? allPages.length + 1 : undefined;
    },

    // ✅ getPreviousPageParam (optional, cho bi-directional scroll)
    getPreviousPageParam: (firstPage, allPages) => {
      return firstPage.page > 1 ? firstPage.page - 1 : undefined;
    },

    initialPageParam: 1, // ✅ Page đầu tiên
  });

  // ✅ Auto load more khi scroll đến cuối
  const { ref, inView } = useInView();

  useEffect(() => {
    if (inView && hasNextPage && !isFetchingNextPage) {
      fetchNextPage();
    }
  }, [inView, hasNextPage, isFetchingNextPage, fetchNextPage]);

  if (isLoading) return <Spinner />;
  if (isError) return <Error message={error.message} />;

  // ✅ data.pages: Array of pages
  // [
  //   { users: [...], page: 1, hasMore: true },
  //   { users: [...], page: 2, hasMore: true },
  //   { users: [...], page: 3, hasMore: false },
  // ]

  return (
    <div>
      {data.pages.map((page, i) => (
        <div key={i}>
          {page.users.map((user) => (
            <UserCard key={user.id} user={user} />
          ))}
        </div>
      ))}

      {/* ✅ Trigger element để detect scroll */}
      <div ref={ref} style={{ height: 20 }}>
        {isFetchingNextPage && <Spinner />}
      </div>

      {!hasNextPage && <div>No more users</div>}

      {/* ✅ Load more button (fallback) */}
      <button
        onClick={() => fetchNextPage()}
        disabled={!hasNextPage || isFetchingNextPage}
      >
        {isFetchingNextPage ? 'Loading...' : 'Load More'}
      </button>
    </div>
  );
}

// ✅ Flatten all pages data (helper)
function useAllUsers() {
  const query = useInfiniteQuery({
    /* ... */
  });

  const allUsers = query.data?.pages.flatMap((page) => page.users) ?? [];

  return { ...query, allUsers };
}
```

---

## **🔧 QUERYCLIENT METHODS - Manual Cache Manipulation**

```typescript
// =====================================
// QUERYCLIENT METHODS - Thao tác cache thủ công
// =====================================

import { useQueryClient } from '@tanstack/react-query';

function DataManagement() {
  const queryClient = useQueryClient();

  // ✅ 1. invalidateQueries: Mark queries as stale → refetch
  const handleInvalidate = () => {
    // Invalidate tất cả queries
    queryClient.invalidateQueries();

    // Invalidate specific query
    queryClient.invalidateQueries({ queryKey: ['users'] });

    // Invalidate với filter
    queryClient.invalidateQueries({
      queryKey: ['users'],
      exact: true, // Chỉ ['users'], không ['users', '123']
    });

    // Invalidate queries bắt đầu với ['users']
    queryClient.invalidateQueries({
      queryKey: ['users'],
      refetchType: 'active', // Chỉ refetch active queries
    });
  };

  // ✅ 2. refetchQueries: Force refetch ngay lập tức
  const handleRefetch = async () => {
    await queryClient.refetchQueries({ queryKey: ['users'] });
    console.log('Refetch completed');
  };

  // ✅ 3. setQueryData: Set data manually (không fetch)
  const handleSetData = () => {
    // Set data cho query
    queryClient.setQueryData(['users'], (oldData: User[]) => {
      return [...oldData, { id: '999', name: 'New User' }];
    });

    // Set data cho specific user
    queryClient.setQueryData(['user', '123'], {
      id: '123',
      name: 'Updated Name',
    });
  };

  // ✅ 4. getQueryData: Đọc data từ cache
  const handleGetData = () => {
    const users = queryClient.getQueryData<User[]>(['users']);
    console.log('Cached users:', users);

    const user = queryClient.getQueryData<User>(['user', '123']);
    console.log('Cached user:', user);
  };

  // ✅ 5. removeQueries: Xóa queries khỏi cache
  const handleRemove = () => {
    // Xóa specific query
    queryClient.removeQueries({ queryKey: ['user', '123'] });

    // Xóa tất cả user queries
    queryClient.removeQueries({ queryKey: ['users'] });
  };

  // ✅ 6. cancelQueries: Cancel ongoing queries
  const handleCancel = async () => {
    await queryClient.cancelQueries({ queryKey: ['users'] });
    console.log('Queries cancelled');
  };

  // ✅ 7. prefetchQuery: Prefetch data trước khi cần
  const handlePrefetch = async () => {
    await queryClient.prefetchQuery({
      queryKey: ['users', 'page-2'],
      queryFn: () => fetchUsers({ page: 2 }),
      staleTime: 5 * 60 * 1000,
    });
    console.log('Prefetched page 2');
  };

  // ✅ 8. ensureQueryData: Fetch nếu chưa có cache
  const handleEnsure = async () => {
    const data = await queryClient.ensureQueryData({
      queryKey: ['users'],
      queryFn: fetchUsers,
    });
    console.log('Data:', data);
  };

  // ✅ 9. fetchQuery: Fetch và return data (không cache)
  const handleFetch = async () => {
    const data = await queryClient.fetchQuery({
      queryKey: ['temp-data'],
      queryFn: fetchSomeData,
      staleTime: 0, // Don't cache
    });
    console.log('Fetched:', data);
  };

  // ✅ 10. getQueriesData: Đọc multiple queries
  const handleGetMultiple = () => {
    // Get all queries starting with ['users']
    const allUserQueries = queryClient.getQueriesData({ queryKey: ['users'] });
    console.log('All user queries:', allUserQueries);
    // Returns: [
    //   [['users'], [...users]],
    //   [['users', '123'], {...user}],
    // ]
  };

  // ✅ 11. setQueriesData: Update multiple queries
  const handleSetMultiple = () => {
    queryClient.setQueriesData({ queryKey: ['users'] }, (oldData: any) => {
      // Update all queries matching ['users']
      return oldData ? [...oldData, newUser] : [newUser];
    });
  };

  return (
    <div>
      <button onClick={handleInvalidate}>Invalidate</button>
      <button onClick={handleRefetch}>Refetch</button>
      <button onClick={handleSetData}>Set Data</button>
      <button onClick={handleGetData}>Get Data</button>
      <button onClick={handleRemove}>Remove</button>
      <button onClick={handleCancel}>Cancel</button>
      <button onClick={handlePrefetch}>Prefetch</button>
    </div>
  );
}
```

---

## **⚡ BEST PRACTICES - Tối Ưu & Patterns**

### **1️⃣ Query Keys Best Practices**

```typescript
// =====================================
// QUERY KEYS BEST PRACTICES
// =====================================

// ❌ BAD: Hardcode query keys
const { data } = useQuery({
  queryKey: ['users'],
  queryFn: fetchUsers,
});

// ✅ GOOD: Centralized query keys
export const queryKeys = {
  // All users
  users: ['users'] as const,

  // User list with filters
  userList: (filters: UserFilters) => ['users', 'list', filters] as const,

  // Single user
  user: (id: string) => ['users', 'detail', id] as const,

  // User's posts
  userPosts: (userId: string) => ['users', 'detail', userId, 'posts'] as const,

  // Posts
  posts: ['posts'] as const,
  postList: (filters: PostFilters) => ['posts', 'list', filters] as const,
  post: (id: string) => ['posts', 'detail', id] as const,
};

// ✅ Usage
const { data: users } = useQuery({
  queryKey: queryKeys.userList({ status: 'active' }),
  queryFn: () => fetchUsers({ status: 'active' }),
});

const { data: user } = useQuery({
  queryKey: queryKeys.user(userId),
  queryFn: () => fetchUser(userId),
});

// ✅ Invalidate với query keys
queryClient.invalidateQueries({ queryKey: queryKeys.users }); // Tất cả user queries
queryClient.invalidateQueries({ queryKey: queryKeys.user('123') }); // Chỉ user 123
```

### **2️⃣ Custom Hooks Pattern**

```typescript
// =====================================
// CUSTOM HOOKS PATTERN - Reusable query logic
// =====================================

// ✅ hooks/useUsers.ts
export function useUsers(filters?: UserFilters) {
  return useQuery({
    queryKey: queryKeys.userList(filters ?? {}),
    queryFn: () => fetchUsers(filters),
    staleTime: 5 * 60 * 1000,
  });
}

export function useUser(userId: string) {
  return useQuery({
    queryKey: queryKeys.user(userId),
    queryFn: () => fetchUser(userId),
    enabled: !!userId,
    staleTime: 10 * 60 * 1000,
  });
}

export function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: createUser,
    onSuccess: (newUser) => {
      // Update cache
      queryClient.setQueryData(queryKeys.user(newUser.id), newUser);

      // Invalidate list
      queryClient.invalidateQueries({ queryKey: queryKeys.users });

      toast.success('User created');
    },
    onError: (error) => {
      toast.error(error.message);
    },
  });
}

export function useUpdateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({ id, data }: { id: string; data: Partial<User> }) =>
      updateUser(id, data),

    onMutate: async ({ id, data }) => {
      // Optimistic update
      await queryClient.cancelQueries({ queryKey: queryKeys.user(id) });

      const previousUser = queryClient.getQueryData(queryKeys.user(id));

      queryClient.setQueryData(queryKeys.user(id), (old: User) => ({
        ...old,
        ...data,
      }));

      return { previousUser };
    },

    onError: (err, { id }, context) => {
      // Rollback
      if (context?.previousUser) {
        queryClient.setQueryData(queryKeys.user(id), context.previousUser);
      }
      toast.error('Update failed');
    },

    onSettled: (data, error, { id }) => {
      queryClient.invalidateQueries({ queryKey: queryKeys.user(id) });
    },
  });
}

// ✅ Usage in components
function UserProfile({ userId }: { userId: string }) {
  const { data: user, isLoading } = useUser(userId);
  const updateUser = useUpdateUser();

  const handleUpdate = (data: Partial<User>) => {
    updateUser.mutate({ id: userId, data });
  };

  if (isLoading) return <Spinner />;

  return <UserForm user={user} onSubmit={handleUpdate} />;
}
```

### **3️⃣ API Service Layer Pattern**

```typescript
// =====================================
// API SERVICE LAYER - Tổ chức API calls
// =====================================

// ✅ services/userService.ts
import { api } from './api'; // Axios instance

export const userService = {
  // GET /api/users
  getUsers: async (filters?: UserFilters): Promise<User[]> => {
    const { data } = await api.get('/users', { params: filters });
    return data;
  },

  // GET /api/users/:id
  getUser: async (id: string): Promise<User> => {
    const { data } = await api.get(`/users/${id}`);
    return data;
  },

  // POST /api/users
  createUser: async (user: CreateUserDTO): Promise<User> => {
    const { data } = await api.post('/users', user);
    return data;
  },

  // PUT /api/users/:id
  updateUser: async (id: string, updates: Partial<User>): Promise<User> => {
    const { data } = await api.put(`/users/${id}`, updates);
    return data;
  },

  // DELETE /api/users/:id
  deleteUser: async (id: string): Promise<void> => {
    await api.delete(`/users/${id}`);
  },
};

// ✅ hooks/useUsers.ts
import { userService } from '@/services/userService';
import { queryKeys } from '@/lib/queryKeys';

export function useUsers(filters?: UserFilters) {
  return useQuery({
    queryKey: queryKeys.userList(filters ?? {}),
    queryFn: () => userService.getUsers(filters),
  });
}

export function useCreateUser() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: userService.createUser,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.users });
    },
  });
}

// ✅ services/api.ts - Axios instance với interceptors
import axios from 'axios';

export const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
  timeout: 10000,
});

// Request interceptor: Add auth token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Response interceptor: Handle errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      // Redirect to login
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);
```

### **4️⃣ Error Handling Patterns**

```typescript
// =====================================
// ERROR HANDLING PATTERNS
// =====================================

// ✅ Type-safe error handling
class ApiError extends Error {
  constructor(message: string, public status: number, public code?: string) {
    super(message);
    this.name = 'ApiError';
  }
}

// ✅ Query with error handling
function UserProfile({ userId }: { userId: string }) {
  const { data, isLoading, isError, error } = useQuery({
    queryKey: queryKeys.user(userId),
    queryFn: async () => {
      const response = await fetch(`/api/users/${userId}`);

      if (!response.ok) {
        const errorData = await response.json();
        throw new ApiError(errorData.message, response.status, errorData.code);
      }

      return response.json();
    },
    retry: (failureCount, error) => {
      // Don't retry on 404
      if (error instanceof ApiError && error.status === 404) {
        return false;
      }
      return failureCount < 3;
    },
  });

  if (isLoading) return <Spinner />;

  if (isError) {
    if (error instanceof ApiError) {
      if (error.status === 404) {
        return <NotFound />;
      }
      if (error.status === 403) {
        return <Forbidden />;
      }
    }
    return <ErrorMessage error={error} />;
  }

  return <UserDetails user={data} />;
}

// ✅ Global error boundary
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
              <h1>Something went wrong</h1>
              <pre>{error.message}</pre>
              <button onClick={resetErrorBoundary}>Try again</button>
            </div>
          )}
        >
          <Router />
        </ErrorBoundary>
      )}
    </QueryErrorResetBoundary>
  );
}
```

### **5️⃣ Dependent Mutations (Sequential mutations)**

```typescript
// =====================================
// DEPENDENT MUTATIONS - Mutations tuần tự
// =====================================

function CreatePostWithImage() {
  const queryClient = useQueryClient();

  // 1️⃣ Upload image
  const uploadImageMutation = useMutation({
    mutationFn: async (file: File) => {
      const formData = new FormData();
      formData.append('image', file);

      const response = await fetch('/api/upload', {
        method: 'POST',
        body: formData,
      });

      return response.json(); // { url: 'https://...' }
    },
  });

  // 2️⃣ Create post (sau khi upload xong)
  const createPostMutation = useMutation({
    mutationFn: async (post: CreatePostDTO) => {
      const response = await fetch('/api/posts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(post),
      });
      return response.json();
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.posts });
    },
  });

  const handleSubmit = async (data: {
    title: string;
    content: string;
    image: File;
  }) => {
    try {
      // Step 1: Upload image
      const imageResult = await uploadImageMutation.mutateAsync(data.image);

      // Step 2: Create post với image URL
      await createPostMutation.mutateAsync({
        title: data.title,
        content: data.content,
        imageUrl: imageResult.url,
      });

      toast.success('Post created successfully');
    } catch (error) {
      toast.error('Failed to create post');
    }
  };

  return (
    <PostForm
      onSubmit={handleSubmit}
      isLoading={uploadImageMutation.isPending || createPostMutation.isPending}
    />
  );
}
```

### **6️⃣ Polling & Auto Refetch**

```typescript
// =====================================
// POLLING - Tự động refetch theo interval
// =====================================

// ✅ Polling với refetchInterval
function RealtimeStats() {
  const { data } = useQuery({
    queryKey: ['stats'],
    queryFn: fetchStats,

    // ✅ Refetch every 5 seconds
    refetchInterval: 5000,

    // ✅ Chỉ poll khi window focus
    refetchIntervalInBackground: false,
  });

  return <StatsDisplay stats={data} />;
}

// ✅ Conditional polling (chỉ poll khi cần)
function OrderTracking({ orderId }: { orderId: string }) {
  const { data: order } = useQuery({
    queryKey: ['order', orderId],
    queryFn: () => fetchOrder(orderId),

    // ✅ Chỉ poll khi order chưa completed
    refetchInterval: (query) => {
      const order = query.state.data;
      return order?.status === 'pending' ? 3000 : false;
    },
  });

  return <OrderStatus order={order} />;
}

// ✅ WebSocket + React Query (real-time updates)
function useLiveOrders() {
  const queryClient = useQueryClient();

  useEffect(() => {
    const ws = new WebSocket('wss://api.example.com/orders');

    ws.onmessage = (event) => {
      const order = JSON.parse(event.data);

      // Update cache khi nhận WebSocket message
      queryClient.setQueryData(['order', order.id], order);

      // Invalidate list
      queryClient.invalidateQueries({ queryKey: ['orders'] });
    };

    return () => ws.close();
  }, [queryClient]);

  return useQuery({
    queryKey: ['orders'],
    queryFn: fetchOrders,
    staleTime: Infinity, // Không auto refetch (rely on WebSocket)
  });
}
```

---

## **🔥 Advanced Patterns**

### **📌 1. Suspense Mode (React 18+)**

```typescript
// =====================================
// SUSPENSE MODE - React Suspense integration
// =====================================

import { Suspense } from 'react';
import { useSuspenseQuery } from '@tanstack/react-query';

// ✅ useSuspenseQuery: Throw promise khi loading → Suspense catch
function UserProfile({ userId }: { userId: string }) {
  // No isLoading check needed!
  const { data } = useSuspenseQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  // Data always exists here (never undefined)
  return (
    <div>
      <h1>{data.name}</h1>
      <p>{data.email}</p>
    </div>
  );
}

// ✅ Wrap với Suspense
function App() {
  return (
    <Suspense fallback={<Spinner />}>
      <UserProfile userId="123" />
    </Suspense>
  );
}

// ✅ Multiple suspense queries
function Dashboard() {
  const { data: users } = useSuspenseQuery({
    queryKey: ['users'],
    queryFn: fetchUsers,
  });

  const { data: posts } = useSuspenseQuery({
    queryKey: ['posts'],
    queryFn: fetchPosts,
  });

  // Both data always exist
  return (
    <div>
      <UserList users={users} />
      <PostList posts={posts} />
    </div>
  );
}

// ✅ Nested Suspense boundaries
function App() {
  return (
    <div>
      {/* Suspense cho navigation */}
      <Suspense fallback={<NavSkeleton />}>
        <Navigation />
      </Suspense>

      {/* Suspense cho main content */}
      <Suspense fallback={<ContentSkeleton />}>
        <Dashboard />
      </Suspense>
    </div>
  );
}
```

### **📌 2. Prefetching Strategies**

```typescript
// =====================================
// PREFETCHING STRATEGIES
// =====================================

// ✅ 1. Prefetch on hover
function UserCard({ userId }: { userId: string }) {
  const queryClient = useQueryClient();

  const handleMouseEnter = () => {
    // Prefetch user details khi hover
    queryClient.prefetchQuery({
      queryKey: ['user', userId],
      queryFn: () => fetchUser(userId),
    });
  };

  return (
    <div onMouseEnter={handleMouseEnter}>
      <Link to={`/users/${userId}`}>View Profile</Link>
    </div>
  );
}

// ✅ 2. Prefetch on route change
import { useRouter } from 'next/router';

function Navigation() {
  const queryClient = useQueryClient();
  const router = useRouter();

  const handleNavClick = (route: string) => {
    // Prefetch data trước khi navigate
    if (route === '/dashboard') {
      queryClient.prefetchQuery({
        queryKey: ['dashboard'],
        queryFn: fetchDashboardData,
      });
    }

    router.push(route);
  };

  return (
    <nav>
      <button onClick={() => handleNavClick('/dashboard')}>Dashboard</button>
    </nav>
  );
}

// ✅ 3. Prefetch in loader (Next.js App Router)
// app/users/[id]/page.tsx
export async function generateMetadata({ params }: { params: { id: string } }) {
  const queryClient = new QueryClient();

  // Prefetch ở server-side
  await queryClient.prefetchQuery({
    queryKey: ['user', params.id],
    queryFn: () => fetchUser(params.id),
  });

  const dehydratedState = dehydrate(queryClient);

  return dehydratedState;
}
```

### **📌 3. Optimistic Updates Patterns**

```typescript
// =====================================
// ADVANCED OPTIMISTIC UPDATES
// =====================================

// ✅ Multiple entities update
function useLikePost() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: likePost,

    onMutate: async (postId) => {
      await queryClient.cancelQueries({ queryKey: ['posts'] });

      // Update post like count
      queryClient.setQueryData(['post', postId], (old: Post) => ({
        ...old,
        likes: old.likes + 1,
        isLiked: true,
      }));

      // Update post in list
      queryClient.setQueryData(['posts'], (old: Post[]) =>
        old.map((post) =>
          post.id === postId
            ? { ...post, likes: post.likes + 1, isLiked: true }
            : post
        )
      );

      // Update user's liked posts
      queryClient.setQueryData(['user', 'liked-posts'], (old: string[]) => [
        ...old,
        postId,
      ]);

      return {
        /* context for rollback */
      };
    },

    onError: (err, postId, context) => {
      // Rollback all updates
      // ...
    },
  });
}

// ✅ Optimistic delete from list
function useDeletePost() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: deletePost,

    onMutate: async (postId) => {
      await queryClient.cancelQueries({ queryKey: ['posts'] });

      const previousPosts = queryClient.getQueryData(['posts']);

      // Remove post from all queries
      queryClient.setQueriesData({ queryKey: ['posts'] }, (old: Post[]) =>
        old.filter((post) => post.id !== postId)
      );

      return { previousPosts };
    },

    onError: (err, postId, context) => {
      queryClient.setQueryData(['posts'], context?.previousPosts);
    },

    onSuccess: (data, postId) => {
      // Remove individual post cache
      queryClient.removeQueries({ queryKey: ['post', postId] });
    },
  });
}
```

---

## **🎯 React Query vs Redux/Zustand**

```typescript
/*
┌─────────────────────────────────────────────────────────────────┐
│  React Query              vs     Redux/Zustand                   │
├─────────────────────────────────────────────────────────────────┤
│  SERVER STATE                   CLIENT STATE                     │
│  (Async, từ API)                (Sync, trong app)                │
├─────────────────────────────────────────────────────────────────┤
│  ✅ Caching                      ✅ UI state                      │
│  ✅ Background refetch           ✅ Form state                    │
│  ✅ Deduplication                ✅ Modal open/close              │
│  ✅ Pagination                   ✅ Theme                         │
│  ✅ Infinite scroll              ✅ Language                      │
│  ✅ Optimistic updates           ✅ Selected items                │
│  ✅ Retry                        ✅ Filters                       │
├─────────────────────────────────────────────────────────────────┤
│  Use React Query for:           Use Redux/Zustand for:          │
│  - API data                     - Global UI state                │
│  - Database queries             - User preferences               │
│  - External data                - App configuration              │
│  - Server state                 - Client-only state              │
└─────────────────────────────────────────────────────────────────┘
*/

// ✅ BEST PRACTICE: Combine both
// React Query: Server state
// Zustand: Client state

// Zustand store
import { create } from 'zustand';

interface AppStore {
  theme: 'light' | 'dark';
  sidebarOpen: boolean;
  setTheme: (theme: 'light' | 'dark') => void;
  toggleSidebar: () => void;
}

export const useAppStore = create<AppStore>((set) => ({
  theme: 'light',
  sidebarOpen: true,
  setTheme: (theme) => set({ theme }),
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
}));

// Component
function App() {
  // ✅ Client state từ Zustand
  const { theme, setTheme } = useAppStore();

  // ✅ Server state từ React Query
  const { data: users } = useUsers();

  return (
    <div data-theme={theme}>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme
      </button>
      <UserList users={users} />
    </div>
  );
}
```

---

## **📊 React Query DevTools**

```typescript
// =====================================
// REACT QUERY DEVTOOLS
// =====================================

import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router />

      {/* ✅ Add DevTools (chỉ hiện ở development) */}
      <ReactQueryDevtools
        initialIsOpen={false} // Đóng mặc định
        position="bottom-right" // Vị trí
        buttonPosition="bottom-right" // Vị trí button
      />
    </QueryClientProvider>
  );
}

// 🔍 DevTools features:
/*
1. ✅ Query Explorer
   - Xem tất cả queries
   - Query status (success, error, loading)
   - Data preview
   - Query key
   - Stale time, cache time

2. ✅ Query Inspector
   - Xem chi tiết 1 query
   - Data, error, status
   - Observers (components đang dùng)
   - Actions (refetch, invalidate, remove)

3. ✅ Mutations
   - Xem tất cả mutations
   - Status, variables, error

4. ✅ Query Timeline
   - Theo dõi queries theo thời gian
   - Fetch, refetch events

5. ✅ Cache Explorer
   - Xem cache size
   - GC events
*/
```

---

## **✅ REACT QUERY BEST PRACTICES - TỔNG KẾT**

### **🎯 1. Query Keys**

```typescript
✅ DO:
- Centralize query keys: const queryKeys = { users: ['users'], ... }
- Use array format: ['users', userId, filters]
- Include dependencies in key: ['posts', { status: 'active' }]
- Use factory functions: queryKeys.user(id)

❌ DON'T:
- Hardcode keys: queryKey: ['users']
- Forget dependencies: queryKey: ['posts'] (missing filters)
- Use objects directly: queryKey: [{ id: '123' }] (order matters!)
```

### **🎯 2. Query Functions**

```typescript
✅ DO:
- Return Promise: queryFn: () => fetch().then(res => res.json())
- Throw errors: throw new Error('Failed')
- Use async/await: queryFn: async () => { ... }
- Type return data: queryFn: (): Promise<User[]> => ...

❌ DON'T:
- Return non-Promise: queryFn: () => data
- Swallow errors: .catch(() => null)
- Use callbacks: queryFn: (callback) => fetch().then(callback)
```

### **🎯 3. Stale Time & GC Time**

```typescript
✅ DO:
- Set appropriate staleTime: 5 * 60 * 1000 (5 phút)
- Static data → high staleTime: Infinity
- Real-time data → low staleTime: 0
- gcTime > staleTime (usually 2x)

❌ DON'T:
- staleTime = 0 everywhere (too many requests)
- staleTime = Infinity everywhere (stale data)
- gcTime < staleTime (premature cleanup)
```

### **🎯 4. Mutations**

```typescript
✅ DO:
- Use optimistic updates for better UX
- Invalidate queries after mutation
- Handle errors properly (rollback)
- Show loading state: mutation.isPending
- Use onMutate, onSuccess, onError, onSettled

❌ DON'T:
- Forget to invalidate queries
- No error handling
- No rollback on error
- Block UI without loading indicator
```

### **🎯 5. Code Organization**

```typescript
✅ DO:
- Custom hooks: useUsers(), useCreateUser()
- API service layer: userService.getUsers()
- Centralized query keys: queryKeys.user(id)
- Type safety: Define types for data

❌ DON'T:
- Inline queries everywhere
- Duplicate query logic
- Hardcode API URLs
- Any types
```

### **🎯 6. Performance**

```typescript
✅ DO:
- Use placeholderData for pagination
- Prefetch next page
- Use suspense for better UX
- Selective refetch: refetchOnWindowFocus: false for expensive queries

❌ DON'T:
- Fetch same data multiple times
- No caching strategy
- Refetch on every render
- No pagination/infinite scroll
```

### **🎯 7. Error Handling**

```typescript
✅ DO:
- Custom error classes: class ApiError extends Error
- Retry with strategy: retry: (failureCount, error) => ...
- Error boundaries: <QueryErrorResetBoundary>
- User-friendly messages

❌ DON'T:
- Silent errors: .catch(() => {})
- Generic error messages: "Error occurred"
- No retry logic
- No fallback UI
```

---

## **📚 Tài Liệu Tham Khảo**

- **Official Docs**: https://tanstack.com/query/latest
- **GitHub**: https://github.com/TanStack/query
- **Discord**: https://discord.com/invite/WrRKjPJ
- **Examples**: https://tanstack.com/query/latest/docs/react/examples/react/simple

---

## **🎓 KẾT LUẬN**

**React Query là thư viện BẮT BUỘC phải biết cho mọi React developer.**

**✅ Key Takeaways:**

1. **React Query = Server State Manager** (không phải client state)
2. **Auto caching + background refetch** → tối ưu performance
3. **Optimistic updates** → UX tốt hơn
4. **Built-in pagination, infinite scroll** → dễ implement
5. **DevTools** → debug dễ dàng

**🚀 Khi nào dùng React Query?**

- ✅ Fetch data từ API
- ✅ CRUD operations
- ✅ Pagination, infinite scroll
- ✅ Real-time updates
- ✅ Optimistic UI

**🎯 Best Practice:**

- Custom hooks cho reusability
- Centralized query keys
- API service layer
- Type safety với TypeScript
- Error handling đầy đủ

**💡 Remember:**

> "React Query makes server state management effortless."
>
> "Don't manage server state in Redux/Zustand. Use React Query."

---

## 🔬 REACT QUERY DEEP DIVE - Advanced Topics

### **📌 1. Query Cancellation & AbortController**

```typescript
// =====================================
// QUERY CANCELLATION - Hủy requests khi component unmount
// =====================================

// ✅ Automatic cancellation với AbortController
function SearchResults({ query }: { query: string }) {
  const { data, isLoading } = useQuery({
    queryKey: ['search', query],
    queryFn: async ({ signal }) => {
      // ✅ React Query tự động pass AbortSignal vào queryFn
      const response = await fetch(`/api/search?q=${query}`, {
        signal, // ✅ Pass signal vào fetch
      });

      if (!response.ok) throw new Error('Search failed');
      return response.json();
    },
    enabled: query.length > 0,
  });

  // 🎯 KHI COMPONENT UNMOUNT hoặc query key thay đổi:
  // → React Query tự động gọi signal.abort()
  // → Fetch request bị cancel
  // → Tránh memory leak và race conditions

  return <ResultsList results={data} />;
}

// ===================================================
// MANUAL CANCELLATION với queryClient
// ===================================================

function SearchPage() {
  const queryClient = useQueryClient();
  const [query, setQuery] = useState('');

  const handleClearSearch = async () => {
    // ✅ Cancel tất cả search queries đang chạy
    await queryClient.cancelQueries({ queryKey: ['search'] });

    // Clear query
    setQuery('');
  };

  return (
    <div>
      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="Search..."
      />
      <button onClick={handleClearSearch}>Clear & Cancel</button>

      <SearchResults query={query} />
    </div>
  );
}

// ===================================================
// AXIOS với CANCELLATION
// ===================================================

import axios from 'axios';

function useSearchWithAxios(query: string) {
  return useQuery({
    queryKey: ['search', query],
    queryFn: async ({ signal }) => {
      // ✅ Convert AbortSignal to Axios CancelToken
      const source = axios.CancelToken.source();

      // Link signal to Axios cancel
      signal?.addEventListener('abort', () => {
        source.cancel('Query was cancelled by React Query');
      });

      const { data } = await axios.get('/api/search', {
        params: { q: query },
        cancelToken: source.token,
      });

      return data;
    },
    enabled: !!query,
  });
}

// ===================================================
// CLEANUP PATTERN cho non-fetch APIs
// ===================================================

function useWebSocketData(channel: string) {
  return useQuery({
    queryKey: ['websocket', channel],
    queryFn: ({ signal }) => {
      return new Promise((resolve, reject) => {
        const ws = new WebSocket(`wss://api.example.com/${channel}`);

        // ✅ Handle abort signal
        signal?.addEventListener('abort', () => {
          ws.close();
          reject(new Error('WebSocket cancelled'));
        });

        ws.onmessage = (event) => {
          resolve(JSON.parse(event.data));
          ws.close();
        };

        ws.onerror = (error) => {
          reject(error);
          ws.close();
        };
      });
    },
    staleTime: Infinity,
  });
}
```

---

### **📌 2. Request Deduplication (Ngăn duplicate requests)**

```typescript
// =====================================
// REQUEST DEDUPLICATION
// =====================================

// 🎯 PROBLEM: Multiple components cùng fetch 1 data
function UserProfile({ userId }: { userId: string }) {
  const { data } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });
  return <div>{data?.name}</div>;
}

function UserAvatar({ userId }: { userId: string }) {
  const { data } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });
  return <img src={data?.avatar} />;
}

function UserBadge({ userId }: { userId: string }) {
  const { data } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });
  return <span>{data?.role}</span>;
}

// ✅ SOLUTION: React Query tự động deduplicate!
function App() {
  return (
    <div>
      {/* 3 components cùng query ['user', '123'] */}
      <UserProfile userId="123" />
      <UserAvatar userId="123" />
      <UserBadge userId="123" />

      {/* ✅ CHỈ 1 REQUEST được gửi!
          ✅ 3 components share cùng 1 cache
          ✅ Tất cả đều update khi data thay đổi
      */}
    </div>
  );
}

// ===================================================
// DEDUPLICATION với DIFFERENT COMPONENTS trong routing
// ===================================================

// Route: /users/123
function UserPage({ userId }: { userId: string }) {
  const { data: user } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  const { data: posts } = useQuery({
    queryKey: ['posts', userId],
    queryFn: () => fetchUserPosts(userId),
  });

  return (
    <div>
      <UserHeader user={user} />
      <UserSidebar user={user} /> {/* ✅ Reuse cache, no request */}
      <PostList posts={posts} />
    </div>
  );
}

// ===================================================
// FORCE SEPARATE REQUESTS (khi cần)
// ===================================================

function Dashboard() {
  // ✅ Thêm unique identifier vào query key
  const { data: stats1 } = useQuery({
    queryKey: ['stats', 'widget-1', Date.now()], // ✅ Unique key
    queryFn: fetchStats,
  });

  const { data: stats2 } = useQuery({
    queryKey: ['stats', 'widget-2', Date.now()], // ✅ Unique key
    queryFn: fetchStats,
  });

  // ❌ 2 requests riêng biệt (không deduplicate)
}
```

---

### **📌 3. Parallel Queries Optimization**

```typescript
// =====================================
// PARALLEL QUERIES OPTIMIZATION
// =====================================

// ✅ PATTERN 1: useQueries với dynamic array
function MultiUserDashboard({ userIds }: { userIds: string[] }) {
  const userQueries = useQueries({
    queries: userIds.map((id) => ({
      queryKey: ['user', id],
      queryFn: () => fetchUser(id),
      staleTime: 5 * 60 * 1000,
    })),
  });

  // ✅ Access loading state
  const isLoading = userQueries.some((q) => q.isLoading);
  const isError = userQueries.some((q) => q.isError);

  // ✅ Get all successful data
  const users = userQueries
    .map((q) => q.data)
    .filter((data): data is User => data !== undefined);

  if (isLoading) return <Spinner />;

  return (
    <div>
      {users.map((user) => (
        <UserCard key={user.id} user={user} />
      ))}
    </div>
  );
}

// ===================================================
// PATTERN 2: useQueries với combine (advanced)
// ===================================================

function CombinedDashboard() {
  const result = useQueries({
    queries: [
      {
        queryKey: ['users'],
        queryFn: fetchUsers,
        staleTime: 5 * 60 * 1000,
      },
      {
        queryKey: ['posts'],
        queryFn: fetchPosts,
        staleTime: 5 * 60 * 1000,
      },
      {
        queryKey: ['comments'],
        queryFn: fetchComments,
        staleTime: 5 * 60 * 1000,
      },
    ],
    // ✅ combine: Transform results
    combine: (results) => {
      return {
        data: {
          users: results[0].data ?? [],
          posts: results[1].data ?? [],
          comments: results[2].data ?? [],
        },
        isLoading: results.some((r) => r.isLoading),
        isError: results.some((r) => r.isError),
        errors: results.map((r) => r.error).filter(Boolean),
      };
    },
  });

  if (result.isLoading) return <Spinner />;
  if (result.isError) return <ErrorDisplay errors={result.errors} />;

  return (
    <div>
      <UserSection users={result.data.users} />
      <PostSection posts={result.data.posts} />
      <CommentSection comments={result.data.comments} />
    </div>
  );
}

// ===================================================
// PATTERN 3: Promise.all với ensureQueryData (manual)
// ===================================================

function usePrefetchDashboard() {
  const queryClient = useQueryClient();

  const prefetchAll = async () => {
    // ✅ Parallel prefetch với Promise.all
    await Promise.all([
      queryClient.ensureQueryData({
        queryKey: ['users'],
        queryFn: fetchUsers,
      }),
      queryClient.ensureQueryData({
        queryKey: ['posts'],
        queryFn: fetchPosts,
      }),
      queryClient.ensureQueryData({
        queryKey: ['comments'],
        queryFn: fetchComments,
      }),
    ]);
  };

  return { prefetchAll };
}

// Usage
function App() {
  const { prefetchAll } = usePrefetchDashboard();

  useEffect(() => {
    prefetchAll(); // Prefetch tất cả khi app mount
  }, []);

  return <Dashboard />;
}
```

---

### **📌 4. Custom QueryClient Configuration**

```typescript
// =====================================
// CUSTOM QUERYCLIENT - Advanced config
// =====================================

import { QueryClient, QueryCache, MutationCache } from '@tanstack/react-query';

// ✅ QueryCache: Global cache với event listeners
const queryCache = new QueryCache({
  // ✅ onError: Handle tất cả query errors globally
  onError: (error, query) => {
    console.error('Query error:', {
      error,
      queryKey: query.queryKey,
      queryHash: query.queryHash,
    });

    // ✅ Send to error tracking service
    if (error instanceof ApiError && error.status >= 500) {
      Sentry.captureException(error, {
        tags: {
          queryKey: JSON.stringify(query.queryKey),
        },
      });
    }

    // ✅ Show toast for specific errors
    if (error instanceof ApiError && error.status === 401) {
      toast.error('Session expired. Please login again.');
      window.location.href = '/login';
    }
  },

  // ✅ onSuccess: Global success handler
  onSuccess: (data, query) => {
    console.log('Query success:', query.queryKey);

    // ✅ Analytics tracking
    trackEvent('query_success', {
      queryKey: query.queryKey,
      dataSize: JSON.stringify(data).length,
    });
  },

  // ✅ onSettled: Chạy sau mỗi query (success/error)
  onSettled: (data, error, query) => {
    console.log('Query settled:', {
      queryKey: query.queryKey,
      success: !error,
    });
  },
});

// ✅ MutationCache: Global mutation cache
const mutationCache = new MutationCache({
  onError: (error, variables, context, mutation) => {
    console.error('Mutation error:', {
      error,
      mutationKey: mutation.options.mutationKey,
      variables,
    });

    // ✅ Auto rollback on error
    if (context?.previousData) {
      queryClient.setQueryData(
        mutation.options.mutationKey!,
        context.previousData
      );
    }

    // ✅ Show error toast
    toast.error(error.message || 'Mutation failed');
  },

  onSuccess: (data, variables, context, mutation) => {
    console.log('Mutation success:', mutation.options.mutationKey);

    // ✅ Success notification
    toast.success('Changes saved successfully');
  },
});

// ✅ QueryClient với custom caches
export const queryClient = new QueryClient({
  queryCache,
  mutationCache,

  defaultOptions: {
    queries: {
      // ✅ Retry strategy
      retry: (failureCount, error) => {
        // Don't retry on 4xx errors
        if (error instanceof ApiError && error.status < 500) {
          return false;
        }
        return failureCount < 3;
      },

      // ✅ Retry delay với exponential backoff
      retryDelay: (attemptIndex) => {
        return Math.min(1000 * 2 ** attemptIndex, 30000);
      },

      // ✅ Network mode
      networkMode: 'online', // 'online' | 'always' | 'offlineFirst'

      // ✅ Meta data (custom data for queries)
      meta: {
        errorMessage: 'Failed to fetch data',
      },
    },

    mutations: {
      // ✅ Mutation network mode
      networkMode: 'online',

      // ✅ Mutation retry
      retry: 0, // Don't retry mutations by default

      // ✅ Meta data
      meta: {
        errorMessage: 'Failed to save changes',
      },
    },
  },
});

// ===================================================
// CUSTOM LOGGER
// ===================================================

class QueryLogger {
  private logs: Array<{
    type: 'query' | 'mutation';
    action: 'start' | 'success' | 'error';
    key: unknown[];
    timestamp: number;
  }> = [];

  log(type: 'query' | 'mutation', action: string, key: unknown[]) {
    const entry = {
      type,
      action,
      key,
      timestamp: Date.now(),
    };

    this.logs.push(entry);

    // Keep only last 100 logs
    if (this.logs.length > 100) {
      this.logs.shift();
    }

    console.log(`[${type.toUpperCase()}] ${action}:`, key);
  }

  getLogs() {
    return this.logs;
  }

  clear() {
    this.logs = [];
  }
}

export const queryLogger = new QueryLogger();

// ✅ Use logger trong queries
function useUserWithLogging(userId: string) {
  return useQuery({
    queryKey: ['user', userId],
    queryFn: async () => {
      queryLogger.log('query', 'start', ['user', userId]);

      try {
        const data = await fetchUser(userId);
        queryLogger.log('query', 'success', ['user', userId]);
        return data;
      } catch (error) {
        queryLogger.log('query', 'error', ['user', userId]);
        throw error;
      }
    },
  });
}
```

---

### **📌 5. Persistence (Persist cache to localStorage)**

```typescript
// =====================================
// PERSISTENCE - Lưu cache vào localStorage
// =====================================

import { persistQueryClient } from '@tanstack/react-query-persist-client';
import { createSyncStoragePersister } from '@tanstack/query-sync-storage-persister';

// ✅ Create persister
const persister = createSyncStoragePersister({
  storage: window.localStorage,
  key: 'REACT_QUERY_CACHE', // LocalStorage key
  serialize: JSON.stringify,
  deserialize: JSON.parse,
});

// ✅ Persist query client
persistQueryClient({
  queryClient,
  persister,
  maxAge: 1000 * 60 * 60 * 24, // 24 hours
  buster: 'v1.0.0', // Cache version (change to invalidate all cache)
  dehydrateOptions: {
    // ✅ Chọn queries nào được persist
    shouldDehydrateQuery: (query) => {
      // Chỉ persist queries có staleTime > 0
      return query.state.status === 'success' && query.state.data !== undefined;
    },
  },
});

// ===================================================
// SELECTIVE PERSISTENCE (chỉ persist 1 số queries)
// ===================================================

import { PersistQueryClientProvider } from '@tanstack/react-query-persist-client';

function App() {
  return (
    <PersistQueryClientProvider
      client={queryClient}
      persistOptions={{
        persister,
        maxAge: 1000 * 60 * 60 * 24,
        dehydrateOptions: {
          shouldDehydrateQuery: (query) => {
            // ✅ Chỉ persist user data, không persist posts
            const queryKey = query.queryKey;
            return queryKey[0] === 'user' && query.state.status === 'success';
          },
        },
      }}
    >
      <Router />
    </PersistQueryClientProvider>
  );
}

// ===================================================
// CUSTOM PERSISTER (IndexedDB)
// ===================================================

import { createAsyncStoragePersister } from '@tanstack/query-async-storage-persister';

const asyncPersister = createAsyncStoragePersister({
  storage: {
    getItem: async (key) => {
      // ✅ Get from IndexedDB
      const db = await openDB('react-query-cache', 1);
      return db.get('cache', key);
    },
    setItem: async (key, value) => {
      // ✅ Set to IndexedDB
      const db = await openDB('react-query-cache', 1);
      await db.put('cache', value, key);
    },
    removeItem: async (key) => {
      const db = await openDB('react-query-cache', 1);
      await db.delete('cache', key);
    },
  },
});

// ===================================================
// CLEAR PERSISTED CACHE
// ===================================================

function useClearCache() {
  const queryClient = useQueryClient();

  const clearCache = async () => {
    // ✅ Clear in-memory cache
    queryClient.clear();

    // ✅ Clear persisted cache
    await persister.removeClient();

    // ✅ Clear localStorage
    localStorage.removeItem('REACT_QUERY_CACHE');

    console.log('Cache cleared');
  };

  return { clearCache };
}
```

---

### **📌 6. SSR/SSG with React Query (Next.js)**

```typescript
// =====================================
// SSR/SSG PATTERNS
// =====================================

// ✅ PATTERN 1: Server-side rendering (getServerSideProps)
// pages/users/[id].tsx
import {
  dehydrate,
  QueryClient,
  useQuery,
  HydrationBoundary,
} from '@tanstack/react-query';
import type { GetServerSideProps } from 'next';

export const getServerSideProps: GetServerSideProps = async ({ params }) => {
  const queryClient = new QueryClient();

  // ✅ Prefetch data on server
  await queryClient.prefetchQuery({
    queryKey: ['user', params?.id],
    queryFn: () => fetchUser(params?.id as string),
  });

  return {
    props: {
      // ✅ Dehydrate cache để serialize
      dehydratedState: dehydrate(queryClient),
    },
  };
};

// ✅ Component
export default function UserPage({ dehydratedState }: any) {
  return (
    <HydrationBoundary state={dehydratedState}>
      <UserProfile />
    </HydrationBoundary>
  );
}

function UserProfile() {
  const router = useRouter();
  const { data } = useQuery({
    queryKey: ['user', router.query.id],
    queryFn: () => fetchUser(router.query.id as string),
    // ✅ Data đã có từ SSR, chỉ refetch khi stale
    staleTime: 5 * 60 * 1000,
  });

  return <div>{data?.name}</div>;
}

// ===================================================
// PATTERN 2: Static Site Generation (getStaticProps)
// ===================================================

export const getStaticProps: GetStaticProps = async ({ params }) => {
  const queryClient = new QueryClient();

  await queryClient.prefetchQuery({
    queryKey: ['user', params?.id],
    queryFn: () => fetchUser(params?.id as string),
  });

  return {
    props: {
      dehydratedState: dehydrate(queryClient),
    },
    revalidate: 60, // ✅ ISR: Revalidate every 60 seconds
  };
};

// ✅ getStaticPaths
export const getStaticPaths: GetStaticPaths = async () => {
  const users = await fetchUsers();

  return {
    paths: users.map((user) => ({ params: { id: user.id } })),
    fallback: 'blocking', // ✅ SSR for non-prerendered paths
  };
};

// ===================================================
// PATTERN 3: Next.js App Router (Server Components)
// ===================================================

// app/users/[id]/page.tsx
import { QueryClient, HydrationBoundary, dehydrate } from '@tanstack/react-query';

export default async function UserPage({ params }: { params: { id: string } }) {
  const queryClient = new QueryClient();

  // ✅ Prefetch trong Server Component
  await queryClient.prefetchQuery({
    queryKey: ['user', params.id],
    queryFn: () => fetchUser(params.id),
  });

  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <UserProfile userId={params.id} />
    </HydrationBoundary>
  );
}

// ✅ Client Component
'use client';
function UserProfile({ userId }: { userId: string }) {
  const { data } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  return <div>{data?.name}</div>;
}
```

---

### **📌 7. Advanced Caching Strategies**

```typescript
// =====================================
// ADVANCED CACHING STRATEGIES
// =====================================

// ✅ STRATEGY 1: Cache-first, then revalidate
function useCacheFirst<T>(key: string[], fetcher: () => Promise<T>) {
  return useQuery({
    queryKey: key,
    queryFn: fetcher,
    staleTime: Infinity, // ✅ Never mark as stale
    gcTime: 1000 * 60 * 60 * 24, // ✅ Keep in cache for 24 hours

    // ✅ Manual revalidation only
    refetchOnWindowFocus: false,
    refetchOnMount: false,
    refetchOnReconnect: false,
  });
}

// Usage
const { data, refetch } = useCacheFirst(['static-data'], fetchStaticData);

// Manual refresh button
<button onClick={() => refetch()}>Refresh</button>;

// ===================================================
// STRATEGY 2: Stale-while-revalidate (SWR pattern)
// ===================================================

function useStaleWhileRevalidate<T>(key: string[], fetcher: () => Promise<T>) {
  return useQuery({
    queryKey: key,
    queryFn: fetcher,
    staleTime: 0, // ✅ Always stale → always revalidate
    gcTime: 1000 * 60 * 5, // ✅ Keep cache 5 minutes

    // ✅ Show cache immediately, refetch in background
    refetchOnMount: true,
    refetchOnWindowFocus: true,
    refetchOnReconnect: true,

    // ✅ Use cached data while refetching
    placeholderData: (previousData) => previousData,
  });
}

// ===================================================
// STRATEGY 3: Time-based invalidation
// ===================================================

function useTimedCache<T>(
  key: string[],
  fetcher: () => Promise<T>,
  ttl: number // Time to live in ms
) {
  const queryClient = useQueryClient();

  // ✅ Auto invalidate after TTL
  useEffect(() => {
    const timer = setTimeout(() => {
      queryClient.invalidateQueries({ queryKey: key });
    }, ttl);

    return () => clearTimeout(timer);
  }, [key, ttl, queryClient]);

  return useQuery({
    queryKey: key,
    queryFn: fetcher,
    staleTime: ttl,
    gcTime: ttl * 2,
  });
}

// Usage
const { data } = useTimedCache(['live-prices'], fetchPrices, 10000); // Invalidate every 10s

// ===================================================
// STRATEGY 4: Conditional caching
// ===================================================

function useConditionalCache<T>(
  key: string[],
  fetcher: () => Promise<T>,
  shouldCache: boolean
) {
  return useQuery({
    queryKey: key,
    queryFn: fetcher,
    staleTime: shouldCache ? 5 * 60 * 1000 : 0,
    gcTime: shouldCache ? 10 * 60 * 1000 : 0,
    enabled: true,
  });
}

// Usage
const isPremiumUser = useIsPremium();
const { data } = useConditionalCache(
  ['premium-data'],
  fetchPremiumData,
  isPremiumUser // ✅ Chỉ cache nếu là premium user
);

// ===================================================
// STRATEGY 5: Multi-level cache (Memory + LocalStorage)
// ===================================================

function useMultiLevelCache<T>(key: string[], fetcher: () => Promise<T>) {
  const queryClient = useQueryClient();

  return useQuery({
    queryKey: key,
    queryFn: async () => {
      // ✅ Level 1: Check localStorage first
      const cached = localStorage.getItem(JSON.stringify(key));
      if (cached) {
        const { data, timestamp } = JSON.parse(cached);
        const age = Date.now() - timestamp;

        // ✅ Use localStorage cache if < 1 hour old
        if (age < 1000 * 60 * 60) {
          return data;
        }
      }

      // ✅ Level 2: Fetch from server
      const freshData = await fetcher();

      // ✅ Save to localStorage
      localStorage.setItem(
        JSON.stringify(key),
        JSON.stringify({ data: freshData, timestamp: Date.now() })
      );

      return freshData;
    },
    staleTime: 5 * 60 * 1000,
  });
}
```

---

### **📌 8. Query Filters & Batch Operations**

```typescript
// =====================================
// QUERY FILTERS - Advanced filtering
// =====================================

import { QueryFilters } from '@tanstack/react-query';

function useBatchOperations() {
  const queryClient = useQueryClient();

  // ✅ Invalidate multiple queries với filter
  const invalidateByType = (type: string) => {
    queryClient.invalidateQueries({
      predicate: (query) => {
        const [firstKey] = query.queryKey;
        return firstKey === type;
      },
    });
  };

  // ✅ Invalidate queries có specific property
  const invalidateStale = () => {
    queryClient.invalidateQueries({
      predicate: (query) => {
        const age = Date.now() - (query.state.dataUpdatedAt || 0);
        return age > 5 * 60 * 1000; // Older than 5 minutes
      },
    });
  };

  // ✅ Remove queries matching pattern
  const removeByPattern = (pattern: string) => {
    queryClient.removeQueries({
      predicate: (query) => {
        return query.queryKey.some((key) => String(key).includes(pattern));
      },
    });
  };

  // ✅ Cancel all queries của specific type
  const cancelByType = async (type: string) => {
    await queryClient.cancelQueries({
      predicate: (query) => query.queryKey[0] === type,
    });
  };

  // ✅ Get all queries matching filter
  const getQueriesByType = (type: string) => {
    return queryClient
      .getQueryCache()
      .findAll({ predicate: (query) => query.queryKey[0] === type });
  };

  return {
    invalidateByType,
    invalidateStale,
    removeByPattern,
    cancelByType,
    getQueriesByType,
  };
}

// ===================================================
// BATCH UPDATES
// ===================================================

function useBatchUpdate() {
  const queryClient = useQueryClient();

  const batchUpdateUsers = (updates: Array<{ id: string; data: Partial<User> }>) => {
    // ✅ Batch update multiple queries
    queryClient.setQueriesData<User[]>({ queryKey: ['users'] }, (old) => {
      if (!old) return old;

      return old.map((user) => {
        const update = updates.find((u) => u.id === user.id);
        return update ? { ...user, ...update.data } : user;
      });
    });

    // ✅ Update individual user queries
    updates.forEach(({ id, data }) => {
      queryClient.setQueryData<User>(['user', id], (old) =>
        old ? { ...old, ...data } : old
      );
    });
  };

  return { batchUpdateUsers };
}

// Usage
const { batchUpdateUsers } = useBatchUpdate();

batchUpdateUsers([
  { id: '1', data: { name: 'Updated User 1' } },
  { id: '2', data: { name: 'Updated User 2' } },
  { id: '3', data: { name: 'Updated User 3' } },
]);
```

---

### **📌 9. Query Dependencies & Waterfalls Prevention**

```typescript
// =====================================
// PREVENT QUERY WATERFALLS
// =====================================

// ❌ BAD: Sequential queries (waterfall)
function BadUserPosts({ userId }: { userId: string }) {
  const { data: user } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  // ⚠️ Chờ user load xong mới fetch posts
  const { data: posts } = useQuery({
    queryKey: ['posts', user?.id],
    queryFn: () => fetchUserPosts(user!.id),
    enabled: !!user,
  });

  // ⚠️ Chờ posts load xong mới fetch comments
  const { data: comments } = useQuery({
    queryKey: ['comments', posts?.[0]?.id],
    queryFn: () => fetchComments(posts![0].id),
    enabled: !!posts && posts.length > 0,
  });

  // 🐌 Timeline: user (1s) → posts (1s) → comments (1s) = 3 giây!
}

// ✅ GOOD: Parallel queries khi có thể
function GoodUserPosts({ userId }: { userId: string }) {
  // ✅ Fetch user & posts song song (nếu userId đủ để fetch posts)
  const { data: user } = useQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });

  const { data: posts } = useQuery({
    queryKey: ['posts', userId], // ✅ Dùng userId, không chờ user
    queryFn: () => fetchUserPosts(userId),
  });

  // ✅ Fetch comments của tất cả posts cùng lúc
  const commentQueries = useQueries({
    queries:
      posts?.map((post) => ({
        queryKey: ['comments', post.id],
        queryFn: () => fetchComments(post.id),
      })) ?? [],
  });

  // ⚡ Timeline: user + posts (1s) → all comments parallel (1s) = 2 giây!
}

// ===================================================
// DEPENDENCY RESOLUTION STRATEGY
// ===================================================

function useUserData(userId: string) {
  // ✅ Fetch tất cả dependencies song song nếu có đủ info
  const results = useQueries({
    queries: [
      {
        queryKey: ['user', userId],
        queryFn: () => fetchUser(userId),
      },
      {
        queryKey: ['user-stats', userId],
        queryFn: () => fetchUserStats(userId),
      },
      {
        queryKey: ['user-posts', userId],
        queryFn: () => fetchUserPosts(userId),
      },
      {
        queryKey: ['user-followers', userId],
        queryFn: () => fetchUserFollowers(userId),
      },
    ],
  });

  return {
    user: results[0].data,
    stats: results[1].data,
    posts: results[2].data,
    followers: results[3].data,
    isLoading: results.some((r) => r.isLoading),
  };
}
```

---

## **🎓 REACT QUERY BEST PRACTICES - ADVANCED EDITION**

### **✅ Performance Optimization**

```typescript
// 1. Selective re-renders với select
const { data: userName } = useQuery({
  queryKey: ['user', userId],
  queryFn: fetchUser,
  select: (user) => user.name, // ✅ Chỉ re-render khi name thay đổi
});

// 2. Structural sharing (automatic)
// React Query tự động so sánh data mới vs cũ
// Chỉ re-render khi có thay đổi thực sự

// 3. Memoize query options
const queryOptions = useMemo(
  () => ({
    queryKey: ['users', filters],
    queryFn: () => fetchUsers(filters),
  }),
  [filters]
);
const { data } = useQuery(queryOptions);

// 4. Prefetch intelligently
const queryClient = useQueryClient();

const handleHover = (userId: string) => {
  queryClient.prefetchQuery({
    queryKey: ['user', userId],
    queryFn: () => fetchUser(userId),
  });
};
```

### **✅ Error Recovery Patterns**

```typescript
// 1. Fallback queries
function useUserWithFallback(userId: string) {
  const primary = useQuery({
    queryKey: ['user', userId, 'primary'],
    queryFn: () => fetchUserFromPrimaryAPI(userId),
    retry: 1,
  });

  const fallback = useQuery({
    queryKey: ['user', userId, 'fallback'],
    queryFn: () => fetchUserFromFallbackAPI(userId),
    enabled: primary.isError, // ✅ Chỉ fetch khi primary failed
  });

  return primary.isError ? fallback : primary;
}

// 2. Retry với custom logic
retry: (failureCount, error) => {
  // Network errors → retry
  if (error.name === 'NetworkError') return failureCount < 5;

  // 5xx errors → retry
  if (error.status >= 500) return failureCount < 3;

  // 4xx errors → don't retry
  return false;
};
```

---

**🎯 Key Takeaways:**

1. **Cancellation** prevents memory leaks & race conditions
2. **Deduplication** saves network bandwidth automatically
3. **Parallel queries** optimize loading performance
4. **Custom QueryClient** enables global error handling
5. **Persistence** improves offline experience
6. **SSR/SSG** enhances initial page load & SEO
7. **Advanced caching** tailors behavior to use case
8. **Query filters** enable powerful batch operations
9. **Prevent waterfalls** reduces total loading time
