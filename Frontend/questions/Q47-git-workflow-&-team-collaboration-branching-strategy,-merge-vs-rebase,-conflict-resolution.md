# 🌿 Q47: Git Workflow & Team Collaboration - Branching Strategy, Merge vs Rebase, Conflict Resolution


**⚡ Quick Summary:**
> Git workflow tốt = ít conflict + dễ review + dễ rollback. Git Flow phù hợp dự án lớn, GitHub Flow phù hợp CI/CD. Rebase tạo history sạch, Merge giữ nguyên context. Feature flags giúp deploy code chưa hoàn thiện mà không ảnh hưởng production.

**💡 Ghi Nhớ:**
- 🌳 **Git Flow**: main + develop + feature/* + release/* + hotfix/* (dự án lớn, release theo version)
- 🚀 **GitHub Flow**: main + feature/* (CI/CD, deploy liên tục)
- ⚔️ **Merge vs Rebase**: Merge = giữ nguyên history, Rebase = history sạch nhưng mất context
- 🚩 **Feature Flags**: Deploy code mới nhưng tắt feature, bật dần theo phần trăm user

---

### **1. Branching Models - Các Mô Hình Phân Nhánh**

#### **1.1. Git Flow - Mô hình phổ biến cho dự án lớn**

```
📊 Structure Git Flow:

main (production)          ───●───────●───────●─────── (v1.0, v2.0, v3.0)
                              ╱         ╲       
develop (staging)      ──────●───●───●───●───●──────── (code mới nhất)
                            ╱     ╲   ╱
feature/login      ────────●───●───●                    (tính năng mới)
feature/payment    ──────────●───●───●                  (tính năng khác)
                                    ╲
release/v2.0       ───────────────────●───●──          (chuẩn bị release)
                                            ╲
hotfix/bug-123     ─────────────────────────●──●─────  (fix lỗi khẩn cấp)
```

**Chi tiết các nhánh:**

```bash
# 1. main (hoặc master) - Production branch
# - Chỉ chứa code ổn định, đã test kỹ
# - Mỗi commit là một version release (v1.0, v1.1, v2.0...)
# - KHÔNG bao giờ commit trực tiếp vào main!

# 2. develop - Integration branch (nhánh phát triển chính)
# - Chứa code mới nhất đã merge từ các feature branches
# - Là base branch để tạo feature mới
# - Code ở đây đã qua code review nhưng chưa release

# 3. feature/* - Feature branches
# - Mỗi tính năng mới = 1 feature branch
# - Tên: feature/ten-tinh-nang (vd: feature/login, feature/payment)
git checkout develop
git checkout -b feature/user-authentication

# Làm việc trên feature branch...
git add .
git commit -m "feat: implement JWT authentication"

# Merge vào develop khi xong
git checkout develop
git pull origin develop  # Lấy code mới nhất
git merge feature/user-authentication
git push origin develop

# Xóa feature branch sau khi merge
git branch -d feature/user-authentication


# 4. release/* - Release branches
# - Chuẩn bị release version mới
# - Fix bugs nhỏ, update version, documentation
git checkout develop
git checkout -b release/v2.0.0

# Fix bugs, update CHANGELOG, version...
git commit -m "chore: bump version to 2.0.0"

# Merge vào CẢHAI main VÀ develop
git checkout main
git merge release/v2.0.0
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin main --tags

git checkout develop
git merge release/v2.0.0
git push origin develop

git branch -d release/v2.0.0


# 5. hotfix/* - Hotfix branches
# - Fix lỗi KHẨN CẤP trên production
# - Branch từ main (không phải develop!)
git checkout main
git checkout -b hotfix/critical-security-bug

# Fix bug...
git commit -m "fix: patch security vulnerability CVE-2024-1234"

# Merge vào CẢHAI main VÀ develop
git checkout main
git merge hotfix/critical-security-bug
git tag -a v2.0.1 -m "Hotfix: security patch"
git push origin main --tags

git checkout develop
git merge hotfix/critical-security-bug
git push origin develop

git branch -d hotfix/critical-security-bug
```

**Ưu điểm Git Flow:**
- ✅ Rõ ràng, dễ quản lý với dự án lớn (nhiều developers, nhiều versions)
- ✅ Tách biệt development và production rõ ràng
- ✅ Hỗ trợ multiple versions đồng thời (v1.x và v2.x)

**Nhược điểm:**
- ❌ Phức tạp, nhiều nhánh
- ❌ Không phù hợp CI/CD (continuous deployment)
- ❌ Merge conflicts nhiều hơn

---

#### **1.2. GitHub Flow - Đơn giản hơn, phù hợp CI/CD**

```
📊 Structure GitHub Flow:

main (production)   ──●───●───────●───●───────●──────
                      │   │       │   │       │
                      │   │       │   │       └─ feature/payment merged
                      │   │       │   └─ feature/dashboard merged  
                      │   │       └─ hotfix/bug-fix merged
                      │   └─ feature/login merged
                      │
feature/login      ───●───●───●
feature/dashboard  ─────────●───●───●
hotfix/bug-fix     ───────────────●──●
feature/payment    ─────────────────────●───●───●
```

**Workflow đơn giản:**

```bash
# 1. Chỉ có 1 nhánh main (production-ready)

# 2. Tạo feature branch từ main
git checkout main
git pull origin main
git checkout -b feature/new-feature

# 3. Commit và push thường xuyên
git add .
git commit -m "feat: add feature X"
git push origin feature/new-feature

# 4. Tạo Pull Request (PR) trên GitHub
# - Code review
# - CI/CD chạy tests tự động
# - Deploy lên staging environment để test

# 5. Merge vào main SAU KHI:
# - ✅ Code review approved
# - ✅ CI/CD tests passed
# - ✅ Staging test OK
git checkout main
git pull origin main
git merge feature/new-feature
git push origin main

# 6. Auto-deploy lên production (CI/CD pipeline)

# 7. Xóa feature branch
git branch -d feature/new-feature
git push origin --delete feature/new-feature
```

**Ưu điểm GitHub Flow:**
- ✅ Đơn giản, dễ hiểu
- ✅ Phù hợp CI/CD, deploy liên tục
- ✅ Ít conflict hơn (merge thường xuyên)

**Nhược điểm:**
- ❌ Không phù hợp với release theo version cố định
- ❌ Khó quản lý nhiều versions đồng thời

---

#### **1.3. Trunk-Based Development - Extreme simplicity**

```bash
# Tất cả developers commit trực tiếp vào main (hoặc trunk)
# Dùng feature flags để tắt/bật features chưa hoàn thiện

git checkout main
git pull origin main

# Làm việc trực tiếp trên main (hoặc short-lived branch < 1 ngày)
# Code mới được bảo vệ bằng feature flags

# Code với feature flag
if (featureFlags.isEnabled('new-payment')) {
  // Code mới (chưa hoàn thiện)
  renderNewPayment();
} else {
  // Code cũ (đang chạy)
  renderOldPayment();
}

git add .
git commit -m "feat: add new payment (behind feature flag)"
git push origin main  # Deploy lên production ngay!

# Feature flag tắt → user không thấy code mới
# Bật dần theo % user: 10% → 50% → 100%
```

**Ưu điểm:**
- ✅ Cực kỳ đơn giản
- ✅ Integration liên tục, ít conflict
- ✅ Deploy nhanh

**Nhược điểm:**
- ❌ Cần CI/CD mạnh (tests tự động kỹ)
- ❌ Cần feature flag infrastructure
- ❌ Rủi ro cao nếu tests không đủ tốt

---

### **2. Merge vs Rebase - Sự Khác Biệt Quan Trọng**

#### **2.1. Git Merge - Giữ nguyên lịch sử**

```bash
# Tình huống: feature branch đã có 3 commits
# main branch có 2 commits mới (từ developer khác)

main:     A ─── B ─── C ─── D ─── E
                        ╲
feature:                 F ─── G ─── H

# Merge feature vào main
git checkout main
git merge feature/login

# Kết quả: Tạo MERGE COMMIT (M)
main:     A ─── B ─── C ─── D ─── E ─── M
                        ╲               ╱
feature:                 F ─── G ─── H
```

**Đặc điểm Merge:**
```bash
# Ưu điểm:
# ✅ Giữ nguyên lịch sử (biết branch từ đâu, merge khi nào)
# ✅ An toàn (không thay đổi commits cũ)
# ✅ Phù hợp public branches (main, develop)

# Nhược điểm:
# ❌ History nhiều merge commits, phức tạp
# ❌ Khó theo dõi khi nhiều branches merge
# ❌ Git log rối (có nhiều nhánh)

# Khi nào dùng Merge?
# - Merge feature vào main/develop (public branches)
# - Muốn giữ context: ai làm gì, khi nào
# - Team lớn, cần trace history đầy đủ
```

---

#### **2.2. Git Rebase - Tạo lịch sử tuyến tính**

```bash
# Tình huống giống trên
main:     A ─── B ─── C ─── D ─── E
                        ╲
feature:                 F ─── G ─── H

# Rebase feature lên main
git checkout feature/login
git rebase main

# Kết quả: "Di chuyển" F, G, H lên SAU E
main:     A ─── B ─── C ─── D ─── E
                                    ╲
feature:                             F' ─── G' ─── H'
#                                    ^^^Commits mới (hash khác!)
```

**Đặc điểm Rebase:**
```bash
# Ưu điểm:
# ✅ Lịch sử sạch, tuyến tính (linear history)
# ✅ Dễ đọc git log (không có merge commits)
# ✅ Dễ cherry-pick, revert

# Nhược điểm:
# ❌ Mất context (không biết branch từ đâu)
# ❌ THAY ĐỔI COMMIT HASH → Nguy hiểm với public branches!
# ❌ Conflict khó resolve hơn (có thể conflict nhiều lần)

# Khi nào dùng Rebase?
# - Rebase local branch (chưa push)
# - Rebase feature branch lên main trước khi tạo PR
# - Muốn history sạch đẹp
# - Team nhỏ, quen với rebase

# ⚠️ GOLDEN RULE OF REBASE:
# "NEVER rebase public branches (main, develop)!"
# Vì sẽ làm conflict với code của người khác!
```

---

#### **2.3. So sánh Merge vs Rebase**

| Feature | Merge | Rebase |
|---------|-------|--------|
| **History** | Giữ nguyên, có merge commits | Tuyến tính, sạch đẹp |
| **Commit hash** | Không đổi | ĐỔI (commits mới) |
| **Context** | ✅ Giữ nguyên (biết branch từ đâu) | ❌ Mất (không biết branch point) |
| **Conflicts** | Resolve 1 lần | Có thể resolve nhiều lần |
| **Safety** | ✅ An toàn (không thay đổi history) | ⚠️ Nguy hiểm nếu rebase public branch |
| **Use case** | Public branches (main, develop) | Local/feature branches |
| **Git log** | Phức tạp (nhiều nhánh) | Đơn giản (tuyến tính) |

---

#### **2.4. Interactive Rebase - Chỉnh sửa commits**

```bash
# Squash nhiều commits thành 1 commit
git rebase -i HEAD~3  # Chỉnh sửa 3 commits gần nhất

# Editor hiện ra:
# pick f7f3f6d feat: add login form
# pick 310154e fix: typo in login
# pick a5f4a0d fix: add validation

# Thay đổi thành:
# pick f7f3f6d feat: add login form
# squash 310154e fix: typo in login
# squash a5f4a0d fix: add validation

# Kết quả: 3 commits → 1 commit sạch đẹp
# feat: add login form (với tất cả changes)

# Use cases:
# - Squash "WIP commits" trước khi tạo PR
# - Chỉnh sửa commit messages
# - Reorder commits
# - Drop commits không cần thiết
```

---

### **3. Feature Flags - Deploy Code Chưa Hoàn Thiện**

#### **3.1. Feature Flags là gì?**

```typescript
// ❌ Cách cũ: Phải chờ feature hoàn thiện mới merge vào main
// → Feature branch sống lâu → Nhiều conflicts!

// ✅ Cách mới: Merge code vào main NGAY, nhưng "tắt" feature
// → Feature branch ngắn → Ít conflicts!

// Feature Flag implementation
interface FeatureFlags {
  newPaymentUI: boolean;      // Feature mới
  darkMode: boolean;           // Theme tối
  experimentalChart: boolean;  // Chart mới (đang test)
}

// Quản lý flags từ server (có thể bật/tắt realtime)
const flags: FeatureFlags = await fetch('/api/feature-flags').then(r => r.json());

// Dùng trong code
function renderPayment() {
  if (flags.newPaymentUI) {
    // Code MỚI (chưa hoàn thiện, nhưng đã merge vào main)
    return <NewPaymentUI />;
  } else {
    // Code CŨ (đang chạy production)
    return <OldPaymentUI />;
  }
}

// Lợi ích:
// 1. Deploy code mới NGAY (không chờ hoàn thiện)
// 2. Bật feature cho 10% users → test → nếu OK → 100%
// 3. Nếu có bug → tắt feature NGAY (không cần rollback code)
// 4. A/B testing: 50% user thấy UI cũ, 50% thấy UI mới
```

#### **3.2. Gradual Rollout - Bật dần theo phần trăm**

```typescript
// Backend API quản lý feature flags
interface FeatureFlagConfig {
  name: string;
  enabled: boolean;
  rolloutPercentage: number; // 0-100
  targetUsers?: string[];    // Bật cho user cụ thể
}

const featureConfig: FeatureFlagConfig = {
  name: 'newPaymentUI',
  enabled: true,
  rolloutPercentage: 10,  // Chỉ 10% users thấy feature mới
  targetUsers: ['admin@company.com', 'beta-tester@company.com']
};

// Frontend check
function isFeatureEnabled(userId: string, featureName: string): boolean {
  const config = getFeatureConfig(featureName);
  
  // Luôn bật cho target users
  if (config.targetUsers?.includes(userId)) {
    return true;
  }
  
  // Bật theo % (consistent hashing để user luôn thấy cùng UI)
  const hash = hashUserId(userId);
  return hash % 100 < config.rolloutPercentage;
}

// Rollout process:
// Day 1: 10% users  → Monitor metrics (errors, performance)
// Day 2: 25% users  → So sánh conversion rate
// Day 3: 50% users  → Gather feedback
// Day 4: 100% users → Full rollout!
// Nếu có vấn đề → rollback về 0% NGAY!
```

#### **3.3. Feature Flag Tools**

```typescript
// 1. LaunchDarkly (commercial, mạnh nhất)
import LaunchDarkly from 'launchdarkly-node-server-sdk';

const client = LaunchDarkly.init('sdk-key');
const showNewUI = await client.variation('new-payment-ui', user, false);

// 2. Unleash (open-source)
import { initialize } from 'unleash-client';

const unleash = initialize({
  url: 'https://unleash.yourcompany.com/api/',
  appName: 'my-app',
});

if (unleash.isEnabled('new-payment-ui')) {
  // Show new UI
}

// 3. Simple custom solution
const FLAGS = {
  newPaymentUI: process.env.FEATURE_NEW_PAYMENT === 'true',
  darkMode: process.env.FEATURE_DARK_MODE === 'true',
};

// Hoặc fetch từ database/config service
```

---

### **4. Tránh Conflicts Khi Làm Việc Team**

#### **4.1. Các Tình Huống Conflicts Thường Gặp**

**Tình huống 1: Hai người sửa cùng 1 file**

```typescript
// Developer A: Thêm function mới
// file: utils.ts (commit vào main)
export function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

export function formatCurrency(amount: number): string {  // ← A thêm
  return `$${amount.toFixed(2)}`;
}

// Developer B: Cũng thêm function (feature branch)
// file: utils.ts
export function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

export function calculateTax(amount: number): number {  // ← B thêm
  return amount * 0.1;
}

// Khi B merge → CONFLICT! (cùng thêm code vào cuối file)
```

**Giải pháp:**
```bash
# 1. Pull code mới THƯỜNG XUYÊN (mỗi ngày)
git checkout main
git pull origin main
git checkout feature/my-feature
git merge main  # Hoặc: git rebase main

# 2. Merge nhỏ, merge thường
# ❌ Không: Feature branch sống 2 tuần
# ✅ Nên: Feature branch sống 1-2 ngày, merge ngay

# 3. Chia nhỏ features
# ❌ Không: 1 PR có 50 files changes
# ✅ Nên: 1 PR có 5-10 files, dễ review, dễ merge

# 4. Communication!
# - Nói với team: "Tôi đang sửa file X"
# - Check PR của người khác trước khi bắt đầu
```

---

**Tình huống 2: Xung đột logic (không phải code conflict)**

```typescript
// Developer A: Đổi API response format
// api/user.ts
export async function getUser(id: string) {
  return {
    id,
    name: "John",
    email: "john@example.com",
    // age: 30  ← A XÓA field này (không cần nữa)
  };
}

// Developer B: Dùng field age trong component
// components/UserProfile.tsx
function UserProfile({ userId }: Props) {
  const user = await getUser(userId);
  
  return (
    <div>
      <p>Name: {user.name}</p>
      <p>Age: {user.age}</p>  {/* ← B dùng age! */}
    </div>
  );
}

