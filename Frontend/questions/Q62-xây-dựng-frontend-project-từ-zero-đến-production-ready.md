# 🏗️ Q62: Xây Dựng Frontend Project từ Zero đến Production-Ready

## **⭐ PHIÊN BẢN TRẢ LỜI 1 PHÚT (Cho Phỏng Vấn Nhanh)**

**"Build Frontend project production-ready cần 8 giai đoạn: Setup Project → Architecture → Code Quality → Performance → Testing → CI/CD → Monitoring → Scalability.**

**Đã lead team build Banking Dashboard từ zero: Nx monorepo với 15 apps/libs, ESLint + Prettier + Husky enforce standards, Vite build optimization (3s → 0.8s), React Query + Zustand state management, Vitest + Playwright testing (85% coverage), GitHub Actions CI/CD auto deploy, Sentry monitoring errors, scalable đến 50+ developers collaboration.**

**Key principles: Clear folder structure (feature-based), Shared libraries (DRY), Automated tooling (ESLint, TypeScript strict), Performance budgets (Lighthouse CI), Modular architecture (micro-frontends ready). Result: 70% faster development, 90% fewer bugs, deploy 20 times/day.**

**Critical: TypeScript strict mode, path aliases, absolute imports, automated code review, bundle analysis, environment variables management, comprehensive testing strategy từ đầu - không phải "sẽ làm sau"."**

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
# TẠI SAO DÙNG NX?
# =====================================
# ✅ Monorepo support - Quản lý multiple apps/libs
# ✅ Built-in code generators
# ✅ Dependency graph visualization
# ✅ Affected commands - Chỉ test/build code thay đổi
# ✅ Caching layer - Build/test nhanh hơn 10x

# Install Nx CLI
npm install -g nx@latest

# Create workspace
npx create-nx-workspace@latest my-app \
  --preset=react-monorepo \
  --packageManager=pnpm \
  --nx-cloud=true

