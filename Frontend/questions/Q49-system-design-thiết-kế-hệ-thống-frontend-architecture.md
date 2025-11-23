# 🏗️ Q49: System Design - Thiết Kế Hệ Thống Frontend Architecture

> **Câu hỏi phỏng vấn Senior/Lead Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)  
> **Thời gian trả lời:** 20-30 phút (với whiteboard)

---

## 📋 **Mục Lục**

1. [Tổng Quan System Design](#1-tổng-quan-system-design)
2. [Micro-frontend Architecture](#2-micro-frontend-architecture)
3. [Monorepo Strategies](#3-monorepo-strategies)
4. [API Design Patterns](#4-api-design-patterns)
5. [State Management Architecture](#5-state-management-architecture)
6. [Error Boundaries & Resilience](#6-error-boundaries--resilience)
7. [Feature Flags System](#7-feature-flags-system)
8. [CDN & Edge Computing](#8-cdn--edge-computing)
9. [Real-World System Design Questions](#9-real-world-system-design-questions)

---

## 1. Tổng Quan System Design

### **1.1. System Design là gì?**

> **System Design (Thiết kế hệ thống)** là quá trình thiết kế kiến trúc hệ thống để đáp ứng **yêu cầu phi chức năng** (scalability - khả năng mở rộng, availability - tính sẵn sàng, performance - hiệu suất, maintainability - khả năng bảo trì) trong khi vẫn đảm bảo **yêu cầu chức năng** (những gì hệ thống cần làm).

**📌 Giải thích đơn giản:**
- **Yêu cầu chức năng:** App cần làm gì? (Ví dụ: Đăng nhập, xem sản phẩm, thanh toán)
- **Yêu cầu phi chức năng:** App cần hoạt động TỐT thế nào? (Ví dụ: Xử lý được 10 triệu user, load trang < 2 giây, hoạt động 99.9% thời gian)

### **📊 Frontend System Design Components**

```
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND SYSTEM DESIGN                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐     │
│  │   Client     │───▶│     CDN      │───▶│  API Gateway │     │
│  │   (Browser)  │    │  (CloudFlare)│    │  (BFF Layer) │     │
│  └──────────────┘    └──────────────┘    └──────────────┘     │
│         │                                         │            │
│         │                                         ▼            │
│         │                              ┌────────────────┐      │
│         │                              │  Microservices │      │
│         │                              │  (REST/GraphQL)│      │
│         │                              └────────────────┘      │
│         ▼                                                       │
│  ┌──────────────────────────────────────────────────────┐      │
│  │           MICRO-FRONTEND SHELL                      │      │
│  ├──────────────────────────────────────────────────────┤      │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌────────┐ │      │
│  │  │ Header  │  │Dashboard│  │ Profile │  │ Footer │ │      │
│  │  │ (Remote)│  │ (Remote)│  │ (Remote)│  │(Remote)│ │      │
│  │  └─────────┘  └─────────┘  └─────────┘  └────────┘ │      │
│  └──────────────────────────────────────────────────────┘      │
│         │                                                       │
│         ▼                                                       │
│  ┌──────────────────────────────────────────────────────┐      │
│  │  State Management Layer (Redux/Zustand/Jotai)       │      │
│  └──────────────────────────────────────────────────────┘      │
│         │                                                       │
│         ▼                                                       │
│  ┌──────────────────────────────────────────────────────┐      │
│  │  Caching Layer (React Query/SWR/Apollo)             │      │
│  └──────────────────────────────────────────────────────┘      │
│         │                                                       │
│         ▼                                                       │
│  ┌──────────────────────────────────────────────────────┐      │
│  │  Monitoring & Observability (Sentry/DataDog)        │      │
│  └──────────────────────────────────────────────────────┘      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### **1.2. Key Design Principles**

```typescript
// ===================================================
// ✅ **SOLID PRINCIPLES CHO FRONTEND**
// ===================================================

// 1️⃣ **Single Responsibility Principle (SRP) - Nguyên tắc Đơn Trách Nhiệm**
// Mỗi component/module chỉ nên làm MỘT việc duy nhất

// ❌ SAI: Component làm QUÁ NHIỀU việc (God Component)
const UserDashboard = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  
  // ❌ Trách nhiệm 1: Fetch data từ API
  useEffect(() => {
    fetchUsers().then(setUsers);
  }, []);
  
  // ❌ Trách nhiệm 2: Lọc dữ liệu
  const filterUsers = (query: string) => { /* ... */ };
  
  // ❌ Trách nhiệm 3: Export file
  const exportToCSV = () => { /* ... */ };
  
  // ❌ Trách nhiệm 4: Render UI (500 dòng JSX!)
  return ( /* ... */ );
};

// ✅ ĐÚNG: Tách thành các trách nhiệm riêng biệt
const UserDashboard = () => {
  // ✅ Custom hook lo data fetching
  const { users, loading } = useUsers();
  
  // ✅ Custom hook lo filter logic
  const { filteredUsers, setFilter } = useUserFilter(users);
  
  // ✅ Custom hook lo export
  const { exportCSV } = useExport(filteredUsers);
  
  // ✅ Component chỉ lo render
  return <UserTable users={filteredUsers} onExport={exportCSV} />;
};

// 💡 LỢI ÍCH:
// - Dễ test (test từng phần riêng)
// - Dễ maintain (sửa filter không ảnh hưởng export)
// - Dễ reuse (dùng useUsers ở component khác)
```

---

## 2. Micro-frontend Architecture

### **2.1. Micro-frontend là gì?**

> **Micro-frontend** là kiến trúc chia nhỏ frontend thành các **autonomous modules** có thể phát triển, deploy, và scale **độc lập**.

### **🎯 Use Cases**

```
✅ Khi nào dùng Micro-frontend:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Team size > 20 developers
2. Multiple independent features (Dashboard, Analytics, Settings)
3. Different tech stacks cần coexist (React + Vue + Angular)
4. Frequent independent deployments
5. Large legacy app cần migrate từng phần

❌ Khi KHÔNG nên dùng:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Small team (< 5 developers)
2. Simple SPA
3. Tight coupling giữa các features
4. Performance critical (overhead của runtime loading)
```

### **2.2. Module Federation Implementation**

```typescript
// ===================================================
// 🏗️ **SHELL APPLICATION** (Container App)
// ===================================================

// webpack.config.js (Shell)
import { ModuleFederationPlugin } from '@module-federation/enhanced';

export default {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        dashboard: 'dashboard@http://localhost:3001/remoteEntry.js',
        profile: 'profile@http://localhost:3002/remoteEntry.js',
        analytics: 'analytics@http://localhost:3003/remoteEntry.js',
      },
      shared: {
        react: { singleton: true, requiredVersion: '^18.3.0' },
        'react-dom': { singleton: true, requiredVersion: '^18.3.0' },
        'react-router-dom': { singleton: true },
      },
    }),
  ],
};

// App.tsx (Shell)
import { lazy, Suspense } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// 🔥 Lazy load remote modules
const Dashboard = lazy(() => import('dashboard/Dashboard'));
const Profile = lazy(() => import('profile/Profile'));
const Analytics = lazy(() => import('analytics/Analytics'));

export const App = () => {
  return (
    <BrowserRouter>
      <ErrorBoundary fallback={<ErrorFallback />}>
        <Header />
        <Suspense fallback={<LoadingSpinner />}>
          <Routes>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/analytics" element={<Analytics />} />
          </Routes>
        </Suspense>
        <Footer />
      </ErrorBoundary>
    </BrowserRouter>
  );
};
```

```typescript
// ===================================================
// 📦 **REMOTE MODULE** (Dashboard App)
// ===================================================

// webpack.config.js (Dashboard Remote)
import { ModuleFederationPlugin } from '@module-federation/enhanced';

export default {
  plugins: [
    new ModuleFederationPlugin({
      name: 'dashboard',
      filename: 'remoteEntry.js',
      exposes: {
        './Dashboard': './src/Dashboard.tsx',
        './Widget': './src/components/Widget.tsx', // Expose individual components
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true },
      },
    }),
  ],
};

// Dashboard.tsx (Exposed Component)
export default function Dashboard() {
  return (
    <div className="dashboard">
      <h1>📊 Dashboard Module</h1>
      <p>Loaded from http://localhost:3001</p>
    </div>
  );
}
```

### **2.3. Communication giữa Micro-frontends**

```typescript
// ===================================================
// 🔗 **SHARED EVENT BUS** (Cross-module Communication)
// ===================================================

// eventBus.ts (Shared Library)
type EventCallback<T = any> = (data: T) => void;

class EventBus {
  private events = new Map<string, Set<EventCallback>>();

  // Subscribe to event
  on<T = any>(event: string, callback: EventCallback<T>) {
    if (!this.events.has(event)) {
      this.events.set(event, new Set());
    }
    this.events.get(event)!.add(callback);

    // Return unsubscribe function
    return () => this.off(event, callback);
  }

  // Unsubscribe
  off<T = any>(event: string, callback: EventCallback<T>) {
    this.events.get(event)?.delete(callback);
  }

  // Emit event
  emit<T = any>(event: string, data?: T) {
    this.events.get(event)?.forEach(callback => callback(data));
  }

  // Clear all listeners
  clear() {
    this.events.clear();
  }
}

export const eventBus = new EventBus();

// ===================================================
// 📡 **USAGE: Cross-module Communication**
// ===================================================

// Dashboard Module (Emitter)
import { eventBus } from '@shared/eventBus';

const Dashboard = () => {
  const handleUserUpdate = (user: User) => {
    // ✅ Emit event to notify other modules
    eventBus.emit('user:updated', user);
  };

  return <button onClick={() => handleUserUpdate(newUser)}>Update User</button>;
};

// Profile Module (Listener)
import { eventBus } from '@shared/eventBus';

const Profile = () => {
  useEffect(() => {
    // ✅ Listen to events from other modules
    const unsubscribe = eventBus.on('user:updated', (user: User) => {
      console.log('🔔 User updated from Dashboard:', user);
      // Update local state
      setCurrentUser(user);
    });

    return () => unsubscribe(); // Cleanup
  }, []);

  return <div>Profile for {currentUser.name}</div>;
};
```

### **2.4. Shared State với Custom Store**

```typescript
// ===================================================
// 🗄️ **SHARED ZUSTAND STORE** (Global State)
// ===================================================

// sharedStore.ts (Shared across all micro-frontends)
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';

interface User {
  id: string;
  name: string;
  email: string;
  role: 'admin' | 'user';
}

interface SharedState {
  user: User | null;
  theme: 'light' | 'dark';
  notifications: Notification[];
  
  // Actions
  setUser: (user: User | null) => void;
  toggleTheme: () => void;
  addNotification: (notification: Notification) => void;
}

export const useSharedStore = create<SharedState>()(
  persist(
    (set, get) => ({
      user: null,
      theme: 'light',
      notifications: [],

      setUser: (user) => set({ user }),
      
      toggleTheme: () => set((state) => ({
        theme: state.theme === 'light' ? 'dark' : 'light',
      })),
      
      addNotification: (notification) => set((state) => ({
        notifications: [...state.notifications, notification],
      })),
    }),
    {
      name: 'shared-storage', // localStorage key
      storage: createJSONStorage(() => localStorage),
    }
  )
);

// ===================================================
// 🎯 **USAGE trong các Micro-frontends**
// ===================================================

// Dashboard Module
import { useSharedStore } from '@shared/store';

const Dashboard = () => {
  const { user, addNotification } = useSharedStore();

  const handleAction = () => {
    addNotification({
      id: crypto.randomUUID(),
      message: 'Data updated from Dashboard!',
      type: 'success',
    });
  };

  return <div>Welcome, {user?.name}!</div>;
};

// Profile Module (cùng state)
import { useSharedStore } from '@shared/store';

const Profile = () => {
  const { user, setUser, theme, toggleTheme } = useSharedStore();

  return (
    <div data-theme={theme}>
      <h1>{user?.name}'s Profile</h1>
      <button onClick={toggleTheme}>Toggle Theme</button>
    </div>
  );
};
```

---

## 3. Monorepo Strategies

### **3.1. Monorepo là gì?**

> **Monorepo** là chiến lược quản lý **multiple projects/packages trong một repository duy nhất** với shared dependencies và tooling.

### **3.2. Nx Monorepo Architecture**

```bash
# Cấu trúc Nx Monorepo
my-workspace/
├── apps/                    # 🎯 Deployable applications
│   ├── web/                 # Main SPA (React + Vite)
│   ├── mobile/              # React Native app
│   ├── admin/               # Admin dashboard
│   └── landing/             # Marketing site (Next.js)
│
├── libs/                    # 📦 Shared libraries
│   ├── shared/
│   │   ├── ui/              # Shared UI components
│   │   │   ├── Button/
│   │   │   ├── Modal/
│   │   │   └── Table/
│   │   ├── utils/           # Utility functions
│   │   ├── types/           # TypeScript types
│   │   └── constants/       # Constants
│   │
│   ├── data-access/         # API clients & data fetching
│   │   ├── auth/
│   │   ├── users/
│   │   └── products/
│   │
│   └── feature/             # Feature modules
│       ├── auth/
│       ├── dashboard/
│       └── profile/
│
├── tools/                   # 🛠️ Custom tooling
│   ├── scripts/
│   └── generators/
│
├── nx.json                  # Nx configuration
├── package.json
└── tsconfig.base.json       # Shared TypeScript config
```

```typescript
// ===================================================
// 📦 **NX PROJECT CONFIGURATION**
// ===================================================

// apps/web/project.json
{
  "name": "web",
  "targets": {
    "build": {
      "executor": "@nx/vite:build",
      "outputs": ["{options.outputPath}"],
      "options": {
        "outputPath": "dist/apps/web"
      }
    },
    "serve": {
      "executor": "@nx/vite:dev-server"
    },
    "test": {
      "executor": "@nx/jest:jest"
    }
  },
  "implicitDependencies": [], // No implicit deps
  "tags": ["type:app", "scope:web"]
}

// libs/shared/ui/project.json
{
  "name": "shared-ui",
  "targets": {
    "build": {
      "executor": "@nx/vite:build",
      "options": {
        "outputPath": "dist/libs/shared/ui"
      }
    }
  },
  "tags": ["type:ui", "scope:shared"]
}
```

```typescript
// ===================================================
// 🏗️ **DEPENDENCY GRAPH & BUILD OPTIMIZATION**
// ===================================================

// nx.json - Task Pipeline Configuration
{
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"], // Build dependencies first
      "cache": true // Cache build results
    },
    "test": {
      "dependsOn": ["build"],
      "cache": true
    }
  },
  "tasksRunnerOptions": {
    "default": {
      "runner": "nx/tasks-runners/default",
      "options": {
        "cacheableOperations": ["build", "test", "lint"],
        "parallel": 3 // Run 3 tasks in parallel
      }
    }
  }
}

// ===================================================
// 🚀 **NX AFFECTED COMMANDS** (Only build what changed)
// ===================================================

// Build only affected apps/libs since last commit
// $ nx affected:build --base=main --head=HEAD

// Test only affected projects
// $ nx affected:test --base=origin/main

// Visualize dependency graph
// $ nx graph
```

```typescript
// ===================================================
// 🔒 **ENFORCE MODULE BOUNDARIES** (Prevent circular deps)
// ===================================================

// .eslintrc.json
{
  "overrides": [
    {
      "files": ["*.ts", "*.tsx"],
      "extends": ["plugin:@nx/typescript"],
      "rules": {
        "@nx/enforce-module-boundaries": [
          "error",
          {
            "allow": [],
            "depConstraints": [
              {
                "sourceTag": "type:app",
                "onlyDependOnLibsWithTags": ["type:feature", "type:ui", "type:util"]
              },
              {
                "sourceTag": "type:feature",
                "onlyDependOnLibsWithTags": ["type:ui", "type:util", "type:data-access"]
              },
              {
                "sourceTag": "type:ui",
                "onlyDependOnLibsWithTags": ["type:util"]
              },
              {
                "sourceTag": "scope:shared",
                "notDependOnLibsWithTags": ["scope:admin", "scope:mobile"]
              }
            ]
          }
        ]
      }
    }
  ]
}
```

### **3.3. Turborepo vs Nx Comparison**

```typescript
// ===================================================
// 🔥 **TURBOREPO** (Vercel's Monorepo Tool)
// ===================================================

// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"], // Build dependencies first
      "outputs": ["dist/**", ".next/**"],
      "cache": true
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": ["coverage/**"],
      "cache": true
    },
    "lint": {
      "cache": true
    },
    "dev": {
      "cache": false,
      "persistent": true // Keep running
    }
  },
  "globalDependencies": ["**/.env.*local"]
}

