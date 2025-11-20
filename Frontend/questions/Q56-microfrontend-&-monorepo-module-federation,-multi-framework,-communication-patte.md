# 🧱 Q56: Microfrontend & Monorepo - Module Federation, Multi-Framework, Communication Patterns




**❓ Câu Hỏi:**

Giải thích chi tiết kiến trúc Microfrontend và Monorepo, bao gồm Module Federation (Webpack/Vite), Multi-framework development, Communication patterns, Routing strategies, và Styling isolation. Phân tích ưu nhược điểm và ứng dụng thực tế.

**📚 Phần 1: Khái Niệm Cơ Bản (Core Concepts)**

#### **💡 Microfrontend Là Gì? (What is Microfrontend?)**

**Microfrontend** là kiến trúc chia ứng dụng frontend lớn thành **nhiều ứng dụng nhỏ độc lập**, mỗi ứng dụng:
- ✅ Được phát triển bởi **team riêng** (độc lập)
- ✅ Deploy **riêng biệt** (independent deployment)
- ✅ Có **technology stack riêng** (React, Vue, Angular, etc.)
- ✅ **Runtime integration** (ghép nối lúc runtime, không phải build time)

---

#### **🔥 Tại Sao Cần Microfrontend? (Why Microfrontend?)**

**💔 Vấn Đề Của Monolithic Frontend (The Problem):**

```typescript
// ===================================================
// ❌ MONOLITHIC FRONTEND - VÍ DỤ THỰC TẾ
// ===================================================

// Tình huống: Công ty e-commerce lớn với 1 app React khổng lồ

📦 ecommerce-app/
├── src/
│   ├── pages/
│   │   ├── ProductCatalog/      ← Team A maintain (10 devs)
│   │   ├── ShoppingCart/        ← Team B maintain (8 devs)
│   │   ├── Checkout/            ← Team C maintain (12 devs)
│   │   ├── UserProfile/         ← Team D maintain (6 devs)
│   │   ├── OrderHistory/        ← Team E maintain (5 devs)
│   │   └── AdminDashboard/      ← Team F maintain (8 devs)
│   │
│   └── package.json             ← 1 file duy nhất cho tất cả!
│       dependencies: {
│         "react": "17.0.0",     ← Team A muốn upgrade React 18
│         "redux": "4.0.0",      ← Team C muốn dùng Zustand
│         ...500 dependencies    ← Cài đặt CHẬM (5-10 phút!)
│       }
```

**❌ Vấn Đề 1: DEPLOYMENT HELL (Địa Ngục Deploy)**

```
┌──────────────────────────────────────────────────────────┐
│         MONOLITHIC DEPLOYMENT NIGHTMARE                   │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  Team A fix bug nhỏ trong ProductCatalog (1 dòng code)  │
│              ↓                                            │
│  ❌ Phải build TOÀN BỘ app (15-20 phút)                 │
│  ❌ Test TOÀN BỘ app (2-3 giờ)                          │
│  ❌ Deploy TOÀN BỘ app → risk cho tất cả teams!         │
│  ❌ Nếu có bug → TOÀN BỘ app down!                      │
│                                                           │
│  Timeline:                                                │
│  ├─ 10:00 AM: Team A commit fix                         │
│  ├─ 10:20 AM: Build xong (20 phút)                      │
│  ├─ 01:00 PM: QA test xong (2h 40 phút)                 │
│  ├─ 02:00 PM: Deploy production                         │
│  └─ 02:30 PM: Rollback vì bug từ Team C! ❌             │
│                                                           │
│  ⏱️ Tổng: 4.5 giờ cho 1 thay đổi nhỏ!                   │
└──────────────────────────────────────────────────────────┘
```

**❌ Vấn Đề 2: TEAM CONFLICTS (Xung Đột Giữa Teams)**

```typescript
// ❌ Team A: Muốn dùng React 18 + TypeScript strict
// ❌ Team B: Vẫn đang dùng React 17 (legacy code)
// ❌ Team C: Muốn thử Svelte cho performance
// ❌ Team D: Muốn migrate từ Redux → Zustand

// Kết quả: KHÔNG AI ĐƯỢC LÀM GÌ CẢ!
// → Phải họp 6 teams để đồng ý 1 quyết định
// → Mất 2-3 tuần chỉ để quyết định upgrade React
// → Team C không được dùng Svelte → frustrated → nghỉ việc 😢
```

**❌ Vấn Đề 3: SLOW BUILD TIME (Build Chậm)**

```
┌──────────────────────────────────────────────────────────┐
│              BUILD TIME COMPARISON                        │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  MONOLITHIC (1 app lớn):                                 │
│  ├─ npm install: 8-10 phút (500 dependencies)           │
│  ├─ Build: 15-20 phút                                    │
│  ├─ Hot reload: 5-10 giây (chậm!)                       │
│  └─ Dev server start: 2-3 phút                          │
│                                                           │
│  ⏱️ Developer experience: RẤT TỆ!                        │
│  😢 Devs phải đợi 10s mỗi lần save code                  │
└──────────────────────────────────────────────────────────┘
```

**❌ Vấn Đề 4: MERGE CONFLICTS (Xung Đột Merge)**

```bash
# Team A, B, C, D, E, F cùng làm việc trên 1 repo

# Monday morning:
git pull origin main
# ❌ Conflict in package.json (6 teams cùng add dependencies)
# ❌ Conflict in webpack.config.js (3 teams cùng config)
# ❌ Conflict in tsconfig.json (2 teams cùng thay đổi)

# Developer phải mất 30-60 phút giải quyết conflicts TRƯỚC KHI code! 😢
```

**❌ Vấn Đề 5: SINGLE POINT OF FAILURE (Điểm Lỗi Duy Nhất)**

```typescript
// Team C viết code có bug trong Checkout module

function calculateTax(amount: number): number {
  return amount * undefined; // ❌ BUG! Undefined reference
}

// Kết quả:
// ❌ TOÀN BỘ app crash (white screen)! 
// ❌ ProductCatalog của Team A: DOWN ❌
// ❌ ShoppingCart của Team B: DOWN ❌
// ❌ UserProfile của Team D: DOWN ❌
// ❌ AdminDashboard của Team F: DOWN ❌

// 💸 Loss: $100,000/hour vì website down!
```

**❌ Vấn Đề 6: HARD TO SCALE TEAMS (Khó Mở Rộng Team)**

```
┌──────────────────────────────────────────────────────────┐
│         MONOLITHIC TEAM SCALING PROBLEM                   │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  Khi team tăng từ 10 → 50 developers:                   │
│                                                           │
│  ❌ Code review CHẬM (phải review toàn bộ codebase)     │
│  ❌ Merge conflicts tăng theo cấp số nhân                │
│  ❌ Communication overhead (50 devs phải sync)           │
│  ❌ Onboarding mới MẤT 2-3 THÁNG (codebase quá lớn)     │
│  ❌ "Ai viết code này?" → Không ai biết 😅              │
│                                                           │
└──────────────────────────────────────────────────────────┘
```

---

**✅ Microfrontend Giải Quyết Như Thế Nào? (The Solution)**

```typescript
// ===================================================
// ✅ MICROFRONTEND - CÙNG VÍ DỤ NHƯNG ĐƯỢC TỔ CHỨC LẠI
// ===================================================

📦 ecommerce-monorepo/
├── apps/
│   ├── shell/                   ← Team Platform (2 devs)
│   │   └── Deploy: Riêng biệt   ← Build 2 phút, Deploy độc lập
│   │
│   ├── product-catalog/         ← Team A (10 devs)
│   │   ├── package.json         ← React 18 ✅
│   │   └── Deploy: Riêng biệt   ← Build 3 phút, Deploy độc lập
│   │
│   ├── shopping-cart/           ← Team B (8 devs)
│   │   ├── package.json         ← React 17 (legacy) ✅
│   │   └── Deploy: Riêng biệt   ← Build 2 phút, Deploy độc lập
│   │
│   ├── checkout/                ← Team C (12 devs)
│   │   ├── package.json         ← Zustand ✅
│   │   └── Deploy: Riêng biệt   ← Build 4 phút, Deploy độc lập
│   │
│   ├── user-profile/            ← Team D (6 devs)
│   │   ├── package.json         ← Vue 3 ✅ (khác framework!)
│   │   └── Deploy: Riêng biệt   ← Build 2 phút, Deploy độc lập
│   │
│   ├── order-history/           ← Team E (5 devs)
│   │   ├── package.json         ← Angular ✅ (khác framework!)
│   │   └── Deploy: Riêng biệt   ← Build 3 phút, Deploy độc lập
│   │
│   └── admin-dashboard/         ← Team F (8 devs)
│       ├── package.json         ← Svelte ✅ (khác framework!)
│       └── Deploy: Riêng biệt   ← Build 1 phút, Deploy độc lập
```

**✅ Lợi Ích 1: INDEPENDENT DEPLOYMENT (Deploy Độc Lập)**

```
┌──────────────────────────────────────────────────────────┐
│         MICROFRONTEND DEPLOYMENT - HEAVEN!                │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  Team A fix bug trong ProductCatalog (1 dòng code)       │
│              ↓                                            │
│  ✅ Build CHỈ product-catalog app (3 phút)              │
│  ✅ Test CHỈ product-catalog (30 phút)                  │
│  ✅ Deploy CHỈ product-catalog → KHÔNG ảnh hưởng teams khác! │
│  ✅ Nếu có bug → CHỈ product-catalog affected           │
│                                                           │
│  Timeline:                                                │
│  ├─ 10:00 AM: Team A commit fix                         │
│  ├─ 10:03 AM: Build xong (3 phút) ⚡                     │
│  ├─ 10:30 AM: QA test xong (27 phút)                    │
│  └─ 10:35 AM: Deploy production ✅                       │
│                                                           │
│  ⏱️ Tổng: 35 phút cho 1 thay đổi! (vs 4.5 giờ trước)   │
│                                                           │
│  🚀 Team B, C, D, E, F vẫn deploy bình thường!          │
└──────────────────────────────────────────────────────────┘
```

**✅ Lợi Ích 2: TEAM AUTONOMY (Tự Chủ Team)**

```typescript
// ✅ Team A: Dùng React 18 + TypeScript strict ✅
// ✅ Team B: Vẫn dùng React 17 (ko ai care) ✅
// ✅ Team C: Dùng Zustand thay Redux ✅
// ✅ Team D: Dùng Vue 3 ✅
// ✅ Team E: Dùng Angular ✅
// ✅ Team F: Dùng Svelte cho performance ✅

// Kết quả: TẤT CẢ ĐỀU HÀI LÒNG! 🎉
// → Mỗi team tự quyết định tech stack
// → Không cần họp 6 teams
// → Team C được dùng Svelte → happy → stay with company 😊
```

**✅ Lợi Ích 3: FAST BUILD TIME (Build Nhanh)**

```
┌──────────────────────────────────────────────────────────┐
│              BUILD TIME - MICROFRONTEND                   │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  MICROFRONTEND (nhiều apps nhỏ):                         │
│  ├─ npm install: 1-2 phút (50 dependencies mỗi app)     │
│  ├─ Build: 2-4 phút (chỉ build app đang làm)           │
│  ├─ Hot reload: <1 giây ⚡                              │
│  └─ Dev server start: 10-20 giây                        │
│                                                           │
│  ⏱️ Developer experience: TUYỆT VỜI!                     │
│  😊 Devs thấy changes NGAY LẬP TỨC                       │
└──────────────────────────────────────────────────────────┘
```

**✅ Lợi Ích 4: NO MERGE CONFLICTS (Không Xung Đột)**

```bash
# Team A làm việc trên apps/product-catalog/
# Team B làm việc trên apps/shopping-cart/
# Team C làm việc trên apps/checkout/

# Monday morning:
git pull origin main
# ✅ NO CONFLICTS! (Mỗi team làm folder riêng)
# ✅ package.json riêng biệt
# ✅ webpack.config.js riêng biệt

# Developer có thể code NGAY! 🚀
```

**✅ Lợi Ích 5: ISOLATED FAILURES (Lỗi Cô Lập)**

```typescript
// Team C viết code có bug trong Checkout module

function calculateTax(amount: number): number {
  return amount * undefined; // ❌ BUG! Undefined reference
}

// Kết quả với Microfrontend:
// ✅ CHỈ Checkout app crash (có Error Boundary)
// ✅ ProductCatalog của Team A: VẪN HOẠT ĐỘNG ✅
// ✅ ShoppingCart của Team B: VẪN HOẠT ĐỘNG ✅
// ✅ UserProfile của Team D: VẪN HOẠT ĐỘNG ✅
// ✅ AdminDashboard của Team F: VẪN HOẠT ĐỘNG ✅

// 💸 Loss: $10,000/hour (chỉ checkout down, còn lại OK)
// 📉 90% giảm loss so với Monolithic!
```

**✅ Lợi Ích 6: EASY TO SCALE TEAMS (Dễ Mở Rộng)**

```
┌──────────────────────────────────────────────────────────┐
│         MICROFRONTEND TEAM SCALING - SMOOTH               │
├──────────────────────────────────────────────────────────┤
│                                                           │
│  Khi team tăng từ 10 → 50 developers:                   │
│                                                           │
│  ✅ Mỗi team có codebase riêng (dễ review)              │
│  ✅ NO merge conflicts                                   │
│  ✅ Teams làm việc parallel (không chờ đợi)             │
│  ✅ Onboarding MỚI CHỈ 1-2 TUẦN (codebase nhỏ)          │
│  ✅ Team ownership rõ ràng (Team A owns Catalog)        │
│                                                           │
│  🚀 Có thể scale đến 100-200 developers!                │
└──────────────────────────────────────────────────────────┘
```

**✅ Lợi Ích 7: INCREMENTAL MIGRATION (Di Chuyển Từng Bước)**

```typescript
// ===================================================
// 📦 VÍ DỤ: Migrate từ Angular (legacy) → React
// ===================================================

// ❌ MONOLITHIC: Phải rewrite TOÀN BỘ app cùng lúc
// → Mất 1-2 năm, risk CAỰ CAO! 😱

// ✅ MICROFRONTEND: Migrate từng module
// → Mất 3-6 tháng, risk THẤP! 😊

// PLAN:
// ┌─────────────────────────────────────────────┐
// │  Month 1-2: Migrate ProductCatalog → React │
// │  Month 3-4: Migrate ShoppingCart → React   │
// │  Month 5-6: Migrate Checkout → React       │
// │  Month 7-8: Migrate UserProfile → React    │
// └─────────────────────────────────────────────┘

// Trong khi migrate:
// ✅ Angular modules VẪN HOẠT ĐỘNG
// ✅ React modules ĐANG ĐƯỢC PHÁT TRIỂN
// ✅ Users KHÔNG BỊ GIÁN ĐOẠN
```

**✅ Lợi Ích 8: A/B TESTING & FEATURE FLAGS**

```typescript
// ===================================================
// 🧪 A/B TESTING với Microfrontend
// ===================================================

// Shell app quyết định load version nào

function App() {
  const userGroup = useABTest('checkout-v2'); // 50% users
  
  return (
    <div>
      {userGroup === 'A' 
        ? <CheckoutV1 /> // ✅ Version cũ (ổn định)
        : <CheckoutV2 /> // ✅ Version mới (thử nghiệm)
      }
    </div>
  );
}

// ✅ Nếu V2 tốt hơn → Deploy 100% users
// ✅ Nếu V2 có bug → Rollback CHỈ Checkout (không ảnh hưởng apps khác)
```

---

**📊 So Sánh Tổng Quan (Overall Comparison)**

| Tiêu Chí                | Monolithic                  | Microfrontend              |
| ----------------------- | --------------------------- | -------------------------- |
| **Deployment Time**     | 4-6 giờ ❌                  | 30-60 phút ✅              |
| **Build Time**          | 15-20 phút ❌               | 2-4 phút ✅                |
| **Hot Reload**          | 5-10 giây ❌                | <1 giây ✅                 |
| **Team Conflicts**      | Cao (merge hell) ❌         | Thấp (isolated) ✅         |
| **Tech Stack**          | 1 stack cho tất cả ❌       | Mỗi team tự chọn ✅        |
| **Risk khi Deploy**     | Cao (toàn bộ app) ❌        | Thấp (1 module) ✅         |
| **Failure Impact**      | Toàn bộ app down ❌         | 1 module down ✅           |
| **Team Scalability**    | Khó (>20 devs) ❌           | Dễ (100+ devs) ✅          |
| **Onboarding Time**     | 2-3 tháng ❌                | 1-2 tuần ✅                |
| **Migration**           | Big bang (risk cao) ❌      | Incremental (risk thấp) ✅ |
| **A/B Testing**         | Khó ❌                      | Dễ ✅                      |
| **Bundle Size**         | Lớn (load tất cả) ❌        | Nhỏ (lazy load) ✅         |

---

**🎯 Khi Nào NÊN Dùng Microfrontend?**

✅ **NÊN dùng khi:**
- ✅ Team > 20 developers
- ✅ App có nhiều domains khác nhau (catalog, cart, checkout, profile, admin)
- ✅ Muốn deploy độc lập từng phần
- ✅ Muốn dùng nhiều tech stack (React + Vue + Angular)
- ✅ Legacy migration (Angular → React từng bước)
- ✅ Cần A/B testing nhiều

❌ **KHÔNG NÊN dùng khi:**
- ❌ Team < 10 developers (overhead lớn)
- ❌ App đơn giản (1-2 pages)
- ❌ Không cần deploy độc lập
- ❌ Chỉ dùng 1 framework
- ❌ Startup giai đoạn đầu (chưa cần scale)

---

**💡 Real-World Examples (Ví Dụ Thực Tế)**

```
🏢 **Spotify**: 
   - Home, Search, Playlist, Player là các micro apps riêng
   - Deploy riêng biệt 50+ lần/ngày
   - Teams độc lập (Squad model)

🏢 **Zalando**: 
   - Product listing, Cart, Checkout, Account là micro apps
   - 200+ developers làm việc parallel
   - Tech stack: React, Vue, Angular cùng tồn tại

🏢 **IKEA**: 
   - Migrate từ .NET → React incrementally
   - 10+ micro apps độc lập
   - Giảm deployment time từ 6 giờ → 30 phút

🏢 **Amazon**: 
   - Mỗi product category là 1 micro app
   - 1000+ developers
   - Deploy hàng trăm lần/ngày
```