// Kết quả: Code merge OK (không conflict)
// Nhưng runtime error: user.age is undefined!
```

**Giải pháp:**
```typescript
// 1. TypeScript giúp phát hiện!
// Khi A xóa field age, TypeScript sẽ báo lỗi ở component B

// 2. Code review kỹ
// Reviewer phải check: "Có ai đang dùng field này không?"

// 3. Deprecation process
// Thay vì xóa ngay, mark as deprecated trước
export async function getUser(id: string) {
  return {
    id,
    name: "John",
    email: "john@example.com",
    /** @deprecated Use birthDate instead */
    age: 30,
    birthDate: "1993-01-01",
  };
}

// Sau 1-2 sprints, search toàn bộ codebase:
// grep -r "user.age" src/
// Nếu không còn ai dùng → mới xóa!

// 4. API Versioning
// /api/v1/users → Trả về có age
// /api/v2/users → Không có age
```

---

**Tình huống 3: Database migration conflicts**

```typescript
// Developer A: Thêm column "phone"
// migrations/001_add_phone.sql
ALTER TABLE users ADD COLUMN phone VARCHAR(20);

// Developer B: Thêm column "address"
// migrations/002_add_address.sql (cùng thời điểm)
ALTER TABLE users ADD COLUMN address TEXT;

