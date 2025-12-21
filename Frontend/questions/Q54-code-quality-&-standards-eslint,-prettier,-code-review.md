# 📏 Q54: Code Quality & Standards - ESLint, Prettier, Code Review

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Code quality tools: ESLint (bugs + patterns), Prettier (formatting), Husky (pre-commit hooks), Commitlint (conventional commits). Code review: Small PRs, clear descriptions, constructive feedback, automated checks."**

**🔑 Tooling Stack:**

**1. ESLint - Linting:**
- **Find bugs**: unused vars, missing deps, type errors
- **Enforce patterns**: no-console, prefer-const, React hooks rules
- **Plugins**: @typescript-eslint, eslint-plugin-react, jsx-a11y
- **Config**: Extend airbnb/standard, customize rules

**2. Prettier - Formatting:**
- **Auto-format**: spacing, quotes, semicolons, line breaks
- **Config**: `.prettierrc` - printWidth, singleQuote, trailingComma
- **Integration**: ESLint plugin (eslint-plugin-prettier)
- **IDE**: Format on save (VSCode, WebStorm)

**3. Husky - Git Hooks:**
- **Pre-commit**: Run lint + format trước commit
- **Pre-push**: Run tests trước push
- **Commit-msg**: Validate commit message format
- **Setup**: `npx husky-init && npm install`

**4. Commitlint - Conventional Commits:**
- **Format**: `type(scope): subject` - `feat(auth): add login`
- **Types**: feat, fix, docs, style, refactor, test, chore
- **Benefits**: Auto-generate changelogs, semantic versioning

**🔑 Code Review Best Practices:**

- **Small PRs**: < 400 lines - dễ review, ít bugs
- **Clear descriptions**: What/Why/How, screenshots, testing steps
- **Automated checks**: Lint, tests, bundle size pass trước review
- **Constructive feedback**: Suggest alternatives, explain WHY
- **Timely reviews**: < 24 hours response time

**⚠️ Lỗi Thường Gặp:**
- ESLint warnings ignored → accumulate technical debt
- Không Prettier → inconsistent formatting, merge conflicts
- Large PRs (>1000 lines) → rubber-stamp reviews
- Blame culture in reviews → team morale giảm

**💡 Kiến Thức Senior:**
- **SonarQube**: Code quality metrics (bugs, vulnerabilities, code smells)
- **Bundle analysis**: webpack-bundle-analyzer - visualize bundle size
- **Lighthouse CI**: Performance budgets trong CI/CD
- **Danger.js**: Automate code review comments (big PRs warning, missing tests)

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)  
> **Thời gian trả lời:** 12-15 phút

---

## 📋 **Mục Lục**