---

```
┌─────────────────────────────────────────────────────────┐
│                  MONOLITHIC FRONTEND                     │
│                  (Kiến trúc cũ - 1 khối)                │
├─────────────────────────────────────────────────────────┤
│                                                          │
│   ┌──────────────────────────────────────────────┐      │
│   │         Entire App (React)                   │      │
│   │  ┌──────────┬──────────┬──────────────┐     │      │
│   │  │  Header  │Dashboard │   Profile    │     │      │
│   │  └──────────┴──────────┴──────────────┘     │      │
│   │                                              │      │
│   │  - 1 codebase                               │      │
│   │  - 1 deployment                             │      │
│   │  - 1 team phải maintain tất cả              │      │
│   │  - Deploy tất cả mỗi lần thay đổi nhỏ      │      │
│   └──────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────┘

                          ↓ CHUYỂN ĐỔI

┌─────────────────────────────────────────────────────────┐
│              MICROFRONTEND ARCHITECTURE                  │
│              (Kiến trúc mới - Nhiều khối nhỏ)           │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  ┌────────────────┐  ┌────────────────┐                │
│  │  Shell App     │  │  Remote Apps   │                │
│  │  (Host/Container)│ │  (Micro Apps) │                │
│  └────────────────┘  └────────────────┘                │
│                                                          │
│  ┌─────────────────────────────────────────────┐        │
│  │           Shell (React) - Team Platform     │        │
│  │  ┌──────────────────────────────────────┐   │        │
│  │  │         Shared Header/Footer          │   │        │
│  │  └──────────────────────────────────────┘   │        │
│  │                                              │        │
│  │  ┌─────────┐  ┌──────────┐  ┌──────────┐  │        │
│  │  │Dashboard│  │ Profile  │  │  Orders  │  │        │
│  │  │ (React) │  │  (Vue)   │  │(Angular) │  │        │
│  │  │ Team A  │  │  Team B  │  │  Team C  │  │        │
│  │  └─────────┘  └──────────┘  └──────────┘  │        │
│  │                                              │        │
│  │  - 3 teams độc lập                          │        │
│  │  - Deploy riêng biệt                        │        │
│  │  - Tech stack khác nhau                     │        │
│  │  - Module Federation ghép nối runtime       │        │
│  └─────────────────────────────────────────────┘        │
└─────────────────────────────────────────────────────────┘
```

#### **💡 Monorepo Là Gì? (What is Monorepo?)**

**Monorepo** là cách quản lý code: **nhiều projects/packages** trong **1 repository duy nhất**.

```
📦 monorepo-root/
├── 📁 apps/                    ← Các ứng dụng (applications)
│   ├── 📁 shell/               ← Shell/Host app (React)
│   │   ├── src/
│   │   ├── package.json
│   │   └── webpack.config.js
│   │
│   ├── 📁 dashboard/           ← Dashboard app (React)
│   │   ├── src/
│   │   └── package.json
│   │
│   └── 📁 profile/             ← Profile app (Vue)
│       ├── src/
│       └── package.json
│
├── 📁 libs/                    ← Shared libraries (thư viện dùng chung)
│   ├── 📁 shared-ui/           ← UI components (Button, Input, etc.)
│   ├── 📁 shared-auth/         ← Auth logic (login, logout, etc.)
│   └── 📁 shared-utils/        ← Utils (date, string, etc.)
│
├── package.json                ← Root package.json
├── nx.json                     ← Nx workspace config
└── tsconfig.base.json          ← Shared TypeScript config
```

**🔥 Ưu Điểm Monorepo:**
- ✅ **Code sharing dễ dàng**: Import libs giữa các apps
- ✅ **Atomic commits**: 1 commit thay đổi nhiều apps
- ✅ **Consistent tooling**: Cùng ESLint, Prettier, TypeScript config
- ✅ **Dependency management**: 1 `package.json` root cho tất cả

---

**📚 Phần 2: Module Federation - Runtime Code Sharing**

#### **💡 Module Federation Là Gì?**

**Module Federation** (Webpack 5 / Vite Federation) là kỹ thuật cho phép **chia sẻ code giữa các apps ở runtime** (không phải build time).

**🔥 Cơ Chế Hoạt Động:**

```typescript
// ===================================================
// 🏠 SHELL APP (Host - React) - webpack.config.js
// ===================================================
// Đây là app chính, load các remote apps vào

const ModuleFederationPlugin = require('webpack/lib/container/ModuleFederationPlugin');

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell', // ⚠️ Tên app này
      
      // 📥 REMOTES: Các app remote mà shell sẽ load
      remotes: {
        // Key: tên import, Value: URL + scope name
        dashboard: 'dashboard@http://localhost:3001/remoteEntry.js', // Dashboard app (React)
        profile: 'profile@http://localhost:3002/remoteEntry.js',     // Profile app (Vue)
      },
      
      // 📤 EXPOSES: Những gì shell chia sẻ cho remote apps
      exposes: {
        './Header': './src/components/Header',     // Share Header component
        './AuthService': './src/services/AuthService', // Share Auth service
      },
      
      // 🔄 SHARED: Dependencies dùng chung (tránh duplicate)
      shared: {
        react: { 
          singleton: true,        // ⚠️ Chỉ có 1 instance React trong toàn bộ app
          requiredVersion: '^18.0.0', // Version yêu cầu
          eager: true             // Load ngay lập tức (không lazy)
        },
        'react-dom': { singleton: true, eager: true },
      },
    }),
  ],
};

// ===================================================
// 📊 DASHBOARD APP (Remote - React) - webpack.config.js
// ===================================================
// App độc lập, expose components cho shell

module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'dashboard', // ⚠️ Tên app này (phải trùng với remotes ở shell)
      filename: 'remoteEntry.js', // ⚠️ File entry point
      
      // 📤 EXPOSES: Components/modules mà dashboard chia sẻ
      exposes: {
        './DashboardPage': './src/pages/DashboardPage',     // Main page
        './StatsWidget': './src/components/StatsWidget',    // Widget component
      },
      
      // 🔄 SHARED: Dependencies dùng chung với shell
      shared: {
        react: { singleton: true, requiredVersion: '^18.0.0' },
        'react-dom': { singleton: true },
      },
    }),
  ],
};

// ===================================================
// 👤 PROFILE APP (Remote - Vue 3) - vite.config.ts
// ===================================================
// App Vue, expose components cho shell (Multi-framework!)

import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import federation from '@originjs/vite-plugin-federation';

export default defineConfig({
  plugins: [
    vue(),
    federation({
      name: 'profile', // ⚠️ Tên app
      filename: 'remoteEntry.js',
      
      // 📤 EXPOSES: Vue components
      exposes: {
        './ProfilePage': './src/pages/ProfilePage.vue',    // Vue component
        './UserAvatar': './src/components/UserAvatar.vue', // Vue component
      },
      
      // 🔄 SHARED: Vue dependencies
      shared: {
        vue: { singleton: true },
      },
    }),
  ],
});
```

#### **🎯 Sử Dụng Remote Components trong Shell**

```typescript
// ===================================================
// 🏠 SHELL APP - src/App.tsx (React)
// ===================================================

import React, { Suspense, lazy } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

// 📥 LAZY LOAD remote components từ dashboard (React)
const DashboardPage = lazy(() => import('dashboard/DashboardPage'));
//                                       ↑         ↑
//                              remote name    exposed module

// 📥 LAZY LOAD remote components từ profile (Vue)
const ProfilePage = lazy(() => import('profile/ProfilePage'));

function App() {
  return (
    <BrowserRouter>
      <div className="app">
        <Header /> {/* Shell's own component */}
        
        <Suspense fallback={<div>Loading...</div>}>
          <Routes>
            {/* Dashboard app (React) - Team A */}
            <Route path="/dashboard" element={<DashboardPage />} />
            
            {/* Profile app (Vue) - Team B */}
            <Route path="/profile" element={<ProfilePage />} />
          </Routes>
        </Suspense>
      </div>
    </BrowserRouter>
  );
}

export default App;

// ⚠️ TypeScript types cho remote modules
// src/types/remotes.d.ts
declare module 'dashboard/DashboardPage' {
  const DashboardPage: React.ComponentType;
  export default DashboardPage;
}

declare module 'profile/ProfilePage' {
  const ProfilePage: React.ComponentType;
  export default ProfilePage;
}
```

**🔥 Timeline Hoạt Động:**

```
User truy cập http://localhost:3000/dashboard

1️⃣ Shell app load (React)
   └─ Load shell bundle (~500KB)
   └─ Render Header, Sidebar

2️⃣ User click "Dashboard" → Route change
   └─ React Router match /dashboard
   └─ Trigger lazy(() => import('dashboard/DashboardPage'))

3️⃣ Module Federation fetch remote
   └─ Fetch http://localhost:3001/remoteEntry.js
   └─ Parse manifest (biết dashboard expose gì)
   └─ Fetch dashboard chunk (~300KB)

4️⃣ Dashboard component render
   └─ Dùng shared React instance từ shell (không duplicate)
   └─ Render DashboardPage component

Total: Shell (500KB) + Dashboard (300KB) = 800KB
✅ Nếu KHÔNG dùng Module Federation: 500KB + 500KB = 1MB (duplicate React)
```

---

**📚 Phần 3: Multi-Framework Development (Phát Triển Đa Framework)**

#### **💡 Tại Sao Cần Multi-Framework?**

- ✅ **Legacy migration**: Migrate từ Angular → React từng phần
- ✅ **Team autonomy**: Team A dùng React, Team B dùng Vue
- ✅ **Best tool for the job**: Dashboard dùng React, Charts dùng Svelte

#### **🔥 Cách Hoạt Động:**

```typescript
// ===================================================
// 🏠 SHELL (React) load PROFILE (Vue)
// ===================================================

// Shell App (React) - src/App.tsx
import React, { Suspense, lazy, useEffect, useRef } from 'react';

// ❌ KHÔNG THỂ: Import Vue component trực tiếp vào React
// import ProfilePage from './ProfilePage.vue'; // ❌ Lỗi!

// ✅ GIẢI PHÁP 1: Module Federation + Wrapper
const ProfilePage = lazy(() => import('profile/ProfilePage'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <ProfilePage /> {/* Vue component trong React! */}
    </Suspense>
  );
}

// ===================================================
// 👤 PROFILE APP (Vue) - src/pages/ProfilePage.vue
// ===================================================

<template>
  <div class="profile-page">
    <h1>{{ user.name }}</h1>
    <p>{{ user.email }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';

const user = ref({ name: '', email: '' });

onMounted(async () => {
  // Fetch user data
  const response = await fetch('/api/user');
  user.value = await response.json();
});
</script>

// ===================================================
// 🔧 PROFILE APP - Wrapper để React hiểu Vue component
// ===================================================

// profile/src/bootstrap.tsx
import { createApp } from 'vue';
import ProfilePage from './pages/ProfilePage.vue';

// Export function để mount Vue app vào DOM element
export function mountProfilePage(el: HTMLElement) {
  const app = createApp(ProfilePage);
  app.mount(el);
  
  // Return cleanup function
  return () => app.unmount();
}

// profile/src/VueWrapper.tsx (React wrapper for Vue)
import React, { useEffect, useRef } from 'react';
import { mountProfilePage } from './bootstrap';

export default function VueWrapper() {
  const ref = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    if (ref.current) {
      const cleanup = mountProfilePage(ref.current); // Mount Vue app
      
      return () => cleanup(); // Unmount khi component unmount
    }
  }, []);
  
  return <div ref={ref}></div>; // Vue app sẽ render vào div này
}
```

**🎯 Framework Compatibility Matrix:**

| Shell ↓ / Remote → | React         | Vue          | Angular      | Svelte       |
| ------------------ | ------------- | ------------ | ------------ | ------------ |
| **React**          | ✅ Native     | ✅ Wrapper   | ✅ Wrapper   | ✅ Wrapper   |
| **Vue**            | ✅ Wrapper    | ✅ Native    | ✅ Wrapper   | ✅ Wrapper   |
| **Angular**        | ✅ Wrapper    | ✅ Wrapper   | ✅ Native    | ✅ Wrapper   |
| **Svelte**         | ✅ Wrapper    | ✅ Wrapper   | ✅ Wrapper   | ✅ Native    |

---

**📚 Phần 4: Communication Patterns (Mẫu Giao Tiếp)**

Các Micro apps cần giao tiếp với nhau (share data, trigger actions). Có 3 patterns chính:

#### **🔥 Pattern 1: Event Bus (Custom Events)**

```typescript
// ===================================================
// 📡 EVENT BUS - libs/shared-communication/EventBus.ts
// ===================================================

// Simple EventEmitter pattern
class EventBus {
  private events: Map<string, Array<(...args: any[]) => void>> = new Map();
  
  // Đăng ký lắng nghe event
  on(event: string, callback: (...args: any[]) => void): void {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    this.events.get(event)!.push(callback);
  }
  
  // Hủy lắng nghe event
  off(event: string, callback: (...args: any[]) => void): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      const index = callbacks.indexOf(callback);
      if (index > -1) callbacks.splice(index, 1);
    }
  }
  
  // Phát event
  emit(event: string, ...args: any[]): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.forEach(callback => callback(...args));
    }
  }
}

// Singleton instance - dùng chung toàn bộ apps
export const eventBus = new EventBus();

// ===================================================
// 🏠 SHELL APP - Listen to events
// ===================================================

import { eventBus } from '@myorg/shared-communication';
import { useEffect } from 'react';

function Shell() {
  useEffect(() => {
    // Lắng nghe event "user-login" từ bất kỳ app nào
    const handleLogin = (user: { name: string; email: string }) => {
      console.log('User logged in:', user);
      // Update shell state, show notification, etc.
    };
    
    eventBus.on('user-login', handleLogin);
    
    // Cleanup khi unmount
    return () => eventBus.off('user-login', handleLogin);
  }, []);
  
  return <div>Shell App</div>;
}

// ===================================================
// 📊 DASHBOARD APP - Emit events
// ===================================================

import { eventBus } from '@myorg/shared-communication';

function LoginButton() {
  const handleLogin = async () => {
    const user = await loginAPI();
    
    // Phát event "user-login" cho tất cả apps lắng nghe
    eventBus.emit('user-login', user);
  };
  
  return <button onClick={handleLogin}>Login</button>;
}
```

**✅ Ưu điểm Event Bus:**
- ✅ Decoupled (apps không cần biết nhau)
- ✅ Dễ implement
- ✅ Multi-framework compatible

**❌ Nhược điểm:**
- ❌ Khó debug (không biết ai emit, ai listen)
- ❌ No type safety (TypeScript không check được)
- ❌ Memory leaks nếu quên `off()`

#### **🔥 Pattern 2: Shared State (Redux/Zustand)**

```typescript
// ===================================================
// 🗃️ SHARED STATE - libs/shared-state/store.ts
// ===================================================

import { create } from 'zustand';

// Zustand store - đơn giản hơn Redux
interface AppState {
  user: { name: string; email: string } | null;
  theme: 'light' | 'dark';
  
  // Actions
  setUser: (user: AppState['user']) => void;
  setTheme: (theme: AppState['theme']) => void;
}

export const useAppStore = create<AppState>((set) => ({
  user: null,
  theme: 'light',
  
  setUser: (user) => set({ user }),
  setTheme: (theme) => set({ theme }),
}));

// ===================================================
// 🏠 SHELL APP - Read/Write shared state
// ===================================================

import { useAppStore } from '@myorg/shared-state';

function Header() {
  const user = useAppStore((state) => state.user);    // Subscribe to user
  const setUser = useAppStore((state) => state.setUser);
  
  const handleLogin = async () => {
    const user = await loginAPI();
    setUser(user); // ⚠️ Tất cả apps subscribe sẽ update!
  };
  
  return (
    <header>
      {user ? `Hello ${user.name}` : 'Not logged in'}
      <button onClick={handleLogin}>Login</button>
    </header>
  );
}

// ===================================================
// 📊 DASHBOARD APP - Read shared state
// ===================================================

import { useAppStore } from '@myorg/shared-state';

function DashboardPage() {
  const user = useAppStore((state) => state.user); // Auto update khi user thay đổi
  
  if (!user) return <div>Please login</div>;
  
  return <div>Welcome {user.name}!</div>;
}
```

**✅ Ưu điểm Shared State:**
- ✅ Type safe (TypeScript)
- ✅ Predictable (1 source of truth)
- ✅ Dễ debug (DevTools)

**❌ Nhược điểm:**
- ❌ Tightly coupled (apps phụ thuộc vào shared state)
- ❌ Phức tạp hơn Event Bus

#### **🔥 Pattern 3: Props/Callbacks (Parent → Child)**

```typescript
// ===================================================
// 🏠 SHELL APP - Pass props to remote apps
// ===================================================

function App() {
  const [user, setUser] = useState(null);
  
  return (
    <div>
      {/* Pass props xuống Dashboard remote */}
      <DashboardPage 
        user={user}                    // ⚠️ Data flow: Shell → Dashboard
        onLogout={() => setUser(null)} // ⚠️ Callback: Dashboard → Shell
      />
    </div>
  );
}
```

**🎯 Khi Nào Dùng Pattern Nào?**

| Pattern             | Use Case                                       | Coupling   |
| ------------------- | ---------------------------------------------- | ---------- |
| **Event Bus**       | Loosely coupled events (login, logout, notify) | Loose ✅   |
| **Shared State**    | Global state (user, theme, cart)               | Medium ⚠️  |
| **Props/Callbacks** | Parent-child communication                     | Tight ❌   |

---

**📚 Phần 5: Routing Strategies (Chiến Lược Định Tuyến)**

#### **💡 Problem: Ai Quản Lý Routes?**

Với Microfrontend, routing có 2 chiến lược:

#### **🔥 Strategy 1: Shell-based Routing (Shell quản lý tất cả routes)**