// Run all builds with cache
// $ turbo run build

// Run only affected (Git-based)
// $ turbo run build --filter=...main

// ===================================================
// 📊 **NX vs TURBOREPO COMPARISON**
// ===================================================
```

| Feature | **Nx** ⭐⭐⭐⭐⭐ | **Turborepo** ⭐⭐⭐⭐ |
|---------|----------------|----------------------|
| **Setup Complexity** | High (opinionated) | Low (minimal config) |
| **Affected Detection** | ✅ Graph-based (accurate) | ⚠️ Git-based (less accurate) |
| **Code Generators** | ✅ Built-in (nx g) | ❌ None |
| **Dependency Graph** | ✅ Interactive UI (`nx graph`) | ⚠️ CLI only |
| **Module Boundaries** | ✅ ESLint rules | ❌ Manual |
| **Cache** | ✅ Local + Remote (Nx Cloud) | ✅ Local + Remote (Vercel) |
| **Performance** | Fast (Smart caching) | Very Fast (Rust-based) |
| **Best For** | Large teams, complex deps | Next.js apps, simplicity |

---

## 4. API Design Patterns

### **4.1. Backend for Frontend (BFF) Pattern**

```typescript
// ===================================================
// 🌐 **BFF LAYER** (API Gateway cho Frontend)
// ===================================================

