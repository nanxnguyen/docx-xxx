# 🏗️ Q62: Xây Dựng Frontend Project từ Zero đến Production-Ready

## **⭐ PHIÊN BẢN TRẢ LỜI 1 PHÚT (Cho Phỏng Vấn Nhanh)**

**"Build Frontend project production-ready cần 8 giai đoạn: Setup Project (Thiết lập dự án) → Architecture (Kiến trúc) → Code Quality (Chất lượng code) → Performance (Hiệu suất) → Testing (Kiểm thử) → CI/CD (Tích hợp/Triển khai liên tục) → Monitoring (Giám sát) → Scalability (Khả năng mở rộng).**

**Đã lead team build Banking Dashboard từ zero: Nx monorepo (Monorepo Nx - Quản lý nhiều app/lib trong 1 repo) với 15 apps/libs, ESLint + Prettier + Husky enforce standards (ESLint + Prettier + Husky thực thi tiêu chuẩn), Vite build optimization (Tối ưu build Vite - 3s → 0.8s), React Query + Zustand state management (Quản lý state), Vitest + Playwright testing (Kiểm thử - 85% coverage - Độ phủ 85%), GitHub Actions CI/CD auto deploy (Tự động triển khai), Sentry monitoring errors (Giám sát lỗi), scalable đến 50+ developers collaboration (Mở rộng cho 50+ lập trình viên).**