# Structure sau khi tạo:
# my-app/
# ├── apps/
# │   ├── web/              # Main web app
# │   ├── admin/            # Admin dashboard
# │   └── mobile/           # React Native (optional)
# ├── libs/
# │   ├── shared/
# │   │   ├── ui/           # Shared components
# │   │   ├── utils/        # Helper functions
# │   │   ├── types/        # TypeScript types
# │   │   └── api/          # API client
# │   └── features/
# │       ├── auth/         # Authentication feature
# │       ├── dashboard/    # Dashboard feature
# │       └── settings/     # Settings feature
# ├── tools/                # Custom scripts
# ├── .github/
# │   └── workflows/        # GitHub Actions
# ├── nx.json
# ├── tsconfig.base.json
# └── package.json
```

#### **Step 1.2: TypeScript Configuration (Strict Mode)**

```json
// tsconfig.base.json
{
  "compilerOptions": {
    // ✅ STRICT MODE - Bắt lỗi sớm nhất
    "strict": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "noImplicitAny": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    
    // ✅ MODULE RESOLUTION
    "module": "ESNext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    
    // ✅ PATH ALIASES - Import rõ ràng
    "baseUrl": ".",
    "paths": {
      "@app/*": ["apps/web/src/*"],
      "@libs/shared/ui": ["libs/shared/ui/src/index.ts"],
      "@libs/shared/utils": ["libs/shared/utils/src/index.ts"],
      "@libs/shared/types": ["libs/shared/types/src/index.ts"],
      "@libs/shared/api": ["libs/shared/api/src/index.ts"],
      "@libs/features/*": ["libs/features/*/src/index.ts"]
    },
    
    // ✅ OUTPUT
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "exclude": ["node_modules", "dist", "build", ".next"]
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
    'plugin:@typescript-eslint/recommended',
    'plugin:@typescript-eslint/recommended-requiring-type-checking',
    'plugin:react/recommended',
    'plugin:react-hooks/recommended',
    'plugin:jsx-a11y/recommended', // Accessibility
    'plugin:import/recommended',
    'plugin:import/typescript',
    'prettier', // Phải để cuối cùng
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
    project: ['./tsconfig.json', './apps/*/tsconfig.json', './libs/*/tsconfig.json'],
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
        project: ['./tsconfig.json', './apps/*/tsconfig.json', './libs/*/tsconfig.json'],
      },
    },
  },
  rules: {
    // ===================================
    // TYPESCRIPT RULES
    // ===================================
    '@typescript-eslint/no-unused-vars': ['error', { 
      argsIgnorePattern: '^_',
      varsIgnorePattern: '^_',
    }],
    '@typescript-eslint/no-explicit-any': 'error',
    '@typescript-eslint/explicit-function-return-type': ['warn', {
      allowExpressions: true,
      allowTypedFunctionExpressions: true,
    }],
    '@typescript-eslint/consistent-type-imports': ['error', {
      prefer: 'type-imports',
    }],
    '@typescript-eslint/no-floating-promises': 'error',
    '@typescript-eslint/await-thenable': 'error',
    '@typescript-eslint/no-misused-promises': 'error',
    
    // ===================================
    // REACT RULES
    // ===================================
    'react/react-in-jsx-scope': 'off', // React 17+
    'react/prop-types': 'off', // TypeScript handles this
    'react/jsx-no-target-blank': ['error', { 
      allowReferrer: false,
      enforceDynamicLinks: 'always',
    }],
    'react/jsx-key': ['error', { 
      checkFragmentShorthand: true,
    }],
    'react-hooks/rules-of-hooks': 'error',
    'react-hooks/exhaustive-deps': 'warn',
    
    // ===================================
    // IMPORT RULES
    // ===================================
    'import/no-unresolved': 'error',
    'import/no-cycle': 'error', // Ngăn circular dependencies
    'import/no-duplicates': 'error',
    'simple-import-sort/imports': 'error',
    'simple-import-sort/exports': 'error',
    'unused-imports/no-unused-imports': 'error',
    
    // ===================================
    // GENERAL RULES
    // ===================================
    'no-console': ['warn', { allow: ['warn', 'error'] }],
    'no-debugger': 'error',
    'no-alert': 'error',
    'prefer-const': 'error',
    'no-var': 'error',
    'eqeqeq': ['error', 'always'],
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
# Install
pnpm add -D husky lint-staged @commitlint/cli @commitlint/config-conventional

# Setup husky
npx husky install
npm pkg set scripts.prepare="husky install"
```

```javascript
// .husky/pre-commit
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# Run lint-staged
pnpm lint-staged
```

```javascript
// .husky/commit-msg
#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# Validate commit message
npx --no -- commitlint --edit ${1}
```

```javascript
// .lintstagedrc.cjs
module.exports = {
  // TypeScript files
  '*.{ts,tsx}': [
    'eslint --fix',
    'prettier --write',
    () => 'tsc --noEmit', // Type check
  ],
  
  // JavaScript files
  '*.{js,jsx}': [
    'eslint --fix',
    'prettier --write',
  ],
  
  // JSON, CSS, Markdown
  '*.{json,css,scss,md}': [
    'prettier --write',
  ],
  
  // Test files - Run related tests
  '*.{test,spec}.{ts,tsx}': [
    'vitest related --run',
  ],
};
```

```javascript
// commitlint.config.cjs
module.exports = {
  extends: ['@commitlint/config-conventional'],
  rules: {
    'type-enum': [
      2,
      'always',
      [
        'feat',     // New feature
        'fix',      // Bug fix
        'docs',     // Documentation
        'style',    // Formatting, missing semicolons, etc.
        'refactor', // Code change that neither fixes a bug nor adds a feature
        'perf',     // Performance improvement
        'test',     // Adding tests
        'chore',    // Updating build tasks, package manager configs, etc.
        'revert',   // Revert a previous commit
        'ci',       // CI/CD changes
      ],
    ],
    'subject-case': [2, 'never', ['upper-case']],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'header-max-length': [2, 'always', 100],
  },
};

// Example valid commits:
// ✅ feat: add user authentication
// ✅ fix: resolve memory leak in dashboard
// ✅ docs: update API documentation
// ❌ Added new feature (missing type)
// ❌ FEAT: Add feature (uppercase subject)
```

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
```

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
export { validateEmail, validatePhone, validateURL } from './validation/validators';

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

// ✅ Reusable schemas
export const emailSchema = z.string().email('Invalid email format');

export const passwordSchema = z
  .string()
  .min(8, 'Password must be at least 8 characters')
  .regex(/[A-Z]/, 'Password must contain uppercase letter')
  .regex(/[a-z]/, 'Password must contain lowercase letter')
  .regex(/[0-9]/, 'Password must contain number')
  .regex(/[^A-Za-z0-9]/, 'Password must contain special character');

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
export type User = z.infer<typeof userSchema>;

// Login form schema
export const loginFormSchema = z.object({
  email: emailSchema,
  password: z.string().min(1, 'Password is required'),
  rememberMe: z.boolean().optional(),
});

export type LoginFormData = z.infer<typeof loginFormSchema>;

// =====================================
// Usage trong component
// =====================================

import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { loginFormSchema, type LoginFormData } from '@libs/shared/utils';

function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginFormSchema),
  });

  const onSubmit = (data: LoginFormData) => {
    // data is fully typed and validated
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
  warn(`:exclamation: Large PR (${changes} lines changed). Consider breaking it into smaller PRs for easier review.`);
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
  fail('⚠️ package.json changed but pnpm-lock.yaml not updated. Run `pnpm install`.');
}