// bff-server/routes/dashboard.ts
import express from 'express';
import { authMiddleware } from '../middleware/auth';

const router = express.Router();

// ✅ BFF endpoint aggregates data from multiple microservices
router.get('/dashboard', authMiddleware, async (req, res) => {
  try {
    // Parallel requests to multiple services
    const [userProfile, analytics, notifications, recentOrders] = await Promise.all([
      fetch('http://user-service/api/profile').then(r => r.json()),
      fetch('http://analytics-service/api/stats').then(r => r.json()),
      fetch('http://notification-service/api/recent').then(r => r.json()),
      fetch('http://order-service/api/orders?limit=5').then(r => r.json()),
    ]);

    // ✅ Transform data to match frontend requirements
    const dashboardData = {
      user: {
        name: userProfile.firstName + ' ' + userProfile.lastName,
        avatar: userProfile.avatarUrl,
      },
      stats: {
        totalViews: analytics.pageViews,
        conversionRate: analytics.conversions / analytics.visitors,
      },
      notifications: notifications.items.map(n => ({
        id: n.notificationId,
        message: n.content,
        time: new Date(n.timestamp).toLocaleDateString(),
      })),
      recentOrders: recentOrders.data,
    };

    res.json(dashboardData);
  } catch (error) {
    res.status(500).json({ error: 'Failed to fetch dashboard data' });
  }
});

