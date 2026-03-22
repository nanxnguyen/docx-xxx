# 🔄 Q55: API Design & Integration Patterns

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"API Design = REST best practices (RESTful principles, versioning, rate limiting) + GraphQL (single endpoint, client-driven). Integration patterns: Pagination (cursor vs offset), Real-time (Polling vs Long-polling vs SSE), Error handling, Caching strategies. Apollo Client: normalized cache, optimistic updates, subscriptions."**

**🔑 GraphQL vs REST:**

| **Aspect** | **REST** | **GraphQL** |
|-----------|---------|------------|
| **Endpoints** | Multiple (`/users`, `/posts`) | Single (`/graphql`) |
| **Data fetching** | Server decides | **Client decides** |
| **Over-fetching** | ✅ Common | ❌ Exact fields |
| **Under-fetching** | ✅ Multiple requests | ❌ Single request |
| **Versioning** | `/v1`, `/v2` | **No versions** (deprecate fields) |
| **Caching** | HTTP cache (simple) | Custom (Apollo cache) |

**🔑 Apollo Client Features:**

**1. Caching:**
- **Normalized cache**: Store objects by ID, auto-dedupe
- **Cache policies**: cache-first, network-only, cache-and-network
- **Auto-update**: Mutations auto-update affected queries

**2. Queries & Mutations:**
- **useQuery**: Fetch data + loading/error states
- **useMutation**: Modify data + optimistic updates
- **Fragments**: Reusable field selections

**3. Subscriptions (Real-time):**
- WebSocket connection cho real-time updates
- Use case: Chat, notifications, live data

**4. Optimistic Updates:**
- Update UI immediately (assume success)
- Rollback if mutation fails

**⚠️ Lỗi Thường Gặp:**
- N+1 queries → backend performance issue (dùng DataLoader)
- Không hiểu cache → redundant network requests
- Over-complicated queries → chậm backend, split queries
- Public GraphQL endpoint không rate limit → DoS risk

**💡 Kiến Thức Senior:**
- **Persisted queries**: Pre-register queries (security + performance)
- **Automatic Persisted Queries** (APQ): Hash queries → reduce bandwidth
- **Federation**: Microservices architecture cho GraphQL
- **Batching**: Combine multiple queries in 1 HTTP request

> **Câu hỏi phỏng vấn Senior Frontend Developer**
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 12-15 phút

---

## 📋 **Mục Lục**