**Key principles (Nguyên tắc chính): Clear folder structure (feature-based - Cấu trúc thư mục rõ ràng theo tính năng), Shared libraries (DRY - Thư viện dùng chung - Don't Repeat Yourself), Automated tooling (ESLint, TypeScript strict - Công cụ tự động), Performance budgets (Lighthouse CI - Ngân sách hiệu suất), Modular architecture (micro-frontends ready - Kiến trúc mô-đun sẵn sàng micro-frontend). Result: 70% faster development (Phát triển nhanh hơn 70%), 90% fewer bugs (Ít lỗi hơn 90%), deploy 20 times/day (Triển khai 20 lần/ngày).**

**Critical (Quan trọng): TypeScript strict mode (Chế độ nghiêm ngặt TypeScript), path aliases (Bí danh đường dẫn), absolute imports (Import tuyệt đối), automated code review (Tự động review code), bundle analysis (Phân tích bundle), environment variables management (Quản lý biến môi trường), comprehensive testing strategy từ đầu (Chiến lược kiểm thử toàn diện từ đầu) - không phải "sẽ làm sau"."**

---

## **📋 2. GIẢI THÍCH CHI TIẾT CẤP SENIOR/STAFF**

### **🎯 Tổng Quan Roadmap**

```
GIAI ĐOẠN 1: FOUNDATION (Ngày 1-3)
├─ Setup project với tooling hiện đại
├─ TypeScript + ESLint + Prettier
└─ Git workflow & commit conventions

GIAI ĐOẠN 2: ARCHITECTURE (Ngày 4-7)
├─ Folder structure & naming conventions
├─ Shared libraries & code reusability
└─ State management strategy

GIAI ĐOẠN 3: CODE QUALITY (Ngày 8-14)
├─ Linting & formatting automation
├─ Type safety & validation
└─ Code review process

GIAI ĐOẠN 4: PERFORMANCE (Ngày 15-21)
├─ Bundle optimization
├─ Lazy loading & code splitting
└─ Performance monitoring

GIAI ĐOẠN 5: TESTING (Ngày 22-28)
├─ Unit tests (Vitest)
├─ Integration tests (Testing Library)
└─ E2E tests (Playwright)

GIAI ĐOẠN 6: CI/CD (Ngày 29-35)
├─ GitHub Actions workflows
├─ Automated deployment
└─ Environment management

GIAI ĐOẠN 7: MONITORING (Ngày 36-42)
├─ Error tracking (Sentry)
├─ Analytics & user behavior
└─ Performance metrics

GIAI ĐOẠN 8: SCALABILITY (Ongoing)
├─ Micro-frontends architecture
├─ Team collaboration patterns
└─ Documentation & onboarding
```

---

## **💻 3. CODE EXAMPLES - PRODUCTION READY**

### **GIAI ĐOẠN 1: FOUNDATION - Project Setup**

#### **Step 1.1: Khởi Tạo Project với Nx**

```bash
# =====================================
# TẠI SAO DÙNG NX? (Why use Nx?)
# =====================================
# ✅🏗️ Monorepo support - Quản lý multiple apps/libs trong 1 repo (tránh dependency hell)
# Monorepo = Monorepo (Quản lý nhiều app/lib trong 1 repository - Tránh dependency hell = Địa ngục phụ thuộc)
# ✅⚙️ Built-in code generators (nx g component, nx g library - tự động tạo boilerplate)
# Built-in code generators = Trình tạo code tích hợp (nx g = Nx generate - Tự động tạo code mẫu)
# boilerplate = Code mẫu (Code template - Code khởi tạo)
# ✅📊 Dependency graph visualization (nx graph - xem quan hệ giữa apps/libs)
# Dependency graph = Đồ thị phụ thuộc (Xem quan hệ giữa các app/lib - nx graph = Lệnh xem đồ thị)
# ✅🎯 Affected commands - Chỉ test/build code thay đổi (nx affected:test - tiết kiệm CI time 80%)
# Affected commands = Lệnh ảnh hưởng (Chỉ test/build code thay đổi - Tiết kiệm 80% thời gian CI)
# CI = Continuous Integration (Tích hợp liên tục)
# ✅💾⚡ Caching layer - Build/test nhanh hơn 10x nhờ local + remote cache (Nx Cloud)
# Caching layer = Lớp cache (Cache cục bộ + từ xa - Nhanh hơn 10x - Nx Cloud = Dịch vụ cache của Nx)
# ✅🔧 Task orchestration - Chạy parallel tasks với dependency resolution tự động
# Task orchestration = Điều phối tác vụ (Chạy song song với giải quyết phụ thuộc tự động)
# parallel = Song song (Chạy đồng thời)
# dependency resolution = Giải quyết phụ thuộc (Tự động sắp xếp thứ tự chạy)
# ✅📦 Plugin ecosystem - React, Angular, Next.js, Vite, Jest, Cypress, Storybook...
# Plugin ecosystem = Hệ sinh thái plugin (Nhiều plugin hỗ trợ các framework/tool)

# 🔹 Install Nx CLI globally (Cài đặt Nx CLI toàn cục)
npm install -g nx@latest  # 🌐 CLI tool để run nx commands
# CLI = Command Line Interface (Giao diện dòng lệnh - Tool chạy lệnh)
# globally = Toàn cục (Cài đặt cho toàn hệ thống, không chỉ project)

# 🔹 Create workspace với preset (Tạo workspace với mẫu có sẵn)
npx create-nx-workspace@latest my-app \
  --preset=react-monorepo \       # 📦⚛️ React monorepo template (apps + libs)
  # preset = Mẫu có sẵn (Template - React monorepo = Mẫu React với nhiều app/lib)
  # template = Mẫu (Cấu trúc dự án có sẵn)
  --packageManager=pnpm \         # 📦💾 pnpm - nhanh hơn npm 2x, tiết kiệm disk space
  # packageManager = Trình quản lý gói (pnpm = Nhanh hơn npm 2x, tiết kiệm dung lượng đĩa)
  # npm = Node Package Manager (Trình quản lý gói Node.js)
  # pnpm = Performant npm (npm hiệu suất cao)
  --nx-cloud=true                 # ☁️⚡ Enable remote caching (free tier 500 hours/month)
  # nx-cloud = Dịch vụ cache từ xa của Nx (Bật cache từ xa - Miễn phí 500 giờ/tháng)
  # remote caching = Cache từ xa (Lưu cache trên cloud - Nhiều dev dùng chung)

# 🏗️📂 Structure sau khi tạo:
# my-app/
# ├── apps/                       # 📱 Applications (deployable)
# │   ├── web/                    # 🌐 Main web app (customer-facing)
# │   ├── admin/                  # 🔐 Admin dashboard (internal tool)
# │   └── mobile/                 # 📱 React Native app (optional)
# ├── libs/                       # 📚 Shared libraries (reusable code)
# │   ├── shared/                 # 🔄 Shared code across all apps
# │   │   ├── ui/                 # 🎨 Shared UI components (Button, Input, Modal...)
# │   │   ├── utils/              # 🔧 Helper functions (formatDate, validateEmail...)
# │   │   ├── types/              # 📋 TypeScript types & interfaces
# │   │   └── api/                # 🌐 API client (axios instance, interceptors)
# │   └── features/               # 🎯 Feature modules (business logic)
# │       ├── auth/               # 🔐 Authentication feature (login, register, tokens)
# │       ├── dashboard/          # 📊 Dashboard feature (charts, stats)
# │       └── settings/           # ⚙️ Settings feature (profile, preferences)
# ├── tools/                      # 🔧 Custom scripts (generators, migrations)
# ├── .github/
# │   └── workflows/              # 🤖 GitHub Actions CI/CD
# ├── nx.json                     # ⚙️ Nx configuration (caching, tasks)
# ├── tsconfig.base.json          # 📋 Base TypeScript config (paths, compiler options)
# └── package.json                # 📦 Dependencies & scripts
```

#### **Step 1.2: TypeScript Configuration (Strict Mode)**

```json
// tsconfig.base.json
{
  "compilerOptions": {
    // ✅🔒 STRICT MODE - Bắt lỗi sớm nhất (bắt buộc cho production)
    // Strict Mode = Chế độ nghiêm ngặt (Bắt lỗi sớm - Bắt buộc cho production)
    "strict": true, // 🔒 Enable tất cả strict checks
    // strict = Nghiêm ngặt (Bật tất cả kiểm tra nghiêm ngặt)
    "strictNullChecks": true, // 🔒❌ Không cho null/undefined nếu không khai báo
    // strictNullChecks = Kiểm tra null nghiêm ngặt (Không cho null/undefined nếu không khai báo)
    "strictFunctionTypes": true, // 🔒🔧 Check function parameter types chặt chẽ
    // strictFunctionTypes = Kiểm tra kiểu hàm nghiêm ngặt (Kiểm tra kiểu tham số chặt chẽ)
    "strictBindCallApply": true, // 🔒📞 Check bind/call/apply arguments
    // strictBindCallApply = Kiểm tra bind/call/apply nghiêm ngặt (Kiểm tra đối số)
    // bind/call/apply = Các phương thức gọi hàm trong JavaScript
    "strictPropertyInitialization": true, // 🔒🏗️ Class properties phải init trong constructor
    // strictPropertyInitialization = Khởi tạo thuộc tính nghiêm ngặt (Thuộc tính class phải khởi tạo trong constructor)
    // constructor = Hàm khởi tạo (Hàm chạy khi tạo đối tượng)
    "noImplicitThis": true, // 🔒❓ Không cho 'this' kiểu any
    // noImplicitThis = Không cho this ngầm định (Không cho 'this' có kiểu any - Phải khai báo rõ)
    "noImplicitAny": true, // 🔒❓ Không cho type any tự động (phải khai báo rõ)
    // noImplicitAny = Không cho any ngầm định (Không cho kiểu any tự động - Phải khai báo rõ)
    // any = Kiểu bất kỳ (Mất type safety - Không an toàn)
    "noImplicitReturns": true, // 🔒↩️ Function phải return ở tất cả code paths
    // noImplicitReturns = Không cho return ngầm định (Function phải return ở tất cả đường dẫn code)
    // code paths = Đường dẫn code (Các nhánh logic trong function)
    "noFallthroughCasesInSwitch": true, // 🔒🔀 Switch case phải có break hoặc return
    // noFallthroughCasesInSwitch = Không cho rơi qua case (Switch case phải có break hoặc return)
    // fallthrough = Rơi qua (Không có break, code chạy tiếp case sau)
    "noUncheckedIndexedAccess": true, // 🔒📋 Array/object access trả về T | undefined (safety)
    // noUncheckedIndexedAccess = Không cho truy cập chỉ mục không kiểm tra (Array/object access trả về T | undefined - An toàn hơn)
    // indexed access = Truy cập chỉ mục (Truy cập phần tử mảng/object bằng index)
    "noUnusedLocals": true, // 🔒🗑️ Cảnh báo biến khai báo nhưng không dùng
    // noUnusedLocals = Không cho biến local không dùng (Cảnh báo biến khai báo nhưng không dùng)
    // locals = Biến cục bộ (Biến trong phạm vi function/block)
    "noUnusedParameters": true, // 🔒🗑️ Cảnh báo parameter không dùng (prefix _ để ignore)
    // noUnusedParameters = Không cho tham số không dùng (Cảnh báo tham số không dùng - Dùng _ để bỏ qua)
    // parameters = Tham số (Tham số của function)

    // ✅📦 MODULE RESOLUTION (chuẩn hiện đại)
    // Module Resolution = Giải quyết module (Cách TypeScript tìm và import modules)
    "module": "ESNext", // 📦 ES modules (import/export)
    // module = Module system (ESNext = ES modules hiện đại - import/export)
    // ES modules = ES modules (Hệ thống module của JavaScript - import/export)
    "moduleResolution": "bundler", // 🔧 Bundler resolution (Vite, Webpack, esbuild)
    // moduleResolution = Giải quyết module (bundler = Dùng bundler để resolve - Vite, Webpack, esbuild)
    // bundler = Trình đóng gói (Tool đóng gói code - Vite, Webpack, esbuild)
    "resolveJsonModule": true, // 📄 Cho phép import .json files
    // resolveJsonModule = Giải quyết module JSON (Cho phép import file .json)
    "esModuleInterop": true, // 🔄 Tương thích CommonJS & ES modules
    // esModuleInterop = Tương thích module (Tương thích giữa CommonJS và ES modules)
    // CommonJS = CommonJS (Hệ thống module cũ - require/module.exports)
    "allowSyntheticDefaultImports": true, // 🔄 Cho phép import default từ modules không có export default
    // allowSyntheticDefaultImports = Cho phép import default giả (Cho phép import default từ module không có export default)
    // synthetic = Giả (Tạo ra, không thật sự có)

    // ✅🗺️ PATH ALIASES - Import rõ ràng, dễ refactor
    // Path Aliases = Bí danh đường dẫn (Định nghĩa đường dẫn ngắn gọn - Import rõ ràng, dễ refactor)
    // refactor = Tái cấu trúc (Sửa code để cải thiện cấu trúc)
    "baseUrl": ".", // 🏠 Base directory cho path resolution
    // baseUrl = URL cơ sở (Thư mục gốc cho giải quyết đường dẫn - "." = Thư mục hiện tại)
    "paths": {
      "@app/*": ["apps/web/src/*"], // 🌐 App code (pages, features...)
      // @app = Bí danh cho app code (apps/web/src/* = Tất cả file trong apps/web/src)
      "@libs/shared/ui": ["libs/shared/ui/src/index.ts"], // 🎨 Shared UI components
      // @libs/shared/ui = Bí danh cho shared UI (libs/shared/ui/src/index.ts = File export UI components)
      "@libs/shared/utils": ["libs/shared/utils/src/index.ts"], // 🔧 Shared utilities
      // @libs/shared/utils = Bí danh cho shared utilities (Helper functions dùng chung)
      "@libs/shared/types": ["libs/shared/types/src/index.ts"], // 📋 Shared TypeScript types
      // @libs/shared/types = Bí danh cho shared types (TypeScript types dùng chung)
      "@libs/shared/api": ["libs/shared/api/src/index.ts"], // 🌐 API client
      // @libs/shared/api = Bí danh cho API client (Client gọi API)
      "@libs/features/*": ["libs/features/*/src/index.ts"] // 🎯 Feature modules
      // @libs/features/* = Bí danh cho feature modules (Modules tính năng - * = Tất cả features)
    },
    // 💡 Sử dụng: import { Button } from '@libs/shared/ui';
    // Sử dụng = Usage (Cách dùng - Import ngắn gọn, rõ ràng)
    // ❌ Thay vì: import { Button } from '../../../libs/shared/ui/src/Button';
    // Thay vì = Instead of (Thay vì import dài, khó đọc - Relative path = Đường dẫn tương đối)

    // ✅🎯 OUTPUT CONFIGURATION
    "target": "ES2022", // 🎯 Target modern browsers (Chrome 90+, Firefox 88+)
    "lib": ["ES2022", "DOM", "DOM.Iterable"], // 📚 Include ES2022 + DOM APIs (fetch, Promise, etc.)
    "jsx": "react-jsx", // ⚛️ React 17+ JSX transform (không cần import React)
    "declaration": true, // 📋 Generate .d.ts declaration files
    "declarationMap": true, // 🗺️ Generate .d.ts.map for IDE navigation
    "sourceMap": true, // 🗺️ Generate source maps cho debugging
    "skipLibCheck": true, // ⏩ Skip type check .d.ts files (faster build)
    "forceConsistentCasingInFileNames": true // 🔠 Case-sensitive imports (Linux/Mac compatibility)
  },
  "exclude": ["node_modules", "dist", "build", ".next"] // 🚫 Không compile các folder này
}
```

#### **Step 1.3: ESLint Configuration (Code Quality)**

```javascript
// .eslintrc.cjs
module.exports = {
  root: true,
  env: {
    browser: true,
    es2022: true,
    node: true,
  },
  extends: [
    'eslint:recommended',
    // eslint:recommended = ESLint được khuyến nghị (Các rules cơ bản được khuyến nghị)
    'plugin:@typescript-eslint/recommended',
    // @typescript-eslint/recommended = TypeScript ESLint được khuyến nghị (Rules cho TypeScript)
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    // @typescript-eslint/recommended-requiring-type-checking = TypeScript ESLint cần type checking (Rules cần kiểm tra kiểu)
    // type-checking = Kiểm tra kiểu (Phân tích kiểu TypeScript)
    'plugin:react/recommended',
    // react/recommended = React được khuyến nghị (Rules cho React)
    'plugin:react-hooks/recommended',
    // react-hooks/recommended = React Hooks được khuyến nghị (Rules cho React Hooks)
    // Hooks = Móc (useState, useEffect, etc. - Cơ chế quản lý state trong React)
    'plugin:jsx-a11y/recommended', // Accessibility
    // jsx-a11y/recommended = JSX Accessibility được khuyến nghị (Rules cho accessibility - Khả năng truy cập)
    // a11y = Accessibility (Khả năng truy cập - Viết tắt của accessibility)
    'plugin:import/recommended',
    // import/recommended = Import được khuyến nghị (Rules cho import/export)
    'plugin:import/typescript',
    // import/typescript = Import TypeScript (Rules import cho TypeScript)
    'prettier', // Phải để cuối cùng
    // prettier = Prettier (Tắt các ESLint rules conflict với Prettier - Phải để cuối cùng)
    // conflict = Xung đột (Mâu thuẫn giữa ESLint và Prettier)
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: [
      './tsconfig.json',
      './apps/*/tsconfig.json',
      './libs/*/tsconfig.json',
    ],
    ecmaFeatures: {
      jsx: true,
    },
  },
  plugins: [
    '@typescript-eslint',
    'react',
    'react-hooks',
    'jsx-a11y',
    'import',
    'unused-imports', // Auto remove unused imports
    'simple-import-sort', // Auto sort imports
  ],
  settings: {
    react: {
      version: 'detect',
    },
    'import/resolver': {
      typescript: {
        alwaysTryTypes: true,
        project: [
          './tsconfig.json',
          './apps/*/tsconfig.json',
          './libs/*/tsconfig.json',
        ],
      },
    },
  },
  rules: {
    // ===================================
    // 📋 TYPESCRIPT RULES - Type safety
    // ===================================
    // Type safety = An toàn kiểu (Đảm bảo kiểu dữ liệu đúng)
    '@typescript-eslint/no-unused-vars': [
      'error',
      {
        // ❌🗑️ Không cho unused variables (code smell)
        // unused variables = Biến không dùng (Code smell = Dấu hiệu code xấu)
        argsIgnorePattern: '^_', // ✅ Cho phép args bắt đầu bằng _ (unused bằng cố ý)
        // argsIgnorePattern = Mẫu bỏ qua tham số (Cho phép tham số bắt đầu bằng _ - Unused cố ý)
        // unused bằng cố ý = Cố tình không dùng (Tham số bắt buộc nhưng không dùng)
        varsIgnorePattern: '^_', // ✅ Cho phép vars bắt đầu bằng _ (tương tự)
        // varsIgnorePattern = Mẫu bỏ qua biến (Cho phép biến bắt đầu bằng _ - Tương tự)
      },
    ],
    '@typescript-eslint/no-explicit-any': 'error', // ❌❓ Cấm type 'any' (mất type safety)
    // no-explicit-any = Không cho any rõ ràng (Cấm khai báo type 'any' - Mất an toàn kiểu)
    // explicit = Rõ ràng (Khai báo rõ ràng)
    '@typescript-eslint/explicit-function-return-type': [
      'warn',
      {
        // ⚠️🔙 Khuyến nghị khai báo return type
        // explicit-function-return-type = Kiểu trả về hàm rõ ràng (Khuyến nghị khai báo kiểu trả về)
        allowExpressions: true, // ✅ Cho phép arrow function không cần
        // allowExpressions = Cho phép biểu thức (Cho phép arrow function không cần khai báo kiểu trả về)
        // arrow function = Hàm mũi tên (() => {} - Cú pháp hàm ngắn gọn)
        allowTypedFunctionExpressions: true, // ✅ Cho phép nếu function đã có type từ biến
        // allowTypedFunctionExpressions = Cho phép biểu thức hàm đã có kiểu (Nếu function đã có type từ biến thì không cần)
        // typed = Đã có kiểu (Đã được gán kiểu)
      },
    ],
    '@typescript-eslint/consistent-type-imports': [
      'error',
      {
        // 📥📋 Bắt buộc dùng 'import type' cho types
        // consistent-type-imports = Import kiểu nhất quán (Bắt buộc dùng 'import type' cho types)
        prefer: 'type-imports', // 💡 Giúp tree-shaking, tách types ra khỏi runtime code
        // prefer = Ưu tiên (Ưu tiên dùng 'import type')
        // tree-shaking = Loại bỏ code không dùng (Xóa code không sử dụng khi build)
        // runtime code = Code chạy (Code thực thi - Không phải types)
      },
    ],
    '@typescript-eslint/no-floating-promises': 'error', // ❌⌛ Promise phải await hoặc .catch (tránh unhandled rejection)
    // no-floating-promises = Không cho Promise trôi nổi (Promise phải await hoặc .catch - Tránh unhandled rejection)
    // floating = Trôi nổi (Không được xử lý)
    // unhandled rejection = Từ chối không xử lý (Promise bị reject nhưng không có .catch)
    '@typescript-eslint/await-thenable': 'error', // ❌⌛ Chỉ await promises, không await non-promise values
    // await-thenable = Await có thể then (Chỉ await promises - Không await giá trị không phải promise)
    // thenable = Có thể then (Có phương thức .then() - Promise)
    '@typescript-eslint/no-misused-promises': 'error', // ❌⌛ Không dùng Promise ở nơi không phù hợp (if, &&, ||)
    // no-misused-promises = Không lạm dụng Promise (Không dùng Promise ở nơi không phù hợp - if, &&, ||)
    // misused = Lạm dụng (Dùng sai chỗ)

    // ===================================
    // ⚛️ REACT RULES - Component best practices
    // ===================================
    // Component best practices = Thực hành tốt cho component (Các quy tắc tốt cho React component)
    'react/react-in-jsx-scope': 'off', // ✅⚛️ Không cần import React (React 17+ JSX transform)
    // react-in-jsx-scope = React trong phạm vi JSX (Không cần import React - React 17+ JSX transform)
    // JSX transform = Chuyển đổi JSX (React 17+ tự động chuyển JSX, không cần import React)
    'react/prop-types': 'off', // ✅📋 TypeScript xử lý props validation rồi
    // prop-types = Kiểu props (Tắt vì TypeScript đã xử lý validation props rồi)
    // props = Thuộc tính (Dữ liệu truyền vào component)
    // validation = Xác thực (Kiểm tra dữ liệu hợp lệ)
    'react/jsx-no-target-blank': [
      'error',
      {
        // ❌🔗 Bảo mật: <a target="_blank"> cần rel="noopener"
        // jsx-no-target-blank = Không cho target="_blank" không an toàn (Cần rel="noopener" - Bảo mật)
        // target="_blank" = Mở tab mới (Mở link trong tab mới)
        // rel="noopener" = Không mở (Bảo mật - Ngăn trang mới truy cập window.opener)
        allowReferrer: false, // 🚫 Không gửi referrer (bảo mật)
        // allowReferrer = Cho phép referrer (Không gửi referrer - Bảo mật)
        // referrer = Người giới thiệu (Thông tin trang nguồn)
        enforceDynamicLinks: 'always', // ✅ Apply cho cả dynamic href
        // enforceDynamicLinks = Thực thi link động (Áp dụng cho cả href động - Luôn luôn)
        // dynamic href = href động (href được tạo từ biến - Không phải hardcode)
      },
    ],
    'react/jsx-key': [
      'error',
      {
        // ❌🔑 Bắt buộc key trong .map() (React performance)
        // jsx-key = Key trong JSX (Bắt buộc key trong .map() - React performance)
        // key = Khóa (React dùng key để theo dõi phần tử - Quan trọng cho performance)
        // .map() = Phương thức map (Duyệt và tạo mảng mới)
        checkFragmentShorthand: true, // ✅ Check cả <> fragment shorthand
        // checkFragmentShorthand = Kiểm tra fragment viết tắt (Kiểm tra cả <> - Fragment viết tắt)
        // fragment = Mảnh (React Fragment - <>...</> - Không tạo thẻ HTML)
        // shorthand = Viết tắt (Cú pháp ngắn gọn)
      },
    ],
    'react-hooks/rules-of-hooks': 'error', // ❌🎣 Chỉ gọi hooks trong component/custom hooks
    // rules-of-hooks = Quy tắc hooks (Chỉ gọi hooks trong component/custom hooks)
    // hooks = Móc (useState, useEffect, etc. - Cơ chế quản lý state trong React)
    // custom hooks = Hooks tùy chỉnh (Hooks tự tạo - Function bắt đầu bằng "use")
    'react-hooks/exhaustive-deps': 'warn', // ⚠️📋 useEffect dependencies phải đầy đủ (tránh stale closure)
    // exhaustive-deps = Phụ thuộc đầy đủ (useEffect dependencies phải đầy đủ - Tránh stale closure)
    // useEffect = Effect hook (Hook chạy side effects - Chạy sau khi render)
    // dependencies = Phụ thuộc (Mảng dependencies - [dep1, dep2])
    // stale closure = Closure cũ (Closure giữ giá trị cũ - Bug phổ biến)
    // closure = Đóng (Function giữ biến từ scope bên ngoài)

    // ===================================
    // 📦 IMPORT RULES - Clean imports
    // ===================================
    // Clean imports = Import sạch (Import rõ ràng, không lộn xộn)
    'import/no-unresolved': 'error', // ❌🔍 Tất cả imports phải resolve được
    // no-unresolved = Không cho import không giải quyết được (Tất cả imports phải tìm thấy file)
    // resolve = Giải quyết (Tìm và load module)
    'import/no-cycle': 'error', // ❌🔄 Ngăn circular dependencies (A import B, B import A)
    // no-cycle = Không cho vòng lặp (Ngăn circular dependencies - A import B, B import A)
    // circular dependencies = Phụ thuộc vòng tròn (A phụ thuộc B, B phụ thuộc A - Gây lỗi)
    'import/no-duplicates': 'error', // ❌🔁 Không import duplicate từ cùng 1 module
    // no-duplicates = Không cho trùng lặp (Không import nhiều lần từ cùng 1 module)
    // duplicate = Trùng lặp (Lặp lại)
    'simple-import-sort/imports': 'error', // 🔢 Auto sort imports (external → internal → relative)
    // simple-import-sort/imports = Sắp xếp import đơn giản (Tự động sắp xếp - external → internal → relative)
    // external = Bên ngoài (Package từ node_modules)
    // internal = Nội bộ (Code trong project)
    // relative = Tương đối (Import bằng đường dẫn tương đối - ./ hoặc ../)
    'simple-import-sort/exports': 'error', // 🔢 Auto sort exports
    // simple-import-sort/exports = Sắp xếp export đơn giản (Tự động sắp xếp exports)
    // exports = Xuất (export - Xuất function/class/constant)
    'unused-imports/no-unused-imports': 'error', // 🗑️❌ Auto remove unused imports
    // no-unused-imports = Không cho import không dùng (Tự động xóa import không dùng)
    // unused = Không dùng (Import nhưng không sử dụng)

    // ===================================
    // 🔧 GENERAL RULES - Code quality
    // ===================================
    // Code quality = Chất lượng code (Đảm bảo code tốt, dễ đọc, dễ maintain)
    'no-console': ['warn', { allow: ['warn', 'error'] }], // ⚠️💬 console.log cảnh báo (dùng logger thay thế)
    // no-console = Không cho console (console.log cảnh báo - Dùng logger thay thế)
    // logger = Trình ghi log (Tool ghi log chuyên nghiệp - Thay thế console.log)
    'no-debugger': 'error', // ❌🐛 Cấm debugger statement (quên xóa khi commit)
    // no-debugger = Không cho debugger (Cấm debugger statement - Quên xóa khi commit)
    // debugger = Trình gỡ lỗi (Statement dừng code để debug - Phải xóa trước khi commit)
    // commit = Cam kết (Lưu code vào git)
    'no-alert': 'error', // ❌⚠️ Cấm alert/confirm/prompt (dùng Modal component)
    // no-alert = Không cho alert (Cấm alert/confirm/prompt - Dùng Modal component thay thế)
    // alert/confirm/prompt = Cảnh báo/Xác nhận/Nhập (Dialog của browser - Không đẹp, không tùy chỉnh)
    // Modal component = Component modal (Component dialog tùy chỉnh - Đẹp hơn, linh hoạt hơn)
    'prefer-const': 'error', // ✅🔒 Dùng const thay vì let nếu không reassign
    // prefer-const = Ưu tiên const (Dùng const thay vì let nếu không gán lại)
    // const = Hằng số (Không thể gán lại - let = Biến có thể gán lại)
    // reassign = Gán lại (Thay đổi giá trị biến)
    'no-var': 'error', // ❌🚫 Cấm var (dùng const/let - block scope)
    // no-var = Không cho var (Cấm var - Dùng const/let - block scope)
    // var = Biến cũ (Function scope - Không nên dùng)
    // block scope = Phạm vi khối (const/let có phạm vi trong {} - An toàn hơn)
    eqeqeq: ['error', 'always'], // ❌=== Bắt buộc === thay vì == (type safety)
    // eqeqeq = So sánh bằng nghiêm ngặt (Bắt buộc === thay vì == - An toàn kiểu)
    // === = So sánh bằng nghiêm ngặt (So sánh giá trị và kiểu)
    // == = So sánh bằng lỏng (Chỉ so sánh giá trị - Không an toàn)
  },
};
```

#### **Step 1.4: Prettier Configuration**

```javascript
// .prettierrc.cjs
module.exports = {
  semi: true,
  singleQuote: true,
  trailingComma: 'es5',
  tabWidth: 2,
  useTabs: false,
  printWidth: 100,
  arrowParens: 'always',
  endOfLine: 'lf',
  bracketSpacing: true,
  jsxSingleQuote: false,
  quoteProps: 'as-needed',

  // Plugin-specific
  plugins: [
    'prettier-plugin-tailwindcss', // Auto sort Tailwind classes
  ],

  // Override cho specific files
  overrides: [
    {
      files: '*.json',
      options: {
        printWidth: 80,
      },
    },
  ],
};
```

#### **Step 1.5: Git Hooks với Husky + lint-staged**

```bash
# 🎣🔐 Install Husky + lint-staged + commitlint
pnpm add -D husky lint-staged @commitlint/cli @commitlint/config-conventional
# husky: Git hooks framework (đăng ký hooks vào .git/hooks)
# Husky = Husky (Framework Git hooks - Đăng ký hooks vào .git/hooks)
# Git hooks = Móc Git (Script tự động chạy khi có sự kiện Git - pre-commit, commit-msg, etc.)
# hooks = Móc (Script tự động chạy)
# lint-staged: Chạy linters chỉ trên staged files (🚀 nhanh hơn full repo)
# lint-staged = Lint đã stage (Chạy linters chỉ trên file đã stage - Nhanh hơn full repo)
# staged files = File đã stage (File đã được git add - Sẵn sàng commit)
# linters = Trình lint (Tool kiểm tra code - ESLint, Prettier, etc.)
# full repo = Toàn bộ repo (Tất cả file trong repository)
# commitlint: Validate commit messages theo chuẩn (Conventional Commits)
# commitlint = Lint commit message (Kiểm tra commit message theo chuẩn)
# Conventional Commits = Commit theo quy ước (Chuẩn commit message - feat:, fix:, etc.)

# 🔹 Setup husky (tạo .husky/ folder)
npx husky install
# ➡️ Tạo .husky/pre-commit, .husky/commit-msg hooks

# 🔹 Thêm prepare script vào package.json
npm pkg set scripts.prepare="husky install"
# 💡 'prepare' chạy tự động sau npm install (setup hooks cho team members)
```

```javascript
// .husky/pre-commit
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# 🎣🔍 Run lint-staged - Check code quality trước khi commit
pnpm lint-staged
# ➡️ Nếu lint/format fail → commit bị block ❌
# 💡 Chỉ check staged files (🚀 nhanh), không check toàn bộ repo
```

```javascript
// .husky/commit-msg
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# 💬✅ Validate commit message format
npx --no -- commitlint --edit ${1}
# ➡️ ${1} = .git/COMMIT_EDITMSG (commit message file)
# 💡 Nếu message không theo chuẩn Conventional Commits → reject ❌
# ✅ Ví dụ hợp lệ: "feat: add login page", "fix: resolve CORS issue"
# ❌ Ví dụ không hợp lệ: "update code", "FEAT: Add Feature" (uppercase)
```

```javascript
// .lintstagedrc.cjs
// lintstagedrc = Lint-staged config (File cấu hình lint-staged)
module.exports = {
  // 📋🔍 TypeScript files - Full validation pipeline
  // Full validation pipeline = Pipeline xác thực đầy đủ (Chuỗi kiểm tra đầy đủ)
  '*.{ts,tsx}': [
    // *.{ts,tsx} = Tất cả file .ts và .tsx (TypeScript files)
    'eslint --fix', // ✅🔧 Auto fix ESLint errors (imports, formatting, unused vars...)
    // eslint --fix = ESLint tự động sửa (Sửa lỗi ESLint - imports, formatting, unused vars...)
    // auto fix = Tự động sửa (Sửa lỗi tự động)
    'prettier --write', // ✅🎨 Auto format code (indentation, quotes, spacing...)
    // prettier --write = Prettier ghi (Tự động format code - indentation, quotes, spacing...)
    // format = Định dạng (Sắp xếp code đẹp - Indentation, quotes, spacing)
    // indentation = Thụt lề (Khoảng cách đầu dòng)
    () => 'tsc --noEmit', // ✅📋 Type check toàn bộ project (không generate .js files)
    // tsc --noEmit = TypeScript compiler không emit (Type check toàn bộ project - Không generate .js files)
    // type check = Kiểm tra kiểu (Kiểm tra lỗi TypeScript)
    // generate = Tạo (Tạo file .js từ .ts)
    // 💡 Lưu ý: tsc --noEmit check toàn bộ, không chỉ staged files (vì types có thể affect nhau)
    // affect = Ảnh hưởng (Types có thể ảnh hưởng lẫn nhau)
  ],

  // 📦 JavaScript files - Lint + Format
  // JavaScript files = File JavaScript (.js, .jsx)
  '*.{js,jsx}': [
    'eslint --fix', // ✅🔧 Fix JS linting issues
    // Fix JS linting issues = Sửa vấn đề lint JS (Sửa lỗi ESLint cho JavaScript)
    'prettier --write', // ✅🎨 Format JS code
    // Format JS code = Định dạng code JS (Sắp xếp code JavaScript đẹp)
  ],

  // 📄🎨 JSON, CSS, Markdown - Format only
  // Format only = Chỉ format (Không lint - Vì JSON/CSS không có ESLint rules)
  '*.{json,css,scss,md}': [
    'prettier --write', // ✅🎨 Chỉ format, không lint (vì JSON/CSS không có ESLint rules)
    // Chỉ format = Only format (Chỉ sắp xếp đẹp - Không kiểm tra lỗi)
    // JSON = JSON (Định dạng dữ liệu)
    // CSS = CSS (Styling)
    // SCSS = SCSS (CSS với biến, nesting)
    // Markdown = Markdown (Định dạng văn bản)
  ],

  // 🧪🔍 Test files - Run related tests
  // Test files = File kiểm thử (.test.ts, .spec.ts)
  '*.{test,spec}.{ts,tsx}': [
    'vitest related --run', // ✅🧪 Chạy tests liên quan đến file thay đổi
    // vitest related --run = Vitest chạy liên quan (Chạy tests liên quan đến file thay đổi)
    // related = Liên quan (Tìm tests import file này)
    // --run = Chạy (Chạy tests một lần - Không watch)
    // 💡 'related' tìm tests import file này (không chạy toàn bộ test suite)
    // test suite = Bộ kiểm thử (Tất cả tests trong project)
    // 🚀 Nhanh hơn full test, vẫn đảm bảo không phá tests
    // phá tests = Break tests (Làm tests bị lỗi)
  ],
};

// 💡 Workflow:
// 1️⃣ git add file.ts         (💾 Stage file)
// 2️⃣ git commit -m "..."     (👉 Trigger pre-commit hook)
// 3️⃣ lint-staged chạy         (⚙️ ESLint, Prettier, TypeScript check)
// 4️⃣ Nếu pass → commit ✅   / Nếu fail → block ❌
```

```javascript
// commitlint.config.cjs
module.exports = {
  extends: ['@commitlint/config-conventional'], // 📋 Chuẩn Conventional Commits (Angular style)
  rules: {
    // 🎯 TYPE ENUM - Danh sách types hợp lệ
    // TYPE ENUM = Kiểu liệt kê (Danh sách types hợp lệ cho commit message)
    'type-enum': [
      2, // ❌ Error level (2 = error, 1 = warning, 0 = off)
      // Error level = Mức lỗi (2 = lỗi, 1 = cảnh báo, 0 = tắt)
      'always', // ✅ Luôn bắt buộc
      // always = Luôn luôn (Luôn bắt buộc phải có type)
      [
        'feat', // ✨🎉 New feature (thêm tính năng mới)
        // feat = Feature (Tính năng mới - Thêm tính năng mới)
        'fix', // 🐛🔧 Bug fix (sửa lỗi)
        // fix = Sửa (Sửa lỗi - Bug fix)
        'docs', // 📚📝 Documentation (cập nhật docs)
        // docs = Documentation (Tài liệu - Cập nhật docs)
        'style', // 🎨 Formatting, missing semicolons (không ảnh hưởng logic)
        // style = Phong cách (Formatting, thiếu semicolons - Không ảnh hưởng logic)
        // formatting = Định dạng (Sắp xếp code đẹp)
        // semicolons = Dấu chấm phẩy (;)
        'refactor', // ♻️🔧 Code refactor (không fix bug, không thêm feature)
        // refactor = Tái cấu trúc (Sửa code để cải thiện - Không fix bug, không thêm feature)
        'perf', // ⚡🚀 Performance improvement (tối ưu performance)
        // perf = Performance (Hiệu suất - Tối ưu performance)
        // performance = Hiệu suất (Tốc độ, tài nguyên)
        'test', // 🧪✅ Adding tests (thêm/sửa tests)
        // test = Kiểm thử (Thêm/sửa tests)
        'chore', // 🔧📦 Build, dependencies, tooling (cập nhật config, packages)
        // chore = Việc vặt (Build, dependencies, tooling - Cập nhật config, packages)
        // dependencies = Phụ thuộc (Packages cần thiết)
        // tooling = Công cụ (Tools, scripts)
        'revert', // ⏪❌ Revert a previous commit (rollback commit trước)
        // revert = Hoàn nguyên (Revert commit trước - Rollback)
        // rollback = Quay lại (Quay lại trạng thái trước)
        'ci', // 🤖⚙️ CI/CD changes (cập nhật GitHub Actions, pipelines)
        // ci = Continuous Integration (Tích hợp liên tục - Cập nhật GitHub Actions, pipelines)
        // CI/CD = Continuous Integration/Continuous Deployment (Tích hợp/Triển khai liên tục)
        // pipelines = Pipeline (Quy trình tự động)
      ],
    ],
    'subject-case': [2, 'never', ['upper-case']], // ❌ Subject không được viết hoa toàn bộ
    'subject-empty': [2, 'never'], // ❌ Subject không được để trống
    'subject-full-stop': [2, 'never', '.'], // ❌ Subject không kết thúc bằng dấu chấm
    'header-max-length': [2, 'always', 100], // ❌ Header tối đa 100 ký tự (title line)
  },
};

// 💬✅ Example valid commits:
// ✅ feat: add user authentication with JWT tokens
// ✅ fix: resolve memory leak in dashboard component
// ✅ docs: update API documentation for auth endpoints
// ✅ perf: optimize bundle size by lazy loading routes
// ✅ test: add unit tests for UserService
// ✅ chore: upgrade React to v18.2.0

// ❌⚠️ Example INVALID commits:
// ❌ Added new feature                    (missing type:)
// ❌ FEAT: Add feature                    (uppercase type)
// ❌ feat: Add Feature                    (uppercase subject)
// ❌ feat: add user authentication.       (kết thúc bằng dấu chấm)
// ❌ feat:add feature                     (thiếu space sau :)
// ❌ update: something                    ('update' không nằm trong type-enum)

// 💡 Commit message structure:
// <type>(<scope>): <subject>
//
// <body>
//
// <footer>

// 💬 Ví dụ full commit message:
// feat(auth): add OAuth2 login with Google
//
// - Implement Google OAuth2 flow
// - Add AuthService with token management
// - Create LoginButton component
//
// Closes #123
```

// ❌ FEAT: Add feature (uppercase subject)

````

#### **Step 1.6: Package.json Scripts**

```json
{
  "name": "my-app",
  "version": "1.0.0",
  "packageManager": "pnpm@8.15.0",
  "scripts": {
    "// === DEVELOPMENT ===": "",
    "dev": "nx serve web",
    "dev:admin": "nx serve admin",
    "dev:all": "nx run-many --target=serve --all",

    "// === BUILD ===": "",
    "build": "nx build web --configuration=production",
    "build:admin": "nx build admin --configuration=production",
    "build:all": "nx run-many --target=build --all",
    "build:affected": "nx affected --target=build",

    "// === TESTING ===": "",
    "test": "nx test",
    "test:watch": "nx test --watch",
    "test:coverage": "nx test --coverage",
    "test:affected": "nx affected --target=test",
    "e2e": "nx e2e web-e2e",

    "// === CODE QUALITY ===": "",
    "lint": "nx run-many --target=lint --all",
    "lint:fix": "nx run-many --target=lint --all --fix",
    "type-check": "tsc --noEmit",
    "format": "prettier --write .",
    "format:check": "prettier --check .",

    "// === GRAPH & ANALYSIS ===": "",
    "graph": "nx graph",
    "affected:graph": "nx affected:graph",
    "analyze": "nx run web:analyze",

    "// === UTILITIES ===": "",
    "clean": "nx reset && rm -rf node_modules dist .next",
    "prepare": "husky install",
    "precommit": "lint-staged",
    "generate:component": "nx g @nx/react:component",
    "generate:lib": "nx g @nx/react:lib"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.20.0",
    "@tanstack/react-query": "^5.14.0",
    "zustand": "^4.4.7",
    "axios": "^1.6.2",
    "zod": "^3.22.4"
  },
  "devDependencies": {
    "@nx/react": "^17.2.0",
    "@nx/vite": "^17.2.0",
    "typescript": "^5.3.3",
    "vite": "^5.0.8",
    "vitest": "^1.1.0",
    "@testing-library/react": "^14.1.2",
    "@playwright/test": "^1.40.1",
    "eslint": "^8.56.0",
    "prettier": "^3.1.1",
    "husky": "^8.0.3",
    "lint-staged": "^15.2.0",
    "@commitlint/cli": "^18.4.3"
  }
}
````

---

### **GIAI ĐOẠN 2: ARCHITECTURE - Folder Structure**

#### **Step 2.1: Feature-Based Folder Structure**

```typescript
// =====================================
// APPS/WEB/SRC/ STRUCTURE
// =====================================

apps/web/src/
├── app/                          # App root
│   ├── App.tsx                  # Main app component
│   ├── router.tsx               # Route configuration
│   └── providers.tsx            # Global providers (Query, Theme, etc.)
│
├── pages/                        # Route pages
│   ├── HomePage/
│   │   ├── index.tsx            # Page component
│   │   ├── HomePage.test.tsx    # Page tests
│   │   └── hooks/               # Page-specific hooks
│   │       └── useHomeData.ts
│   ├── DashboardPage/
│   ├── SettingsPage/
│   └── NotFoundPage/
│
├── features/                     # Feature modules
│   ├── auth/
│   │   ├── components/          # Feature components
│   │   │   ├── LoginForm/
│   │   │   │   ├── LoginForm.tsx
│   │   │   │   ├── LoginForm.test.tsx
│   │   │   │   └── LoginForm.module.css
│   │   │   └── RegisterForm/
│   │   ├── hooks/               # Feature hooks
│   │   │   ├── useAuth.ts
│   │   │   └── useLogin.ts
│   │   ├── api/                 # Feature API calls
│   │   │   └── authApi.ts
│   │   ├── store/               # Feature state
│   │   │   └── authStore.ts
│   │   ├── types/               # Feature types
│   │   │   └── auth.types.ts
│   │   └── utils/               # Feature utilities
│   │       └── tokenUtils.ts
│   │
│   ├── dashboard/
│   │   ├── components/
│   │   │   ├── DashboardStats/
│   │   │   ├── RecentActivity/
│   │   │   └── QuickActions/
│   │   ├── hooks/
│   │   ├── api/
│   │   └── types/
│   │
│   └── settings/
│
├── components/                   # Shared components
│   ├── ui/                      # Base UI components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   ├── Button.stories.tsx  # Storybook
│   │   │   └── Button.module.css
│   │   ├── Input/
│   │   ├── Modal/
│   │   └── Card/
│   │
│   ├── layout/                  # Layout components
│   │   ├── Header/
│   │   ├── Sidebar/
│   │   ├── Footer/
│   │   └── MainLayout/
│   │
│   └── common/                  # Common components
│       ├── ErrorBoundary/
│       ├── LoadingSpinner/
│       └── EmptyState/
│
├── hooks/                        # Shared hooks
│   ├── useLocalStorage.ts
│   ├── useDebounce.ts
│   ├── useMediaQuery.ts
│   └── useIntersectionObserver.ts
│
├── utils/                        # Utility functions
│   ├── format/
│   │   ├── date.ts
│   │   ├── currency.ts
│   │   └── number.ts
│   ├── validation/
│   │   └── schemas.ts           # Zod schemas
│   └── helpers/
│       ├── storage.ts
│       └── api.ts
│
├── services/                     # External services
│   ├── api/
│   │   ├── client.ts            # Axios instance
│   │   ├── interceptors.ts      # Request/response interceptors
│   │   └── endpoints.ts         # API endpoints constants
│   ├── analytics/
│   │   └── analytics.ts         # Google Analytics, etc.
│   └── monitoring/
│       └── sentry.ts            # Error monitoring
│
├── store/                        # Global state
│   ├── useAppStore.ts           # Zustand store
│   ├── slices/                  # Store slices
│   │   ├── userSlice.ts
│   │   └── uiSlice.ts
│   └── middleware/
│       └── logger.ts
│
├── types/                        # Global types
│   ├── api.types.ts
│   ├── common.types.ts
│   └── models/
│       ├── User.ts
│       └── Product.ts
│
├── constants/                    # Constants
│   ├── routes.ts
│   ├── config.ts
│   └── apiEndpoints.ts
│
├── styles/                       # Global styles
│   ├── globals.css
│   ├── variables.css
│   └── themes/
│       ├── light.css
│       └── dark.css
│
├── assets/                       # Static assets
│   ├── images/
│   ├── icons/
│   └── fonts/
│
└── __tests__/                    # Integration tests
    ├── setup.ts
    └── utils/
        └── testUtils.tsx        # Test helpers
```

#### **Step 2.2: Shared Libraries Structure**

```typescript
// =====================================
// LIBS/ STRUCTURE (Shared Code)
// =====================================

libs/
├── shared/
│   ├── ui/                      # Shared UI components
│   │   ├── src/
│   │   │   ├── index.ts        # Public API
│   │   │   ├── Button/
│   │   │   ├── Input/
│   │   │   └── Modal/
│   │   ├── project.json
│   │   └── tsconfig.json
│   │
│   ├── utils/                   # Shared utilities
│   │   ├── src/
│   │   │   ├── index.ts
│   │   │   ├── date/
│   │   │   ├── string/
│   │   │   └── number/
│   │   └── project.json
│   │
│   ├── types/                   # Shared TypeScript types
│   │   ├── src/
│   │   │   ├── index.ts
│   │   │   ├── api.types.ts
│   │   │   └── common.types.ts
│   │   └── project.json
│   │
│   └── api/                     # Shared API client
│       ├── src/
│       │   ├── index.ts
│       │   ├── client.ts
│       │   └── hooks/
│       │       ├── useQuery.ts
│       │       └── useMutation.ts
│       └── project.json
│
└── features/                     # Feature libraries
    ├── auth/                    # Authentication feature
    │   ├── src/
    │   │   ├── index.ts
    │   │   ├── components/
    │   │   ├── hooks/
    │   │   └── api/
    │   └── project.json
    │
    └── analytics/               # Analytics feature
        ├── src/
        └── project.json
```

#### **Step 2.3: Barrel Exports (index.ts)**

```typescript
// =====================================
// libs/shared/ui/src/index.ts
// =====================================

// ✅ Named exports cho tree-shaking
export { Button } from './Button/Button';
export { Input } from './Input/Input';
export { Modal } from './Modal/Modal';
export { Card } from './Card/Card';

// Export types
export type { ButtonProps } from './Button/Button';
export type { InputProps } from './Input/Input';
export type { ModalProps } from './Modal/Modal';

// ❌ AVOID: export * from './Button'
// Vì có thể export cả internal implementation details

// =====================================
// libs/shared/utils/src/index.ts
// =====================================

// Date utilities
export { formatDate, parseDate, addDays, isValid } from './date/dateUtils';

// String utilities
export { capitalize, truncate, slugify } from './string/stringUtils';

// Number utilities
export { formatCurrency, formatNumber, roundTo } from './number/numberUtils';

// Validation
export {
  validateEmail,
  validatePhone,
  validateURL,
} from './validation/validators';

// =====================================
// Usage trong app
// =====================================

// ✅ Clean imports với path aliases
import { Button, Modal } from '@libs/shared/ui';
import { formatDate, validateEmail } from '@libs/shared/utils';
import type { User, ApiResponse } from '@libs/shared/types';

// ❌ AVOID: Relative imports
// import { Button } from '../../../libs/shared/ui/src/Button/Button';
```

---

### **GIAI ĐOẠN 3: CODE QUALITY - Automated Tools**

#### **Step 3.1: TypeScript Strict Configuration Examples**

```typescript
// =====================================
// libs/shared/types/src/api.types.ts
// =====================================

// ✅ Strict type definitions
export interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
  timestamp: number;
}