export default router;
```

### **4.2. GraphQL Schema Stitching**

```graphql
# ===================================================
# 🧩 **GRAPHQL SCHEMA** (Type-safe API)
# ===================================================

# schema.graphql
type User {
  id: ID!
  name: String!
  email: String!
  profile: UserProfile
  orders: [Order!]!
  analytics: UserAnalytics
}

type UserProfile {
  avatar: String
  bio: String
  location: String
}

type Order {
  id: ID!
  total: Float!
  status: OrderStatus!
  items: [OrderItem!]!
}

type UserAnalytics {
  totalSpent: Float!
  orderCount: Int!
  averageOrderValue: Float!
}

enum OrderStatus {
  PENDING
  PROCESSING
  SHIPPED
  DELIVERED
  CANCELLED
}

type Query {
  # ✅ Single query fetches all dashboard data
  dashboard: DashboardData!
  user(id: ID!): User
}

type DashboardData {
  user: User!
  stats: UserAnalytics!
  recentOrders: [Order!]!
  notifications: [Notification!]!
}
```

```typescript
// ===================================================
// 🚀 **APOLLO CLIENT SETUP** (Frontend)
// ===================================================

import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client';
import { setContext } from '@apollo/client/link/context';

const httpLink = createHttpLink({
  uri: 'https://api.example.com/graphql',
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem('auth_token');
  return {
    headers: {
      ...headers,
      authorization: token ? `Bearer ${token}` : '',
    },
  };
});

export const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache({
    typePolicies: {
      Query: {
        fields: {
          dashboard: {
            // ✅ Cache dashboard data for 5 minutes
            merge(existing, incoming) {
              return incoming;
            },
          },
        },
      },
    },
  }),
});

// ===================================================
// 📡 **FETCH DASHBOARD DATA** (React Component)
// ===================================================

import { gql, useQuery } from '@apollo/client';

const GET_DASHBOARD = gql`
  query GetDashboard {
    dashboard {
      user {
        id
        name
        email
        profile {
          avatar
        }
      }
      stats {
        totalSpent
        orderCount
        averageOrderValue
      }
      recentOrders {
        id
        total
        status
      }
      notifications {
        id
        message
        createdAt
      }
    }
  }
`;

const Dashboard = () => {
  const { loading, error, data } = useQuery(GET_DASHBOARD, {
    pollInterval: 30000, // Refetch every 30s
  });

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;

  return (
    <div>
      <h1>Welcome, {data.dashboard.user.name}!</h1>
      <Stats stats={data.dashboard.stats} />
      <Orders orders={data.dashboard.recentOrders} />
      <Notifications items={data.dashboard.notifications} />
    </div>
  );
};
```

---

## 5. State Management Architecture

### **5.1. State Management Decision Tree**

```
                     Cần share state?
                            │
            ┌───────────────┴────────────────┐
            │                                │
           NO                               YES
            │                                │
            ▼                                ▼
     ┌──────────────┐              State scope bao nhiêu?
     │ Local State  │                       │
     │ (useState)   │       ┌───────────────┼───────────────┐
     └──────────────┘       │               │               │
                      Component Tree    Few Components  Global App
                            │               │               │
                            ▼               ▼               ▼
                    ┌──────────────┐  ┌──────────┐  ┌──────────────┐
                    │Context API   │  │ Zustand  │  │ Redux Toolkit│
                    │(Light weight)│  │ (Medium) │  │ (Enterprise) │
                    └──────────────┘  └──────────┘  └──────────────┘
                                                            │
                                            Need time-travel debugging?
                                                            │
                                                    ┌───────┴────────┐
                                                   YES              NO
                                                    │                │
                                                    ▼                ▼
                                            Redux DevTools      RTK Query
                                                                (+ caching)