// ===================================
// CONSOLE.LOG CHECK
// ===================================
const newOrModified = [...danger.git.created_files, ...danger.git.modified_files];
const jsFiles = newOrModified.filter((file) => file.endsWith('.ts') || file.endsWith('.tsx'));

for (const file of jsFiles) {
  const content = await danger.github.utils.fileContents(file);
  
  if (content.includes('console.log')) {
    warn(`⚠️ Found \`console.log\` in ${file}. Remove before merging or use proper logger.`);
  }
  
  if (content.includes('debugger')) {
    fail(`🚫 Found \`debugger\` statement in ${file}. Remove before merging.`);
  }
}

// ===================================
// BUNDLE SIZE CHECK
// ===================================
const bundleAnalysis = danger.git.modified_files.find(
  (file) => file.includes('bundle-stats.json')
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
    react(),
    
    // ✅ Bundle analyzer
    visualizer({
      filename: 'dist/stats.html',
      gzipSize: true,
      brotliSize: true,
    }),
    
    // ✅ Gzip compression
    compression({
      algorithm: 'gzip',
      ext: '.gz',
    }),
    
    // ✅ Brotli compression (tốt hơn gzip)
    compression({
      algorithm: 'brotliCompress',
      ext: '.br',
    }),
    
    // ✅ PWA support
    VitePWA({
      registerType: 'autoUpdate',
      includeAssets: ['favicon.ico', 'robots.txt', 'apple-touch-icon.png'],
      manifest: {
        name: 'My App',
        short_name: 'App',
        theme_color: '#ffffff',
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
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
    target: 'esnext',
    
    // ✅ Minify với esbuild (nhanh)
    minify: 'esbuild',
    
    // ✅ Source maps cho production debug
    sourcemap: true,
    
    // ✅ Code splitting
    rollupOptions: {
      output: {
        manualChunks: {
          // Vendor chunks
          'react-vendor': ['react', 'react-dom', 'react-router-dom'],
          'query-vendor': ['@tanstack/react-query'],
          'ui-vendor': ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
          
          // Feature chunks
          'dashboard': ['./src/features/dashboard'],
          'settings': ['./src/features/settings'],
        },
        
        // ✅ Chunk naming
        chunkFileNames: 'assets/js/[name]-[hash].js',
        entryFileNames: 'assets/js/[name]-[hash].js',
        assetFileNames: 'assets/[ext]/[name]-[hash].[ext]',
      },
    },
    
    // ✅ Chunk size warnings
    chunkSizeWarningLimit: 500, // 500kb
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
const HomePage = lazy(() => import('../pages/HomePage'));
const DashboardPage = lazy(() => import('../pages/DashboardPage'));
const SettingsPage = lazy(() => import('../pages/SettingsPage'));
const ProfilePage = lazy(() => import('../pages/ProfilePage'));

// ✅ Preload critical routes
const preloadDashboard = () => import('../pages/DashboardPage');
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
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json', 'html', 'lcov'],
      exclude: [
        'node_modules/',
        'src/__tests__/',
        '**/*.test.{ts,tsx}',
        '**/*.spec.{ts,tsx}',
        '**/*.stories.{ts,tsx}',
        '**/types/',
        '**/*.d.ts',
      ],
      // ✅ Coverage thresholds
      statements: 80,
      branches: 75,
      functions: 80,
      lines: 80,
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
  {
    initialRoute = '/',
    ...renderOptions
  }: CustomRenderOptions = {}
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
        <BrowserRouter>
          {children}
        </BrowserRouter>
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
export const mockApiSuccess = <T,>(data: T) => {
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
    
    expect(await screen.findByText(/invalid email format/i)).toBeInTheDocument();
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
    await page.waitForResponse((response) =>
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
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

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
      tracesSampleRate: 0.1, // 10% của transactions
      replaysSessionSampleRate: 0.1, // 10% sessions
      replaysOnErrorSampleRate: 1.0, // 100% khi có error
      
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
import { initSentry, SentryErrorBoundary } from '@app/services/monitoring/sentry';

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
import { onCLS, onFID, onFCP, onLCP, onTTFB } from 'web-vitals';
import { trackTiming } from '../analytics/analytics';

// ✅ Track Web Vitals
export function initPerformanceMonitoring() {
  // Cumulative Layout Shift
  onCLS((metric) => {
    trackTiming('Web Vitals', 'CLS', metric.value);
    console.log('CLS:', metric.value);
  });
  
  // First Input Delay
  onFID((metric) => {
    trackTiming('Web Vitals', 'FID', metric.value);
    console.log('FID:', metric.value);
  });
  
  // First Contentful Paint
  onFCP((metric) => {
    trackTiming('Web Vitals', 'FCP', metric.value);
    console.log('FCP:', metric.value);
  });
  
  // Largest Contentful Paint
  onLCP((metric) => {
    trackTiming('Web Vitals', 'LCP', metric.value);
    console.log('LCP:', metric.value);
  });
  
  // Time to First Byte
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

```typescript
// libs/shared/utils/src/featureFlags/featureFlags.ts
type FeatureFlag =
  | 'newDashboard'
  | 'darkMode'
  | 'advancedFilters'
  | 'experimentalFeature';

interface FeatureFlagConfig {
  enabled: boolean;
  rolloutPercentage?: number; // 0-100
  enabledFor?: string[]; // User IDs
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
      hash = ((hash << 5) - hash) + userId.charCodeAt(i);
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
    expect(calculateTotal([
      { price: 10, quantity: 2 },
      { price: 5, quantity: 3 },
    ])).toBe(35);
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
    fetch('/api/data').then(res => setData(res.data));
  }, []);
  
  return <Table data={data} />;
}

// ✅ GOOD: Performance tracking
function DataTable() {
  const [data, setData] = useState([]);
  
  useEffect(() => {
    const perf = measurePerformance('data-fetch');
    perf.start();
    
    fetch('/api/data')
      .then(res => {
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

| Aspect | Monorepo (Nx) | Polyrepo |
|--------|---------------|----------|
| **Code Sharing** | ⭐⭐⭐⭐⭐ Easy with libs | ⭐⭐ Requires npm packages |
| **Consistency** | ⭐⭐⭐⭐⭐ Enforced standards | ⭐⭐ Varies per repo |
| **Refactoring** | ⭐⭐⭐⭐⭐ Atomic changes | ⭐⭐ Multiple PRs needed |
| **CI/CD Speed** | ⭐⭐⭐⭐⭐ Affected commands | ⭐⭐⭐ Build everything |
| **Onboarding** | ⭐⭐⭐ Single repo to clone | ⭐⭐ Multiple repos |
| **Team Scale** | ⭐⭐⭐⭐⭐ 50+ developers | ⭐⭐⭐ Best for small teams |
| **Dependencies** | ⭐⭐⭐⭐ Centralized | ⭐⭐ Can drift |

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
```typescript
// ✅ 1. SWC instead of Babel (20x faster)
// vite.config.ts
plugins: [react({ jsxRuntime: 'automatic', jsxImportSource: '@emotion/react' })]

// ✅ 2. Dependency pre-bundling
optimizeDeps: {
  include: ['react', 'react-dom', 'react-router-dom'],
}

// ✅ 3. Code splitting per route
const Dashboard = lazy(() => import('./pages/Dashboard'));

// ✅ 4. Analyze bundle
pnpm vite-bundle-visualizer
```

### **Runtime Optimization**
```typescript
// ✅ 1. React.memo for expensive components
const ExpensiveComponent = React.memo(({ data }) => {
  return <div>{/* Heavy render logic */}</div>;
});

// ✅ 2. useMemo for expensive calculations
const sortedData = useMemo(() => {
  return data.sort((a, b) => a.value - b.value);
}, [data]);

// ✅ 3. Virtual scrolling for large lists
import { FixedSizeList } from 'react-window';

function LargeList({ items }) {
  return (
    <FixedSizeList
      height={600}
      itemCount={items.length}
      itemSize={50}
    >
      {({ index, style }) => (
        <div style={style}>{items[index]}</div>
      )}
    </FixedSizeList>
  );
}

// ✅ 4. Image optimization
<img
  src="/image.jpg"
  loading="lazy"
  decoding="async"
  alt="..."
/>
```

### **Network Optimization**
```typescript
// ✅ 1. React Query stale-while-revalidate
const { data } = useQuery({
  queryKey: ['users'],
  queryFn: fetchUsers,
  staleTime: 5 * 60 * 1000, // 5 minutes
  cacheTime: 10 * 60 * 1000, // 10 minutes
});

// ✅ 2. Prefetch on hover
<Link
  to="/dashboard"
  onMouseEnter={() => queryClient.prefetchQuery({
    queryKey: ['dashboard'],
    queryFn: fetchDashboard,
  })}
>
  Dashboard
</Link>

// ✅ 3. Parallel requests
const [users, posts, comments] = await Promise.all([
  fetchUsers(),
  fetchPosts(),
  fetchComments(),
]);
```

---

## **📝 8. KEY TAKEAWAYS**

### **🎯 Essential Checklist**

```markdown
## ✅ PRODUCTION-READY CHECKLIST

### Foundation
- [ ] TypeScript strict mode enabled
- [ ] ESLint + Prettier configured
- [ ] Git hooks (Husky + lint-staged)
- [ ] Commit conventions enforced
- [ ] Path aliases configured

### Architecture
- [ ] Feature-based folder structure
- [ ] Shared libraries created
- [ ] State management strategy defined
- [ ] API client with interceptors
- [ ] Error boundaries implemented

### Code Quality
- [ ] Automated code review (Danger.js)
- [ ] Type safety enforced (Zod schemas)
- [ ] Code formatting automated
- [ ] Import sorting configured
- [ ] Unused code detected

### Performance
- [ ] Build optimization (Vite/SWC)
- [ ] Code splitting per route
- [ ] Lazy loading implemented
- [ ] Bundle analysis setup
- [ ] Performance budgets defined

### Testing
- [ ] Unit tests (80%+ coverage)
- [ ] Integration tests
- [ ] E2E tests (critical paths)
- [ ] Visual regression tests
- [ ] Accessibility tests

### CI/CD
- [ ] GitHub Actions workflows
- [ ] Affected commands configured
- [ ] Auto deployment setup
- [ ] Environment management
- [ ] Secret management

### Monitoring
- [ ] Error tracking (Sentry)
- [ ] Analytics (Google Analytics)
- [ ] Performance monitoring (Web Vitals)
- [ ] Logging strategy
- [ ] Alerts configured

### Documentation
- [ ] README comprehensive
- [ ] Storybook for components
- [ ] API documentation
- [ ] Architecture diagrams
- [ ] Onboarding guide

### Scalability
- [ ] Micro-frontends ready
- [ ] Feature flags system
- [ ] A/B testing capability
- [ ] Multi-tenancy support
- [ ] Internationalization (i18n)
```

### **💡 Core Principles**

1. **Start with solid foundation** - TypeScript strict, proper tooling
2. **Automate everything** - Linting, testing, deployment
3. **Measure performance** - Lighthouse CI, Web Vitals
4. **Test comprehensively** - Unit, integration, E2E
5. **Monitor in production** - Sentry, analytics, metrics
6. **Document thoroughly** - README, Storybook, diagrams
7. **Scale thoughtfully** - Monorepo, shared libraries, feature flags
8. **Iterate continuously** - Regular audits, refactoring, updates

### **🚀 Final Wisdom**

**"Tốt nhất là xây dựng từ đầu đúng cách, không phải refactor sau. Investment vào tooling, testing, và monitoring ngày đầu sẽ trả về gấp 10 lần về sau."**

**Success Metrics:**
- **Developer Experience**: How fast can new dev be productive?
- **Code Quality**: How many bugs reach production?
- **Performance**: How fast is the app?
- **Reliability**: How often does it break?
- **Maintainability**: How easy to change?

**Remember:** Production-ready ≠ Perfect. Ship fast, iterate, improve continuously! 🚀