// Khi merge:
// - Nếu A merge trước → migrations/001 chạy OK
// - B merge sau → migrations/002 chạy OK
// - Nhưng trên main: có CẢ HAI migrations
// - Production: Chạy migrations theo thứ tự nào? 001 hay 002?
```

**Giải pháp:**
```bash
# 1. Migration với timestamp
# migrations/20241115_120000_add_phone.sql
# migrations/20241115_120100_add_address.sql
# → Thứ tự rõ ràng theo thời gian

# 2. Naming convention
# migrations/001_add_phone.sql
# migrations/002_add_address.sql
# → Nếu conflict, rename 002 → 003

# 3. Database migration tools
# - Flyway, Liquibase: Tự động quản lý thứ tự
# - Prisma, TypeORM: Generate migrations với timestamp

# 4. Communication
# Announce trong team chat: "Tôi đang tạo migration mới"
# → Người khác biết và tránh conflict
```

---

#### **4.2. Best Practices Tránh Conflicts**

```bash
# 1. Pull code thường xuyên (hàng ngày)
git checkout main
git pull origin main
git checkout feature/my-feature
git rebase main  # Hoặc merge main vào feature

# 2. Push code thường xuyên
# - Backup code (nếu máy hỏng)
# - Người khác biết bạn đang làm gì
git push origin feature/my-feature