1. [GraphQL vs REST Comparison](#1-graphql-vs-rest-comparison)
2. [REST Best Practices](#2-rest-best-practices)
3. [API Versioning](#3-api-versioning)
4. [Rate Limiting Handling](#4-rate-limiting-handling)
5. [Pagination Strategies](#5-pagination-strategies)
6. [Real-time Data Patterns](#6-real-time-data-patterns)
7. [Apollo Client Setup](#7-apollo-client-setup)
8. [Queries & Mutations](#8-queries--mutations)
9. [Caching Strategies](#9-caching-strategies)
10. [Optimistic Updates](#10-optimistic-updates)
11. [Error Handling](#11-error-handling)

---

## 1. GraphQL vs REST Comparison

### **1.1. Key Differences**

```typescript
// ===================================================
// 🔄 **REST vs GRAPHQL COMPARISON**
// ===================================================

// ❌ REST: Multiple endpoints, over-fetching (Nhiều endpoints, lấy thừa data)
// 📍 GET /api/users/123          → Lấy user info
// 📍 GET /api/users/123/posts    → Lấy posts của user
// 📍 GET /api/users/123/friends  → Lấy friends của user

const userData = await fetch('/api/users/123').then(r => r.json());
// 📦 Returns: { id, name, email, phone, address, ... } ← ❌ Over-fetching
// Server trả về TẤT CẢ fields (phone, address) dù client chỉ cần id, name, email
// → Lãng phí bandwidth, chậm trên mobile

const userPosts = await fetch('/api/users/123/posts').then(r => r.json());
const userFriends = await fetch('/api/users/123/friends').then(r => r.json());
// 📊 Total: 3 HTTP requests (3 round-trips → slow)
// → Under-fetching problem: Cần nhiều requests để lấy đủ data

// ✅ GraphQL: Single endpoint, exact data (1 endpoint, chính xác data cần)
// 🎯 POST /graphql → Chỉ 1 endpoint duy nhất
const { data } = await apolloClient.query({
  query: gql`
    query GetUserProfile($userId: ID!) {  # 📝 Query name + variables
      user(id: $userId) {  # 🔍 Root field: lấy user theo ID
        id          # ✅ Chỉ lấy fields cần thiết
        name        # ✅ Không lấy phone, address (không cần)
        email
        posts(limit: 5) {  # 🔗 Nested field: lấy 5 posts mới nhất
          id
          title
          createdAt
        }
        friends(limit: 10) {  # 🔗 Nested field: lấy 10 friends
          id
          name
          avatar
        }
      }
    }
  `,
  variables: { userId: '123' },  // 📌 Truyền biến userId
});
// 📊 Total: 1 HTTP request (1 round-trip) ✅
// 🎯 No over-fetching: Client chỉ định CHÍNH XÁC fields cần
// 🎯 No under-fetching: Lấy tất cả data cần trong 1 request

// ===================================================
// 📊 **COMPARISON TABLE**
// ===================================================

const COMPARISON_TABLE = {
  feature: {
    REST: 'Multiple endpoints (/users, /posts, /comments)',
    GraphQL: 'Single endpoint (/graphql)',
  },

  dataFetching: {
    REST: 'Fixed response structure (over/under-fetching)',
    GraphQL: 'Client specifies exact fields needed',
  },

  versioning: {
    REST: 'Version in URL (/v1/users, /v2/users)',
    GraphQL: 'Field-level deprecation, no versioning',
  },

  caching: {
    REST: 'HTTP caching (Cache-Control, ETag)',
    GraphQL: 'Client-side normalized cache (Apollo)',
  },

  typing: {
    REST: 'Manual TypeScript types or OpenAPI',
    GraphQL: 'Auto-generated from schema',
  },

  realTime: {
    REST: 'Polling, WebSockets, SSE',
    GraphQL: 'Subscriptions built-in',
  },

  complexity: {
    REST: 'Simple to understand, mature ecosystem',
    GraphQL: 'Steeper learning curve, powerful',
  },
};

// ===================================================
// 🎯 **WHEN TO USE EACH**
// ===================================================

const USE_GRAPHQL_WHEN = [
  '✅ Complex data requirements (nested relationships)',
  '✅ Mobile apps (reduce network requests)',
  '✅ Multiple clients with different needs',
  '✅ Need strong typing & auto-generated docs',
  '✅ Real-time features (subscriptions)',
];

const USE_REST_WHEN = [
  '✅ Simple CRUD operations',
  '✅ File uploads/downloads',
  '✅ HTTP caching is critical',
  '✅ Team unfamiliar with GraphQL',
  '✅ Existing REST infrastructure',
];
```

---

## 2. Apollo Client Setup

### **2.1. Apollo Client Configuration**

```typescript
// ===================================================
// ⚙️ **APOLLO CLIENT SETUP**
// ===================================================

import { ApolloClient, InMemoryCache, HttpLink, ApolloLink } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';
import { onError } from '@apollo/client/link/error';
import { RetryLink } from '@apollo/client/link/retry';

// ✅ HTTP Link (Kết nối HTTP tới GraphQL server)
const httpLink = new HttpLink({
  uri: import.meta.env.VITE_GRAPHQL_ENDPOINT,  // 🌐 GraphQL endpoint (VD: https://api.example.com/graphql)
  // → Chỉ có 1 endpoint duy nhất (khác REST có nhiều endpoints)
});

// ✅ Auth Link (Thêm JWT token vào mỗi request)
const authLink = setContext((_, { headers }) => {  // 🔧 Middleware chạy TRƯỚC mỗi request
  const token = localStorage.getItem('auth_token');  // 🔑 Lấy JWT token từ localStorage
  return {
    headers: {  // 📝 Merge headers
      ...headers,  // 📦 Giữ lại headers hiện có
      authorization: token ? `Bearer ${token}` : '',  // 🔑 Thêm Authorization header
      // Nếu có token → "Bearer eyJhbG..."
      // Nếu không → "" (empty string)
    },
  };
});

// ✅ Error Link (Xử lý lỗi toàn cục)
const errorLink = onError(({ graphQLErrors, networkError, operation }) => {
  if (graphQLErrors) {  // 🚨 GraphQL errors (lỗi từ server GraphQL)
    graphQLErrors.forEach(({ message, locations, path, extensions }) => {
      console.error(
        `[GraphQL error]: Message: ${message}, Path: ${path}`,  // 📍 Đường dẫn query bị lỗi
        extensions  // 📦 Thêm info (code, timestamp, etc.)
      );

      // 🔑 Handle authentication errors (Lỗi xác thực)
      if (extensions?.code === 'UNAUTHENTICATED') {
        localStorage.removeItem('auth_token');  // 🗄️ Xóa token hết hạn
        window.location.href = '/login';  // 🔄 Redirect về login
      }
    });
  }

  if (networkError) {  // 🌐 Network errors (lỗi kết nối)
    console.error(`[Network error]: ${networkError}`);
    // VD: 500 Internal Server Error, timeout, no internet
  }
});

// ✅ Retry Link (Tự động retry khi request fail)
const retryLink = new RetryLink({
  delay: {  // ⏰ Thời gian chờ giữa các lần retry
    initial: 300,  // 🔹 Lần đầu: 300ms
    max: 5000,     // 🔹 Tối đa: 5s (exponential backoff)
    jitter: true,  // 🎲 Thêm random để tránh thundering herd
  },
  attempts: {  // 🔢 Số lần retry
    max: 3,  // 🔹 Tối đa 3 lần
    retryIf: (error, operation) => {  // ❓ Kiểm tra có nên retry không
      // Retry on network errors, not on GraphQL errors
      return !!error && !error.result;  // ✅ Chỉ retry network errors (không retry GraphQL errors)
      // GraphQL errors (VD: validation) không cần retry (chắc chắn fail)
    },
  },
});

// ✅ Apollo Client (Main client instance)
export const apolloClient = new ApolloClient({
  link: ApolloLink.from([  // 🔗 Chain các links (chạy theo thứ tự)
    errorLink,    // 1️⃣ Xử lý lỗi đầu tiên
    retryLink,    // 2️⃣ Retry nếu cần
    authLink,     // 3️⃣ Thêm auth token
    httpLink,     // 4️⃣ Cuối cùng: Gửi HTTP request
  ]),

  cache: new InMemoryCache({  // 💾 Normalized cache (cache chuẩn hóa)
    typePolicies: {  // 📖 Cấu hình cache cho từng type
      Query: {  // 🔍 Root Query type
        fields: {  // 📋 Các fields trong Query
          // ✅ Pagination merge function (Hàm merge cho infinite scroll)
          posts: {
            keyArgs: ['filter'],  // 🔑 Các args quyết định cache key
            // Nếu filter khác → cache entry khác
            merge(existing = { edges: [] }, incoming) {  // 🔀 Merge data mới với cũ
              return {
                ...incoming,
                edges: [...existing.edges, ...incoming.edges],  // 📦 Nối edges (append)
                // → Infinite scroll: giữ posts cũ + thêm posts mới
              };
            },
          },
        },
      },

      // ✅ Custom cache ID (ID chuẩn hóa)
      User: {  // 👤 User type
        keyFields: ['id'],  // 🔑 Dùng field 'id' làm cache key
        // Cache key = "User:123" (User:${id})
      },

      Post: {  // 📝 Post type
        keyFields: ['id'],  // 🔑 Dùng 'id' làm cache key
        fields: {  // 📋 Fields config
          // ✅ Normalize nested objects (Chuẩn hóa objects lồng nhau)
          author: {  // 👤 Author là nested User object
            merge: true,  // ✅ Merge thay vì replace (giữ data cũ)
            // Nếu author đã có trong cache → reference tới User object đó
          },
        },
      },
    },
  }),

  defaultOptions: {  // ⚙️ Tùy chọn mặc định cho tất cả queries/mutations
    watchQuery: {  // 👁️ useQuery hook options
      fetchPolicy: 'cache-and-network',  // 💾 Trả về cache ngay + fetch network
      // → UX nhanh (hiển cache trước) + data mới nhất (fetch sau)
      errorPolicy: 'all',  // 🚨 Trả về data + errors (không throw)
    },
    query: {  // 🔍 client.query() options
      fetchPolicy: 'network-only',  // 🌐 Luôn fetch từ network (bỏ qua cache)
      // → Luôn lấy data mới nhất
      errorPolicy: 'all',  // 🚨 Trả về data + errors
    },
    mutate: {  // ✏️ useMutation hook options
      errorPolicy: 'all',  // 🚨 Trả về data + errors
    },
  },
});

// ===================================================
// 🎯 **APOLLO PROVIDER**
// ===================================================

import { ApolloProvider } from '@apollo/client';

export function App() {
  return (
    <ApolloProvider client={apolloClient}>
      <Router />
    </ApolloProvider>
  );
}
```

---

## 3. Queries & Mutations

### **3.1. Type-Safe Queries**

```typescript
// ===================================================
// 📝 **GRAPHQL QUERIES**
// ===================================================

import { gql, useQuery, TypedDocumentNode } from '@apollo/client';

// ✅ GraphQL query with fragment
const USER_FRAGMENT = gql`
  fragment UserFields on User {
    id
    name
    email
    avatar
    createdAt
  }
`;

const GET_USER_QUERY: TypedDocumentNode<
  { user: User },
  { userId: string }
> = gql`
  ${USER_FRAGMENT}

  query GetUser($userId: ID!) {
    user(id: $userId) {
      ...UserFields
      posts(limit: 10) {
        id
        title
        content
        publishedAt
      }
    }
  }
`;

// ✅ Component using query (Component dùng query)
function UserProfile({ userId }: { userId: string }) {
  const { data, loading, error, refetch } = useQuery(GET_USER_QUERY, {  // 🎯 Hook query data
    variables: { userId },  // 📌 Biến truyền vào query ($userId)

    // ✅ Fetch policy options (Chiến lược fetch):
    // - cache-first: Kiểm tra cache trước (default) → nhanh nhưng có thể stale
    // - cache-and-network: Trả cache ngay + fetch network → UX tốt nhất
    // - network-only: Luôn fetch từ network → luôn mới nhất
    // - cache-only: Chỉ dùng cache, không fetch → offline mode
    // - no-cache: Fetch nhưng không cache → dùng cho sensitive data
    fetchPolicy: 'cache-and-network',  // 💾+🌐 Hiển cache + fetch mới

    // ✅ Poll every 30 seconds (Tự động refetch mỗi 30s)
    pollInterval: 30000,  // ⏰ 30000ms = 30s
    // → Auto-refresh data (VD: dashboard, live data)

    // ✅ Skip query conditionally (Bỏ qua query nếu điều kiện)
    skip: !userId,  // ⚠️ Nếu userId không có → không chạy query
    // → Tránh query với biến invalid

    // ✅ On complete callback (Callback khi query thành công)
    onCompleted: (data) => {
      console.log('User loaded:', data.user.name);  // 📝 Log success
    },

    // ✅ On error callback (Callback khi query lỗi)
    onError: (error) => {
      console.error('Failed to load user:', error);  // 🚨 Log error
    },
  });

  if (loading) return <Skeleton />;
  if (error) return <ErrorMessage error={error} retry={refetch} />;
  if (!data?.user) return <NotFound />;

  return (
    <div>
      <h1>{data.user.name}</h1>
      <img src={data.user.avatar} alt={data.user.name} />

      <PostList posts={data.user.posts} />

      <button onClick={() => refetch()}>Refresh</button>
    </div>
  );
}
```

### **3.2. Mutations**

```typescript
// ===================================================
// ✏️ **GRAPHQL MUTATIONS**
// ===================================================

const CREATE_POST_MUTATION = gql`
  mutation CreatePost($input: CreatePostInput!) {
    createPost(input: $input) {
      id
      title
      content
      publishedAt
      author {
        id
        name
      }
    }
  }
`;

function CreatePostForm() {
  const [createPost, { data, loading, error }] = useMutation(  // ✏️ Hook mutation
    CREATE_POST_MUTATION,
    {
      // ✅ Update cache after mutation (Cập nhật cache sau khi mutation)
      update(cache, { data: { createPost } }) {  // 💾 Callback nhận cache + data mới
        // 🔹 Đọc existing posts từ cache
        const existing: any = cache.readQuery({  // 💾 Đọc query cũ
          query: GET_POSTS_QUERY,
        });

        // 🔹 Ghi updated posts vào cache
        cache.writeQuery({  // ✏️ Ghi vào cache
          query: GET_POSTS_QUERY,
          data: {
            posts: {
              ...existing.posts,
              edges: [createPost, ...existing.posts.edges],  // 📦 Thêm post mới vào đầu list
              // → UI tự động cập nhật (không cần refetch)
            },
          },
        });
      },

      // ✅ Refetch queries after mutation (Refetch queries sau mutation)
      refetchQueries: [  // 🔄 Danh sách queries cần refetch
        { query: GET_POSTS_QUERY },  // 🔄 Refetch all posts
        { query: GET_USER_POSTS_QUERY, variables: { userId: currentUserId } },  // 🔄 Refetch user posts
      ],
      // → Đảm bảo data mới nhất sau mutation

      // ✅ Await refetch queries (Chờ refetch hoàn thành)
      awaitRefetchQueries: true,  // ⏳ Chờ refetch xong mới resolve mutation
      // → Đảm bảo UI cập nhật trước khi tiếp tục

      // ✅ On completed callback
      onCompleted: (data) => {
        toast.success(`Post "${data.createPost.title}" created!`);  // 🎉 Hiển thông báo
        navigate(`/posts/${data.createPost.id}`);  // 🔀 Navigate đến post mới
      },

      // ✅ On error callback
      onError: (error) => {
        toast.error('Failed to create post');  // ❌ Hiển lỗi
        console.error(error);  // 🚨 Log error
      },
    }
  );

  const handleSubmit = async (values: FormValues) => {
    await createPost({
      variables: {
        input: {
          title: values.title,
          content: values.content,
        },
      },
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="title" />
      <textarea name="content" />
      <button type="submit" disabled={loading}>
        {loading ? 'Creating...' : 'Create Post'}
      </button>
      {error && <ErrorMessage error={error} />}
    </form>
  );
}
```

---

## 4. Caching Strategies

### **4.1. Normalized Cache**

```typescript
// ===================================================
// 💾 **APOLLO CACHE MANAGEMENT**
// ===================================================

import { useApolloClient } from '@apollo/client';

function UserActions({ userId }: { userId: string }) {
  const client = useApolloClient();  // 🔧 Lấy Apollo client instance

  // ✅ Read from cache (Đọc từ cache)
  const readUser = () => {
    const user = client.readFragment({  // 💾 Đọc fragment từ cache
      id: `User:${userId}`,  // 🔑 Cache ID (Type:id format)
      fragment: gql`  // 📝 Fragment định nghĩa fields cần đọc
        fragment MyUser on User {
          id
          name
          email
        }
      `,
    });
    console.log('Cached user:', user);  // 💾 In ra user từ cache
  };

  // ✅ Write to cache (Ghi vào cache)
  const updateUserName = (newName: string) => {
    client.writeFragment({  // ✏️ Ghi fragment vào cache
      id: `User:${userId}`,  // 🔑 Cache ID
      fragment: gql`  // 📝 Fragment định nghĩa fields cần ghi
        fragment UpdatedUser on User {
          name
        }
      `,
      data: {  // 📦 Data mới
        name: newName,  // ✏️ Cập nhật name
      },
    });
    // → UI tự động re-render (React hooks lắng nghe cache)
  };

  // ✅ Evict from cache (Xóa khỏi cache)
  const removeUser = () => {
    client.cache.evict({  // 🗄️ Xóa object khỏi cache
      id: `User:${userId}`,  // 🔑 Cache ID cần xóa
    });
    client.cache.gc();  // 🧹 Garbage collect (dọn dẹp cache)
    // → Xóa các references không còn dùng
  };

  // ✅ Reset entire cache (Reset toàn bộ cache)
  const clearCache = () => {
    client.cache.reset();  // 🗄️ Xóa TẤT CẢ cache
    // → Mọi queries sẽ refetch lại
  };

  // ✅ Modify cache field (Sửa field trong cache)
  const incrementLikes = (postId: string) => {
    client.cache.modify({  // ✏️ Sửa đổi cache
      id: `Post:${postId}`,  // 🔑 Cache ID
      fields: {  // 📋 Fields cần sửa
        likes(existing = 0) {  // 🔹 Nhận giá trị hiện tại
          return existing + 1;  // 🔼 Tăng lên 1
        },
      },
    });
    // → UI tự động cập nhật số likes
  };

  return (
    <div>
      <button onClick={readUser}>Read Cache</button>
      <button onClick={() => updateUserName('New Name')}>Update Name</button>
      <button onClick={removeUser}>Remove User</button>
      <button onClick={clearCache}>Clear All Cache</button>
    </div>
  );
}
```

---

## 5. Pagination

### **5.1. Cursor-Based Pagination**

```typescript
// ===================================================
// 📄 **CURSOR PAGINATION**
// ===================================================

const GET_POSTS_QUERY = gql`
  query GetPosts($after: String, $limit: Int!) {
    posts(after: $after, limit: $limit) {
      edges {
        cursor
        node {
          id
          title
          content
          author {
            id
            name
          }
        }
      }
      pageInfo {
        hasNextPage
        endCursor
      }
    }
  }
`;

function InfinitePostList() {
  const { data, loading, fetchMore } = useQuery(GET_POSTS_QUERY, {  // 🔍 Query posts
    variables: { limit: 20 },  // 🔢 Lấy 20 posts mỗi lần
  });

  const loadMore = () => {  // 📥 Hàm load thêm posts
    fetchMore({  // 🔄 Fetch thêm data (không refetch from scratch)
      variables: {
        after: data?.posts.pageInfo.endCursor,  // 🔹 Cursor: Vị trí cuối cùng
        // → Lấy posts SAU cursor này (pagination)
      },
    });
    // → Apollo tự động merge với data cũ (theo merge function trong cache config)
  };

  return (
    <div>
      {data?.posts.edges.map(({ node }) => (  // 📋 Map qua edges
        <PostCard key={node.id} post={node} />  // 📦 Hiển thị mỗi post
      ))}

      {data?.posts.pageInfo.hasNextPage && (  // ❓ Nếu còn trang tiếp theo
        <button onClick={loadMore} disabled={loading}>  // 📥 Nút load more
          {loading ? 'Loading...' : 'Load More'}  // ⏳ Hiển trạng thái
        </button>
      )}
    </div>
  );
}

// ===================================================
// 🔢 **OFFSET PAGINATION** (Phân trang theo offset)
// ===================================================

const GET_PRODUCTS_QUERY = gql`
  query GetProducts($offset: Int!, $limit: Int!) {
    products(offset: $offset, limit: $limit) {
      items {
        id
        name
        price
      }
      total
    }
  }
`;

function PaginatedProducts() {
  const [page, setPage] = useState(1);  // 📌 State: Trang hiện tại
  const limit = 20;  // 🔢 Số items mỗi trang

  const { data, loading } = useQuery(GET_PRODUCTS_QUERY, {  // 🔍 Query products
    variables: {
      offset: (page - 1) * limit,  // 📍 Offset: Bỏ qua bao nhiêu items
      // VD: Page 1 → offset = 0, Page 2 → offset = 20, Page 3 → offset = 40
      limit,  // 🔢 Lấy bao nhiêu items
    },
  });

  const totalPages = Math.ceil((data?.products.total ?? 0) / limit);  // 📊 Tính tổng số trang
  // VD: Total 95 items, limit 20 → 95/20 = 4.75 → ceil = 5 trang

  return (
    <div>
      <ProductGrid products={data?.products.items ?? []} />  // 📋 Hiển thị products

      <Pagination  // 🔢 Component pagination
        currentPage={page}  // 📍 Trang hiện tại
        totalPages={totalPages}  // 📊 Tổng số trang
        onPageChange={setPage}  // 🔄 Callback khi chuyển trang
      />
    </div>
  );
}
```

---

## 6. Optimistic Updates

### **6.1. Optimistic UI**

```typescript
// ===================================================
// ⚡ **OPTIMISTIC UPDATES**
// ===================================================

const LIKE_POST_MUTATION = gql`
  mutation LikePost($postId: ID!) {
    likePost(postId: $postId) {
      id
      likes
      isLikedByMe
    }
  }
`;

function LikeButton({ postId, likes, isLiked }: LikeButtonProps) {
  const [likePost] = useMutation(LIKE_POST_MUTATION, {  // ✏️ Mutation like post
    // ✅ Optimistic response (Cập nhật UI NGAY - giả định thành công)
    optimisticResponse: {  // 🚀 Instant UI update (không chờ server response)
      likePost: {  // 📦 Fake response (giống thật)
        __typename: 'Post',  // 🏷️ Type name
        id: postId,  // 🔑 Post ID
        likes: likes + (isLiked ? -1 : 1),  // 🔢 Tăng/giảm likes ngay lập tức
        // Nếu đang liked → giảm 1 (unlike), ngược lại → tăng 1 (like)
        isLikedByMe: !isLiked,  // 👤 Đảo trạng thái liked
      },
    },
    // → UI cập nhật NGAY (trước khi server response) → UX tuyệt vời!

    // ✅ Update cache optimistically (Cập nhật cache ngay)
    update(cache, { data: { likePost } }) {  // 💾 Callback cập nhật cache
      cache.modify({  // ✏️ Sửa cache
        id: cache.identify({ __typename: 'Post', id: postId }),  // 🔑 Tìm Post trong cache
        fields: {  // 📋 Cập nhật fields
          likes() {  // 🔢 Update likes
            return likePost.likes;  // ✅ Giá trị mới
          },
          isLikedByMe() {  // 👤 Update isLikedByMe
            return likePost.isLikedByMe;  // ✅ Giá trị mới
          },
        },
      });
    },

    // ✅ Rollback on error (Rollback nếu thất bại)
    onError: (error) => {  // 🚨 Nếu server trả lỗi
      console.error('Like failed, rolling back...', error);  // 🚨 Log error
      toast.error('Failed to like post');  // ❌ Hiển thông báo lỗi
      // → Apollo tự động ROLLBACK optimistic update (trả về giá trị cũ)
    },
  });

  return (
    <button onClick={() => likePost({ variables: { postId } })}>  // 💆 Click để like
      {isLiked ? '❤️' : '🤍'} {likes}  // 📊 Hiển trạng thái + số likes
    </button>
  );
}
```

---

## 7. Error Handling

### **7.1. Comprehensive Error Handling**

```typescript
// ===================================================
// ❌ **ERROR HANDLING**
// ===================================================

import { ApolloError } from '@apollo/client';

function GraphQLErrorHandler({ error }: { error: ApolloError }) {
  // ✅ Handle GraphQL errors (Xử lý lỗi GraphQL)
  if (error.graphQLErrors.length > 0) {  // 🚨 Nếu có GraphQL errors
    return (
      <div>
        {error.graphQLErrors.map((err, i) => {  // 🔄 Loop qua tất cả errors
          // ❓ Check error code (Mã lỗi từ server)
          switch (err.extensions?.code) {  // 📌 extensions.code = custom error code
            case 'UNAUTHENTICATED':  // 🔑 Chưa đăng nhập
              return <LoginPrompt key={i} />;  // → Hiển form login

            case 'FORBIDDEN':  // 🚫 Không có quyền
              return <AccessDenied key={i} />;  // → Hiển thông báo không có quyền

            case 'NOT_FOUND':  // 🔍 Không tìm thấy
              return <NotFound key={i} />;  // → Hiển 404 page

            case 'VALIDATION_ERROR':  // ✅ Lỗi validation
              return <ValidationErrors key={i} errors={err.extensions.errors} />;  // → Hiển chi tiết lỗi

            default:  // 🚨 Lỗi khác
              return <GenericError key={i} message={err.message} />;  // → Hiển lỗi chung
          }
        })}
      </div>
    );
  }

  // ✅ Handle network errors (Xử lý lỗi network)
  if (error.networkError) {  // 🌐 Nếu có network error
    return <NetworkErrorMessage />;  // → Hiển thông báo lỗi kết nối
    // VD: 500 Internal Server Error, timeout, no internet
  }

  return <GenericError message={error.message} />;  // 🚨 Lỗi không xác định
}
```

---

**🎯 Remember:** "GraphQL gives you exactly what you ask for - no more, no less. Design your queries wisely!"