```

### **5.2. Layered State Architecture**

```typescript
// ===================================================
// 🏗️ **3-LAYER STATE ARCHITECTURE**
// ===================================================

// Layer 1: Server State (React Query)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';

const useUsers = () => {
  return useQuery({
    queryKey: ['users'],
    queryFn: async () => {
      const res = await fetch('/api/users');
      return res.json();
    },
    staleTime: 5 * 60 * 1000, // 5 minutes
  });
};

const useUpdateUser = () => {
  const queryClient = useQueryClient();
  
  return useMutation({
    mutationFn: async (user: User) => {
      const res = await fetch(`/api/users/${user.id}`, {
        method: 'PUT',
        body: JSON.stringify(user),
      });
      return res.json();
    },
    onSuccess: () => {
      // ✅ Invalidate & refetch
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });
};

// Layer 2: Global UI State (Zustand)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import { create } from 'zustand';

interface UIState {
  sidebarOpen: boolean;
  theme: 'light' | 'dark';
  notifications: Notification[];
  
  toggleSidebar: () => void;
  setTheme: (theme: 'light' | 'dark') => void;
  addNotification: (notification: Notification) => void;
}

export const useUIStore = create<UIState>((set) => ({
  sidebarOpen: true,
  theme: 'light',
  notifications: [],
  
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
  setTheme: (theme) => set({ theme }),
  addNotification: (notification) => set((state) => ({
    notifications: [...state.notifications, notification],
  })),
}));

// Layer 3: Local Component State (useState)
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
const UserForm = () => {
  const [formData, setFormData] = useState({ name: '', email: '' });
  const [errors, setErrors] = useState<Record<string, string>>({});
  
  const { mutate: updateUser } = useUpdateUser();
  
  const handleSubmit = () => {
    if (validate(formData)) {
      updateUser(formData);
    }
  };
  
  return <form onSubmit={handleSubmit}>{/* ... */}</form>;
};
```

---

## 6. Error Boundaries & Resilience

### **6.1. Error Boundary Implementation**

```typescript
// ===================================================
// 🛡️ **ERROR BOUNDARY COMPONENT**
// ===================================================

import { Component, ReactNode, ErrorInfo } from 'react';
import * as Sentry from '@sentry/react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
  onError?: (error: Error, errorInfo: ErrorInfo) => void;
}

interface State {
  hasError: boolean;
  error: Error | null;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    // ✅ Log to error tracking service
    Sentry.captureException(error, {
      contexts: {
        react: {
          componentStack: errorInfo.componentStack,
        },
      },
    });

    // ✅ Custom error handler
    this.props.onError?.(error, errorInfo);

    // ✅ Log to console in development
    if (process.env.NODE_ENV === 'development') {
      console.error('Error Boundary caught:', error, errorInfo);
    }
  }

  handleReset = () => {
    this.setState({ hasError: false, error: null });
  };

  render() {
    if (this.state.hasError) {
      // ✅ Custom fallback UI
      if (this.props.fallback) {
        return this.props.fallback;
      }

      // ✅ Default error UI
      return (
        <div className="error-boundary">
          <h1>🚨 Something went wrong</h1>
          <details>
            <summary>Error details</summary>
            <pre>{this.state.error?.message}</pre>
            <pre>{this.state.error?.stack}</pre>
          </details>
          <button onClick={this.handleReset}>Try again</button>
          <button onClick={() => window.location.reload()}>Reload page</button>
        </div>
      );
    }

    return this.props.children;
  }
}

// ===================================================
// 🎯 **USAGE: Granular Error Boundaries**
// ===================================================

const App = () => {
  return (
    <ErrorBoundary fallback={<ErrorPage />}>
      <Header />
      
      {/* ✅ Separate error boundary cho từng section */}
      <ErrorBoundary fallback={<SidebarError />}>
        <Sidebar />
      </ErrorBoundary>
      
      <main>
        <ErrorBoundary fallback={<DashboardError />}>
          <Dashboard />
        </ErrorBoundary>
      </main>
      
      <Footer />
    </ErrorBoundary>
  );
};
```

### **6.2. Retry & Circuit Breaker Pattern**

```typescript
// ===================================================
// 🔁 **RETRY MECHANISM với Exponential Backoff**
// ===================================================

interface RetryOptions {
  maxRetries: number;
  initialDelay: number;
  maxDelay: number;
  factor: number;
}

async function fetchWithRetry<T>(
  fn: () => Promise<T>,
  options: RetryOptions = {
    maxRetries: 3,
    initialDelay: 1000,
    maxDelay: 10000,
    factor: 2,
  }
): Promise<T> {
  let lastError: Error;
  
  for (let attempt = 0; attempt <= options.maxRetries; attempt++) {
    try {
      return await fn();
    } catch (error) {
      lastError = error as Error;
      
      if (attempt === options.maxRetries) {
        throw lastError;
      }
      
      // ✅ Exponential backoff: 1s, 2s, 4s, 8s...
      const delay = Math.min(
        options.initialDelay * Math.pow(options.factor, attempt),
        options.maxDelay
      );
      
      console.log(`⏳ Retry attempt ${attempt + 1} after ${delay}ms`);
      await new Promise(resolve => setTimeout(resolve, delay));
    }
  }
  
  throw lastError!;
}

// ===================================================
// ⚡ **CIRCUIT BREAKER PATTERN**
// ===================================================

class CircuitBreaker {
  private failureCount = 0;
  private lastFailureTime?: number;
  private state: 'CLOSED' | 'OPEN' | 'HALF_OPEN' = 'CLOSED';
  
  constructor(
    private threshold: number = 5,
    private timeout: number = 60000 // 1 minute
  ) {}