# 3. Small PRs (Pull Requests nhỏ)
# ❌ Không: 1 PR = 50 files, 2000 lines
# ✅ Nên: 1 PR = 5-10 files, 200-300 lines
# → Dễ review, merge nhanh, ít conflict

# 4. Feature flags cho features lớn
# - Merge code vào main NGAY (tắt feature flag)
# - Không chờ feature hoàn thiện
# → Feature branch ngắn → ít conflict

# 5. Communication là chìa khóa!
# - Daily standup: "Hôm nay tôi sẽ sửa file X, Y"
# - Slack/Teams: "Ai đang làm việc với module authentication không?"
# - Code review: Xem PR của người khác, biết họ đang làm gì

# 6. Code ownership
# - Mỗi module có 1-2 người "owner"
# - Muốn sửa module → hỏi owner trước
# → Tránh 2 người sửa cùng lúc

# 7. Git hooks
# Pre-commit: Format code tự động (Prettier)
# Pre-push: Run tests
# → Tránh conflicts do format code khác nhau
```

---

#### **4.3. Resolve Conflicts Khi Xảy Ra**

```bash
# Tình huống: Merge conflict
git checkout main
git pull origin main
git checkout feature/my-feature
git merge main

# Auto-merging src/utils.ts
# CONFLICT (content): Merge conflict in src/utils.ts
# Automatic merge failed; fix conflicts and then commit the result.

# File src/utils.ts sẽ có dạng:
```

```typescript
export function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

<<<<<<< HEAD (your code - feature branch)
export function calculateTax(amount: number): number {
  return amount * 0.1; // 10% tax
}
=======
export function formatCurrency(amount: number): string {
  return `$${amount.toFixed(2)}`;
}
>>>>>>> main (their code - main branch)
```

**Cách resolve:**

```typescript
// Option 1: Giữ CẢ HAI (thường là đúng)
export function calculateTotal(items: Item[]): number {
  return items.reduce((sum, item) => sum + item.price, 0);
}

export function calculateTax(amount: number): number {
  return amount * 0.1; // 10% tax
}

export function formatCurrency(amount: number): string {
  return `$${amount.toFixed(2)}`;
}

// Option 2: Giữ của bạn (ít khi dùng)
// Xóa code của main, chỉ giữ code của bạn

// Option 3: Giữ của main (ít khi dùng)
// Xóa code của bạn, chỉ giữ code của main

// Option 4: Combine intelligent (phổ biến)
// Kết hợp logic của cả hai nếu cần thiết
```

```bash
# Sau khi resolve:
git add src/utils.ts
git commit -m "chore: resolve merge conflict in utils.ts"
git push origin feature/my-feature