export interface PaginatedResponse<T> extends ApiResponse<T[]> {
  pagination: {
    page: number;
    pageSize: number;
    total: number;
    totalPages: number;
  };
}

// ✅ Discriminated unions cho type safety
export type ApiError =
  | { type: 'network'; message: string; code?: undefined }
  | { type: 'validation'; message: string; errors: Record<string, string[]> }
  | { type: 'server'; message: string; code: number }
  | { type: 'timeout'; message: string; timeout: number };

// ✅ Utility types
export type Nullable<T> = T | null;
export type Optional<T> = T | undefined;
export type AsyncData<T> = {
  data: T | null;
  loading: boolean;
  error: ApiError | null;
};

// =====================================
// Usage với type guards
// =====================================

function handleError(error: ApiError): string {
  // TypeScript biết chính xác type trong mỗi case
  switch (error.type) {
    case 'network':
      return `Network error: ${error.message}`;

    case 'validation':
      return `Validation failed: ${Object.entries(error.errors)
        .map(([field, msgs]) => `${field}: ${msgs.join(', ')}`)
        .join('; ')}`;

    case 'server':
      return `Server error (${error.code}): ${error.message}`;

    case 'timeout':
      return `Request timeout after ${error.timeout}ms`;

    default:
      // TypeScript ensure exhaustiveness
      const _exhaustive: never = error;
      return 'Unknown error';
  }
}
```

#### **Step 3.2: Zod Schema Validation**

```typescript
// =====================================
// libs/shared/utils/src/validation/schemas.ts
// =====================================

import { z } from 'zod';
// z = Zod (Import Zod - Thư viện validation TypeScript-first)
// zod = Zod (Thư viện validation - Type-safe validation)

// ✅ Reusable schemas
// Reusable schemas = Schema tái sử dụng (Schema dùng lại nhiều nơi)
// schemas = Schema (Định nghĩa validation rules)
export const emailSchema = z.string().email('Invalid email format');
// emailSchema = Schema email (Schema validate email)
// z.string() = Chuỗi (Kiểu string - Zod string)
// .email() = Email (Validate định dạng email)
// 'Invalid email format' = Thông báo lỗi (Message khi validation fail)

export const passwordSchema = z
  // passwordSchema = Schema password (Schema validate password)
  .string()
  // .string() = Chuỗi (Kiểu string)
  .min(8, 'Password must be at least 8 characters')
  // .min(8) = Tối thiểu 8 (Password phải có ít nhất 8 ký tự)
  .regex(/[A-Z]/, 'Password must contain uppercase letter')
  // .regex() = Biểu thức chính quy (Kiểm tra pattern - Phải có chữ hoa)
  // regex = Regular expression (Biểu thức chính quy - Pattern matching)
  // [A-Z] = Chữ hoa (Pattern chữ hoa A-Z)
  // uppercase = Chữ hoa (Uppercase letter = Chữ cái viết hoa)
  .regex(/[a-z]/, 'Password must contain lowercase letter')
  // [a-z] = Chữ thường (Pattern chữ thường a-z)
  // lowercase = Chữ thường (Lowercase letter = Chữ cái viết thường)
  .regex(/[0-9]/, 'Password must contain number')
  // [0-9] = Số (Pattern số 0-9)
  .regex(/[^A-Za-z0-9]/, 'Password must contain special character');
// [^A-Za-z0-9] = Ký tự đặc biệt (Pattern không phải chữ/số - Special character)
// ^ = Không phải (Not - Trong regex)
// special character = Ký tự đặc biệt (!, @, #, $, etc.)

export const phoneSchema = z
  .string()
  .regex(/^(\+84|0)[0-9]{9,10}$/, 'Invalid Vietnam phone number');

// User schema
export const userSchema = z.object({
  id: z.string().uuid(),
  email: emailSchema,
  name: z.string().min(2).max(100),
  phone: phoneSchema.optional(),
  role: z.enum(['admin', 'user', 'guest']),
  createdAt: z.string().datetime(),
  updatedAt: z.string().datetime(),
});

// Infer TypeScript type từ Zod schema
// Infer = Suy luận (Tự động tạo TypeScript type từ Zod schema)
// TypeScript type = Kiểu TypeScript (Interface, type - Định nghĩa kiểu dữ liệu)
export type User = z.infer<typeof userSchema>;
// z.infer = Zod infer (Tạo TypeScript type từ Zod schema)
// typeof = Type of (Lấy type của schema)
// User = User type (TypeScript type cho User - Tự động từ userSchema)

// Login form schema
// Login form = Form đăng nhập (Form nhập email, password)
export const loginFormSchema = z.object({
  // z.object() = Object Zod (Schema cho object - Validate object)
  email: emailSchema,
  // email = Email (Dùng emailSchema đã định nghĩa)
  password: z.string().min(1, 'Password is required'),
  // password = Mật khẩu (String, tối thiểu 1 ký tự - Bắt buộc)
  // required = Bắt buộc (Phải có - Không được để trống)
  rememberMe: z.boolean().optional(),
  // rememberMe = Nhớ tôi (Boolean - Tùy chọn)
  // .optional() = Tùy chọn (Có thể không có - Không bắt buộc)
});

export type LoginFormData = z.infer<typeof loginFormSchema>;
// LoginFormData = Dữ liệu form đăng nhập (TypeScript type cho login form data)

// =====================================
// Usage trong component
// =====================================

import { useForm } from 'react-hook-form';
// useForm = useForm hook (React Hook Form hook - Quản lý form)
// react-hook-form = React Hook Form (Thư viện quản lý form - Validation, state)
import { zodResolver } from '@hookform/resolvers/zod';
// zodResolver = Zod resolver (Resolver tích hợp Zod với React Hook Form)
// resolver = Bộ giải quyết (Xử lý validation - Kết nối Zod với React Hook Form)
// @hookform/resolvers = Resolvers (Package chứa resolvers - Zod, Yup, etc.)
import { loginFormSchema, type LoginFormData } from '@libs/shared/utils';
// loginFormSchema = Schema form đăng nhập (Zod schema)
// LoginFormData = Dữ liệu form đăng nhập (TypeScript type)

