# 🔐 Tóm Tắt Keycloak - Hướng Dẫn Toàn Diện

## 📚 Mục Lục
1. [Keycloak là gì?](#keycloak-là-gì)
2. [Ưu & Nhược điểm](#ưu--nhược-điểm)
3. [Các khái niệm cơ bản](#các-khái-niệm-cơ-bản)
4. [Loại Client: PUBLIC vs CONFIDENTIAL](#loại-client-public-vs-confidential)
5. [Vấn đề 401 Unauthorized](#vấn-đề-401-unauthorized)
6. [Token Management](#token-management)
7. [Role-Based Access Control (RBAC)](#role-based-access-control-rbac)
8. [Authorization Services](#authorization-services)
9. [Cách Fix Triệt Để](#cách-fix-triệt-để)
10. [Quick Start](#quick-start)

---

## 🎯 Keycloak là gì?

**Keycloak** là một **Open Source Identity and Access Management (IAM)** solution:

- ✅ **Centralized Authentication**: Quản lý user tập trung
- ✅ **Single Sign-On (SSO)**: Đăng nhập một lần, dùng nhiều app
- ✅ **Social Login**: Google, Facebook, GitHub, etc.
- ✅ **LDAP/Active Directory**: Tích hợp với enterprise systems
- ✅ **Multi-Factor Authentication (MFA)**: Bảo mật 2 lớp
- ✅ **Standard Protocols**: OAuth 2.0, OpenID Connect, SAML 2.0

### **Cách hoạt động:**
```
User → Login → Keycloak → Verify → Generate Tokens → App uses tokens
```

---

## ⚖️ Ưu & Nhược điểm

### **✅ Ưu điểm:**
- 🆓 **Free & Open Source**
- 🔒 **Bảo mật cao** (Industry standards)
- 🌐 **Multi-platform**: Web, Mobile, Desktop
- 🔌 **Dễ tích hợp** (React, Angular, Vue, Node.js, Spring Boot)
- 📱 **Social Login** built-in
- 🎭 **Fine-grained Authorization** (Roles, Permissions, Policies)
- 📊 **Admin Console** trực quan
- 🔄 **Token Refresh** tự động
- 🌍 **Multi-tenancy** (Realms)

### **❌ Nhược điểm:**
- 📚 **Learning curve** cao (nhiều concepts phức tạp)
- 🐘 **Heavy** (yêu cầu Java, database)
- 🔧 **Setup phức tạp** cho production
- 📖 **Documentation** đôi khi khó hiểu
- ⚠️ **Breaking changes** giữa các versions

---

## 🧩 Các Khái Niệm Cơ Bản

### **1. Realm**
- **Namespace** để tách biệt users, clients, roles
- Mỗi realm có config riêng
- Ví dụ: `trading-realm`, `production-realm`

### **2. Client**
- **Application** sử dụng Keycloak để authenticate
- Có 2 loại: **PUBLIC** và **CONFIDENTIAL**
- Ví dụ: `trading-app`

### **3. User**
- **Người dùng** có thể login
- Có username, password, email, attributes
- Ví dụ: `cs-user`, `admin-user`

### **4. Role**
- **Vai trò** của user (CS, MO, BO, GD)
- **Realm Roles**: Áp dụng cho toàn realm
- **Client Roles**: Áp dụng cho specific client
- Ví dụ: `cs`, `admin`, `trader`

### **5. Group**
- **Nhóm users** (có thể assign roles cho group)
- Ví dụ: `customer-service`, `management`

### **6. Token**
- **Access Token**: Dùng để access APIs (thường 5-15 phút)
- **Refresh Token**: Dùng để renew access token (thường 30 phút - 8 giờ)
- **ID Token**: Chứa thông tin user (OpenID Connect)

### **7. PKCE (Proof Key for Code Exchange)**
- **Bảo mật** cho Public Clients
- Ngăn chặn **Authorization Code Interception**
- Flow: `code_challenge` → `code_verifier`

---

## 🔑 Loại Client: PUBLIC vs CONFIDENTIAL

### **📊 So Sánh:**

| Tiêu chí | PUBLIC Client | CONFIDENTIAL Client |
|----------|--------------|---------------------|
| **Client Secret** | ❌ Không cần | ✅ Cần (hoặc dùng PKCE) |
| **PKCE** | ✅ Required | ✅ Optional (recommended) |
| **Use Case** | SPAs, Mobile Apps | Backend APIs, Services |
| **Roles** | ✅ Có | ✅ Có |
| **Authorization Services** | ❌ KHÔNG | ✅ Có |
| **Resources** | ❌ KHÔNG | ✅ Có |
| **Policies** | ❌ KHÔNG | ✅ Có |
| **Permissions** | ❌ KHÔNG | ✅ Có |
| **Service Accounts** | ❌ KHÔNG | ✅ Có |
| **Bảo mật** | PKCE | Client Secret + PKCE |

### **🎯 Khi Nào Dùng PUBLIC Client:**
- ✅ Frontend app đơn giản (React, Vue, Angular)
- ✅ Chỉ cần **ROLES** cho access control
- ✅ Không cần fine-grained permissions
- ✅ Không cần service accounts

### **🎯 Khi Nào Dùng CONFIDENTIAL Client:**
- ✅ Backend services, APIs
- ✅ Cần **Authorization Services** (Resources, Policies, Permissions)
- ✅ Cần **Service Accounts**
- ✅ Cần fine-grained authorization

---

## ⚠️ Vấn Đề 401 Unauthorized

### **Nguyên Nhân Chính:**

#### **1. Client Type Mismatch:**
```
Client = CONFIDENTIAL + Frontend không gửi client_secret
→ 401 Unauthorized
```

**Giải pháp:**
- **Option A**: Đổi về PUBLIC client (nếu không cần Authorization Services)
- **Option B**: Giữ CONFIDENTIAL và config frontend để dùng client secret

#### **2. Authorization Code Flow Error:**
```
Frontend gửi code nhưng không gửi code_verifier (PKCE)
→ invalid_client_credentials
```

**Giải pháp:**
- Enable PKCE trong frontend: `pkceMethod: 'S256'`

#### **3. Redirect URI Mismatch:**
```
Frontend redirect về http://localhost:9060
Keycloak chỉ allow http://localhost:3000
→ invalid_redirect_uri
```

**Giải pháp:**
- Add đúng redirect URIs trong client config:
  ```
  http://localhost:9060/*
  http://localhost:3000/*
  ```

#### **4. CORS Issues:**
```
Frontend gọi Keycloak từ domain khác
→ CORS blocked
```

**Giải pháp:**
- Add Web Origins:
  ```
  http://localhost:9060
  http://localhost:3000
  +  (allow all origins - chỉ dùng dev)
  ```

---

## ⏰ Token Management

### **Token Lifecycle:**

```
1. Login → Access Token (5 min) + Refresh Token (30 min)
2. After 5 min → Access Token expired
3. Auto refresh → New Access Token (5 min)
4. After 30 min → Refresh Token expired
5. Force re-login
```

### **Token Settings trong Keycloak:**

| Setting | Mô Tả | Default | Recommended |
|---------|-------|---------|-------------|
| **Access Token Lifespan** | Thời gian access token còn hiệu lực | 5 min | 5-15 min |
| **SSO Session Idle** | Thời gian idle trước khi logout | 30 min | 30 min - 1 giờ |
| **SSO Session Max** | Thời gian tối đa của session | 10 giờ | 8-12 giờ |
| **Client Session Idle** | Thời gian idle cho client | 30 min | 30 min |
| **Offline Session Idle** | Thời gian idle cho offline session | 30 ngày | 7-30 ngày |

### **Config trong Code:**

```typescript
// keycloak.service.ts
const initOptions: KeycloakInitOptions = {
  onLoad: 'check-sso',
  checkLoginIframe: false,
  pkceMethod: 'S256',  // ✅ PKCE for security
  enableLogging: true
};

// Auto token refresh
keycloak.onTokenExpired = () => {
  keycloak.updateToken(30)
    .then(refreshed => {
      if (refreshed) {
        console.log('✅ Token refreshed');
      }
    })
    .catch(() => {
      console.log('❌ Token refresh failed → logout');
      keycloak.logout();
    });
};
```

---

## 🎭 Role-Based Access Control (RBAC)

### **Concept:**
- Assign **ROLES** cho users
- Check roles trong frontend để show/hide UI
- Check roles trong backend để allow/deny API calls

### **Ví Dụ: Trading App:**

```typescript
// Roles
const roles = {
  CS: 'cs',           // Customer Service
  MO: 'mo',           // Market Operations
  BO: 'bo',           // Back Office
  GD: 'gd',           // General Director
  ADMIN: 'admin',
  USER: 'user'
};

// Test users
const testUsers = [
  { username: 'cs-user', password: 'cs123', roles: ['cs', 'user'] },
  { username: 'mo-user', password: 'mo123', roles: ['mo', 'user'] },
  { username: 'bo-user', password: 'bo123', roles: ['bo', 'user'] },
  { username: 'gd-user', password: 'gd123', roles: ['gd', 'admin', 'user'] }
];
```

### **Sử Dụng trong Code:**

```typescript
// Zustand store
import { useHasRole } from './keycloakAuth.store';

// Component
const MyComponent = () => {
  const isCS = useHasRole('cs');
  const isAdmin = useHasRole('admin');

  return (
    <>
      {isCS && <CustomerServicePanel />}
      {isAdmin && <AdminPanel />}
    </>
  );
};
```

---

## 🔐 Authorization Services

### **⚠️ CHỈ Hoạt Động với CONFIDENTIAL Client!**

### **Components:**

#### **1. Resources:**
- Đại diện cho **protected assets** (APIs, pages, features)
- Ví dụ:
  ```json
  {
    "name": "Customer API",
    "type": "urn:trading-app:resources:customer-api",
    "uris": ["/api/customer/*"],
    "scopes": ["view", "edit"]
  }
  ```

#### **2. Scopes:**
- **Actions** có thể thực hiện trên resource
- Ví dụ: `view`, `edit`, `delete`, `manage`

#### **3. Policies:**
- **Rules** để grant access
- **Role-Based Policy**: Grant nếu user có role
  ```json
  {
    "name": "CS Role Policy",
    "type": "role",
    "roles": ["cs"]
  }
  ```

#### **4. Permissions:**
- **Combine** Resources + Scopes + Policies
- Ví dụ:
  ```json
  {
    "name": "Customer View Permission",
    "resource": "Customer API",
    "scopes": ["view"],
    "policies": ["CS Role Policy"]
  }
  ```

### **Setup Flow:**

```
1. Create Resources (Customer API, Trading API, etc.)
2. Create Policies (CS Role Policy, MO Role Policy, etc.)
3. Create Permissions (Customer View Permission, etc.)
4. Test in app
```

### **Check Permissions trong Code:**

```typescript
import { useHasPermission } from './keycloakAuth.store';

const MyComponent = () => {
  const canViewCustomer = useHasPermission('Customer API', 'view');

  return (
    <>
      {canViewCustomer && <CustomerList />}
    </>
  );
};
```

---

## 🔧 Cách Fix Triệt Để

### **Script 1: Fix về PUBLIC Client (Simple)**

```bash
./apps/trading-frontend/src/app/keycloack/fix-to-public-simple.sh
```

**Kết quả:**
- ✅ Client Type: PUBLIC
- ✅ PKCE: ENABLED
- ❌ Authorization Services: DISABLED

**Khi nào dùng:**
- Chỉ cần ROLES
- Không cần fine-grained permissions

---

### **Script 2: Setup CONFIDENTIAL Client (Advanced)**

```bash
./apps/trading-frontend/src/app/keycloack/setup-confidential-client-with-auth.sh
```

**Kết quả:**
- ✅ Client Type: CONFIDENTIAL
- ✅ Client Secret: Auto-generated
- ✅ Authorization Services: ENABLED
- ✅ Service Accounts: ENABLED

**Khi nào dùng:**
- Cần Authorization Services
- Cần Resources, Policies, Permissions

---

### **Script 3: Create Permissions**

```bash
./apps/trading-frontend/src/app/keycloack/create-permissions.sh
```

**Tạo:**
- ✅ Resources (Customer API, Trading API, Finance API, Admin API)
- ✅ Policies (CS Role Policy, MO Role Policy, BO Role Policy, GD Role Policy)
- ✅ Permissions (View, Edit, Execute, Process, Manage)

---

## 🚀 Quick Start

### **1. Start Keycloak:**

```bash
cd trading-workspace
docker-compose -f docker-compose.keycloak.yml up -d
```

**Kiểm tra:**
- Keycloak: http://localhost:8080
- Admin: `admin/admin123`

---

### **2. Setup Client (Choose ONE):**

#### **Option A: PUBLIC Client (Simple)**
```bash
./apps/trading-frontend/src/app/keycloack/fix-to-public-simple.sh
```

#### **Option B: CONFIDENTIAL Client (Advanced)**
```bash
./apps/trading-frontend/src/app/keycloack/setup-confidential-client-with-auth.sh
# Tạo permissions
./apps/trading-frontend/src/app/keycloack/create-permissions.sh
```

---

### **3. Start Frontend:**

```bash
npm run trading-frontend:serve
```

**Open:** http://localhost:9060

---

### **4. Test Login:**

**Test Users:**
- `cs-user/cs123` → Customer Service role
- `mo-user/mo123` → Market Operations role
- `bo-user/bo123` → Back Office role
- `gd-user/gd123` → General Director role

---

### **5. Test Features:**

**Tabs:**
- **Overview**: Xem user info, roles
- **Token**: Xem token details, test expiration
- **API Demo**: Test protected API calls
- **Profile**: Xem & update user profile
- **🎭 Role Demo**: Test role-based UI (AVAILABLE for PUBLIC)

**Permission Tabs** (CHỈ với CONFIDENTIAL client):
- **🔐 Permissions Demo**: Test permissions
- **⚙️ Role Management**: Quản lý roles
- **🔧 Permissions Management**: Quản lý permissions
- **🎭 Permission UI**: UI based on permissions
- **🔍 Permission Logger**: Log permissions to console

---

## 📝 Tóm Tắt Cuối

### **Current Setup:**
✅ **Client Type**: PUBLIC
✅ **PKCE**: ENABLED
✅ **Roles**: cs, mo, bo, gd, admin, user
✅ **Test Users**: cs-user, mo-user, bo-user, gd-user
❌ **Authorization Services**: DISABLED (not supported for PUBLIC)

### **Nếu Cần Authorization Services:**
1. Run: `./apps/trading-frontend/src/app/keycloack/setup-confidential-client-with-auth.sh`
2. Update frontend để dùng client secret (nếu cần)
3. Run: `./apps/trading-frontend/src/app/keycloack/create-permissions.sh`
4. Restart frontend

### **Common Commands:**

```bash
# Check Keycloak status
docker ps | grep keycloak

# Check Keycloak logs
docker logs keycloak-server --tail 50

# Restart Keycloak
docker restart keycloak-server

# Fix client to PUBLIC
./apps/trading-frontend/src/app/keycloack/fix-to-public-simple.sh

# Setup CONFIDENTIAL with Authorization
./apps/trading-frontend/src/app/keycloack/setup-confidential-client-with-auth.sh

# Create permissions
./apps/trading-frontend/src/app/keycloack/create-permissions.sh

# Start frontend
npm run trading-frontend:serve
```

---

## 🎓 Key Takeaways

1. **PUBLIC Client**: Simple, chỉ dùng Roles, không cần client secret
2. **CONFIDENTIAL Client**: Advanced, dùng Authorization Services, cần client secret
3. **PKCE**: Bảo mật cho PUBLIC clients
4. **Roles**: Coarse-grained access control
5. **Permissions**: Fine-grained access control (chỉ CONFIDENTIAL)
6. **Token Management**: Auto-refresh, expiration handling
7. **401 Unauthorized**: Thường do client type mismatch
8. **Scripts**: Dùng scripts để fix nhanh và tránh lỗi manual config

---

**🎉 Chúc bạn thành công với Keycloak!**