```typescript
// ===================================================
// 🏠 SHELL APP - Quản lý tất cả routes
// ===================================================

import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { lazy, Suspense } from 'react';

// Lazy load remote apps
const DashboardPage = lazy(() => import('dashboard/DashboardPage'));
const ProfilePage = lazy(() => import('profile/ProfilePage'));
const OrdersPage = lazy(() => import('orders/OrdersPage'));

function App() {
  return (
    <BrowserRouter>
      <Header />
      <Suspense fallback={<div>Loading...</div>}>
        <Routes>
          {/* Shell routes */}
          <Route path="/" element={<HomePage />} />
          
          {/* Dashboard routes - SHELL quyết định */}
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/dashboard/stats" element={<DashboardPage />} />
          
          {/* Profile routes - SHELL quyết định */}
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/profile/settings" element={<ProfilePage />} />
          
          {/* Orders routes - SHELL quyết định */}
          <Route path="/orders" element={<OrdersPage />} />
          <Route path="/orders/:id" element={<OrdersPage />} />
        </Routes>
      </Suspense>
    </BrowserRouter>
  );
}
```

**✅ Ưu điểm:**
- ✅ Centralized routing (1 nơi quản lý tất cả)
- ✅ Dễ setup, dễ hiểu
- ✅ Shell control navigation flow

**❌ Nhược điểm:**
- ❌ Remote apps không autonomous (phụ thuộc shell)
- ❌ Shell phải biết tất cả routes của remotes

#### **🔥 Strategy 2: Distributed Routing (Mỗi app tự quản lý routes)**

```typescript
// ===================================================
// 🏠 SHELL APP - Chỉ route top-level
// ===================================================

import { BrowserRouter, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        {/* Shell chỉ route /dashboard/*, còn lại để Dashboard tự handle */}
        <Route path="/dashboard/*" element={<DashboardApp />} />
        
        {/* Profile tự handle /profile/* */}
        <Route path="/profile/*" element={<ProfileApp />} />
      </Routes>
    </BrowserRouter>
  );
}

// ===================================================
// 📊 DASHBOARD APP - Tự quản lý routes con
// ===================================================

import { Routes, Route } from 'react-router-dom';

function DashboardApp() {
  return (
    <Routes>
      {/* /dashboard → /dashboard (trang chính) */}
      <Route path="/" element={<DashboardHome />} />
      
      {/* /dashboard/stats */}
      <Route path="/stats" element={<StatsPage />} />
      
      {/* /dashboard/reports */}
      <Route path="/reports" element={<ReportsPage />} />
    </Routes>
  );
}
```

**✅ Ưu điểm:**
- ✅ Autonomous apps (mỗi app tự quản lý routes)
- ✅ Shell không cần biết routes của remotes

**❌ Nhược điểm:**
- ❌ Phức tạp hơn
- ❌ Có thể conflict routes giữa apps

---

**📚 Phần 6: Styling Isolation (Cô Lập CSS)**

#### **💡 Problem: CSS Conflicts Giữa Các Apps**

```css
/* Dashboard App - styles.css */
.header { background: red; }      /* ❌ Class name chung */

/* Profile App - styles.css */
.header { background: blue; }     /* ❌ Conflict! */

/* Kết quả: Header màu gì? Tùy thuộc CSS nào load sau! */
```

#### **🔥 Solution 1: CSS Modules**

```typescript
// ===================================================
// 📊 DASHBOARD APP - DashboardHeader.module.css
// ===================================================

/* File: DashboardHeader.module.css */
.header {
  background: red;
  padding: 20px;
}

.title {
  font-size: 24px;
}

// ===================================================
// 📊 DASHBOARD APP - DashboardHeader.tsx
// ===================================================

import styles from './DashboardHeader.module.css';

function DashboardHeader() {
  return (
    <header className={styles.header}> {/* ✅ className = "DashboardHeader_header__abc123" */}
      <h1 className={styles.title}>Dashboard</h1>
    </header>
  );
}

// Output HTML:
// <header class="DashboardHeader_header__abc123">
//   <h1 class="DashboardHeader_title__def456">Dashboard</h1>
// </header>
```

**✅ Ưu điểm CSS Modules:**
- ✅ Scoped styles (không conflict)
- ✅ Build-time transformation

**❌ Nhược điểm:**
- ❌ Không dùng được global styles dễ dàng

#### **🔥 Solution 2: CSS-in-JS (Styled Components, Emotion)**

```typescript
// ===================================================
// 📊 DASHBOARD APP - Styled Components
// ===================================================

import styled from 'styled-components';

// ✅ Styles scoped to component, auto-generate unique class names
const Header = styled.header`
  background: red;
  padding: 20px;
  
  h1 {
    font-size: 24px;
  }
`;

function DashboardHeader() {
  return (
    <Header>
      <h1>Dashboard</h1>
    </Header>
  );
}

// Output HTML:
// <header class="sc-bdnxRM jZQkXY">  ← Unique class name
//   <h1>Dashboard</h1>
// </header>
```

**✅ Ưu điểm CSS-in-JS:**
- ✅ Scoped styles
- ✅ Dynamic styles (props-based)
- ✅ No CSS files

**❌ Nhược điểm:**
- ❌ Runtime overhead
- ❌ Larger bundle size

#### **🔥 Solution 3: Shadow DOM**

```typescript
// ===================================================
// 📊 DASHBOARD APP - Shadow DOM (Web Components)
// ===================================================

class DashboardHeader extends HTMLElement {
  connectedCallback() {
    // Tạo Shadow DOM - HOÀN TOÀN CÔ LẬP!
    const shadow = this.attachShadow({ mode: 'open' });
    
    shadow.innerHTML = `
      <style>
        /* ✅ CSS này CHỈ apply trong Shadow DOM, KHÔNG leak ra ngoài */
        .header {
          background: red;
          padding: 20px;
        }
      </style>
      
      <header class="header">
        <h1>Dashboard</h1>
      </header>
    `;
  }
}

customElements.define('dashboard-header', DashboardHeader);

// Usage: <dashboard-header></dashboard-header>
```

**✅ Ưu điểm Shadow DOM:**
- ✅ TRUE isolation (100% không conflict)
- ✅ Native browser API

**❌ Nhược điểm:**
- ❌ Khó style từ bên ngoài
- ❌ Không dùng được với React/Vue components

#### **🔥 Solution 4: Prefix/Namespace**

```css
/* ===================================================
   📊 DASHBOARD APP - Prefix tất cả classes
   =================================================== */

/* dashboard-styles.css */
.dashboard-header { background: red; }      /* ✅ Prefix "dashboard-" */
.dashboard-title { font-size: 24px; }

/* ===================================================
   👤 PROFILE APP - Prefix khác
   =================================================== */

/* profile-styles.css */
.profile-header { background: blue; }       /* ✅ Prefix "profile-" */
.profile-title { font-size: 20px; }

/* ✅ Không conflict vì tên classes khác nhau */
```

**🎯 Styling Strategy Comparison:**

| Strategy            | Isolation | Performance | DX (Developer Experience) | Use Case           |
| ------------------- | --------- | ----------- | ------------------------- | ------------------ |
| **CSS Modules**     | ⭐⭐⭐⭐    | ⭐⭐⭐⭐⭐     | ⭐⭐⭐⭐                      | Default choice     |
| **CSS-in-JS**       | ⭐⭐⭐⭐⭐   | ⭐⭐⭐        | ⭐⭐⭐⭐⭐                    | Dynamic styles     |
| **Shadow DOM**      | ⭐⭐⭐⭐⭐   | ⭐⭐⭐⭐⭐     | ⭐⭐⭐                       | Web Components     |
| **Prefix/Namespace**| ⭐⭐⭐      | ⭐⭐⭐⭐⭐     | ⭐⭐                         | Simple projects    |

---

**📚 Phần 7: Nx Monorepo Setup (Thực Hành)**

```bash
# ===================================================
# 🚀 Tạo Nx Monorepo với Microfrontend
# ===================================================

# 1️⃣ Tạo workspace
npx create-nx-workspace@latest myorg --preset=react-monorepo

# 2️⃣ Tạo Shell app (Host)
nx g @nx/react:app shell

# 3️⃣ Tạo Remote apps
nx g @nx/react:app dashboard
nx g @nx/react:app profile

# 4️⃣ Tạo Shared library
nx g @nx/react:lib shared-ui
nx g @nx/js:lib shared-communication

# 5️⃣ Configure Module Federation
nx g @nx/react:setup-mf shell --mfType=host
nx g @nx/react:setup-mf dashboard --mfType=remote --host=shell
nx g @nx/react:setup-mf profile --mfType=remote --host=shell

# 6️⃣ Serve tất cả apps
nx serve shell  # http://localhost:4200 (auto serve remotes)

# 📊 Kết quả cấu trúc:
# myorg/
# ├── apps/
# │   ├── shell/              ← Host app (React)
# │   ├── dashboard/          ← Remote app (React)
# │   └── profile/            ← Remote app (React)
# ├── libs/
# │   ├── shared-ui/          ← Shared components
# │   └── shared-communication/ ← Event Bus, Shared State
# └── nx.json
```

---

**✅ Best Practices (Thực Hành Tốt Nhất)**

#### **🔥 1. Dependency Management**

```json
// ❌ SAI: Mỗi app có version React khác nhau
{
  "shell": { "react": "18.0.0" },
  "dashboard": { "react": "17.0.0" },  // ❌ Conflict!
  "profile": { "react": "18.2.0" }      // ❌ Duplicate bundles!
}

// ✅ ĐÚNG: Shared dependencies ở root
// package.json (root)
{
  "dependencies": {
    "react": "18.2.0",        // ✅ Tất cả apps dùng chung version
    "react-dom": "18.2.0"
  }
}
```

#### **🔥 2. Versioning Strategy**

```bash
# Semantic Versioning cho remote apps
dashboard@1.2.3
          │ │ └─ PATCH: Bug fixes (backward compatible)
          │ └─── MINOR: New features (backward compatible)
          └───── MAJOR: Breaking changes (NOT backward compatible)

# Shell compatibility matrix
shell@2.0.0 → dashboard@^1.0.0 (✅ Compatible với 1.x.x)
            → profile@^2.0.0
```

#### **🔥 3. Error Boundaries**

```typescript
// ===================================================
// 🏠 SHELL APP - Error Boundary cho remote apps
// ===================================================

import { Component, ErrorInfo, ReactNode } from 'react';

class RemoteErrorBoundary extends Component<
  { children: ReactNode },
  { hasError: boolean }
> {
  state = { hasError: false };
  
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  
  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('Remote app crashed:', error, errorInfo);
    // Log to Sentry, Datadog, etc.
  }
  
  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h2>Oops! Dashboard app crashed 😢</h2>
          <button onClick={() => this.setState({ hasError: false })}>
            Retry
          </button>
        </div>
      );
    }
    
    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <RemoteErrorBoundary>
      <DashboardPage /> {/* Nếu crash, không ảnh hưởng Shell */}
    </RemoteErrorBoundary>
  );
}
```

#### **🔥 4. Performance Optimization**

```typescript
// ===================================================
// 🚀 Preload remote apps khi user hover
// ===================================================

import { useState } from 'react';

function Navigation() {
  const [prefetched, setPrefetched] = useState<Set<string>>(new Set());
  
  const prefetchRemote = (remoteName: string) => {
    if (prefetched.has(remoteName)) return;
    
    // Preload remote module
    import(`${remoteName}/App`).then(() => {
      setPrefetched(prev => new Set(prev).add(remoteName));
      console.log(`✅ Prefetched ${remoteName}`);
    });
  };
  
  return (
    <nav>
      <a 
        href="/dashboard"
        onMouseEnter={() => prefetchRemote('dashboard')} // ⚡ Hover = preload
      >
        Dashboard
      </a>
      <a 
        href="/profile"
        onMouseEnter={() => prefetchRemote('profile')}
      >
        Profile
      </a>
    </nav>
  );
}
```

---

**❌ Common Mistakes (Lỗi Thường Gặp)**

```typescript
// ❌ 1. Duplicate dependencies (React loaded 2 lần)
// Shell: 500KB React + Dashboard: 500KB React = 1MB! ❌
// ✅ Fix: Dùng Module Federation shared config

// ❌ 2. Tight coupling via shared state
const user = useGlobalState('user'); // ❌ Dashboard phụ thuộc shell
// ✅ Fix: Dùng Event Bus cho loose coupling

// ❌ 3. No error boundaries
<DashboardPage /> // ❌ Nếu crash → toàn bộ app crash
// ✅ Fix: Wrap trong ErrorBoundary

// ❌ 4. CSS conflicts
.header { ... } // ❌ Dashboard và Profile cùng class name
// ✅ Fix: CSS Modules, CSS-in-JS, hoặc prefix

// ❌ 5. Version mismatch
shell: react@18 ↔ dashboard: react@17 // ❌ Conflict!
// ✅ Fix: Enforce singleton trong Module Federation
```

---

**📝 Summary (Tóm Tắt)**

| Concept                | Giải Thích                                             | Use Case                   |
| ---------------------- | ------------------------------------------------------ | -------------------------- |
| **Microfrontend**      | Chia app lớn thành nhiều apps nhỏ độc lập              | Large teams, multi-product |
| **Monorepo**           | Nhiều projects trong 1 repo                            | Code sharing, consistency  |
| **Module Federation**  | Share code runtime (không phải build time)             | Microfrontend architecture |
| **Multi-Framework**    | React + Vue + Angular trong 1 app                      | Legacy migration           |
| **Event Bus**          | Apps giao tiếp qua events                              | Loosely coupled            |
| **Shared State**       | Global state (Redux, Zustand)                          | User, theme, cart          |
| **Shell Routing**      | Shell quản lý tất cả routes                            | Centralized control        |
| **Distributed Routing**| Mỗi app tự quản lý routes                              | Autonomous apps            |
| **CSS Modules**        | Scoped CSS với unique class names                      | Default choice             |
| **CSS-in-JS**          | Styles trong JS, scoped                                | Dynamic styles             |
| **Shadow DOM**         | 100% CSS isolation                                     | Web Components             |

**🔥 Key Takeaways:**
- ✅ **Microfrontend** = Independent deployment + Team autonomy
- ✅ **Module Federation** = Runtime code sharing (no duplicate React)
- ✅ **Multi-framework** = React + Vue + Angular cùng app (với wrapper)
- ✅ **Communication**: Event Bus (loose) vs Shared State (tight)
- ✅ **Routing**: Shell-based (centralized) vs Distributed (autonomous)
- ✅ **Styling**: CSS Modules (default), CSS-in-JS (dynamic), Shadow DOM (isolation)
- ✅ **Monorepo** với Nx = Best DX + Code sharing + Consistent tooling

---


**❓ Câu Hỏi:**
> "Design system, Steps to build a FE structure? How you define structure for app can be scale? Apply any design pattern yet?"

**📋 Phân Tích:**
- **Design System** là gì? Tại sao cần?
- **Các bước xây dựng cấu trúc Frontend** có thể scale
- **Cách định nghĩa cấu trúc** cho app lớn (kiến trúc phân tầng)
- **Design Patterns** nào được áp dụng trong FE?

---

### **🎯 PHẦN 1: DESIGN SYSTEM LÀ GÌ? (What is Design System?)**

```typescript
/**
 * 🎨 DESIGN SYSTEM (Hệ Thống Thiết Kế)
 * 
 * Là TẬP HỢP các thành phần UI, quy tắc thiết kế, và hướng dẫn sử dụng
 * để đảm bảo TÍNH NHẤT QUÁN (consistency) trong toàn bộ sản phẩm.
 * 
 * 🔥 DESIGN SYSTEM ≠ COMPONENT LIBRARY
 * 
 * Design System bao gồm:
 * ├── 1️⃣ Design Tokens (Màu sắc, Font, Spacing, Shadow...)
 * ├── 2️⃣ Component Library (Button, Input, Modal, Table...)
 * ├── 3️⃣ Patterns & Guidelines (Cách sử dụng, Best practices)
 * ├── 4️⃣ Documentation (Storybook, Docs site)
 * └── 5️⃣ Tools & Processes (Figma, Design workflow)
 * 
 * Component Library chỉ là 1 PHẦN của Design System!
 */

// ===================================================
// 🏢 VÍ DỤ THỰC TẾ: KHÔNG CÓ DESIGN SYSTEM
// ===================================================

// ❌ SCENARIO: 10 developers, không có design system
// → Mỗi người code Button theo ý mình

// Developer 1 (Team Dashboard):
const Button1 = styled.button`
  background: #007bff;      // Màu xanh dương
  padding: 10px 20px;       // Padding
  border-radius: 4px;       // Bo góc 4px
  font-size: 14px;          // Font size 14px
`;

// Developer 2 (Team Profile):
const Button2 = styled.button`
  background: #0066cc;      // Màu xanh khác! ❌
  padding: 12px 24px;       // Padding khác! ❌
  border-radius: 8px;       // Bo góc khác! ❌
  font-size: 16px;          // Font khác! ❌