  async execute<T>(fn: () => Promise<T>): Promise<T> {
    // ✅ OPEN state: Reject immediately
    if (this.state === 'OPEN') {
      if (Date.now() - this.lastFailureTime! < this.timeout) {
        throw new Error('Circuit breaker is OPEN');
      }
      // Try to recover
      this.state = 'HALF_OPEN';
    }

    try {
      const result = await fn();
      this.onSuccess();
      return result;
    } catch (error) {
      this.onFailure();
      throw error;
    }
  }

  private onSuccess() {
    this.failureCount = 0;
    this.state = 'CLOSED';
  }

  private onFailure() {
    this.failureCount++;
    this.lastFailureTime = Date.now();
    
    if (this.failureCount >= this.threshold) {
      this.state = 'OPEN';
      console.warn('🔴 Circuit breaker opened!');
    }
  }

  getState() {
    return this.state;
  }
}

// ===================================================
// 🎯 **USAGE: API Client with Retry & Circuit Breaker**
// ===================================================

const circuitBreaker = new CircuitBreaker(5, 60000);

export async function apiCall<T>(url: string): Promise<T> {
  return circuitBreaker.execute(async () => {
    return fetchWithRetry(async () => {
      const response = await fetch(url);
      
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      
      return response.json();
    });
  });
}
```

---

## 7. Feature Flags System

### **7.1. Feature Flags Architecture**

```typescript
// ===================================================
// 🚩 **FEATURE FLAGS PROVIDER**
// ===================================================

import { createContext, useContext, ReactNode } from 'react';

interface FeatureFlags {
  newDashboard: boolean;
  darkMode: boolean;
  experimentalCharts: boolean;
  aiAssistant: boolean;
}

interface User {
  id: string;
  email: string;
  role: 'admin' | 'user';
  betaTester: boolean;
}

const FeatureFlagsContext = createContext<FeatureFlags>({} as FeatureFlags);

export const FeatureFlagsProvider = ({ children }: { children: ReactNode }) => {
  const user = useCurrentUser();
  
  // ✅ Evaluate flags based on user context
  const flags: FeatureFlags = {
    // Enable for all users
    darkMode: true,
    
    // Enable only for admins
    experimentalCharts: user?.role === 'admin',
    
    // Enable for beta testers
    newDashboard: user?.betaTester || false,
    
    // A/B test: 50% of users
    aiAssistant: hashUserId(user?.id) % 100 < 50,
  };
  
  return (
    <FeatureFlagsContext.Provider value={flags}>
      {children}
    </FeatureFlagsContext.Provider>
  );
};

// ✅ Hook to access feature flags
export const useFeatureFlags = () => useContext(FeatureFlagsContext);

// ✅ Hook to check specific flag
export const useFeatureFlag = (flag: keyof FeatureFlags) => {
  const flags = useFeatureFlags();
  return flags[flag];
};

// ===================================================
// 🎯 **USAGE: Conditional Rendering**
// ===================================================

const Dashboard = () => {
  const { newDashboard, experimentalCharts } = useFeatureFlags();
  
  if (newDashboard) {
    return <NewDashboardV2 />;
  }
  
  return (
    <div>
      <OldDashboard />
      {experimentalCharts && <ExperimentalCharts />}
    </div>
  );
};

// ===================================================
// 🔧 **FEATURE FLAG COMPONENT**
// ===================================================

interface FeatureFlagProps {
  flag: keyof FeatureFlags;
  children: ReactNode;
  fallback?: ReactNode;
}

export const FeatureFlag = ({ flag, children, fallback }: FeatureFlagProps) => {
  const isEnabled = useFeatureFlag(flag);
  
  if (isEnabled) {
    return <>{children}</>;
  }
  
  return <>{fallback}</> || null;
};

// Usage
<FeatureFlag flag="aiAssistant" fallback={<LegacyHelper />}>
  <AIAssistant />
</FeatureFlag>
```

### **7.2. Remote Config với LaunchDarkly**

```typescript
// ===================================================
// ☁️ **LAUNCHDARKLY INTEGRATION**
// ===================================================

import { LDProvider, useLDClient, useFlags } from 'launchdarkly-react-client-sdk';

const LAUNCHDARKLY_CLIENT_ID = 'your-client-id';

export const App = () => {
  return (
    <LDProvider
      clientSideID={LAUNCHDARKLY_CLIENT_ID}
      user={{
        key: currentUser.id,
        email: currentUser.email,
        custom: {
          role: currentUser.role,
          plan: currentUser.plan,
        },
      }}
    >
      <AppContent />
    </LDProvider>
  );
};

const AppContent = () => {
  const flags = useFlags();
  
  return (
    <div>
      {flags.showNewFeature && <NewFeature />}
      {flags.enablePaywall && <PaywallBanner />}
    </div>
  );
};

// ===================================================
// 🎯 **DYNAMIC FLAG UPDATES** (Real-time)
// ===================================================

const FeatureComponent = () => {
  const ldClient = useLDClient();
  
  useEffect(() => {
    // ✅ Listen to flag changes in real-time
    const listener = () => {
      console.log('Feature flag updated!');
      // Re-render component
    };
    
    ldClient?.on('change:showNewFeature', listener);
    
    return () => {
      ldClient?.off('change:showNewFeature', listener);
    };
  }, [ldClient]);
  
  return <div>...</div>;
};
```

---

## 8. CDN & Edge Computing

### **8.1. CloudFlare Workers (Edge Functions)**

```typescript
// ===================================================
// ⚡ **CLOUDFLARE WORKER** (Edge Compute)
// ===================================================

// worker.ts (Runs on CloudFlare edge)
addEventListener('fetch', (event) => {
  event.respondWith(handleRequest(event.request));
});