1. [ESLint Configuration](#1-eslint-configuration)
2. [Prettier Setup](#2-prettier-setup)
3. [Husky & Git Hooks](#3-husky--git-hooks)
4. [Commitlint & Conventional Commits](#4-commitlint--conventional-commits)
5. [SonarQube Integration](#5-sonarqube-integration)
6. [Bundle Analysis](#6-bundle-analysis)
7. [Code Review Best Practices](#7-code-review-best-practices)

---

## 1. ESLint Configuration

### **1.1. Advanced ESLint Setup**

```javascript
// ===================================================
// 🔍 **ESLINT.CONFIG.MJS** (Flat Config - ESLint 9+)
// ===================================================

import js from '@eslint/js';
import typescript from '@typescript-eslint/eslint-plugin';
import tsParser from '@typescript-eslint/parser';
import react from 'eslint-plugin-react';
import reactHooks from 'eslint-plugin-react-hooks';
import reactRefresh from 'eslint-plugin-react-refresh';
import jsxA11y from 'eslint-plugin-jsx-a11y';
import importPlugin from 'eslint-plugin-import';
import prettier from 'eslint-plugin-prettier';

export default [
  js.configs.recommended, // ✅ ESLint recommended rules (cấu hình mặc định)
  
  {
    files: ['**/*.{ts,tsx}'], // 📁 Apply cho file TypeScript/TSX
    languageOptions: {
      parser: tsParser, // 🔧 Parser cho TypeScript
      parserOptions: {
        ecmaVersion: 'latest', // 🆕 Sử dụng ES version mới nhất
        sourceType: 'module', // 📦 ES Modules
        ecmaFeatures: {
          jsx: true, // ⚛️ Enable JSX parsing
        },
        project: './tsconfig.json', // 📋 TypeScript config file
      },
      globals: { // 🌐 Global variables (không cần import)
        window: 'readonly', // 🪟 Browser window object
        document: 'readonly', // 📄 DOM document
        navigator: 'readonly', // 🧭 Browser navigator
      },
    },
    
    plugins: { // 🔌 ESLint plugins
      '@typescript-eslint': typescript, // 📘 TypeScript rules
      'react': react, // ⚛️ React rules
      'react-hooks': reactHooks, // 🪝 React Hooks rules
      'react-refresh': reactRefresh, // 🔄 Vite HMR rules
      'jsx-a11y': jsxA11y, // ♿ Accessibility rules
      'import': importPlugin, // 📦 Import/export rules
      'prettier': prettier, // 💅 Prettier formatting
    },
    
    rules: {
      // ===================================================
      // ✅ TYPESCRIPT RULES - Kiểm tra lỗi TypeScript
      // ===================================================
      '@typescript-eslint/no-unused-vars': ['error', { // ❌ Báo lỗi biến không dùng
        argsIgnorePattern: '^_', // 🚫 Ignore args bắt đầu bằng _
        varsIgnorePattern: '^_', // 🚫 Ignore vars bắt đầu bằng _
      }],
      '@typescript-eslint/no-explicit-any': 'warn', // ⚠️ Cảnh báo khi dùng any
      '@typescript-eslint/explicit-function-return-type': ['warn', { // 🔤 Yêu cầu khai báo return type
        allowExpressions: true, // ✅ Cho phép arrow functions không cần type
        allowTypedFunctionExpressions: true, // ✅ Cho phép typed function expressions
      }],
      '@typescript-eslint/no-floating-promises': 'error', // ❌ Promise phải await hoặc .catch
      '@typescript-eslint/await-thenable': 'error', // ❌ Chỉ await những gì thenable
      '@typescript-eslint/no-misused-promises': 'error', // ❌ Không dùng Promise sai cách
      '@typescript-eslint/strict-boolean-expressions': 'off', // 🔓 Cho phép truthy/falsy
      
      // ===================================================
      // ⚛️ REACT RULES - Kiểm tra React best practices
      // ===================================================
      'react/react-in-jsx-scope': 'off', // 🔓 Not needed in React 17+ (auto import)
      'react/prop-types': 'off', // 🔓 Using TypeScript (không cần PropTypes)
      'react/jsx-no-target-blank': 'error', // ❌ <a target="_blank"> phải có rel="noreferrer"
      'react/jsx-key': ['error', { // ❌ Bắt buộc key khi map array
        checkFragmentShorthand: true, // ✅ Check cả <> fragment
      }],
      'react/no-array-index-key': 'warn', // ⚠️ Không dùng index làm key
      'react/no-unescaped-entities': 'warn', // ⚠️ Escape quotes trong JSX
      
      // ===================================================
      // 🪝 REACT HOOKS RULES - Kiểm tra Hooks
      // ===================================================
      'react-hooks/rules-of-hooks': 'error', // ❌ Hooks phải gọi ở top level
      'react-hooks/exhaustive-deps': 'warn', // ⚠️ Check dependencies đầy đủ
      
      // ===================================================
      // ♿ ACCESSIBILITY RULES - Kiểm tra khả năng tiếp cận
      // ===================================================
      'jsx-a11y/alt-text': 'error', // ❌ <img> phải có alt text
      'jsx-a11y/anchor-is-valid': 'error', // ❌ <a> phải có href hợp lệ
      'jsx-a11y/aria-props': 'error', // ❌ ARIA props phải hợp lệ
      'jsx-a11y/aria-role': 'error', // ❌ ARIA role phải đúng
      'jsx-a11y/click-events-have-key-events': 'warn', // ⚠️ onClick cần onKeyDown
      'jsx-a11y/no-static-element-interactions': 'warn', // ⚠️ Div onClick cần role
      
      // ===================================================
      // 📦 IMPORT RULES - Sắp xếp imports
      // ===================================================
      'import/order': ['error', { // ❌ Bắt buộc sắp xếp imports
        groups: [ // 📋 Thứ tự nhóm imports
          'builtin',   // 🏗️ Node.js built-in (fs, path)
          'external',  // 📦 npm packages (react, lodash)
          'internal',  // 🏠 Internal aliases (@/components)
          'parent',    // ⬆️ Parent imports (../)
          'sibling',   // ➡️ Sibling imports (./)
          'index',     // 📁 Index imports (./index)
        ],
        pathGroups: [ // 🎯 Custom grouping
          {
            pattern: 'react', // ⚛️ React luôn đầu tiên
            group: 'builtin',
            position: 'before',
          },
          {
            pattern: '@/**', // 🏠 Internal paths (@/...)
            group: 'internal',
          },
        ],
        pathGroupsExcludedImportTypes: ['react'], // 🚫 Exclude react khỏi sorting
        'newlines-between': 'always', // 📏 Dòng trống giữa các nhóm
        alphabetize: { // 🔤 Sắp xếp alphabet
          order: 'asc', // ⬆️ A → Z
          caseInsensitive: true, // 🔓 Không phân biệt hoa thường
        },
      }],
      'import/no-duplicates': 'error', // ❌ Không import trùng
      'import/no-unused-modules': 'warn', // ⚠️ File không được import
      
      // ===================================================
      // 💅 PRETTIER INTEGRATION - Tích hợp Prettier
      // ===================================================
      'prettier/prettier': 'error', // ❌ Formatting sai theo Prettier
      
      // ===================================================
      // 🚀 REACT REFRESH (Vite HMR) - Hot Module Replacement
      // ===================================================
      'react-refresh/only-export-components': ['warn', { // ⚠️ File chỉ export components
        allowConstantExport: true, // ✅ Cho phép export const
      }],
    },
    
    settings: { // ⚙️ Cấu hình bổ sung
      react: {
        version: 'detect', // 🔍 Auto detect React version
      },
      'import/resolver': { // 📦 Resolve TypeScript paths
        typescript: {
          project: './tsconfig.json', // 📋 TypeScript config
        },
      },
    },
  },
  
  {
    files: ['**/*.test.{ts,tsx}', '**/*.spec.{ts,tsx}'], // 🧪 Test files
    rules: { // 🔓 Relax rules cho test files
      '@typescript-eslint/no-explicit-any': 'off', // ✅ Cho phép any trong tests
      '@typescript-eslint/no-non-null-assertion': 'off', // ✅ Cho phép ! assertion
    },
  },
  
  {
    ignores: [ // 🚫 Files/folders bỏ qua
      'dist/', // 📦 Build output
      'build/', // 📦 Build folder
      'coverage/', // 📊 Test coverage
      'node_modules/', // 📦 Dependencies
      '*.config.js', // ⚙️ Config files
      '*.config.ts', // ⚙️ TS config files
    ],
  },
];
```

### **1.2. Custom ESLint Rules**

```javascript
// ===================================================
// 🎨 **CUSTOM ESLINT RULE** (Enforce naming conventions)
// ===================================================

// eslint-rules/component-naming.js
module.exports = {
  meta: {
    type: 'problem',
    docs: {
      description: 'Enforce PascalCase for React component files',
      category: 'Best Practices',
    },
    schema: [],
  },
  
  create(context) {
    return {
      Program(node) {
        const filename = context.getFilename();
        const componentFilePattern = /\.tsx$/;
        
        if (componentFilePattern.test(filename)) {
          const baseName = filename.split('/').pop().replace('.tsx', '');
          
          // Check if filename is PascalCase
          if (!/^[A-Z][a-zA-Z0-9]*$/.test(baseName)) {
            context.report({
              node,
              message: `Component file "${baseName}.tsx" should be PascalCase`,
            });
          }
        }
      },
    };
  },
};

// ===================================================
// 🔧 **USE CUSTOM RULE**
// ===================================================

// eslint.config.mjs
import componentNaming from './eslint-rules/component-naming.js';

export default [
  {
    plugins: {
      'custom': {
        rules: {
          'component-naming': componentNaming,
        },
      },
    },
    rules: {
      'custom/component-naming': 'error',
    },
  },
];
```

---

## 2. Prettier Setup

### **2.1. Prettier Configuration**

```javascript
// ===================================================
// 💅 **.PRETTIERRC.MJS** - Cấu hình Prettier
// ===================================================

export default {
  // ✅ Basic formatting - Định dạng cơ bản
  printWidth: 100, // 📏 Độ rộng tối đa 1 dòng (100 ký tự)
  tabWidth: 2, // 🔢 Kích thước tab = 2 spaces
  useTabs: false, // 🚫 Dùng spaces thay vì tabs
  semi: true, // ✅ Thêm semicolon (;) cuối dòng
  singleQuote: true, // '' Dùng single quotes thay vì double
  quoteProps: 'as-needed', // 🔑 Chỉ quote object keys khi cần
  
  // ✅ JSX formatting - Định dạng JSX
  jsxSingleQuote: false, // "" JSX dùng double quotes
  jsxBracketSameLine: false, // 📐 Đóng tag JSX xuống dòng mới
  
  // ✅ Trailing commas - Dấu phẩy cuối
  trailingComma: 'es5', // , Thêm dấu phẩy cuối (tương thích ES5)
  
  // ✅ Spacing - Khoảng trắng
  bracketSpacing: true, // { } Có space trong brackets
  arrowParens: 'avoid', // 🏹 x => x (không có parens nếu 1 param)
  
  // ✅ Line endings - Kết thúc dòng
  endOfLine: 'lf', // 🐧 Unix line endings (LF)
  
  // ✅ Import sorting (with plugin) - Sắp xếp imports
  importOrder: [ // 📋 Thứ tự imports
    '^react', // 1️⃣ React đầu tiên
    '^@?\\w', // 2️⃣ External packages (npm)
    '^@/(.*)$', // 3️⃣ Internal paths (@/...)
    '^[./]', // 4️⃣ Relative imports (./ ../)
  ],
  importOrderSeparation: true, // 📏 Dòng trống giữa nhóm
  importOrderSortSpecifiers: true, // 🔤 Sort named imports
  
  // ✅ Plugins - Prettier plugins
  plugins: [
    '@trivago/prettier-plugin-sort-imports', // 📦 Sắp xếp imports
    'prettier-plugin-tailwindcss', // 🎨 Format Tailwind classes
  ],
  
  // ✅ File-specific overrides - Cấu hình riêng cho từng loại file
  overrides: [
    {
      files: '*.json', // 📄 JSON files
      options: {
        printWidth: 80, // 📏 Rút ngắn độ rộng cho JSON
      },
    },
    {
      files: '*.md', // 📝 Markdown files
      options: {
        proseWrap: 'always', // 📖 Wrap text trong markdown
      },
    },
  ],
};
```

```json
// ===================================================
// 🚫 **.PRETTIERIGNORE** - Files không format
// ===================================================

# Build outputs - Thư mục build
dist/ # 📦 Production build
build/ # 📦 Build folder
coverage/ # 📊 Test coverage reports

# Dependencies - Dependencies
node_modules/ # 📦 npm packages

# Logs - File logs
*.log # 📝 Log files

# Auto-generated files - Files tự động tạo
*.generated.ts # 🤖 Generated TypeScript
*.d.ts # 📘 TypeScript declarations

# Config files - Lock files
pnpm-lock.yaml # 🔒 pnpm lock
package-lock.json # 🔒 npm lock
package-lock.json
```

---

## 3. Husky & Git Hooks

### **3.1. Husky Setup**

```bash
# ===================================================
# 🐶 **INSTALL HUSKY**
# ===================================================

npm install --save-dev husky lint-staged
npx husky init

# Creates .husky/ folder with pre-commit hook
```

```bash
# ===================================================
# 🔒 **.husky/pre-commit**
# ===================================================

#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# ✅ Run lint-staged
npx lint-staged

# ✅ Run type check
npm run type-check

# ✅ Run tests on changed files
npm run test:changed
```

```bash
# ===================================================
# 📝 **.husky/commit-msg**
# ===================================================

#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# ✅ Validate commit message format
npx commitlint --edit $1
```

```bash
# ===================================================
# 🚀 **.husky/pre-push** - Chạy trước khi push
# ===================================================

#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# ✅ Run full test suite - Chạy tất cả tests
npm run test

# ✅ Build check - Kiểm tra build có lỗi không
npm run build

# ✅ Bundle size check - Kiểm tra kích thước bundle
npm run size-limit
```

### **3.2. Lint-Staged Configuration**

```json
// ===================================================
// 🎯 **LINT-STAGED** (package.json) - Chạy cho staged files
// ===================================================

{
  "lint-staged": {
    "*.{ts,tsx}": [ // 📘 TypeScript/TSX files
      "eslint --fix", // 🔧 Auto-fix lỗi ESLint
      "prettier --write", // 💅 Format code
      "vitest related --run" // 🧪 Chạy tests liên quan
    ],
    "*.{js,jsx}": [ // 📄 JavaScript/JSX files
      "eslint --fix", // 🔧 Auto-fix lỗi
      "prettier --write" // 💅 Format code
    ],
    "*.{json,md,yml,yaml}": [ // 📝 Config/doc files
      "prettier --write" // 💅 Format only
    ],
    "*.css": [ // 🎨 CSS files
      "prettier --write", // 💅 Format CSS
      "stylelint --fix" // 🔧 Fix CSS linting
    ]
  }
}
```

---

## 4. Commitlint & Conventional Commits

### **4.1. Commitlint Setup**

```javascript
// ===================================================
// 📋 **COMMITLINT.CONFIG.MJS** - Kiểm tra commit message
// ===================================================

export default {
  extends: ['@commitlint/config-conventional'], // 📏 Dùng conventional commits
  
  rules: {
    // ✅ Type enum - Các loại commit hợp lệ
    'type-enum': [
      2, // ❌ Error level (bắt buộc)
      'always', // 🔒 Luôn check
      [
        'feat',     // ✨ New feature - Tính năng mới
        'fix',      // 🐛 Bug fix - Sửa lỗi
        'docs',     // 📝 Documentation - Tài liệu
        'style',    // 💄 Formatting - Format code
        'refactor', // ♻️ Code restructuring - Tái cấu trúc
        'perf',     // ⚡ Performance improvement - Cải thiện performance
        'test',     // 🧪 Tests - Viết tests
        'chore',    // 🔧 Maintenance - Bảo trì
        'ci',       // 👷 CI/CD changes - Thay đổi CI/CD
        'revert',   // ⏪ Revert commit - Hoàn tác commit
      ],
    ],
    
    // ✅ Subject rules - Quy tắc cho subject (tiêu đề)
    'subject-case': [2, 'never', ['upper-case']], // 🔡 Không viết hoa đầu
    'subject-empty': [2, 'never'], // ❌ Subject không được rỗng
    'subject-full-stop': [2, 'never', '.'], // 🚫 Không dấu chấm cuối
    'subject-max-length': [2, 'always', 100], // 📏 Tối đa 100 ký tự
    
    // ✅ Body rules - Quy tắc cho body (nội dung)
    'body-leading-blank': [2, 'always'], // 📏 Dòng trống trước body
    'body-max-line-length': [2, 'always', 100], // 📏 Tối đa 100 ký tự/dòng
    
    // ✅ Footer rules - Quy tắc cho footer
    'footer-leading-blank': [2, 'always'], // 📏 Dòng trống trước footer
    
    // ✅ Scope enum (optional) - Các scope hợp lệ (không bắt buộc)
    'scope-enum': [
      1, // ⚠️ Warning level (khuyến nghị)
      'always', // 🔓 Luôn check nếu có scope
      [
        'core',       // 🏗️ Core functionality
        'ui',         // 🎨 UI components
        'api',        // 📡 API changes
        'auth',       // 🔐 Authentication
        'components', // 🧩 React components
        'hooks',      // 🪝 Custom hooks
        'utils',      // 🛠️ Utility functions
        'config',     // ⚙️ Configuration
        'deps',       // 📦 Dependencies
      ],
    ],
  },
};
        'ui',
        'api',
        'auth',
        'components',
        'hooks',
        'utils',
        'config',
        'deps',
      ],
    ],
  },
};
```

```bash
# ===================================================
# ✅ **VALID COMMIT MESSAGES** - Commit messages đúng
# ===================================================

feat(auth): add OAuth2 login support # ✨ Thêm tính năng mới
fix(ui): resolve button hover state bug # 🐛 Sửa lỗi
docs(readme): update installation instructions # 📝 Cập nhật docs
refactor(api): simplify user service logic # ♻️ Refactor code
perf(core): optimize bundle size with code splitting # ⚡ Tối ưu performance
test(hooks): add tests for useDebounce # 🧪 Thêm tests
chore(deps): upgrade React to 18.3.0 # 🔧 Update dependencies

# ===================================================
# ❌ **INVALID COMMIT MESSAGES** - Commit messages sai
# ===================================================

Fixed bug              # ❌ Missing type (thiếu type)
FEAT: new feature      # ❌ Wrong case (viết hoa sai)
feat add feature       # ❌ Missing colon (thiếu dấu :)
feat: Add new feature. # ❌ Full stop at end (có dấu chấm cuối)
```

---

## 5. SonarQube Integration

### **5.1. SonarQube Setup**

```yaml
# ===================================================
# 📊 **SONARQUBE WORKFLOW** (.github/workflows/sonar.yml)
# ===================================================

name: SonarQube Analysis # 📏 Tên workflow

on:
  push:
    branches: [main, develop] # 🌿 Chạy khi push vào main/develop
  pull_request:
    types: [opened, synchronize, reopened] # 🔄 Chạy khi tạo/update PR

jobs:
  sonar:
    runs-on: ubuntu-latest # 🐧 Chạy trên Ubuntu
    steps:
      - uses: actions/checkout@v4 # 📥 Checkout code
        with:
          fetch-depth: 0 # 🔍 Full history for better analysis (lịch sử đầy đủ)
      
      - uses: actions/setup-node@v4 # ⚙️ Setup Node.js
        with:
          node-version: 20 # 🔢 Node version 20
      
      - run: npm ci # 📦 Install dependencies (clean install)
      - run: npm run test:coverage # 🧪 Chạy tests + coverage
      
      - name: SonarQube Scan # 🔍 Scan code quality
        uses: SonarSource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }} # 🔑 SonarQube token
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }} # 🌐 SonarQube server URL
      
      - name: SonarQube Quality Gate # 🚦 Check quality gate
        uses: SonarSource/sonarqube-quality-gate-action@master
        timeout-minutes: 5 # ⏱️ Timeout 5 phút
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }} # 🔑 Token
```

```properties
# ===================================================
# ⚙️ **SONAR-PROJECT.PROPERTIES** - Cấu hình SonarQube
# ===================================================

sonar.projectKey=my-frontend-app # 🔑 Project key (unique)
sonar.organization=my-org # 🏢 Organization name

# ✅ Source configuration - Cấu hình source code
sonar.sources=src # 📁 Thư mục source code
sonar.tests=src # 🧪 Thư mục tests (cùng folder với src)
sonar.test.inclusions=**/*.test.ts,**/*.test.tsx,**/*.spec.ts,**/*.spec.tsx # 🎯 Test files pattern
sonar.exclusions=**/node_modules/**,**/dist/**,**/coverage/** # 🚫 Bỏ qua folders

# ✅ Coverage report - Báo cáo coverage
sonar.javascript.lcov.reportPaths=coverage/lcov.info # 📊 LCOV coverage file
sonar.testExecutionReportPaths=coverage/test-report.xml # 📄 Test execution report

# ✅ Code quality settings - Cài đặt chất lượng code
sonar.sourceEncoding=UTF-8 # 🔤 Encoding UTF-8
sonar.javascript.node.maxspace=4096 # 💾 Max memory cho Node.js (MB)

# ✅ Quality gates - Ngưỡng chất lượng
sonar.qualitygate.wait=true # ⏳ Chờ quality gate check xong
sonar.qualitygate.timeout=300 # ⏱️ Timeout 300s (5 phút)
```

---

## 6. Bundle Analysis

### **6.1. Bundle Size Monitoring**

```json
// ===================================================
// 📦 **SIZE-LIMIT** (.size-limit.json) - Giới hạn kích thước bundle
// ===================================================

[
  {
    "name": "Main Bundle", // 📄 Tên bundle
    "path": "dist/assets/index-*.js", // 📁 Đường dẫn file
    "limit": "200 KB", // ⚠️ Giới hạn 200 KB
    "gzip": true, // 🗜️ Tính gzip size
    "webpack": false // 🚫 Không dùng webpack
  },
  {
    "name": "Vendor Bundle", // 📦 Bundle libraries
    "path": "dist/assets/vendor-*.js",
    "limit": "150 KB", // ⚠️ Giới hạn 150 KB
    "gzip": true
  },
  {
    "name": "CSS Bundle", // 🎨 Bundle CSS
    "path": "dist/assets/index-*.css",
    "limit": "50 KB", // ⚠️ Giới hạn 50 KB
    "gzip": true
  }
]
```

```javascript
// ===================================================
// 📊 **VITE BUNDLE ANALYZER** (vite.config.ts)
// ===================================================

import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { visualizer } from 'rollup-plugin-visualizer';

export default defineConfig({
  plugins: [
    react(), // ⚛️ React plugin
    
    // ✅ Bundle analyzer - Phân tích bundle size
    visualizer({
      open: true, // 🌐 Tự động mở browser
      filename: 'dist/stats.html', // 📄 File output
      gzipSize: true, // 🗜️ Hiển thị gzip size
      brotliSize: true, // 🗜️ Hiển thị brotli size
      template: 'treemap', // 📊 treemap, sunburst, network (kiểu hiển thị)
    }),
  ],
  
  build: {
    rollupOptions: {
      output: {
        manualChunks: { // 📦 Chia nhỏ chunks thủ công
          // ✅ Split vendor chunks - Tách riêng vendors
          vendor: ['react', 'react-dom'], // ⚛️ React core
          router: ['react-router-dom'], // 🛤️ Router
          ui: ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'], // 🎨 UI libs
        },
      },
    },
    
    // ✅ Report compressed size - Báo cáo size nén
    reportCompressedSize: true, // 📊 Hiển thị gzip size khi build
    
    // ✅ Chunk size warning limit - Cảnh báo chunk quá lớn
    chunkSizeWarningLimit: 500, // ⚠️ Cảnh báo nếu > 500 KB
  },
});
```

---

## 7. Code Review Best Practices

### **7.1. Pull Request Template**

```markdown
<!-- ===================================================
     📝 **PULL REQUEST TEMPLATE** (.github/pull_request_template.md)
     =================================================== -->

## 📋 Description
Brief description of what this PR does

## 🎯 Type of Change
- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📝 Documentation update
- [ ] ♻️ Code refactoring

## 🔗 Related Issues
Closes #(issue_number)

## 🧪 Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E tests added/updated
- [ ] Manual testing completed

## 📸 Screenshots (if applicable)
<!-- Add screenshots here -->

## ✅ Checklist
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## 📊 Performance Impact
- Bundle size change: ±X KB
- Lighthouse score impact: No change / Improved / Degraded

## 🔒 Security Considerations
<!-- Any security implications? -->

## 📚 Documentation
- [ ] README updated
- [ ] CHANGELOG updated
- [ ] API documentation updated
```

### **7.2. Automated PR Checks**

```yaml
# ===================================================
# 🤖 **PR CHECKS WORKFLOW**
# ===================================================

name: PR Checks

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  pr-validation:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      # ✅ Check PR title format
      - name: Validate PR title
        uses: amannn/action-semantic-pull-request@v5
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          types: |
            feat
            fix
            docs
            style
            refactor
            perf
            test
            chore
      
      # ✅ Check for TODO comments
      - name: Check for TODOs
        run: |
          if grep -r "TODO" src/; then
            echo "⚠️ Found TODO comments in code"
            exit 1
          fi
      
      # ✅ Bundle size check
      - run: npm ci
      - run: npm run build
      - name: Check bundle size
        uses: andresz1/size-limit-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
      
      # ✅ Lighthouse CI
      - name: Lighthouse
        uses: treosh/lighthouse-ci-action@v10
        with:
          urls: |
            http://localhost:3000
          uploadArtifacts: true
          temporaryPublicStorage: true
```

---

**🎯 Remember:** "Code quality tools are not police - they're assistants. Configure them to help your team, not hinder productivity!"