`;

// Developer 3 (Team Settings):
const Button3 = styled.button`
  background: linear-gradient(to right, #007bff, #0066cc); // Gradient! ❌
  padding: 8px 16px;        // Padding khác nữa! ❌
  border-radius: 6px;       // Bo góc khác nữa! ❌
  font-size: 15px;          // Font khác nữa! ❌
`;

/**
 * ❌ KẾT QUẢ:
 * - App có 3 LOẠI BUTTON KHÁC NHAU (không nhất quán)
 * - User bối rối: "Button nào để click?"
 * - Designer phát điên: "Đây không phải design tôi đưa!"
 * - Developers tranh cãi: "Button của tôi đẹp hơn!"
 * - Maintenance nightmare: Muốn đổi màu → phải sửa 3 chỗ
 */

// ===================================================
// ✅ GIẢI PHÁP: CÓ DESIGN SYSTEM
// ===================================================

// 1️⃣ DESIGN TOKENS (Token Thiết Kế)
// tokens/colors.ts
export const colors = {
  // Primary colors (Màu chính)
  primary: {
    50: '#e3f2fd',    // Lightest (nhạt nhất)
    100: '#bbdefb',
    200: '#90caf9',
    300: '#64b5f6',
    400: '#42a5f5',
    500: '#2196f3',   // Default (mặc định)
    600: '#1e88e5',
    700: '#1976d2',
    800: '#1565c0',
    900: '#0d47a1',   // Darkest (đậm nhất)
  },
  // Semantic colors (Màu theo ngữ nghĩa)
  success: '#4caf50',
  warning: '#ff9800',
  error: '#f44336',
  info: '#2196f3',
};

// tokens/spacing.ts
export const spacing = {
  xs: '4px',      // Extra small
  sm: '8px',      // Small
  md: '16px',     // Medium (default)
  lg: '24px',     // Large
  xl: '32px',     // Extra large
  xxl: '48px',    // 2x Extra large
};

// tokens/typography.ts
export const typography = {
  fontFamily: {
    body: "'Inter', sans-serif",
    heading: "'Poppins', sans-serif",
    mono: "'Fira Code', monospace",
  },
  fontSize: {
    xs: '12px',
    sm: '14px',
    md: '16px',   // Base font size (cỡ chữ cơ bản)
    lg: '18px',
    xl: '20px',
    '2xl': '24px',
    '3xl': '30px',
  },
  fontWeight: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },
};

// 2️⃣ COMPONENT LIBRARY (Thư Viện Components)
// components/Button/Button.tsx
import { colors, spacing, typography } from '@tokens';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
}

const Button: React.FC<ButtonProps> = ({ 
  variant = 'primary', 
  size = 'md',
  children 
}) => {
  // ✅ Dùng design tokens (không hardcode)
  const styles = {
    primary: {
      background: colors.primary[500],    // Dùng token
      color: '#fff',
      padding: spacing[size],             // Dùng token
      fontSize: typography.fontSize[size], // Dùng token
      borderRadius: '4px',
      border: 'none',
    },
    secondary: {
      background: colors.primary[100],
      color: colors.primary[900],
      padding: spacing[size],
      fontSize: typography.fontSize[size],
      borderRadius: '4px',
      border: 'none',
    },
    outline: {
      background: 'transparent',
      color: colors.primary[500],
      padding: spacing[size],
      fontSize: typography.fontSize[size],
      borderRadius: '4px',
      border: `2px solid ${colors.primary[500]}`,
    },
  };

  return (
    <button style={styles[variant]}>
      {children}
    </button>
  );
};

/**
 * ✅ LỢI ÍCH:
 * - Tất cả Buttons GIỐNG NHAU (consistent)
 * - Muốn đổi màu → chỉ sửa 1 chỗ (colors.primary[500])
 * - Developers KHÔNG TRANH CÃI (follow design system)
 * - Designer VUI VẺ (đúng design)
 * - User KHÔNG BỐI RỐI (UI nhất quán)
 */

// ===================================================
// 📊 SO SÁNH: KHÔNG VS CÓ DESIGN SYSTEM
// ===================================================

/**
 * ❌ KHÔNG CÓ DESIGN SYSTEM:
 * ├── 10 developers → 10 cách code Button khác nhau
 * ├── Buttons: 10 loại màu, 8 loại padding, 6 loại border-radius
 * ├── Colors: 50+ màu xanh khác nhau (hardcoded)
 * ├── Spacing: 30+ giá trị padding/margin khác nhau
 * ├── Typography: 15+ font sizes khác nhau
 * ├── Maintenance: Đổi màu → sửa 100+ chỗ (3 ngày)
 * └── User experience: Rối, không nhất quán
 * 
 * ✅ CÓ DESIGN SYSTEM:
 * ├── 10 developers → 1 cách code Button (follow tokens)
 * ├── Buttons: 1 component, 3 variants (primary, secondary, outline)
 * ├── Colors: 1 file colors.ts với 10 màu primary (50-900)
 * ├── Spacing: 6 values (xs, sm, md, lg, xl, xxl)
 * ├── Typography: 7 font sizes (xs, sm, md, lg, xl, 2xl, 3xl)
 * ├── Maintenance: Đổi màu → sửa 1 chỗ (5 phút)
 * └── User experience: Mượt mà, nhất quán
 */

// ===================================================
// 🎯 TẠI SAO CẦN DESIGN SYSTEM? (Why Design System?)
// ===================================================

/**
 * 1️⃣ CONSISTENCY (Tính Nhất Quán)
 *    → Tất cả UI elements giống nhau trong toàn app
 *    → User không bối rối
 * 
 * 2️⃣ SCALABILITY (Khả Năng Mở Rộng)
 *    → Thêm 100 developers → vẫn giữ consistency
 *    → Thêm 50 pages mới → vẫn dùng components cũ
 * 
 * 3️⃣ SPEED (Tốc Độ Phát Triển)
 *    → Developers không cần design từ đầu
 *    → Copy component từ Storybook → paste vào code
 *    → Build page mới: 1 ngày thay vì 1 tuần
 * 
 * 4️⃣ MAINTAINABILITY (Dễ Bảo Trì)
 *    → Đổi màu toàn app: 1 file thay vì 100 files
 *    → Fix bug Button: 1 component thay vì 50 chỗ
 * 
 * 5️⃣ COLLABORATION (Hợp Tác)
 *    → Designer và Developer nói chung 1 ngôn ngữ
 *    → "Dùng Button variant='primary' size='lg'" (rõ ràng)
 *    → Không còn: "Button màu xanh, padding 12px..." (mơ hồ)
 * 
 * 6️⃣ ACCESSIBILITY (Khả Năng Tiếp Cận)
 *    → Components built-in accessibility (ARIA labels, keyboard nav)
 *    → Developers KHÔNG QUÊN implement a11y
 */

---

### **🏗️ PHẦN 2: STEPS TO BUILD SCALABLE FE STRUCTURE (Các Bước Xây Dựng Cấu Trúc FE Có Thể Scale)**

```typescript
/**
 * 🎯 MỤC TIÊU:
 * Xây dựng cấu trúc Frontend cho app LỚN (100+ developers, 500+ components)
 * có thể SCALE dễ dàng mà KHÔNG TRỞ THÀNH SPAGHETTI CODE.
 * 
 * 📋 7 BƯỚC XÂY DỰNG:
 * 1️⃣ Define Architecture Pattern (Chọn kiến trúc phân tầng)
 * 2️⃣ Folder Structure (Cấu trúc thư mục rõ ràng)
 * 3️⃣ Design System Setup (Thiết lập Design System)
 * 4️⃣ State Management Strategy (Chiến lược quản lý state)
 * 5️⃣ Code Organization (Tổ chức code module hóa)
 * 6️⃣ Tooling & DX (Công cụ và Developer Experience)
 * 7️⃣ Testing & Documentation (Kiểm thử và tài liệu)
 */

// ===================================================
// 1️⃣ DEFINE ARCHITECTURE PATTERN (Kiến Trúc Phân Tầng)
// ===================================================

/**
 * 🏛️ LAYERED ARCHITECTURE (Kiến Trúc Phân Tầng)
 * 
 * Chia app thành các TẦNG (layers) với trách nhiệm rõ ràng:
 * 
 * ┌─────────────────────────────────────────┐
 * │  PRESENTATION LAYER (Tầng Hiển Thị)    │ ← React Components, UI
 * ├─────────────────────────────────────────┤
 * │  BUSINESS LOGIC LAYER (Tầng Logic)     │ ← Hooks, Utils, Validators
 * ├─────────────────────────────────────────┤
 * │  DATA ACCESS LAYER (Tầng Dữ Liệu)      │ ← API calls, Repositories
 * ├─────────────────────────────────────────┤
 * │  INFRASTRUCTURE LAYER (Tầng Hạ Tầng)   │ ← Axios, Storage, Config
 * └─────────────────────────────────────────┘
 * 
 * 🔥 NGUYÊN TẮC:
 * - Tầng trên CHỈ PHỤ THUỘC vào tầng dưới (one-way dependency)
 * - Tầng dưới KHÔNG BIẾT tầng trên (no reverse dependency)
 * - Mỗi tầng có thể THAY THẾ độc lập (interchangeable)
 */

// ===================================================
// 2️⃣ FOLDER STRUCTURE (Cấu Trúc Thư Mục)
// ===================================================

/**
 * 📁 FEATURE-BASED STRUCTURE (Cấu Trúc Theo Feature)
 * 
 * Nhóm code theo FEATURE thay vì theo TYPE (components, hooks...)
 * → Dễ tìm, dễ maintain, dễ scale
 */

// ✅ RECOMMENDED: Feature-based (Theo Feature)
/*
src/
├── features/                    # Tất cả features của app
│   ├── auth/                    # Feature: Authentication
│   │   ├── components/          # Components của Auth
│   │   │   ├── LoginForm.tsx
│   │   │   ├── RegisterForm.tsx
│   │   │   └── ForgotPassword.tsx
│   │   ├── hooks/               # Hooks của Auth
│   │   │   ├── useAuth.ts
│   │   │   └── useLogin.ts
│   │   ├── services/            # API calls của Auth
│   │   │   └── authService.ts
│   │   ├── store/               # State của Auth (nếu dùng Redux)
│   │   │   ├── authSlice.ts
│   │   │   └── authSelectors.ts
│   │   ├── types/               # TypeScript types của Auth
│   │   │   └── auth.types.ts
│   │   ├── utils/               # Utils của Auth
│   │   │   └── tokenUtils.ts
│   │   └── index.ts             # Public API của Auth feature
│   │
│   ├── dashboard/               # Feature: Dashboard
│   │   ├── components/
│   │   │   ├── DashboardLayout.tsx
│   │   │   ├── StatsCard.tsx
│   │   │   └── RecentOrders.tsx
│   │   ├── hooks/
│   │   │   └── useDashboardData.ts
│   │   ├── services/
│   │   │   └── dashboardService.ts
│   │   └── index.ts
│   │
│   ├── orders/                  # Feature: Orders
│   │   ├── components/
│   │   │   ├── OrderList.tsx
│   │   │   ├── OrderDetail.tsx
│   │   │   └── OrderForm.tsx
│   │   ├── hooks/
│   │   │   ├── useOrders.ts
│   │   │   └── useOrderMutations.ts
│   │   ├── services/
│   │   │   └── orderService.ts
│   │   └── index.ts
│   │
│   └── products/                # Feature: Products
│       ├── components/
│       ├── hooks/
│       ├── services/
│       └── index.ts
│
├── shared/                      # Code DÙNG CHUNG (shared across features)
│   ├── components/              # Shared components (Button, Input, Modal...)
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   ├── Button.stories.tsx  # Storybook story
│   │   │   └── index.ts
│   │   ├── Input/
│   │   ├── Modal/
│   │   └── Table/
│   │
│   ├── hooks/                   # Shared hooks (useDebounce, useLocalStorage...)
│   │   ├── useDebounce.ts
│   │   ├── useLocalStorage.ts
│   │   └── useMediaQuery.ts
│   │
│   ├── utils/                   # Shared utilities
│   │   ├── formatters.ts        # Format date, currency, số điện thoại...
│   │   ├── validators.ts        # Validate email, phone, credit card...
│   │   └── helpers.ts           # Helper functions
│   │
│   ├── constants/               # Shared constants
│   │   ├── routes.ts            # App routes
│   │   ├── api.ts               # API endpoints
│   │   └── config.ts            # App config
│   │
│   └── types/                   # Shared TypeScript types
│       ├── api.types.ts
│       └── common.types.ts
│
├── core/                        # CORE INFRASTRUCTURE (hạ tầng cốt lõi)
│   ├── api/                     # API client setup
│   │   ├── apiClient.ts         # Axios instance với interceptors
│   │   └── endpoints.ts         # API endpoints
│   │
│   ├── store/                   # Global state setup (Redux/Zustand)
│   │   ├── store.ts             # Store configuration
│   │   └── rootReducer.ts       # Combine reducers
│   │
│   ├── router/                  # Routing setup
│   │   ├── routes.tsx           # App routes
│   │   └── ProtectedRoute.tsx   # Auth guard
│   │
│   └── theme/                   # Design System
│       ├── tokens/              # Design tokens
│       │   ├── colors.ts
│       │   ├── spacing.ts
│       │   └── typography.ts
│       └── GlobalStyles.ts      # Global CSS
│
├── pages/                       # PAGE COMPONENTS (route pages)
│   ├── LoginPage.tsx            # /login
│   ├── DashboardPage.tsx        # /dashboard
│   ├── OrdersPage.tsx           # /orders
│   └── ProductsPage.tsx         # /products
│
├── App.tsx                      # Root component
├── main.tsx                     # Entry point
└── vite-env.d.ts                # Vite types
*/

/**
 * ✅ LỢI ÍCH CỦA FEATURE-BASED STRUCTURE:
 * 
 * 1️⃣ CO-LOCATION (Đặt Cùng Chỗ):
 *    → Tất cả code của 1 feature ở 1 folder
 *    → Dễ tìm: Cần sửa Login? → vào features/auth/
 * 
 * 2️⃣ ENCAPSULATION (Đóng Gói):
 *    → Mỗi feature là 1 MODULE độc lập
 *    → Export qua index.ts (public API)
 *    → Các files khác PRIVATE (không export)
 * 
 * 3️⃣ SCALABILITY (Mở Rộng):
 *    → Thêm feature mới? → Tạo folder mới
 *    → 100 features? → Vẫn rõ ràng!
 * 
 * 4️⃣ TEAM AUTONOMY (Độc Lập Team):
 *    → Team A làm feature Auth
 *    → Team B làm feature Orders
 *    → KHÔNG CONFLICT (ít merge conflicts)
 * 
 * 5️⃣ CODE SPLITTING:
 *    → Lazy load từng feature
 *    → User vào /login → chỉ load Auth feature
 *    → Không load Orders, Products (tiết kiệm bandwidth)
 */

// ❌ ANTI-PATTERN: Type-based structure (Theo Type - KHÔNG KHUYẾN KHÍCH)
/*
src/
├── components/          # TẤT CẢ components (100+ files) ❌
│   ├── LoginForm.tsx
│   ├── RegisterForm.tsx
│   ├── DashboardLayout.tsx
│   ├── OrderList.tsx
│   ├── ProductCard.tsx
│   └── ... 95 files nữa
├── hooks/               # TẤT CẢ hooks (50+ files) ❌
│   ├── useAuth.ts
│   ├── useOrders.ts
│   ├── useProducts.ts
│   └── ... 47 files nữa
└── services/            # TẤT CẢ services (30+ files) ❌
    ├── authService.ts
    ├── orderService.ts
    └── ... 28 files nữa

❌ VẤN ĐỀ:
- components/ có 100 files → TÌM KHÔNG RA!
- Muốn sửa Auth → phải mở 3 folders (components, hooks, services)
- Team A sửa LoginForm.tsx, Team B sửa RegisterForm.tsx → CONFLICT!
- Không thể code split theo feature
*/

// ===================================================
// 3️⃣ DESIGN SYSTEM SETUP (Thiết Lập Design System)
// ===================================================

// Step 1: Define Design Tokens
// core/theme/tokens/colors.ts
export const colors = {
  primary: {
    50: '#e3f2fd',
    500: '#2196f3',  // Main primary color
    900: '#0d47a1',
  },
  semantic: {
    success: '#4caf50',
    error: '#f44336',
    warning: '#ff9800',
    info: '#2196f3',
  },
  neutral: {
    0: '#ffffff',
    50: '#fafafa',
    100: '#f5f5f5',
    500: '#9e9e9e',
    900: '#212121',
  },
};

// core/theme/tokens/spacing.ts
export const spacing = {
  xs: 4,   // 4px
  sm: 8,   // 8px
  md: 16,  // 16px (base)
  lg: 24,  // 24px
  xl: 32,  // 32px
  xxl: 48, // 48px
};

// core/theme/tokens/typography.ts
export const typography = {
  fontFamily: {
    body: "'Inter', -apple-system, sans-serif",
    heading: "'Poppins', sans-serif",
  },
  fontSize: {
    xs: 12,
    sm: 14,
    md: 16,  // Base font size
    lg: 18,
    xl: 20,
    '2xl': 24,
  },
  fontWeight: {
    normal: 400,
    medium: 500,
    semibold: 600,
    bold: 700,
  },
  lineHeight: {
    tight: 1.2,
    normal: 1.5,
    relaxed: 1.75,
  },
};

// Step 2: Create Theme Provider
// core/theme/ThemeProvider.tsx
import { createContext, useContext } from 'react';
import { colors, spacing, typography } from './tokens';

const theme = {
  colors,
  spacing,
  typography,
};

const ThemeContext = createContext(theme);

export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return (
    <ThemeContext.Provider value={theme}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => useContext(ThemeContext);

// Step 3: Create Base Components (Button example)
// shared/components/Button/Button.tsx
import { useTheme } from '@core/theme';

interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
}

export const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children,
  onClick,
}) => {
  const theme = useTheme();

  // ✅ Dùng theme tokens (không hardcode)
  const styles = {
    primary: {
      backgroundColor: theme.colors.primary[500],
      color: theme.colors.neutral[0],
      padding: `${theme.spacing.sm}px ${theme.spacing.md}px`,
      fontSize: theme.typography.fontSize[size],
      fontWeight: theme.typography.fontWeight.semibold,
      border: 'none',
      borderRadius: '4px',
      cursor: 'pointer',
    },
    // ... secondary, outline variants
  };

  return (
    <button style={styles[variant]} onClick={onClick}>
      {children}
    </button>
  );
};

/**
 * ✅ LỢI ÍCH:
 * - Thay đổi màu primary: 1 file (colors.ts)
 * - Thay đổi spacing: 1 file (spacing.ts)
 * - Consistent UI: Tất cả Buttons giống nhau
 */

// ===================================================
// 4️⃣ STATE MANAGEMENT STRATEGY (Chiến Lược Quản Lý State)
// ===================================================

/**
 * 🎯 PHÂN LOẠI STATE:
 * 
 * 1️⃣ LOCAL STATE (State Cục Bộ):
 *    → Chỉ dùng trong 1 component
 *    → Dùng useState, useReducer
 *    → VD: Form input value, modal open/close
 * 
 * 2️⃣ SHARED STATE (State Chia Sẻ):
 *    → Dùng trong nhiều components (cùng feature)
 *    → Dùng Context API, Zustand
 *    → VD: User info trong Auth feature
 * 
 * 3️⃣ GLOBAL STATE (State Toàn Cục):
 *    → Dùng trong TOÀN APP
 *    → Dùng Redux, Zustand (global store)
 *    → VD: Theme, Language, Current User
 * 
 * 4️⃣ SERVER STATE (State Từ Server):
 *    → Data từ API
 *    → Dùng React Query, SWR
 *    → VD: User list, Product list, Order details
 * 
 * 🔥 NGUYÊN TẮC:
 * - Ưu tiên LOCAL STATE (đơn giản nhất)
 * - Chỉ dùng GLOBAL STATE khi THỰC SỰ CẦN
 * - Dùng React Query cho SERVER STATE (caching, revalidation)
 */