async function handleRequest(request: Request): Promise<Response> {
  const url = new URL(request.url);
  
  // ✅ A/B Testing at Edge
  if (url.pathname === '/dashboard') {
    const variant = Math.random() < 0.5 ? 'A' : 'B';
    
    // Rewrite URL based on variant
    const targetUrl = variant === 'A'
      ? 'https://cdn.example.com/dashboard-v1.html'
      : 'https://cdn.example.com/dashboard-v2.html';
    
    const response = await fetch(targetUrl);
    
    // Add custom headers
    const newHeaders = new Headers(response.headers);
    newHeaders.set('X-AB-Variant', variant);
    
    return new Response(response.body, {
      status: response.status,
      headers: newHeaders,
    });
  }
  
  // ✅ Geo-based Routing
  const country = request.headers.get('CF-IPCountry');
  
  if (country === 'CN') {
    return fetch('https://cdn-china.example.com' + url.pathname);
  }
  
  // ✅ Default: Origin server
  return fetch(request);
}
```

### **8.2. Static Asset Optimization**

```typescript
// ===================================================
// 📦 **VITE CONFIG** (Build Optimization)
// ===================================================

// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(),
    visualizer({ open: true }), // Bundle analyzer
  ],
  
  build: {
    // ✅ Code splitting
    rollupOptions: {
      output: {
        manualChunks: {
          // Vendor chunks
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'ui-vendor': ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
          'chart-vendor': ['recharts', 'd3'],
          
          // Feature-based chunks
          dashboard: ['./src/features/dashboard'],
          analytics: ['./src/features/analytics'],
        },
      },
    },
    
    // ✅ Minification
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true, // Remove console.log in production
        drop_debugger: true,
      },
    },
    
    // ✅ Asset optimization
    assetsInlineLimit: 4096, // Inline assets < 4KB as base64
    chunkSizeWarningLimit: 500, // Warn if chunk > 500KB
  },
  
  // ✅ CDN base URL
  base: process.env.NODE_ENV === 'production'
    ? 'https://cdn.example.com/'
    : '/',
});
```

```html
<!-- ===================================================
     🚀 **HTML WITH PRELOAD & PREFETCH**
     =================================================== -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  
  <!-- ✅ Preconnect to CDN -->
  <link rel="preconnect" href="https://cdn.example.com" crossorigin>
  <link rel="dns-prefetch" href="https://api.example.com">
  
  <!-- ✅ Preload critical assets -->
  <link rel="preload" href="/fonts/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/critical.css" as="style">
  
  <!-- ✅ Prefetch next page -->
  <link rel="prefetch" href="/dashboard.js">
  
  <!-- ✅ Service Worker registration -->
  <script>
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/sw.js');
    }
  </script>
  
  <title>My App</title>
</head>
<body>
  <div id="root"></div>
  
  <!-- ✅ Defer non-critical scripts -->
  <script src="/analytics.js" defer></script>
  <script src="/main.js" type="module"></script>
</body>
</html>
```

---

## 9. Real-World System Design Questions

### **🎯 Question 1: Design Shopee Homepage (10M DAU)**

```
📋 Requirements:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 10 million daily active users
- Flash sales with 100K concurrent users
- Real-time inventory updates
- Personalized product recommendations
- 99.9% uptime SLA
- < 2s page load time (LCP)

🏗️ Architecture Design:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────┐
│                    USER (Browser)                        │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│              CloudFlare CDN (Edge Caching)               │
│  - Static assets (JS, CSS, Images)                      │
│  - A/B testing at edge                                  │
│  - DDoS protection                                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            Load Balancer (Nginx/HAProxy)                │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┼───────────┐
         │           │           │
         ▼           ▼           ▼
    ┌────────┐  ┌────────┐  ┌────────┐
    │ Next.js│  │ Next.js│  │ Next.js│
    │ Server │  │ Server │  │ Server │
    │  (SSR) │  │  (SSR) │  │  (SSR) │
    └────────┘  └────────┘  └────────┘
         │           │           │
         └───────────┼───────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  BFF Layer (GraphQL)                     │
│  - Data aggregation                                     │
│  - Authentication                                       │
│  - Rate limiting                                        │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┼───────────────────┐
         │           │                   │
         ▼           ▼                   ▼
    ┌────────┐  ┌──────────┐      ┌──────────┐
    │Product │  │Inventory │      │  User    │
    │Service │  │ Service  │      │ Service  │
    │(REST)  │  │(gRPC)    │      │ (REST)   │
    └────────┘  └──────────┘      └──────────┘
         │           │                   │
         ▼           ▼                   ▼
    ┌────────┐  ┌──────────┐      ┌──────────┐
    │MongoDB │  │ Redis    │      │PostgreSQL│
    │        │  │(Inventory│      │          │
    │        │  │ Cache)   │      │          │
    └────────┘  └──────────┘      └──────────┘

🔥 Flash Sale Architecture:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Browser ──▶ WebSocket Server ──▶ Redis Pub/Sub
                     │
                     ▼
              Queue (Kafka/RabbitMQ)
                     │
                     ▼
              Order Processing Workers
                     │
                     ▼
              Database (Write)

📈 Performance Optimizations:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ✅ SSR with ISR (Next.js)
   - Static product pages regenerate every 60s
   - Homepage ISR every 30s

2. ✅ Redis Caching
   - Product catalog: 5 min TTL
   - Flash sale inventory: Real-time

3. ✅ Image Optimization
   - WebP format
   - Lazy loading below fold
   - Responsive images (srcset)

4. ✅ Code Splitting
   - Route-based splitting
   - Component lazy loading

5. ✅ API Rate Limiting
   - 100 req/min per user
   - Burst protection

6. ✅ Database Optimization
   - Read replicas (3x)
   - Connection pooling
   - Indexed queries