function LoginForm() {
  const {
    // useForm = useForm hook (Trả về object chứa register, handleSubmit, errors, etc.)
    register,
    // register = Đăng ký (Đăng ký input với form - {...register('email')})
    handleSubmit,
    // handleSubmit = Xử lý submit (Xử lý khi submit form - handleSubmit(onSubmit))
    formState: { errors },
    // formState = Trạng thái form (State của form - errors, isValid, isDirty, etc.)
    // errors = Lỗi (Object chứa lỗi validation - { email: { message: '...' } })
  } = useForm<LoginFormData>({
    // useForm<LoginFormData> = useForm với type (TypeScript type cho form data)
    resolver: zodResolver(loginFormSchema),
    // resolver = Bộ giải quyết (Zod resolver - Kết nối Zod với React Hook Form)
    // zodResolver(loginFormSchema) = Zod resolver với schema (Validate bằng Zod schema)
  });

  const onSubmit = (data: LoginFormData) => {
    // onSubmit = Khi submit (Function chạy khi submit form)
    // data = Dữ liệu (Form data đã validate - Type-safe)
    // data is fully typed and validated
    // fully typed = Đầy đủ kiểu (TypeScript type đầy đủ)
    // validated = Đã validate (Đã kiểm tra hợp lệ)
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}

      <input type="password" {...register('password')} />
      {errors.password && <span>{errors.password.message}</span>}

      <button type="submit">Login</button>
    </form>
  );
}
```

#### **Step 3.3: Code Review Automation với Danger.js**

```bash
# Install
pnpm add -D danger
```

```typescript
// dangerfile.ts
import { danger, warn, fail, message, markdown } from 'danger';

// ===================================
// PR SIZE CHECK
// ===================================
const bigPRThreshold = 500;
const changes = danger.github.pr.additions + danger.github.pr.deletions;

if (changes > bigPRThreshold) {
  warn(
    `:exclamation: Large PR (${changes} lines changed). Consider breaking it into smaller PRs for easier review.`
  );
}

// ===================================
// PR DESCRIPTION CHECK
// ===================================
if (!danger.github.pr.body || danger.github.pr.body.length < 10) {
  fail('⚠️ Please add a meaningful description to your PR.');
}

// ===================================
// MISSING TESTS CHECK
// ===================================
const hasAppChanges = danger.git.modified_files.some(
  (file) => file.startsWith('apps/') && file.endsWith('.tsx')
);
const hasTestChanges = danger.git.modified_files.some(
  (file) => file.includes('.test.') || file.includes('.spec.')
);

if (hasAppChanges && !hasTestChanges) {
  warn('⚠️ App code changed but no tests added. Consider adding tests.');
}

// ===================================
// LOCKFILE CHECK
// ===================================
const hasPackageChanges = danger.git.modified_files.includes('package.json');
const hasLockfileChanges = danger.git.modified_files.includes('pnpm-lock.yaml');

if (hasPackageChanges && !hasLockfileChanges) {
  fail(
    '⚠️ package.json changed but pnpm-lock.yaml not updated. Run `pnpm install`.'
  );
}

// ===================================
// CONSOLE.LOG CHECK
// ===================================
const newOrModified = [
  ...danger.git.created_files,
  ...danger.git.modified_files,
];
const jsFiles = newOrModified.filter(
  (file) => file.endsWith('.ts') || file.endsWith('.tsx')
);

for (const file of jsFiles) {
  const content = await danger.github.utils.fileContents(file);

  if (content.includes('console.log')) {
    warn(
      `⚠️ Found \`console.log\` in ${file}. Remove before merging or use proper logger.`
    );
  }

  if (content.includes('debugger')) {
    fail(`🚫 Found \`debugger\` statement in ${file}. Remove before merging.`);
  }
}

// ===================================
// BUNDLE SIZE CHECK
// ===================================
const bundleAnalysis = danger.git.modified_files.find((file) =>
  file.includes('bundle-stats.json')
);

if (bundleAnalysis) {
  message('📊 Bundle size analysis available. Review the changes carefully.');
}

// ===================================
// CHANGELOG CHECK
// ===================================
const hasChangelog = danger.git.modified_files.includes('CHANGELOG.md');

if (!hasChangelog && changes > 100) {
  warn('📝 Consider updating CHANGELOG.md for significant changes.');
}

// ===================================
// SUMMARY
// ===================================
markdown(`
## PR Summary
- **Files Changed**: ${danger.git.created_files.length} created, ${danger.git.modified_files.length} modified, ${danger.git.deleted_files.length} deleted
- **Lines Changed**: +${danger.github.pr.additions} / -${danger.github.pr.deletions}
- **Commits**: ${danger.github.commits.length}
`);
```

```yaml
# .github/workflows/danger.yml
name: Danger JS

on:
  pull_request:
    types: [opened, edited, synchronize]

jobs:
  danger:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install

      - name: Run Danger
        run: pnpm danger ci
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

---

### **GIAI ĐOẠN 4: PERFORMANCE OPTIMIZATION**

#### **Step 4.1: Vite Build Configuration**

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import { visualizer } from 'rollup-plugin-visualizer';
import compression from 'vite-plugin-compression';
import { VitePWA } from 'vite-plugin-pwa';

export default defineConfig({
  plugins: [
    // ✅ React với SWC compiler (nhanh hơn Babel 20x)
    // SWC compiler = Trình biên dịch SWC (Nhanh hơn Babel 20x - Compile JavaScript/TypeScript)
    // compiler = Trình biên dịch (Chuyển code TypeScript/JSX thành JavaScript)
    // Babel = Babel (Trình biên dịch JavaScript cũ - Chậm hơn SWC)
    react(),

    // ✅ Bundle analyzer
    // Bundle analyzer = Phân tích bundle (Tool phân tích kích thước bundle)
    // bundle = Gói (File JavaScript đã đóng gói)
    visualizer({
      filename: 'dist/stats.html',
      // filename = Tên file (File kết quả phân tích - stats.html)
      gzipSize: true,
      // gzipSize = Kích thước gzip (Hiển thị kích thước sau khi nén gzip)
      // gzip = Gzip (Thuật toán nén - Giảm kích thước file)
      brotliSize: true,
      // brotliSize = Kích thước brotli (Hiển thị kích thước sau khi nén brotli)
      // brotli = Brotli (Thuật toán nén tốt hơn gzip)
    }),

    // ✅ Gzip compression
    // Gzip compression = Nén gzip (Nén file bằng gzip)
    // compression = Nén (Giảm kích thước file)
    compression({
      algorithm: 'gzip',
      // algorithm = Thuật toán (Thuật toán nén - gzip)
      ext: '.gz',
      // ext = Extension (Phần mở rộng file - .gz)
    }),

    // ✅ Brotli compression (tốt hơn gzip)
    // Brotli compression = Nén brotli (Nén file bằng brotli - Tốt hơn gzip)
    compression({
      algorithm: 'brotliCompress',
      // brotliCompress = Nén brotli (Thuật toán nén brotli)
      ext: '.br',
      // .br = Extension brotli (Phần mở rộng file brotli)
    }),

    // ✅ PWA support
    // PWA = Progressive Web App (Ứng dụng web tiến bộ - Hoạt động như app native)
    VitePWA({
      registerType: 'autoUpdate',
      // registerType = Loại đăng ký (autoUpdate = Tự động cập nhật)
      // autoUpdate = Tự động cập nhật (Tự động cập nhật khi có phiên bản mới)
      includeAssets: ['favicon.ico', 'robots.txt', 'apple-touch-icon.png'],
      // includeAssets = Bao gồm tài sản (Bao gồm các file tĩnh)
      // assets = Tài sản (File tĩnh - favicon, robots.txt, icon)
      // favicon = Favicon (Icon hiển thị trên tab browser)
      // robots.txt = Robots.txt (File hướng dẫn search engine)
      // apple-touch-icon = Icon Apple (Icon cho iOS)
      manifest: {
        // manifest = Manifest (File mô tả PWA)
        name: 'My App',
        // name = Tên (Tên ứng dụng)
        short_name: 'App',
        // short_name = Tên ngắn (Tên ngắn hiển thị trên home screen)
        theme_color: '#ffffff',
        // theme_color = Màu chủ đề (Màu chủ đề của app)
        icons: [
          // icons = Icon (Danh sách icon)
          {
            src: 'pwa-192x192.png',
            // src = Source (Nguồn - Đường dẫn icon)
            sizes: '192x192',
            // sizes = Kích thước (Kích thước icon - 192x192 pixels)
            type: 'image/png',
            // type = Loại (Loại file - image/png)
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
          },
        ],
      },
    }),
  ],

  build: {
    // ✅ Target modern browsers
    // Target = Mục tiêu (Target modern browsers = Nhắm đến trình duyệt hiện đại)
    // modern browsers = Trình duyệt hiện đại (Chrome, Firefox, Safari mới)
    target: 'esnext',
    // esnext = ES Next (JavaScript phiên bản mới nhất - ES2022+)

    // ✅ Minify với esbuild (nhanh)
    // Minify = Nén (Xóa khoảng trắng, rút gọn code - Giảm kích thước file)
    minify: 'esbuild',
    // esbuild = esbuild (Trình minify nhanh - Nhanh hơn Terser)

    // ✅ Source maps cho production debug
    // Source maps = Bản đồ nguồn (File map code đã minify về code gốc - Debug production)
    // production debug = Gỡ lỗi production (Debug code đã build)
    sourcemap: true,

    // ✅ Code splitting
    // Code splitting = Chia tách code (Chia code thành nhiều file nhỏ - Tải nhanh hơn)
    rollupOptions: {
      // rollupOptions = Tùy chọn Rollup (Cấu hình Rollup - Bundler của Vite)
      // Rollup = Rollup (Bundler đóng gói code)
      output: {
        // output = Đầu ra (Cấu hình file đầu ra)
        manualChunks: {
          // manualChunks = Chunks thủ công (Chia code thành chunks thủ công)
          // chunks = Khối (Các file JavaScript đã chia)
          // Vendor chunks
          // Vendor = Nhà cung cấp (Thư viện bên thứ ba - node_modules)
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          // react-vendor = Vendor React (Chunk chứa React, React DOM, React Router)
          'query-vendor': ['@tanstack/react-query'],
          // query-vendor = Vendor Query (Chunk chứa React Query)
          'ui-vendor': [
            '@radix-ui/react-dialog',
            '@radix-ui/react-dropdown-menu',
          ],
          // ui-vendor = Vendor UI (Chunk chứa UI libraries - Radix UI)

          // Feature chunks
          // Feature = Tính năng (Code tính năng - Dashboard, Settings)
          dashboard: ['./src/features/dashboard'],
          // dashboard = Dashboard (Chunk chứa code dashboard)
          settings: ['./src/features/settings'],
          // settings = Settings (Chunk chứa code settings)
        },

        // ✅ Chunk naming
        // Chunk naming = Đặt tên chunk (Quy tắc đặt tên file chunk)
        chunkFileNames: 'assets/js/[name]-[hash].js',
        // chunkFileNames = Tên file chunk (assets/js/[name]-[hash].js)
        // [name] = Tên chunk (Tên chunk - react-vendor, dashboard, etc.)
        // [hash] = Hash (Hash để cache busting - Thay đổi khi code thay đổi)
        // cache busting = Phá cache (Làm browser tải file mới)
        entryFileNames: 'assets/js/[name]-[hash].js',
        // entryFileNames = Tên file entry (File entry point - File bắt đầu)
        // entry = Điểm vào (File bắt đầu ứng dụng)
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]',
        // assetFileNames = Tên file asset (File tài sản - CSS, images, fonts)
        // assets = Tài sản (File tĩnh - CSS, images, fonts)
        // [ext] = Extension (Phần mở rộng - css, png, woff2)
      },
    },

    // ✅ Chunk size warnings
    // Chunk size warnings = Cảnh báo kích thước chunk (Cảnh báo khi chunk quá lớn)
    chunkSizeWarningLimit: 500, // 500kb
    // chunkSizeWarningLimit = Giới hạn cảnh báo kích thước chunk (500KB - Cảnh báo nếu chunk > 500KB)
    // 500kb = 500 kilobyte (Kích thước file - 500KB)
  },

  // ✅ Performance optimizations
  optimizeDeps: {
    include: ['react', 'react-dom'], // Pre-bundle dependencies
  },

  // ✅ Path aliases (sync with tsconfig)
  resolve: {
    alias: {
      '@app': '/src',
      '@libs/shared/ui': '/libs/shared/ui/src',
      '@libs/shared/utils': '/libs/shared/utils/src',
    },
  },
});
```

#### **Step 4.2: Code Splitting Strategy**

```typescript
// =====================================
// apps/web/src/app/router.tsx
// =====================================

import { lazy, Suspense } from 'react';
import { createBrowserRouter } from 'react-router-dom';
import { LoadingSpinner } from '@libs/shared/ui';

// ✅ Lazy load pages (route-based code splitting)
// Lazy load = Tải chậm (Tải code khi cần - Không tải ngay)
// route-based code splitting = Chia tách code theo route (Chia code theo trang)
const HomePage = lazy(() => import('../pages/HomePage'));
// lazy = Lười (React.lazy - Tải component khi cần)
// import = Nhập (Nhập module - Dynamic import = Nhập động)
const DashboardPage = lazy(() => import('../pages/DashboardPage'));
const SettingsPage = lazy(() => import('../pages/SettingsPage'));
const ProfilePage = lazy(() => import('../pages/ProfilePage'));

// ✅ Preload critical routes
// Preload = Tải trước (Tải code trước khi cần - Tăng tốc độ)
// critical routes = Route quan trọng (Trang quan trọng - Dashboard, Settings)
const preloadDashboard = () => import('../pages/DashboardPage');
// preloadDashboard = Tải trước Dashboard (Function tải Dashboard trước)
const preloadSettings = () => import('../pages/SettingsPage');

export const router = createBrowserRouter([
  {
    path: '/',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <HomePage />
      </Suspense>
    ),
  },
  {
    path: '/dashboard',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <DashboardPage />
      </Suspense>
    ),
    // ✅ Preload on hover (faster perceived performance)
    loader: async () => {
      await preloadDashboard();
      return null;
    },
  },
  {
    path: '/settings',
    element: (
      <Suspense fallback={<LoadingSpinner />}>
        <SettingsPage />
      </Suspense>
    ),
  },
]);

// =====================================
// Dynamic imports for heavy libraries
// =====================================

// ❌ BEFORE: Bundle bloat
import { Chart } from 'chart.js';

// ✅ AFTER: Lazy load only when needed
function DashboardChart() {
  const [Chart, setChart] = useState(null);

  useEffect(() => {
    import('chart.js').then((module) => {
      setChart(() => module.Chart);
    });
  }, []);

  if (!Chart) return <LoadingSpinner />;

  return <Chart {...props} />;
}

// ✅ BETTER: React.lazy for components
const HeavyChart = lazy(() => import('./HeavyChart'));

function Dashboard() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <HeavyChart data={data} />
    </Suspense>
  );
}
```

#### **Step 4.3: Performance Budget với Lighthouse CI**

```bash
# Install
pnpm add -D @lhci/cli
```

```javascript
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      startServerCommand: 'pnpm preview',
      url: ['http://localhost:4173'],
      numberOfRuns: 3,
    },
    assert: {
      preset: 'lighthouse:recommended',
      assertions: {
        // ✅ Performance budgets
        'first-contentful-paint': ['error', { maxNumericValue: 2000 }], // 2s
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }], // 2.5s
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-blocking-time': ['error', { maxNumericValue: 300 }], // 300ms
        'speed-index': ['error', { maxNumericValue: 3000 }], // 3s

        // ✅ Accessibility
        'categories:accessibility': ['error', { minScore: 0.9 }],

        // ✅ Best practices
        'categories:best-practices': ['error', { minScore: 0.9 }],

        // ✅ SEO
        'categories:seo': ['error', { minScore: 0.9 }],

        // ✅ Resource hints
        'uses-rel-preconnect': 'off',
        'uses-http2': 'warn',
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
```

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI

on:
  pull_request:
    branches: [main]

jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install

      - name: Build
        run: pnpm build

      - name: Run Lighthouse CI
        run: pnpm lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}
```

---

### **GIAI ĐOẠN 5: TESTING STRATEGY**

#### **Step 5.1: Vitest Configuration (Unit Tests)**

```typescript
// vitest.config.ts
import { defineConfig } from 'vitest/config';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  test: {
    // ✅ Environment
    environment: 'jsdom',

    // ✅ Setup files
    setupFiles: ['./src/__tests__/setup.ts'],

    // ✅ Coverage configuration
    // Coverage = Độ phủ (Tỷ lệ code được test - Code coverage)
    coverage: {
      provider: 'v8',
      // provider = Nhà cung cấp (v8 = V8 engine coverage - Engine của Chrome)
      // v8 = V8 (JavaScript engine của Chrome - Nhanh, chính xác)
      reporter: ['text', 'json', 'html', 'lcov'],
      // reporter = Báo cáo (Các định dạng báo cáo coverage)
      // text = Văn bản (Báo cáo dạng text trong terminal)
      // json = JSON (Báo cáo dạng JSON - Dùng cho CI/CD)
      // html = HTML (Báo cáo dạng HTML - Xem trong browser)
      // lcov = LCOV (Định dạng LCOV - Dùng cho Codecov, Coveralls)
      exclude: [
        // exclude = Loại trừ (Loại trừ các file/folder không cần test)
        'node_modules/',
        // node_modules = node_modules (Thư viện bên thứ ba - Không cần test)
        'src/__tests__/',
        // __tests__ = __tests__ (Folder test - Không cần test test files)
        '**/*.test.{ts,tsx}',
        // *.test = File test (File test - Không cần test test files)
        '**/*.spec.{ts,tsx}',
        // *.spec = File spec (File spec - Tương tự test files)
        '**/*.stories.{ts,tsx}',
        // *.stories = File stories (File Storybook - Không cần test)
        '**/types/',
        // types = Types (Folder types - Chỉ định nghĩa types, không có logic)
        '**/*.d.ts',
        // *.d.ts = Declaration files (File định nghĩa TypeScript - Không có code thực thi)
      ],
      // ✅ Coverage thresholds
      // Coverage thresholds = Ngưỡng độ phủ (Yêu cầu tối thiểu coverage)
      statements: 80,
      // statements = Câu lệnh (80% câu lệnh phải được test)
      branches: 75,
      // branches = Nhánh (75% nhánh if/else phải được test)
      functions: 80,
      // functions = Hàm (80% hàm phải được test)
      lines: 80,
      // lines = Dòng (80% dòng code phải được test)
    },

    // ✅ Globals (không cần import describe, it, expect)
    globals: true,

    // ✅ Watch mode
    watch: false,

    // ✅ Reporters
    reporters: ['default', 'html'],
  },
  resolve: {
    alias: {
      '@app': path.resolve(__dirname, './src'),
      '@libs/shared/ui': path.resolve(__dirname, './libs/shared/ui/src'),
      '@libs/shared/utils': path.resolve(__dirname, './libs/shared/utils/src'),
    },
  },
});
```

```typescript
// src/__tests__/setup.ts
import '@testing-library/jest-dom';
import { cleanup } from '@testing-library/react';
import { afterEach, vi } from 'vitest';

// ✅ Cleanup after each test
afterEach(() => {
  cleanup();
});

// ✅ Mock window.matchMedia
Object.defineProperty(window, 'matchMedia', {
  writable: true,
  value: vi.fn().mockImplementation((query) => ({
    matches: false,
    media: query,
    onchange: null,
    addListener: vi.fn(),
    removeListener: vi.fn(),
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
    dispatchEvent: vi.fn(),
  })),
});

// ✅ Mock IntersectionObserver
global.IntersectionObserver = class IntersectionObserver {
  constructor() {}
  disconnect() {}
  observe() {}
  takeRecords() {
    return [];
  }
  unobserve() {}
};

// ✅ Mock localStorage
const localStorageMock = {
  getItem: vi.fn(),
  setItem: vi.fn(),
  removeItem: vi.fn(),
  clear: vi.fn(),
};
global.localStorage = localStorageMock as any;
```