// Example: State Strategy trong 1 Trading App

// 1️⃣ LOCAL STATE: Form input
const OrderForm = () => {
  const [quantity, setQuantity] = useState(0);  // ✅ Local state
  const [price, setPrice] = useState(0);        // ✅ Local state
  
  return (
    <form>
      <input value={quantity} onChange={e => setQuantity(+e.target.value)} />
      <input value={price} onChange={e => setPrice(+e.target.value)} />
    </form>
  );
};

// 2️⃣ SHARED STATE: Auth state (dùng trong Auth feature)
// features/auth/store/authStore.ts
import create from 'zustand';

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  login: (user: User) => void;
  logout: () => void;
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  isAuthenticated: false,
  login: (user) => set({ user, isAuthenticated: true }),
  logout: () => set({ user: null, isAuthenticated: false }),
}));

// 3️⃣ GLOBAL STATE: Theme
// core/store/themeStore.ts
export const useThemeStore = create<ThemeState>((set) => ({
  theme: 'light',
  toggleTheme: () => set((state) => ({
    theme: state.theme === 'light' ? 'dark' : 'light'
  })),
}));

// 4️⃣ SERVER STATE: Orders list
// features/orders/hooks/useOrders.ts
import { useQuery } from '@tanstack/react-query';
import { orderService } from '../services/orderService';

export const useOrders = () => {
  return useQuery({
    queryKey: ['orders'],
    queryFn: orderService.getOrders,
    staleTime: 5 * 60 * 1000,  // Cache 5 phút
    cacheTime: 10 * 60 * 1000, // Giữ cache 10 phút
  });
};

/**
 * ✅ LỢI ÍCH:
 * - Local state: Đơn giản, không cần setup
 * - Shared state (Zustand): Nhẹ, dễ dùng hơn Redux
 * - Global state: Centralized, predictable
 * - Server state (React Query): Auto caching, revalidation, loading states
 */

---

### **🎨 PHẦN 3: DESIGN PATTERNS TRONG FRONTEND (Các Mẫu Thiết Kế)**

```typescript
/**
 * 🏗️ DESIGN PATTERNS (Mẫu Thiết Kế)
 * 
 * Là các GIẢI PHÁP ĐÃ ĐƯỢC CHỨNG MINH (proven solutions)
 * cho các VẤN ĐỀ THƯỜNG GẶP trong lập trình.
 * 
 * 📋 CÁC PATTERN THƯỜNG DÙNG TRONG REACT:
 * 1️⃣ Container/Presentational Pattern
 * 2️⃣ Compound Component Pattern
 * 3️⃣ Render Props Pattern
 * 4️⃣ Higher-Order Component (HOC) Pattern
 * 5️⃣ Custom Hooks Pattern
 * 6️⃣ Provider Pattern
 * 7️⃣ Observer Pattern (Pub/Sub)
 * 8️⃣ Factory Pattern
 * 9️⃣ Singleton Pattern
 * 🔟 Module Pattern
 */

// ===================================================
// 1️⃣ CONTAINER/PRESENTATIONAL PATTERN
// ===================================================

/**
 * 🎯 MỤC ĐÍCH:
 * Tách LOGIC (business logic) ra khỏi UI (presentation)
 * 
 * 📦 CONTAINER (Smart Component):
 * - Xử lý logic, fetch data, state management
 * - KHÔNG quan tâm UI
 * 
 * 🎨 PRESENTATIONAL (Dumb Component):
 * - Chỉ nhận props và render UI
 * - KHÔNG có logic, KHÔNG fetch data
 */

// ❌ BAD: Logic và UI lẫn lộn
const UserList = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Logic: Fetch data ❌ Lẫn với UI
    setLoading(true);
    fetch('/api/users')
      .then(res => res.json())
      .then(data => {
        setUsers(data);
        setLoading(false);
      });
  }, []);

  // UI: Render ❌ Lẫn với Logic
  if (loading) return <div>Loading...</div>;
  
  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} - {user.email}
        </li>
      ))}
    </ul>
  );
};

// ✅ GOOD: Tách Container (Logic) và Presentational (UI)

// 📦 CONTAINER (Logic)
const UserListContainer = () => {
  const { data: users, isLoading } = useQuery({
    queryKey: ['users'],
    queryFn: fetchUsers,
  });

  // ✅ Container KHÔNG RENDER UI, chỉ pass props
  return <UserListView users={users} loading={isLoading} />;
};

// 🎨 PRESENTATIONAL (UI)
interface UserListViewProps {
  users: User[];
  loading: boolean;
}

const UserListView: React.FC<UserListViewProps> = ({ users, loading }) => {
  // ✅ Presentational chỉ render UI, KHÔNG có logic
  if (loading) return <div>Loading...</div>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>
          {user.name} - {user.email}
        </li>
      ))}
    </ul>
  );
};

/**
 * ✅ LỢI ÍCH:
 * - Dễ test: Test logic riêng, test UI riêng
 * - Dễ reuse: UserListView có thể dùng với data khác
 * - Dễ đọc: Logic ở Container, UI ở Presentational (rõ ràng)
 */

// ===================================================
// 2️⃣ COMPOUND COMPONENT PATTERN
// ===================================================

/**
 * 🎯 MỤC ĐÍCH:
 * Tạo components LINH HOẠT bằng cách chia thành các SUB-COMPONENTS
 * có thể tùy chỉnh thứ tự, layout.
 * 
 * VD: <Select>, <Tabs>, <Menu> - user tự quyết định thứ tự các phần
 */

// ❌ BAD: Component cứng nhắc
interface TabsProps {
  tabs: Array<{ label: string; content: React.ReactNode }>;
}

const Tabs: React.FC<TabsProps> = ({ tabs }) => {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <div>
      {/* ❌ Tab headers CỐ ĐỊNH ở trên */}
      <div className="tab-headers">
        {tabs.map((tab, index) => (
          <button key={index} onClick={() => setActiveTab(index)}>
            {tab.label}
          </button>
        ))}
      </div>

      {/* ❌ Tab content CỐ ĐỊNH ở dưới */}
      <div className="tab-content">
        {tabs[activeTab].content}
      </div>
    </div>
  );
};

// Usage: ❌ Không thể thay đổi layout
<Tabs tabs={[
  { label: 'Tab 1', content: <div>Content 1</div> },
  { label: 'Tab 2', content: <div>Content 2</div> },
]} />

// ✅ GOOD: Compound Components (Linh hoạt)

// Context để share state giữa sub-components
const TabsContext = createContext<{
  activeTab: number;
  setActiveTab: (index: number) => void;
} | null>(null);

// Main component
const Tabs: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [activeTab, setActiveTab] = useState(0);

  return (
    <TabsContext.Provider value={{ activeTab, setActiveTab }}>
      <div className="tabs">{children}</div>
    </TabsContext.Provider>
  );
};

// Sub-component: TabList
Tabs.List = ({ children }: { children: React.ReactNode }) => {
  return <div className="tab-list">{children}</div>;
};

// Sub-component: Tab
Tabs.Tab = ({ index, children }: { index: number; children: React.ReactNode }) => {
  const context = useContext(TabsContext);
  if (!context) throw new Error('Tab must be used within Tabs');

  const isActive = context.activeTab === index;

  return (
    <button
      className={`tab ${isActive ? 'active' : ''}`}
      onClick={() => context.setActiveTab(index)}
    >
      {children}
    </button>
  );
};

// Sub-component: TabPanel
Tabs.Panel = ({ index, children }: { index: number; children: React.ReactNode }) => {
  const context = useContext(TabsContext);
  if (!context) throw new Error('TabPanel must be used within Tabs');

  if (context.activeTab !== index) return null;

  return <div className="tab-panel">{children}</div>;
};

// ✅ Usage: LINH HOẠT - user tự quyết định layout
<Tabs>
  {/* User tự quyết định: Tabs ở trên hay dưới */}
  <Tabs.List>
    <Tabs.Tab index={0}>Profile</Tabs.Tab>
    <Tabs.Tab index={1}>Settings</Tabs.Tab>
    <Tabs.Tab index={2}>Billing</Tabs.Tab>
  </Tabs.List>

  <Tabs.Panel index={0}>
    <ProfileContent />
  </Tabs.Panel>
  <Tabs.Panel index={1}>
    <SettingsContent />
  </Tabs.Panel>
  <Tabs.Panel index={2}>
    <BillingContent />
  </Tabs.Panel>
</Tabs>

// Hoặc: Tabs ở dưới
<Tabs>
  <Tabs.Panel index={0}><ProfileContent /></Tabs.Panel>
  <Tabs.Panel index={1}><SettingsContent /></Tabs.Panel>
  
  <Tabs.List>
    <Tabs.Tab index={0}>Profile</Tabs.Tab>
    <Tabs.Tab index={1}>Settings</Tabs.Tab>
  </Tabs.List>
</Tabs>

/**
 * ✅ LỢI ÍCH:
 * - Flexibility (Linh hoạt): User tự quyết định layout
 * - Maintainability: Mỗi sub-component độc lập
 * - API rõ ràng: <Tabs.List>, <Tabs.Tab>, <Tabs.Panel>
 * 
 * 📚 REAL EXAMPLES:
 * - Radix UI: <Tabs>, <Dialog>, <DropdownMenu>
 * - Headless UI: Tất cả components
 * - Chakra UI: <Menu>, <Accordion>
 */

// ===================================================
// 3️⃣ CUSTOM HOOKS PATTERN
// ===================================================

/**
 * 🎯 MỤC ĐÍCH:
 * Tái sử dụng STATEFUL LOGIC (logic có state) giữa các components
 * 
 * 🔥 KHÔNG PHẢI tái sử dụng UI, mà tái sử dụng LOGIC!
 */

// ❌ BAD: Copy-paste logic vào mỗi component
const LoginForm = () => {
  const [value, setValue] = useState('');
  const [error, setError] = useState('');

  const validate = (val: string) => {
    if (!val) setError('Required');
    else if (!/\S+@\S+\.\S+/.test(val)) setError('Invalid email');
    else setError('');
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setValue(val);
    validate(val);
  };

  return <input value={value} onChange={handleChange} />;
};

const RegisterForm = () => {
  // ❌ Copy-paste SAME LOGIC!
  const [value, setValue] = useState('');
  const [error, setError] = useState('');

  const validate = (val: string) => {
    if (!val) setError('Required');
    else if (!/\S+@\S+\.\S+/.test(val)) setError('Invalid email');
    else setError('');
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setValue(val);
    validate(val);
  };

  return <input value={value} onChange={handleChange} />;
};

// ✅ GOOD: Extract logic vào Custom Hook
const useFormField = (initialValue = '', validator?: (val: string) => string) => {
  const [value, setValue] = useState(initialValue);
  const [error, setError] = useState('');
  const [touched, setTouched] = useState(false);

  const validate = (val: string) => {
    if (validator) {
      const errorMsg = validator(val);
      setError(errorMsg);
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const val = e.target.value;
    setValue(val);
    if (touched) validate(val);
  };

  const handleBlur = () => {
    setTouched(true);
    validate(value);
  };

  const reset = () => {
    setValue(initialValue);
    setError('');
    setTouched(false);
  };

  return {
    value,
    error,
    touched,
    handleChange,
    handleBlur,
    reset,
  };
};

// ✅ Usage: Tái sử dụng logic
const LoginForm = () => {
  const email = useFormField('', (val) => {
    if (!val) return 'Required';
    if (!/\S+@\S+\.\S+/.test(val)) return 'Invalid email';
    return '';
  });

  const password = useFormField('', (val) => {
    if (!val) return 'Required';
    if (val.length < 8) return 'Min 8 characters';
    return '';
  });

  return (
    <form>
      <input {...email} />
      {email.touched && <span>{email.error}</span>}

      <input type="password" {...password} />
      {password.touched && <span>{password.error}</span>}
    </form>
  );
};

/**
 * ✅ LỢI ÍCH:
 * - Reusability: Dùng lại logic ở nhiều components
 * - Testability: Test hook riêng (với @testing-library/react-hooks)
 * - Separation of Concerns: Logic tách khỏi UI
 * 
 * 📚 POPULAR CUSTOM HOOKS:
 * - useDebounce: Delay input
 * - useLocalStorage: Sync state với localStorage
 * - useMediaQuery: Responsive breakpoints
 * - useFetch: Fetch data với loading/error states
 * - useIntersectionObserver: Lazy load images
 */

// ===================================================
// 4️⃣ OBSERVER PATTERN (Pub/Sub)
// ===================================================

/**
 * 🎯 MỤC ĐÍCH:
 * Nhiều components LẮNG NGHE (subscribe) và PHẢN ỨNG (react)
 * khi có SỰ KIỆN (event) xảy ra.
 * 
 * 🔥 Dùng cho: Event Bus, Global notifications, Real-time updates
 */

// Implementation: Event Emitter
class EventEmitter {
  private events: Map<string, Array<(data: any) => void>> = new Map();

  // Subscribe to event (Đăng ký lắng nghe)
  on(event: string, callback: (data: any) => void) {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    this.events.get(event)!.push(callback);

    // Return unsubscribe function
    return () => {
      const callbacks = this.events.get(event);
      if (callbacks) {
        const index = callbacks.indexOf(callback);
        if (index > -1) callbacks.splice(index, 1);
      }
    };
  }

  // Emit event (Phát sự kiện)
  emit(event: string, data?: any) {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.forEach(callback => callback(data));
    }
  }

  // Remove all listeners
  off(event: string) {
    this.events.delete(event);
  }
}

// Global event bus
export const eventBus = new EventEmitter();

// ✅ Usage Example: Real-time notifications

// Component 1: Emit event khi order completed
const OrderForm = () => {
  const handleSubmit = async () => {
    const order = await createOrder();
    
    // 📢 Emit event: "order:completed"
    eventBus.emit('order:completed', {
      orderId: order.id,
      total: order.total,
    });
  };

  return <form onSubmit={handleSubmit}>...</form>;
};

// Component 2: Listen to event và show notification
const NotificationBar = () => {
  const [notifications, setNotifications] = useState<string[]>([]);

  useEffect(() => {
    // 👂 Subscribe to "order:completed"
    const unsubscribe = eventBus.on('order:completed', (data) => {
      setNotifications(prev => [
        ...prev,
        `Order #${data.orderId} completed! Total: $${data.total}`
      ]);
    });

    // Cleanup: Unsubscribe khi unmount
    return unsubscribe;
  }, []);

  return (
    <div className="notifications">
      {notifications.map((msg, i) => (
        <div key={i}>{msg}</div>
      ))}
    </div>
  );
};

// Component 3: Listen và update stats
const DashboardStats = () => {
  const [totalOrders, setTotalOrders] = useState(0);

  useEffect(() => {
    // 👂 Same event, different action
    const unsubscribe = eventBus.on('order:completed', () => {
      setTotalOrders(prev => prev + 1);
    });

    return unsubscribe;
  }, []);

  return <div>Total Orders: {totalOrders}</div>;
};

/**
 * ✅ LỢI ÍCH:
 * - Loose Coupling: Components KHÔNG BIẾT nhau
 * - Scalability: Thêm listener mới dễ dàng
 * - Flexibility: 1 event → nhiều reactions
 * 
 * ⚠️ NHƯỢC ĐIỂM:
 * - Hard to debug: Không biết ai emit, ai listen
 * - Memory leaks: Quên unsubscribe
 * 
 * 💡 KHI NÀO DÙNG:
 * - Real-time notifications
 * - Cross-feature communication
 * - Event tracking (analytics)
 */

// ===================================================
// 5️⃣ SINGLETON PATTERN
// ===================================================

/**
 * 🎯 MỤC ĐÍCH:
 * Đảm bảo 1 class CHỈ CÓ 1 INSTANCE duy nhất trong toàn app.
 * 
 * 🔥 Dùng cho: API client, Logger, Config manager
 */

// ✅ Implementation: API Client Singleton
class ApiClient {
  private static instance: ApiClient;
  private baseURL: string;
  private token: string | null = null;

  // Private constructor (Không thể new ApiClient())
  private constructor() {
    this.baseURL = import.meta.env.VITE_API_URL;
  }

  // Get singleton instance
  public static getInstance(): ApiClient {
    if (!ApiClient.instance) {
      ApiClient.instance = new ApiClient();
    }
    return ApiClient.instance;
  }

  // Set auth token
  public setToken(token: string) {
    this.token = token;
  }

  // API methods
  public async get<T>(endpoint: string): Promise<T> {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      headers: {
        'Authorization': `Bearer ${this.token}`,
      },
    });
    return response.json();
  }

  public async post<T>(endpoint: string, data: any): Promise<T> {
    const response = await fetch(`${this.baseURL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${this.token}`,
      },
      body: JSON.stringify(data),
    });
    return response.json();
  }
}

// ✅ Usage: Luôn cùng 1 instance
const api = ApiClient.getInstance();

// Component 1: Set token
const LoginForm = () => {
  const handleLogin = async (credentials) => {
    const { token } = await api.post('/auth/login', credentials);
    
    // Set token vào singleton instance
    api.setToken(token);
  };
};

// Component 2: Token đã có sẵn (cùng instance)
const Dashboard = () => {
  const { data } = useQuery({
    queryKey: ['dashboard'],
    queryFn: () => api.get('/dashboard'),  // ✅ Token already set
  });
};

/**
 * ✅ LỢI ÍCH:
 * - Shared state: Token được share giữa tất cả API calls
 * - Memory efficient: Chỉ 1 instance
 * - Consistent config: Tất cả calls dùng cùng baseURL
 * 
 * ⚠️ NHƯỢC ĐIỂM:
 * - Hard to test: Singleton state persist giữa tests
 * - Global state: Có thể gây side effects
 * 
 * 💡 ALTERNATIVE: Dependency Injection
 *    → Inject API client vào components (testable hơn)
 */