```

---

### **🎯 Question 2: Design Google Docs Clone (Real-time Collaboration)**

```typescript
// ===================================================
// 📝 **COLLABORATIVE EDITOR ARCHITECTURE**
// ===================================================

// Real-time Collaboration với Operational Transformation (OT)

import { WebSocket } from 'ws';
import { v4 as uuidv4 } from 'uuid';

interface Operation {
  type: 'insert' | 'delete';
  position: number;
  content?: string;
  userId: string;
  timestamp: number;
}

class CollaborativeDocument {
  private content: string = '';
  private operations: Operation[] = [];
  private clients = new Map<string, WebSocket>();

  // ✅ Apply operation với Operational Transformation
  applyOperation(op: Operation): void {
    switch (op.type) {
      case 'insert':
        this.content =
          this.content.slice(0, op.position) +
          op.content +
          this.content.slice(op.position);
        break;
      case 'delete':
        this.content =
          this.content.slice(0, op.position) +
          this.content.slice(op.position + 1);
        break;
    }
    
    this.operations.push(op);
    
    // ✅ Broadcast to all clients except sender
    this.broadcastOperation(op);
  }

  // ✅ Broadcast to all connected clients
  private broadcastOperation(op: Operation): void {
    const message = JSON.stringify({ type: 'operation', data: op });
    
    this.clients.forEach((client, clientId) => {
      if (clientId !== op.userId && client.readyState === WebSocket.OPEN) {
        client.send(message);
      }
    });
  }

  // ✅ Handle new client connection
  addClient(userId: string, ws: WebSocket): void {
    this.clients.set(userId, ws);
    
    // Send current document state
    ws.send(JSON.stringify({
      type: 'init',
      data: {
        content: this.content,
        operations: this.operations,
      },
    }));
  }

  removeClient(userId: string): void {
    this.clients.delete(userId);
  }
}

// ===================================================
// 🚀 **FRONTEND: React Editor Component**
// ===================================================

import { useEffect, useRef, useState } from 'react';

const CollaborativeEditor = ({ documentId, userId }) => {
  const [content, setContent] = useState('');
  const ws = useRef<WebSocket>();
  
  useEffect(() => {
    // ✅ Connect to WebSocket server
    ws.current = new WebSocket(`wss://api.example.com/docs/${documentId}`);
    
    ws.current.onmessage = (event) => {
      const message = JSON.parse(event.data);
      
      if (message.type === 'init') {
        setContent(message.data.content);
      } else if (message.type === 'operation') {
        // ✅ Apply remote operation
        applyRemoteOperation(message.data);
      }
    };
    
    return () => {
      ws.current?.close();
    };
  }, [documentId]);
  
  const handleTextChange = (newContent: string) => {
    const oldContent = content;
    const operation = generateOperation(oldContent, newContent, userId);
    
    // ✅ Send operation to server
    ws.current?.send(JSON.stringify(operation));
    
    // ✅ Optimistic update
    setContent(newContent);
  };
  
  return (
    <textarea
      value={content}
      onChange={(e) => handleTextChange(e.target.value)}
      placeholder="Start typing..."
    />
  );
};

// 🏗️ Architecture Diagram:
// ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

//     User A                    User B                    User C
//        │                         │                         │
//        │    WebSocket            │   WebSocket             │   WebSocket
//        ▼                         ▼                         ▼
//   ┌─────────────────────────────────────────────────────────────┐
//   │              WebSocket Server (Node.js)                     │
//   │  - Operational Transformation (OT)                          │
//   │  - Conflict resolution                                      │
//   │  - Presence detection                                       │
//   └────────────────────┬────────────────────────────────────────┘
//                        │
//                        ▼
//   ┌─────────────────────────────────────────────────────────────┐
//   │              Redis Pub/Sub                                  │
//   │  - Real-time operation broadcast                            │
//   │  - User presence (who's online)                             │
//   └────────────────────┬────────────────────────────────────────┘
//                        │
//                        ▼
//   ┌─────────────────────────────────────────────────────────────┐
//   │              MongoDB                                         │
//   │  - Document storage                                         │
//   │  - Operation history (CRDT log)                             │
//   │  - Version snapshots (every 100 operations)                 │
//   └─────────────────────────────────────────────────────────────┘
```

---

## 📚 **Tài Liệu Tham Khảo**

### **Books**
- **"System Design Interview"** by Alex Xu (Volume 1 & 2)
- **"Designing Data-Intensive Applications"** by Martin Kleppmann
- **"Web Scalability for Startup Engineers"** by Artur Ejsmont

### **Online Resources**
- **System Design Primer:** https://github.com/donnemartin/system-design-primer
- **Frontend System Design:** https://www.frontendinterviewhandbook.com/system-design
- **Micro-frontend.org:** https://micro-frontends.org/

### **Tools & Frameworks**
- **Nx Monorepo:** https://nx.dev/
- **Turborepo:** https://turbo.build/
- **Module Federation:** https://webpack.js.org/concepts/module-federation/
- **LaunchDarkly:** https://launchdarkly.com/

---

## ✅ **Checklist cho Senior Interview**

```markdown
□ Có thể thiết kế kiến trúc cho 1M+ concurrent users
□ Giải thích trade-offs giữa Micro-frontend vs Monolith
□ Setup Monorepo với Nx/Turborepo cho team 20+ người
□ Implement BFF layer với GraphQL/REST
□ Thiết kế State Management architecture (3 layers)
□ Implement Error Boundary với Sentry integration
□ Setup Feature Flags system (local + remote)
□ Configure CDN với CloudFlare Workers
□ Design real-time collaboration system (WebSocket)
□ Explain caching strategies (Browser, CDN, Server, Database)
```

---

**🎯 Tip:** Trong phỏng vấn Senior, **không chỉ code mà còn phải explain trade-offs, scalability, maintainability**.

**📌 Remember:** "The best architecture is the one that evolves with your team's needs."