#### **Step 5.2: Test Utilities & Helpers**

```typescript
// src/__tests__/utils/testUtils.tsx
import { ReactElement } from 'react';
import { render, RenderOptions } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter } from 'react-router-dom';

// ✅ Custom render với providers
interface CustomRenderOptions extends Omit<RenderOptions, 'wrapper'> {
  initialRoute?: string;
}

export function renderWithProviders(
  ui: ReactElement,
  { initialRoute = '/', ...renderOptions }: CustomRenderOptions = {}
) {
  // Create fresh QueryClient mỗi test
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        retry: false, // Không retry trong tests
        cacheTime: 0,
      },
    },
  });

  // Wrapper với tất cả providers
  function Wrapper({ children }: { children: React.ReactNode }) {
    return (
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>{children}</BrowserRouter>
      </QueryClientProvider>
    );
  }

  // Set initial route
  window.history.pushState({}, 'Test page', initialRoute);

  return {
    ...render(ui, { wrapper: Wrapper, ...renderOptions }),
    queryClient,
  };
}

// ✅ Mock user factory
export function createMockUser(overrides = {}) {
  return {
    id: '123',
    email: 'test@example.com',
    name: 'Test User',
    role: 'user' as const,
    createdAt: '2024-01-01T00:00:00Z',
    ...overrides,
  };
}

// ✅ Wait for async operations
export const waitForLoadingToFinish = () =>
  waitFor(() => {
    expect(screen.queryByRole('progressbar')).not.toBeInTheDocument();
  });

// ✅ Mock API handlers
export const mockApiSuccess = <T>(data: T) => {
  return Promise.resolve({ data, status: 200, message: 'Success' });
};

export const mockApiError = (message: string, code = 500) => {
  return Promise.reject({
    response: {
      data: { message },
      status: code,
    },
  });
};
```

#### **Step 5.3: Component Test Examples**

```typescript
// libs/shared/ui/src/Button/Button.test.tsx
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('renders with correct text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByRole('button')).toHaveTextContent('Click me');
  });

  it('handles click events', () => {
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);

    fireEvent.click(screen.getByRole('button'));
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('is disabled when disabled prop is true', () => {
    render(<Button disabled>Click me</Button>);
    expect(screen.getByRole('button')).toBeDisabled();
  });

  it('shows loading state', () => {
    render(<Button loading>Click me</Button>);
    expect(screen.getByRole('button')).toHaveAttribute('aria-busy', 'true');
    expect(screen.getByRole('progressbar')).toBeInTheDocument();
  });

  it('applies variant styles correctly', () => {
    const { rerender } = render(<Button variant="primary">Button</Button>);
    expect(screen.getByRole('button')).toHaveClass('btn-primary');

    rerender(<Button variant="secondary">Button</Button>);
    expect(screen.getByRole('button')).toHaveClass('btn-secondary');
  });
});
```

```typescript
// features/auth/components/LoginForm/LoginForm.test.tsx
import { screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { renderWithProviders } from '@app/__tests__/utils/testUtils';
import { LoginForm } from './LoginForm';
import { vi } from 'vitest';

// Mock API
const mockLogin = vi.fn();
vi.mock('../../api/authApi', () => ({
  login: (data: any) => mockLogin(data),
}));

describe('LoginForm', () => {
  beforeEach(() => {
    mockLogin.mockClear();
  });

  it('validates email format', async () => {
    const user = userEvent.setup();
    renderWithProviders(<LoginForm />);

    const emailInput = screen.getByLabelText(/email/i);
    await user.type(emailInput, 'invalid-email');
    await user.tab(); // Blur to trigger validation

    expect(
      await screen.findByText(/invalid email format/i)
    ).toBeInTheDocument();
  });

  it('submits form with valid data', async () => {
    const user = userEvent.setup();
    mockLogin.mockResolvedValue({ token: 'abc123' });

    renderWithProviders(<LoginForm />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'Password123!');
    await user.click(screen.getByRole('button', { name: /login/i }));

    await waitFor(() => {
      expect(mockLogin).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'Password123!',
      });
    });
  });

  it('shows error message on failed login', async () => {
    const user = userEvent.setup();
    mockLogin.mockRejectedValue({
      response: { data: { message: 'Invalid credentials' } },
    });

    renderWithProviders(<LoginForm />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'wrong');
    await user.click(screen.getByRole('button', { name: /login/i }));

    expect(await screen.findByText(/invalid credentials/i)).toBeInTheDocument();
  });

  it('disables submit button while loading', async () => {
    const user = userEvent.setup();
    mockLogin.mockImplementation(() => new Promise(() => {})); // Never resolves

    renderWithProviders(<LoginForm />);

    await user.type(screen.getByLabelText(/email/i), 'test@example.com');
    await user.type(screen.getByLabelText(/password/i), 'Password123!');

    const submitButton = screen.getByRole('button', { name: /login/i });
    await user.click(submitButton);

    expect(submitButton).toBeDisabled();
  });
});
```

#### **Step 5.4: Playwright E2E Tests**

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',

  // ✅ Timeout settings
  timeout: 30_000,
  expect: {
    timeout: 5_000,
  },

  // ✅ Run tests in parallel
  fullyParallel: true,

  // ✅ Retry on CI
  retries: process.env.CI ? 2 : 0,

  // ✅ Workers
  workers: process.env.CI ? 1 : undefined,

  // ✅ Reporter
  reporter: [
    ['html'],
    ['json', { outputFile: 'test-results.json' }],
    ['junit', { outputFile: 'junit.xml' }],
  ],

  // ✅ Shared settings
  use: {
    baseURL: 'http://localhost:4173',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },

  // ✅ Projects (browsers)
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    {
      name: 'mobile-chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'mobile-safari',
      use: { ...devices['iPhone 12'] },
    },
  ],

  // ✅ Web server
  webServer: {
    command: 'pnpm preview',
    port: 4173,
    reuseExistingServer: !process.env.CI,
  },
});
```

```typescript
// e2e/auth.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Authentication Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/login');
  });

  test('should login successfully', async ({ page }) => {
    // Fill form
    await page.getByLabel(/email/i).fill('test@example.com');
    await page.getByLabel(/password/i).fill('Password123!');

    // Submit
    await page.getByRole('button', { name: /login/i }).click();

    // Verify redirect to dashboard
    await expect(page).toHaveURL('/dashboard');

    // Verify user is logged in
    await expect(page.getByText(/welcome back/i)).toBeVisible();
  });

  test('should show validation errors', async ({ page }) => {
    // Submit without filling
    await page.getByRole('button', { name: /login/i }).click();

    // Verify validation errors
    await expect(page.getByText(/email is required/i)).toBeVisible();
    await expect(page.getByText(/password is required/i)).toBeVisible();
  });

  test('should handle failed login', async ({ page }) => {
    await page.getByLabel(/email/i).fill('wrong@example.com');
    await page.getByLabel(/password/i).fill('wrongpass');
    await page.getByRole('button', { name: /login/i }).click();

    // Verify error message
    await expect(page.getByText(/invalid credentials/i)).toBeVisible();
  });

  test('should remember me', async ({ page, context }) => {
    await page.getByLabel(/email/i).fill('test@example.com');
    await page.getByLabel(/password/i).fill('Password123!');
    await page.getByLabel(/remember me/i).check();
    await page.getByRole('button', { name: /login/i }).click();

    await expect(page).toHaveURL('/dashboard');

    // Close and reopen browser
    await page.close();
    const newPage = await context.newPage();
    await newPage.goto('/');

    // Should still be logged in
    await expect(newPage).toHaveURL('/dashboard');
  });

  test('should logout successfully', async ({ page }) => {
    // Login first
    await page.getByLabel(/email/i).fill('test@example.com');
    await page.getByLabel(/password/i).fill('Password123!');
    await page.getByRole('button', { name: /login/i }).click();
    await expect(page).toHaveURL('/dashboard');

    // Logout
    await page.getByRole('button', { name: /logout/i }).click();

    // Verify redirect to login
    await expect(page).toHaveURL('/login');
  });
});
```

```typescript
// e2e/dashboard.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page }) => {
    // Login before each test
    await page.goto('/login');
    await page.getByLabel(/email/i).fill('test@example.com');
    await page.getByLabel(/password/i).fill('Password123!');
    await page.getByRole('button', { name: /login/i }).click();
    await expect(page).toHaveURL('/dashboard');
  });

  test('should display user stats', async ({ page }) => {
    await expect(page.getByTestId('total-orders')).toBeVisible();
    await expect(page.getByTestId('total-revenue')).toBeVisible();
    await expect(page.getByTestId('active-users')).toBeVisible();
  });

  test('should filter data by date range', async ({ page }) => {
    // Open date picker
    await page.getByRole('button', { name: /select date range/i }).click();

    // Select last 7 days
    await page.getByText(/last 7 days/i).click();

    // Wait for data to update
    await page.waitForResponse(
      (response) =>
        response.url().includes('/api/dashboard') && response.status() === 200
    );

    // Verify data updated
    await expect(page.getByText(/showing data for last 7 days/i)).toBeVisible();
  });

  test('should navigate to different sections', async ({ page }) => {
    // Click on orders tab
    await page.getByRole('tab', { name: /orders/i }).click();
    await expect(page).toHaveURL('/dashboard/orders');

    // Click on analytics tab
    await page.getByRole('tab', { name: /analytics/i }).click();
    await expect(page).toHaveURL('/dashboard/analytics');
  });

  test('should handle loading states', async ({ page }) => {
    // Reload page
    await page.reload();

    // Should show loading spinner
    await expect(page.getByRole('progressbar')).toBeVisible();

    // Wait for data to load
    await expect(page.getByRole('progressbar')).not.toBeVisible();
    await expect(page.getByTestId('dashboard-content')).toBeVisible();
  });
});
```

---

### **GIAI ĐOẠN 6: CI/CD AUTOMATION**

#### **Step 6.1: GitHub Actions - Main Workflow**

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main, develop]

concurrency:
  // concurrency = Đồng thời (Chạy đồng thời - Quản lý nhiều workflow cùng lúc)
  group: ${{ github.workflow }}-${{ github.ref }}
  // group = Nhóm (Nhóm workflow - Cùng workflow và branch)
  // github.workflow = Tên workflow (Tên workflow - ci.yml)
  // github.ref = Tham chiếu (Branch hoặc tag - main, develop, etc.)
  cancel-in-progress: true
  // cancel-in-progress = Hủy đang chạy (Hủy workflow cũ khi có workflow mới - Tránh chạy trùng)

jobs:
  # ===================================
  # JOB 1: SETUP & CACHE
  # ===================================
  setup:
    name: Setup
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Nx affected needs git history

      - name: Setup pnpm
        uses: pnpm/action-setup@v2
        with:
          version: 8

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - name: Install dependencies
        run: pnpm install --frozen-lockfile

      - name: Cache Nx
        uses: actions/cache@v3
        with:
          path: .nx/cache
          key: nx-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}
          restore-keys: nx-${{ runner.os }}-

  # ===================================
  # JOB 2: LINT & TYPE CHECK
  # ===================================
  lint:
    name: Lint & Type Check
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Restore Nx cache
        uses: actions/cache@v3
        with:
          path: .nx/cache
          key: nx-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}

      - name: Run ESLint
        run: pnpm nx affected --target=lint --parallel=3

      - name: Run TypeScript
        run: pnpm nx affected --target=type-check --parallel=3

      - name: Check formatting
        run: pnpm format:check

  # ===================================
  # JOB 3: UNIT TESTS
  # ===================================
  test:
    name: Unit Tests
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Restore Nx cache
        uses: actions/cache@v3
        with:
          path: .nx/cache
          key: nx-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}

      - name: Run tests
        run: pnpm nx affected --target=test --parallel=3 --coverage

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/lcov.info
          flags: unittests
          name: codecov-umbrella

  # ===================================
  # JOB 4: BUILD
  # ===================================
  build:
    name: Build
    needs: [lint, test]
    runs-on: ubuntu-latest
    strategy:
      matrix:
        app: [web, admin]
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Restore Nx cache
        uses: actions/cache@v3
        with:
          path: .nx/cache
          key: nx-${{ runner.os }}-${{ hashFiles('pnpm-lock.yaml') }}

      - name: Build ${{ matrix.app }}
        run: pnpm nx build ${{ matrix.app }} --configuration=production

      - name: Analyze bundle
        run: pnpm nx run ${{ matrix.app }}:analyze

      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: ${{ matrix.app }}-dist
          path: dist/apps/${{ matrix.app }}
          retention-days: 7

      - name: Upload bundle stats
        uses: actions/upload-artifact@v3
        with:
          name: ${{ matrix.app }}-stats
          path: dist/apps/${{ matrix.app }}/stats.html

  # ===================================
  # JOB 5: E2E TESTS
  # ===================================
  e2e:
    name: E2E Tests
    needs: build
    runs-on: ubuntu-latest
    strategy:
      matrix:
        browser: [chromium, firefox, webkit]
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: web-dist
          path: dist/apps/web

      - name: Install Playwright browsers
        run: pnpm playwright install --with-deps ${{ matrix.browser }}

      - name: Run E2E tests
        run: pnpm nx e2e web-e2e --project=${{ matrix.browser }}

      - name: Upload test results
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report-${{ matrix.browser }}
          path: playwright-report/
          retention-days: 7

  # ===================================
  # JOB 6: LIGHTHOUSE
  # ===================================
  lighthouse:
    name: Lighthouse CI
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Download build artifacts
        uses: actions/download-artifact@v3
        with:
          name: web-dist
          path: dist/apps/web

      - name: Run Lighthouse CI
        run: pnpm lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}

  # ===================================
  # JOB 7: SECURITY SCAN
  # ===================================
  security:
    name: Security Scan
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Run npm audit
        run: pnpm audit --audit-level=moderate

      - name: Run Snyk security scan
        uses: snyk/actions/node@master
        env:
          SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
        with:
          args: --severity-threshold=high

      - name: OWASP Dependency Check
        uses: dependency-check/Dependency-Check_Action@main
        with:
          project: 'my-app'
          path: '.'
          format: 'HTML'
```

#### **Step 6.2: Deployment Workflows**

```yaml
# .github/workflows/deploy-staging.yml
name: Deploy to Staging

on:
  push:
    branches: [develop]

jobs:
  deploy:
    name: Deploy to Staging
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.myapp.com

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Build for staging
        run: pnpm nx build web --configuration=staging
        env:
          VITE_API_URL: ${{ secrets.STAGING_API_URL }}
          VITE_SENTRY_DSN: ${{ secrets.SENTRY_DSN }}

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
          working-directory: ./dist/apps/web

      - name: Notify Slack
        if: always()
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: 'Staging deployment ${{ job.status }}'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

```yaml
# .github/workflows/deploy-production.yml
name: Deploy to Production

on:
  push:
    tags:
      - 'v*.*.*'

jobs:
  deploy:
    name: Deploy to Production
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com

    steps:
      - uses: actions/checkout@v4

      - uses: pnpm/action-setup@v2
        with:
          version: 8

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: 'pnpm'

      - run: pnpm install --frozen-lockfile

      - name: Run full test suite
        run: pnpm test

      - name: Build for production
        run: pnpm nx build web --configuration=production
        env:
          VITE_API_URL: ${{ secrets.PROD_API_URL }}
          VITE_SENTRY_DSN: ${{ secrets.SENTRY_DSN }}

      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
          working-directory: ./dist/apps/web

      - name: Create Sentry release
        uses: getsentry/action-release@v1
        env:
          SENTRY_AUTH_TOKEN: ${{ secrets.SENTRY_AUTH_TOKEN }}
          SENTRY_ORG: ${{ secrets.SENTRY_ORG }}
          SENTRY_PROJECT: ${{ secrets.SENTRY_PROJECT }}
        with:
          environment: production
          sourcemaps: './dist/apps/web'

      - name: Notify team
        if: always()
        uses: 8398a7/action-slack@v3
        with:
          status: ${{ job.status }}
          text: 'Production deployment ${{ job.status }}'
          webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

---

### **GIAI ĐOẠN 7: MONITORING & OBSERVABILITY**

#### **Step 7.1: Sentry Error Tracking**

```typescript
// apps/web/src/services/monitoring/sentry.ts
import * as Sentry from '@sentry/react';
import { BrowserTracing } from '@sentry/tracing';
import { useEffect } from 'react';
import {
  createRoutesFromChildren,
  matchRoutes,
  useLocation,
  useNavigationType,
} from 'react-router-dom';

export function initSentry() {
  if (import.meta.env.PROD) {
    Sentry.init({
      dsn: import.meta.env.VITE_SENTRY_DSN,
      environment: import.meta.env.MODE,

      // ✅ Performance monitoring
      integrations: [
        new BrowserTracing({
          routingInstrumentation: Sentry.reactRouterV6Instrumentation(
            useEffect,
            useLocation,
            useNavigationType,
            createRoutesFromChildren,
            matchRoutes
          ),
        }),
      ],

      // ✅ Sample rates
      // Sample rates = Tỷ lệ mẫu (Tỷ lệ gửi dữ liệu - Giảm chi phí)
      tracesSampleRate: 0.1, // 10% của transactions
      // tracesSampleRate = Tỷ lệ mẫu trace (10% transactions - Trace = Theo dõi performance)
      // transactions = Giao dịch (Request, page load, user action)
      replaysSessionSampleRate: 0.1, // 10% sessions
      // replaysSessionSampleRate = Tỷ lệ mẫu replay session (10% sessions - Replay = Ghi lại hành động user)
      // sessions = Phiên (Phiên người dùng - Từ khi mở đến khi đóng)
      replaysOnErrorSampleRate: 1.0, // 100% khi có error
      // replaysOnErrorSampleRate = Tỷ lệ mẫu replay khi lỗi (100% khi có error - Luôn ghi lại khi lỗi)
      // error = Lỗi (Exception, crash)

      // ✅ Filter sensitive data
      beforeSend(event, hint) {
        // Remove sensitive data
        if (event.request) {
          delete event.request.cookies;
          delete event.request.headers?.Authorization;
        }

        // Filter local development errors
        if (event.request?.url?.includes('localhost')) {
          return null;
        }

        return event;
      },

      // ✅ Ignore certain errors
      ignoreErrors: [
        'ResizeObserver loop limit exceeded',
        'Non-Error promise rejection captured',
        /^Network request failed$/,
      ],
    });
  }
}

// ✅ Custom error boundary
export const SentryErrorBoundary = Sentry.ErrorBoundary;

// ✅ Custom hooks
export function useSentryUser(user: User | null) {
  useEffect(() => {
    if (user) {
      Sentry.setUser({
        id: user.id,
        email: user.email,
        username: user.name,
      });
    } else {
      Sentry.setUser(null);
    }
  }, [user]);
}

// ✅ Manual error reporting
export function captureError(error: Error, context?: Record<string, any>) {
  Sentry.captureException(error, {
    extra: context,
  });
}

// ✅ Performance tracking
export function trackPerformance(name: string, duration: number) {
  const transaction = Sentry.startTransaction({
    name,
    op: 'custom',
  });

  transaction.setMeasurement('duration', duration, 'millisecond');
  transaction.finish();
}
```

```typescript
// Usage trong App.tsx
import {
  initSentry,
  SentryErrorBoundary,
} from '@app/services/monitoring/sentry';

// Initialize Sentry
initSentry();

function App() {
  return (
    <SentryErrorBoundary
      fallback={({ error, resetError }) => (
        <ErrorFallback error={error} onReset={resetError} />
      )}
      showDialog
    >
      <AppContent />
    </SentryErrorBoundary>
  );
}
```