# Tips resolve conflicts:
# 1. Hiểu code của CẢ HAI bên (your code và their code)
# 2. Test sau khi resolve (chạy tests, manual test)
# 3. Hỏi người viết code kia nếu không chắc
# 4. Dùng merge tools: VS Code, GitKraken, SourceTree
```

---

#### **4.4. Git Tools Giúp Collaboration**

```bash
# 1. Git Blame - Xem ai viết dòng code này
git blame src/utils.ts
# 3a4b5c6d (John Doe  2024-11-01 10:30:00 +0700  15) export function calculateTax() {
# → John Doe viết dòng này → Hỏi John nếu conflict

# 2. Git Log - Xem lịch sử file
git log --oneline src/utils.ts
# a1b2c3d feat: add calculateTax
# f4e5d6c fix: update calculateTotal
# → Hiểu file thay đổi như thế nào

# 3. Git Diff - So sánh changes
git diff main...feature/my-feature
# → Xem tất cả changes giữa main và feature branch

# 4. Git Stash - Tạm cất code chưa commit
# Tình huống: Đang code dở, cần pull code mới
git stash  # Cất code đang làm
git pull origin main
git stash pop  # Lấy code ra tiếp tục

# 5. Git Reflog - "Time machine" (lưu mọi thay đổi)
git reflog
# Nếu làm sai (merge nhầm, rebase lỗi) → quay lại!
git reset --hard HEAD@{2}  # Quay lại 2 bước trước
```

---

### **5. CI/CD với Git Workflow**

```yaml
# .github/workflows/ci.yml (GitHub Actions)
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]  # Chạy khi push vào main/develop
  pull_request:
    branches: [main, develop]  # Chạy khi tạo PR

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      # 1. Install dependencies
      - name: Install
        run: npm ci
      
      # 2. Lint code
      - name: Lint
        run: npm run lint
      
      # 3. Run tests
      - name: Test
        run: npm test
      
      # 4. Build
      - name: Build
        run: npm run build
      
      # 5. Deploy (chỉ khi merge vào main)
      - name: Deploy
        if: github.ref == 'refs/heads/main'
        run: npm run deploy

# Lợi ích:
# - Mọi PR phải pass tests mới được merge
# - Auto deploy khi merge vào main
# - Phát hiện bugs sớm (trước khi merge)
```

---

### **6. Git Commands Cheat Sheet - Các Lệnh Git Thường Dùng** 📝

#### **6.1. Setup & Configuration**

```bash
# ═══════════════════════════════════════════════════════════
# 1. CONFIG - Cấu hình Git
# ═══════════════════════════════════════════════════════════

# Set tên và email (bắt buộc cho mọi commit)
git config --global user.name "Nguyen Van A"
git config --global user.email "vana@company.com"

# Xem tất cả config
git config --list

# Set editor mặc định (VS Code, Vim, Nano...)
git config --global core.editor "code --wait"  # VS Code
git config --global core.editor "vim"          # Vim

# Bật màu sắc trong terminal (dễ đọc hơn)
git config --global color.ui auto

# Alias - Tạo shortcut cho lệnh dài
git config --global alias.st status           # git st = git status
git config --global alias.co checkout         # git co = git checkout
git config --global alias.br branch           # git br = git branch
git config --global alias.cm "commit -m"      # git cm "message" = git commit -m "message"
git config --global alias.last "log -1 HEAD" # Xem commit cuối cùng
git config --global alias.unstage "reset HEAD --"  # Bỏ file khỏi staging

# Set line ending (quan trọng khi team có Windows + Mac)
git config --global core.autocrlf true   # Windows
git config --global core.autocrlf input  # Mac/Linux

# Lưu credentials (không cần nhập password mỗi lần)
git config --global credential.helper cache  # Cache 15 phút
git config --global credential.helper store  # Lưu vĩnh viễn (không an toàn)
git config --global credential.helper "cache --timeout=3600"  # Cache 1 giờ
```

---

#### **6.2. Repository Operations**

```bash
# ═══════════════════════════════════════════════════════════
# 2. INIT & CLONE - Tạo mới hoặc clone repo
# ═══════════════════════════════════════════════════════════

# Tạo repo mới từ folder hiện tại
git init
git init my-project  # Tạo folder mới + init git

# Clone repo từ remote
git clone https://github.com/username/repo.git
git clone https://github.com/username/repo.git my-folder  # Clone vào folder tên khác
git clone --depth 1 https://github.com/username/repo.git  # Shallow clone (chỉ lấy commit mới nhất)

# Clone specific branch
git clone -b develop https://github.com/username/repo.git

# Add remote repository
git remote add origin https://github.com/username/repo.git

# Xem danh sách remotes
git remote -v

# Đổi URL remote (khi đổi repo)
git remote set-url origin https://github.com/username/new-repo.git

# Xóa remote
git remote remove origin
```

---

#### **6.3. Basic Workflow Commands**

```bash
# ═══════════════════════════════════════════════════════════
# 3. STATUS & DIFF - Xem thay đổi
# ═══════════════════════════════════════════════════════════

# Xem trạng thái hiện tại (file nào đã thay đổi)
git status
git status -s  # Short format (ngắn gọn hơn)

# Xem chi tiết thay đổi (chưa staging)
git diff
git diff src/app.ts  # Xem changes của file cụ thể

# Xem changes đã staging (chuẩn bị commit)
git diff --staged
git diff --cached  # Tương tự --staged

# So sánh 2 branches
git diff main..feature/login
git diff main...feature/login  # 3 dots = so sánh từ merge-base

# So sánh 2 commits
git diff a1b2c3d f4e5d6c

# Xem thay đổi của 1 file qua các commits
git log -p src/app.ts


# ═══════════════════════════════════════════════════════════
# 4. ADD & COMMIT - Lưu thay đổi
# ═══════════════════════════════════════════════════════════

