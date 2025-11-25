# 🔄 Q55: GraphQL vs REST - API Design, Apollo Client

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"GraphQL = single endpoint, client-driven queries, exact data (no over/under-fetching). REST = multiple endpoints, server-driven. Apollo Client: caching, optimistic updates, subscriptions. GraphQL tốt cho complex data, REST tốt cho simple CRUD."**

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
2. [Apollo Client Setup](#2-apollo-client-setup)
3. [Queries & Mutations](#3-queries--mutations)
4. [Caching Strategies](#4-caching-strategies)
5. [Pagination](#5-pagination)
6. [Optimistic Updates](#6-optimistic-updates)
7. [Error Handling](#7-error-handling)

---

## 1. GraphQL vs REST Comparison

### **1.1. Key Differences**

```typescript
// ===================================================
// 🔄 **REST vs GRAPHQL COMPARISON**
// ===================================================

// ❌ REST: Multiple endpoints, over-fetching
// GET /api/users/123
// GET /api/users/123/posts
// GET /api/users/123/friends

const userData = await fetch('/api/users/123').then(r => r.json());
// Returns: { id, name, email, phone, address, ... } ← Over-fetching

const userPosts = await fetch('/api/users/123/posts').then(r => r.json());
const userFriends = await fetch('/api/users/123/friends').then(r => r.json());
// Total: 3 HTTP requests

// ✅ GraphQL: Single endpoint, exact data
const { data } = await apolloClient.query({
  query: gql`
    query GetUserProfile($userId: ID!) {
      user(id: $userId) {
        id
        name
        email
        posts(limit: 5) {
          id
          title
          createdAt
        }
        friends(limit: 10) {
          id
          name
          avatar
        }
      }
    }
  `,
  variables: { userId: '123' },
});
// Total: 1 HTTP request, no over-fetching

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

// ✅ HTTP Link
const httpLink = new HttpLink({
  uri: import.meta.env.VITE_GRAPHQL_ENDPOINT,
});

// ✅ Auth Link (add JWT token)
const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem('auth_token');
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : '',
    },
  };
});

// ✅ Error Link (global error handling)
const errorLink = onError(({ graphQLErrors, networkError, operation }) => {
  if (graphQLErrors) {
    graphQLErrors.forEach(({ message, locations, path, extensions }) => {
      console.error(
        `[GraphQL error]: Message: ${message}, Path: ${path}`,
        extensions
      );
      
      // Handle authentication errors
      if (extensions?.code === 'UNAUTHENTICATED') {
        localStorage.removeItem('auth_token');
        window.location.href = '/login';
      }
    });
  }
  
  if (networkError) {
    console.error(`[Network error]: ${networkError}`);
  }
});

// ✅ Retry Link (retry failed requests)
const retryLink = new RetryLink({
  delay: {
    initial: 300,
    max: 5000,
    jitter: true,
  },
  attempts: {
    max: 3,
    retryIf: (error, operation) => {
      // Retry on network errors, not on GraphQL errors
      return !!error && !error.result;
    },
  },
});

// ✅ Apollo Client
export const apolloClient = new ApolloClient({
  link: ApolloLink.from([
    errorLink,
    retryLink,
    authLink,
    httpLink,
  ]),
  
  cache: new InMemoryCache({
    typePolicies: {
      Query: {
        fields: {
          // ✅ Pagination merge function
          posts: {
            keyArgs: ['filter'],
            merge(existing = { edges: [] }, incoming) {
              return {
                ...incoming,
                edges: [...existing.edges, ...incoming.edges],
              };
            },
          },
        },
      },
      
      // ✅ Custom cache ID
      User: {
        keyFields: ['id'],
      },
      
      Post: {
        keyFields: ['id'],
        fields: {
          // ✅ Normalize nested objects
          author: {
            merge: true,
          },
        },
      },
    },
  }),
  
  defaultOptions: {
    watchQuery: {
      fetchPolicy: 'cache-and-network',
      errorPolicy: 'all',
    },
    query: {
      fetchPolicy: 'network-only',
      errorPolicy: 'all',
    },
    mutate: {
      errorPolicy: 'all',
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

// ✅ Component using query
function UserProfile({ userId }: { userId: string }) {
  const { data, loading, error, refetch } = useQuery(GET_USER_QUERY, {
    variables: { userId },
    
    // ✅ Fetch policy options:
    // - cache-first: Check cache first (default)
    // - cache-and-network: Return cache immediately, then fetch
    // - network-only: Always fetch from network
    // - cache-only: Only use cache, don't fetch
    // - no-cache: Fetch but don't cache
    fetchPolicy: 'cache-and-network',
    
    // ✅ Poll every 30 seconds
    pollInterval: 30000,
    
    // ✅ Skip query conditionally
    skip: !userId,
    
    // ✅ On complete callback
    onCompleted: (data) => {
      console.log('User loaded:', data.user.name);
    },
    
    // ✅ On error callback
    onError: (error) => {
      console.error('Failed to load user:', error);
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
  const [createPost, { data, loading, error }] = useMutation(
    CREATE_POST_MUTATION,
    {
      // ✅ Update cache after mutation
      update(cache, { data: { createPost } }) {
        // Read existing posts from cache
        const existing: any = cache.readQuery({
          query: GET_POSTS_QUERY,
        });
        
        // Write updated posts to cache
        cache.writeQuery({
          query: GET_POSTS_QUERY,
          data: {
            posts: {
              ...existing.posts,
              edges: [createPost, ...existing.posts.edges],
            },
          },
        });
      },
      
      // ✅ Refetch queries after mutation
      refetchQueries: [
        { query: GET_POSTS_QUERY },
        { query: GET_USER_POSTS_QUERY, variables: { userId: currentUserId } },
      ],
      
      // ✅ Await refetch queries
      awaitRefetchQueries: true,
      
      // ✅ On completed callback
      onCompleted: (data) => {
        toast.success(`Post "${data.createPost.title}" created!`);
        navigate(`/posts/${data.createPost.id}`);
      },
      
      // ✅ On error callback
      onError: (error) => {
        toast.error('Failed to create post');
        console.error(error);
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
  const client = useApolloClient();
  
  // ✅ Read from cache
  const readUser = () => {
    const user = client.readFragment({
      id: `User:${userId}`,
      fragment: gql`
        fragment MyUser on User {
          id
          name
          email
        }
      `,
    });
    console.log('Cached user:', user);
  };
  
  // ✅ Write to cache
  const updateUserName = (newName: string) => {
    client.writeFragment({
      id: `User:${userId}`,
      fragment: gql`
        fragment UpdatedUser on User {
          name
        }
      `,
      data: {
        name: newName,
      },
    });
  };
  
  // ✅ Evict from cache
  const removeUser = () => {
    client.cache.evict({
      id: `User:${userId}`,
    });
    client.cache.gc(); // Garbage collect
  };
  
  // ✅ Reset entire cache
  const clearCache = () => {
    client.cache.reset();
  };
  
  // ✅ Modify cache field
  const incrementLikes = (postId: string) => {
    client.cache.modify({
      id: `Post:${postId}`,
      fields: {
        likes(existing = 0) {
          return existing + 1;
        },
      },
    });
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
  const { data, loading, fetchMore } = useQuery(GET_POSTS_QUERY, {
    variables: { limit: 20 },
  });
  
  const loadMore = () => {
    fetchMore({
      variables: {
        after: data?.posts.pageInfo.endCursor,
      },
    });
  };
  
  return (
    <div>
      {data?.posts.edges.map(({ node }) => (
        <PostCard key={node.id} post={node} />
      ))}
      
      {data?.posts.pageInfo.hasNextPage && (
        <button onClick={loadMore} disabled={loading}>
          {loading ? 'Loading...' : 'Load More'}
        </button>
      )}
    </div>
  );
}

// ===================================================
// 🔢 **OFFSET PAGINATION**
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
  const [page, setPage] = useState(1);
  const limit = 20;
  
  const { data, loading } = useQuery(GET_PRODUCTS_QUERY, {
    variables: {
      offset: (page - 1) * limit,
      limit,
    },
  });
  
  const totalPages = Math.ceil((data?.products.total ?? 0) / limit);
  
  return (
    <div>
      <ProductGrid products={data?.products.items ?? []} />
      
      <Pagination
        currentPage={page}
        totalPages={totalPages}
        onPageChange={setPage}
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
  const [likePost] = useMutation(LIKE_POST_MUTATION, {
    // ✅ Optimistic response (instant UI update)
    optimisticResponse: {
      likePost: {
        __typename: 'Post',
        id: postId,
        likes: likes + (isLiked ? -1 : 1),
        isLikedByMe: !isLiked,
      },
    },
    
    // ✅ Update cache optimistically
    update(cache, { data: { likePost } }) {
      cache.modify({
        id: cache.identify({ __typename: 'Post', id: postId }),
        fields: {
          likes() {
            return likePost.likes;
          },
          isLikedByMe() {
            return likePost.isLikedByMe;
          },
        },
      });
    },
    
    // ✅ Rollback on error
    onError: (error) => {
      console.error('Like failed, rolling back...', error);
      toast.error('Failed to like post');
    },
  });
  
  return (
    <button onClick={() => likePost({ variables: { postId } })}>
      {isLiked ? '❤️' : '🤍'} {likes}
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
  // ✅ Handle GraphQL errors
  if (error.graphQLErrors.length > 0) {
    return (
      <div>
        {error.graphQLErrors.map((err, i) => {
          // Check error code
          switch (err.extensions?.code) {
            case 'UNAUTHENTICATED':
              return <LoginPrompt key={i} />;
            
            case 'FORBIDDEN':
              return <AccessDenied key={i} />;
            
            case 'NOT_FOUND':
              return <NotFound key={i} />;
            
            case 'VALIDATION_ERROR':
              return <ValidationErrors key={i} errors={err.extensions.errors} />;
            
            default:
              return <GenericError key={i} message={err.message} />;
          }
        })}
      </div>
    );
  }
  
  // ✅ Handle network errors
  if (error.networkError) {
    return <NetworkErrorMessage />;
  }
  
  return <GenericError message={error.message} />;
}
```

---

**🎯 Remember:** "GraphQL gives you exactly what you ask for - no more, no less. Design your queries wisely!"