#### **Step 7.2: Analytics & User Tracking**

```typescript
// apps/web/src/services/analytics/analytics.ts
import ReactGA from 'react-ga4';
import { useEffect } from 'react';
import { useLocation } from 'react-router-dom';

// ✅ Initialize Google Analytics
export function initAnalytics() {
  if (import.meta.env.PROD && import.meta.env.VITE_GA_MEASUREMENT_ID) {
    ReactGA.initialize(import.meta.env.VITE_GA_MEASUREMENT_ID, {
      gaOptions: {
        siteSpeedSampleRate: 100,
      },
    });
  }
}

// ✅ Track page views
export function usePageTracking() {
  const location = useLocation();

  useEffect(() => {
    if (import.meta.env.PROD) {
      ReactGA.send({
        hitType: 'pageview',
        page: location.pathname + location.search,
        title: document.title,
      });
    }
  }, [location]);
}

// ✅ Track events
export function trackEvent(
  category: string,
  action: string,
  label?: string,
  value?: number
) {
  if (import.meta.env.PROD) {
    ReactGA.event({
      category,
      action,
      label,
      value,
    });
  }
}

// ✅ Track timing
export function trackTiming(
  category: string,
  variable: string,
  value: number,
  label?: string
) {
  if (import.meta.env.PROD) {
    ReactGA.event({
      category,
      action: variable,
      label,
      value,
      nonInteraction: true,
    });
  }
}

// ✅ Custom dimensions
export function setUserProperties(properties: Record<string, any>) {
  if (import.meta.env.PROD) {
    ReactGA.gtag('set', 'user_properties', properties);
  }
}

// ✅ E-commerce tracking
export function trackPurchase(transaction: {
  transactionId: string;
  revenue: number;
  items: Array<{
    id: string;
    name: string;
    price: number;
    quantity: number;
  }>;
}) {
  if (import.meta.env.PROD) {
    ReactGA.gtag('event', 'purchase', {
      transaction_id: transaction.transactionId,
      value: transaction.revenue,
      items: transaction.items,
    });
  }
}
```

```typescript
// Usage examples
import { trackEvent, trackTiming } from '@app/services/analytics/analytics';

function ProductPage() {
  const handleAddToCart = () => {
    // Track user action
    trackEvent('Product', 'Add to Cart', product.name, product.price);
  };

  useEffect(() => {
    const startTime = performance.now();

    // Fetch product data
    fetchProduct().then(() => {
      const loadTime = performance.now() - startTime;

      // Track performance
      trackTiming('Product Page', 'Load Time', loadTime, product.id);
    });
  }, []);

  return <div>...</div>;
}
```

#### **Step 7.3: Performance Monitoring**

```typescript
// apps/web/src/services/monitoring/performance.ts
// monitoring = Giám sát (Theo dõi hiệu suất)
// performance = Hiệu suất (Tốc độ, tài nguyên)
import { onCLS, onFID, onFCP, onLCP, onTTFB } from 'web-vitals';
// web-vitals = Web Vitals (Thư viện đo Web Vitals - Chỉ số hiệu suất web)
// onCLS = On Cumulative Layout Shift (Callback khi CLS thay đổi)
// onFID = On First Input Delay (Callback khi FID thay đổi)
// onFCP = On First Contentful Paint (Callback khi FCP thay đổi)
// onLCP = On Largest Contentful Paint (Callback khi LCP thay đổi)
// onTTFB = On Time to First Byte (Callback khi TTFB thay đổi)
import { trackTiming } from '../analytics/analytics';
// trackTiming = Theo dõi thời gian (Gửi dữ liệu timing đến analytics)

// ✅ Track Web Vitals
// Track = Theo dõi (Ghi lại, gửi dữ liệu)
// Web Vitals = Web Vitals (Chỉ số hiệu suất web quan trọng - CLS, FID, FCP, LCP, TTFB)
export function initPerformanceMonitoring() {
  // initPerformanceMonitoring = Khởi tạo giám sát hiệu suất (Bắt đầu theo dõi performance)
  // Cumulative Layout Shift
  // Cumulative Layout Shift = Dịch chuyển layout tích lũy (CLS - Đo độ ổn định layout)
  // Layout Shift = Dịch chuyển layout (Phần tử di chuyển khi load - Gây khó chịu)
  onCLS((metric) => {
    // metric = Chỉ số (Dữ liệu CLS - { value: số, entries: [...] })
    trackTiming('Web Vitals', 'CLS', metric.value);
    // trackTiming = Theo dõi thời gian (Gửi CLS đến analytics)
    console.log('CLS:', metric.value);
  });

  // First Input Delay
  // First Input Delay = Độ trễ đầu vào đầu tiên (FID - Đo độ phản hồi)
  // Input = Đầu vào (Click, tap, keypress)
  // Delay = Độ trễ (Thời gian từ khi click đến khi browser phản hồi)
  onFID((metric) => {
    trackTiming('Web Vitals', 'FID', metric.value);
    console.log('FID:', metric.value);
  });

  // First Contentful Paint
  // First Contentful Paint = Vẽ nội dung đầu tiên (FCP - Đo thời gian hiển thị nội dung đầu)
  // Contentful = Có nội dung (Có text, image - Không phải background)
  // Paint = Vẽ (Browser vẽ nội dung lên màn hình)
  onFCP((metric) => {
    trackTiming('Web Vitals', 'FCP', metric.value);
    console.log('FCP:', metric.value);
  });

  // Largest Contentful Paint
  // Largest Contentful Paint = Vẽ nội dung lớn nhất (LCP - Đo thời gian hiển thị nội dung lớn nhất)
  // Largest = Lớn nhất (Phần tử lớn nhất trong viewport)
  onLCP((metric) => {
    trackTiming('Web Vitals', 'LCP', metric.value);
    console.log('LCP:', metric.value);
  });

  // Time to First Byte
  // Time to First Byte = Thời gian đến byte đầu tiên (TTFB - Đo thời gian nhận byte đầu từ server)
  // First Byte = Byte đầu tiên (Byte đầu tiên từ server response)
  onTTFB((metric) => {
    trackTiming('Web Vitals', 'TTFB', metric.value);
    console.log('TTFB:', metric.value);
  });
}

// ✅ Custom performance marks
export function measurePerformance(name: string) {
  const startMark = `${name}-start`;
  const endMark = `${name}-end`;
  const measureName = name;

  return {
    start: () => performance.mark(startMark),
    end: () => {
      performance.mark(endMark);
      performance.measure(measureName, startMark, endMark);

      const measure = performance.getEntriesByName(measureName)[0];
      trackTiming('Custom Performance', name, measure.duration);

      // Cleanup
      performance.clearMarks(startMark);
      performance.clearMarks(endMark);
      performance.clearMeasures(measureName);

      return measure.duration;
    },
  };
}

// Usage
const perf = measurePerformance('data-fetch');
perf.start();
await fetchData();
const duration = perf.end();
console.log(`Data fetch took ${duration}ms`);
```

---

### **GIAI ĐOẠN 8: SCALABILITY & ADVANCED PATTERNS**

#### **Step 8.1: Micro-Frontends Architecture (Module Federation)**

// Micro-Frontends = Vi frontend (Kiến trúc chia frontend thành nhiều app độc lập)
// Architecture = Kiến trúc (Cấu trúc hệ thống)
// Module Federation = Liên bang module (Cơ chế chia sẻ code giữa các app - Webpack 5)
// Federation = Liên bang (Kết hợp nhiều app độc lập thành 1 hệ thống)

```typescript
// apps/web/vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import federation from '@originjs/vite-plugin-federation';

export default defineConfig({
  plugins: [
    react(),
    federation({
      name: 'host',
      remotes: {
        // Remote apps
        dashboard: 'http://localhost:4001/assets/remoteEntry.js',
        settings: 'http://localhost:4002/assets/remoteEntry.js',
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true },
        'react-router-dom': { singleton: true },
      },
    }),
  ],
});
```

```typescript
// apps/dashboard/vite.config.ts (Remote app)
export default defineConfig({
  plugins: [
    react(),
    federation({
      name: 'dashboard',
      filename: 'remoteEntry.js',
      exposes: {
        './DashboardApp': './src/App',
        './DashboardRoutes': './src/routes',
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true },
      },
    }),
  ],
  build: {
    target: 'esnext',
  },
});
```

```typescript
// Dynamic import remote modules
import { lazy, Suspense } from 'react';
import { LoadingSpinner } from '@libs/shared/ui';

const DashboardApp = lazy(() => import('dashboard/DashboardApp'));

function App() {
  return (
    <Suspense fallback={<LoadingSpinner />}>
      <DashboardApp />
    </Suspense>
  );
}
```

#### **Step 8.2: Feature Flags System**

// Feature Flags = Cờ tính năng (Bật/tắt tính năng mà không cần deploy lại)
// System = Hệ thống (Hệ thống quản lý feature flags)

```typescript
// libs/shared/utils/src/featureFlags/featureFlags.ts
// featureFlags = Cờ tính năng (File quản lý feature flags)
type FeatureFlag =
  // FeatureFlag = Kiểu cờ tính năng (Danh sách tên feature flags)
  | 'newDashboard'
  // newDashboard = Dashboard mới (Tính năng dashboard mới)
  | 'darkMode'
  // darkMode = Chế độ tối (Tính năng chế độ tối)
  | 'advancedFilters'
  // advancedFilters = Bộ lọc nâng cao (Tính năng bộ lọc nâng cao)
  | 'experimentalFeature';
// experimentalFeature = Tính năng thử nghiệm (Tính năng đang thử nghiệm)

interface FeatureFlagConfig {
  // FeatureFlagConfig = Cấu hình cờ tính năng (Cấu hình cho mỗi feature flag)
  enabled: boolean;
  // enabled = Đã bật (Bật/tắt feature flag)
  rolloutPercentage?: number; // 0-100
  // rolloutPercentage = Tỷ lệ triển khai (0-100 - Triển khai cho % user)
  // rollout = Triển khai (Phát hành tính năng từ từ)
  // percentage = Phần trăm (Tỷ lệ - 0-100%)
  enabledFor?: string[]; // User IDs
  // enabledFor = Bật cho (Danh sách User IDs - Chỉ bật cho user cụ thể)
  // User IDs = ID người dùng (Danh sách ID user được bật tính năng)
}

class FeatureFlagService {
  private flags: Map<FeatureFlag, FeatureFlagConfig> = new Map();

  constructor() {
    this.initializeFlags();
  }

  private initializeFlags() {
    // Load từ remote config hoặc environment
    this.flags.set('newDashboard', {
      enabled: true,
      rolloutPercentage: 50, // Rollout 50% users
    });

    this.flags.set('darkMode', {
      enabled: true,
    });

    this.flags.set('advancedFilters', {
      enabled: true,
      enabledFor: ['admin-user-id'], // Chỉ cho admin
    });
  }

  isEnabled(flag: FeatureFlag, userId?: string): boolean {
    const config = this.flags.get(flag);

    if (!config || !config.enabled) {
      return false;
    }

    // Check user-specific enable
    if (config.enabledFor && userId) {
      return config.enabledFor.includes(userId);
    }

    // Check rollout percentage
    if (config.rolloutPercentage && userId) {
      const hash = this.hashUserId(userId);
      return hash < config.rolloutPercentage;
    }

    return config.enabled;
  }

  private hashUserId(userId: string): number {
    // Simple hash function 0-100
    let hash = 0;
    for (let i = 0; i < userId.length; i++) {
      hash = (hash << 5) - hash + userId.charCodeAt(i);
      hash = hash & hash; // Convert to 32bit integer
    }
    return Math.abs(hash % 100);
  }
}

export const featureFlags = new FeatureFlagService();

// React hook
export function useFeatureFlag(flag: FeatureFlag): boolean {
  const { user } = useAuth();
  return featureFlags.isEnabled(flag, user?.id);
}
```

```typescript
// Usage
function Dashboard() {
  const hasNewDashboard = useFeatureFlag('newDashboard');
  const hasDarkMode = useFeatureFlag('darkMode');

  if (hasNewDashboard) {
    return <NewDashboard />;
  }

  return <OldDashboard />;
}
```

#### **Step 8.3: Documentation với Storybook**

```bash
# Install Storybook
pnpm dlx storybook@latest init
```

```typescript
// .storybook/main.ts
import type { StorybookConfig } from '@storybook/react-vite';

const config: StorybookConfig = {
  stories: [
    '../apps/**/*.stories.@(js|jsx|ts|tsx)',
    '../libs/**/*.stories.@(js|jsx|ts|tsx)',
  ],
  addons: [
    '@storybook/addon-links',
    '@storybook/addon-essentials',
    '@storybook/addon-interactions',
    '@storybook/addon-a11y', // Accessibility testing
  ],
  framework: {
    name: '@storybook/react-vite',
    options: {},
  },
  docs: {
    autodocs: 'tag',
  },
};

export default config;
```

```typescript
// libs/shared/ui/src/Button/Button.stories.tsx
import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'UI/Button',
  component: Button,
  parameters: {
    layout: 'centered',
  },
  tags: ['autodocs'],
  argTypes: {
    variant: {
      control: 'select',
      options: ['primary', 'secondary', 'danger'],
    },
    size: {
      control: 'select',
      options: ['sm', 'md', 'lg'],
    },
    disabled: {
      control: 'boolean',
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Button',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Button',
  },
};

export const Danger: Story = {
  args: {
    variant: 'danger',
    children: 'Delete',
  },
};

export const Loading: Story = {
  args: {
    loading: true,
    children: 'Loading...',
  },
};

export const Disabled: Story = {
  args: {
    disabled: true,
    children: 'Disabled',
  },
};

// Interactive story
export const WithClick: Story = {
  args: {
    children: 'Click me',
  },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const button = canvas.getByRole('button');
    await userEvent.click(button);
  },
};
```

---

## **⚠️ 4. COMMON PITFALLS & SOLUTIONS**

### **❌ Pitfall #1: Không Có TypeScript Strict Mode**

```typescript
// ❌ BAD: Loose types
function fetchUser(id: string) {
  return api.get(`/users/${id}`);
}

const user = await fetchUser('123');
user.name; // No type safety!

// ✅ GOOD: Strict types
interface User {
  id: string;
  name: string;
  email: string;
}

async function fetchUser(id: string): Promise<User> {
  const response = await api.get<User>(`/users/${id}`);
  return response.data;
}

const user = await fetchUser('123');
user.name; // ✅ Type-safe
```

### **❌ Pitfall #2: Monolithic Folder Structure**

```typescript
// ❌ BAD: Flat structure
src/
├── components/  // 100+ components in one folder!
├── utils/       // 50+ utility files
└── hooks/       // 30+ hooks

// ✅ GOOD: Feature-based structure
src/
├── features/
│   ├── auth/
│   │   ├── components/
│   │   ├── hooks/
│   │   └── utils/
│   └── dashboard/
│       ├── components/
│       ├── hooks/
│       └── utils/
└── components/  // Only shared components
```

### **❌ Pitfall #3: Không Test Coverage**

```typescript
// ❌ BAD: No tests
export function calculateTotal(items: CartItem[]) {
  return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}

// ✅ GOOD: Comprehensive tests
describe('calculateTotal', () => {
  it('calculates total for single item', () => {
    expect(calculateTotal([{ price: 10, quantity: 2 }])).toBe(20);
  });

  it('calculates total for multiple items', () => {
    expect(
      calculateTotal([
        { price: 10, quantity: 2 },
        { price: 5, quantity: 3 },
      ])
    ).toBe(35);
  });

  it('returns 0 for empty cart', () => {
    expect(calculateTotal([])).toBe(0);
  });
});
```

### **❌ Pitfall #4: Hardcoded Configuration**

```typescript
// ❌ BAD: Hardcoded
const API_URL = 'https://api.production.com';

// ✅ GOOD: Environment variables
const API_URL = import.meta.env.VITE_API_URL;

// .env.development
// VITE_API_URL=http://localhost:3000

// .env.production
// VITE_API_URL=https://api.production.com
```

### **❌ Pitfall #5: No Performance Monitoring**

```typescript
// ❌ BAD: No monitoring
function DataTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch('/api/data').then((res) => setData(res.data));
  }, []);

  return <Table data={data} />;
}

// ✅ GOOD: Performance tracking
function DataTable() {
  const [data, setData] = useState([]);

  useEffect(() => {
    const perf = measurePerformance('data-fetch');
    perf.start();

    fetch('/api/data').then((res) => {
      setData(res.data);
      const duration = perf.end();

      if (duration > 1000) {
        captureError(new Error('Slow data fetch'), {
          duration,
          endpoint: '/api/data',
        });
      }
    });
  }, []);

  return <Table data={data} />;
}
```

---

## **📊 5. COMPARISON: MONOREPO VS POLYREPO**

| Aspect           | Monorepo (Nx)                                                                                  | Polyrepo                    |
| ---------------- | ---------------------------------------------------------------------------------------------- | --------------------------- |
| **Code Sharing** | ⭐⭐⭐⭐⭐ Easy with libs                                                                      | ⭐⭐ Requires npm packages  |
|                  | // Code Sharing = Chia sẻ code (Monorepo: Dễ với libs - Polyrepo: Cần npm packages)            |
|                  | // libs = Thư viện (Shared libraries - Thư viện dùng chung)                                    |
|                  | // npm packages = Gói npm (Phải publish lên npm để dùng chung)                                 |
| **Consistency**  | ⭐⭐⭐⭐⭐ Enforced standards                                                                  | ⭐⭐ Varies per repo        |
|                  | // Consistency = Nhất quán (Monorepo: Tiêu chuẩn được thực thi - Polyrepo: Khác nhau mỗi repo) |
|                  | // Enforced standards = Tiêu chuẩn được thực thi (ESLint, Prettier chung)                      |
|                  | // Varies per repo = Khác nhau mỗi repo (Mỗi repo có config riêng)                             |
| **Refactoring**  | ⭐⭐⭐⭐⭐ Atomic changes                                                                      | ⭐⭐ Multiple PRs needed    |
|                  | // Refactoring = Tái cấu trúc (Monorepo: Thay đổi nguyên tử - Polyrepo: Cần nhiều PR)          |
|                  | // Atomic changes = Thay đổi nguyên tử (Thay đổi tất cả cùng lúc - 1 commit)                   |
|                  | // Multiple PRs = Nhiều PR (Cần nhiều Pull Request - Mỗi repo 1 PR)                            |
| **CI/CD Speed**  | ⭐⭐⭐⭐⭐ Affected commands                                                                   | ⭐⭐⭐ Build everything     |
|                  | // CI/CD Speed = Tốc độ CI/CD (Monorepo: Chỉ build code thay đổi - Polyrepo: Build tất cả)     |
|                  | // Affected commands = Lệnh ảnh hưởng (Chỉ test/build code thay đổi - Nhanh)                   |
|                  | // Build everything = Build tất cả (Build toàn bộ repo - Chậm)                                 |
| **Onboarding**   | ⭐⭐⭐ Single repo to clone                                                                    | ⭐⭐ Multiple repos         |
|                  | // Onboarding = Đưa vào (Monorepo: 1 repo clone - Polyrepo: Nhiều repo)                        |
|                  | // Single repo = 1 repo (Chỉ cần clone 1 repo)                                                 |
|                  | // Multiple repos = Nhiều repo (Phải clone nhiều repo)                                         |
| **Team Scale**   | ⭐⭐⭐⭐⭐ 50+ developers                                                                      | ⭐⭐⭐ Best for small teams |
|                  | // Team Scale = Quy mô team (Monorepo: 50+ dev - Polyrepo: Tốt cho team nhỏ)                   |
|                  | // developers = Lập trình viên (Số lượng dev trong team)                                       |
|                  | // small teams = Team nhỏ (Team ít người)                                                      |
| **Dependencies** | ⭐⭐⭐⭐ Centralized                                                                           | ⭐⭐ Can drift              |
|                  | // Dependencies = Phụ thuộc (Monorepo: Tập trung - Polyrepo: Có thể lệch)                      |
|                  | // Centralized = Tập trung (Tất cả dùng cùng version - Dễ quản lý)                             |
|                  | // Can drift = Có thể lệch (Mỗi repo có thể dùng version khác - Khó quản lý)                   |
|                  | // drift = Lệch (Version khác nhau giữa các repo)                                              |

