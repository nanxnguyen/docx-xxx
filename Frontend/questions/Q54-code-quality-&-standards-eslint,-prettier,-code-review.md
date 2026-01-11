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

> **Câu hỏi phỏng vấn Senior Frontend Developer** > **Độ khó:** ⭐⭐⭐⭐ (Advanced)
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
// 📦 ESLint core recommended config (Cấu hình ESLint core được khuyến nghị)
import typescript from '@typescript-eslint/eslint-plugin';
// 📦 TypeScript ESLint plugin - Rules cho TypeScript (TypeScript ESLint plugin - Rules for TypeScript)
import tsParser from '@typescript-eslint/parser';
// 📦 TypeScript parser - Parse TypeScript code (TypeScript parser - Parse TypeScript code)
import react from 'eslint-plugin-react';
// 📦 React plugin - Rules cho React (React plugin - Rules for React)
import reactHooks from 'eslint-plugin-react-hooks';
// 📦 React Hooks plugin - Rules cho React Hooks (React Hooks plugin - Rules for React Hooks)
import reactRefresh from 'eslint-plugin-react-refresh';
// 📦 React Refresh plugin - Rules cho Vite HMR (React Refresh plugin - Rules for Vite HMR)
import jsxA11y from 'eslint-plugin-jsx-a11y';
// 📦 JSX A11y plugin - Rules cho accessibility (JSX A11y plugin - Rules for accessibility)
import importPlugin from 'eslint-plugin-import';
// 📦 Import plugin - Rules cho import/export (Import plugin - Rules for import/export)
import prettier from 'eslint-plugin-prettier';
// 📦 Prettier plugin - Tích hợp Prettier với ESLint (Prettier plugin - Integrate Prettier with ESLint)