---

### **🚀 PHẦN 4: CODE ORGANIZATION & BEST PRACTICES (Tổ Chức Code & Thực Hành Tốt)**

```typescript
/**
 * 📋 BEST PRACTICES ĐỂ CODE SCALE TỐT:
 * 
 * 1️⃣ SINGLE RESPONSIBILITY (Trách Nhiệm Đơn Nhất)
 * 2️⃣ DRY (Don't Repeat Yourself)
 * 3️⃣ KISS (Keep It Simple, Stupid)
 * 4️⃣ YAGNI (You Aren't Gonna Need It)
 * 5️⃣ Dependency Injection
 * 6️⃣ Error Boundaries
 * 7️⃣ Code Splitting & Lazy Loading
 * 8️⃣ Performance Optimization
 */

// ===================================================
// 1️⃣ SINGLE RESPONSIBILITY PRINCIPLE
// ===================================================

// ❌ BAD: 1 component làm QUÁ NHIỀU việc
const UserDashboard = () => {
  const [user, setUser] = useState(null);
  const [orders, setOrders] = useState([]);
  const [products, setProducts] = useState([]);
  
  // Fetch user ❌
  useEffect(() => {
    fetch('/api/user').then(res => res.json()).then(setUser);
  }, []);

  // Fetch orders ❌
  useEffect(() => {
    fetch('/api/orders').then(res => res.json()).then(setOrders);
  }, []);

  // Fetch products ❌
  useEffect(() => {
    fetch('/api/products').then(res => res.json()).then(setProducts);
  }, []);

  // Render user info ❌
  // Render orders table ❌
  // Render products grid ❌
  // → Component làm QUÁ NHIỀU việc!
};

// ✅ GOOD: Chia nhỏ thành nhiều components, mỗi component 1 trách nhiệm

// Component 1: Chỉ hiển thị user info
const UserInfo: React.FC<{ user: User }> = ({ user }) => {
  return (
    <div>
      <h2>{user.name}</h2>
      <p>{user.email}</p>
    </div>
  );
};

// Component 2: Chỉ hiển thị orders
const OrderList: React.FC<{ orders: Order[] }> = ({ orders }) => {
  return (
    <table>
      {orders.map(order => (
        <tr key={order.id}>
          <td>{order.id}</td>
          <td>${order.total}</td>
        </tr>
      ))}
    </table>
  );
};

// Component 3: Chỉ hiển thị products
const ProductGrid: React.FC<{ products: Product[] }> = ({ products }) => {
  return (
    <div className="grid">
      {products.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
};

// Container: Chỉ fetch data và orchestrate (điều phối)
const UserDashboard = () => {
  const { data: user } = useQuery({ queryKey: ['user'], queryFn: fetchUser });
  const { data: orders } = useQuery({ queryKey: ['orders'], queryFn: fetchOrders });
  const { data: products } = useQuery({ queryKey: ['products'], queryFn: fetchProducts });

  return (
    <div>
      <UserInfo user={user} />
      <OrderList orders={orders} />
      <ProductGrid products={products} />
    </div>
  );
};

// ===================================================
// 2️⃣ ERROR BOUNDARIES
// ===================================================

/**
 * ⚠️ VẤN ĐỀ:
 * 1 component crash → TOÀN BỘ APP crash (blank screen)
 * 
 * ✅ GIẢI PHÁP:
 * Wrap components trong Error Boundary
 * → Component crash → hiện fallback UI (không crash app)
 */

class ErrorBoundary extends React.Component<
  { children: React.ReactNode; fallback: React.ReactNode },
  { hasError: boolean }
> {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error) {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
    // Log error to service (Sentry, LogRocket...)
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback;
    }

    return this.props.children;
  }
}

// ✅ Usage: Wrap risky components
const App = () => {
  return (
    <div>
      {/* Dashboard crash → chỉ hiện fallback, app vẫn hoạt động */}
      <ErrorBoundary fallback={<div>Dashboard failed to load</div>}>
        <Dashboard />
      </ErrorBoundary>

      {/* Orders crash → chỉ Orders fail, Dashboard vẫn OK */}
      <ErrorBoundary fallback={<div>Orders failed to load</div>}>
        <Orders />
      </ErrorBoundary>
    </div>
  );
};

// ===================================================
// 3️⃣ CODE SPLITTING & LAZY LOADING
// ===================================================

/**
 * 🎯 MỤC ĐÍCH:
 * Chỉ load code KHI CẦN (on-demand)
 * → Initial bundle nhỏ hơn → Trang load nhanh hơn
 */

// ❌ BAD: Load tất cả routes ngay từ đầu
import Dashboard from './pages/Dashboard';  // 500 KB
import Orders from './pages/Orders';        // 300 KB
import Products from './pages/Products';    // 400 KB
import Settings from './pages/Settings';    // 200 KB

// Total bundle: 1.4 MB
// User vào /dashboard → phải tải 1.4 MB (dù chỉ cần 500 KB) ❌

// ✅ GOOD: Lazy load routes
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Orders = lazy(() => import('./pages/Orders'));
const Products = lazy(() => import('./pages/Products'));
const Settings = lazy(() => import('./pages/Settings'));

const App = () => {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/orders" element={<Orders />} />
        <Route path="/products" element={<Products />} />
        <Route path="/settings" element={<Settings />} />
      </Routes>
    </Suspense>
  );
};

// ✅ Kết quả:
// User vào /dashboard:
//   - Initial load: vendor.js (300 KB) + main.js (50 KB) = 350 KB
//   - Dashboard chunk: 500 KB
//   - Total: 850 KB thay vì 1.4 MB (39% nhỏ hơn!)

// ===================================================
// 4️⃣ PERFORMANCE OPTIMIZATION
// ===================================================

/**
 * 🚀 KỸ THUẬT TỐI ƯU PERFORMANCE:
 * 
 * 1. React.memo: Tránh re-render không cần thiết
 * 2. useMemo: Cache expensive calculations
 * 3. useCallback: Cache functions (tránh re-create)
 * 4. Virtual Scrolling: Render chỉ items visible
 * 5. Debounce/Throttle: Giảm số lần gọi hàm
 */

// Example 1: React.memo
// ❌ BAD: Child re-render mỗi khi Parent re-render (dù props không đổi)
const ExpensiveChild = ({ data }) => {
  console.log('ExpensiveChild rendered');  // Log mỗi lần render
  
  // Expensive calculation (tính toán nặng)
  const result = data.map(item => /* complex calculation */ item);
  
  return <div>{result}</div>;
};

const Parent = () => {
  const [count, setCount] = useState(0);  // State không liên quan
  const data = [1, 2, 3];  // Data không đổi

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <ExpensiveChild data={data} />
      {/* ❌ Click button → count thay đổi → Parent re-render
          → ExpensiveChild re-render (dù data không đổi!) */}
    </div>
  );
};

// ✅ GOOD: Dùng React.memo
const ExpensiveChild = React.memo(({ data }) => {
  console.log('ExpensiveChild rendered');
  const result = data.map(item => /* complex calculation */ item);
  return <div>{result}</div>;
});
// ✅ Child CHỈ re-render khi props thay đổi

// Example 2: useMemo cho expensive calculations
const ProductList = ({ products, searchTerm }) => {
  // ❌ BAD: Filter mỗi lần render (dù searchTerm không đổi)
  const filtered = products.filter(p => 
    p.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // ✅ GOOD: Cache filtered result
  const filtered = useMemo(() => {
    return products.filter(p => 
      p.name.toLowerCase().includes(searchTerm.toLowerCase())
    );
  }, [products, searchTerm]);  // Chỉ re-calculate khi dependencies đổi

  return <div>{filtered.map(p => <ProductCard product={p} />)}</div>;
};

// Example 3: Virtual Scrolling với react-window
import { FixedSizeList } from 'react-window';

const VirtualizedList = ({ items }) => {
  // ✅ Chỉ render items VISIBLE (VD: 10 items)
  // Không render 10,000 items cùng lúc ❌
  
  const Row = ({ index, style }) => (
    <div style={style}>
      {items[index].name}
    </div>
  );

  return (
    <FixedSizeList
      height={600}        // Viewport height
      itemCount={items.length}  // 10,000 items
      itemSize={50}       // Mỗi item cao 50px
      width="100%"
    >
      {Row}
    </FixedSizeList>
  );
};

/**
 * 📊 PERFORMANCE COMPARISON:
 * 
 * ❌ WITHOUT Optimization (10,000 items):
 * - Initial render: 5 seconds
 * - Re-render on scroll: 500ms (lag!)
 * - Memory: 200 MB
 * 
 * ✅ WITH Virtual Scrolling:
 * - Initial render: 100ms (50x faster)
 * - Re-render on scroll: 16ms (smooth 60fps)
 * - Memory: 20 MB (10x less)
 */

---

### **📊 PHẦN 5: SUMMARY & COMPARISON (Tóm Tắt & So Sánh)**

```typescript
/**
 * 🎯 DESIGN SYSTEM - TẠI SAO CẦN?
 * 
 * ✅ CONSISTENCY (Nhất Quán):
 *    → Tất cả UI elements giống nhau
 *    → User không bối rối
 * 
 * ✅ SCALABILITY (Mở Rộng):
 *    → 100 developers vẫn consistent
 *    → Thêm 50 pages mới dễ dàng
 * 
 * ✅ SPEED (Tốc Độ):
 *    → Build page: 1 ngày thay vì 1 tuần
 *    → Copy từ Storybook → paste
 * 
 * ✅ MAINTAINABILITY (Bảo Trì):
 *    → Đổi màu: 1 file thay vì 100 files
 *    → Fix bug: 1 component thay vì 50 chỗ
 */

/**
 * 🏗️ SCALABLE FE ARCHITECTURE - 7 BƯỚC:
 * 
 * 1️⃣ Layered Architecture: Presentation, Business Logic, Data Access, Infrastructure
 * 2️⃣ Feature-based Folder Structure: Nhóm theo feature, không theo type
 * 3️⃣ Design System: Tokens + Components + Guidelines + Docs
 * 4️⃣ State Strategy: Local, Shared, Global, Server state (phân loại rõ ràng)
 * 5️⃣ Code Organization: Single Responsibility, DRY, KISS
 * 6️⃣ Tooling: Storybook, TypeScript, ESLint, Prettier
 * 7️⃣ Testing: Unit, Integration, E2E + Documentation
 */

/**
 * 🎨 DESIGN PATTERNS - KHI NÀO DÙNG?
 * 
 * 1️⃣ Container/Presentational:
 *    → Tách logic ra khỏi UI
 *    → Dùng: Hầu hết components
 * 
 * 2️⃣ Compound Components:
 *    → Components linh hoạt, customizable layout
 *    → Dùng: Tabs, Menu, Accordion, Dialog
 * 
 * 3️⃣ Custom Hooks:
 *    → Tái sử dụng stateful logic
 *    → Dùng: Form validation, Debounce, LocalStorage sync
 * 
 * 4️⃣ Observer Pattern (Pub/Sub):
 *    → Cross-component communication
 *    → Dùng: Notifications, Real-time updates, Analytics
 * 
 * 5️⃣ Singleton:
 *    → 1 instance duy nhất
 *    → Dùng: API client, Logger, Config manager
 */
```

---

**📊 COMPARISON TABLE (Bảng So Sánh)**

| Aspect | ❌ WITHOUT Design System | ✅ WITH Design System |
|--------|---------------------------|------------------------|
| **Consistency** | 10 loại Button khác nhau | 1 Button, 3 variants |
| **Colors** | 50+ màu hardcoded | 10 màu trong tokens |
| **Maintenance** | Đổi màu: 100 files, 3 ngày | Đổi màu: 1 file, 5 phút |
| **Developer Speed** | Build page: 1 tuần | Build page: 1 ngày |
| **Onboarding** | 2-3 tuần học codebase | 3-5 ngày (có Storybook) |
| **Design-Dev Sync** | "Button màu gì?" (mơ hồ) | "Button variant='primary'" (rõ ràng) |
| **Accessibility** | Developers quên implement | Built-in (ARIA, keyboard nav) |

| Architecture | ❌ Type-based Structure | ✅ Feature-based Structure |
|--------------|-------------------------|----------------------------|
| **Folder Structure** | components/ (100 files) | features/auth/, features/orders/ |
| **Find Code** | Tìm trong 3 folders | Tìm trong 1 folder |
| **Team Autonomy** | Conflict nhiều | Ít conflict (isolated) |
| **Code Splitting** | Khó | Dễ (lazy load theo feature) |
| **Scalability** | Khó scale (100+ files/folder) | Dễ scale (mỗi feature độc lập) |

| Pattern | Use Case | ✅ Benefits | ⚠️ Drawbacks |
|---------|----------|-------------|--------------|
| **Container/Presentational** | Hầu hết components | Dễ test, reusable UI | Thêm boilerplate |
| **Compound Components** | Tabs, Menu, Accordion | Flexibility, API rõ ràng | Phức tạp hơn |
| **Custom Hooks** | Form, Debounce, Storage | Reusability, Testability | Cần hiểu hooks tốt |
| **Observer (Pub/Sub)** | Notifications, Events | Loose coupling | Hard to debug |
| **Singleton** | API client, Logger | Shared state, 1 instance | Hard to test |

---

**💡 KEY TAKEAWAYS (Điểm Chính Cần Nhớ)**

```typescript
/**
 * ✅ DESIGN SYSTEM:
 * - Tokens (colors, spacing, typography) → 1 source of truth
 * - Components → Reusable, accessible
 * - Documentation (Storybook) → Onboarding nhanh
 * 
 * ✅ SCALABLE ARCHITECTURE:
 * - Feature-based structure → Dễ tìm, dễ scale
 * - Layered architecture → Separation of concerns
 * - State strategy → Local, Shared, Global, Server (phân loại rõ)
 * 
 * ✅ DESIGN PATTERNS:
 * - Container/Presentational → Tách logic/UI
 * - Compound Components → Flexibility
 * - Custom Hooks → Reuse stateful logic
 * - Observer → Cross-component events
 * - Singleton → Shared resources
 * 
 * ✅ PERFORMANCE:
 * - Code splitting → Load on-demand
 * - React.memo → Tránh re-render
 * - useMemo/useCallback → Cache
 * - Virtual scrolling → Large lists
 * - Error boundaries → Graceful failures
 * 
 * 🎯 MỤC TIÊU CUỐI CÙNG:
 * - 100 developers vẫn consistent
 * - 500+ components vẫn maintainable
 * - Thêm features mới không phá code cũ
 * - Performance tốt (< 3s load time)
 * - Developer Experience tuyệt vời (< 1 tuần onboarding)
 */
```

---

**🔥 REAL-WORLD EXAMPLE: TRADING PLATFORM**

```typescript
// Áp dụng TẤT CẢ principles vào 1 Trading App thực tế

/**
 * 📁 FOLDER STRUCTURE (Feature-based)
 */
/*
src/
├── features/
│   ├── trading/              # Feature: Trading
│   │   ├── components/
│   │   │   ├── OrderForm/    # Compound Component
│   │   │   ├── OrderBook/
│   │   │   └── TradeHistory/
│   │   ├── hooks/
│   │   │   ├── useOrderForm.ts      # Custom Hook
│   │   │   └── useRealTimePrice.ts  # Observer Pattern
│   │   ├── services/
│   │   │   └── tradingService.ts    # Singleton
│   │   └── store/
│   │       └── tradingStore.ts      # State Management
│   │
│   ├── portfolio/
│   │   ├── components/
│   │   │   ├── PortfolioSummary/    # Presentational
│   │   │   └── AssetList/
│   │   ├── hooks/
│   │   │   └── usePortfolio.ts      # Custom Hook + React Query
│   │   └── services/
│   │       └── portfolioService.ts
│   │
│   └── market/
│       ├── components/
│       │   ├── PriceChart/          # React.memo + useMemo
│       │   └── MarketOverview/
│       └── hooks/
│           └── useMarketData.ts
│
├── shared/
│   ├── components/              # Design System
│   │   ├── Button/              # Tokens-based
│   │   ├── Input/
│   │   └── Table/               # Virtual Scrolling
│   └── hooks/
│       ├── useDebounce.ts
│       └── useWebSocket.ts      # Observer Pattern
│
└── core/
    ├── theme/
    │   ├── tokens/              # Design Tokens
    │   │   ├── colors.ts
    │   │   ├── spacing.ts
    │   │   └── typography.ts
    │   └── GlobalStyles.ts
    │
    └── api/
        └── apiClient.ts         # Singleton Pattern
*/

/**
 * 📊 RESULTS (Kết Quả):
 * 
 * ✅ BEFORE Refactoring:
 * - 50 developers, tranh cãi về UI
 * - Build page mới: 1-2 tuần
 * - Bundle size: 3.5 MB
 * - Load time: 8 seconds
 * - Onboarding: 1 tháng
 * 
 * ✅ AFTER Refactoring (với Design System + Patterns):
 * - 50 developers, consistent UI
 * - Build page mới: 2-3 ngày (7x nhanh hơn)
 * - Bundle size: 1.2 MB (66% nhỏ hơn)
 * - Load time: 2.5 seconds (3.2x nhanh hơn)
 * - Onboarding: 1 tuần (4x nhanh hơn)
 */
```

---

## 64. State Management - Redux vs Zustand vs Context API: Phân Biệt, Ưu Nhược Điểm, Cách Hoạt Động

**❓ Câu Hỏi:**
> "Store management: Redux, zustand, context. Phân biệt chúng, ưu và nhược điểm, hoạt động như thế nào, tại sao lại dùng chúng?"

**📋 Phân Tích:**
- **Redux, Zustand, Context API** khác nhau thế nào?
- **Ưu điểm & Nhược điểm** của từng thư viện
- **Cách hoạt động** bên trong (internal mechanism)
- **Khi nào dùng** từng loại?
- **Performance comparison** (so sánh hiệu suất)

---

### **🎯 PHẦN 1: TẠI SAO CẦN STATE MANAGEMENT? (Why State Management?)**

```typescript
/**
 * 🔥 VẤN ĐỀ: PROP DRILLING (Truyền Props Qua Nhiều Tầng)
 * 
 * Khi app lớn, truyền state từ component cha → con → cháu → chắt...
 * → Code rối, khó maintain, component trung gian không cần props nhưng phải nhận
 */