# Add file vào staging area
git add src/app.ts                    # Add 1 file
git add src/                          # Add cả folder
git add .                             # Add tất cả files
git add *.ts                          # Add tất cả file .ts
git add -p                            # Add từng phần (interactive)

# Remove file khỏi staging (nhưng giữ changes)
git reset HEAD src/app.ts
git restore --staged src/app.ts       # Git 2.23+

# Discard changes (XÓA changes, cẩn thận!)
git checkout -- src/app.ts            # Git cũ
git restore src/app.ts                # Git 2.23+

# Commit changes
git commit -m "feat: add login feature"
git commit -m "fix: resolve login bug" -m "Detailed description here"

# Commit tất cả changes (tracked files) - bỏ qua git add
git commit -am "fix: update logic"

# Amend commit cuối (sửa commit message hoặc thêm files)
git add forgotten-file.ts
git commit --amend                     # Mở editor để sửa message
git commit --amend -m "New message"    # Sửa message trực tiếp
git commit --amend --no-edit           # Thêm files mà không đổi message

# Tạo empty commit (dùng để trigger CI/CD)
git commit --allow-empty -m "chore: trigger CI"


# ═══════════════════════════════════════════════════════════
# 5. PUSH & PULL - Đồng bộ với remote
# ═══════════════════════════════════════════════════════════

# Push lên remote
git push origin main                   # Push branch main
git push origin feature/login          # Push branch feature
git push -u origin feature/login       # Push + set upstream (lần đầu)
git push                               # Push (nếu đã set upstream)

# Force push (CẨN THẬN! Ghi đè lịch sử remote)
git push --force                       # ⚠️ Nguy hiểm!
git push --force-with-lease            # ✅ An toàn hơn (kiểm tra trước khi force)

# Push tags
git push origin v1.0.0                 # Push 1 tag
git push origin --tags                 # Push tất cả tags

# Pull từ remote
git pull origin main                   # Pull từ main
git pull                               # Pull từ upstream branch
git pull --rebase                      # Pull + rebase thay vì merge

# Fetch (lấy về nhưng không merge)
git fetch origin                       # Fetch tất cả branches
git fetch origin main                  # Fetch chỉ branch main
git fetch --all                        # Fetch từ tất cả remotes
git fetch --prune                      # Xóa references không còn trên remote
```

---

#### **6.4. Branch Management**

```bash
# ═══════════════════════════════════════════════════════════
# 6. BRANCH - Quản lý nhánh
# ═══════════════════════════════════════════════════════════

# Xem danh sách branches
git branch                             # Local branches
git branch -r                          # Remote branches
git branch -a                          # Tất cả (local + remote)
git branch -v                          # Với commit message cuối

# Tạo branch mới
git branch feature/login               # Tạo nhưng không chuyển sang
git checkout -b feature/login          # Tạo + chuyển sang
git switch -c feature/login            # Git 2.23+ (khuyến nghị)

# Chuyển branch
git checkout main                      # Git cũ
git switch main                        # Git 2.23+

# Đổi tên branch
git branch -m old-name new-name        # Đổi tên branch khác
git branch -m new-name                 # Đổi tên branch hiện tại

# Xóa branch
git branch -d feature/login            # Xóa local (safe - đã merge)
git branch -D feature/login            # Force xóa local (chưa merge)
git push origin --delete feature/login # Xóa remote branch

# Track remote branch
git checkout -b feature/login origin/feature/login
git switch -c feature/login --track origin/feature/login

# Xem branch nào đã merge vào main
git branch --merged main
git branch --no-merged main            # Ngược lại
```

---

#### **6.5. Merge & Rebase**

```bash
# ═══════════════════════════════════════════════════════════
# 7. MERGE - Gộp nhánh
# ═══════════════════════════════════════════════════════════

# Merge branch vào branch hiện tại
git checkout main
git merge feature/login                # Merge feature vào main

# Merge với commit message custom
git merge feature/login -m "Merge login feature"

# Merge nhưng không fast-forward (luôn tạo merge commit)
git merge --no-ff feature/login

# Hủy merge đang conflict
git merge --abort

# Xem files conflict
git status
git diff --name-only --diff-filter=U  # Chỉ xem tên files conflict


# ═══════════════════════════════════════════════════════════
# 8. REBASE - Tạo lịch sử tuyến tính
# ═══════════════════════════════════════════════════════════

# Rebase branch hiện tại lên main
git checkout feature/login
git rebase main

# Rebase interactive (chỉnh sửa commits)
git rebase -i HEAD~3                   # Chỉnh sửa 3 commits gần nhất
git rebase -i main                     # Rebase từ main

# Continue/Skip/Abort rebase
git rebase --continue                  # Tiếp tục sau khi resolve conflict
git rebase --skip                      # Bỏ qua commit hiện tại
git rebase --abort                     # Hủy rebase, quay lại trạng thái ban đầu

# Rebase và force push (cẩn thận!)
git rebase main
git push --force-with-lease            # ✅ An toàn hơn force
```

---

#### **6.6. Stash - Tạm cất code**

```bash
# ═══════════════════════════════════════════════════════════
# 9. STASH - Cất code tạm thời
# ═══════════════════════════════════════════════════════════

# Stash changes
git stash                              # Cất tất cả changes
git stash save "work in progress"      # Stash với message
git stash -u                           # Stash cả untracked files
git stash --include-untracked          # Tương tự -u

# Xem danh sách stashes
git stash list
# stash@{0}: WIP on main: a1b2c3d commit message
# stash@{1}: On feature: work in progress

# Apply stash (lấy ra nhưng giữ trong stash list)
git stash apply                        # Apply stash mới nhất
git stash apply stash@{1}              # Apply stash cụ thể

# Pop stash (lấy ra VÀ xóa khỏi stash list)
git stash pop                          # Pop stash mới nhất
git stash pop stash@{1}                # Pop stash cụ thể