export default [
  js.configs.recommended,
  // ✅ ESLint recommended rules (cấu hình mặc định)
  // (ESLint recommended rules - default configuration)
  // 💡 Bật các rules được khuyến nghị bởi ESLint team
  // (Enable rules recommended by ESLint team)

  {
    files: ['**/*.{ts,tsx}'],
    // 📁 Apply cho file TypeScript/TSX (Apply to TypeScript/TSX files)
    // 💡 **/*.{ts,tsx}: Tất cả file .ts và .tsx trong mọi thư mục
    // (**/*.{ts,tsx}: All .ts and .tsx files in any directory)

    languageOptions: {
      // 💡 languageOptions: Cấu hình ngôn ngữ và parser (Language and parser configuration)
      parser: tsParser,
      // 🔧 Parser cho TypeScript (Parser for TypeScript)
      // 💡 tsParser: Parse TypeScript syntax (parse TypeScript syntax)

      parserOptions: {
        // 💡 parserOptions: Tùy chọn cho parser (Options for parser)
        ecmaVersion: 'latest',
        // 🆕 Sử dụng ES version mới nhất (Use latest ES version)
        // 💡 'latest': Tự động dùng ES version mới nhất (Automatically use latest ES version)

        sourceType: 'module',
        // 📦 ES Modules (ES Modules)
        // 💡 'module': Code dùng import/export (Code uses import/export)

        ecmaFeatures: {
          // 💡 ecmaFeatures: Tính năng ECMAScript bổ sung (Additional ECMAScript features)
          jsx: true,
          // ⚛️ Enable JSX parsing (Bật parse JSX)
          // 💡 Cho phép parse JSX syntax trong TypeScript files
          // (Allow parsing JSX syntax in TypeScript files)
        },
        project: './tsconfig.json',
        // 📋 TypeScript config file (TypeScript config file)
        // 💡 Đường dẫn đến tsconfig.json để type-aware linting
        // (Path to tsconfig.json for type-aware linting)
      },

      globals: {
        // 🌐 Global variables (không cần import) (Global variables - no need to import)
        // 💡 globals: Khai báo biến global có sẵn (Declare available global variables)
        window: 'readonly',
        // 🪟 Browser window object (Browser window object)
        // 💡 'readonly': Chỉ đọc, không thể gán lại (Read-only, cannot reassign)

        document: 'readonly',
        // 📄 DOM document (DOM document)
        // 💡 'readonly': Chỉ đọc (Read-only)

        navigator: 'readonly',
        // 🧭 Browser navigator (Browser navigator)
        // 💡 'readonly': Chỉ đọc (Read-only)
      },
    },

    plugins: {
      // 🔌 ESLint plugins (ESLint plugins)
      // 💡 plugins: Đăng ký các plugins để sử dụng rules (Register plugins to use rules)

      '@typescript-eslint': typescript,
      // 📘 TypeScript rules (TypeScript rules)
      // 💡 Plugin cung cấp rules cho TypeScript (Plugin provides rules for TypeScript)
      // 💡 Prefix: @typescript-eslint/rule-name (Prefix: @typescript-eslint/rule-name)

      react: react,
      // ⚛️ React rules (React rules)
      // 💡 Plugin cung cấp rules cho React (Plugin provides rules for React)
      // 💡 Prefix: react/rule-name (Prefix: react/rule-name)

      'react-hooks': reactHooks,
      // 🪝 React Hooks rules (React Hooks rules)
      // 💡 Plugin kiểm tra React Hooks best practices (Plugin checks React Hooks best practices)
      // 💡 Prefix: react-hooks/rule-name (Prefix: react-hooks/rule-name)

      'react-refresh': reactRefresh,
      // 🔄 Vite HMR rules (Vite HMR rules)
      // 💡 Plugin cho Vite Hot Module Replacement (Plugin for Vite Hot Module Replacement)
      // 💡 Đảm bảo components export đúng cách cho HMR (Ensures components export correctly for HMR)

      'jsx-a11y': jsxA11y,
      // ♿ Accessibility rules (Accessibility rules)
      // 💡 Plugin kiểm tra accessibility trong JSX (Plugin checks accessibility in JSX)
      // 💡 Prefix: jsx-a11y/rule-name (Prefix: jsx-a11y/rule-name)

      import: importPlugin,
      // 📦 Import/export rules (Import/export rules)
      // 💡 Plugin kiểm tra import/export statements (Plugin checks import/export statements)
      // 💡 Prefix: import/rule-name (Prefix: import/rule-name)

      prettier: prettier,
      // 💅 Prettier formatting (Prettier formatting)
      // 💡 Plugin tích hợp Prettier với ESLint (Plugin integrates Prettier with ESLint)
      // 💡 Prefix: prettier/prettier (Prefix: prettier/prettier)
    },

    rules: {
      // ===================================================
      // ✅ TYPESCRIPT RULES - Kiểm tra lỗi TypeScript
      // ===================================================
      '@typescript-eslint/no-unused-vars': [
        'error',
        {
          // ❌ Báo lỗi biến không dùng (Report error for unused variables)
          // 💡 'error': Báo lỗi khi có biến không sử dụng (Report error when variable is unused)
          // 💡 Array format: ['error', options] - Level và options (Array format: ['error', options] - Level and options)
          argsIgnorePattern: '^_',
          // 🚫 Ignore args bắt đầu bằng _ (Ignore args starting with _)
          // 💡 Pattern: ^_ - Regex pattern, bỏ qua parameters như _event, _props
          // (Pattern: ^_ - Regex pattern, ignore parameters like _event, _props)

          varsIgnorePattern: '^_',
          // 🚫 Ignore vars bắt đầu bằng _ (Ignore vars starting with _)
          // 💡 Bỏ qua variables như _unusedVar (Ignore variables like _unusedVar)
        },
      ],

      '@typescript-eslint/no-explicit-any': 'warn',
      // ⚠️ Cảnh báo khi dùng any (Warning when using any)
      // 💡 'warn': Cảnh báo nhưng không fail build (Warning but doesn't fail build)
      // 💡 Ngăn chặn dùng any type (khuyến khích dùng unknown) (Prevent using any type - encourage unknown)

      '@typescript-eslint/explicit-function-return-type': [
        'warn',
        {
          // 🔤 Yêu cầu khai báo return type (Require explicit return type)
          // 💡 Bắt buộc khai báo return type cho functions (Require return type for functions)
          allowExpressions: true,
          // ✅ Cho phép arrow functions không cần type (Allow arrow functions without type)
          // 💡 Cho phép: const fn = () => {} (không cần type) (Allow: const fn = () => {} - no type needed)

          allowTypedFunctionExpressions: true,
          // ✅ Cho phép typed function expressions (Allow typed function expressions)
          // 💡 Cho phép: const fn: () => void = () => {} (Allow: const fn: () => void = () => {})
        },
      ],

      '@typescript-eslint/no-floating-promises': 'error',
      // ❌ Promise phải await hoặc .catch (Promise must be awaited or .catch)
      // 💡 Bắt lỗi khi Promise không được xử lý (Catch error when Promise is not handled)
      // 💡 Ví dụ lỗi: fetch('/api') → phải: await fetch() hoặc fetch().catch()
      // (Example error: fetch('/api') → must: await fetch() or fetch().catch())

      '@typescript-eslint/await-thenable': 'error',
      // ❌ Chỉ await những gì thenable (Only await what is thenable)
      // 💡 Bắt lỗi khi await non-Promise (Catch error when awaiting non-Promise)
      // 💡 Ví dụ lỗi: await 123 → không phải Promise (Example error: await 123 → not a Promise)

      '@typescript-eslint/no-misused-promises': 'error',
      // ❌ Không dùng Promise sai cách (Don't misuse Promises)
      // 💡 Bắt lỗi khi dùng Promise trong điều kiện if/while (Catch error when using Promise in if/while)
      // 💡 Ví dụ lỗi: if (fetch('/api')) → phải: if (await fetch('/api'))
      // (Example error: if (fetch('/api')) → must: if (await fetch('/api')))

      '@typescript-eslint/strict-boolean-expressions': 'off',
      // 🔓 Cho phép truthy/falsy (Allow truthy/falsy)
      // 💡 'off': Tắt rule này (Turn off this rule)
      // 💡 Cho phép: if (value) thay vì if (value === true) (Allow: if (value) instead of if (value === true))

      // ===================================================
      // ⚛️ REACT RULES - Kiểm tra React best practices
      // ===================================================
      'react/react-in-jsx-scope': 'off',
      // 🔓 Not needed in React 17+ (auto import) (Không cần trong React 17+ - tự động import)
      // 💡 React 17+ tự động import React, không cần: import React from 'react'
      // (React 17+ automatically imports React, no need: import React from 'react')

      'react/prop-types': 'off',
      // 🔓 Using TypeScript (không cần PropTypes) (Using TypeScript - no need PropTypes)
      // 💡 TypeScript đã có type checking, không cần PropTypes (TypeScript already has type checking, no need PropTypes)

      'react/jsx-no-target-blank': 'error',
      // ❌ <a target="_blank"> phải có rel="noreferrer" (<a target="_blank"> must have rel="noreferrer")
      // 💡 Bảo mật: Ngăn window.opener access (Security: Prevent window.opener access)
      // 💡 Ví dụ lỗi: <a target="_blank"> → phải: <a target="_blank" rel="noreferrer">
      // (Example error: <a target="_blank"> → must: <a target="_blank" rel="noreferrer">)

      'react/jsx-key': [
        'error',
        {
          // ❌ Bắt buộc key khi map array (Require key when mapping array)
          // 💡 React cần key để optimize re-render (React needs key to optimize re-render)
          // 💡 Ví dụ lỗi: items.map(item => <div>{item}</div>) → phải có key
          // (Example error: items.map(item => <div>{item}</div>) → must have key)
          checkFragmentShorthand: true,
          // ✅ Check cả <> fragment (Check <> fragment too)
          // 💡 Kiểm tra key trong shorthand fragment: <>{items.map(...)}</>
          // (Check key in shorthand fragment: <>{items.map(...)}</>)
        },
      ],

      'react/no-array-index-key': 'warn',
      // ⚠️ Không dùng index làm key (Don't use index as key)
      // 💡 Warning khi dùng: items.map((item, index) => <div key={index}>)
      // (Warning when using: items.map((item, index) => <div key={index}>))
      // 💡 Nên dùng unique ID: key={item.id} (Should use unique ID: key={item.id})

      'react/no-unescaped-entities': 'warn',
      // ⚠️ Escape quotes trong JSX (Escape quotes in JSX)
      // 💡 Warning khi dùng: <div>It's me</div> → phải: <div>It&apos;s me</div>
      // (Warning when using: <div>It's me</div> → must: <div>It&apos;s me</div>)

      // ===================================================
      // 🪝 REACT HOOKS RULES - Kiểm tra Hooks (React Hooks Rules - Check Hooks)
      // ===================================================
      'react-hooks/rules-of-hooks': 'error',
      // ❌ Hooks phải gọi ở top level (Hooks must be called at top level)
      // 💡 Bắt lỗi khi hooks gọi trong if/loop/nested functions
      // (Catch error when hooks called in if/loop/nested functions)
      // 💡 Ví dụ lỗi: if (condition) { useState() } → không được
      // (Example error: if (condition) { useState() } → not allowed)

      'react-hooks/exhaustive-deps': 'warn',
      // ⚠️ Check dependencies đầy đủ (Check dependencies are complete)
      // 💡 Warning khi useEffect/useMemo/useCallback thiếu dependencies
      // (Warning when useEffect/useMemo/useCallback missing dependencies)
      // 💡 Ví dụ: useEffect(() => {}, []) → thiếu deps trong []
      // (Example: useEffect(() => {}, []) → missing deps in [])

      // ===================================================
      // ♿ ACCESSIBILITY RULES - Kiểm tra khả năng tiếp cận
      // ===================================================
      'jsx-a11y/alt-text': 'error',
      // ❌ <img> phải có alt text (<img> must have alt text)
      // 💡 Accessibility: Screen readers cần alt text (Accessibility: Screen readers need alt text)
      // 💡 Ví dụ lỗi: <img src="photo.jpg" /> → phải: <img src="photo.jpg" alt="Description" />
      // (Example error: <img src="photo.jpg" /> → must: <img src="photo.jpg" alt="Description" />)

      'jsx-a11y/anchor-is-valid': 'error',
      // ❌ <a> phải có href hợp lệ (<a> must have valid href)
      // 💡 Bắt lỗi: <a> không có href hoặc href="javascript:void(0)"
      // (Catch error: <a> without href or href="javascript:void(0)")
      // 💡 Nên dùng <button> nếu không có href (Should use <button> if no href)

      'jsx-a11y/aria-props': 'error',
      // ❌ ARIA props phải hợp lệ (ARIA props must be valid)
      // 💡 Kiểm tra ARIA attributes đúng chuẩn (Check ARIA attributes are standard)
      // 💡 Ví dụ lỗi: <div aria-invalid="maybe" /> → không hợp lệ
      // (Example error: <div aria-invalid="maybe" /> → invalid)

      'jsx-a11y/aria-role': 'error',
      // ❌ ARIA role phải đúng (ARIA role must be correct)
      // 💡 Kiểm tra role values hợp lệ (Check role values are valid)
      // 💡 Ví dụ lỗi: <div role="buttonn" /> → typo, phải là "button"
      // (Example error: <div role="buttonn" /> → typo, must be "button")

      'jsx-a11y/click-events-have-key-events': 'warn',
      // ⚠️ onClick cần onKeyDown (onClick needs onKeyDown)
      // 💡 Accessibility: Keyboard users cần keyboard events (Accessibility: Keyboard users need keyboard events)
      // 💡 Ví dụ: <div onClick={handleClick} /> → nên có onKeyDown
      // (Example: <div onClick={handleClick} /> → should have onKeyDown)

      'jsx-a11y/no-static-element-interactions': 'warn',
      // ⚠️ Div onClick cần role (Div onClick needs role)
      // 💡 Static elements (div, span) với interactions cần role
      // (Static elements (div, span) with interactions need role)
      // 💡 Ví dụ: <div onClick={...} /> → nên có role="button"
      // (Example: <div onClick={...} /> → should have role="button")

      // ===================================================
      // 📦 IMPORT RULES - Sắp xếp imports
      // ===================================================
      'import/order': [
        'error',
        {
          // ❌ Bắt buộc sắp xếp imports (Require import ordering)
          // 💡 'error': Báo lỗi nếu imports không đúng thứ tự (Report error if imports not in correct order)

          groups: [
            // 📋 Thứ tự nhóm imports (Import groups order)
            // 💡 Thứ tự các nhóm imports (Order of import groups)
            'builtin',
            // 🏗️ Node.js built-in (fs, path) (Node.js built-in modules)
            // 💡 Ví dụ: import fs from 'fs', import path from 'path'
            // (Example: import fs from 'fs', import path from 'path')

            'external',
            // 📦 npm packages (react, lodash) (npm packages)
            // 💡 Ví dụ: import React from 'react', import _ from 'lodash'
            // (Example: import React from 'react', import _ from 'lodash')

            'internal',
            // 🏠 Internal aliases (@/components) (Internal aliases)
            // 💡 Ví dụ: import Button from '@/components/Button'
            // (Example: import Button from '@/components/Button')

            'parent',
            // ⬆️ Parent imports (../) (Parent directory imports)
            // 💡 Ví dụ: import utils from '../utils'
            // (Example: import utils from '../utils')

            'sibling',
            // ➡️ Sibling imports (./) (Sibling directory imports)
            // 💡 Ví dụ: import Header from './Header'
            // (Example: import Header from './Header')

            'index',
            // 📁 Index imports (./index) (Index file imports)
            // 💡 Ví dụ: import { Button } from './index'
            // (Example: import { Button } from './index')
          ],

          pathGroups: [
            // 🎯 Custom grouping (Custom grouping)
            // 💡 Tùy chỉnh nhóm cho specific patterns (Customize groups for specific patterns)
            {
              pattern: 'react',
              // ⚛️ React luôn đầu tiên (React always first)
              // 💡 Pattern: 'react' - Match imports từ 'react' (Pattern: 'react' - Match imports from 'react')
              group: 'builtin',
              // 💡 group: 'builtin' - Xếp vào nhóm builtin (Put in builtin group)
              position: 'before',
              // 💡 position: 'before' - Đặt trước các builtin khác (Place before other builtins)
            },
            {
              pattern: '@/**',
              // 🏠 Internal paths (@/...) (Internal paths)
              // 💡 Pattern: '@/**' - Match tất cả imports từ @/ (Match all imports from @/)
              group: 'internal',
              // 💡 group: 'internal' - Xếp vào nhóm internal (Put in internal group)
            },
          ],

          pathGroupsExcludedImportTypes: ['react'],
          // 🚫 Exclude react khỏi sorting (Exclude react from sorting)
          // 💡 React không bị sắp xếp alphabet, giữ nguyên vị trí (React not alphabetized, keep position)

          'newlines-between': 'always',
          // 📏 Dòng trống giữa các nhóm (Blank lines between groups)
          // 💡 'always': Luôn có dòng trống giữa các nhóm imports (Always blank line between import groups)
          // 💡 Ví dụ: import React from 'react'\n\nimport Button from '@/components'
          // (Example: import React from 'react'\n\nimport Button from '@/components')

          alphabetize: {
            // 🔤 Sắp xếp alphabet (Alphabetize)
            // 💡 Sắp xếp imports trong cùng nhóm theo alphabet (Sort imports in same group alphabetically)
            order: 'asc',
            // ⬆️ A → Z (A → Z)
            // 💡 'asc': Tăng dần (Ascending order)

            caseInsensitive: true,
            // 🔓 Không phân biệt hoa thường (Case insensitive)
            // 💡 true: 'Button' và 'button' được xem như nhau (Button and button treated same)
          },
        },
      ],

      'import/no-duplicates': 'error',
      // ❌ Không import trùng (No duplicate imports)
      // 💡 Bắt lỗi khi import cùng module nhiều lần (Catch error when importing same module multiple times)
      // 💡 Ví dụ lỗi: import { A } from 'lib'; import { B } from 'lib' → gộp thành 1 dòng
      // (Example error: import { A } from 'lib'; import { B } from 'lib' → merge into 1 line)

      'import/no-unused-modules': 'warn',
      // ⚠️ File không được import (File not imported)
      // 💡 Warning khi có file không được import ở đâu (Warning when file not imported anywhere)
      // 💡 Có thể là dead code (Could be dead code)

      // ===================================================
      // 💅 PRETTIER INTEGRATION - Tích hợp Prettier
      // ===================================================
      'prettier/prettier': 'error', // ❌ Formatting sai theo Prettier

      // ===================================================
      // 🚀 REACT REFRESH (Vite HMR) - Hot Module Replacement
      // ===================================================
      'react-refresh/only-export-components': [
        'warn',
        {
          // ⚠️ File chỉ export components
          allowConstantExport: true, // ✅ Cho phép export const
        },
      ],
    },

    settings: {
      // ⚙️ Cấu hình bổ sung
      react: {
        version: 'detect', // 🔍 Auto detect React version
      },
      'import/resolver': {
        // 📦 Resolve TypeScript paths
        typescript: {
          project: './tsconfig.json', // 📋 TypeScript config
        },
      },
    },
  },

  {
    files: ['**/*.test.{ts,tsx}', '**/*.spec.{ts,tsx}'], // 🧪 Test files
    rules: {
      // 🔓 Relax rules cho test files
      '@typescript-eslint/no-explicit-any': 'off', // ✅ Cho phép any trong tests
      '@typescript-eslint/no-non-null-assertion': 'off', // ✅ Cho phép ! assertion
    },
  },

  {
    ignores: [
      // 🚫 Files/folders bỏ qua
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
// 💡 Custom ESLint rule: Kiểm tra tên file component phải PascalCase
// (Custom ESLint rule: Check component file name must be PascalCase)

module.exports = {
  meta: {
    // 💡 meta: Metadata của rule (Rule metadata)
    type: 'problem',
    // 💡 'problem': Rule báo lỗi (Rule reports error)
    // 💡 Các loại: 'problem' (lỗi), 'suggestion' (gợi ý), 'layout' (format)
    // (Types: 'problem' - error, 'suggestion' - suggestion, 'layout' - format)

    docs: {
      // 💡 docs: Tài liệu cho rule (Documentation for rule)
      description: 'Enforce PascalCase for React component files',
      // 📝 Mô tả rule (Rule description)
      category: 'Best Practices',
      // 📋 Category: Best Practices (Category: Best Practices)
    },
    schema: [],
    // 💡 schema: Options schema (empty = không có options)
    // (schema: Options schema - empty = no options)
  },

  create(context) {
    // 💡 create: Function tạo rule (Function to create rule)
    // 💡 context: ESLint context object (ESLint context object)
    // 💡 context.getFilename(): Lấy tên file (Get filename)
    // 💡 context.report(): Báo lỗi (Report error)

    return {
      // 💡 Return object với AST node visitors (Return object with AST node visitors)
      Program(node) {
        // 💡 Program: Root node của AST (Root node of AST)
        // 💡 node: AST node (AST node)
        const filename = context.getFilename();
        // 📁 Lấy tên file đầy đủ (Get full filename)
        // 💡 Ví dụ: '/src/components/Button.tsx' (Example: '/src/components/Button.tsx')

        const componentFilePattern = /\.tsx$/;
        // 🔍 Pattern: File kết thúc bằng .tsx (Pattern: File ending with .tsx)
        // 💡 Regex: /\.tsx$/ - Match .tsx ở cuối (Regex: /\.tsx$/ - Match .tsx at end)

        if (componentFilePattern.test(filename)) {
          // ❓ Nếu là file .tsx (If is .tsx file)
          const baseName = filename.split('/').pop().replace('.tsx', '');
          // 📝 Lấy tên file (không có path và extension)
          // (Get filename - without path and extension)
          // 💡 split('/'): Tách path thành array (Split path into array)
          // 💡 .pop(): Lấy phần tử cuối (tên file) (Get last element - filename)
          // 💡 .replace('.tsx', ''): Bỏ extension (Remove extension)
          // 💡 Ví dụ: 'Button' từ '/src/components/Button.tsx' (Example: 'Button' from '/src/components/Button.tsx')

          // Check if filename is PascalCase
          if (!/^[A-Z][a-zA-Z0-9]*$/.test(baseName)) {
            // ❓ Kiểm tra có phải PascalCase không (Check if PascalCase)
            // 💡 Regex: /^[A-Z][a-zA-Z0-9]*$/
            // 💡 ^[A-Z]: Bắt đầu bằng chữ hoa (Start with uppercase)
            // 💡 [a-zA-Z0-9]*: Theo sau là chữ và số (Followed by letters and numbers)
            // 💡 $: Kết thúc (End)
            // 💡 Ví dụ hợp lệ: Button, UserProfile, Header123 (Valid: Button, UserProfile, Header123)
            // 💡 Ví dụ không hợp lệ: button, user-profile, _Header (Invalid: button, user-profile, _Header)

            context.report({
              // 🚨 Báo lỗi (Report error)
              node,
              // 💡 node: AST node để đánh dấu lỗi (AST node to mark error)
              message: `Component file "${baseName}.tsx" should be PascalCase`,
              // 📝 Message lỗi (Error message)
              // 💡 Ví dụ: "Component file "button.tsx" should be PascalCase"
              // (Example: "Component file "button.tsx" should be PascalCase")
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
      custom: {
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
  // ✅ Basic formatting - Định dạng cơ bản (Basic formatting)

  printWidth: 100,
  // 📏 Độ rộng tối đa 1 dòng (100 ký tự) (Max line width - 100 characters)
  // 💡 Prettier sẽ wrap dòng nếu vượt quá 100 ký tự (Prettier will wrap line if exceeds 100 chars)
  // 💡 Ví dụ: Dòng dài 120 ký tự → tự động xuống dòng (Example: 120 char line → auto wrap)

  tabWidth: 2,
  // 🔢 Kích thước tab = 2 spaces (Tab size = 2 spaces)
  // 💡 Mỗi tab = 2 spaces (Each tab = 2 spaces)
  // 💡 Ví dụ: Indent 1 level = 2 spaces (Example: Indent 1 level = 2 spaces)

  useTabs: false,
  // 🚫 Dùng spaces thay vì tabs (Use spaces instead of tabs)
  // 💡 false: Dùng spaces (Use spaces)
  // 💡 true: Dùng tabs (Use tabs)
  // 💡 Spaces nhất quán hơn trên các editor (Spaces more consistent across editors)

  semi: true,
  // ✅ Thêm semicolon (;) cuối dòng (Add semicolon (;) at end of line)
  // 💡 true: const x = 1; (có semicolon) (true: const x = 1; - with semicolon)
  // 💡 false: const x = 1 (không semicolon) (false: const x = 1 - no semicolon)

  singleQuote: true,
  // '' Dùng single quotes thay vì double (Use single quotes instead of double)
  // 💡 true: const name = 'John' (single quotes) (true: const name = 'John' - single quotes)
  // 💡 false: const name = "John" (double quotes) (false: const name = "John" - double quotes)

  quoteProps: 'as-needed',
  // 🔑 Chỉ quote object keys khi cần (Only quote object keys when needed)
  // 💡 'as-needed': { name: 'John' } (không quote nếu không cần) (no quote if not needed)
  // 💡 'always': { 'name': 'John' } (luôn quote) (always quote)
  // 💡 'preserve': Giữ nguyên (Keep as is)

  // ✅ JSX formatting - Định dạng JSX (JSX formatting)

  jsxSingleQuote: false,
  // "" JSX dùng double quotes (JSX uses double quotes)
  // 💡 false: <div className="container"> (double quotes) (false: <div className="container"> - double quotes)
  // 💡 true: <div className='container'> (single quotes) (true: <div className='container'> - single quotes)

  jsxBracketSameLine: false,
  // 📐 Đóng tag JSX xuống dòng mới (Close JSX tag on new line)
  // 💡 false: <div\n> (đóng tag xuống dòng) (false: <div\n> - close tag on new line)
  // 💡 true: <div> (đóng tag cùng dòng) (true: <div> - close tag same line)

  // ✅ Trailing commas - Dấu phẩy cuối (Trailing commas)

  trailingComma: 'es5',
  // , Thêm dấu phẩy cuối (tương thích ES5) (Add trailing comma - ES5 compatible)
  // 💡 'es5': Thêm comma cho objects/arrays (ES5 compatible) (Add comma for objects/arrays - ES5 compatible)
  // 💡 'none': Không thêm comma (No trailing comma)
  // 💡 'all': Thêm comma cho tất cả (functions, etc.) (Add comma for all - functions, etc.)
  // 💡 Ví dụ: { a: 1, b: 2, } (có comma cuối) (Example: { a: 1, b: 2, } - has trailing comma)

  // ✅ Spacing - Khoảng trắng (Spacing)

  bracketSpacing: true,
  // { } Có space trong brackets (Space in brackets)
  // 💡 true: { name: 'John' } (có space) (true: { name: 'John' } - has space)
  // 💡 false: {name: 'John'} (không space) (false: {name: 'John'} - no space)

  arrowParens: 'avoid',
  // 🏹 x => x (không có parens nếu 1 param) (x => x - no parens if 1 param)
  // 💡 'avoid': x => x (không parens) (avoid: x => x - no parens)
  // 💡 'always': (x) => x (luôn parens) (always: (x) => x - always parens)

  // ✅ Line endings - Kết thúc dòng (Line endings)

  endOfLine: 'lf',
  // 🐧 Unix line endings (LF) (Unix line endings - LF)
  // 💡 'lf': \n (Unix/Linux/Mac) (LF - Unix/Linux/Mac)
  // 💡 'crlf': \r\n (Windows) (CRLF - Windows)
  // 💡 'auto': Tự động detect (Auto detect)
  // 💡 Dùng 'lf' để nhất quán trên mọi OS (Use 'lf' for consistency across OS)

  // ✅ Import sorting (with plugin) - Sắp xếp imports
  importOrder: [
    // 📋 Thứ tự imports
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
# 💡 Shebang: Chạy script bằng sh shell (Shebang: Run script with sh shell)
# 💡 #!/usr/bin/env sh: Tìm sh trong PATH và dùng để chạy script
# (#!/usr/bin/env sh: Find sh in PATH and use to run script)

. "$(dirname -- "$0")/_/husky.sh"
# 💡 Source husky.sh script (Source husky.sh script)
# 💡 $(dirname -- "$0"): Lấy thư mục chứa script hiện tại (Get directory containing current script)
# 💡 .: Source script (load functions) (Source script - load functions)
# 💡 Husky setup script (Husky setup script)

# ✅ Run lint-staged
npx lint-staged
# 🔧 Chạy lint-staged (Run lint-staged)
# 💡 lint-staged: Chạy linters cho files đã staged (Run linters for staged files)
# 💡 Chỉ check files trong git staging area (Only check files in git staging area)
# 💡 Nhanh hơn check toàn bộ codebase (Faster than checking entire codebase)

# ✅ Run type check
npm run type-check
# 🔍 Chạy type check (Run type check)
# 💡 Kiểm tra TypeScript types (Check TypeScript types)
# 💡 Ví dụ: tsc --noEmit (Example: tsc --noEmit)
# 💡 Bắt lỗi type trước khi commit (Catch type errors before commit)

# ✅ Run tests on changed files
npm run test:changed
# 🧪 Chạy tests cho files đã thay đổi (Run tests for changed files)
# 💡 Chỉ chạy tests liên quan đến files đã thay đổi (Only run tests related to changed files)
# 💡 Nhanh hơn chạy toàn bộ test suite (Faster than running entire test suite)
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
    // 💡 lint-staged: Chạy commands cho staged files (Run commands for staged files)
    // 💡 Key: File pattern (glob pattern) (Key: File pattern - glob pattern)
    // 💡 Value: Array of commands (Giá trị: Mảng các lệnh)

    "*.{ts,tsx}": [
      // 📘 TypeScript/TSX files (TypeScript/TSX files)
      // 💡 Pattern: *.{ts,tsx} - Match tất cả .ts và .tsx files (Match all .ts and .tsx files)
      // 💡 Commands chạy tuần tự (Commands run sequentially)

      "eslint --fix",
      // 🔧 Auto-fix lỗi ESLint (Auto-fix ESLint errors)
      // 💡 --fix: Tự động sửa lỗi có thể fix được (Automatically fix fixable errors)
      // 💡 Chỉ sửa lỗi auto-fixable, không sửa lỗi cần manual (Only fix auto-fixable, not manual errors)

      "prettier --write",
      // 💅 Format code (Format code)
      // 💡 --write: Ghi đè file với formatted code (Overwrite file with formatted code)
      // 💡 Format code theo .prettierrc config (Format code according to .prettierrc config)

      "vitest related --run"
      // 🧪 Chạy tests liên quan (Run related tests)
      // 💡 vitest related: Chỉ chạy tests liên quan đến staged files (Only run tests related to staged files)
      // 💡 --run: Chạy tests một lần (không watch mode) (Run tests once - not watch mode)
    ],

    "*.{js,jsx}": [
      // 📄 JavaScript/JSX files (JavaScript/JSX files)
      // 💡 Pattern: *.{js,jsx} - Match tất cả .js và .jsx files (Match all .js and .jsx files)

      "eslint --fix",
      // 🔧 Auto-fix lỗi (Auto-fix errors)
      // 💡 Tương tự như TypeScript files (Similar to TypeScript files)

      "prettier --write"
      // 💅 Format code (Format code)
      // 💡 Format JavaScript/JSX files (Format JavaScript/JSX files)
    ],

    "*.{json,md,yml,yaml}": [
      // 📝 Config/doc files (Config/doc files)
      // 💡 Pattern: *.{json,md,yml,yaml} - Match config và doc files (Match config and doc files)

      "prettier --write"
      // 💅 Format only (Chỉ format) (Format only)
      // 💡 Chỉ format, không cần lint (Only format, no lint needed)
      // 💡 JSON, Markdown, YAML chỉ cần format (JSON, Markdown, YAML only need formatting)
    ],

    "*.css": [
      // 🎨 CSS files (CSS files)
      // 💡 Pattern: *.css - Match tất cả .css files (Match all .css files)

      "prettier --write",
      // 💅 Format CSS (Format CSS)
      // 💡 Format CSS code (Format CSS code)

      "stylelint --fix"
      // 🔧 Fix CSS linting (Fix CSS linting)
      // 💡 stylelint: CSS linter (CSS linter)
      // 💡 --fix: Tự động sửa lỗi CSS (Automatically fix CSS errors)
      // 💡 Kiểm tra CSS best practices (Check CSS best practices)
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
  extends: ['@commitlint/config-conventional'],
  // 📏 Dùng conventional commits (Use conventional commits)
  // 💡 @commitlint/config-conventional: Config chuẩn cho conventional commits
  // (@commitlint/config-conventional: Standard config for conventional commits)
  // 💡 Format: type(scope): subject (Format: type(scope): subject)

  rules: {
    // 💡 rules: Quy tắc validate commit messages (Rules to validate commit messages)
    // 💡 Format: 'rule-name': [level, 'when', value] (Format: 'rule-name': [level, 'when', value])
    // 💡 level: 0 = off, 1 = warn, 2 = error (level: 0 = off, 1 = warn, 2 = error)
    // 💡 when: 'always' (luôn check), 'never' (không check) (when: 'always' - always check, 'never' - never check)

    // ✅ Type enum - Các loại commit hợp lệ (Type enum - Valid commit types)
    'type-enum': [
      2,
      // ❌ Error level (bắt buộc) (Error level - required)
      // 💡 2 = error: Bắt buộc phải đúng (2 = error: Must be correct)
      // 💡 Commit sẽ bị reject nếu type không hợp lệ (Commit will be rejected if type invalid)

      'always',
      // 🔒 Luôn check (Always check)
      // 💡 'always': Luôn validate rule này (Always validate this rule)

      [
        // 💡 Array: Danh sách types hợp lệ (Array: List of valid types)
        'feat',
        // ✨ New feature - Tính năng mới (New feature)
        // 💡 Ví dụ: feat(auth): add login functionality
        // (Example: feat(auth): add login functionality)

        'fix',
        // 🐛 Bug fix - Sửa lỗi (Bug fix)
        // 💡 Ví dụ: fix(ui): resolve button hover bug
        // (Example: fix(ui): resolve button hover bug)

        'docs',
        // 📝 Documentation - Tài liệu (Documentation)
        // 💡 Ví dụ: docs(readme): update installation guide
        // (Example: docs(readme): update installation guide)

        'style',
        // 💄 Formatting - Format code (Formatting)
        // 💡 Ví dụ: style: format code with prettier
        // (Example: style: format code with prettier)

        'refactor',
        // ♻️ Code restructuring - Tái cấu trúc (Code restructuring)
        // 💡 Ví dụ: refactor(api): simplify user service
        // (Example: refactor(api): simplify user service)

        'perf',
        // ⚡ Performance improvement - Cải thiện performance (Performance improvement)
        // 💡 Ví dụ: perf(core): optimize bundle size
        // (Example: perf(core): optimize bundle size)

        'test',
        // 🧪 Tests - Viết tests (Tests)
        // 💡 Ví dụ: test(hooks): add tests for useDebounce
        // (Example: test(hooks): add tests for useDebounce)

        'chore',
        // 🔧 Maintenance - Bảo trì (Maintenance)
        // 💡 Ví dụ: chore(deps): upgrade React to 18.3.0
        // (Example: chore(deps): upgrade React to 18.3.0)

        'ci',
        // 👷 CI/CD changes - Thay đổi CI/CD (CI/CD changes)
        // 💡 Ví dụ: ci: add GitHub Actions workflow
        // (Example: ci: add GitHub Actions workflow)

        'revert',
        // ⏪ Revert commit - Hoàn tác commit (Revert commit)
        // 💡 Ví dụ: revert: revert "feat(auth): add login"
        // (Example: revert: revert "feat(auth): add login")
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
    "name": "Main Bundle",
    // 📄 Tên bundle (Bundle name)
    // 💡 Tên hiển thị trong report (Display name in report)

    "path": "dist/assets/index-*.js",
    // 📁 Đường dẫn file (File path)
    // 💡 Pattern: index-*.js - Match files bắt đầu bằng index- (Match files starting with index-)
    // 💡 *: Wildcard - Match bất kỳ ký tự nào (Wildcard - Match any characters)
    // 💡 Ví dụ: index-abc123.js, index-def456.js (Example: index-abc123.js, index-def456.js)

    "limit": "200 KB",
    // ⚠️ Giới hạn 200 KB (Limit 200 KB)
    // 💡 Nếu bundle > 200 KB → báo lỗi (If bundle > 200 KB → report error)
    // 💡 Format: "200 KB" - String với unit (Format: "200 KB" - String with unit)

    "gzip": true,
    // 🗜️ Tính gzip size (Calculate gzip size)
    // 💡 true: Kiểm tra size sau khi gzip (Check size after gzip)
    // 💡 Gzip size thường nhỏ hơn 30-40% so với original (Gzip size usually 30-40% smaller than original)

    "webpack": false
    // 🚫 Không dùng webpack (Not using webpack)
    // 💡 false: Dùng cho Vite/Rollup (Use for Vite/Rollup)
    // 💡 true: Dùng cho webpack (Use for webpack)
  },
  {
    "name": "Vendor Bundle",
    // 📦 Bundle libraries (Bundle libraries)
    // 💡 Bundle chứa third-party libraries (Bundle containing third-party libraries)
    // 💡 Ví dụ: react, react-dom, lodash (Example: react, react-dom, lodash)

    "path": "dist/assets/vendor-*.js",
    // 📁 Pattern: vendor-*.js (Pattern: vendor-*.js)
    "limit": "150 KB",
    // ⚠️ Giới hạn 150 KB (Limit 150 KB)
    // 💡 Vendor bundle thường lớn hơn main bundle (Vendor bundle usually larger than main bundle)

    "gzip": true
    // 🗜️ Tính gzip size (Calculate gzip size)
  },
  {
    "name": "CSS Bundle",
    // 🎨 Bundle CSS (CSS Bundle)
    // 💡 Bundle chứa CSS styles (Bundle containing CSS styles)

    "path": "dist/assets/index-*.css",
    // 📁 Pattern: index-*.css (Pattern: index-*.css)
    "limit": "50 KB",
    // ⚠️ Giới hạn 50 KB (Limit 50 KB)
    // 💡 CSS bundle thường nhỏ hơn JS bundles (CSS bundle usually smaller than JS bundles)

    "gzip": true
    // 🗜️ Tính gzip size (Calculate gzip size)
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
  // 💡 defineConfig: Vite config helper (Vite config helper)
  // 💡 Type-safe config với autocomplete (Type-safe config with autocomplete)

  plugins: [
    react(),
    // ⚛️ React plugin (React plugin)
    // 💡 @vitejs/plugin-react: Hỗ trợ React trong Vite (Support React in Vite)

    // ✅ Bundle analyzer - Phân tích bundle size (Bundle analyzer - Analyze bundle size)
    visualizer({
      // 💡 rollup-plugin-visualizer: Visualize bundle size (Visualize bundle size)
      // 💡 Tạo HTML report hiển thị bundle structure (Create HTML report showing bundle structure)

      open: true,
      // 🌐 Tự động mở browser (Automatically open browser)
      // 💡 true: Tự động mở file HTML sau khi build (Automatically open HTML file after build)
      // 💡 false: Chỉ tạo file, không mở (Only create file, don't open)

      filename: 'dist/stats.html',
      // 📄 File output (Output file)
      // 💡 Đường dẫn file HTML report (Path to HTML report file)
      // 💡 Mở file này trong browser để xem bundle visualization (Open this file in browser to see bundle visualization)

      gzipSize: true,
      // 🗜️ Hiển thị gzip size (Display gzip size)
      // 💡 true: Hiển thị size sau khi gzip (Display size after gzip)
      // 💡 Giúp ước tính size thực tế khi deploy (Helps estimate actual size when deployed)

      brotliSize: true,
      // 🗜️ Hiển thị brotli size (Display brotli size)
      // 💡 true: Hiển thị size sau khi brotli compress (Display size after brotli compression)
      // 💡 Brotli nhỏ hơn gzip ~15-20% (Brotli smaller than gzip ~15-20%)

      template: 'treemap',
      // 📊 treemap, sunburst, network (kiểu hiển thị) (treemap, sunburst, network - display type)
      // 💡 'treemap': Hiển thị dạng treemap (phổ biến nhất) (Display as treemap - most common)
      // 💡 'sunburst': Hiển thị dạng sunburst (circular) (Display as sunburst - circular)
      // 💡 'network': Hiển thị dạng network graph (Display as network graph)
    }),
  ],

  build: {
    // 💡 build: Cấu hình build (Build configuration)

    rollupOptions: {
      // 💡 rollupOptions: Tùy chọn cho Rollup (Options for Rollup)
      // 💡 Vite dùng Rollup để bundle (Vite uses Rollup to bundle)

      output: {
        // 💡 output: Cấu hình output (Output configuration)

        manualChunks: {
          // 📦 Chia nhỏ chunks thủ công (Manually split chunks)
          // 💡 Chia bundle thành nhiều chunks nhỏ hơn (Split bundle into smaller chunks)
          // 💡 Giúp code splitting và lazy loading (Helps code splitting and lazy loading)

          // ✅ Split vendor chunks - Tách riêng vendors (Split vendor chunks - Separate vendors)
          vendor: ['react', 'react-dom'],
          // ⚛️ React core (React core)
          // 💡 Tách react và react-dom thành vendor chunk riêng (Separate react and react-dom into vendor chunk)
          // 💡 Vendor chunk ít thay đổi → cache tốt hơn (Vendor chunk changes less → better caching)

          router: ['react-router-dom'],
          // 🛤️ Router (Router)
          // 💡 Tách router thành chunk riêng (Separate router into own chunk)
          // 💡 Chỉ load khi cần routing (Only load when routing needed)

          ui: ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
          // 🎨 UI libs (UI libraries)
          // 💡 Tách UI libraries thành chunk riêng (Separate UI libraries into own chunk)
          // 💡 Lazy load UI components khi cần (Lazy load UI components when needed)
        },
      },
    },

    // ✅ Report compressed size - Báo cáo size nén (Report compressed size)
    reportCompressedSize: true,
    // 📊 Hiển thị gzip size khi build (Display gzip size when building)
    // 💡 true: Hiển thị cả original size và gzip size (Display both original and gzip size)
    // 💡 Giúp theo dõi bundle size thực tế (Helps track actual bundle size)

    // ✅ Chunk size warning limit - Cảnh báo chunk quá lớn (Chunk size warning limit)
    chunkSizeWarningLimit: 500,
    // ⚠️ Cảnh báo nếu > 500 KB (Warning if > 500 KB)
    // 💡 Nếu chunk > 500 KB → Vite hiển warning (If chunk > 500 KB → Vite shows warning)
    // 💡 Giúp phát hiện bundle bloat sớm (Helps detect bundle bloat early)
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