// ❌ PROBLEM: Prop Drilling Hell
const App = () => {
  const [user, setUser] = useState({ name: 'John', role: 'admin' });

  return <Dashboard user={user} setUser={setUser} />;
};

const Dashboard = ({ user, setUser }) => {
  // ❌ Dashboard không dùng user, nhưng phải nhận để pass xuống
  return <Sidebar user={user} setUser={setUser} />;
};

const Sidebar = ({ user, setUser }) => {
  // ❌ Sidebar cũng không dùng, nhưng phải nhận để pass xuống
  return <UserMenu user={user} setUser={setUser} />;
};

const UserMenu = ({ user, setUser }) => {
  // ✅ CHỈ UserMenu mới dùng user!
  return (
    <div>
      {user.name} ({user.role})
      <button onClick={() => setUser({ ...user, role: 'user' })}>
        Change Role
      </button>
    </div>
  );
};

/**
 * ❌ VẤN ĐỀ:
 * - App → Dashboard → Sidebar → UserMenu (4 tầng!)
 * - Dashboard, Sidebar không cần user nhưng phải nhận props
 * - Thêm 1 props mới → phải sửa 4 components
 * - Rất khó maintain!
 */

// ✅ GIẢI PHÁP: STATE MANAGEMENT
// UserMenu truy cập TRỰC TIẾP vào global state
// → Không cần prop drilling!

const UserMenu = () => {
  const { user, setUser } = useGlobalState();  // ✅ Lấy trực tiếp từ store
  
  return (
    <div>
      {user.name} ({user.role})
      <button onClick={() => setUser({ ...user, role: 'user' })}>
        Change Role
      </button>
    </div>
  );
};

/**
 * ✅ LỢI ÍCH:
 * - Không cần truyền props qua Dashboard, Sidebar
 * - Thêm props mới → chỉ sửa 1 component (UserMenu)
 * - Code sạch, dễ maintain
 */

// ===================================================
// 🎯 3 GIẢI PHÁP STATE MANAGEMENT
// ===================================================

/**
 * 1️⃣ CONTEXT API (Built-in React)
 *    → Đơn giản, không cần library
 *    → Dùng cho app nhỏ/vừa
 * 
 * 2️⃣ ZUSTAND (Modern, lightweight)
 *    → Đơn giản như Context, nhưng performance tốt hơn
 *    → Dùng cho app vừa/lớn
 * 
 * 3️⃣ REDUX (Traditional, powerful)
 *    → Phức tạp, nhiều boilerplate
 *    → Dùng cho app cực lớn, cần DevTools, middleware
 */
```

---

### **📦 PHẦN 2: CONTEXT API (React Built-in)**

```typescript
/**
 * 🎯 CONTEXT API LÀ GÌ?
 * 
 * Built-in API của React để CHIA SẺ STATE giữa nhiều components
 * mà KHÔNG CẦN truyền props qua từng tầng.
 * 
 * 🔥 CÁCH HOẠT ĐỘNG:
 * 1. Tạo Context với createContext()
 * 2. Wrap app trong <Provider value={state}>
 * 3. Components dùng useContext() để lấy state
 */

// ===================================================
// ✅ IMPLEMENTATION: Context API
// ===================================================

// Step 1: Tạo Context
import { createContext, useContext, useState } from 'react';

interface User {
  name: string;
  email: string;
  role: 'admin' | 'user';
}

interface UserContextType {
  user: User | null;
  login: (user: User) => void;
  logout: () => void;
  updateRole: (role: 'admin' | 'user') => void;
}

const UserContext = createContext<UserContextType | undefined>(undefined);

// Step 2: Tạo Provider
export const UserProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);

  const login = (userData: User) => {
    setUser(userData);
  };

  const logout = () => {
    setUser(null);
  };

  const updateRole = (role: 'admin' | 'user') => {
    if (user) {
      setUser({ ...user, role });
    }
  };

  return (
    <UserContext.Provider value={{ user, login, logout, updateRole }}>
      {children}
    </UserContext.Provider>
  );
};

// Step 3: Tạo custom hook
export const useUser = () => {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUser must be used within UserProvider');
  }
  return context;
};

// Step 4: Wrap App trong Provider
const App = () => {
  return (
    <UserProvider>
      <Dashboard />
    </UserProvider>
  );
};

// Step 5: Dùng trong components
const UserMenu = () => {
  const { user, logout, updateRole } = useUser();  // ✅ Lấy trực tiếp

  if (!user) return <div>Please login</div>;

  return (
    <div>
      <h3>{user.name}</h3>
      <p>{user.email} - {user.role}</p>
      <button onClick={() => updateRole('admin')}>Make Admin</button>
      <button onClick={logout}>Logout</button>
    </div>
  );
};

const AnotherComponent = () => {
  const { user } = useUser();  // ✅ Component khác cũng dùng được

  return <div>Welcome, {user?.name}</div>;
};

/**
 * ✅ ƯU ĐIỂM CONTEXT API:
 * 
 * 1️⃣ BUILT-IN (Có sẵn):
 *    → Không cần cài thêm library
 *    → Bundle size nhỏ
 * 
 * 2️⃣ SIMPLE (Đơn giản):
 *    → Dễ học, dễ dùng
 *    → Ít boilerplate
 * 
 * 3️⃣ TYPE-SAFE (An toàn kiểu):
 *    → TypeScript support tốt
 *    → Auto-complete trong IDE
 * 
 * ❌ NHƯỢC ĐIỂM CONTEXT API:
 * 
 * 1️⃣ PERFORMANCE ISSUES (Vấn đề hiệu suất):
 *    → Khi state thay đổi → TẤT CẢ components dùng Context RE-RENDER
 *    → Dù chỉ cần 1 field trong state!
 * 
 * 2️⃣ NO BUILT-IN DEVTOOLS:
 *    → Không có DevTools để debug
 *    → Khó track state changes
 * 
 * 3️⃣ NO MIDDLEWARE:
 *    → Không có logger, persist, thunk...
 *    → Phải tự implement
 * 
 * 4️⃣ MULTIPLE CONTEXTS = PROVIDER HELL:
 *    → 10 contexts → 10 Providers lồng nhau
 */

// ===================================================
// ⚠️ CONTEXT API PERFORMANCE PROBLEM
// ===================================================

const UserContext = createContext<UserContextType | undefined>(undefined);

const UserProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [user, setUser] = useState({
    name: 'John',
    email: 'john@example.com',
    role: 'admin',
    preferences: { theme: 'dark', language: 'en' },
  });

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
};

// Component 1: Chỉ dùng user.name
const UserName = () => {
  const { user } = useUser();
  console.log('UserName rendered');  // 👈 Log để track re-renders
  
  return <div>{user.name}</div>;
};

// Component 2: Chỉ dùng user.email
const UserEmail = () => {
  const { user } = useUser();
  console.log('UserEmail rendered');  // 👈 Log để track re-renders
  
  return <div>{user.email}</div>;
};

// Component 3: Chỉ dùng user.preferences.theme
const ThemeToggle = () => {
  const { user, setUser } = useUser();
  console.log('ThemeToggle rendered');  // 👈 Log để track re-renders

  const toggleTheme = () => {
    setUser({
      ...user,
      preferences: {
        ...user.preferences,
        theme: user.preferences.theme === 'dark' ? 'light' : 'dark'
      }
    });
  };

  return <button onClick={toggleTheme}>Toggle Theme</button>;
};

/**
 * ❌ VẤN ĐỀ PERFORMANCE:
 * 
 * Click "Toggle Theme" → Chỉ đổi user.preferences.theme
 * 
 * NHƯNG:
 * - UserName rendered  ❌ (không cần re-render, name không đổi)
 * - UserEmail rendered ❌ (không cần re-render, email không đổi)
 * - ThemeToggle rendered ✅ (cần re-render, theme đổi)
 * 
 * → Context re-render TẤT CẢ components dùng useUser()
 * → Ngay cả khi chỉ 1 field thay đổi!
 * 
 * 📊 IMPACT:
 * - 100 components dùng useUser() → 100 re-renders
 * - App lag, slow, poor UX
 */

// ✅ WORKAROUND: Split contexts
const UserNameContext = createContext(null);
const UserEmailContext = createContext(null);
const UserPreferencesContext = createContext(null);

// → Phức tạp, nhiều Providers lồng nhau (Provider Hell)
```

---

### **⚡ PHẦN 3: ZUSTAND (Modern & Lightweight)**

```typescript
/**
 * 🎯 ZUSTAND LÀ GÌ?
 * 
 * State management library ĐƠN GIẢN, NHANH, ÍT BOILERPLATE.
 * 
 * 🔥 ĐẶC ĐIỂM:
 * - Không cần Provider (không có Provider Hell)
 * - Hooks-based (dùng như useState)
 * - Auto-optimization (chỉ re-render components cần thiết)
 * - TypeScript support tốt
 * - Bundle size nhỏ (1.2 KB gzipped)
 */

// ===================================================
// ✅ IMPLEMENTATION: Zustand
// ===================================================

// Step 1: Install
// npm install zustand

// Step 2: Tạo store
import create from 'zustand';

interface User {
  name: string;
  email: string;
  role: 'admin' | 'user';
  preferences: {
    theme: 'light' | 'dark';
    language: string;
  };
}

interface UserStore {
  user: User | null;
  login: (user: User) => void;
  logout: () => void;
  updateRole: (role: 'admin' | 'user') => void;
  toggleTheme: () => void;
}

export const useUserStore = create<UserStore>((set) => ({
  user: null,

  login: (user) => set({ user }),

  logout: () => set({ user: null }),

  updateRole: (role) => set((state) => ({
    user: state.user ? { ...state.user, role } : null
  })),

  toggleTheme: () => set((state) => ({
    user: state.user ? {
      ...state.user,
      preferences: {
        ...state.user.preferences,
        theme: state.user.preferences.theme === 'dark' ? 'light' : 'dark'
      }
    } : null
  })),
}));

// Step 3: Dùng trong components (KHÔNG CẦN PROVIDER!)
const UserName = () => {
  // ✅ CHỈ subscribe vào user.name
  const name = useUserStore((state) => state.user?.name);
  console.log('UserName rendered');
  
  return <div>{name}</div>;
};

const UserEmail = () => {
  // ✅ CHỈ subscribe vào user.email
  const email = useUserStore((state) => state.user?.email);
  console.log('UserEmail rendered');
  
  return <div>{email}</div>;
};

const ThemeToggle = () => {
  // ✅ CHỈ subscribe vào user.preferences.theme và toggleTheme
  const theme = useUserStore((state) => state.user?.preferences.theme);
  const toggleTheme = useUserStore((state) => state.toggleTheme);
  console.log('ThemeToggle rendered');

  return (
    <button onClick={toggleTheme}>
      Theme: {theme}
    </button>
  );
};

/**
 * ✅ ZUSTAND AUTO-OPTIMIZATION:
 * 
 * Click "Toggle Theme" → Chỉ đổi user.preferences.theme
 * 
 * RESULT:
 * - UserName rendered  ❌ (KHÔNG re-render, name không đổi) ✅
 * - UserEmail rendered ❌ (KHÔNG re-render, email không đổi) ✅
 * - ThemeToggle rendered ✅ (re-render, theme đổi) ✅
 * 
 * → Zustand CHỈ re-render components subscribe vào field thay đổi!
 * → Performance TỐT HƠN Context API nhiều!
 */

// ===================================================
// ✅ ZUSTAND ADVANCED FEATURES
// ===================================================

// 1️⃣ PERSIST (Lưu state vào localStorage)
import { persist } from 'zustand/middleware';

export const useUserStore = create(
  persist<UserStore>(
    (set) => ({
      user: null,
      login: (user) => set({ user }),
      logout: () => set({ user: null }),
      // ... other actions
    }),
    {
      name: 'user-storage',  // localStorage key
    }
  )
);

// ✅ State tự động lưu vào localStorage
// ✅ Reload page → state vẫn còn

// 2️⃣ DEVTOOLS (Redux DevTools support)
import { devtools } from 'zustand/middleware';

export const useUserStore = create(
  devtools<UserStore>(
    (set) => ({
      user: null,
      login: (user) => set({ user }, false, 'user/login'),  // Action name
      logout: () => set({ user: null }, false, 'user/logout'),
      // ... other actions
    }),
    { name: 'UserStore' }
  )
);

// ✅ Mở Redux DevTools → thấy được state changes
// ✅ Time-travel debugging

// 3️⃣ IMMER (Immutable updates dễ dàng)
import { immer } from 'zustand/middleware/immer';

export const useUserStore = create(
  immer<UserStore>((set) => ({
    user: null,
    
    updateRole: (role) => set((state) => {
      // ✅ Mutate trực tiếp (Immer tự chuyển thành immutable update)
      if (state.user) {
        state.user.role = role;  // Dễ đọc hơn spread operator!
      }
    }),
  }))
);

/**
 * ✅ ƯU ĐIỂM ZUSTAND:
 * 
 * 1️⃣ SIMPLE API:
 *    → Dễ học, dễ dùng
 *    → Ít boilerplate (không có actions, reducers riêng)
 * 
 * 2️⃣ PERFORMANCE:
 *    → Auto-optimization (chỉ re-render components cần thiết)
 *    → Nhanh hơn Context API
 * 
 * 3️⃣ NO PROVIDER:
 *    → Không cần wrap app trong Provider
 *    → Không có Provider Hell
 * 
 * 4️⃣ SMALL BUNDLE:
 *    → 1.2 KB gzipped (nhỏ hơn Redux 10x)
 * 
 * 5️⃣ DEVTOOLS:
 *    → Redux DevTools support
 *    → Time-travel debugging
 * 
 * 6️⃣ MIDDLEWARE:
 *    → Persist, Immer, Devtools...
 *    → Dễ extend
 * 
 * ❌ NHƯỢC ĐIỂM ZUSTAND:
 * 
 * 1️⃣ KHÔNG PHẢI BUILT-IN:
 *    → Phải cài thêm library (1.2 KB)
 * 
 * 2️⃣ ÍT ECOSYSTEM HƠN REDUX:
 *    → Ít plugins, tutorials
 *    → Community nhỏ hơn Redux
 * 
 * 3️⃣ KHÔNG CÓ STRICT STRUCTURE:
 *    → Dễ viết code không nhất quán
 *    → Cần conventions rõ ràng
 */
```

---

### **🏛️ PHẦN 4: REDUX (Traditional & Powerful)**

```typescript
/**
 * 🎯 REDUX LÀ GÌ?
 * 
 * State management library MẠNH MẼ, theo kiến trúc FLUX.
 * 
 * 🔥 CORE CONCEPTS:
 * - Store: Lưu toàn bộ state
 * - Actions: Mô tả "điều gì xảy ra"
 * - Reducers: Hàm xử lý state dựa trên action
 * - Dispatch: Gửi action đến store
 * 
 * 📊 DATA FLOW (Luồng dữ liệu):
 * Component → dispatch(action) → Reducer → Update Store → Component re-render
 */

// ===================================================
// ✅ IMPLEMENTATION: Redux (với Redux Toolkit - modern way)
// ===================================================

// Step 1: Install
// npm install @reduxjs/toolkit react-redux

// Step 2: Tạo Slice (Reducer + Actions)
import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface User {
  name: string;
  email: string;
  role: 'admin' | 'user';
  preferences: {
    theme: 'light' | 'dark';
    language: string;
  };
}

interface UserState {
  user: User | null;
  loading: boolean;
  error: string | null;
}

const initialState: UserState = {
  user: null,
  loading: false,
  error: null,
};

const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    // Action: login
    loginStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    loginSuccess: (state, action: PayloadAction<User>) => {
      state.user = action.payload;
      state.loading = false;
    },
    loginFailure: (state, action: PayloadAction<string>) => {
      state.loading = false;
      state.error = action.payload;
    },
    
    // Action: logout
    logout: (state) => {
      state.user = null;
      state.error = null;
    },
    
    // Action: updateRole
    updateRole: (state, action: PayloadAction<'admin' | 'user'>) => {
      if (state.user) {
        state.user.role = action.payload;
      }
    },
    
    // Action: toggleTheme
    toggleTheme: (state) => {
      if (state.user) {
        state.user.preferences.theme = 
          state.user.preferences.theme === 'dark' ? 'light' : 'dark';
      }
    },
  },
});

export const {
  loginStart,
  loginSuccess,
  loginFailure,
  logout,
  updateRole,
  toggleTheme,
} = userSlice.actions;

export default userSlice.reducer;

// Step 3: Tạo Store
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
    // cart: cartReducer,
    // products: productsReducer,
    // ... other reducers
  },
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Step 4: Wrap App trong Provider
import { Provider } from 'react-redux';

const App = () => {
  return (
    <Provider store={store}>
      <Dashboard />
    </Provider>
  );
};

// Step 5: Dùng trong components
import { useSelector, useDispatch } from 'react-redux';
import { RootState, AppDispatch } from './store';

const UserName = () => {
  // ✅ CHỈ subscribe vào user.name
  const name = useSelector((state: RootState) => state.user.user?.name);
  console.log('UserName rendered');
  
  return <div>{name}</div>;
};

const UserEmail = () => {
  // ✅ CHỈ subscribe vào user.email
  const email = useSelector((state: RootState) => state.user.user?.email);
  console.log('UserEmail rendered');
  
  return <div>{email}</div>;
};

const ThemeToggle = () => {
  const theme = useSelector((state: RootState) => 
    state.user.user?.preferences.theme
  );
  const dispatch = useDispatch<AppDispatch>();
  console.log('ThemeToggle rendered');

  return (
    <button onClick={() => dispatch(toggleTheme())}>
      Theme: {theme}
    </button>
  );
};

/**
 * ✅ REDUX AUTO-OPTIMIZATION (giống Zustand):
 * 
 * Click "Toggle Theme" → Chỉ đổi user.preferences.theme
 * 
 * RESULT:
 * - UserName rendered  ❌ (KHÔNG re-render, name không đổi) ✅
 * - UserEmail rendered ❌ (KHÔNG re-render, email không đổi) ✅
 * - ThemeToggle rendered ✅ (re-render, theme đổi) ✅
 * 
 * → Redux cũng CHỈ re-render components subscribe vào field thay đổi!
 */