# Xóa stash
git stash drop stash@{0}               # Xóa 1 stash
git stash clear                        # Xóa tất cả stashes

# Tạo branch từ stash
git stash branch feature/from-stash stash@{0}

# Xem changes trong stash
git stash show                         # Summary
git stash show -p                      # Full diff
git stash show stash@{1} -p           # Xem stash cụ thể
```

---

#### **6.7. Log & History**

```bash
# ═══════════════════════════════════════════════════════════
# 10. LOG - Xem lịch sử commits
# ═══════════════════════════════════════════════════════════

# Xem lịch sử commits
git log                                # Full log
git log --oneline                      # 1 dòng mỗi commit
git log --oneline --graph              # Với graph (branches)
git log --oneline --graph --all        # Tất cả branches

# Giới hạn số lượng commits
git log -5                             # 5 commits gần nhất
git log -n 10                          # 10 commits gần nhất

# Log với filter
git log --author="John Doe"            # Commits của John
git log --since="2 weeks ago"          # 2 tuần gần đây
git log --until="2024-11-01"           # Trước ngày 1/11/2024
git log --grep="fix"                   # Commit message có "fix"

# Log của 1 file
git log src/app.ts                     # Lịch sử file
git log -p src/app.ts                  # Với full diff
git log --follow src/app.ts            # Follow khi file rename

# Pretty format
git log --pretty=format:"%h - %an, %ar : %s"
# a1b2c3d - John Doe, 2 days ago : fix: resolve bug

# Xem ai viết dòng nào (blame)
git blame src/app.ts
git blame -L 10,20 src/app.ts          # Chỉ dòng 10-20

# Xem changes của 1 commit
git show a1b2c3d
git show a1b2c3d:src/app.ts            # Xem nội dung file tại commit đó
```

---

#### **6.8. Undo & Reset**

```bash
# ═══════════════════════════════════════════════════════════
# 11. RESET & REVERT - Undo changes
# ═══════════════════════════════════════════════════════════

# Reset về commit trước (XÓA commits)
git reset HEAD~1                       # Về 1 commit trước, GIỮ changes
git reset --soft HEAD~1                # Về 1 commit trước, changes vào staging
git reset --mixed HEAD~1               # Default, changes thành unstaged
git reset --hard HEAD~1                # ⚠️ XÓA HOÀN TOÀN changes!

git reset a1b2c3d                      # Reset về commit cụ thể
git reset --hard origin/main           # Reset về giống remote

# Revert commit (TẠO commit mới để undo)
git revert a1b2c3d                     # Revert 1 commit (an toàn cho public branch)
git revert HEAD                        # Revert commit cuối
git revert --no-commit a1b2c3d         # Revert nhưng chưa commit

# Unstage files (bỏ khỏi staging area)
git reset HEAD src/app.ts              # Git cũ
git restore --staged src/app.ts        # Git 2.23+

# Discard changes (XÓA changes chưa commit)
git checkout -- src/app.ts             # Git cũ
git restore src/app.ts                 # Git 2.23+ ✅

# Xóa untracked files
git clean -n                           # Dry-run (xem sẽ xóa gì)
git clean -f                           # Xóa untracked files
git clean -fd                          # Xóa cả folders
git clean -fX                          # Xóa chỉ files trong .gitignore
git clean -fx                          # Xóa tất cả (bao gồm .gitignore)
```

---

#### **6.9. Tags**

```bash
# ═══════════════════════════════════════════════════════════
# 12. TAG - Đánh dấu versions
# ═══════════════════════════════════════════════════════════

# Xem danh sách tags
git tag
git tag -l "v1.*"                      # Filter tags

# Tạo tag
git tag v1.0.0                         # Lightweight tag
git tag -a v1.0.0 -m "Release 1.0.0"   # Annotated tag (khuyến nghị)

# Tag commit cũ
git tag -a v0.9.0 a1b2c3d -m "Version 0.9.0"

# Xem thông tin tag
git show v1.0.0

# Push tags lên remote
git push origin v1.0.0                 # Push 1 tag
git push origin --tags                 # Push tất cả tags

# Xóa tag
git tag -d v1.0.0                      # Xóa local
git push origin --delete v1.0.0        # Xóa remote

# Checkout tag (xem code tại version cũ)
git checkout v1.0.0                    # Detached HEAD state
git checkout -b branch-from-tag v1.0.0 # Tạo branch từ tag
```

---

#### **6.10. Advanced Commands**

```bash
# ═══════════════════════════════════════════════════════════
# 13. REFLOG - Time machine Git
# ═══════════════════════════════════════════════════════════

# Xem tất cả thay đổi (kể cả đã xóa)
git reflog
git reflog show main                   # Reflog của branch main

# Quay lại trạng thái trước (undo mọi thứ!)
git reset --hard HEAD@{2}              # Quay lại 2 bước trước
git reset --hard a1b2c3d               # Quay lại commit cụ thể (từ reflog)

# Reflog expire (xóa old entries)
git reflog expire --expire=30.days --all


# ═══════════════════════════════════════════════════════════
# 14. CHERRY-PICK - Copy commit từ branch khác
# ═══════════════════════════════════════════════════════════

# Pick 1 commit từ branch khác
git cherry-pick a1b2c3d                # Copy commit a1b2c3d vào branch hiện tại
git cherry-pick a1b2c3d f4e5d6c        # Pick nhiều commits

# Cherry-pick với conflict
git cherry-pick --continue             # Continue sau khi resolve
git cherry-pick --abort                # Hủy cherry-pick

# Cherry-pick không commit ngay
git cherry-pick -n a1b2c3d             # Stage changes nhưng chưa commit


