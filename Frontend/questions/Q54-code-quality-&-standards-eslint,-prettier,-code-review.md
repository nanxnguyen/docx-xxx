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
  js.configs.recommended,
  
  {
    files: ['**/*.{ts,tsx}'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: {
          jsx: true,
        },
        project: './tsconfig.json',
      },
      globals: {
        window: 'readonly',
        document: 'readonly',
        navigator: 'readonly',
      },
    },
    
    plugins: {
      '@typescript-eslint': typescript,
      'react': react,
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      'jsx-a11y': jsxA11y,
      'import': importPlugin,
      'prettier': prettier,
    },
    
    rules: {
      // ===================================================
      // ✅ TYPESCRIPT RULES
      // ===================================================
      '@typescript-eslint/no-unused-vars': ['error', {
        argsIgnorePattern: '^_',
        varsIgnorePattern: '^_',
      }],
      '@typescript-eslint/no-explicit-any': 'warn',
      '@typescript-eslint/explicit-function-return-type': ['warn', {
        allowExpressions: true,
        allowTypedFunctionExpressions: true,
      }],
      '@typescript-eslint/no-floating-promises': 'error',
      '@typescript-eslint/await-thenable': 'error',
      '@typescript-eslint/no-misused-promises': 'error',
      '@typescript-eslint/strict-boolean-expressions': 'off',
      
      // ===================================================
      // ⚛️ REACT RULES
      // ===================================================
      'react/react-in-jsx-scope': 'off', // Not needed in React 17+
      'react/prop-types': 'off', // Using TypeScript
      'react/jsx-no-target-blank': 'error',
      'react/jsx-key': ['error', {
        checkFragmentShorthand: true,
      }],
      'react/no-array-index-key': 'warn',
      'react/no-unescaped-entities': 'warn',
      
      // ===================================================
      // 🪝 REACT HOOKS RULES
      // ===================================================
      'react-hooks/rules-of-hooks': 'error',
      'react-hooks/exhaustive-deps': 'warn',
      
      // ===================================================
      // ♿ ACCESSIBILITY RULES
      // ===================================================
      'jsx-a11y/alt-text': 'error',
      'jsx-a11y/anchor-is-valid': 'error',
      'jsx-a11y/aria-props': 'error',
      'jsx-a11y/aria-role': 'error',
      'jsx-a11y/click-events-have-key-events': 'warn',
      'jsx-a11y/no-static-element-interactions': 'warn',
      
      // ===================================================
      // 📦 IMPORT RULES
      // ===================================================
      'import/order': ['error', {
        groups: [
          'builtin',
          'external',
          'internal',
          'parent',
          'sibling',
          'index',
        ],
        pathGroups: [
          {
            pattern: 'react',
            group: 'builtin',
            position: 'before',
          },
          {
            pattern: '@/**',
            group: 'internal',
          },
        ],
        pathGroupsExcludedImportTypes: ['react'],
        'newlines-between': 'always',
        alphabetize: {
          order: 'asc',
          caseInsensitive: true,
        },
      }],
      'import/no-duplicates': 'error',
      'import/no-unused-modules': 'warn',
      
      // ===================================================
      // 💅 PRETTIER INTEGRATION
      // ===================================================
      'prettier/prettier': 'error',
      
      // ===================================================
      // 🚀 REACT REFRESH (Vite HMR)
      // ===================================================
      'react-refresh/only-export-components': ['warn', {
        allowConstantExport: true,
      }],
    },
    
    settings: {
      react: {
        version: 'detect',
      },
      'import/resolver': {
        typescript: {
          project: './tsconfig.json',
        },
      },
    },
  },
  
  {
    files: ['**/*.test.{ts,tsx}', '**/*.spec.{ts,tsx}'],
    rules: {
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/no-non-null-assertion': 'off',
    },
  },
  
  {
    ignores: [
      'dist/',
      'build/',
      'coverage/',
      'node_modules/',
      '*.config.js',
      '*.config.ts',
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
// 💅 **.PRETTIERRC.MJS**
// ===================================================

export default {
  // ✅ Basic formatting
  printWidth: 100,
  tabWidth: 2,
  useTabs: false,
  semi: true,
  singleQuote: true,
  quoteProps: 'as-needed',
  
  // ✅ JSX formatting
  jsxSingleQuote: false,
  jsxBracketSameLine: false,
  
  // ✅ Trailing commas
  trailingComma: 'es5',
  
  // ✅ Spacing
  bracketSpacing: true,
  arrowParens: 'avoid',
  
  // ✅ Line endings
  endOfLine: 'lf',
  
  // ✅ Import sorting (with plugin)
  importOrder: [
    '^react',
    '^@?\\w',
    '^@/(.*)$',
    '^[./]',
  ],
  importOrderSeparation: true,
  importOrderSortSpecifiers: true,
  
  // ✅ Plugins
  plugins: [
    '@trivago/prettier-plugin-sort-imports',
    'prettier-plugin-tailwindcss',
  ],
  
  // ✅ File-specific overrides
  overrides: [
    {
      files: '*.json',
      options: {
        printWidth: 80,
      },
    },
    {
      files: '*.md',
      options: {
        proseWrap: 'always',
      },
    },
  ],
};
```

```json
// ===================================================
// 🚫 **.PRETTIERIGNORE**
// ===================================================

# Build outputs
dist/
build/
coverage/

# Dependencies
node_modules/

# Logs
*.log

# Auto-generated files
*.generated.ts
*.d.ts

# Config files
pnpm-lock.yaml
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
# 🚀 **.husky/pre-push**
# ===================================================

#!/usr/bin/env sh
. "$(dirname -- "$0")/_/husky.sh"

# ✅ Run full test suite
npm run test

# ✅ Build check
npm run build

# ✅ Bundle size check
npm run size-limit
```

### **3.2. Lint-Staged Configuration**

```json
// ===================================================
// 🎯 **LINT-STAGED** (package.json)
// ===================================================

{
  "lint-staged": {
    "*.{ts,tsx}": [
      "eslint --fix",
      "prettier --write",
      "vitest related --run"
    ],
    "*.{js,jsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{json,md,yml,yaml}": [
      "prettier --write"
    ],
    "*.css": [
      "prettier --write",
      "stylelint --fix"
    ]
  }
}
```

---

## 4. Commitlint & Conventional Commits

### **4.1. Commitlint Setup**

```javascript
// ===================================================
// 📋 **COMMITLINT.CONFIG.MJS**
// ===================================================

export default {
  extends: ['@commitlint/config-conventional'],
  
  rules: {
    // ✅ Type enum
    'type-enum': [
      2,
      'always',
      [
        'feat',     // New feature
        'fix',      // Bug fix
        'docs',     // Documentation
        'style',    // Formatting
        'refactor', // Code restructuring
        'perf',     // Performance improvement
        'test',     // Tests
        'chore',    // Maintenance
        'ci',       // CI/CD changes
        'revert',   // Revert commit
      ],
    ],
    
    // ✅ Subject rules
    'subject-case': [2, 'never', ['upper-case']],
    'subject-empty': [2, 'never'],
    'subject-full-stop': [2, 'never', '.'],
    'subject-max-length': [2, 'always', 100],
    
    // ✅ Body rules
    'body-leading-blank': [2, 'always'],
    'body-max-line-length': [2, 'always', 100],
    
    // ✅ Footer rules
    'footer-leading-blank': [2, 'always'],
    
    // ✅ Scope enum (optional)
    'scope-enum': [
      1,
      'always',
      [
        'core',
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
# ✅ **VALID COMMIT MESSAGES**
# ===================================================

feat(auth): add OAuth2 login support
fix(ui): resolve button hover state bug
docs(readme): update installation instructions
refactor(api): simplify user service logic
perf(core): optimize bundle size with code splitting
test(hooks): add tests for useDebounce
chore(deps): upgrade React to 18.3.0

# ❌ **INVALID COMMIT MESSAGES**
# ===================================================

Fixed bug              # Missing type
FEAT: new feature      # Wrong case
feat add feature       # Missing colon
feat: Add new feature. # Full stop at end
```

---

## 5. SonarQube Integration

### **5.1. SonarQube Setup**

```yaml
# ===================================================
# 📊 **SONARQUBE WORKFLOW** (.github/workflows/sonar.yml)
# ===================================================

name: SonarQube Analysis

on:
  push:
    branches: [main, develop]
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  sonar:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # Full history for better analysis
      
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      
      - run: npm ci
      - run: npm run test:coverage
      
      - name: SonarQube Scan
        uses: SonarSource/sonarqube-scan-action@master
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
          SONAR_HOST_URL: ${{ secrets.SONAR_HOST_URL }}
      
      - name: SonarQube Quality Gate
        uses: SonarSource/sonarqube-quality-gate-action@master
        timeout-minutes: 5
        env:
          SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
```

```properties
# ===================================================
# ⚙️ **SONAR-PROJECT.PROPERTIES**
# ===================================================

sonar.projectKey=my-frontend-app
sonar.organization=my-org

# ✅ Source configuration
sonar.sources=src
sonar.tests=src
sonar.test.inclusions=**/*.test.ts,**/*.test.tsx,**/*.spec.ts,**/*.spec.tsx
sonar.exclusions=**/node_modules/**,**/dist/**,**/coverage/**

# ✅ Coverage report
sonar.javascript.lcov.reportPaths=coverage/lcov.info
sonar.testExecutionReportPaths=coverage/test-report.xml

# ✅ Code quality settings
sonar.sourceEncoding=UTF-8
sonar.javascript.node.maxspace=4096

# ✅ Quality gates
sonar.qualitygate.wait=true
sonar.qualitygate.timeout=300
```

---

## 6. Bundle Analysis

### **6.1. Bundle Size Monitoring**

```json
// ===================================================
// 📦 **SIZE-LIMIT** (.size-limit.json)
// ===================================================

[
  {
    "name": "Main Bundle",
    "path": "dist/assets/index-*.js",
    "limit": "200 KB",
    "gzip": true,
    "webpack": false
  },
  {
    "name": "Vendor Bundle",
    "path": "dist/assets/vendor-*.js",
    "limit": "150 KB",
    "gzip": true
  },
  {
    "name": "CSS Bundle",
    "path": "dist/assets/index-*.css",
    "limit": "50 KB",
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
    react(),
    
    // ✅ Bundle analyzer
    visualizer({
      open: true,
      filename: 'dist/stats.html',
      gzipSize: true,
      brotliSize: true,
      template: 'treemap', // sunburst, treemap, network
    }),
  ],
  
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          // ✅ Split vendor chunks
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom'],
          ui: ['@radix-ui/react-dialog', '@radix-ui/react-dropdown-menu'],
        },
      },
    },
    
    // ✅ Report compressed size
    reportCompressedSize: true,
    
    // ✅ Chunk size warning limit
    chunkSizeWarningLimit: 500,
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