**Recommendation:**

- **Monorepo (Nx)**: Multi-app projects, shared libraries, large teams
- **Polyrepo**: Independent services, different tech stacks

---

## **🏢 6. REAL-WORLD SCENARIO: Banking Dashboard**

### **Project Context**

- **Scale**: 2M+ users, 50+ developers
- **Apps**: Customer portal, Admin dashboard, Mobile app
- **Shared**: UI library, API client, Utils, Types
- **Tech**: React, TypeScript, Vite, Nx, Playwright

### **Implementation Journey**

**Week 1-2: Foundation**

```bash
# Setup Nx monorepo
npx create-nx-workspace banking-app --preset=react-monorepo

# Generate apps
nx g @nx/react:app customer-portal
nx g @nx/react:app admin-dashboard

# Generate shared libraries
nx g @nx/react:lib shared-ui
nx g @nx/react:lib shared-utils
nx g @nx/react:lib shared-api
```

**Week 3-4: Architecture**

- Feature-based folder structure
- Path aliases setup
- Shared component library (50+ components)
- API client with interceptors
- State management (React Query + Zustand)

**Week 5-6: Code Quality**

- ESLint + Prettier + Husky
- TypeScript strict mode
- Zod validation schemas
- Danger.js code review automation
- **Result**: 90% fewer bugs in code review

**Week 7-8: Performance**

- Vite build optimization
- Code splitting strategy
- Lazy loading routes
- Bundle analysis
- **Result**: Build time 3s → 0.8s, Bundle size reduced 40%

**Week 9-10: Testing**

- Vitest setup (85% coverage)
- React Testing Library
- Playwright E2E (100+ scenarios)
- **Result**: Caught 150+ bugs before production

**Week 11-12: CI/CD**

- GitHub Actions workflows
- Affected commands (only test/build changed code)
- Auto deployment to staging/production
- **Result**: Deploy 20 times/day, 5min pipeline

**Week 13-14: Monitoring**

- Sentry error tracking
- Google Analytics
- Web Vitals monitoring
- **Result**: 99.9% uptime, MTTR < 10min

**Final Metrics:**

- **Development Speed**: 70% faster (shared libraries, no duplication)
- **Bug Rate**: 90% reduction (strict TypeScript, testing, code review)
- **Build Time**: 3s → 0.8s (Vite, caching)
- **Bundle Size**: 2MB → 800KB (code splitting, tree-shaking)
- **Test Coverage**: 85% (comprehensive testing strategy)
- **Deployment**: 20 times/day (CI/CD automation)
- **Team Satisfaction**: 9/10 (tooling, DX improvements)

---

## **⚡ 7. OPTIMIZATION STRATEGIES**

### **Build Optimization**

// Build Optimization = Tối ưu build (Tối ưu quá trình build - Nhanh hơn, nhỏ hơn)

```typescript
// ✅ 1. SWC instead of Babel (20x faster)
// SWC instead of Babel = SWC thay vì Babel (Nhanh hơn 20x)
// instead of = Thay vì (Dùng SWC thay vì Babel)
// vite.config.ts
plugins: [react({ jsxRuntime: 'automatic', jsxImportSource: '@emotion/react' })]
// jsxRuntime = JSX runtime (automatic = Tự động - Không cần import React)
// jsxImportSource = Nguồn import JSX (@emotion/react = Dùng Emotion cho CSS-in-JS)

// ✅ 2. Dependency pre-bundling
// Dependency pre-bundling = Đóng gói phụ thuộc trước (Đóng gói dependencies trước - Tăng tốc dev)
// pre-bundling = Đóng gói trước (Đóng gói dependencies trước khi chạy)
optimizeDeps: {
  // optimizeDeps = Tối ưu phụ thuộc (Cấu hình tối ưu dependencies)
  include: ['react', 'react-dom', 'react-router-dom'],
  // include = Bao gồm (Bao gồm các package cần pre-bundle)
}

// ✅ 3. Code splitting per route
// Code splitting per route = Chia tách code theo route (Chia code theo trang - Tải nhanh hơn)
const Dashboard = lazy(() => import('./pages/Dashboard'));
// lazy = Lười (React.lazy - Tải component khi cần)
// import = Nhập (Dynamic import - Nhập động)

// ✅ 4. Analyze bundle
// Analyze bundle = Phân tích bundle (Xem bundle có gì, kích thước bao nhiêu)
pnpm vite-bundle-visualizer
// vite-bundle-visualizer = Trình trực quan hóa bundle Vite (Tool xem bundle - HTML report)
// visualizer = Trình trực quan hóa (Tool hiển thị bundle dạng đồ thị)
```

### **Runtime Optimization**

// Runtime Optimization = Tối ưu runtime (Tối ưu khi chạy - Tăng tốc độ render)

```typescript
// ✅ 1. React.memo for expensive components
// React.memo = React memo (Memoization - Chỉ re-render khi props thay đổi)
// expensive components = Component đắt (Component render nặng - Tốn nhiều tài nguyên)
const ExpensiveComponent = React.memo(({ data }) => {
  // memo = Memoization (Ghi nhớ - Chỉ re-render khi props thay đổi)
  return <div>{/* Heavy render logic */}</div>;
  // Heavy render logic = Logic render nặng (Logic render phức tạp, tốn thời gian)
});

// ✅ 2. useMemo for expensive calculations
// useMemo = useMemo hook (Memoization cho giá trị - Chỉ tính lại khi dependencies thay đổi)
// expensive calculations = Tính toán đắt (Tính toán phức tạp, tốn thời gian)
const sortedData = useMemo(() => {
  // useMemo = useMemo hook (Ghi nhớ kết quả tính toán)
  return data.sort((a, b) => a.value - b.value);
  // sort = Sắp xếp (Sắp xếp mảng - Tốn thời gian với mảng lớn)
}, [data]);
// [data] = Dependencies (Chỉ tính lại khi data thay đổi)

// ✅ 3. Virtual scrolling for large lists
// Virtual scrolling = Cuộn ảo (Chỉ render phần tử visible - Tối ưu cho danh sách lớn)
// large lists = Danh sách lớn (Danh sách nhiều phần tử - 1000+ items)
import { FixedSizeList } from 'react-window';
// react-window = react-window (Thư viện virtual scrolling - Chỉ render phần tử visible)
// FixedSizeList = Danh sách kích thước cố định (List với item size cố định)

function LargeList({ items }) {
  return (
    <FixedSizeList height={600} itemCount={items.length} itemSize={50}>
      // height = Chiều cao (Chiều cao danh sách - 600px) // itemCount = Số phần
      tử (Tổng số items - items.length) // itemSize = Kích thước phần tử (Chiều
      cao mỗi item - 50px)
      {({ index, style }) => <div style={style}>{items[index]}</div>}
      // index = Chỉ mục (Chỉ mục phần tử hiện tại) // style = Style (Style từ
      react-window - Position absolute để virtual scroll)
    </FixedSizeList>
  );
}

// ✅ 4. Image optimization
// Image optimization = Tối ưu hình ảnh (Tối ưu tải hình ảnh - Lazy load, async decode)
<img src="/image.jpg" loading="lazy" decoding="async" alt="..." />;
// loading="lazy" = Tải lười (Lazy load - Chỉ tải khi vào viewport)
// lazy = Lười (Tải khi cần - Không tải ngay)
// decoding="async" = Giải mã bất đồng bộ (Decode ảnh bất đồng bộ - Không block render)
// async = Bất đồng bộ (Không chờ - Chạy song song)
// alt = Alternative text (Văn bản thay thế - Accessibility)
```

### **Network Optimization**

// Network Optimization = Tối ưu mạng (Tối ưu request - Giảm số request, tăng tốc độ)

```typescript
// ✅ 1. React Query stale-while-revalidate
// React Query = React Query (Thư viện quản lý server state - Cache, sync, etc.)
// stale-while-revalidate = Cũ trong khi tái xác thực (Hiển thị data cũ, fetch data mới ngầm)
// stale = Cũ (Data đã cũ - Hết hạn)
// revalidate = Tái xác thực (Kiểm tra lại, fetch data mới)
const { data } = useQuery({
  // useQuery = useQuery hook (Hook fetch data với cache)
  queryKey: ['users'],
  // queryKey = Khóa truy vấn (Key để cache - ['users'] = Cache key)
  queryFn: fetchUsers,
  // queryFn = Hàm truy vấn (Function fetch data - fetchUsers)
  staleTime: 5 * 60 * 1000, // 5 minutes
  // staleTime = Thời gian cũ (5 phút - Data còn mới trong 5 phút)
  // 5 * 60 * 1000 = 5 phút (5 phút * 60 giây * 1000 milliseconds)
  cacheTime: 10 * 60 * 1000, // 10 minutes
  // cacheTime = Thời gian cache (10 phút - Giữ cache 10 phút sau khi không dùng)
  // cache = Cache (Lưu trữ tạm - Giữ data trong bộ nhớ)
});

// ✅ 2. Prefetch on hover
// Prefetch = Tải trước (Tải data trước khi cần - Tăng tốc độ)
// on hover = Khi di chuột (Khi user di chuột vào link)
<Link
  to="/dashboard"
  // Link = Link (React Router Link - Điều hướng)
  onMouseEnter={() =>
    // onMouseEnter = Khi di chuột vào (Event khi mouse vào element)
    queryClient.prefetchQuery({
      // queryClient = Query client (Client quản lý queries)
      // prefetchQuery = Tải trước query (Tải data trước khi cần)
      queryKey: ['dashboard'],
      queryFn: fetchDashboard,
    })
  }
>
  Dashboard
</Link>;

// ✅ 3. Parallel requests
// Parallel requests = Request song song (Gửi nhiều request cùng lúc - Nhanh hơn tuần tự)
// parallel = Song song (Đồng thời - Không chờ nhau)
const [users, posts, comments] = await Promise.all([
  // Promise.all = Promise tất cả (Chờ tất cả promises hoàn thành - Song song)
  // await = Đợi (Đợi promise hoàn thành)
  fetchUsers(),
  // fetchUsers = Lấy users (Function fetch danh sách users)
  fetchPosts(),
  // fetchPosts = Lấy posts (Function fetch danh sách posts)
  fetchComments(),
  // fetchComments = Lấy comments (Function fetch danh sách comments)
]);
// Promise.all = Chạy song song (Tất cả requests chạy cùng lúc - Nhanh hơn tuần tự)
// Tuần tự = Sequential (Chạy lần lượt - Chậm hơn)
```

---

## **📝 8. KEY TAKEAWAYS**

### **🎯 Essential Checklist**

```markdown
## ✅ PRODUCTION-READY CHECKLIST

### Foundation

// Foundation = Nền tảng (Cơ sở - Setup ban đầu)

- [ ] TypeScript strict mode enabled
      // TypeScript strict mode = Chế độ nghiêm ngặt TypeScript (Bật tất cả strict checks)
      // enabled = Đã bật (Đã kích hoạt)
- [ ] ESLint + Prettier configured
      // ESLint = ESLint (Linter - Kiểm tra lỗi code)
      // Prettier = Prettier (Formatter - Sắp xếp code đẹp)
      // configured = Đã cấu hình (Đã setup)
- [ ] Git hooks (Husky + lint-staged)
      // Git hooks = Móc Git (Script tự động chạy khi có sự kiện Git)
      // Husky = Husky (Framework Git hooks)
      // lint-staged = Lint đã stage (Chạy linters trên file đã stage)
- [ ] Commit conventions enforced
      // Commit conventions = Quy ước commit (Chuẩn commit message - feat:, fix:, etc.)
      // enforced = Được thực thi (Bắt buộc phải theo)
- [ ] Path aliases configured
      // Path aliases = Bí danh đường dẫn (@app, @libs - Import ngắn gọn)
      // configured = Đã cấu hình (Đã setup trong tsconfig)

### Architecture

// Architecture = Kiến trúc (Cấu trúc code, tổ chức project)

- [ ] Feature-based folder structure
      // Feature-based = Dựa trên tính năng (Tổ chức code theo tính năng - auth/, dashboard/)
      // folder structure = Cấu trúc thư mục (Cách tổ chức folders)
- [ ] Shared libraries created
      // Shared libraries = Thư viện dùng chung (Libraries dùng chung giữa các app)
      // created = Đã tạo (Đã tạo shared libs)
- [ ] State management strategy defined
      // State management = Quản lý state (Cách quản lý state - Zustand, Redux, React Query)
      // strategy = Chiến lược (Kế hoạch, cách làm)
      // defined = Đã định nghĩa (Đã quyết định dùng gì)
- [ ] API client with interceptors
      // API client = Client API (Client gọi API - Axios, Fetch)
      // interceptors = Bộ chặn (Request/Response interceptors - Thêm token, xử lý lỗi)
      // interceptors = Chặn request/response (Thêm header, xử lý lỗi tự động)
- [ ] Error boundaries implemented
      // Error boundaries = Ranh giới lỗi (React component bắt lỗi - Ngăn app crash)
      // implemented = Đã triển khai (Đã code error boundaries)

### Code Quality

// Code Quality = Chất lượng code (Đảm bảo code tốt, dễ đọc, dễ maintain)

- [ ] Automated code review (Danger.js)
      // Automated = Tự động (Tự động kiểm tra - Không cần người)
      // code review = Review code (Kiểm tra code trước khi merge)
      // Danger.js = Danger.js (Tool tự động review PR - Kiểm tra PR size, tests, etc.)
- [ ] Type safety enforced (Zod schemas)
      // Type safety = An toàn kiểu (Đảm bảo kiểu dữ liệu đúng)
      // enforced = Được thực thi (Bắt buộc)
      // Zod schemas = Schema Zod (Zod validation schemas - Validate data)
      // Zod = Zod (Thư viện validation TypeScript-first)
- [ ] Code formatting automated
      // Code formatting = Định dạng code (Sắp xếp code đẹp - Prettier)
      // automated = Tự động (Tự động format khi commit)
- [ ] Import sorting configured
      // Import sorting = Sắp xếp import (Tự động sắp xếp imports - simple-import-sort)
      // configured = Đã cấu hình (Đã setup)
- [ ] Unused code detected
      // Unused code = Code không dùng (Code không được sử dụng)
      // detected = Phát hiện (Tool phát hiện unused code - ESLint, TypeScript)

### Performance

// Performance = Hiệu suất (Tốc độ, tài nguyên)

- [ ] Build optimization (Vite/SWC)
      // Build optimization = Tối ưu build (Tối ưu quá trình build - Vite, SWC)
      // Vite = Vite (Build tool nhanh)
      // SWC = SWC (Compiler nhanh - Thay thế Babel)
- [ ] Code splitting per route
      // Code splitting = Chia tách code (Chia code thành nhiều file - Tải nhanh hơn)
      // per route = Theo route (Chia code theo trang)
- [ ] Lazy loading implemented
      // Lazy loading = Tải chậm (Tải code khi cần - React.lazy)
      // implemented = Đã triển khai (Đã code lazy loading)
- [ ] Bundle analysis setup
      // Bundle analysis = Phân tích bundle (Xem bundle có gì, kích thước bao nhiêu)
      // setup = Đã setup (Đã cấu hình bundle analyzer)
- [ ] Performance budgets defined
      // Performance budgets = Ngân sách hiệu suất (Giới hạn kích thước bundle, thời gian load)
      // budgets = Ngân sách (Giới hạn - Ví dụ: Bundle < 500KB, LCP < 2.5s)
      // defined = Đã định nghĩa (Đã set performance budgets)

### Testing

// Testing = Kiểm thử (Test code - Đảm bảo code đúng)

- [ ] Unit tests (80%+ coverage)
      // Unit tests = Kiểm thử đơn vị (Test từng function/component riêng lẻ)
      // coverage = Độ phủ (Tỷ lệ code được test - 80%+ = Ít nhất 80%)
- [ ] Integration tests
      // Integration tests = Kiểm thử tích hợp (Test nhiều component/service cùng lúc)
      // integration = Tích hợp (Kết hợp nhiều phần)
- [ ] E2E tests (critical paths)
      // E2E tests = Kiểm thử end-to-end (Test toàn bộ flow - User click → API → Database)
      // E2E = End-to-End (Từ đầu đến cuối - Toàn bộ flow)
      // critical paths = Đường dẫn quan trọng (Flow quan trọng - Login, checkout, etc.)
- [ ] Visual regression tests
      // Visual regression tests = Kiểm thử hồi quy trực quan (Test UI không thay đổi)
      // visual = Trực quan (Giao diện, UI)
      // regression = Hồi quy (Thay đổi không mong muốn - UI bị vỡ)
- [ ] Accessibility tests
      // Accessibility tests = Kiểm thử khả năng truy cập (Test a11y - Screen reader, keyboard)
      // accessibility = Khả năng truy cập (a11y - Người khuyết tật có thể dùng)

### CI/CD

// CI/CD = Continuous Integration/Continuous Deployment (Tích hợp/Triển khai liên tục)

- [ ] GitHub Actions workflows
      // GitHub Actions = GitHub Actions (CI/CD platform của GitHub)
      // workflows = Quy trình làm việc (File .yml định nghĩa CI/CD pipeline)
- [ ] Affected commands configured
      // Affected commands = Lệnh ảnh hưởng (Chỉ test/build code thay đổi - Nx affected)
      // configured = Đã cấu hình (Đã setup affected commands)
- [ ] Auto deployment setup
      // Auto deployment = Triển khai tự động (Tự động deploy khi merge PR)
      // deployment = Triển khai (Deploy code lên server)
      // setup = Đã setup (Đã cấu hình auto deployment)
- [ ] Environment management
      // Environment management = Quản lý môi trường (Quản lý dev, staging, production)
      // environment = Môi trường (dev, staging, production)
      // management = Quản lý (Cách quản lý env vars, configs)
- [ ] Secret management
      // Secret management = Quản lý bí mật (Quản lý API keys, tokens - GitHub Secrets)
      // secret = Bí mật (API keys, tokens, passwords)
      // management = Quản lý (Cách lưu trữ, sử dụng secrets an toàn)

### Monitoring

// Monitoring = Giám sát (Theo dõi app trong production)

- [ ] Error tracking (Sentry)
      // Error tracking = Theo dõi lỗi (Ghi lại lỗi trong production - Sentry)
      // Sentry = Sentry (Error tracking service - Ghi lại lỗi, stack trace)
- [ ] Analytics (Google Analytics)
      // Analytics = Phân tích (Theo dõi user behavior - Google Analytics)
      // Google Analytics = Google Analytics (Tool phân tích user behavior)
- [ ] Performance monitoring (Web Vitals)
      // Performance monitoring = Giám sát hiệu suất (Theo dõi performance - Web Vitals)
      // Web Vitals = Web Vitals (Chỉ số hiệu suất web - CLS, FID, FCP, LCP, TTFB)
- [ ] Logging strategy
      // Logging strategy = Chiến lược ghi log (Cách ghi log - Winston, Pino)
      // logging = Ghi log (Ghi lại events, errors, info)
      // strategy = Chiến lược (Kế hoạch, cách làm)
- [ ] Alerts configured
      // Alerts = Cảnh báo (Thông báo khi có vấn đề - Email, Slack)
      // configured = Đã cấu hình (Đã setup alerts)

### Documentation

// Documentation = Tài liệu (Hướng dẫn, mô tả)

- [ ] README comprehensive
      // README = README (File hướng dẫn project - Setup, usage)
      // comprehensive = Toàn diện (Đầy đủ, chi tiết)
- [ ] Storybook for components
      // Storybook = Storybook (Tool xem components - Component documentation)
      // components = Components (React components)
- [ ] API documentation
      // API documentation = Tài liệu API (Mô tả API endpoints - Swagger, OpenAPI)
      // API = API (Application Programming Interface - Giao diện lập trình)
- [ ] Architecture diagrams
      // Architecture diagrams = Sơ đồ kiến trúc (Vẽ cấu trúc hệ thống - Mermaid, Draw.io)
      // diagrams = Sơ đồ (Hình vẽ mô tả)
- [ ] Onboarding guide
      // Onboarding guide = Hướng dẫn đưa vào (Hướng dẫn dev mới - Setup, workflow)
      // onboarding = Đưa vào (Quá trình dev mới bắt đầu làm việc)

### Scalability

// Scalability = Khả năng mở rộng (Có thể mở rộng khi cần - Thêm dev, thêm tính năng)

- [ ] Micro-frontends ready
      // Micro-frontends = Vi frontend (Kiến trúc chia frontend thành nhiều app độc lập)
      // ready = Sẵn sàng (Có thể chuyển sang micro-frontends khi cần)
- [ ] Feature flags system
      // Feature flags = Cờ tính năng (Bật/tắt tính năng mà không cần deploy lại)
      // system = Hệ thống (Hệ thống quản lý feature flags)
- [ ] A/B testing capability
      // A/B testing = Kiểm thử A/B (Test 2 phiên bản - Xem phiên bản nào tốt hơn)
      // capability = Khả năng (Có thể làm A/B testing)
- [ ] Multi-tenancy support
      // Multi-tenancy = Đa thuê (Hỗ trợ nhiều tenant - Nhiều khách hàng dùng chung app)
      // tenancy = Thuê (Tenant = Khách hàng thuê app)
      // support = Hỗ trợ (Có thể hỗ trợ multi-tenancy)
- [ ] Internationalization (i18n)
      // Internationalization = Quốc tế hóa (Hỗ trợ nhiều ngôn ngữ - i18n)
      // i18n = Internationalization (i + 18 chữ cái + n = i18n)
      // Hỗ trợ nhiều ngôn ngữ (Tiếng Việt, Tiếng Anh, etc.)
```