# ═══════════════════════════════════════════════════════════
# 15. BISECT - Tìm commit gây bug (binary search)
# ═══════════════════════════════════════════════════════════

# Start bisect
git bisect start
git bisect bad                         # Commit hiện tại có bug
git bisect good v1.0.0                 # Commit v1.0.0 không có bug

# Git sẽ checkout commit ở giữa, test xem có bug không
# Nếu có bug:
git bisect bad
# Nếu không có bug:
git bisect good

# Repeat cho đến khi tìm ra commit gây bug

# End bisect
git bisect reset


# ═══════════════════════════════════════════════════════════
# 16. WORKTREE - Nhiều working directories
# ═══════════════════════════════════════════════════════════

# Tạo worktree mới (làm việc nhiều branches cùng lúc)
git worktree add ../my-feature feature/login
# Tạo folder ../my-feature chứa code của feature/login
# Làm việc 2 branches đồng thời mà không cần stash!

# List worktrees
git worktree list

# Remove worktree
git worktree remove ../my-feature
git worktree prune                     # Cleanup old worktrees


# ═══════════════════════════════════════════════════════════
# 17. SUBMODULE - Quản lý dependencies
# ═══════════════════════════════════════════════════════════

# Add submodule
git submodule add https://github.com/user/repo.git libs/repo

# Clone repo với submodules
git clone --recursive https://github.com/user/repo.git

# Update submodules
git submodule update --init --recursive

# Pull submodule changes
git submodule update --remote


# ═══════════════════════════════════════════════════════════
# 18. GIT SHORTCUTS - Alias hữu ích
# ═══════════════════════════════════════════════════════════

# Thêm vào ~/.gitconfig hoặc chạy git config --global

git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status

# Undo last commit (giữ changes)
git config --global alias.undo 'reset HEAD~1 --mixed'

# Pretty log
git config --global alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"

# Xem branches sorted by last commit
git config --global alias.recent "branch --sort=-committerdate"

# Amend without editing message
git config --global alias.cane 'commit --amend --no-edit'

# Force push with lease
git config --global alias.pushf 'push --force-with-lease'
```

---

#### **6.11. .gitignore Patterns**

```bash
# ═══════════════════════════════════════════════════════════
# .gitignore - Bỏ qua files không cần track
# ═══════════════════════════════════════════════════════════

# Tạo file .gitignore
cat > .gitignore << EOF
# Dependencies
node_modules/
vendor/

# Build outputs
dist/
build/
*.min.js
*.min.css

# Environment variables
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Testing
coverage/
.nyc_output/

# Temporary
tmp/
temp/
*.tmp
EOF

# Ignore file đã tracked (nhưng giữ trong git history)
git rm --cached file.txt               # Remove from index
git rm -r --cached folder/             # Remove folder

# Xem files bị ignore
git status --ignored

# Check xem file có bị ignore không
git check-ignore -v file.txt

# Tạo global .gitignore (áp dụng cho tất cả repos)
git config --global core.excludesfile ~/.gitignore_global
```

---

#### **6.12. Git Hooks (Automation)**

```bash
# ═══════════════════════════════════════════════════════════
# Git Hooks - Tự động chạy scripts
# ═══════════════════════════════════════════════════════════

# Hooks nằm trong .git/hooks/
# Hoặc dùng tools: Husky (Node.js), pre-commit (Python)

# Example: pre-commit hook (format code trước khi commit)
# File: .git/hooks/pre-commit
#!/bin/sh
npm run lint
npm run format

# Nếu lỗi (exit code != 0) → commit bị hủy

# Example: commit-msg hook (validate commit message)
# File: .git/hooks/commit-msg
#!/bin/sh
commit_msg=$(cat $1)
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|chore):"; then
  echo "❌ Commit message phải bắt đầu bằng: feat|fix|docs|chore"
  exit 1
fi

# Dùng Husky (Node.js) - dễ hơn
npm install --save-dev husky
npx husky install
npx husky add .husky/pre-commit "npm run lint"
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

---

### **📊 Tóm Tắt So Sánh**

| Model | Phù hợp | Ưu điểm | Nhược điểm |
|-------|---------|---------|------------|
| **Git Flow** | Dự án lớn, release theo version | Rõ ràng, quản lý tốt | Phức tạp, nhiều conflicts |
| **GitHub Flow** | CI/CD, deploy liên tục | Đơn giản, ít conflicts | Khó quản lý versions |
| **Trunk-Based** | Team giỏi, CI/CD mạnh | Cực đơn giản | Cần tests tốt, feature flags |

| Kỹ thuật | Khi nào dùng | Tránh |
|----------|--------------|-------|
| **Merge** | Public branches (main, develop) | Feature branches (history rối) |
| **Rebase** | Feature branches (local) | Public branches (conflicts team) |
| **Feature Flags** | Features lớn, A/B testing | Features nhỏ (overhead) |

---

### **🎯 Best Practices Cuối Cùng**

**Senior Developer nên:**

1. ✅ **Hiểu rõ Git Flow của team** - Tuân thủ quy tắc chung
2. ✅ **Pull code hàng ngày** - Tránh conflicts lớn
3. ✅ **Small PRs** - 200-300 lines, dễ review, merge nhanh
4. ✅ **Feature flags cho features lớn** - Deploy sớm, ít conflicts
5. ✅ **Communicate với team** - Biết ai đang làm gì, tránh đụng độ
6. ✅ **Code review kỹ** - Phát hiện conflicts logic sớm
7. ✅ **Rebase local, merge public** - History sạch nhưng an toàn
8. ✅ **CI/CD automation** - Tests tự động, deploy tự động

**💡 Remember:**
> "Git workflow tốt = ít conflicts + deploy nhanh + dễ rollback. Communication > Tools!" 🚀