// ===================================================
// 🚀 REDUX ASYNC ACTIONS (với createAsyncThunk)
// ===================================================

import { createAsyncThunk } from '@reduxjs/toolkit';

// Async action: Login với API call
export const loginAsync = createAsyncThunk(
  'user/login',  // Action type prefix
  async (credentials: { email: string; password: string }, { rejectWithValue }) => {
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(credentials),
      });

      if (!response.ok) {
        throw new Error('Login failed');
      }

      const user = await response.json();
      return user;  // ✅ Return user data
    } catch (error) {
      return rejectWithValue(error.message);  // ❌ Return error
    }
  }
);

// Update slice để handle async action
const userSlice = createSlice({
  name: 'user',
  initialState,
  reducers: {
    // ... sync actions
  },
  extraReducers: (builder) => {
    builder
      // loginAsync.pending
      .addCase(loginAsync.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      // loginAsync.fulfilled
      .addCase(loginAsync.fulfilled, (state, action) => {
        state.user = action.payload;
        state.loading = false;
      })
      // loginAsync.rejected
      .addCase(loginAsync.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

// Dùng trong component
const LoginForm = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { loading, error } = useSelector((state: RootState) => state.user);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    // ✅ Dispatch async action
    const result = await dispatch(loginAsync({
      email: 'user@example.com',
      password: 'password123',
    }));

    if (loginAsync.fulfilled.match(result)) {
      // ✅ Login thành công
      console.log('Logged in:', result.payload);
    } else {
      // ❌ Login thất bại
      console.error('Error:', result.payload);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" placeholder="Email" />
      <input type="password" placeholder="Password" />
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}
      </button>
      {error && <div className="error">{error}</div>}
    </form>
  );
};

// ===================================================
// 🔧 REDUX MIDDLEWARE (Logger, Persist...)
// ===================================================

// Custom logger middleware
const loggerMiddleware = (store) => (next) => (action) => {
  console.log('Dispatching:', action);
  console.log('Previous State:', store.getState());
  
  const result = next(action);  // Pass action to reducer
  
  console.log('Next State:', store.getState());
  return result;
};

// Persist middleware (redux-persist)
import { persistStore, persistReducer } from 'redux-persist';
import storage from 'redux-persist/lib/storage';  // localStorage

const persistConfig = {
  key: 'root',
  storage,
  whitelist: ['user'],  // Chỉ persist user state
};

const persistedReducer = persistReducer(persistConfig, userReducer);

export const store = configureStore({
  reducer: {
    user: persistedReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: false,  // Tắt warning cho redux-persist
    }).concat(loggerMiddleware),
});

export const persistor = persistStore(store);

// Wrap App
import { PersistGate } from 'redux-persist/integration/react';

const App = () => {
  return (
    <Provider store={store}>
      <PersistGate loading={<div>Loading...</div>} persistor={persistor}>
        <Dashboard />
      </PersistGate>
    </Provider>
  );
};

/**
 * ✅ ƯU ĐIỂM REDUX:
 * 
 * 1️⃣ PREDICTABLE STATE:
 *    → Luồng dữ liệu rõ ràng (Action → Reducer → Store)
 *    → Dễ debug, dễ test
 * 
 * 2️⃣ DEVTOOLS MẠNH MẼ:
 *    → Redux DevTools (time-travel, state diff)
 *    → Track mọi action, state change
 * 
 * 3️⃣ MIDDLEWARE ECOSYSTEM:
 *    → Redux Thunk, Redux Saga (async)
 *    → Redux Persist (localStorage)
 *    → Logger, Router, Form...
 * 
 * 4️⃣ HUGE ECOSYSTEM:
 *    → Nhiều libraries, plugins
 *    → Nhiều tutorials, community lớn
 * 
 * 5️⃣ PERFORMANCE:
 *    → Auto-optimization như Zustand
 *    → Chỉ re-render components cần thiết
 * 
 * 6️⃣ SCALABILITY:
 *    → Dùng cho app CỰC LỚN (1000+ components)
 *    → Team lớn (50+ developers)
 * 
 * ❌ NHƯỢC ĐIỂM REDUX:
 * 
 * 1️⃣ BOILERPLATE NHIỀU:
 *    → Actions, Reducers, Types, Selectors...
 *    → Thêm 1 feature → phải tạo nhiều files
 * 
 * 2️⃣ LEARNING CURVE CAO:
 *    → Khái niệm phức tạp (Flux, Reducers, Middleware...)
 *    → Khó học cho beginners
 * 
 * 3️⃣ BUNDLE SIZE LỚN:
 *    → Redux + React-Redux: ~12 KB gzipped
 *    → Lớn hơn Zustand 10x
 * 
 * 4️⃣ CẦN PROVIDER:
 *    → Phải wrap app trong <Provider>
 *    → Nhiều stores → nhiều Providers
 */

---

### **📊 PHẦN 5: SO SÁNH CHI TIẾT (Detailed Comparison)**

```typescript
/**
 * 🎯 COMPARISON TABLE: Context API vs Zustand vs Redux
 */
```

| Feature | Context API | Zustand | Redux (RTK) |
|---------|-------------|---------|-------------|
| **Bundle Size** | 0 KB (built-in) | 1.2 KB | ~12 KB |
| **Setup Complexity** | Simple | Simple | Medium |
| **Boilerplate** | Low | Very Low | Medium |
| **Learning Curve** | Easy | Easy | Hard |
| **Performance** | Poor (re-render all) | Excellent (auto-opt) | Excellent (auto-opt) |
| **DevTools** | ❌ No | ✅ Redux DevTools | ✅ Redux DevTools |
| **Middleware** | ❌ No | ✅ Yes (Persist, Immer) | ✅ Yes (Thunk, Saga, Persist) |
| **TypeScript** | ✅ Good | ✅ Excellent | ✅ Excellent |
| **Provider Needed** | ✅ Yes (Provider Hell) | ❌ No | ✅ Yes |
| **Async Actions** | Manual | Manual | Built-in (createAsyncThunk) |
| **Computed Values** | Manual (useMemo) | Manual | Built-in (createSelector) |
| **Time-travel Debug** | ❌ No | ✅ Yes (with devtools) | ✅ Yes |
| **Ecosystem** | Small | Medium | Huge |
| **Community** | Medium | Growing | Very Large |
| **Use Case** | Small/Medium apps | Medium/Large apps | Large/Enterprise apps |

---

**🔥 PERFORMANCE COMPARISON (Benchmark)**

```typescript
/**
 * 📊 TEST SCENARIO:
 * - 1000 components subscribe to store
 * - Update 1 field in state
 * - Measure re-renders
 */

// Context API
// ❌ Result: 1000 components re-rendered (100% re-render rate)
// ⏱️ Time: 150ms

// Zustand
// ✅ Result: 1 component re-rendered (0.1% re-render rate)
// ⏱️ Time: 2ms (75x faster than Context)

// Redux (RTK)
// ✅ Result: 1 component re-rendered (0.1% re-render rate)
// ⏱️ Time: 3ms (50x faster than Context)
```

---

**💡 KHI NÀO DÙNG? (When to Use?)**

```typescript
/**
 * ✅ DÙNG CONTEXT API KHI:
 * 
 * 1️⃣ App nhỏ (< 10 components dùng state)
 * 2️⃣ State ít thay đổi (theme, language)
 * 3️⃣ Không cần DevTools
 * 4️⃣ Không muốn cài thêm library
 * 
 * VD:
 * - Theme provider (dark/light mode)
 * - Language provider (i18n)
 * - Auth context (user login status)
 */

// Example: Theme Context (ít thay đổi)
const ThemeContext = createContext({ theme: 'light', toggleTheme: () => {} });

const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

/**
 * ✅ DÙNG ZUSTAND KHI:
 * 
 * 1️⃣ App vừa/lớn (10-100 components dùng state)
 * 2️⃣ State thay đổi thường xuyên
 * 3️⃣ Cần performance tốt
 * 4️⃣ Muốn code đơn giản, ít boilerplate
 * 5️⃣ Cần DevTools để debug
 * 
 * VD:
 * - Shopping cart (add/remove items)
 * - User profile (update thông tin)
 * - Notifications (show/hide toast)
 * - Form state (multi-step forms)
 */

// Example: Shopping Cart với Zustand
import create from 'zustand';

interface CartStore {
  items: CartItem[];
  addItem: (item: CartItem) => void;
  removeItem: (id: string) => void;
  clearCart: () => void;
  total: number;
}

export const useCartStore = create<CartStore>((set, get) => ({
  items: [],
  
  addItem: (item) => set((state) => ({
    items: [...state.items, item]
  })),
  
  removeItem: (id) => set((state) => ({
    items: state.items.filter(item => item.id !== id)
  })),
  
  clearCart: () => set({ items: [] }),
  
  // Computed value (total price)
  get total() {
    return get().items.reduce((sum, item) => sum + item.price, 0);
  },
}));

/**
 * ✅ DÙNG REDUX KHI:
 * 
 * 1️⃣ App CỰC LỚN (100+ components dùng state)
 * 2️⃣ Team lớn (10+ developers)
 * 3️⃣ Cần structure rõ ràng (Actions, Reducers, Selectors)
 * 4️⃣ Cần middleware phức tạp (Saga, custom middleware)
 * 5️⃣ Cần time-travel debugging
 * 6️⃣ Đã có sẵn Redux trong project (legacy code)
 * 
 * VD:
 * - E-commerce platform (cart, products, orders, users...)
 * - Trading platform (real-time data, complex state)
 * - CRM system (customers, deals, tasks...)
 * - Admin dashboard (users, analytics, settings...)
 */

// Example: Trading Platform với Redux
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

// Async action: Fetch real-time price
export const fetchPrice = createAsyncThunk(
  'trading/fetchPrice',
  async (symbol: string) => {
    const response = await fetch(`/api/price/${symbol}`);
    return response.json();
  }
);

const tradingSlice = createSlice({
  name: 'trading',
  initialState: {
    prices: {},
    orders: [],
    positions: [],
    loading: false,
  },
  reducers: {
    placeOrder: (state, action) => {
      state.orders.push(action.payload);
    },
    closePosition: (state, action) => {
      state.positions = state.positions.filter(p => p.id !== action.payload);
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchPrice.pending, (state) => {
        state.loading = true;
      })
      .addCase(fetchPrice.fulfilled, (state, action) => {
        state.prices[action.meta.arg] = action.payload;
        state.loading = false;
      });
  },
});
```

---

### **🎯 PHẦN 6: MIGRATION GUIDE (Hướng Dẫn Chuyển Đổi)**

```typescript
/**
 * 🔄 MIGRATION: Context API → Zustand
 */

// BEFORE: Context API
const UserContext = createContext(null);

const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  
  const login = (userData) => setUser(userData);
  const logout = () => setUser(null);

  return (
    <UserContext.Provider value={{ user, login, logout }}>
      {children}
    </UserContext.Provider>
  );
};

// Usage
const Profile = () => {
  const { user } = useContext(UserContext);
  return <div>{user?.name}</div>;
};

// AFTER: Zustand
import create from 'zustand';

const useUserStore = create((set) => ({
  user: null,
  login: (userData) => set({ user: userData }),
  logout: () => set({ user: null }),
}));

// Usage (KHÔNG CẦN Provider!)
const Profile = () => {
  const user = useUserStore((state) => state.user);
  return <div>{user?.name}</div>;
};

/**
 * ✅ BENEFITS:
 * - Bỏ Provider → code sạch hơn
 * - Performance tốt hơn
 * - Dễ test hơn (không cần wrap trong Provider)
 */

/**
 * 🔄 MIGRATION: Zustand → Redux
 */

// BEFORE: Zustand
const useUserStore = create((set) => ({
  user: null,
  loading: false,
  error: null,
  
  login: async (credentials) => {
    set({ loading: true });
    try {
      const user = await api.login(credentials);
      set({ user, loading: false });
    } catch (error) {
      set({ error: error.message, loading: false });
    }
  },
}));

// AFTER: Redux (RTK)
const userSlice = createSlice({
  name: 'user',
  initialState: { user: null, loading: false, error: null },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(loginAsync.pending, (state) => {
        state.loading = true;
      })
      .addCase(loginAsync.fulfilled, (state, action) => {
        state.user = action.payload;
        state.loading = false;
      })
      .addCase(loginAsync.rejected, (state, action) => {
        state.error = action.payload;
        state.loading = false;
      });
  },
});

export const loginAsync = createAsyncThunk(
  'user/login',
  async (credentials) => {
    return await api.login(credentials);
  }
);

/**
 * ✅ BENEFITS:
 * - Structure rõ ràng hơn (Actions, Reducers tách riêng)
 * - DevTools mạnh hơn
 * - Middleware ecosystem lớn hơn
 * - Dễ maintain trong team lớn
 */

---

### **📊 PHẦN 7: REAL-WORLD EXAMPLES (Ví Dụ Thực Tế)**

```typescript
/**
 * 🏢 SCENARIO 1: E-COMMERCE APP
 * 
 * State cần quản lý:
 * - User (auth, profile)
 * - Cart (items, total)
 * - Products (list, filters)
 * - Orders (history, status)
 * - UI (modal, notifications)
 * 
 * 🎯 RECOMMEND: ZUSTAND
 * 
 * WHY?
 * - App vừa phải (không quá phức tạp)
 * - Cần performance tốt (cart update nhiều)
 * - Code đơn giản, dễ maintain
 * - DevTools để debug cart issues
 */

// Store structure với Zustand
import create from 'zustand';
import { persist, devtools } from 'zustand/middleware';

// 1. User Store
export const useUserStore = create(
  persist(
    (set) => ({
      user: null,
      login: (user) => set({ user }),
      logout: () => set({ user: null }),
    }),
    { name: 'user-storage' }
  )
);

// 2. Cart Store
export const useCartStore = create(
  devtools((set, get) => ({
    items: [],
    
    addItem: (product) => set((state) => ({
      items: [...state.items, { ...product, quantity: 1 }]
    })),
    
    removeItem: (id) => set((state) => ({
      items: state.items.filter(item => item.id !== id)
    })),
    
    updateQuantity: (id, quantity) => set((state) => ({
      items: state.items.map(item =>
        item.id === id ? { ...item, quantity } : item
      )
    })),
    
    clearCart: () => set({ items: [] }),
    
    get total() {
      return get().items.reduce((sum, item) => 
        sum + item.price * item.quantity, 0
      );
    },
  }))
);

// 3. UI Store (modal, notifications)
export const useUIStore = create((set) => ({
  modal: null,
  notifications: [],
  
  openModal: (modalType) => set({ modal: modalType }),
  closeModal: () => set({ modal: null }),
  
  addNotification: (message) => set((state) => ({
    notifications: [...state.notifications, { id: Date.now(), message }]
  })),
  
  removeNotification: (id) => set((state) => ({
    notifications: state.notifications.filter(n => n.id !== id)
  })),
}));

/**
 * 🏢 SCENARIO 2: TRADING PLATFORM
 * 
 * State cần quản lý:
 * - User (auth, account balance)
 * - Market Data (real-time prices, charts)
 * - Orders (pending, filled, cancelled)
 * - Positions (open, closed, P&L)
 * - Watchlist (favorite symbols)
 * - Notifications (trade alerts, margin calls)
 * 
 * 🎯 RECOMMEND: REDUX (RTK)
 * 
 * WHY?
 * - App CỰC PHỨC TẠP (nhiều state phụ thuộc nhau)
 * - Real-time data (cần middleware như Redux Saga)
 * - Team lớn (10+ developers)
 * - Cần DevTools mạnh để debug trades
 * - Cần time-travel để reproduce bugs
 */

// Store structure với Redux
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './slices/userSlice';
import marketReducer from './slices/marketSlice';
import ordersReducer from './slices/ordersSlice';
import positionsReducer from './slices/positionsSlice';

export const store = configureStore({
  reducer: {
    user: userReducer,
    market: marketReducer,
    orders: ordersReducer,
    positions: positionsReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(
      // Custom middleware: WebSocket cho real-time data
      websocketMiddleware,
      // Logger middleware
      loggerMiddleware
    ),
});

/**
 * 🏢 SCENARIO 3: BLOG/PORTFOLIO WEBSITE
 * 
 * State cần quản lý:
 * - Theme (dark/light)
 * - Language (en/vi)
 * 
 * 🎯 RECOMMEND: CONTEXT API
 * 
 * WHY?
 * - App ĐƠN GIẢN (chỉ 2-3 states)
 * - State ÍT THAY ĐỔI (theme, language)
 * - Không cần DevTools
 * - Không muốn cài thêm library
 */

// Theme Context
const ThemeContext = createContext({ theme: 'light', toggleTheme: () => {} });

export const ThemeProvider = ({ children }) => {
  const [theme, setTheme] = useState('light');
  
  const toggleTheme = () => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  };

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};
```

---

**💡 KEY TAKEAWAYS (Điểm Chính Cần Nhớ)**

```typescript
/**
 * ✅ CONTEXT API:
 * - Built-in React, 0 KB
 * - Đơn giản, dễ học
 * - Performance KÉMFORM state ít thay đổi
 * - Dùng cho: Theme, Language, Auth status
 * 
 * ✅ ZUSTAND:
 * - 1.2 KB, simple API
 * - Performance XUẤT SẮC (auto-optimization)
 * - Không cần Provider
 * - Dùng cho: Cart, User profile, Notifications, Form state
 * - RECOMMEND cho MOST APPS!
 * 
 * ✅ REDUX (RTK):
 * - 12 KB, nhiều boilerplate
 * - Performance tốt, DevTools mạnh
 * - Ecosystem lớn, middleware nhiều
 * - Dùng cho: E-commerce, Trading, CRM, Admin dashboard
 * - RECOMMEND cho LARGE/ENTERPRISE APPS
 * 
 * 🎯 DECISION TREE:
 * 
 * App nhỏ, state ít thay đổi (theme, language)
 *   → Context API
 * 
 * App vừa/lớn, cần performance, code đơn giản
 *   → Zustand (✅ RECOMMEND!)
 * 
 * App cực lớn, team lớn, cần structure rõ ràng
 *   → Redux (RTK)
 */
```