### **💡 Core Principles**

// Core Principles = Nguyên tắc cốt lõi (Nguyên tắc quan trọng nhất)

1. **Start with solid foundation** - TypeScript strict, proper tooling
   // Start with solid foundation = Bắt đầu với nền tảng vững chắc (TypeScript strict, tooling đúng)
   // solid = Vững chắc (Tốt, mạnh)
   // foundation = Nền tảng (Cơ sở - TypeScript, ESLint, Prettier)
   // proper tooling = Tooling đúng (Công cụ phù hợp - ESLint, Prettier, Husky)
2. **Automate everything** - Linting, testing, deployment
   // Automate everything = Tự động hóa mọi thứ (Linting, testing, deployment tự động)
   // automate = Tự động hóa (Không cần làm thủ công)
   // linting = Linting (Kiểm tra code tự động)
   // deployment = Triển khai (Deploy tự động)
3. **Measure performance** - Lighthouse CI, Web Vitals
   // Measure performance = Đo hiệu suất (Lighthouse CI, Web Vitals)
   // measure = Đo (Đo lường, đánh giá)
   // Lighthouse CI = Lighthouse CI (Tool đo performance tự động trong CI)
   // Web Vitals = Web Vitals (Chỉ số hiệu suất web)
4. **Test comprehensively** - Unit, integration, E2E
   // Test comprehensively = Kiểm thử toàn diện (Unit, integration, E2E)
   // comprehensively = Toàn diện (Đầy đủ, nhiều loại test)
5. **Monitor in production** - Sentry, analytics, metrics
   // Monitor in production = Giám sát trong production (Sentry, analytics, metrics)
   // production = Production (Môi trường production - App đang chạy thật)
   // metrics = Chỉ số (Số liệu - Performance, errors, users)
6. **Document thoroughly** - README, Storybook, diagrams
   // Document thoroughly = Tài liệu kỹ lưỡng (README, Storybook, diagrams)
   // thoroughly = Kỹ lưỡng (Đầy đủ, chi tiết)
7. **Scale thoughtfully** - Monorepo, shared libraries, feature flags
   // Scale thoughtfully = Mở rộng có suy nghĩ (Monorepo, shared libraries, feature flags)
   // thoughtfully = Có suy nghĩ (Cẩn thận, có kế hoạch)
8. **Iterate continuously** - Regular audits, refactoring, updates
   // Iterate continuously = Lặp lại liên tục (Regular audits, refactoring, updates)
   // iterate = Lặp lại (Làm đi làm lại, cải thiện)
   // continuously = Liên tục (Không ngừng)
   // audits = Kiểm toán (Kiểm tra định kỳ - Code review, performance audit)
   // refactoring = Tái cấu trúc (Sửa code để cải thiện cấu trúc)
   // updates = Cập nhật (Cập nhật dependencies, tools)

### **🚀 Final Wisdom**

// Final Wisdom = Trí tuệ cuối cùng (Lời khuyên cuối cùng, quan trọng nhất)

**"Tốt nhất là xây dựng từ đầu đúng cách, không phải refactor sau. Investment vào tooling, testing, và monitoring ngày đầu sẽ trả về gấp 10 lần về sau."**
// Investment = Đầu tư (Đầu tư thời gian, công sức)
// tooling = Công cụ (ESLint, Prettier, Husky, etc.)
// testing = Kiểm thử (Unit tests, E2E tests)
// monitoring = Giám sát (Sentry, analytics)
// trả về = Return (Lợi ích nhận được - Gấp 10 lần)

**Success Metrics:**
// Success Metrics = Chỉ số thành công (Cách đánh giá project thành công)

- **Developer Experience**: How fast can new dev be productive?
  // Developer Experience = Trải nghiệm lập trình viên (Dev mới có thể làm việc nhanh như thế nào?)
  // productive = Năng suất (Có thể làm việc hiệu quả)
- **Code Quality**: How many bugs reach production?
  // Code Quality = Chất lượng code (Bao nhiêu lỗi đến production?)
  // bugs = Lỗi (Bugs - Lỗi code)
  // reach production = Đến production (Lỗi xuất hiện trong production)
- **Performance**: How fast is the app?
  // Performance = Hiệu suất (App nhanh như thế nào?)
  // fast = Nhanh (Tốc độ - Load time, render time)
- **Reliability**: How often does it break?
  // Reliability = Độ tin cậy (App bị lỗi thường xuyên như thế nào?)
  // break = Bị lỗi (Crash, error - App không hoạt động)
- **Maintainability**: How easy to change?
  // Maintainability = Khả năng bảo trì (Dễ thay đổi như thế nào?)
  // maintain = Bảo trì (Sửa, cập nhật code)
  // change = Thay đổi (Thêm tính năng, sửa lỗi)

**Remember:** Production-ready ≠ Perfect. Ship fast, iterate, improve continuously! 🚀
// Remember = Nhớ (Lưu ý)
// Production-ready = Sẵn sàng production (Đủ tốt để deploy - Không phải hoàn hảo)
// Perfect = Hoàn hảo (100% - Không cần thiết)
// Ship fast = Ship nhanh (Deploy nhanh - Không chờ hoàn hảo)
// iterate = Lặp lại (Làm đi làm lại, cải thiện)
// improve = Cải thiện (Làm tốt hơn)
// continuously = Liên tục (Không ngừng)

---

## **📊 9. PHÂN TÍCH & ĐỀ XUẤT BỔ SUNG**

### **🔍 Đánh Giá Tổng Quan**

File Q62 hiện tại đã cover **8 giai đoạn chính** từ Foundation đến Scalability với code examples chi tiết. Tuy nhiên, để đạt mức **Production-Ready hoàn chỉnh**, còn thiếu một số phần quan trọng:

### **🔴 CRITICAL - Cần Bổ Sung Ngay**

#### **1. Error Handling Strategy (Global Error Handling)**

**Hiện trạng:**

- ✅ Có ErrorBoundary trong folder structure (dòng 601)
- ✅ Có SentryErrorBoundary trong Step 7.1 (dòng 2357)
- ❌ **THIẾU**: Global error handling strategy chi tiết
- ❌ **THIẾU**: API error handling patterns
- ❌ **THIẾU**: Unhandled promise rejection handling
- ❌ **THIẾU**: Network error recovery strategies

**Cần bổ sung:**

```typescript
// apps/web/src/services/error/globalErrorHandler.ts
// - Window error event listener
// - Unhandled promise rejection handler
// - API error interceptor với retry logic
// - Error classification (NetworkError, ValidationError, ServerError)
// - Error recovery strategies (retry, fallback, graceful degradation)
```

**Vị trí đề xuất:** Thêm sau **Step 7.1: Sentry Error Tracking** (sau dòng 2412)

---

#### **2. Environment Variables Management (Chi Tiết)**

**Hiện trạng:**

- ✅ Có đề cập trong Pitfall #4 (dòng 2970-2983)
- ✅ Có trong CI/CD workflows (dòng 2199, 2257)
- ❌ **THIẾT**: Type-safe environment variables
- ❌ **THIẾU**: Environment validation với Zod
- ❌ **THIẾU**: Multi-environment configuration strategy
- ❌ **THIẾU**: Secret management best practices

**Cần bổ sung:**

```typescript
// apps/web/src/config/env.ts
// - Zod schema cho environment variables
// - Type-safe env access
// - Validation on app startup
// - Default values cho development
// - Error messages rõ ràng khi thiếu env vars
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 1: FOUNDATION** sau Step 1.6 (sau dòng 523)

---

#### **3. Internationalization (i18n) Setup**

**Hiện trạng:**

- ❌ **THIẾU HOÀN TOÀN**: Không có i18n setup
- ❌ **THIẾU**: react-i18next configuration
- ❌ **THIẾU**: Translation file structure
- ❌ **THIẾU**: RTL support
- ❌ **THIẾU**: Date/number/currency formatting với locale

**Cần bổ sung:**

```typescript
// libs/shared/i18n/
// - i18n configuration
// - Translation files structure (en, vi, ja...)
// - Language detection
// - Lazy loading translations
// - RTL support setup
// - Integration với date/number formatting
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 2: ARCHITECTURE** sau Step 2.3 (sau dòng 774)

---

#### **4. Progressive Web App (PWA) Implementation Chi Tiết**

**Hiện trạng:**

- ✅ Có VitePWA plugin trong vite.config.ts (dòng 1104-1125)
- ❌ **THIẾU**: Service Worker strategy chi tiết
- ❌ **THIẾU**: Offline fallback strategies
- ❌ **THIẾU**: Background sync implementation
- ❌ **THIẾU**: Push notifications setup
- ❌ **THIẾU**: Update notification UI

**Cần bổ sung:**

```typescript
// apps/web/src/services/pwa/
// - Service Worker registration
// - Cache strategies (NetworkFirst, CacheFirst, StaleWhileRevalidate)
// - Offline fallback pages
// - Background sync cho failed requests
// - Push notification setup
// - Update prompt component
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 4: PERFORMANCE** sau Step 4.3 (sau dòng 1345)

---

#### **5. SEO Optimization Strategy**

**Hiện trạng:**

- ✅ Có Lighthouse CI với SEO checks (dòng 1298-1299)
- ❌ **THIẾU**: Meta tags management
- ❌ **THIẾU**: Open Graph tags
- ❌ **THIẾU**: Structured data (JSON-LD)
- ❌ **THIẾU**: Sitemap generation
- ❌ **THIẾU**: robots.txt configuration

**Cần bổ sung:**

```typescript
// apps/web/src/services/seo/
// - Meta tags component với TypeScript
// - Open Graph generator
// - JSON-LD structured data
// - Dynamic sitemap generation
// - robots.txt với environment-based rules
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 4: PERFORMANCE** sau PWA section

---

### **🟡 IMPORTANT - Nên Bổ Sung**

#### **6. Security Best Practices (Chi Tiết Hơn)**

**Hiện trạng:**

- ✅ Có security scan trong CI/CD (dòng 2128-2161)
- ✅ Có Sentry security filters (dòng 2331-2343)
- ❌ **THIẾU**: Content Security Policy (CSP) setup
- ❌ **THIẾU**: XSS prevention patterns
- ❌ **THIẾU**: CSRF token handling
- ❌ **THIẾU**: Secure cookie configuration

**Cần bổ sung:**

```typescript
// apps/web/src/services/security/
// - CSP headers configuration
// - XSS sanitization utilities
// - CSRF token management
// - Secure cookie settings
// - Security headers middleware
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 3: CODE QUALITY** sau Step 3.3 (sau dòng 1064)

---

#### **7. Accessibility (a11y) Implementation**

**Hiện trạng:**

- ✅ Có jsx-a11y trong ESLint (dòng 185)
- ✅ Có Lighthouse a11y check (dòng 1293)
- ❌ **THIẾU**: Accessibility testing setup
- ❌ **THIẾU**: Keyboard navigation patterns
- ❌ **THIẾU**: Screen reader testing
- ❌ **THIẾU**: Focus management utilities

**Cần bổ sung:**

```typescript
// libs/shared/ui/src/a11y/
// - Focus trap component
// - Skip links component
// - ARIA utilities
// - Keyboard navigation hooks
// - Screen reader testing utilities
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 5: TESTING** sau Step 5.4 (sau dòng 1865)

---

#### **8. Logging Strategy (Chi Tiết)**

**Hiện trạng:**

- ✅ Có console.log warnings trong ESLint (dòng 267)
- ✅ Có Sentry logging (dòng 2294-2390)
- ❌ **THIẾU**: Structured logging library (Winston, Pino)
- ❌ **THIẾU**: Log levels configuration
- ❌ **THIẾU**: Log aggregation strategy
- ❌ **THIẾU**: Performance logging patterns

**Cần bổ sung:**

```typescript
// apps/web/src/services/logging/
// - Logger service với levels (debug, info, warn, error)
// - Structured logging format
// - Log aggregation setup (LogRocket, Datadog)
// - Performance logging utilities
// - Error context logging
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 7: MONITORING** sau Step 7.3 (sau dòng 2608)

---

#### **9. State Persistence Strategy**

**Hiện trạng:**

- ✅ Có Zustand store (dòng 633)
- ✅ Có useLocalStorage hook (dòng 606)
- ❌ **THIẾU**: State persistence patterns
- ❌ **THIẾU**: State hydration từ localStorage
- ❌ **THIẾU**: State migration strategies
- ❌ **THIẾU**: State versioning

**Cần bổ sung:**

```typescript
// libs/shared/utils/src/state/
// - State persistence middleware cho Zustand
// - State hydration utilities
// - State migration utilities
// - State versioning system
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 2: ARCHITECTURE** sau state management (sau dòng 638)

---

#### **10. API Documentation & Type Generation**

**Hiện trạng:**

- ✅ Có API client setup (dòng 623-626)
- ❌ **THIẾU**: API documentation strategy
- ❌ **THIẾU**: OpenAPI/Swagger integration
- ❌ **THIẾU**: Type generation từ API schema
- ❌ **THIẾU**: API mocking strategy

**Cần bổ sung:**

```typescript
// tools/api-generator/
// - OpenAPI schema parser
// - TypeScript type generator từ OpenAPI
// - API client generator
// - Mock server setup (MSW)
```

**Vị trí đề xuất:** Thêm vào **GIAI ĐOẠN 2: ARCHITECTURE** sau API client (sau dòng 630)

---

### **🟢 NICE TO HAVE - Có Thể Bổ Sung Sau**

#### **11. Dark Mode Implementation**

- Theme switching strategy
- System preference detection
- Theme persistence
- CSS variables cho theming

#### **12. Browser Compatibility & Polyfills**

- Browserslist configuration
- Polyfill strategy
- Feature detection
- Graceful degradation

#### **13. Memory Leak Detection**

- Memory profiling setup
- Leak detection patterns
- React DevTools Profiler integration
- Performance monitoring

#### **14. API Mocking & Testing**

- MSW (Mock Service Worker) setup
- Mock data factories
- API contract testing

#### **15. Component Documentation**

- Storybook setup chi tiết hơn
- Component API documentation
- Usage examples
- Design system integration

---

### **📋 TỔNG KẾT ĐỀ XUẤT BỔ SUNG**

| Priority     | Section                          | Lines Đề Xuất | Status     |
| ------------ | -------------------------------- | ------------- | ---------- |
| 🔴 Critical  | Error Handling Strategy          | ~200 lines    | ⚠️ Thiếu   |
| 🔴 Critical  | Environment Variables (Chi tiết) | ~150 lines    | ⚠️ Thiếu   |
| 🔴 Critical  | i18n Setup                       | ~250 lines    | ❌ Chưa có |
| 🔴 Critical  | PWA Implementation               | ~300 lines    | ⚠️ Thiếu   |
| 🔴 Critical  | SEO Optimization                 | ~200 lines    | ⚠️ Thiếu   |
| 🟡 Important | Security Best Practices          | ~200 lines    | ⚠️ Thiếu   |
| 🟡 Important | Accessibility Implementation     | ~150 lines    | ⚠️ Thiếu   |
| 🟡 Important | Logging Strategy                 | ~150 lines    | ⚠️ Thiếu   |
| 🟡 Important | State Persistence                | ~100 lines    | ⚠️ Thiếu   |
| 🟡 Important | API Documentation                | ~150 lines    | ⚠️ Thiếu   |

**Tổng cộng:** ~1,850 lines code examples + explanations cần bổ sung

---

### **🎯 Ưu Tiên Triển Khai**

**Phase 1 (Ngay lập tức):**

1. Error Handling Strategy
2. Environment Variables Management
3. i18n Setup

**Phase 2 (Tuần tiếp theo):** 4. PWA Implementation 5. SEO Optimization 6. Security Best Practices

**Phase 3 (Sau đó):** 7. Accessibility Implementation 8. Logging Strategy 9. State Persistence 10. API Documentation

---

### **💡 Lưu Ý Khi Bổ Sung**

1. **Giữ format nhất quán**: Mỗi section nên có:

   - Giải thích tại sao cần
   - Code examples production-ready
   - Best practices
   - Common pitfalls
   - Integration với các phần khác

2. **Cross-references**: Link đến các sections liên quan (ví dụ: Error Handling → Sentry, i18n → Date formatting)

3. **Real-world examples**: Dùng Banking Dashboard scenario như các phần khác

4. **Vietnamese comments**: Giữ style Vietnamese comments như hiện tại

5. **Code quality**: Tất cả code examples phải:
   - TypeScript strict mode compliant
   - Có error handling
   - Có proper types
   - Production-ready patterns
