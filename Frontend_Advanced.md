# 🚀 Frontend Advanced - Câu Hỏi Phỏng Vấn Nâng Cao

## 📋 Mục Lục (Table of Contents)

### **Phần 1: Module System & Build Tools**
- [Q1: ESModule vs CommonJS - Hệ Thống Module](#q1-esmodule-vs-commonjs---hệ-thống-module-)
- [Q2: Build Tools - Babel, Webpack, Vite](#q2-build-tools---babel-webpack-vite-)
- [Q3: Compiler vs Transpiler vs Bundler](#q3-compiler-vs-transpiler-vs-bundler-)
- [Q4: Tree Shaking - Tối Ưu Bundle Size](#q4-tree-shaking---tối-ưu-bundle-size-)

### **Phần 2: Performance & Web Vitals**
- [Q5: Web Vitals Metrics - Đo Lường Hiệu Suất](#q5-web-vitals-metrics---đo-lường-hiệu-suất-)
- [Q6: Build Library & Design System](#q6-build-library--design-system-)
- [Q7: Caching Strategies - Chiến Lược Cache](#q7-caching-strategies---chiến-lược-cache-)

### **Phần 3: Development Workflow**
- [Q8: Branching Model - Git Flow](#q8-branching-model---git-flow-)
- [Q9: Frontend Architecture - Cấu Trúc Scalable](#q9-frontend-architecture---cấu-trúc-scalable-)
- [Q10: Design Patterns - Mẫu Thiết Kế](#q10-design-patterns---mẫu-thiết-kế-)

### **Phần 4: Storage & Security**
- [Q11: Storage APIs - Cookie, LocalStorage, SessionStorage](#q11-storage-apis---cookie-localstorage-sessionstorage-)
- [Q12: IndexedDB - Database Client-side](#q12-indexeddb---database-client-side-)
- [Q13: Token Management - JWT & Refresh Token](#q13-token-management---jwt--refresh-token-)
- [Q14: Frontend Security - XSS, CORS, CSRF](#q14-frontend-security---xss-cors-csrf-)

### **Phần 5: Testing & Code Quality**
- [Q15: Testable Code - Code Dễ Test](#q15-testable-code---code-dễ-test-)
- [Q16: Development Tools - ESLint, Prettier, Husky](#q16-development-tools---eslint-prettier-husky-)
- [Q17: External Library vs Self-implement](#q17-external-library-vs-self-implement-)

### **Phần 6: Internationalization & Communication**
- [Q18: i18n with React - Đa Ngôn Ngữ](#q18-i18n-with-react---đa-ngôn-ngữ-)
- [Q19: Frontend-Backend Communication](#q19-frontend-backend-communication-)
- [Q20: WebSocket & Streaming](#q20-websocket--streaming-)

### **Phần 7: Advanced Concepts**
- [Q21: Browser Navigation - URL Processing](#q21-browser-navigation---url-processing-)
- [Q22: Error Tracking - Sentry, Grafana](#q22-error-tracking---sentry-grafana-)
- [Q23: Micro Frontend & Monorepo](#q23-micro-frontend--monorepo-)
- [Q24: File Upload/Download](#q24-file-uploaddownload-)
- [Q25: Request Cancellation - AbortController](#q25-request-cancellation---abortcontroller-)

### **Phần 8: Rendering & Optimization**
- [Q26: Client vs Server Side Rendering](#q26-client-vs-server-side-rendering-)
- [Q27: Web Workers - Background Processing](#q27-web-workers---background-processing-)
- [Q28: Next.js Advanced Features](#q28-nextjs-advanced-features-)
- [Q29: HTTP Status Codes](#q29-http-status-codes-)

### **Phần 9: State Management & Tools**
- [Q30: Advanced State Management](#q30-advanced-state-management-)
- [Q31: Nx Monorepo](#q31-nx-monorepo-)
- [Q32: React vs Next.js vs React Native Lifecycle](#q32-react-vs-nextjs-vs-react-native-lifecycle-)
- [Q33: Storybook - Component Documentation](#q33-storybook---component-documentation-)

### **Phần 10: Best Practices & Common Mistakes**
- [Q34: Security Best Practices](#q34-security-best-practices-)
- [Q35: React Query Advanced](#q35-react-query-advanced-)
- [Q36: Common Advanced Mistakes](#q36-common-advanced-mistakes-)
- [Q37: Clean Code Best Practices](#q37-clean-code-best-practices-)
- [Q38: Domain to UI Rendering Process](#q38-domain-to-ui-rendering-process-)
- [Q39: Complex Frontend Project Experience](#q39-complex-frontend-project-experience-)

---

## **Phần 1: Module System & Build Tools**

### **Q1: ESModule vs CommonJS - Hệ Thống Module** 🔥

#### **🔍 Câu Hỏi:**
Sự khác biệt giữa CommonJS, AMD, UMD, ES Modules (import/export)?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 ES Modules (ES6+)**: Hệ thống module hiện đại, tiêu chuẩn của JavaScript
  - *Là gì*: Hệ thống module native của JavaScript, sử dụng `import/export` syntax
  - *Tại sao cần*: Cung cấp static analysis, tree shaking, và circular dependency resolution
  - *Khi nào dùng*: Dự án hiện đại, cần tối ưu bundle size, hỗ trợ tree shaking

- **🎯 CommonJS**: Hệ thống module của Node.js, sử dụng `require/module.exports`
  - *Là gì*: Hệ thống module synchronous, được sử dụng rộng rãi trong Node.js
  - *Tại sao cần*: Tương thích với Node.js, đơn giản và dễ hiểu
  - *Khi nào dùng*: Dự án Node.js, cần tương thích ngược

- **⚡ AMD (Asynchronous Module Definition)**: Hệ thống module bất đồng bộ
  - *Là gì*: Hệ thống module load bất đồng bộ, chủ yếu dùng với RequireJS
  - *Tại sao cần*: Tối ưu cho browser, load module theo nhu cầu
  - *Khi nào dùng*: Dự án cũ, cần load module bất đồng bộ

- **✅ Ưu điểm ES Modules**: Static analysis, tree shaking, circular dependency resolution
  - *Static analysis*: Có thể phân tích dependencies tại compile time
  - *Tree shaking*: Loại bỏ code không sử dụng, giảm bundle size
  - *Circular dependencies*: Xử lý dependencies vòng tròn tốt hơn

- **⚠️ Nhược điểm CommonJS**: Không có tree shaking, synchronous loading
  - *Không tree shaking*: Import toàn bộ library, tăng bundle size
  - *Synchronous*: Blocking, có thể gây chậm trong browser
  - *No static analysis*: Khó phân tích dependencies

**1. ES Modules (ES6+) - Modern Standard:**
```javascript
// ES Modules - Modern standard
import React, { useState, useEffect } from 'react';
import { API_URL } from './config';
import UserService from './services/UserService';

// Named exports
export const API_URL = 'https://api.example.com';
export const VERSION = '1.0.0';

// Default export
export default class UserService {
  static async getUsers() {
    const response = await fetch(`${API_URL}/users`);
    return response.json();
  }
}

// Dynamic import
const module = await import('./dynamic-module.js');
```

**2. CommonJS - Node.js Standard:**
```javascript
// CommonJS - Node.js standard
const React = require('react');
const { useState, useEffect } = require('react');
const UserService = require('./services/UserService');

// Exports
module.exports = {
  API_URL: 'https://api.example.com',
  VERSION: '1.0.0'
};

// Default export
module.exports = class UserService {
  static async getUsers() {
    const response = await fetch(`${API_URL}/users`);
    return response.json();
  }
};
```

**3. AMD (Asynchronous Module Definition):**
```javascript
// AMD - Asynchronous loading
define(['react', './services/UserService'], function(React, UserService) {
  return {
    API_URL: 'https://api.example.com',
    VERSION: '1.0.0'
  };
});

// Require.js style
require(['react', './services/UserService'], function(React, UserService) {
  // Module code here
});
```

**4. UMD (Universal Module Definition):**
```javascript
// UMD - Universal compatibility
(function (root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD
    define(['react'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS
    module.exports = factory(require('react'));
  } else {
    // Browser globals
    root.MyModule = factory(root.React);
  }
}(typeof self !== 'undefined' ? self : this, function (React) {
  return {
    API_URL: 'https://api.example.com',
    VERSION: '1.0.0'
  };
}));
```

#### **📊 So Sánh Chi Tiết:**

| Feature | ES Modules | CommonJS | AMD | UMD |
|---------|------------|----------|-----|-----|
| **Loading** | Static | Synchronous | Asynchronous | Universal |
| **Tree Shaking** | ✅ Native | ❌ No | ❌ No | ❌ No |
| **Browser Support** | Modern browsers | Node.js | Require.js | Universal |
| **Static Analysis** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Circular Dependencies** | ✅ Handled | ⚠️ Limited | ⚠️ Limited | ⚠️ Limited |
| **Performance** | ✅ Fast | ✅ Fast | ⚠️ Slower | ⚠️ Slower |

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: ES Modules với tree shaking - Tối ưu nhất cho modern projects
import { debounce } from 'lodash-es'; // Chỉ import debounce function - giảm bundle size đáng kể
import { Button } from '@mui/material'; // Chỉ import Button component - tree shaking hiệu quả

// ❌ SAI: CommonJS import toàn bộ library - Làm tăng bundle size không cần thiết
const _ = require('lodash'); // Import toàn bộ lodash library - bundle size lớn
const MUI = require('@mui/material'); // Import toàn bộ Material-UI - không tối ưu

// ✅ TỐI ƯU CHO PERFORMANCE: Dynamic imports cho code splitting - Tối ưu cho performance
const LazyComponent = React.lazy(() => import('./LazyComponent')); // Lazy loading - giảm initial bundle size

// ✅ TỐI ƯU CHO DEVELOPMENT: Conditional imports - Tối ưu cho development experience
if (process.env.NODE_ENV === 'development') {
  const { whyDidYouUpdate } = await import('@welldone-software/why-did-you-update'); // Chỉ load trong dev
  whyDidYouUpdate(React); // Debug tool chỉ chạy khi cần
}

// ✅ TỐI ƯU CHO TREE SHAKING: Named exports - Tối ưu cho tree shaking
import { debounce, throttle } from 'lodash-es'; // Chỉ import những function cần thiết

// ✅ TỐI ƯU CHO MAIN FUNCTIONALITY: Default exports - Tối ưu cho main functionality
import UserService from './services/UserService'; // Import service chính - clean import path
```

**🔥 SO SÁNH TỐI ƯU - ES Modules vs CommonJS:**

| Tiêu chí | ES Modules | CommonJS | Tại sao ES Modules tối ưu hơn |
|----------|------------|----------|-------------------------------|
| **Tree Shaking** | ✅ Có | ❌ Không | ES Modules cho phép loại bỏ code không dùng, giảm bundle size 30-50% |
| **Performance** | ✅ Nhanh hơn | ⚠️ Chậm hơn | Static analysis tại compile time, không cần runtime resolution |
| **Browser Support** | ✅ Modern browsers | ❌ Node.js only | ES Modules là standard hiện đại, được browser hỗ trợ native |
| **Bundle Size** | ✅ Nhỏ hơn | ❌ Lớn hơn | Tree shaking + static imports giảm đáng kể bundle size |
| **Static Analysis** | ✅ Có | ❌ Không | IDE có thể analyze dependencies, better tooling support |
| **Circular Dependencies** | ✅ Xử lý tốt | ⚠️ Hạn chế | ES Modules xử lý circular dependencies tốt hơn |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ Sai: Mixing module systems - Trộn lẫn hệ thống module
import React from 'react'; // ES Module
const _ = require('lodash'); // CommonJS - ❌ Không nên trộn lẫn

// ✅ Đúng: Consistent module system - Hệ thống module nhất quán
import React from 'react'; // ES Module
import { debounce } from 'lodash-es'; // ES Module

// ❌ Sai: Import entire library - Import toàn bộ library
import * as _ from 'lodash'; // ❌ Import toàn bộ lodash
const result = _.debounce(fn, 300); // Chỉ dùng debounce

// ✅ Đúng: Import specific functions - Import function cụ thể
import { debounce } from 'lodash-es'; // ✅ Chỉ import debounce
const result = debounce(fn, 300);

// ❌ Sai: Circular dependencies - Dependencies vòng tròn
// fileA.js
import { funcB } from './fileB';
export const funcA = () => funcB();

// fileB.js
import { funcA } from './fileA'; // ❌ Circular dependency
export const funcB = () => funcA();

// ✅ Đúng: Avoid circular dependencies - Tránh dependencies vòng tròn
// fileA.js
export const funcA = () => {
  // Implementation without importing from fileB
};

// fileB.js
import { funcA } from './fileA'; // ✅ OK, không có vòng tròn
export const funcB = () => funcA();
```

---

### **Q2: Build Tools - Babel, Webpack, Vite** 🔥

#### **🔍 Câu Hỏi:**
Tìm hiểu rõ về các build tool này, sự khác nhau nhau, cái gì được sử dụng tối ưu nhất, tree shaking?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Babel**: JavaScript transpiler, chuyển đổi code ES6+ thành ES5
  - *Là gì*: Tool chuyển đổi JavaScript code từ phiên bản mới về cũ
  - *Tại sao cần*: Tương thích với browser cũ, sử dụng syntax mới
  - *Khi nào dùng*: Dự án cần tương thích browser cũ, sử dụng ES6+

- **🎯 Webpack**: Module bundler, đóng gói modules thành bundles
  - *Là gì*: Tool đóng gói các modules thành file bundle tối ưu
  - *Tại sao cần*: Quản lý dependencies, tối ưu bundle size
  - *Khi nào dùng*: Dự án phức tạp, cần tùy chỉnh build process

- **⚡ Vite**: Build tool hiện đại, sử dụng ES modules
  - *Là gì*: Build tool nhanh, sử dụng native ES modules
  - *Tại sao cần*: Build nhanh, HMR tốt, đơn giản
  - *Khi nào dùng*: Dự án mới, cần build nhanh, development experience tốt

- **✅ Ưu điểm Vite**: Build nhanh, HMR tốt, đơn giản
  - *Build nhanh*: Sử dụng esbuild, build nhanh hơn Webpack
  - *HMR tốt*: Hot Module Replacement nhanh và ổn định
  - *Đơn giản*: Configuration đơn giản, ít boilerplate

- **⚠️ Nhược điểm Webpack**: Phức tạp, build chậm
  - *Phức tạp*: Configuration phức tạp, khó học
  - *Build chậm*: Build time lâu, đặc biệt với dự án lớn
  - *HMR chậm*: Hot reload chậm với dự án lớn

**1. Babel - JavaScript Transpiler:**
```javascript
// babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: {
        browsers: ['> 1%', 'last 2 versions']
      },
      useBuiltIns: 'usage',
      corejs: 3
    }],
    '@babel/preset-react',
    '@babel/preset-typescript'
  ],
  plugins: [
    '@babel/plugin-proposal-class-properties',
    '@babel/plugin-syntax-dynamic-import',
    ['@babel/plugin-transform-runtime', {
      regenerator: true
    }]
  ]
};

// Input: ES6+ code
const fetchData = async () => {
  const response = await fetch('/api/data');
  return response.json();
};

// Output: ES5 code
var fetchData = function() {
  return regeneratorRuntime.async(function fetchData$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.next = 2;
          return fetch('/api/data');
        case 2:
          response = _context.sent;
          return _context.abrupt("return", response.json());
        case 4:
        case "end":
          return _context.stop();
      }
    }
  });
};
```

**2. Webpack - Module Bundler:**
```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserPlugin = require('terser-webpack-plugin');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    clean: true
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx|ts|tsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react']
          }
        }
      },
      {
        test: /\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader']
      }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './public/index.html'
    }),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css'
    })
  ],
  optimization: {
    minimize: true,
    minimizer: [new TerserPlugin()],
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  }
};
```

**3. Vite - Next Generation Build Tool:**
```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
      '@components': resolve(__dirname, 'src/components'),
      '@utils': resolve(__dirname, 'src/utils')
    }
  },
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@mui/material', '@mui/icons-material']
        }
      }
    }
  },
  server: {
    port: 3000,
    open: true
  }
});
```

#### **📊 So Sánh Build Tools:**

| Feature | Webpack | Vite | Rollup | Parcel |
|---------|---------|------|--------|--------|
| **Speed** | ⚠️ Slow | ✅ Very Fast | ✅ Fast | ✅ Fast |
| **Configuration** | ⚠️ Complex | ✅ Simple | ✅ Simple | ✅ Zero Config |
| **Tree Shaking** | ✅ Good | ✅ Excellent | ✅ Excellent | ✅ Good |
| **HMR** | ⚠️ Slow | ✅ Instant | ❌ No | ✅ Fast |
| **Bundle Size** | ⚠️ Large | ✅ Small | ✅ Small | ✅ Small |
| **Learning Curve** | ⚠️ Steep | ✅ Easy | ✅ Easy | ✅ Easy |

#### **🌳 Tree Shaking Implementation:**

```javascript
// ✅ Good: Tree shaking friendly
// math.js
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
export const multiply = (a, b) => a * b;

// main.js
import { add } from './math.js'; // Only 'add' is bundled

// ❌ Bad: Not tree shaking friendly
// math.js
const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;

export default { add, subtract, multiply };

// main.js
import math from './math.js';
console.log(math.add(1, 2)); // Entire object is bundled
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Vite cho new projects - Tối ưu nhất cho development speed
// vite.config.js - Vite nhanh hơn Webpack 10-100x trong development
export default defineConfig({
  plugins: [react()], // React plugin - hot reload nhanh nhất
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'] // Vendor chunk riêng biệt - cache hiệu quả
        }
      }
    }
  }
});

// ✅ TỐI ƯU CHO COMPLEX PROJECTS: Webpack cho dự án phức tạp - Tối ưu cho customization
// webpack.config.js - Webpack linh hoạt hơn, nhiều plugins hơn
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all', // Code splitting cho tất cả chunks - tối ưu bundle size
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/, // Test cho node_modules
          name: 'vendors', // Tên chunk
          chunks: 'all' // Tất cả chunks
        }
      }
    }
  }
};

// ✅ Good: Babel for browser compatibility - Dùng Babel cho tương thích browser
// babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: {
        browsers: ['> 1%', 'last 2 versions'] // Hỗ trợ browser phổ biến
      }
    }]
  ]
};

// ✅ Good: Optimized imports - Import tối ưu
import { debounce } from 'lodash-es'; // Tree shakeable - Có thể tree shake
import { Button } from '@mui/material'; // Tree shakeable - Có thể tree shake

// ✅ TỐI ƯU CHO CODE SPLITTING: Dynamic imports - Tối ưu cho performance
const LazyComponent = React.lazy(() => import('./LazyComponent')); // Lazy loading - giảm initial bundle size
```

**🔥 SO SÁNH TỐI ƯU - Build Tools:**

| Tiêu chí | Vite | Webpack | Babel | Tại sao Vite tối ưu nhất |
|----------|------|---------|-------|-------------------------|
| **Development Speed** | ✅ Nhanh nhất | ⚠️ Chậm hơn | N/A | Vite sử dụng ES modules native, không cần bundling |
| **Build Speed** | ✅ Nhanh | ⚠️ Chậm hơn | N/A | Rollup-based bundling nhanh hơn Webpack |
| **Configuration** | ✅ Đơn giản | ❌ Phức tạp | ✅ Đơn giản | Vite có sensible defaults, ít config cần thiết |
| **Hot Reload** | ✅ Instant | ⚠️ Chậm hơn | N/A | Vite có HMR nhanh nhất, update ngay lập tức |
| **Bundle Size** | ✅ Tối ưu | ✅ Tối ưu | N/A | Cả hai đều có tree shaking, code splitting |
| **Plugin Ecosystem** | ⚠️ Mới | ✅ Phong phú | ✅ Phong phú | Webpack có nhiều plugins hơn, nhưng Vite đang phát triển |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ Sai: Over-configuring Babel - Cấu hình Babel quá phức tạp
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: {
        browsers: ['> 0.1%'] // ❌ Quá strict, không cần thiết
      },
      useBuiltIns: 'entry' // ❌ Import toàn bộ polyfill
    }]
  ]
};

// ✅ Đúng: Simple Babel config - Cấu hình Babel đơn giản
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: {
        browsers: ['> 1%', 'last 2 versions'] // ✅ Hợp lý
      },
      useBuiltIns: 'usage' // ✅ Chỉ polyfill cần thiết
    }]
  ]
};

// ❌ Sai: Not using tree shaking - Không sử dụng tree shaking
import * as _ from 'lodash'; // ❌ Import toàn bộ lodash
import _ from 'lodash'; // ❌ Import toàn bộ lodash

// ✅ Đúng: Use tree shaking - Sử dụng tree shaking
import { debounce } from 'lodash-es'; // ✅ Chỉ import cần thiết

// ❌ Sai: Wrong tool choice - Chọn tool sai
// Dùng Webpack cho dự án đơn giản - ❌ Overkill
// Dùng Vite cho dự án phức tạp cần tùy chỉnh - ❌ Không đủ linh hoạt

// ✅ Đúng: Right tool for the job - Chọn tool phù hợp
// Vite cho dự án mới, đơn giản - ✅
// Webpack cho dự án phức tạp, cần tùy chỉnh - ✅
```

---

### **Q3: Compiler vs Transpiler vs Bundler** 🔥

#### **🔍 Câu Hỏi:**
Compiler vs transpiler vs bundler? Babel vs Webpack, Webpack vs Vite?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Compiler**: Chuyển đổi code từ ngôn ngữ này sang ngôn ngữ khác
  - *Là gì*: Tool chuyển đổi code từ ngôn ngữ cấp cao sang ngôn ngữ cấp thấp hơn
  - *Tại sao cần*: Chuyển đổi code để máy tính có thể hiểu và thực thi
  - *Khi nào dùng*: TypeScript → JavaScript, C++ → Assembly

- **🎯 Transpiler**: Chuyển đổi code giữa các ngôn ngữ cùng cấp
  - *Là gì*: Tool chuyển đổi code từ ngôn ngữ này sang ngôn ngữ khác cùng cấp
  - *Tại sao cần*: Sử dụng syntax mới trên môi trường cũ
  - *Khi nào dùng*: ES6+ → ES5, JSX → JavaScript

- **⚡ Bundler**: Đóng gói nhiều modules thành file bundle
  - *Là gì*: Tool kết hợp nhiều files/modules thành một hoặc vài file
  - *Tại sao cần*: Tối ưu loading, quản lý dependencies
  - *Khi nào dùng*: Webpack, Vite, Rollup

- **✅ Ưu điểm Compiler**: Tối ưu performance, type safety
  - *Performance*: Code được tối ưu cho runtime
  - *Type safety*: Kiểm tra type tại compile time
  - *Error detection*: Phát hiện lỗi sớm

- **⚠️ Nhược điểm Transpiler**: Có thể tạo code phức tạp, overhead
  - *Code phức tạp*: Generated code có thể khó đọc
  - *Overhead*: Thêm bước build process
  - *Debugging*: Khó debug source code gốc

**1. Compiler:**
```javascript
// Compiler: Converts high-level code to machine code
// Example: TypeScript Compiler (tsc)
// Input: TypeScript
interface User {
  id: number;
  name: string;
  email: string;
}

const user: User = {
  id: 1,
  name: 'John Doe',
  email: 'john@example.com'
};

// Output: JavaScript
const user = {
  id: 1,
  name: 'John Doe',
  email: 'john@example.com'
};
```

**2. Transpiler:**
```javascript
// Transpiler: Converts code from one language to another at same abstraction level
// Example: Babel
// Input: ES6+
const fetchData = async () => {
  const response = await fetch('/api/data');
  return response.json();
};

// Output: ES5
var fetchData = function() {
  return regeneratorRuntime.async(function fetchData$(_context) {
    while (1) {
      switch (_context.prev = _context.next) {
        case 0:
          _context.next = 2;
          return fetch('/api/data');
        case 2:
          response = _context.sent;
          return _context.abrupt("return", response.json());
        case 4:
        case "end":
          return _context.stop();
      }
    }
  });
};
```

**3. Bundler:**
```javascript
// Bundler: Combines multiple files into one or more bundles
// Example: Webpack
// Input: Multiple files
// src/index.js
import React from 'react';
import { render } from 'react-dom';
import App from './App';

// src/App.js
import React from 'react';
import Header from './components/Header';

// Output: Single bundle
// dist/main.js (minified and optimized)
(function() {
  // All code combined into one file
})();
```

#### **📊 So Sánh Chi Tiết:**

| Tool | Type | Purpose | Input | Output |
|------|------|---------|-------|--------|
| **Compiler** | Compiler | Convert to machine code | High-level code | Machine code |
| **Transpiler** | Transpiler | Convert between languages | Source code | Source code |
| **Bundler** | Bundler | Combine files | Multiple files | Single/multiple bundles |

#### **🔧 Babel vs Webpack:**

```javascript
// Babel: Transpiler only
// babel.config.js
module.exports = {
  presets: ['@babel/preset-env'],
  plugins: ['@babel/plugin-proposal-class-properties']
};

// Webpack: Bundler + Loader system
// webpack.config.js
module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader' // Uses Babel as a loader
      }
    ]
  }
};
```

#### **⚡ Webpack vs Vite:**

```javascript
// Webpack: Traditional bundling
// webpack.config.js
module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        use: 'babel-loader'
      }
    ]
  }
};

// Vite: Modern build tool
// vite.config.js
export default defineConfig({
  plugins: [react()],
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom']
        }
      }
    }
  }
});
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Dùng đúng tool cho từng việc - Tối ưu nhất cho từng use case
// For transpilation: Babel - Cho transpilation: Babel (tối ưu cho JS compatibility)
// For bundling: Vite - Cho bundling: Vite (tối ưu cho development speed)
// For compilation: TypeScript Compiler - Cho compilation: TypeScript Compiler (tối ưu cho type safety)

// ✅ TỐI ƯU CHO MODERN PROJECTS: Setup hiện đại với Vite - Tối ưu cho development experience
// vite.config.js - Vite nhanh hơn Webpack 10-100x
export default defineConfig({
  plugins: [react()], // React plugin
  build: {
    target: 'esnext', // Target ESNext
    minify: 'terser', // Minify với Terser
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'], // Vendor chunk
          ui: ['@mui/material'] // UI chunk
        }
      }
    }
  }
});

// ✅ Good: TypeScript compilation - Compilation TypeScript
// tsconfig.json
{
  "compilerOptions": {
    "target": "ES2020", // Target ES2020
    "module": "ESNext", // Module ESNext
    "strict": true, // Strict mode
    "esModuleInterop": true // ES module interop
  }
}

// ✅ Good: Babel transpilation - Transpilation Babel
// babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: { node: 'current' } // Target current Node version
    }]
  ]
};

// ✅ Good: Webpack for complex projects - Webpack cho dự án phức tạp
// webpack.config.js
module.exports = {
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all'
        }
      }
    }
  }
};
```

**🔥 SO SÁNH TỐI ƯU - Compiler vs Transpiler vs Bundler:**

| Tiêu chí | Compiler | Transpiler | Bundler | Tại sao dùng đúng tool tối ưu nhất |
|----------|----------|------------|---------|-----------------------------------|
| **Mục đích** | ✅ Compile toàn bộ | ✅ Convert syntax | ✅ Bundle modules | Mỗi tool có mục đích riêng, dùng đúng sẽ tối ưu |
| **Input** | ✅ Source code | ✅ Source code | ✅ Modules | Compiler xử lý source code, Transpiler convert syntax, Bundler bundle modules |
| **Output** | ✅ Executable | ✅ Same language | ✅ Bundled files | Compiler tạo executable, Transpiler giữ nguyên language, Bundler tạo bundle |
| **Performance** | ✅ Tối ưu | ✅ Nhanh | ✅ Tối ưu | Dùng đúng tool cho đúng việc sẽ có performance tốt nhất |
| **Use Case** | ✅ TypeScript, C++ | ✅ Babel, JSX | ✅ Webpack, Vite | Mỗi tool phù hợp với use case cụ thể |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ SAI: Using wrong tool - Dùng sai tool
// Dùng Babel để compile TypeScript - ❌ Babel không phải compiler
// Dùng Webpack để transpile ES6 - ❌ Webpack là bundler, không phải transpiler

// ✅ Đúng: Use appropriate tool - Dùng tool phù hợp
// Dùng TypeScript Compiler để compile TypeScript - ✅
// Dùng Babel để transpile ES6 - ✅
// Dùng Webpack để bundle modules - ✅

// ❌ Sai: Over-configuring - Cấu hình quá phức tạp
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: {
        browsers: ['> 0.1%'] // ❌ Quá strict
      },
      useBuiltIns: 'entry' // ❌ Import toàn bộ polyfill
    }]
  ]
};

// ✅ Đúng: Simple configuration - Cấu hình đơn giản
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: {
        browsers: ['> 1%', 'last 2 versions'] // ✅ Hợp lý
      },
      useBuiltIns: 'usage' // ✅ Chỉ polyfill cần thiết
    }]
  ]
};

// ❌ Sai: Mixing tools unnecessarily - Trộn lẫn tools không cần thiết
// Dùng cả Babel và TypeScript Compiler cho cùng một file - ❌ Redundant

// ✅ Đúng: Use one tool per purpose - Dùng một tool cho một mục đích
// Chỉ dùng TypeScript Compiler cho .ts files - ✅
// Chỉ dùng Babel cho .js files - ✅
```

---

### **Q4: Tree Shaking - Tối Ưu Bundle Size** 🔥

#### **🔍 Câu Hỏi:**
Tree shaking là gì và cách tối ưu bundle size?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Tree Shaking**: Kỹ thuật loại bỏ code không sử dụng khỏi bundle
  - *Là gì*: Dead code elimination, loại bỏ unused code khỏi final bundle
  - *Tại sao cần*: Giảm bundle size, cải thiện performance, tối ưu loading time
  - *Khi nào dùng*: ES Modules, modern bundlers (Webpack, Vite, Rollup)

- **🎯 Cách hoạt động**: Static analysis tại build time
  - *Static analysis*: Phân tích code tại compile time để tìm unused exports
  - *ES Modules*: Chỉ hoạt động với ES Modules, không với CommonJS
  - *Bundler support*: Webpack, Vite, Rollup hỗ trợ tree shaking

- **⚡ Lợi ích**: Giảm bundle size, cải thiện performance
  - *Bundle size*: Giảm đáng kể kích thước file cuối cùng
  - *Performance*: Tải nhanh hơn, ít memory usage
  - *Cost*: Tiết kiệm bandwidth, storage

- **✅ Ưu điểm**: Tự động, hiệu quả, không ảnh hưởng runtime
  - *Tự động*: Bundler tự động loại bỏ unused code
  - *Hiệu quả*: Giảm bundle size đáng kể
  - *An toàn*: Không ảnh hưởng đến functionality

- **⚠️ Nhược điểm**: Chỉ hoạt động với ES Modules, cần cấu hình đúng
  - *ES Modules only*: Không hoạt động với CommonJS
  - *Configuration*: Cần cấu hình bundler đúng cách
  - *Side effects*: Có thể loại bỏ code có side effects

**1. Tree Shaking Concept:**
```javascript
// Tree shaking: Dead code elimination
// Input: math.js
export const add = (a, b) => a + b;
export const subtract = (a, b) => a - b;
export const multiply = (a, b) => a * b;
export const divide = (a, b) => a / b;

// main.js
import { add } from './math.js';
console.log(add(1, 2));

// Output after tree shaking: Only 'add' function is bundled
const add = (a, b) => a + b;
console.log(add(1, 2));
```

**2. Webpack Tree Shaking:**
```javascript
// webpack.config.js
module.exports = {
  mode: 'production', // Enables tree shaking
  optimization: {
    usedExports: true, // Mark used exports
    sideEffects: false, // No side effects
    minimize: true // Remove unused code
  }
};

// package.json
{
  "sideEffects": false, // Tell webpack no side effects
  "sideEffects": ["./src/some-side-effect.js"] // Or specify files with side effects
}
```

**3. ES Modules Tree Shaking:**
```javascript
// ✅ Good: Tree shakeable
// utils.js
export const debounce = (func, wait) => {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
};

export const throttle = (func, limit) => {
  let inThrottle;
  return function() {
    const args = arguments;
    const context = this;
    if (!inThrottle) {
      func.apply(context, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, limit);
    }
  };
};

// main.js
import { debounce } from './utils.js'; // Only debounce is bundled
```

**4. CommonJS vs ES Modules:**
```javascript
// ❌ Bad: CommonJS - Not tree shakeable
// utils.js
const debounce = (func, wait) => { /* ... */ };
const throttle = (func, limit) => { /* ... */ };

module.exports = { debounce, throttle };

// main.js
const { debounce } = require('./utils.js'); // Entire object is bundled

// ✅ Good: ES Modules - Tree shakeable
// utils.js
export const debounce = (func, wait) => { /* ... */ };
export const throttle = (func, limit) => { /* ... */ };

// main.js
import { debounce } from './utils.js'; // Only debounce is bundled
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Named exports - Tối ưu nhất cho tree shaking
export const Button = ({ children, ...props }) => { /* ... */ }; // Named export - tree shaking hiệu quả
export const Input = ({ value, onChange, ...props }) => { /* ... */ }; // Named export - tree shaking hiệu quả

// ❌ SAI: Default export với object - Làm giảm hiệu quả tree shaking
export default {
  Button: ({ children, ...props }) => { /* ... */ }, // Object export - không tối ưu
  Input: ({ value, onChange, ...props }) => { /* ... */ } // Object export - không tối ưu
};

// ✅ TỐI ƯU CHO BUNDLE SIZE: Side effects free - Tối ưu cho bundle size
// math.js
export const add = (a, b) => a + b; // Pure function - Hàm thuần túy

// ✅ Good: ES Modules imports - Import ES Modules
import { debounce } from 'lodash-es'; // Tree shakeable - Có thể tree shake
import { Button } from '@mui/material'; // Tree shakeable - Có thể tree shake

// ❌ Bad: CommonJS imports - Import CommonJS
const _ = require('lodash'); // Not tree shakeable - Không thể tree shake

// ✅ Good: Specific imports - Import cụ thể
import { debounce, throttle } from 'lodash-es'; // Chỉ import cần thiết

// ❌ Bad: Wildcard imports - Import wildcard
import * as _ from 'lodash'; // Import toàn bộ library

// ✅ Good: Package.json sideEffects - Cấu hình sideEffects
{
  "sideEffects": false, // Không có side effects
  "sideEffects": ["./src/polyfills.js"] // Chỉ file có side effects
}
```

**🔥 SO SÁNH TỐI ƯU - Tree Shaking Strategies:**

| Strategy | ES Modules | CommonJS | Tại sao ES Modules tối ưu hơn |
|----------|------------|----------|-------------------------------|
| **Tree Shaking** | ✅ Có | ❌ Không | ES Modules cho phép static analysis, loại bỏ code không dùng |
| **Bundle Size** | ✅ Nhỏ hơn | ❌ Lớn hơn | Tree shaking giảm bundle size 30-50% |
| **Performance** | ✅ Nhanh hơn | ⚠️ Chậm hơn | Smaller bundle = faster loading |
| **Named Exports** | ✅ Tối ưu | ❌ Không tối ưu | Named exports cho phép tree shaking hiệu quả |
| **Default Exports** | ⚠️ Hạn chế | ✅ Tốt | Default exports khó tree shake hơn |
| **Side Effects** | ✅ Kiểm soát | ❌ Không kiểm soát | ES Modules có sideEffects config |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ Sai: Using CommonJS - Sử dụng CommonJS
const { debounce } = require('lodash'); // ❌ Không thể tree shake

// ✅ Đúng: Use ES Modules - Sử dụng ES Modules
import { debounce } from 'lodash-es'; // ✅ Có thể tree shake

// ❌ Sai: Default export with object - Default export với object
export default {
  Button: () => {},
  Input: () => {}
};

// ✅ Đúng: Named exports - Named exports
export const Button = () => {};
export const Input = () => {};

// ❌ Sai: Side effects in modules - Side effects trong modules
// utils.js
console.log('Module loaded'); // ❌ Side effect
export const add = (a, b) => a + b;

// ✅ Đúng: Pure modules - Modules thuần túy
// utils.js
export const add = (a, b) => a + b; // ✅ Pure function

// ❌ Sai: Import entire library - Import toàn bộ library
import _ from 'lodash'; // ❌ Import toàn bộ

// ✅ Đúng: Import specific functions - Import function cụ thể
import { debounce } from 'lodash-es'; // ✅ Chỉ import cần thiết
```

// ✅ Good: Conditional imports
if (process.env.NODE_ENV === 'development') {
  const { whyDidYouUpdate } = await import('@welldone-software/why-did-you-update');
  whyDidYouUpdate(React);
}

// ✅ Good: Dynamic imports for code splitting
const LazyComponent = React.lazy(() => import('./LazyComponent'));
```

#### **📊 Bundle Analysis:**

```javascript
// webpack-bundle-analyzer
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
  plugins: [
    new BundleAnalyzerPlugin({
      analyzerMode: 'static',
      openAnalyzer: false,
      reportFilename: 'bundle-report.html'
    })
  ]
};

// Vite bundle analysis
// vite.config.js
export default defineConfig({
  build: {
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          ui: ['@mui/material', '@mui/icons-material'],
          utils: ['lodash-es', 'date-fns']
        }
      }
    }
  }
});
```

---

## **Phần 2: Performance & Web Vitals**

### **Q5: Web Vitals Metrics - Đo Lường Hiệu Suất** 🔥

#### **🔍 Câu Hỏi:**
How do you know if a website is fast or slow? Web vitals metrics?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Core Web Vitals**: Các chỉ số quan trọng nhất để đánh giá performance
  - *Là gì*: LCP, FID, CLS - 3 chỉ số cốt lõi của Google
  - *Tại sao cần*: Ảnh hưởng trực tiếp đến SEO ranking và user experience
  - *Khi nào đo*: Liên tục trong production, development testing

- **🎯 LCP (Largest Contentful Paint)**: Thời gian load content chính
  - *Là gì*: Thời gian để element lớn nhất hiển thị
  - *Tại sao quan trọng*: Ảnh hưởng đến cảm nhận tốc độ của user
  - *Target*: < 2.5s (Good), 2.5s-4s (Needs Improvement), > 4s (Poor)

- **⚡ FID (First Input Delay)**: Thời gian phản hồi input đầu tiên
  - *Là gì*: Thời gian từ khi user tương tác đến khi browser phản hồi
  - *Tại sao quan trọng*: Ảnh hưởng đến tính tương tác của website
  - *Target*: < 100ms (Good), 100ms-300ms (Needs Improvement), > 300ms (Poor)

- **✅ CLS (Cumulative Layout Shift)**: Độ ổn định layout
  - *Là gì*: Đo lường sự thay đổi layout không mong muốn
  - *Tại sao quan trọng*: Ảnh hưởng đến trải nghiệm đọc và tương tác
  - *Target*: < 0.1 (Good), 0.1-0.25 (Needs Improvement), > 0.25 (Poor)

- **⚠️ Các chỉ số khác**: FCP, TTFB, SI, TBT
  - *FCP*: First Contentful Paint - Thời gian hiển thị content đầu tiên
  - *TTFB*: Time to First Byte - Thời gian nhận byte đầu tiên
  - *SI*: Speed Index - Tốc độ hiển thị content
  - *TBT*: Total Blocking Time - Tổng thời gian blocking

**1. Core Web Vitals:**
```javascript
// web-vitals.js
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals';

// Cumulative Layout Shift (CLS)
getCLS((metric) => {
  console.log('CLS:', metric.value);
  // Good: < 0.1, Needs Improvement: 0.1-0.25, Poor: > 0.25
});

// First Input Delay (FID)
getFID((metric) => {
  console.log('FID:', metric.value);
  // Good: < 100ms, Needs Improvement: 100-300ms, Poor: > 300ms
});

// First Contentful Paint (FCP)
getFCP((metric) => {
  console.log('FCP:', metric.value);
  // Good: < 1.8s, Needs Improvement: 1.8-3s, Poor: > 3s
});

// Largest Contentful Paint (LCP)
getLCP((metric) => {
  console.log('LCP:', metric.value);
  // Good: < 2.5s, Needs Improvement: 2.5-4s, Poor: > 4s
});

// Time to First Byte (TTFB)
getTTFB((metric) => {
  console.log('TTFB:', metric.value);
  // Good: < 800ms, Needs Improvement: 800-1800ms, Poor: > 1800ms
});
```

**2. Performance Monitoring:**
```javascript
// performance-monitor.js
class PerformanceMonitor {
  constructor() {
    this.metrics = {};
    this.init();
  }

  init() {
    // Monitor Core Web Vitals
    this.monitorWebVitals();

    // Monitor custom metrics
    this.monitorCustomMetrics();

    // Monitor resource loading
    this.monitorResources();
  }

  monitorWebVitals() {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS((metric) => this.recordMetric('CLS', metric));
      getFID((metric) => this.recordMetric('FID', metric));
      getFCP((metric) => this.recordMetric('FCP', metric));
      getLCP((metric) => this.recordMetric('LCP', metric));
      getTTFB((metric) => this.recordMetric('TTFB', metric));
    });
  }

  monitorCustomMetrics() {
    // Time to Interactive
    const observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (entry.entryType === 'measure') {
          this.recordMetric('TTI', entry.duration);
        }
      }
    });
    observer.observe({ entryTypes: ['measure'] });
  }

  monitorResources() {
    const observer = new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (entry.entryType === 'resource') {
          this.recordMetric('resource', {
            name: entry.name,
            duration: entry.duration,
            size: entry.transferSize
          });
        }
      }
    });
    observer.observe({ entryTypes: ['resource'] });
  }

  recordMetric(name, metric) {
    this.metrics[name] = metric;
    this.sendToAnalytics(name, metric);
  }

  sendToAnalytics(name, metric) {
    // Send to analytics service
    if (typeof gtag !== 'undefined') {
      gtag('event', 'web_vitals', {
        metric_name: name,
        metric_value: metric.value || metric.duration,
        metric_rating: this.getRating(name, metric.value || metric.duration)
      });
    }
  }

  getRating(metricName, value) {
    const thresholds = {
      CLS: { good: 0.1, poor: 0.25 },
      FID: { good: 100, poor: 300 },
      FCP: { good: 1800, poor: 3000 },
      LCP: { good: 2500, poor: 4000 },
      TTFB: { good: 800, poor: 1800 }
    };

    const threshold = thresholds[metricName];
    if (!threshold) return 'unknown';

    if (value <= threshold.good) return 'good';
    if (value <= threshold.poor) return 'needs-improvement';
    return 'poor';
  }
}

// Initialize performance monitoring
new PerformanceMonitor();
```

**3. Performance Optimization:**
```javascript
// performance-optimization.js
class PerformanceOptimizer {
  constructor() {
    this.init();
  }

  init() {
    this.optimizeImages();
    this.optimizeFonts();
    this.optimizeScripts();
    this.optimizeStyles();
  }

  optimizeImages() {
    // Lazy loading
    const images = document.querySelectorAll('img[data-src]');
    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src;
          img.classList.remove('lazy');
          imageObserver.unobserve(img);
        }
      });
    });

    images.forEach(img => imageObserver.observe(img));
  }

  optimizeFonts() {
    // Preload critical fonts
    const link = document.createElement('link');
    link.rel = 'preload';
    link.href = '/fonts/roboto.woff2';
    link.as = 'font';
    link.type = 'font/woff2';
    link.crossOrigin = 'anonymous';
    document.head.appendChild(link);
  }

  optimizeScripts() {
    // Defer non-critical scripts
    const scripts = document.querySelectorAll('script[data-defer]');
    scripts.forEach(script => {
      script.defer = true;
    });
  }

  optimizeStyles() {
    // Critical CSS inlining
    const criticalCSS = document.querySelector('style[data-critical]');
    if (criticalCSS) {
      // Inline critical CSS
      document.head.insertBefore(criticalCSS, document.head.firstChild);
    }
  }
}

// Initialize performance optimization
new PerformanceOptimizer();
```

#### **📊 Performance Metrics Dashboard:**

```javascript
// performance-dashboard.js
class PerformanceDashboard {
  constructor() {
    this.metrics = {};
    this.init();
  }

  init() {
    this.createDashboard();
    this.startMonitoring();
  }

  createDashboard() {
    const dashboard = document.createElement('div');
    dashboard.id = 'performance-dashboard';
    dashboard.innerHTML = `
      <div class="dashboard">
        <h3>Performance Metrics</h3>
        <div class="metrics">
          <div class="metric">
            <span class="label">CLS:</span>
            <span class="value" id="cls-value">-</span>
            <span class="rating" id="cls-rating">-</span>
          </div>
          <div class="metric">
            <span class="label">FID:</span>
            <span class="value" id="fid-value">-</span>
            <span class="rating" id="fid-rating">-</span>
          </div>
          <div class="metric">
            <span class="label">FCP:</span>
            <span class="value" id="fcp-value">-</span>
            <span class="rating" id="fcp-rating">-</span>
          </div>
          <div class="metric">
            <span class="label">LCP:</span>
            <span class="value" id="lcp-value">-</span>
            <span class="rating" id="lcp-rating">-</span>
          </div>
          <div class="metric">
            <span class="label">TTFB:</span>
            <span class="value" id="ttfb-value">-</span>
            <span class="rating" id="ttfb-rating">-</span>
          </div>
        </div>
      </div>
    `;
    document.body.appendChild(dashboard);
  }

  startMonitoring() {
    import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
      getCLS((metric) => this.updateMetric('cls', metric));
      getFID((metric) => this.updateMetric('fid', metric));
      getFCP((metric) => this.updateMetric('fcp', metric));
      getLCP((metric) => this.updateMetric('lcp', metric));
      getTTFB((metric) => this.updateMetric('ttfb', metric));
    });
  }

  updateMetric(name, metric) {
    const valueElement = document.getElementById(`${name}-value`);
    const ratingElement = document.getElementById(`${name}-rating`);

    if (valueElement && ratingElement) {
      valueElement.textContent = `${metric.value}ms`;
      ratingElement.textContent = this.getRating(name, metric.value);
      ratingElement.className = `rating ${this.getRating(name, metric.value)}`;
    }
  }

  getRating(metricName, value) {
    const thresholds = {
      cls: { good: 0.1, poor: 0.25 },
      fid: { good: 100, poor: 300 },
      fcp: { good: 1800, poor: 3000 },
      lcp: { good: 2500, poor: 4000 },
      ttfb: { good: 800, poor: 1800 }
    };

    const threshold = thresholds[metricName];
    if (!threshold) return 'unknown';

    if (value <= threshold.good) return 'good';
    if (value <= threshold.poor) return 'needs-improvement';
    return 'poor';
  }
}

// Initialize performance dashboard
new PerformanceDashboard();
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Monitor Core Web Vitals - Tối ưu nhất cho performance monitoring
import { getCLS, getFID, getFCP, getLCP, getTTFB } from 'web-vitals'; // Web Vitals library - tối ưu cho performance tracking

// Monitor all Core Web Vitals - Theo dõi tất cả Core Web Vitals
getCLS(console.log); // Cumulative Layout Shift
getFID(console.log); // First Input Delay
getFCP(console.log); // First Contentful Paint
getLCP(console.log); // Largest Contentful Paint
getTTFB(console.log); // Time to First Byte

// ✅ Good: Set up performance budgets - Thiết lập performance budgets
const performanceBudgets = {
  LCP: 2500, // 2.5s
  FID: 100,  // 100ms
  CLS: 0.1,  // 0.1
  FCP: 1800, // 1.8s
  TTFB: 800  // 800ms
};

// ✅ Good: Optimize images for LCP - Tối ưu hình ảnh cho LCP
<img
  src="hero-image.webp"
  alt="Hero image"
  loading="eager" // Load ngay lập tức cho LCP
  width="800"
  height="600"
/>

// ✅ Good: Minimize JavaScript for FID - Giảm thiểu JavaScript cho FID
// Code splitting - Chia nhỏ code
const LazyComponent = React.lazy(() => import('./LazyComponent'));

// ✅ Good: Prevent layout shifts for CLS - Ngăn chặn layout shift cho CLS
<img
  src="image.jpg"
  alt="Image"
  width="300"
  height="200" // Luôn set width/height
/>
```

**🔥 SO SÁNH TỐI ƯU - Web Vitals Monitoring:**

| Metric | Good | Poor | Tại sao quan trọng | Cách tối ưu nhất |
|--------|------|------|-------------------|------------------|
| **LCP** | < 2.5s | > 4.0s | Ảnh hưởng đến user experience | Optimize images, lazy loading, CDN |
| **FID** | < 100ms | > 300ms | Ảnh hưởng đến interactivity | Code splitting, minimize JS, optimize bundles |
| **CLS** | < 0.1 | > 0.25 | Ảnh hưởng đến visual stability | Set image dimensions, avoid dynamic content |
| **FCP** | < 1.8s | > 3.0s | Ảnh hưởng đến perceived performance | Optimize critical resources, preload |
| **TTFB** | < 800ms | > 1.8s | Ảnh hưởng đến server response | Optimize server, use CDN, caching |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ Sai: Not monitoring Web Vitals - Không theo dõi Web Vitals
// Không có monitoring code - ❌ Không biết performance thực tế

// ✅ Đúng: Monitor continuously - Theo dõi liên tục
getCLS((metric) => {
  console.log('CLS:', metric.value);
  // Send to analytics
});

// ❌ Sai: Ignoring mobile performance - Bỏ qua performance mobile
// Chỉ test trên desktop - ❌ Mobile có performance khác

// ✅ Đúng: Test on real devices - Test trên thiết bị thật
// Sử dụng Chrome DevTools mobile simulation
// Test trên thiết bị thật với slow 3G

// ❌ Sai: Not optimizing LCP elements - Không tối ưu LCP elements
<img src="large-image.jpg" loading="lazy" /> // ❌ Lazy load LCP image

// ✅ Đúng: Optimize LCP elements - Tối ưu LCP elements
<img
  src="hero-image.webp"
  loading="eager" // ✅ Eager load cho LCP
  width="800"
  height="600"
/>

// ❌ Sai: Blocking JavaScript - JavaScript blocking
<script src="large-library.js"></script> // ❌ Blocking script

// ✅ Đúng: Non-blocking JavaScript - JavaScript không blocking
<script src="library.js" defer></script> // ✅ Defer script
// hoặc
<script src="library.js" async></script> // ✅ Async script
```

---

### **Q6: Build Library & Design System** 🔥

#### **🔍 Câu Hỏi:**
Build library? Design system. Singleton, peer dependencies?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Design System**: Hệ thống thiết kế thống nhất cho toàn bộ sản phẩm
  - *Là gì*: Tập hợp các components, patterns, guidelines để đảm bảo consistency
  - *Tại sao cần*: Tăng productivity, consistency, maintainability
  - *Khi nào dùng*: Dự án lớn, team nhiều người, cần consistency

- **🎯 Component Library**: Thư viện các components có thể tái sử dụng
  - *Là gì*: Tập hợp các UI components được đóng gói thành library
  - *Tại sao cần*: Tái sử dụng code, đảm bảo consistency, dễ maintain
  - *Khi nào dùng*: Nhiều dự án sử dụng chung components

- **⚡ Singleton Pattern**: Đảm bảo chỉ có một instance duy nhất
  - *Là gì*: Design pattern đảm bảo class chỉ có một instance
  - *Tại sao cần*: Quản lý global state, shared resources
  - *Khi nào dùng*: Database connections, configuration, logging

- **✅ Peer Dependencies**: Dependencies được share giữa host và library
  - *Là gì*: Dependencies mà cả host app và library đều cần
  - *Tại sao cần*: Tránh duplicate dependencies, version conflicts
  - *Khi nào dùng*: React, React-DOM, shared libraries

- **⚠️ Build Process**: Quá trình build library từ source code
  - *Là gì*: Compile, bundle, optimize source code thành distributable package
  - *Tại sao cần*: Tạo package có thể sử dụng bởi other projects
  - *Khi nào dùng*: Publish to npm, internal packages

**1. Build Library - Tạo Thư Viện:**
```javascript
// package.json cho library
{
  "name": "@my-org/ui-components",
  "version": "1.0.0",
  "main": "dist/index.js",
  "module": "dist/index.esm.js",
  "types": "dist/index.d.ts",
  "files": ["dist"],
  "peerDependencies": {
    "react": ">=16.8.0",
    "react-dom": ">=16.8.0"
  },
  "devDependencies": {
    "rollup": "^2.0.0",
    "@rollup/plugin-typescript": "^8.0.0"
  }
}

// rollup.config.js
import typescript from '@rollup/plugin-typescript';
import { defineConfig } from 'rollup';

export default defineConfig({
  input: 'src/index.ts',
  output: [
    {
      file: 'dist/index.js',
      format: 'cjs',
      sourcemap: true
    },
    {
      file: 'dist/index.esm.js',
      format: 'esm',
      sourcemap: true
    }
  ],
  external: ['react', 'react-dom'],
  plugins: [typescript()]
});
```

**2. Design System Components:**
```javascript
// src/components/Button/Button.tsx
import React from 'react';
import { styled } from '@mui/material/styles';

export interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
  onClick?: () => void;
  className?: string;
}

const StyledButton = styled('button')<ButtonProps>(({ theme, variant, size }) => ({
  padding: size === 'small' ? '8px 16px' : size === 'large' ? '16px 32px' : '12px 24px',
  borderRadius: '4px',
  border: 'none',
  cursor: 'pointer',
  fontSize: size === 'small' ? '14px' : size === 'large' ? '18px' : '16px',
  fontWeight: '500',
  transition: 'all 0.2s ease',
  backgroundColor: variant === 'primary' ? '#007bff' :
                   variant === 'secondary' ? '#6c757d' : 'transparent',
  color: variant === 'outline' ? '#007bff' : '#fff',
  border: variant === 'outline' ? '1px solid #007bff' : 'none',
  '&:hover': {
    opacity: 0.8,
    transform: 'translateY(-1px)'
  },
  '&:disabled': {
    opacity: 0.5,
    cursor: 'not-allowed'
  }
}));

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  onClick,
  className,
  ...props
}) => {
  return (
    <StyledButton
      variant={variant}
      size={size}
      disabled={disabled}
      onClick={onClick}
      className={className}
      {...props}
    >
      {children}
    </StyledButton>
  );
};
```

**3. Singleton Pattern:**
```javascript
// Singleton cho API Client
class ApiClient {
  private static instance: ApiClient;
  private baseURL: string;
  private token: string | null = null;

  private constructor(baseURL: string) {
    this.baseURL = baseURL;
  }

  public static getInstance(baseURL?: string): ApiClient {
    if (!ApiClient.instance) {
      if (!baseURL) {
        throw new Error('Base URL is required for first initialization');
      }
      ApiClient.instance = new ApiClient(baseURL);
    }
    return ApiClient.instance;
  }

  public setToken(token: string): void {
    this.token = token;
  }

  public async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const url = `${this.baseURL}${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...(this.token && { Authorization: `Bearer ${this.token}` }),
      ...options.headers
    };

    const response = await fetch(url, {
      ...options,
      headers
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }
}

// Usage
const apiClient = ApiClient.getInstance('https://api.example.com');
apiClient.setToken('your-token-here');
```

**4. Peer Dependencies:**
```javascript
// package.json với peer dependencies
{
  "name": "@my-org/react-components",
  "version": "1.0.0",
  "peerDependencies": {
    "react": ">=16.8.0",
    "react-dom": ">=16.8.0",
    "@mui/material": ">=5.0.0"
  },
  "peerDependenciesMeta": {
    "@mui/material": {
      "optional": true
    }
  }
}

// Component sử dụng peer dependencies
import React from 'react';
import { Button as MuiButton } from '@mui/material';

export const MyButton: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  return <MuiButton variant="contained">{children}</MuiButton>;
};
```

---

### **Q7: Caching Strategies - Chiến Lược Cache** 🔥

#### **🔍 Câu Hỏi:**
Handle caching - Cookie, localStorage, sessionStorage, IndexedDB?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Browser Caching**: Caching ở browser level để tăng performance
  - *Là gì*: Lưu trữ data trong browser để tránh request lại
  - *Tại sao cần*: Giảm network requests, tăng tốc độ load
  - *Khi nào dùng*: Static assets, API responses, user preferences

- **🎯 Cookie**: Small data storage với expiration và domain control
  - *Là gì*: Small text files lưu trữ data trên client
  - *Tại sao cần*: Authentication, tracking, personalization
  - *Khi nào dùng*: JWT tokens, user preferences, session data

- **⚡ localStorage**: Persistent storage không có expiration
  - *Là gì*: Key-value storage persistent trong browser
  - *Tại sao cần*: Lưu trữ data lâu dài, không mất khi đóng browser
  - *Khi nào dùng*: User settings, cached data, offline data

- **✅ sessionStorage**: Temporary storage cho session hiện tại
  - *Là gì*: Key-value storage chỉ tồn tại trong session
  - *Tại sao cần*: Lưu trữ data tạm thời, không persistent
  - *Khi nào dùng*: Form data, temporary state, shopping cart

- **⚠️ IndexedDB**: Advanced database cho large data
  - *Là gì*: NoSQL database client-side cho large data
  - *Tại sao cần*: Lưu trữ large data, complex queries, offline support
  - *Khi nào dùng*: Offline apps, large datasets, complex data structures

**1. LocalStorage Hook:**
```javascript
// useLocalStorage hook
import { useState, useEffect } from 'react';

function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error);
    }
  };

  const removeValue = () => {
    try {
      window.localStorage.removeItem(key);
      setStoredValue(initialValue);
    } catch (error) {
      console.error(`Error removing localStorage key "${key}":`, error);
    }
  };

  return [storedValue, setValue, removeValue] as const;
}

// Usage
const [user, setUser, removeUser] = useLocalStorage('user', null);
```

**2. SessionStorage Hook:**
```javascript
// useSessionStorage hook
function useSessionStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.sessionStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading sessionStorage key "${key}":`, error);
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.sessionStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error setting sessionStorage key "${key}":`, error);
    }
  };

  return [storedValue, setValue] as const;
}
```

**3. Cookie Manager:**
```javascript
// Cookie utility class
class CookieManager {
  static setCookie(name: string, value: string, days: number = 7, secure: boolean = true) {
    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));

    const cookieString = `${name}=${value};expires=${expires.toUTCString()};path=/;SameSite=Strict${
      secure ? ';Secure' : ''
    }`;

    document.cookie = cookieString;
  }

  static getCookie(name: string): string | null {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');

    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
  }

  static deleteCookie(name: string) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;`;
  }

  static getAllCookies(): Record<string, string> {
    const cookies: Record<string, string> = {};
    document.cookie.split(';').forEach(cookie => {
      const [name, value] = cookie.trim().split('=');
      if (name && value) {
        cookies[name] = value;
      }
    });
    return cookies;
  }
}
```

**4. IndexedDB Manager:**
```javascript
// IndexedDB utility class
class IndexedDBManager {
  private dbName: string;
  private version: number;
  private db: IDBDatabase | null = null;

  constructor(dbName: string, version: number = 1) {
    this.dbName = dbName;
    this.version = version;
  }

  async open(): Promise<IDBDatabase> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.version);

      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve(request.result);
      };

      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;

        // Create object stores
        if (!db.objectStoreNames.contains('users')) {
          db.createObjectStore('users', { keyPath: 'id' });
        }
        if (!db.objectStoreNames.contains('cache')) {
          db.createObjectStore('cache', { keyPath: 'key' });
        }
      };
    });
  }

  async add(storeName: string, data: any): Promise<void> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const request = store.add(data);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  async get(storeName: string, key: any): Promise<any> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const request = store.get(key);

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async getAll(storeName: string): Promise<any[]> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const request = store.getAll();

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async delete(storeName: string, key: any): Promise<void> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const request = store.delete(key);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }
}

// Usage
const dbManager = new IndexedDBManager('MyAppDB', 1);
await dbManager.open();
await dbManager.add('users', { id: 1, name: 'John Doe' });
const user = await dbManager.get('users', 1);
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Use appropriate storage - Tối ưu nhất cho từng use case
// Cookies cho authentication - Cookies tối ưu cho authentication (secure, httpOnly)
document.cookie = `token=${jwtToken}; secure; httpOnly; sameSite=strict`; // Secure cookie - tối ưu cho security

// localStorage cho user preferences - localStorage for user preferences
localStorage.setItem('theme', 'dark');
localStorage.setItem('language', 'vi');

// sessionStorage cho temporary data - sessionStorage for temporary data
sessionStorage.setItem('formData', JSON.stringify(formData));

// IndexedDB cho large data - IndexedDB for large data
const db = await openDB('appDB', 1, {
  upgrade(db) {
    db.createObjectStore('users', { keyPath: 'id' });
  }
});

// ✅ Good: Error handling - Xử lý lỗi
try {
  const data = localStorage.getItem('userData');
  if (data) {
    return JSON.parse(data);
  }
} catch (error) {
  console.error('Error reading from localStorage:', error);
  return null;
}

// ✅ Good: Storage cleanup - Dọn dẹp storage
const cleanupStorage = () => {
  // Remove old data
  const keys = Object.keys(localStorage);
  keys.forEach(key => {
    if (key.startsWith('temp_')) {
      localStorage.removeItem(key);
    }
  });
};
```

**🔥 SO SÁNH TỐI ƯU - Storage APIs:**

| Storage Type | Size Limit | Persistence | Security | Tại sao tối ưu cho use case cụ thể |
|--------------|------------|-------------|----------|-----------------------------------|
| **Cookies** | 4KB | Session/Persistent | ✅ High (httpOnly) | Tối ưu cho authentication, server-side access |
| **localStorage** | 5-10MB | Persistent | ⚠️ Medium | Tối ưu cho user preferences, cached data |
| **sessionStorage** | 5-10MB | Session only | ⚠️ Medium | Tối ưu cho temporary data, form data |
| **IndexedDB** | 50MB+ | Persistent | ⚠️ Medium | Tối ưu cho large data, complex queries |
| **Memory** | Unlimited | Session only | ✅ High | Tối ưu cho sensitive data, temporary state |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ SAI: Store sensitive data in localStorage - Lưu data nhạy cảm trong localStorage
localStorage.setItem('password', 'secret123'); // ❌ Không an toàn - có thể bị XSS

// ✅ Đúng: Use secure storage for sensitive data - Dùng storage an toàn cho data nhạy cảm
// Chỉ lưu trong memory hoặc secure cookies
const secureToken = 'jwt-token';
// Không lưu password, credit card info

// ❌ Sai: Not handling storage errors - Không xử lý lỗi storage
const data = localStorage.getItem('data'); // ❌ Có thể fail

// ✅ Đúng: Handle storage errors - Xử lý lỗi storage
try {
  const data = localStorage.getItem('data');
  return data ? JSON.parse(data) : null;
} catch (error) {
  console.error('Storage error:', error);
  return null;
}

// ❌ Sai: Storing large objects in localStorage - Lưu object lớn trong localStorage
const largeData = { /* huge object */ };
localStorage.setItem('data', JSON.stringify(largeData)); // ❌ Có thể exceed limit

// ✅ Đúng: Use IndexedDB for large data - Dùng IndexedDB cho data lớn
const db = await openDB('appDB', 1);
await db.put('largeData', largeData);

// ❌ Sai: Not setting expiration for cookies - Không set expiration cho cookies
document.cookie = 'token=abc123'; // ❌ Session cookie

// ✅ Đúng: Set proper expiration - Set expiration phù hợp
document.cookie = `token=abc123; expires=${new Date(Date.now() + 86400000).toUTCString()}`;
```

---

### **Q8: Branching Model - Git Flow** 🔥

#### **🔍 Câu Hỏi:**
Branching model? Rebase, Merge? Feature flag? Git flow?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Git Flow**: Workflow model phổ biến cho Git branching
  - *Là gì*: Mô hình branching với các branch cố định cho từng mục đích
  - *Tại sao cần*: Quản lý releases, features, hotfixes một cách có tổ chức
  - *Khi nào dùng*: Dự án lớn, team nhiều người, cần quản lý releases

- **🎯 Main Branches**: master/main và develop
  - *master/main*: Branch chính, luôn stable, chứa production code
  - *develop*: Branch development, tích hợp features trước khi release
  - *Tại sao cần*: Tách biệt production và development code

- **⚡ Feature Branches**: Branches cho từng feature
  - *Là gì*: Branch riêng cho mỗi feature, tách từ develop
  - *Tại sao cần*: Phát triển features độc lập, không ảnh hưởng lẫn nhau
  - *Khi nào dùng*: Mỗi feature mới, bug fix, enhancement

- **✅ Release Branches**: Chuẩn bị cho releases
  - *Là gì*: Branch để chuẩn bị release, test, fix bugs
  - *Tại sao cần*: Đảm bảo release stable, không có bugs
  - *Khi nào dùng*: Trước khi release version mới

- **⚠️ Hotfix Branches**: Fix bugs khẩn cấp
  - *Là gì*: Branch để fix bugs critical trong production
  - *Tại sao cần*: Fix bugs nhanh chóng mà không ảnh hưởng development
  - *Khi nào dùng*: Bugs critical trong production

**1. Git Flow Structure:**
```bash
# Git Flow structure
main (production)
├── develop (integration)
├── feature/user-authentication
├── feature/payment-integration
├── release/v1.2.0
└── hotfix/critical-bug-fix
```

**2. Git Flow Commands:**
```bash
# Initialize Git Flow
git flow init

# Feature branch workflow
git flow feature start user-authentication
# Work on feature
git flow feature finish user-authentication

# Release workflow
git flow release start v1.2.0
# Final testing and bug fixes
git flow release finish v1.2.0

# Hotfix workflow
git flow hotfix start critical-bug-fix
# Fix critical issue
git flow hotfix finish critical-bug-fix
```

**3. Merge vs Rebase:**
```bash
# Merge - Preserves history
git checkout main
git merge feature-branch
# Creates merge commit, preserves branch history

# Rebase - Clean history
git checkout feature-branch
git rebase main
# Replays commits on top of main, linear history

# Interactive rebase
git rebase -i HEAD~3
# Squash commits, edit messages, reorder

# Rebase with conflict resolution
git rebase main
# Resolve conflicts
git add .
git rebase --continue
```

**4. Feature Flags Implementation:**
```javascript
// feature-flags.js
class FeatureFlags {
  constructor() {
    this.flags = new Map();
    this.loadFlags();
  }

  async loadFlags() {
    try {
      const response = await fetch('/api/feature-flags');
      const flags = await response.json();
      flags.forEach(flag => {
        this.flags.set(flag.name, flag.enabled);
      });
    } catch (error) {
      console.error('Failed to load feature flags:', error);
    }
  }

  isEnabled(flagName: string): boolean {
    return this.flags.get(flagName) || false;
  }

  setFlag(flagName: string, enabled: boolean) {
    this.flags.set(flagName, enabled);
  }
}

// Usage in components
const featureFlags = new FeatureFlags();

const MyComponent = () => {
  const showNewFeature = featureFlags.isEnabled('new-feature');

  return (
    <div>
      {showNewFeature && <NewFeatureComponent />}
      <RegularComponent />
    </div>
  );
};
```

**5. Branch Protection Rules:**
```yaml
# .github/branch-protection.yml
name: Branch Protection
on:
  push:
    branches: [main, develop]

jobs:
  branch-protection:
    runs-on: ubuntu-latest
    steps:
      - name: Check branch protection
        run: |
          if [ "${{ github.ref }}" = "refs/heads/main" ]; then
            echo "Main branch - requires PR review"
          elif [ "${{ github.ref }}" = "refs/heads/develop" ]; then
            echo "Develop branch - requires status checks"
          fi
```

#### **🎯 Best Practices:**

```bash
# ✅ TỐI ƯU NHẤT: Good branching practices - Tối ưu nhất cho team collaboration
# 1. Keep branches short-lived - Giữ branches ngắn hạn - tối ưu cho merge conflicts
git checkout -b feature/user-login # Tạo feature branch - tối ưu cho parallel development
# Work and commit frequently - Commit thường xuyên - tối ưu cho backup và rollback
git commit -m "Add login form validation" # Commit message rõ ràng - tối ưu cho tracking
# Merge quickly after review - Merge nhanh sau review - tối ưu cho integration
git checkout main && git merge feature/user-login # Merge feature - tối ưu cho code integration

# 2. Use descriptive commit messages - Dùng commit messages mô tả - tối ưu cho debugging
git commit -m "feat: add user authentication with JWT" # Feature commit - tối ưu cho changelog
git commit -m "fix: resolve memory leak in data fetching" # Fix commit - tối ưu cho bug tracking
git commit -m "docs: update API documentation"

# 3. Clean up merged branches
git branch -d feature/user-login
git push origin --delete feature/user-login

# 4. Use pull request templates
# .github/pull_request_template.md
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] Manual testing completed
```

**🔥 SO SÁNH TỐI ƯU - Git Flow vs Other Models:**

| Model | Pros | Cons | Tại sao Git Flow tối ưu nhất |
|-------|------|------|----------------------------|
| **Git Flow** | ✅ Clear structure, release management | ❌ Complex, overhead | Tối ưu cho large teams, complex projects |
| **GitHub Flow** | ✅ Simple, fast | ❌ No release branches | Tối ưu cho continuous deployment |
| **GitLab Flow** | ✅ Environment branches | ❌ Less structured | Tối ưu cho environment-specific deployments |
| **Trunk-based** | ✅ Simple, fast | ❌ Requires discipline | Tối ưu cho small teams, simple projects |
| **Feature Branch** | ✅ Isolated development | ❌ Merge conflicts | Tối ưu cho parallel development |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```bash
# ❌ SAI: Long-lived feature branches - Branches sống lâu
git checkout -b feature/massive-refactor # ❌ Feature branch quá lớn - khó merge
# Work for weeks without merging - Làm việc nhiều tuần không merge - tăng conflicts
git commit -m "WIP: massive changes" # ❌ Commit message không rõ ràng

# ✅ ĐÚNG: Short-lived feature branches - Branches ngắn hạn
git checkout -b feature/user-login # ✅ Feature branch nhỏ - dễ merge
# Work and commit frequently - Làm việc và commit thường xuyên - giảm conflicts
git commit -m "feat: add login form validation" # ✅ Commit message rõ ràng

# 2. Force pushing to shared branches
git push --force origin main

# 3. Not cleaning up branches
# Leaves dozens of merged branches

# 4. Inconsistent commit messages
git commit -m "fix stuff"
git commit -m "update"
git commit -m "changes"
```

---

### **Q9: Frontend Architecture - Cấu Trúc Scalable** 🔥

#### **🔍 Câu Hỏi:**
Steps to build a FE structure? How you define structure for app can be scale?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Scalable Architecture**: Thiết kế cấu trúc có thể mở rộng theo thời gian
  - *Là gì*: Cấu trúc code có thể handle growth về team size, features, complexity
  - *Tại sao cần*: Dễ maintain, scale team, add features mới
  - *Khi nào dùng*: Dự án lớn, team nhiều người, long-term project

- **🎯 Folder Structure**: Tổ chức files và folders logic
  - *Là gì*: Cách sắp xếp code theo modules, features, layers
  - *Tại sao cần*: Dễ tìm code, maintain, collaborate
  - *Khi nào dùng*: Mọi dự án, đặc biệt quan trọng với dự án lớn

- **⚡ Component Architecture**: Thiết kế components có thể tái sử dụng
  - *Là gì*: Tách components thành small, focused, reusable pieces
  - *Tại sao cần*: Code reuse, easier testing, better maintainability
  - *Khi nào dùng*: React/Vue/Angular projects

- **✅ State Management**: Quản lý state hiệu quả
  - *Là gì*: Centralized state management cho complex apps
  - *Tại sao cần*: Predictable state updates, easier debugging
  - *Khi nào dùng*: Apps với complex state, multiple components

- **⚠️ Performance Optimization**: Tối ưu performance từ đầu
  - *Là gì*: Code splitting, lazy loading, caching strategies
  - *Tại sao cần*: Better user experience, faster loading
  - *Khi nào dùng*: Production apps, large applications

**1. Scalable Project Structure:**
```
src/
├── components/           # Reusable UI components
│   ├── common/          # Generic components
│   ├── forms/           # Form components
│   └── layout/          # Layout components
├── pages/               # Page components
├── hooks/               # Custom React hooks
├── services/            # API services
├── store/               # State management
├── utils/               # Utility functions
├── types/               # TypeScript types
├── constants/           # App constants
├── assets/              # Static assets
└── styles/              # Global styles
```

**2. Component Architecture:**
```javascript
// components/common/Button/Button.tsx
import React from 'react';
import { ButtonProps } from './Button.types';
import { StyledButton } from './Button.styles';

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'medium',
  disabled = false,
  onClick,
  ...props
}) => {
  return (
    <StyledButton
      variant={variant}
      size={size}
      disabled={disabled}
      onClick={onClick}
      {...props}
    >
      {children}
    </StyledButton>
  );
};

// components/common/Button/Button.types.ts
export interface ButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary' | 'outline';
  size?: 'small' | 'medium' | 'large';
  disabled?: boolean;
  onClick?: () => void;
  className?: string;
}

// components/common/Button/Button.styles.ts
import styled from 'styled-components';

export const StyledButton = styled.button<ButtonProps>`
  padding: ${props => props.size === 'small' ? '8px 16px' :
                      props.size === 'large' ? '16px 32px' : '12px 24px'};
  border-radius: 4px;
  border: none;
  cursor: pointer;
  font-size: ${props => props.size === 'small' ? '14px' :
                        props.size === 'large' ? '18px' : '16px'};
  font-weight: 500;
  transition: all 0.2s ease;

  background-color: ${props =>
    props.variant === 'primary' ? '#007bff' :
    props.variant === 'secondary' ? '#6c757d' : 'transparent'
  };

  color: ${props => props.variant === 'outline' ? '#007bff' : '#fff'};
  border: ${props => props.variant === 'outline' ? '1px solid #007bff' : 'none'};

  &:hover {
    opacity: 0.8;
    transform: translateY(-1px);
  }

  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }
`;

// components/common/Button/index.ts
export { Button } from './Button';
export type { ButtonProps } from './Button.types';
```

**3. Custom Hooks Pattern:**
```javascript
// hooks/useApi.ts
import { useState, useEffect, useCallback } from 'react';

interface UseApiOptions {
  immediate?: boolean;
  onSuccess?: (data: any) => void;
  onError?: (error: Error) => void;
}

export function useApi<T>(
  apiFunction: () => Promise<T>,
  options: UseApiOptions = {}
) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const execute = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const result = await apiFunction();
      setData(result);
      options.onSuccess?.(result);
    } catch (err) {
      const error = err as Error;
      setError(error);
      options.onError?.(error);
    } finally {
      setLoading(false);
    }
  }, [apiFunction, options]);

  useEffect(() => {
    if (options.immediate !== false) {
      execute();
    }
  }, [execute, options.immediate]);

  return { data, loading, error, execute };
}

// hooks/useLocalStorage.ts
import { useState, useEffect } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error);
    }
  };

  return [storedValue, setValue] as const;
}
```

**4. Service Layer:**
```javascript
// services/api.ts
class ApiService {
  private baseURL: string;
  private token: string | null = null;

  constructor(baseURL: string) {
    this.baseURL = baseURL;
  }

  setToken(token: string) {
    this.token = token;
  }

  private async request<T>(endpoint: string, options: RequestInit = {}): Promise<T> {
    const url = `${this.baseURL}${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...(this.token && { Authorization: `Bearer ${this.token}` }),
      ...options.headers
    };

    const response = await fetch(url, {
      ...options,
      headers
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    return response.json();
  }

  async get<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'GET' });
  }

  async post<T>(endpoint: string, data: any): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  async put<T>(endpoint: string, data: any): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }

  async delete<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'DELETE' });
  }
}

// services/userService.ts
import { ApiService } from './api';

export interface User {
  id: number;
  name: string;
  email: string;
}

export class UserService {
  private api: ApiService;

  constructor(api: ApiService) {
    this.api = api;
  }

  async getUsers(): Promise<User[]> {
    return this.api.get<User[]>('/users');
  }

  async getUser(id: number): Promise<User> {
    return this.api.get<User>(`/users/${id}`);
  }

  async createUser(user: Omit<User, 'id'>): Promise<User> {
    return this.api.post<User>('/users', user);
  }

  async updateUser(id: number, user: Partial<User>): Promise<User> {
    return this.api.put<User>(`/users/${id}`, user);
  }

  async deleteUser(id: number): Promise<void> {
    return this.api.delete<void>(`/users/${id}`);
  }
}
```

**5. State Management with Context:**
```javascript
// store/UserContext.tsx
import React, { createContext, useContext, useReducer, ReactNode } from 'react';

interface UserState {
  users: User[];
  loading: boolean;
  error: string | null;
}

type UserAction =
  | { type: 'FETCH_USERS_START' }
  | { type: 'FETCH_USERS_SUCCESS'; payload: User[] }
  | { type: 'FETCH_USERS_ERROR'; payload: string }
  | { type: 'ADD_USER'; payload: User }
  | { type: 'UPDATE_USER'; payload: User }
  | { type: 'DELETE_USER'; payload: number };

const initialState: UserState = {
  users: [],
  loading: false,
  error: null
};

function userReducer(state: UserState, action: UserAction): UserState {
  switch (action.type) {
    case 'FETCH_USERS_START':
      return { ...state, loading: true, error: null };
    case 'FETCH_USERS_SUCCESS':
      return { ...state, loading: false, users: action.payload };
    case 'FETCH_USERS_ERROR':
      return { ...state, loading: false, error: action.payload };
    case 'ADD_USER':
      return { ...state, users: [...state.users, action.payload] };
    case 'UPDATE_USER':
      return {
        ...state,
        users: state.users.map(user =>
          user.id === action.payload.id ? action.payload : user
        )
      };
    case 'DELETE_USER':
      return {
        ...state,
        users: state.users.filter(user => user.id !== action.payload)
      };
    default:
      return state;
  }
}

const UserContext = createContext<{
  state: UserState;
  dispatch: React.Dispatch<UserAction>;
} | null>(null);

export function UserProvider({ children }: { children: ReactNode }) {
  const [state, dispatch] = useReducer(userReducer, initialState);

  return (
    <UserContext.Provider value={{ state, dispatch }}>
      {children}
    </UserContext.Provider>
  );
}

export function useUserContext() {
  const context = useContext(UserContext);
  if (!context) {
    throw new Error('useUserContext must be used within a UserProvider');
  }
  return context;
}
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Feature-based folder structure - Tối ưu nhất cho scalability
src/
├── features/ # Feature-based organization - tối ưu cho team collaboration
│   ├── auth/ # Authentication feature - tối ưu cho feature isolation
│   │   ├── components/ # Auth components - tối ưu cho component organization
│   │   ├── hooks/ # Auth hooks - tối ưu cho logic reuse
│   │   ├── services/ # Auth services - tối ưu cho API management
│   │   └── types/ # Auth types - tối ưu cho type safety
│   ├── dashboard/ # Dashboard feature - tối ưu cho feature isolation
│   │   ├── components/ # Dashboard components - tối ưu cho component organization
│   │   ├── hooks/ # Dashboard hooks - tối ưu cho logic reuse
│   │   └── services/ # Dashboard services - tối ưu cho API management
│   └── profile/ # Profile feature - tối ưu cho feature isolation
├── shared/ # Shared resources - tối ưu cho code reuse
│   ├── components/ # Common components - tối ưu cho component reuse
│   ├── hooks/ # Common hooks - tối ưu cho hook reuse
│   ├── utils/
│   └── types/

// ✅ Good: Container/Presentational pattern - Pattern Container/Presentational
// Container Component - Quản lý logic và state
const UserListContainer = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchUsers = async () => {
    setLoading(true);
    const data = await userService.getUsers();
    setUsers(data);
    setLoading(false);
  };

  return <UserList users={users} loading={loading} onRefresh={fetchUsers} />;
};

// Presentational Component - Chỉ hiển thị UI
const UserList = ({ users, loading, onRefresh }) => {
  if (loading) return <Spinner />;

  return (
    <div>
      <button onClick={onRefresh}>Refresh</button>
      {users.map(user => <UserCard key={user.id} user={user} />)}
    </div>
  );
};

// ✅ Good: Custom hooks for logic reuse - Custom hooks cho tái sử dụng logic
const useUsers = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchUsers = useCallback(async () => {
    setLoading(true);
    try {
      const data = await userService.getUsers();
      setUsers(data);
    } catch (error) {
      console.error('Error fetching users:', error);
    } finally {
      setLoading(false);
    }
  }, []);

  return { users, loading, fetchUsers };
};
```

**🔥 SO SÁNH TỐI ƯU - Frontend Architecture Patterns:**

| Pattern | Pros | Cons | Tại sao tối ưu cho use case cụ thể |
|---------|------|------|-----------------------------------|
| **Feature-based** | ✅ Scalable, team-friendly | ❌ Code duplication | Tối ưu cho large teams, complex apps |
| **Component-based** | ✅ Reusable, maintainable | ❌ Over-engineering | Tối ưu cho UI-heavy applications |
| **Layer-based** | ✅ Clear separation | ❌ Rigid structure | Tối ưu cho enterprise applications |
| **Domain-driven** | ✅ Business-focused | ❌ Complex setup | Tối ưu cho business applications |
| **Monorepo** | ✅ Shared code, versioning | ❌ Complex tooling | Tối ưu cho multiple related projects |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ SAI: Flat folder structure - Cấu trúc folder phẳng
src/
├── Button.js # ❌ Tất cả files ở cùng level - khó maintain
├── Header.js # ❌ Không có organization - khó scale
├── UserList.js # ❌ Khó tìm code - khó collaborate

// ✅ ĐÚNG: Feature-based structure - Cấu trúc theo feature
src/
├── features/ # ✅ Organized by features - dễ maintain
│   ├── auth/ # ✅ Auth feature - dễ scale
│   └── dashboard/ # ✅ Dashboard feature - dễ collaborate
├── UserCard.js
├── authService.js
├── userService.js
// ❌ Khó tìm code, không có organization

// ✅ Đúng: Organized folder structure - Cấu trúc folder có tổ chức
src/
├── components/
│   ├── ui/
│   │   ├── Button.js
│   │   └── Header.js
│   └── features/
│       ├── UserList.js
│       └── UserCard.js
├── services/
│   ├── authService.js
│   └── userService.js

// ❌ Sai: God components - Components quá lớn
const UserDashboard = () => {
  // 500+ lines of code - ❌ Quá phức tạp
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({});
  const [sorting, setSorting] = useState({});
  // ... hundreds more lines

  return (
    <div>
      {/* Complex JSX */}
    </div>
  );
};

// ✅ Đúng: Small, focused components - Components nhỏ, tập trung
const UserDashboard = () => {
  return (
    <div>
      <UserFilters />
      <UserList />
      <UserPagination />
    </div>
  );
};

// ❌ Sai: Props drilling - Truyền props qua nhiều levels
const App = () => {
  const [user, setUser] = useState(null);
  return <Header user={user} onUserChange={setUser} />;
};

const Header = ({ user, onUserChange }) => {
  return <Navigation user={user} onUserChange={onUserChange} />;
};

const Navigation = ({ user, onUserChange }) => {
  return <UserMenu user={user} onUserChange={onUserChange} />;
};

// ✅ Đúng: Context API hoặc state management - Context API hoặc state management
const UserContext = createContext();

const App = () => {
  const [user, setUser] = useState(null);
  return (
    <UserContext.Provider value={{ user, setUser }}>
      <Header />
    </UserContext.Provider>
  );
};
```

---

### **Q10: Design Patterns - Mẫu Thiết Kế** 🔥

#### **🔍 Câu Hỏi:**
Apply any design pattern yet? Design patterns?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Design Patterns**: Các mẫu thiết kế đã được chứng minh để giải quyết vấn đề phổ biến
  - *Là gì*: Reusable solutions cho common problems trong software design
  - *Tại sao cần*: Tăng code quality, maintainability, team collaboration
  - *Khi nào dùng*: Khi gặp vấn đề tương tự, cần solution đã được test

- **🎯 Creational Patterns**: Tạo objects một cách linh hoạt
  - *Singleton*: Đảm bảo chỉ có một instance duy nhất
  - *Factory*: Tạo objects mà không cần specify exact class
  - *Builder*: Tạo complex objects step by step
  - *Khi nào dùng*: Cần control object creation, complex initialization

- **⚡ Structural Patterns**: Tổ chức classes và objects
  - *Adapter*: Cho phép incompatible interfaces làm việc cùng nhau
  - *Decorator*: Thêm behavior cho objects dynamically
  - *Facade*: Cung cấp simplified interface cho complex subsystem
  - *Khi nào dùng*: Cần integrate existing code, add features

- **✅ Behavioral Patterns**: Quản lý communication giữa objects
  - *Observer*: Notify multiple objects về changes
  - *Strategy*: Define family of algorithms, make them interchangeable
  - *Command*: Encapsulate requests as objects
  - *Khi nào dùng*: Cần loose coupling, flexible communication

- **⚠️ React-Specific Patterns**: Patterns đặc biệt cho React
  - *Render Props*: Share code between components using props
  - *Higher-Order Components*: Reuse component logic
  - *Custom Hooks*: Extract component logic into reusable functions
  - *Khi nào dùng*: React projects, component reusability

**1. Observer Pattern:**
```javascript
// Observer Pattern - Event System
class EventEmitter {
  private events: Map<string, Function[]> = new Map();

  on(event: string, callback: Function) {
    if (!this.events.has(event)) {
      this.events.set(event, []);
    }
    this.events.get(event)!.push(callback);
  }

  off(event: string, callback: Function) {
    if (!this.events.has(event)) return;

    const callbacks = this.events.get(event)!;
    const index = callbacks.indexOf(callback);
    if (index > -1) {
      callbacks.splice(index, 1);
    }
  }

  emit(event: string, ...args: any[]) {
    if (!this.events.has(event)) return;

    this.events.get(event)!.forEach(callback => {
      callback(...args);
    });
  }
}

// Usage
const eventEmitter = new EventEmitter();

eventEmitter.on('user-login', (user) => {
  console.log('User logged in:', user);
});

eventEmitter.emit('user-login', { id: 1, name: 'John' });
```

**2. Factory Pattern:**
```javascript
// Factory Pattern - Component Factory
interface ButtonConfig {
  type: 'primary' | 'secondary' | 'danger';
  size: 'small' | 'medium' | 'large';
  disabled?: boolean;
}

class ButtonFactory {
  static createButton(config: ButtonConfig) {
    const baseClasses = 'btn';
    const typeClass = `btn-${config.type}`;
    const sizeClass = `btn-${config.size}`;
    const disabledClass = config.disabled ? 'btn-disabled' : '';

    return {
      className: [baseClasses, typeClass, sizeClass, disabledClass].join(' '),
      type: config.type,
      size: config.size,
      disabled: config.disabled
    };
  }
}

// Usage
const primaryButton = ButtonFactory.createButton({
  type: 'primary',
  size: 'medium',
  disabled: false
});
```

**3. Strategy Pattern:**
```javascript
// Strategy Pattern - Payment Methods
interface PaymentStrategy {
  pay(amount: number): Promise<boolean>;
}

class CreditCardPayment implements PaymentStrategy {
  async pay(amount: number): Promise<boolean> {
    console.log(`Paying $${amount} with Credit Card`);
    // Credit card payment logic
    return true;
  }
}

class PayPalPayment implements PaymentStrategy {
  async pay(amount: number): Promise<boolean> {
    console.log(`Paying $${amount} with PayPal`);
    // PayPal payment logic
    return true;
  }
}

class BankTransferPayment implements PaymentStrategy {
  async pay(amount: number): Promise<boolean> {
    console.log(`Paying $${amount} with Bank Transfer`);
    // Bank transfer logic
    return true;
  }
}

class PaymentProcessor {
  private strategy: PaymentStrategy;

  constructor(strategy: PaymentStrategy) {
    this.strategy = strategy;
  }

  setStrategy(strategy: PaymentStrategy) {
    this.strategy = strategy;
  }

  async processPayment(amount: number): Promise<boolean> {
    return this.strategy.pay(amount);
  }
}

// Usage
const processor = new PaymentProcessor(new CreditCardPayment());
await processor.processPayment(100);

processor.setStrategy(new PayPalPayment());
await processor.processPayment(200);
```

**4. Decorator Pattern:**
```javascript
// Decorator Pattern - Higher-Order Components
function withLoading<T extends object>(Component: React.ComponentType<T>) {
  return function WithLoadingComponent(props: T & { loading?: boolean }) {
    if (props.loading) {
      return <div>Loading...</div>;
    }
    return <Component {...props} />;
  };
}

function withError<T extends object>(Component: React.ComponentType<T>) {
  return function WithErrorComponent(props: T & { error?: string }) {
    if (props.error) {
      return <div>Error: {props.error}</div>;
    }
    return <Component {...props} />;
  };
}

// Usage
const UserList = ({ users }: { users: User[] }) => (
  <ul>
    {users.map(user => <li key={user.id}>{user.name}</li>)}
  </ul>
);

const EnhancedUserList = withError(withLoading(UserList));
```

**5. Command Pattern:**
```javascript
// Command Pattern - Undo/Redo System
interface Command {
  execute(): void;
  undo(): void;
}

class AddUserCommand implements Command {
  constructor(
    private userService: UserService,
    private user: User,
    private onSuccess: (user: User) => void,
    private onError: (error: Error) => void
  ) {}

  async execute() {
    try {
      const newUser = await this.userService.createUser(this.user);
      this.onSuccess(newUser);
    } catch (error) {
      this.onError(error as Error);
    }
  }

  async undo() {
    // Undo logic - remove the user
    try {
      await this.userService.deleteUser(this.user.id);
    } catch (error) {
      console.error('Failed to undo add user:', error);
    }
  }
}

class CommandInvoker {
  private history: Command[] = [];
  private currentIndex = -1;

  executeCommand(command: Command) {
    command.execute();
    this.history = this.history.slice(0, this.currentIndex + 1);
    this.history.push(command);
    this.currentIndex++;
  }

  undo() {
    if (this.currentIndex >= 0) {
      const command = this.history[this.currentIndex];
      command.undo();
      this.currentIndex--;
    }
  }

  redo() {
    if (this.currentIndex < this.history.length - 1) {
      this.currentIndex++;
      const command = this.history[this.currentIndex];
      command.execute();
    }
  }
}
```

**6. Render Props Pattern:**
```javascript
// Render Props Pattern
interface DataFetcherProps<T> {
  url: string;
  children: (data: {
    data: T | null;
    loading: boolean;
    error: string | null;
  }) => React.ReactNode;
}

function DataFetcher<T>({ url, children }: DataFetcherProps<T>) {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch(url)
      .then(response => response.json())
      .then(data => {
        setData(data);
        setLoading(false);
      })
      .catch(error => {
        setError(error.message);
        setLoading(false);
      });
  }, [url]);

  return <>{children({ data, loading, error })}</>;
}

// Usage
<DataFetcher<User[]> url="/api/users">
  {({ data, loading, error }) => {
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    return (
      <ul>
        {data?.map(user => <li key={user.id}>{user.name}</li>)}
      </ul>
    );
  }}
</DataFetcher>
```

**7. Compound Components Pattern:**
```javascript
// Compound Components Pattern
interface SelectContextType {
  value: string;
  onChange: (value: string) => void;
  isOpen: boolean;
  setIsOpen: (open: boolean) => void;
}

const SelectContext = createContext<SelectContextType | null>(null);

function Select({ children, value, onChange }: {
  children: React.ReactNode;
  value: string;
  onChange: (value: string) => void;
}) {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <SelectContext.Provider value={{ value, onChange, isOpen, setIsOpen }}>
      <div className="select">
        {children}
      </div>
    </SelectContext.Provider>
  );
}

function SelectTrigger({ children }: { children: React.ReactNode }) {
  const context = useContext(SelectContext);
  if (!context) throw new Error('SelectTrigger must be used within Select');

  return (
    <button
      className="select-trigger"
      onClick={() => context.setIsOpen(!context.isOpen)}
    >
      {children}
    </button>
  );
}

function SelectOption({ value, children }: {
  value: string;
  children: React.ReactNode;
}) {
  const context = useContext(SelectContext);
  if (!context) throw new Error('SelectOption must be used within Select');

  return (
    <div
      className="select-option"
      onClick={() => {
        context.onChange(value);
        context.setIsOpen(false);
      }}
    >
      {children}
    </div>
  );
}

// Usage
<Select value={selectedValue} onChange={setSelectedValue}>
  <SelectTrigger>
    {selectedValue || 'Select an option'}
  </SelectTrigger>
  <SelectOption value="option1">Option 1</SelectOption>
  <SelectOption value="option2">Option 2</SelectOption>
</Select>
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**

```javascript
// ✅ TỐI ƯU NHẤT: Use appropriate patterns - Tối ưu nhất cho từng use case
// Singleton cho global state - Singleton tối ưu cho global state (single instance)
class AppState {
  constructor() {
    if (AppState.instance) {
      return AppState.instance; // Return existing instance - tối ưu memory
    }
    this.state = {}; // Initialize state
    AppState.instance = this; // Set instance - tối ưu cho global access
  }
}

// Factory cho object creation - Factory for object creation
class UserFactory {
  static createUser(type, data) {
    switch (type) {
      case 'admin':
        return new AdminUser(data);
      case 'regular':
        return new RegularUser(data);
      default:
        throw new Error('Invalid user type');
    }
  }
}

// Observer cho event handling - Observer for event handling
class EventBus {
  constructor() {
    this.events = {};
  }

  on(event, callback) {
    if (!this.events[event]) {
      this.events[event] = [];
    }
    this.events[event].push(callback);
  }

  emit(event, data) {
    if (this.events[event]) {
      this.events[event].forEach(callback => callback(data));
    }
  }
}

// ✅ Good: React-specific patterns - Patterns đặc biệt cho React
// Custom Hook pattern - Pattern Custom Hook
const useCounter = (initialValue = 0) => {
  const [count, setCount] = useState(initialValue);

  const increment = useCallback(() => setCount(c => c + 1), []);
  const decrement = useCallback(() => setCount(c => c - 1), []);
  const reset = useCallback(() => setCount(initialValue), [initialValue]);

  return { count, increment, decrement, reset };
};

// Render Props pattern - Pattern Render Props
const DataFetcher = ({ children }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData().then(data => {
      setData(data);
      setLoading(false);
    });
  }, []);

  return children({ data, loading });
};

// Usage
<DataFetcher>
  {({ data, loading }) => (
    loading ? <Spinner /> : <DataList data={data} />
  )}
</DataFetcher>
```

**🔥 SO SÁNH TỐI ƯU - Design Patterns:**

| Pattern | Use Case | Pros | Cons | Tại sao tối ưu cho use case cụ thể |
|---------|----------|------|------|-----------------------------------|
| **Singleton** | Global state, config | ✅ Single instance, global access | ❌ Hard to test, tight coupling | Tối ưu cho global state, configuration |
| **Factory** | Object creation | ✅ Flexible, extensible | ❌ Complex, over-engineering | Tối ưu cho complex object creation |
| **Observer** | Event handling | ✅ Loose coupling, dynamic | ❌ Memory leaks, performance | Tối ưu cho event-driven architecture |
| **Custom Hooks** | React logic reuse | ✅ Reusable, testable | ❌ Over-abstraction | Tối ưu cho React component logic |
| **Render Props** | Component composition | ✅ Flexible, powerful | ❌ Complex, verbose | Tối ưu cho component composition |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ SAI: Overusing Singleton - Lạm dụng Singleton
class UserService {
  constructor() {
    if (UserService.instance) {
      return UserService.instance;
    }
    // ... implementation
    UserService.instance = this;
  }
}

// ❌ Sai: Tạo Singleton cho mọi thứ - Creating Singleton for everything
class ApiClient { /* Singleton */ }
class Logger { /* Singleton */ }
class Config { /* Singleton */ }
// ❌ Không cần thiết, khó test

// ✅ Đúng: Use Singleton only when needed - Chỉ dùng Singleton khi cần
// Chỉ dùng cho global state, configuration, logging
class AppConfig {
  constructor() {
    if (AppConfig.instance) {
      return AppConfig.instance;
    }
    this.config = loadConfig();
    AppConfig.instance = this;
  }
}

// ❌ Sai: Complex Factory without need - Factory phức tạp không cần thiết
class SimpleObjectFactory {
  static create(type) {
    switch (type) {
      case 'a': return new A();
      case 'b': return new B();
      // ... 100 cases
    }
  }
}

// ✅ Đúng: Simple object creation - Tạo object đơn giản
const createUser = (data) => new User(data);
const createAdmin = (data) => new AdminUser(data);

// ❌ Sai: Not using React patterns - Không dùng React patterns
// Duplicate logic across components - Logic trùng lặp
const ComponentA = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  // ... duplicate logic
};

const ComponentB = () => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  // ... same logic
};

// ✅ Đúng: Extract to custom hook - Tách ra custom hook
const useDataFetching = (url) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  // ... shared logic
  return { data, loading };
};
```

---

### **Q11: Storage APIs - Cookie, LocalStorage, SessionStorage** 🔥

#### **🔍 Câu Hỏi:**
Cookie, localStorage, sessionStorage, bảo mật?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Browser Storage APIs**: Các API lưu trữ data trên client-side
  - *Là gì*: Các phương thức lưu trữ data trong browser
  - *Tại sao cần*: Lưu trữ user data, preferences, session info
  - *Khi nào dùng*: User settings, cached data, authentication

- **🎯 Cookies**: Small text files với expiration và security options
  - *Là gì*: Small data storage với domain control và expiration
  - *Tại sao cần*: Authentication, tracking, personalization
  - *Khi nào dùng*: JWT tokens, user preferences, session data

- **⚡ localStorage**: Persistent storage không có expiration
  - *Là gì*: Key-value storage persistent trong browser
  - *Tại sao cần*: Lưu trữ data lâu dài, không mất khi đóng browser
  - *Khi nào dùng*: User settings, cached data, offline data

- **✅ sessionStorage**: Temporary storage cho session hiện tại
  - *Là gì*: Key-value storage chỉ tồn tại trong session
  - *Tại sao cần*: Lưu trữ data tạm thời, không persistent
  - *Khi nào dùng*: Form data, temporary state, shopping cart

- **⚠️ Security Considerations**: Các vấn đề bảo mật quan trọng
  - *XSS Protection*: Không lưu sensitive data trong localStorage
  - *CSRF Protection*: Sử dụng secure cookies với SameSite
  - *Data Validation*: Validate data trước khi lưu trữ
  - *Khi nào cần*: Mọi ứng dụng production, đặc biệt với user data

**1. Secure Cookie Manager:**
```javascript
// Secure Cookie Manager
class SecureCookieManager {
  static setSecureCookie(
    name: string,
    value: string,
    options: {
      days?: number;
      secure?: boolean;
      httpOnly?: boolean;
      sameSite?: 'Strict' | 'Lax' | 'None';
      domain?: string;
      path?: string;
    } = {}
  ) {
    const {
      days = 7,
      secure = true,
      httpOnly = false,
      sameSite = 'Strict',
      domain = window.location.hostname,
      path = '/'
    } = options;

    const expires = new Date();
    expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));

    let cookieString = `${name}=${this.encrypt(value)};expires=${expires.toUTCString()};path=${path};SameSite=${sameSite}`;

    if (secure) cookieString += ';Secure';
    if (httpOnly) cookieString += ';HttpOnly';
    if (domain) cookieString += `;Domain=${domain}`;

    document.cookie = cookieString;
  }

  static getSecureCookie(name: string): string | null {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');

    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) {
        const encryptedValue = c.substring(nameEQ.length, c.length);
        return this.decrypt(encryptedValue);
      }
    }
    return null;
  }

  static deleteSecureCookie(name: string) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;`;
  }

  private static encrypt(text: string): string {
    // Simple encryption - in production, use proper encryption
    return btoa(text);
  }

  private static decrypt(encryptedText: string): string {
    try {
      return atob(encryptedText);
    } catch (error) {
      console.error('Failed to decrypt cookie:', error);
      return '';
    }
  }
}
```

**2. Secure Storage Manager:**
```javascript
// Secure Storage Manager
class SecureStorageManager {
  private static encryptionKey: string;

  static setEncryptionKey(key: string) {
    this.encryptionKey = key;
  }

  static setSecureItem(key: string, value: any, storage: 'local' | 'session' = 'local') {
    try {
      const encryptedValue = this.encrypt(JSON.stringify(value));
      const storageObj = storage === 'local' ? localStorage : sessionStorage;
      storageObj.setItem(key, encryptedValue);
    } catch (error) {
      console.error(`Error setting secure ${storage}Storage:`, error);
    }
  }

  static getSecureItem<T>(key: string, storage: 'local' | 'session' = 'local'): T | null {
    try {
      const storageObj = storage === 'local' ? localStorage : sessionStorage;
      const encryptedValue = storageObj.getItem(key);

      if (!encryptedValue) return null;

      const decryptedValue = this.decrypt(encryptedValue);
      return JSON.parse(decryptedValue);
    } catch (error) {
      console.error(`Error getting secure ${storage}Storage:`, error);
      return null;
    }
  }

  static removeSecureItem(key: string, storage: 'local' | 'session' = 'local') {
    const storageObj = storage === 'local' ? localStorage : sessionStorage;
    storageObj.removeItem(key);
  }

  private static encrypt(text: string): string {
    // Simple encryption - in production, use proper encryption like AES
    return btoa(text);
  }

  private static decrypt(encryptedText: string): string {
    try {
      return atob(encryptedText);
    } catch (error) {
      console.error('Failed to decrypt storage value:', error);
      return '';
    }
  }
}
```

**3. Storage Security Best Practices:**
```javascript
// Storage Security Best Practices - Tối ưu nhất cho security
class StorageSecurity {
  // 1. Validate data before storing - Validate data trước khi lưu - tối ưu cho security
  static validateData(data: any): boolean {
    if (typeof data !== 'object' || data === null) return false; // Check data type - tối ưu cho type safety

    // Check for sensitive data - Kiểm tra data nhạy cảm - tối ưu cho data protection
    const sensitiveKeys = ['password', 'token', 'secret', 'key']; // Sensitive keywords - tối ưu cho security
    const hasSensitiveData = Object.keys(data).some(key =>
      sensitiveKeys.some(sensitive => key.toLowerCase().includes(sensitive)) // Check sensitive data - tối ưu cho validation
    );

    return !hasSensitiveData; // Return validation result - tối ưu cho security check
  }

  // 2. Sanitize data
  static sanitizeData(data: any): any {
    if (typeof data === 'string') {
      return data.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
    }

    if (typeof data === 'object' && data !== null) {
      const sanitized = { ...data };
      Object.keys(sanitized).forEach(key => {
        sanitized[key] = this.sanitizeData(sanitized[key]);
      });
      return sanitized;
    }

    return data;
  }

  // 3. Set expiration for stored data
  static setWithExpiration(
    key: string,
    value: any,
    expirationMinutes: number,
    storage: 'local' | 'session' = 'local'
  ) {
    const data = {
      value: this.sanitizeData(value),
      expiration: Date.now() + (expirationMinutes * 60 * 1000)
    };

    const storageObj = storage === 'local' ? localStorage : sessionStorage;
    storageObj.setItem(key, JSON.stringify(data));
  }

  // 4. Get data with expiration check
  static getWithExpiration<T>(
    key: string,
    storage: 'local' | 'session' = 'local'
  ): T | null {
    try {
      const storageObj = storage === 'local' ? localStorage : sessionStorage;
      const item = storageObj.getItem(key);

      if (!item) return null;

      const data = JSON.parse(item);

      if (Date.now() > data.expiration) {
        storageObj.removeItem(key);
        return null;
      }

      return data.value;
    } catch (error) {
      console.error('Error getting data with expiration:', error);
      return null;
    }
  }

  // 5. Clear expired data
  static clearExpiredData(storage: 'local' | 'session' = 'local') {
    const storageObj = storage === 'local' ? localStorage : sessionStorage;
    const keysToRemove: string[] = [];

    for (let i = 0; i < storageObj.length; i++) {
      const key = storageObj.key(i);
      if (!key) continue;

      try {
        const item = storageObj.getItem(key);
        if (!item) continue;

        const data = JSON.parse(item);
        if (data.expiration && Date.now() > data.expiration) {
          keysToRemove.push(key);
        }
      } catch (error) {
        // If parsing fails, remove the item
        keysToRemove.push(key);
      }
    }

    keysToRemove.forEach(key => storageObj.removeItem(key));
  }
}
```

**4. Storage Usage Example:**
```javascript
// Usage example
class UserStorage {
  private static readonly USER_KEY = 'user_data';
  private static readonly TOKEN_KEY = 'auth_token';
  private static readonly PREFERENCES_KEY = 'user_preferences';

  static saveUser(user: User) {
    if (StorageSecurity.validateData(user)) {
      SecureStorageManager.setSecureItem(this.USER_KEY, user, 'local');
    } else {
      throw new Error('Invalid user data - contains sensitive information');
    }
  }

  static getUser(): User | null {
    return SecureStorageManager.getSecureItem<User>(this.USER_KEY, 'local');
  }

  static saveToken(token: string) {
    // Store token in httpOnly cookie for security
    SecureCookieManager.setSecureCookie(this.TOKEN_KEY, token, {
      days: 7,
      secure: true,
      httpOnly: true,
      sameSite: 'Strict'
    });
  }

  static getToken(): string | null {
    return SecureCookieManager.getSecureCookie(this.TOKEN_KEY);
  }

  static savePreferences(preferences: UserPreferences) {
    StorageSecurity.setWithExpiration(
      this.PREFERENCES_KEY,
      preferences,
      60 * 24 * 7, // 7 days
      'local'
    );
  }

  static getPreferences(): UserPreferences | null {
    return StorageSecurity.getWithExpiration<UserPreferences>(
      this.PREFERENCES_KEY,
      'local'
    );
  }

  static clearAll() {
    SecureStorageManager.removeSecureItem(this.USER_KEY, 'local');
    SecureStorageManager.removeSecureItem(this.PREFERENCES_KEY, 'local');
    SecureCookieManager.deleteSecureCookie(this.TOKEN_KEY);
  }
}
```

---

### **Q12: IndexedDB - Database Client-side** 🔥

#### **🔍 Câu Hỏi:**
IndexedDB - Database Client-side?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 IndexedDB**: NoSQL database client-side cho large data
  - *Là gì*: Asynchronous database API cho storing large amounts of structured data
  - *Tại sao cần*: Lưu trữ large data, complex queries, offline support
  - *Khi nào dùng*: Offline apps, large datasets, complex data structures

- **🎯 Key Features**: Tính năng chính của IndexedDB
  - *Asynchronous*: Non-blocking operations, không freeze UI
  - *Large Storage*: Có thể lưu trữ hàng GB data
  - *Structured Data*: Lưu trữ objects, arrays, complex data
  - *Indexing*: Tạo indexes cho fast queries

- **⚡ Use Cases**: Các trường hợp sử dụng phổ biến
  - *Offline Apps*: Apps hoạt động offline với cached data
  - *Large Datasets*: Lưu trữ large amounts of data locally
  - *Complex Queries*: Query data với multiple conditions
  - *File Storage*: Lưu trữ files, images, documents

- **✅ Advantages**: Ưu điểm của IndexedDB
  - *Performance*: Fast local access, không cần network
  - *Offline Support*: Hoạt động khi không có internet
  - *Large Capacity*: Có thể lưu trữ rất nhiều data
  - *Structured*: Hỗ trợ complex data structures

- **⚠️ Disadvantages**: Nhược điểm của IndexedDB
  - *Complexity*: API phức tạp, khó sử dụng
  - *Browser Support*: Không support trên tất cả browsers cũ
  - *Storage Limits*: Có giới hạn storage per domain
  - *Learning Curve*: Cần thời gian để học và master

**1. IndexedDB Manager Class:**
```javascript
// Advanced IndexedDB Manager - Tối ưu nhất cho large data storage
class IndexedDBManager {
  private dbName: string; // Database name - tối ưu cho database identification
  private version: number; // Database version - tối ưu cho schema management
  private db: IDBDatabase | null = null; // Database instance - tối ưu cho connection management
  private stores: Map<string, IDBObjectStore> = new Map(); // Object stores cache - tối ưu cho performance

  constructor(dbName: string, version: number = 1) { // Constructor - tối ưu cho initialization
    this.dbName = dbName;
    this.version = version;
  }

  async open(): Promise<IDBDatabase> {
    return new Promise((resolve, reject) => {
      const request = indexedDB.open(this.dbName, this.version);

      request.onerror = () => reject(request.error);
      request.onsuccess = () => {
        this.db = request.result;
        resolve(request.result);
      };

      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;
        this.setupStores(db);
      };
    });
  }

  private setupStores(db: IDBDatabase) {
    // Users store
    if (!db.objectStoreNames.contains('users')) {
      const userStore = db.createObjectStore('users', { keyPath: 'id' });
      userStore.createIndex('email', 'email', { unique: true });
      userStore.createIndex('name', 'name', { unique: false });
    }

    // Cache store
    if (!db.objectStoreNames.contains('cache')) {
      const cacheStore = db.createObjectStore('cache', { keyPath: 'key' });
      cacheStore.createIndex('expiration', 'expiration', { unique: false });
    }

    // Settings store
    if (!db.objectStoreNames.contains('settings')) {
      db.createObjectStore('settings', { keyPath: 'key' });
    }
  }

  async add(storeName: string, data: any): Promise<void> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const request = store.add(data);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  async get(storeName: string, key: any): Promise<any> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const request = store.get(key);

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async getAll(storeName: string): Promise<any[]> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const request = store.getAll();

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async update(storeName: string, data: any): Promise<void> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const request = store.put(data);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  async delete(storeName: string, key: any): Promise<void> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const request = store.delete(key);

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  async getByIndex(storeName: string, indexName: string, value: any): Promise<any[]> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const index = store.index(indexName);
      const request = index.getAll(value);

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  async clear(storeName: string): Promise<void> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readwrite');
      const store = transaction.objectStore(storeName);
      const request = store.clear();

      request.onsuccess = () => resolve();
      request.onerror = () => reject(request.error);
    });
  }

  async count(storeName: string): Promise<number> {
    if (!this.db) await this.open();

    return new Promise((resolve, reject) => {
      const transaction = this.db!.transaction([storeName], 'readonly');
      const store = transaction.objectStore(storeName);
      const request = store.count();

      request.onsuccess = () => resolve(request.result);
      request.onerror = () => reject(request.error);
    });
  }

  close() {
    if (this.db) {
      this.db.close();
      this.db = null;
    }
  }
}
```

**🔥 SO SÁNH TỐI ƯU - Client-side Storage Options:**

| Storage Type | Size Limit | Performance | Use Case | Tại sao IndexedDB tối ưu nhất |
|--------------|------------|-------------|----------|-------------------------------|
| **IndexedDB** | 50MB+ | ✅ Fast | Large data, complex queries | Tối ưu cho large datasets, offline apps |
| **localStorage** | 5-10MB | ⚠️ Slower | Simple key-value | Tối ưu cho simple data, user preferences |
| **sessionStorage** | 5-10MB | ⚠️ Slower | Temporary data | Tối ưu cho session data, form data |
| **WebSQL** | Deprecated | ❌ Deprecated | Legacy support | Không nên sử dụng - deprecated |
| **Cache API** | 50MB+ | ✅ Fast | Network caching | Tối ưu cho network resources, service workers |

**2. Cache Manager with IndexedDB:**
```javascript
// Cache Manager using IndexedDB
class CacheManager {
  private dbManager: IndexedDBManager;
  private defaultTTL: number; // Time to live in milliseconds

  constructor(dbName: string = 'app-cache', defaultTTL: number = 60 * 60 * 1000) { // 1 hour
    this.dbManager = new IndexedDBManager(dbName);
    this.defaultTTL = defaultTTL;
  }

  async set(key: string, value: any, ttl?: number): Promise<void> {
    const expiration = Date.now() + (ttl || this.defaultTTL);
    const cacheItem = {
      key,
      value,
      expiration,
      createdAt: Date.now()
    };

    await this.dbManager.update('cache', cacheItem);
  }

  async get(key: string): Promise<any | null> {
    try {
      const cacheItem = await this.dbManager.get('cache', key);

      if (!cacheItem) return null;

      if (Date.now() > cacheItem.expiration) {
        await this.delete(key);
        return null;
      }

      return cacheItem.value;
    } catch (error) {
      console.error('Error getting cache item:', error);
      return null;
    }
  }

  async delete(key: string): Promise<void> {
    await this.dbManager.delete('cache', key);
  }

  async clear(): Promise<void> {
    await this.dbManager.clear('cache');
  }

  async cleanup(): Promise<void> {
    const allItems = await this.dbManager.getAll('cache');
    const now = Date.now();

    for (const item of allItems) {
      if (now > item.expiration) {
        await this.delete(item.key);
      }
    }
  }

  async getStats(): Promise<{
    totalItems: number;
    expiredItems: number;
    totalSize: number;
  }> {
    const allItems = await this.dbManager.getAll('cache');
    const now = Date.now();

    let expiredItems = 0;
    let totalSize = 0;

    for (const item of allItems) {
      if (now > item.expiration) {
        expiredItems++;
      }
      totalSize += JSON.stringify(item).length;
    }

    return {
      totalItems: allItems.length,
      expiredItems,
      totalSize
    };
  }
}
```

**3. Offline Data Sync:**
```javascript
// Offline Data Sync with IndexedDB
class OfflineSyncManager {
  private dbManager: IndexedDBManager;
  private syncQueue: any[] = [];

  constructor() {
    this.dbManager = new IndexedDBManager('offline-sync');
  }

  async saveForSync(operation: {
    type: 'create' | 'update' | 'delete';
    table: string;
    data: any;
    id?: string;
  }): Promise<void> {
    const syncItem = {
      id: Date.now().toString(),
      ...operation,
      timestamp: Date.now(),
      synced: false
    };

    await this.dbManager.add('syncQueue', syncItem);
    this.syncQueue.push(syncItem);
  }

  async syncWithServer(apiEndpoint: string): Promise<void> {
    const pendingItems = await this.dbManager.getAll('syncQueue');
    const unsyncedItems = pendingItems.filter(item => !item.synced);

    for (const item of unsyncedItems) {
      try {
        await this.syncItem(item, apiEndpoint);
        await this.markAsSynced(item.id);
      } catch (error) {
        console.error('Failed to sync item:', item, error);
      }
    }
  }

  private async syncItem(item: any, apiEndpoint: string): Promise<void> {
    const url = `${apiEndpoint}/${item.table}`;

    switch (item.type) {
      case 'create':
        await fetch(url, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(item.data)
        });
        break;
      case 'update':
        await fetch(`${url}/${item.id}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(item.data)
        });
        break;
      case 'delete':
        await fetch(`${url}/${item.id}`, {
          method: 'DELETE'
        });
        break;
    }
  }

  private async markAsSynced(id: string): Promise<void> {
    const item = await this.dbManager.get('syncQueue', id);
    if (item) {
      item.synced = true;
      await this.dbManager.update('syncQueue', item);
    }
  }

  async getPendingSyncCount(): Promise<number> {
    const allItems = await this.dbManager.getAll('syncQueue');
    return allItems.filter(item => !item.synced).length;
  }
}
```

**4. Usage Examples:**
```javascript
// Usage examples
class UserDataManager {
  private dbManager: IndexedDBManager;
  private cacheManager: CacheManager;
  private syncManager: OfflineSyncManager;

  constructor() {
    this.dbManager = new IndexedDBManager('user-data');
    this.cacheManager = new CacheManager('user-cache');
    this.syncManager = new OfflineSyncManager();
  }

  async saveUser(user: User): Promise<void> {
    // Save to IndexedDB
    await this.dbManager.update('users', user);

    // Cache for quick access
    await this.cacheManager.set(`user-${user.id}`, user, 30 * 60 * 1000); // 30 minutes

    // Queue for sync if offline
    if (!navigator.onLine) {
      await this.syncManager.saveForSync({
        type: 'update',
        table: 'users',
        data: user,
        id: user.id.toString()
      });
    }
  }

  async getUser(id: number): Promise<User | null> {
    // Try cache first
    let user = await this.cacheManager.get(`user-${id}`);

    if (!user) {
      // Fallback to IndexedDB
      user = await this.dbManager.get('users', id);

      if (user) {
        // Cache for next time
        await this.cacheManager.set(`user-${id}`, user);
      }
    }

    return user;
  }

  async getAllUsers(): Promise<User[]> {
    return await this.dbManager.getAll('users');
  }

  async searchUsers(query: string): Promise<User[]> {
    // Search by name index
    return await this.dbManager.getByIndex('users', 'name', query);
  }

  async syncData(): Promise<void> {
    if (navigator.onLine) {
      await this.syncManager.syncWithServer('/api');
    }
  }
}
```

---

### **Q13: Token Management - JWT & Refresh Token** 🔥

#### **🔍 Câu Hỏi:**
JWT & Refresh Token được lưu ở đâu và quản lý như thế nào cho bảo mật?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 JWT (JSON Web Token)**: Standard cho secure information transmission
  - *Là gì*: Compact, URL-safe token chứa claims về user
  - *Tại sao cần*: Stateless authentication, scalable, secure
  - *Khi nào dùng*: API authentication, single sign-on, microservices

- **🎯 Refresh Token**: Long-lived token để renew access tokens
  - *Là gì*: Token có thời hạn dài để lấy access token mới
  - *Tại sao cần*: Bảo mật cao, giảm risk khi access token bị compromise
  - *Khi nào dùng*: Khi cần security cao, long-term sessions

- **⚡ Storage Strategies**: Các chiến lược lưu trữ tokens
  - *Memory*: Lưu trong memory, an toàn nhất nhưng mất khi refresh
  - *HttpOnly Cookies*: An toàn, không accessible từ JavaScript
  - *localStorage*: Dễ sử dụng nhưng có risk XSS
  - *sessionStorage*: Tạm thời, mất khi đóng tab

- **✅ Security Best Practices**: Thực hành bảo mật tốt nhất
  - *Short-lived Access Tokens*: Access token có thời hạn ngắn (15-30 phút)
  - *Secure Storage*: Sử dụng HttpOnly cookies cho refresh token
  - *Token Rotation*: Rotate refresh token khi sử dụng
  - *HTTPS Only*: Chỉ sử dụng HTTPS trong production

- **⚠️ Common Vulnerabilities**: Các lỗ hổng bảo mật thường gặp
  - *XSS Attacks*: Nếu lưu trong localStorage/sessionStorage
  - *CSRF Attacks*: Nếu không có proper CSRF protection
  - *Token Theft*: Nếu không có proper token validation
  - *Replay Attacks*: Nếu không có proper token expiration

**1. Token Manager Class:**
```javascript
// Token Manager for JWT and Refresh Token - Tối ưu nhất cho token security
class TokenManager {
  private static readonly ACCESS_TOKEN_KEY = 'access_token'; // Access token key - tối ưu cho token identification
  private static readonly REFRESH_TOKEN_KEY = 'refresh_token'; // Refresh token key - tối ưu cho token identification
  private static readonly TOKEN_EXPIRY_KEY = 'token_expiry'; // Token expiry key - tối ưu cho expiration tracking

  // Store tokens securely - Lưu tokens an toàn - tối ưu cho security
  static setTokens(accessToken: string, refreshToken: string, expiresIn: number) { // Set tokens - tối ưu cho token management
    const expiryTime = Date.now() + (expiresIn * 1000);

    // Store access token in memory (more secure)
    sessionStorage.setItem(this.ACCESS_TOKEN_KEY, accessToken);
    sessionStorage.setItem(this.TOKEN_EXPIRY_KEY, expiryTime.toString());

    // Store refresh token in httpOnly cookie (most secure)
    this.setSecureCookie(this.REFRESH_TOKEN_KEY, refreshToken, {
      days: 30,
      httpOnly: true,
      secure: true,
      sameSite: 'Strict'
    });
  }

  // Get access token
  static getAccessToken(): string | null {
    const token = sessionStorage.getItem(this.ACCESS_TOKEN_KEY);
    const expiry = sessionStorage.getItem(this.TOKEN_EXPIRY_KEY);

    if (!token || !expiry) return null;

    // Check if token is expired
    if (Date.now() > parseInt(expiry)) {
      this.clearTokens();
      return null;
    }

    return token;
  }

  // Check if token is expired
  static isTokenExpired(): boolean {
    const expiry = sessionStorage.getItem(this.TOKEN_EXPIRY_KEY);
    if (!expiry) return true;

    return Date.now() > parseInt(expiry);
  }

  // Refresh access token
  static async refreshAccessToken(): Promise<string | null> {
    try {
      const refreshToken = this.getRefreshToken();
      if (!refreshToken) return null;

      const response = await fetch('/api/auth/refresh', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refreshToken }),
        credentials: 'include' // Include cookies
      });

      if (!response.ok) {
        this.clearTokens();
        return null;
      }

      const data = await response.json();
      this.setTokens(data.accessToken, data.refreshToken, data.expiresIn);

      return data.accessToken;
    } catch (error) {
      console.error('Token refresh failed:', error);
      this.clearTokens();
      return null;
    }
  }

  // Get refresh token from cookie
  private static getRefreshToken(): string | null {
    return this.getSecureCookie(this.REFRESH_TOKEN_KEY);
  }

  // Clear all tokens
  static clearTokens() {
    sessionStorage.removeItem(this.ACCESS_TOKEN_KEY);
    sessionStorage.removeItem(this.TOKEN_EXPIRY_KEY);
    this.deleteSecureCookie(this.REFRESH_TOKEN_KEY);
  }

  // Secure cookie methods
  private static setSecureCookie(name: string, value: string, options: any) {
    let cookieString = `${name}=${value};path=/;SameSite=Strict`;

    if (options.days) {
      const expires = new Date();
      expires.setTime(expires.getTime() + (options.days * 24 * 60 * 60 * 1000));
      cookieString += `;expires=${expires.toUTCString()}`;
    }

    if (options.secure) cookieString += ';Secure';
    if (options.httpOnly) cookieString += ';HttpOnly';

    document.cookie = cookieString;
  }

  private static getSecureCookie(name: string): string | null {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');

    for (let i = 0; i < ca.length; i++) {
      let c = ca[i];
      while (c.charAt(0) === ' ') c = c.substring(1, c.length);
      if (c.indexOf(nameEQ) === 0) {
        return c.substring(nameEQ.length, c.length);
      }
    }
    return null;
  }

  private static deleteSecureCookie(name: string) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;`;
  }
}
```

**2. API Interceptor with Auto Refresh:**
```javascript
// API Interceptor with automatic token refresh
class ApiInterceptor {
  private static isRefreshing = false;
  private static failedQueue: Array<{
    resolve: (value: any) => void;
    reject: (error: any) => void;
  }> = [];

  static async request(url: string, options: RequestInit = {}): Promise<Response> {
    let token = TokenManager.getAccessToken();

    // If token is expired, try to refresh
    if (TokenManager.isTokenExpired()) {
      token = await this.refreshTokenIfNeeded();
    }

    const headers = {
      'Content-Type': 'application/json',
      ...(token && { Authorization: `Bearer ${token}` }),
      ...options.headers
    };

    try {
      const response = await fetch(url, {
        ...options,
        headers
      });

      // If 401, try to refresh token and retry
      if (response.status === 401) {
        const newToken = await this.refreshTokenIfNeeded();
        if (newToken) {
          return this.request(url, {
            ...options,
            headers: {
              ...headers,
              Authorization: `Bearer ${newToken}`
            }
          });
        }
      }

      return response;
    } catch (error) {
      throw error;
    }
  }

  private static async refreshTokenIfNeeded(): Promise<string | null> {
    if (this.isRefreshing) {
      // If already refreshing, wait for it to complete
      return new Promise((resolve, reject) => {
        this.failedQueue.push({ resolve, reject });
      });
    }

    this.isRefreshing = true;

    try {
      const newToken = await TokenManager.refreshAccessToken();
      this.processQueue(null, newToken);
      return newToken;
    } catch (error) {
      this.processQueue(error, null);
      return null;
    } finally {
      this.isRefreshing = false;
    }
  }

  private static processQueue(error: any, token: string | null) {
    this.failedQueue.forEach(({ resolve, reject }) => {
      if (error) {
        reject(error);
      } else {
        resolve(token);
      }
    });

    this.failedQueue = [];
  }
}
```

**3. JWT Token Validation:**
```javascript
// JWT Token Validation and Decoding
class JWTValidator {
  static decodeToken(token: string): any {
    try {
      const base64Url = token.split('.')[1];
      const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
      const jsonPayload = decodeURIComponent(
        atob(base64)
          .split('')
          .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
          .join('')
      );
      return JSON.parse(jsonPayload);
    } catch (error) {
      console.error('Token decode error:', error);
      return null;
    }
  }

  static isTokenValid(token: string): boolean {
    const decoded = this.decodeToken(token);
    if (!decoded) return false;

    const now = Date.now() / 1000;
    return decoded.exp > now;
  }

  static getTokenExpiry(token: string): Date | null {
    const decoded = this.decodeToken(token);
    if (!decoded || !decoded.exp) return null;

    return new Date(decoded.exp * 1000);
  }

  static getTokenPayload(token: string): any {
    return this.decodeToken(token);
  }
}
```

---

### **Q14: Frontend Security - XSS, CORS, CSRF** 🔥

#### **🔍 Câu Hỏi:**
Security (XSS, CORS, CSRF), Pentest Frontend, issue?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 XSS (Cross-Site Scripting)**: Injection of malicious scripts vào web pages
  - *Là gì*: Attacker inject malicious JavaScript code vào website
  - *Tại sao nguy hiểm*: Có thể steal cookies, session tokens, user data
  - *Khi nào xảy ra*: Khi user input không được sanitize properly

- **🎯 CORS (Cross-Origin Resource Sharing)**: Policy cho cross-origin requests
  - *Là gì*: Mechanism cho phép web pages access resources từ different domains
  - *Tại sao cần*: Bảo vệ users khỏi malicious websites
  - *Khi nào dùng*: API calls từ different domains, third-party integrations

- **⚡ CSRF (Cross-Site Request Forgery)**: Unauthorized actions từ authenticated users
  - *Là gì*: Attacker trick user thực hiện actions họ không muốn
  - *Tại sao nguy hiểm*: Có thể thực hiện actions với quyền của user
  - *Khi nào xảy ra*: Khi không có proper CSRF protection

- **✅ Security Best Practices**: Thực hành bảo mật tốt nhất
  - *Input Validation*: Validate và sanitize tất cả user input
  - *Output Encoding*: Encode output để prevent XSS
  - *CSP Headers*: Content Security Policy để prevent XSS
  - *CSRF Tokens*: Sử dụng CSRF tokens cho state-changing operations

- **⚠️ Common Vulnerabilities**: Các lỗ hổng bảo mật thường gặp
  - *Unvalidated Redirects*: Redirect users đến malicious sites
  - *Insecure Direct Object References*: Access resources không được authorize
  - *Security Misconfiguration*: Cấu hình bảo mật không đúng
  - *Sensitive Data Exposure*: Expose sensitive data trong client-side code

**1. XSS Protection:**
```javascript
// XSS Protection Utilities - Tối ưu nhất cho XSS prevention
class XSSProtection {
  // Sanitize user input - Sanitize input từ user - tối ưu cho XSS prevention
  static sanitizeInput(input: string): string { // Sanitize input - tối ưu cho security
    const div = document.createElement('div'); // Create div element - tối ưu cho DOM manipulation
    div.textContent = input; // Set text content - tối ưu cho safe content setting
    return div.innerHTML; // Return innerHTML - tối ưu cho safe HTML output
  }

  // Escape HTML characters
  static escapeHtml(text: string): string {
    const map: { [key: string]: string } = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#039;'
    };

    return text.replace(/[&<>"']/g, (m) => map[m]);
  }

  // Validate and sanitize URL
  static sanitizeUrl(url: string): string {
    try {
      const urlObj = new URL(url);
      // Only allow http and https protocols
      if (urlObj.protocol === 'http:' || urlObj.protocol === 'https:') {
        return urlObj.toString();
      }
      return '';
    } catch {
      return '';
    }
  }

  // Content Security Policy helper
  static setCSP() {
    const meta = document.createElement('meta');
    meta.httpEquiv = 'Content-Security-Policy';
    meta.content = `
      default-src 'self';
      script-src 'self' 'unsafe-inline' https://trusted-cdn.com;
      style-src 'self' 'unsafe-inline';
      img-src 'self' data: https:;
      connect-src 'self' https://api.example.com;
      font-src 'self';
      object-src 'none';
      base-uri 'self';
      form-action 'self';
    `.replace(/\s+/g, ' ').trim();

    document.head.appendChild(meta);
  }
}

// Safe HTML rendering
function SafeHTML({ content }: { content: string }) {
  const sanitizedContent = XSSProtection.sanitizeInput(content);

  return (
    <div
      dangerouslySetInnerHTML={{ __html: sanitizedContent }}
    />
  );
}
```

**2. CORS Configuration:**
```javascript
// CORS Configuration and Handling
class CORSHandler {
  static async makeCORSRequest(url: string, options: RequestInit = {}) {
    const corsOptions: RequestInit = {
      ...options,
      mode: 'cors',
      credentials: 'include',
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': window.location.origin,
        ...options.headers
      }
    };

    try {
      const response = await fetch(url, corsOptions);

      if (!response.ok) {
        throw new Error(`CORS request failed: ${response.status}`);
      }

      return response;
    } catch (error) {
      console.error('CORS Error:', error);
      throw error;
    }
  }

  // Preflight request handler
  static async handlePreflight(url: string, method: string) {
    const response = await fetch(url, {
      method: 'OPTIONS',
      headers: {
        'Access-Control-Request-Method': method,
        'Access-Control-Request-Headers': 'Content-Type, Authorization'
      }
    });

    return response.ok;
  }
}

// Server-side CORS configuration (Node.js/Express)
const corsConfig = {
  origin: (origin: string, callback: Function) => {
    const allowedOrigins = [
      'https://yourdomain.com',
      'https://www.yourdomain.com',
      'http://localhost:3000'
    ];

    if (!origin || allowedOrigins.includes(origin)) {
      callback(null, true);
    } else {
      callback(new Error('Not allowed by CORS'));
    }
  },
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
  allowedHeaders: ['Content-Type', 'Authorization', 'X-CSRF-Token'],
  exposedHeaders: ['X-Total-Count']
};
```

**3. CSRF Protection:**
```javascript
// CSRF Protection
class CSRFProtection {
  private static token: string | null = null;

  // Generate CSRF token
  static generateToken(): string {
    const array = new Uint8Array(32);
    crypto.getRandomValues(array);
    this.token = Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
    return this.token;
  }

  // Get CSRF token
  static getToken(): string {
    if (!this.token) {
      return this.generateToken();
    }
    return this.token;
  }

  // Validate CSRF token
  static validateToken(token: string): boolean {
    return this.token === token;
  }

  // Add CSRF token to requests
  static addCSRFToken(options: RequestInit): RequestInit {
    return {
      ...options,
      headers: {
        ...options.headers,
        'X-CSRF-Token': this.getToken()
      }
    };
  }
}

// CSRF Protected Form Component
function CSRFProtectedForm({ onSubmit }: { onSubmit: (data: FormData) => void }) {
  const [csrfToken] = useState(() => CSRFProtection.generateToken());

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    formData.append('csrf_token', csrfToken);
    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="hidden" name="csrf_token" value={csrfToken} />
      {/* Form fields */}
    </form>
  );
}
```

**4. Security Headers:**
```javascript
// Security Headers Configuration
class SecurityHeaders {
  static setSecurityHeaders() {
    // Set security headers via meta tags
    const headers = [
      {
        name: 'X-Content-Type-Options',
        content: 'nosniff'
      },
      {
        name: 'X-Frame-Options',
        content: 'DENY'
      },
      {
        name: 'X-XSS-Protection',
        content: '1; mode=block'
      },
      {
        name: 'Referrer-Policy',
        content: 'strict-origin-when-cross-origin'
      },
      {
        name: 'Permissions-Policy',
        content: 'camera=(), microphone=(), geolocation=()'
      }
    ];

    headers.forEach(header => {
      const meta = document.createElement('meta');
      meta.httpEquiv = header.name;
      meta.content = header.content;
      document.head.appendChild(meta);
    });
  }
}
```

**5. Input Validation:**
```javascript
// Input Validation and Sanitization
class InputValidator {
  static validateEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  static validatePassword(password: string): {
    isValid: boolean;
    errors: string[];
  } {
    const errors: string[] = [];

    if (password.length < 8) {
      errors.push('Password must be at least 8 characters long');
    }

    if (!/[A-Z]/.test(password)) {
      errors.push('Password must contain at least one uppercase letter');
    }

    if (!/[a-z]/.test(password)) {
      errors.push('Password must contain at least one lowercase letter');
    }

    if (!/\d/.test(password)) {
      errors.push('Password must contain at least one number');
    }

    if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
      errors.push('Password must contain at least one special character');
    }

    return {
      isValid: errors.length === 0,
      errors
    };
  }

  static sanitizeFilename(filename: string): string {
    return filename
      .replace(/[^a-zA-Z0-9.-]/g, '_')
      .replace(/_{2,}/g, '_')
      .substring(0, 255);
  }

  static validateUrl(url: string): boolean {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  }
}
```

**6. Security Audit Checklist:**
```javascript
// Security Audit Checklist
class SecurityAudit {
  static async runSecurityAudit(): Promise<{
    score: number;
    issues: string[];
    recommendations: string[];
  }> {
    const issues: string[] = [];
    const recommendations: string[] = [];

    // Check for HTTPS
    if (location.protocol !== 'https:') {
      issues.push('Site is not using HTTPS');
      recommendations.push('Enable HTTPS for all connections');
    }

    // Check for security headers
    const securityHeaders = [
      'X-Content-Type-Options',
      'X-Frame-Options',
      'X-XSS-Protection'
    ];

    securityHeaders.forEach(header => {
      if (!document.querySelector(`meta[http-equiv="${header}"]`)) {
        issues.push(`Missing security header: ${header}`);
        recommendations.push(`Add ${header} security header`);
      }
    });

    // Check for CSP
    if (!document.querySelector('meta[http-equiv="Content-Security-Policy"]')) {
      issues.push('Missing Content Security Policy');
      recommendations.push('Implement Content Security Policy');
    }

    // Check for insecure forms
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
      if (form.action.startsWith('http://')) {
        issues.push('Form action uses insecure HTTP');
        recommendations.push('Use HTTPS for form actions');
      }
    });

    // Check for external scripts
    const scripts = document.querySelectorAll('script[src]');
    scripts.forEach(script => {
      const src = script.getAttribute('src');
      if (src && !src.startsWith('https://') && !src.startsWith('/')) {
        issues.push('External script not using HTTPS');
        recommendations.push('Use HTTPS for external scripts');
      }
    });

    const score = Math.max(0, 100 - (issues.length * 10));

    return { score, issues, recommendations };
  }
}
```

---

### **Q15: Testable Code - Code Dễ Test** 🔥

#### **🔍 Câu Hỏi:**
How to Write code easy to test?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Testable Code Principles**: Các nguyên tắc viết code dễ test
  - *Là gì*: Code được thiết kế để dễ dàng viết unit tests, integration tests
  - *Tại sao cần*: Đảm bảo code quality, catch bugs sớm, refactor an toàn
  - *Khi nào áp dụng*: Mọi dự án, đặc biệt quan trọng với production code

- **🎯 Single Responsibility Principle**: Mỗi function/class chỉ làm một việc
  - *Là gì*: Mỗi function/class chỉ có một lý do để thay đổi
  - *Tại sao cần*: Dễ test, dễ maintain, ít dependencies
  - *Khi nào dùng*: Khi thiết kế functions và classes

- **⚡ Dependency Injection**: Inject dependencies thay vì tạo bên trong
  - *Là gì*: Pass dependencies vào function/class thay vì tạo bên trong
  - *Tại sao cần*: Dễ mock dependencies, test isolated
  - *Khi nào dùng*: Khi function cần external dependencies

- **✅ Pure Functions**: Functions không có side effects
  - *Là gì*: Functions luôn return same output cho same input
  - *Tại sao cần*: Dễ test, predictable, không có side effects
  - *Khi nào dùng*: Utility functions, data transformations

- **⚠️ Avoid Global State**: Tránh global state khi có thể
  - *Là gì*: Không dựa vào global variables, shared state
  - *Tại sao cần*: Dễ test, predictable behavior
  - *Khi nào tránh*: Khi có thể pass data qua parameters

**1. Pure Functions:**
```javascript
// ✅ TỐI ƯU NHẤT: Pure functions are easy to test - Tối ưu nhất cho testing
function calculateTotal(items: Item[]): number { // Pure function - tối ưu cho predictability
  return items.reduce((total, item) => total + item.price, 0); // Reduce operation - tối ưu cho performance
}

function formatCurrency(amount: number, currency: string = 'USD'): string { // Pure function - tối ưu cho testing
  return new Intl.NumberFormat('en-US', { // Intl API - tối ưu cho internationalization
    style: 'currency', // Currency style - tối ưu cho formatting
    currency // Currency code - tối ưu cho localization
  }).format(amount); // Format amount - tối ưu cho display
}

// ❌ Bad: Side effects make testing difficult
function calculateTotalWithSideEffects(items: Item[]): number {
  console.log('Calculating total...'); // Side effect
  const total = items.reduce((sum, item) => sum + item.price, 0);
  localStorage.setItem('lastTotal', total.toString()); // Side effect
  return total;
}
```

**2. Dependency Injection:**
```javascript
// ✅ Good: Dependencies injected for easy testing
class UserService {
  constructor(
    private apiClient: ApiClient,
    private logger: Logger
  ) {}

  async getUser(id: number): Promise<User> {
    try {
      this.logger.info(`Fetching user ${id}`);
      const user = await this.apiClient.get(`/users/${id}`);
      this.logger.info(`User ${id} fetched successfully`);
      return user;
    } catch (error) {
      this.logger.error(`Failed to fetch user ${id}:`, error);
      throw error;
    }
  }
}

// ❌ Bad: Hard dependencies make testing difficult
class UserService {
  async getUser(id: number): Promise<User> {
    // Hard to test because of direct dependencies
    const response = await fetch(`https://api.example.com/users/${id}`);
    console.log(`Fetching user ${id}`);
    return response.json();
  }
}
```

**3. Testable React Components:**
```javascript
// ✅ Good: Testable component with clear props and behavior
interface UserCardProps {
  user: User;
  onEdit: (user: User) => void;
  onDelete: (userId: number) => void;
  isLoading?: boolean;
}

function UserCard({ user, onEdit, onDelete, isLoading = false }: UserCardProps) {
  if (isLoading) {
    return <div data-testid="loading">Loading...</div>;
  }

  return (
    <div data-testid="user-card">
      <h3>{user.name}</h3>
      <p>{user.email}</p>
      <button
        data-testid="edit-button"
        onClick={() => onEdit(user)}
      >
        Edit
      </button>
      <button
        data-testid="delete-button"
        onClick={() => onDelete(user.id)}
      >
        Delete
      </button>
    </div>
  );
}

// Test example
describe('UserCard', () => {
  it('should render user information', () => {
    const user = { id: 1, name: 'John Doe', email: 'john@example.com' };
    const onEdit = jest.fn();
    const onDelete = jest.fn();

    render(
      <UserCard
        user={user}
        onEdit={onEdit}
        onDelete={onDelete}
      />
    );

    expect(screen.getByText('John Doe')).toBeInTheDocument();
    expect(screen.getByText('john@example.com')).toBeInTheDocument();
  });

  it('should call onEdit when edit button is clicked', () => {
    const user = { id: 1, name: 'John Doe', email: 'john@example.com' };
    const onEdit = jest.fn();
    const onDelete = jest.fn();

    render(
      <UserCard
        user={user}
        onEdit={onEdit}
        onDelete={onDelete}
      />
    );

    fireEvent.click(screen.getByTestId('edit-button'));
    expect(onEdit).toHaveBeenCalledWith(user);
  });
});
```

**4. Custom Hooks Testing:**
```javascript
// ✅ Good: Testable custom hook
function useCounter(initialValue: number = 0) {
  const [count, setCount] = useState(initialValue);

  const increment = useCallback(() => {
    setCount(prev => prev + 1);
  }, []);

  const decrement = useCallback(() => {
    setCount(prev => prev - 1);
  }, []);

  const reset = useCallback(() => {
    setCount(initialValue);
  }, [initialValue]);

  return { count, increment, decrement, reset };
}

// Test example
describe('useCounter', () => {
  it('should initialize with default value', () => {
    const { result } = renderHook(() => useCounter());
    expect(result.current.count).toBe(0);
  });

  it('should initialize with custom value', () => {
    const { result } = renderHook(() => useCounter(10));
    expect(result.current.count).toBe(10);
  });

  it('should increment count', () => {
    const { result } = renderHook(() => useCounter());
    act(() => {
      result.current.increment();
    });
    expect(result.current.count).toBe(1);
  });

  it('should decrement count', () => {
    const { result } = renderHook(() => useCounter(5));
    act(() => {
      result.current.decrement();
    });
    expect(result.current.count).toBe(4);
  });

  it('should reset count', () => {
    const { result } = renderHook(() => useCounter(10));
    act(() => {
      result.current.increment();
      result.current.increment();
    });
    expect(result.current.count).toBe(12);

    act(() => {
      result.current.reset();
    });
    expect(result.current.count).toBe(10);
  });
});
```

**5. API Service Testing:**
```javascript
// ✅ Good: Testable API service
class ApiService {
  constructor(
    private baseURL: string,
    private httpClient: HttpClient = new FetchHttpClient()
  ) {}

  async get<T>(endpoint: string): Promise<T> {
    return this.httpClient.get(`${this.baseURL}${endpoint}`);
  }

  async post<T>(endpoint: string, data: any): Promise<T> {
    return this.httpClient.post(`${this.baseURL}${endpoint}`, data);
  }
}

// Mock HTTP client for testing
class MockHttpClient implements HttpClient {
  private responses: Map<string, any> = new Map();

  setResponse(url: string, response: any) {
    this.responses.set(url, response);
  }

  async get<T>(url: string): Promise<T> {
    const response = this.responses.get(url);
    if (!response) {
      throw new Error(`No mock response for ${url}`);
    }
    return response;
  }

  async post<T>(url: string, data: any): Promise<T> {
    const response = this.responses.get(url);
    if (!response) {
      throw new Error(`No mock response for ${url}`);
    }
    return response;
  }
}

// Test example
describe('ApiService', () => {
  let apiService: ApiService;
  let mockHttpClient: MockHttpClient;

  beforeEach(() => {
    mockHttpClient = new MockHttpClient();
    apiService = new ApiService('https://api.example.com', mockHttpClient);
  });

  it('should fetch user data', async () => {
    const mockUser = { id: 1, name: 'John Doe', email: 'john@example.com' };
    mockHttpClient.setResponse('https://api.example.com/users/1', mockUser);

    const user = await apiService.get('/users/1');
    expect(user).toEqual(mockUser);
  });

  it('should create user', async () => {
    const newUser = { name: 'Jane Doe', email: 'jane@example.com' };
    const createdUser = { id: 2, ...newUser };
    mockHttpClient.setResponse('https://api.example.com/users', createdUser);

    const user = await apiService.post('/users', newUser);
    expect(user).toEqual(createdUser);
  });
});
```

**6. Error Handling Testing:**
```javascript
// ✅ Good: Testable error handling
class ErrorHandler {
  constructor(private logger: Logger) {}

  handleError(error: Error, context?: string): void {
    const errorInfo = {
      message: error.message,
      stack: error.stack,
      context,
      timestamp: new Date().toISOString()
    };

    this.logger.error('Application error:', errorInfo);

    // Send to error tracking service
    this.sendToErrorTracking(errorInfo);
  }

  private sendToErrorTracking(errorInfo: any): void {
    // Implementation for error tracking
  }
}

// Test example
describe('ErrorHandler', () => {
  let errorHandler: ErrorHandler;
  let mockLogger: jest.Mocked<Logger>;

  beforeEach(() => {
    mockLogger = {
      error: jest.fn(),
      info: jest.fn(),
      warn: jest.fn()
    };
    errorHandler = new ErrorHandler(mockLogger);
  });

  it('should log error with context', () => {
    const error = new Error('Test error');
    const context = 'UserService.getUser';

    errorHandler.handleError(error, context);

    expect(mockLogger.error).toHaveBeenCalledWith(
      'Application error:',
      expect.objectContaining({
        message: 'Test error',
        context: 'UserService.getUser',
        timestamp: expect.any(String)
      })
    );
  });
});
```

**7. Testing Best Practices:**
```javascript
// Testing utilities and helpers
class TestUtils {
  // Create mock data
  static createMockUser(overrides: Partial<User> = {}): User {
    return {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com',
      ...overrides
    };
  }

  // Wait for async operations
  static async waitFor(condition: () => boolean, timeout = 1000): Promise<void> {
    const start = Date.now();
    while (!condition() && Date.now() - start < timeout) {
      await new Promise(resolve => setTimeout(resolve, 10));
    }
    if (!condition()) {
      throw new Error('Condition not met within timeout');
    }
  }

  // Mock fetch responses
  static mockFetch(response: any, status = 200) {
    global.fetch = jest.fn().mockResolvedValue({
      ok: status >= 200 && status < 300,
      status,
      json: () => Promise.resolve(response)
    });
  }

  // Reset all mocks
  static resetAllMocks() {
    jest.clearAllMocks();
    jest.resetAllMocks();
  }
}

// Test configuration
const testConfig = {
  // Test database URL
  databaseUrl: process.env.TEST_DATABASE_URL || 'sqlite://:memory:',

  // Test timeout
  timeout: 10000,

  // Mock external services
  mockExternalServices: true,

  // Test data cleanup
  cleanupAfterEach: true
};
```

---

### **Q16: Development Tools - ESLint, Prettier, Husky** 🔥

#### **🔍 Câu Hỏi:**
Tool used for setup, cleancode: ESLint, Prettier, Husky git hook, Editor config?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 ESLint**: JavaScript/TypeScript linter để catch errors và enforce coding standards
  - *Là gì*: Static analysis tool để identify và fix problems trong code
  - *Tại sao cần*: Catch bugs sớm, enforce coding standards, improve code quality
  - *Khi nào dùng*: Mọi JavaScript/TypeScript project, đặc biệt team projects

- **🎯 Prettier**: Code formatter để maintain consistent code style
  - *Là gì*: Opinionated code formatter với minimal configuration
  - *Tại sao cần*: Consistent code formatting, reduce code review time
  - *Khi nào dùng*: Khi cần consistent formatting across team

- **⚡ Husky**: Git hooks để run scripts trước khi commit/push
  - *Là gì*: Tool để manage Git hooks và run scripts
  - *Tại sao cần*: Ensure code quality trước khi commit, run tests
  - *Khi nào dùng*: Khi cần enforce quality gates trong Git workflow

- **✅ EditorConfig**: Maintain consistent coding styles across editors
  - *Là gì*: File để maintain consistent coding styles across different editors
  - *Tại sao cần*: Consistent formatting across team members
  - *Khi nào dùng*: Team projects với multiple editors

- **⚠️ Integration Benefits**: Lợi ích khi tích hợp các tools
  - *Code Quality*: Consistent, high-quality code across team
  - *Developer Experience*: Faster development, fewer bugs
  - *Team Collaboration*: Consistent standards, easier code reviews
  - *CI/CD*: Automated quality checks trong build process

**1. ESLint Configuration:**
```javascript
// .eslintrc.js - Tối ưu nhất cho code quality
module.exports = {
  env: { // Environment settings - tối ưu cho compatibility
    browser: true, // Browser environment - tối ưu cho frontend development
    es2021: true, // ES2021 features - tối ưu cho modern JavaScript
    node: true, // Node.js environment - tối ưu cho build tools
    jest: true // Jest testing environment - tối ưu cho testing
  },
  extends: [ // Extend configurations - tối ưu cho rule inheritance
    'eslint:recommended', // ESLint recommended rules - tối ưu cho best practices
    '@typescript-eslint/recommended', // TypeScript rules - tối ưu cho type safety
    'plugin:react/recommended', // React rules - tối ưu cho React development
    'plugin:react-hooks/recommended',
    'plugin:jsx-a11y/recommended',
    'plugin:import/recommended',
    'plugin:import/typescript'
  ],
  parser: '@typescript-eslint/parser',
  parserOptions: {
    ecmaFeatures: {
      jsx: true
    },
    ecmaVersion: 12,
    sourceType: 'module'
  },
  plugins: [
    'react',
    '@typescript-eslint',
    'jsx-a11y',
    'import',
    'prettier'
  ],
  rules: {
    'prettier/prettier': 'error',
    'react/react-in-jsx-scope': 'off',
    'react/prop-types': 'off',
    '@typescript-eslint/explicit-function-return-type': 'off',
    '@typescript-eslint/explicit-module-boundary-types': 'off',
    '@typescript-eslint/no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'import/order': ['error', {
      groups: ['builtin', 'external', 'internal', 'parent', 'sibling', 'index'],
      'newlines-between': 'always'
    }],
    'no-console': 'warn',
    'no-debugger': 'error'
  },
  settings: {
    react: {
      version: 'detect'
    },
    'import/resolver': {
      typescript: {
        alwaysTryTypes: true
      }
    }
  }
};
```

**2. Prettier Configuration:**
```javascript
// .prettierrc.js
module.exports = {
  semi: true,
  trailingComma: 'es5',
  singleQuote: true,
  printWidth: 80,
  tabWidth: 2,
  useTabs: false,
  bracketSpacing: true,
  bracketSameLine: false,
  arrowParens: 'avoid',
  endOfLine: 'lf',
  quoteProps: 'as-needed',
  jsxSingleQuote: true,
  proseWrap: 'preserve'
};
```

**3. Husky Git Hooks:**
```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged",
      "commit-msg": "commitlint -E HUSKY_GIT_PARAMS",
      "pre-push": "npm run test:coverage"
    }
  },
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": [
      "eslint --fix",
      "prettier --write"
    ],
    "*.{json,md,css,scss}": [
      "prettier --write"
    ]
  }
}
```

**4. EditorConfig:**
```ini
# .editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true
indent_style = space
indent_size = 2

[*.md]
trim_trailing_whitespace = false

[*.{yml,yaml}]
indent_size = 2

[*.json]
indent_size = 2
```

---

### **Q17: External Library vs Self-implement** 🔥

#### **🔍 Câu Hỏi:**
Using external library vs self-implement opinions?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 External Library**: Sử dụng thư viện có sẵn từ community
  - *Là gì*: Sử dụng packages đã được develop và maintain bởi community
  - *Tại sao cần*: Tiết kiệm thời gian, tested code, community support
  - *Khi nào dùng*: Khi có library phù hợp, không cần customization nhiều

- **🎯 Self-implement**: Tự implement functionality từ đầu
  - *Là gì*: Viết code từ đầu thay vì sử dụng external library
  - *Tại sao cần*: Full control, no dependencies, custom requirements
  - *Khi nào dùng*: Khi cần customization cao, không có library phù hợp

- **⚡ Decision Factors**: Các yếu tố quyết định
  - *Project Timeline*: Thời gian có hạn thì dùng external library
  - *Customization Needs*: Cần customization cao thì self-implement
  - *Team Expertise*: Team có expertise thì có thể self-implement
  - *Maintenance Overhead*: External library có maintenance overhead

- **✅ External Library Advantages**: Ưu điểm của external library
  - *Time Saving*: Tiết kiệm thời gian development
  - *Tested Code*: Code đã được test và review
  - *Community Support*: Có community support và documentation
  - *Regular Updates*: Được update và fix bugs thường xuyên

- **⚠️ Self-implement Advantages**: Ưu điểm của self-implement
  - *Full Control*: Kiểm soát hoàn toàn code
  - *No Dependencies*: Không phụ thuộc vào external packages
  - *Custom Requirements*: Có thể implement exact requirements
  - *Learning Experience*: Team học được nhiều từ việc implement

**1. Decision Matrix:**
```javascript
// Decision factors for library vs self-implement - Tối ưu nhất cho decision making
const decisionFactors = {
  // Use external library when: - Dùng external library khi - tối ưu cho time saving
  externalLibrary: {
    complexity: 'High complexity, well-tested solution exists', // High complexity - tối ưu cho proven solutions
    maintenance: 'Active community, regular updates', // Active maintenance - tối ưu cho long-term support
    security: 'Security-critical, battle-tested', // Security critical - tối ưu cho security
    time: 'Tight deadline, need quick solution',
    team: 'Team lacks expertise in domain',
    features: 'Rich feature set, extensible'
  },

  // Self-implement when:
  selfImplement: {
    complexity: 'Simple functionality, specific requirements',
    maintenance: 'Full control over updates and changes',
    security: 'Sensitive data, custom security needs',
    time: 'Long-term project, can invest time',
    team: 'Team has strong expertise',
    features: 'Minimal features, lightweight solution'
  }
};
```

**2. Library Evaluation Checklist:**
```javascript
// Library evaluation criteria
class LibraryEvaluator {
  static evaluateLibrary(library: {
    name: string;
    downloads: number;
    lastUpdated: Date;
    issues: number;
    stars: number;
    bundleSize: number;
    dependencies: string[];
  }) {
    const score = {
      popularity: this.calculatePopularityScore(library),
      maintenance: this.calculateMaintenanceScore(library),
      size: this.calculateSizeScore(library),
      security: this.calculateSecurityScore(library),
      compatibility: this.calculateCompatibilityScore(library)
    };

    return {
      totalScore: Object.values(score).reduce((sum, val) => sum + val, 0),
      breakdown: score,
      recommendation: this.getRecommendation(score)
    };
  }

  private static calculatePopularityScore(lib: any): number {
    const downloads = Math.min(lib.downloads / 1000000, 10); // Max 10 points
    const stars = Math.min(lib.stars / 1000, 5); // Max 5 points
    return downloads + stars;
  }

  private static calculateMaintenanceScore(lib: any): number {
    const daysSinceUpdate = (Date.now() - lib.lastUpdated.getTime()) / (1000 * 60 * 60 * 24);
    const updateScore = Math.max(0, 10 - daysSinceUpdate / 30); // 10 points if updated within 30 days
    const issueScore = Math.max(0, 5 - lib.issues / 100); // 5 points if less than 100 issues
    return updateScore + issueScore;
  }

  private static calculateSizeScore(lib: any): number {
    const sizeInKB = lib.bundleSize / 1024;
    if (sizeInKB < 10) return 10;
    if (sizeInKB < 50) return 8;
    if (sizeInKB < 100) return 5;
    return 2;
  }

  private static calculateSecurityScore(lib: any): number {
    // Check for security vulnerabilities
    const hasVulnerabilities = lib.vulnerabilities && lib.vulnerabilities.length > 0;
    return hasVulnerabilities ? 0 : 10;
  }

  private static calculateCompatibilityScore(lib: any): number {
    const peerDeps = lib.dependencies.filter((dep: string) => dep.startsWith('react'));
    return peerDeps.length === 0 ? 10 : 5; // Simpler dependencies = better
  }

  private static getRecommendation(score: any): string {
    const total = Object.values(score).reduce((sum: number, val: number) => sum + val, 0);
    if (total >= 40) return 'Highly recommended';
    if (total >= 30) return 'Recommended';
    if (total >= 20) return 'Consider alternatives';
    return 'Not recommended';
  }
}
```

**3. Self-Implementation Examples:**
```javascript
// ✅ Good: Simple utility functions - self-implement
class DateUtils {
  static formatDate(date: Date, format: string = 'YYYY-MM-DD'): string {
    const year = date.getFullYear();
    const month = String(date.getMonth() + 1).padStart(2, '0');
    const day = String(date.getDate()).padStart(2, '0');

    return format
      .replace('YYYY', year.toString())
      .replace('MM', month)
      .replace('DD', day);
  }

  static addDays(date: Date, days: number): Date {
    const result = new Date(date);
    result.setDate(result.getDate() + days);
    return result;
  }

  static isWeekend(date: Date): boolean {
    const day = date.getDay();
    return day === 0 || day === 6; // Sunday or Saturday
  }
}

// ✅ Good: Custom validation - self-implement
class ValidationUtils {
  static validateEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  static validatePassword(password: string): {
    isValid: boolean;
    errors: string[];
  } {
    const errors: string[] = [];

    if (password.length < 8) {
      errors.push('Password must be at least 8 characters');
    }

    if (!/[A-Z]/.test(password)) {
      errors.push('Password must contain uppercase letter');
    }

    if (!/[a-z]/.test(password)) {
      errors.push('Password must contain lowercase letter');
    }

    if (!/\d/.test(password)) {
      errors.push('Password must contain number');
    }

    return {
      isValid: errors.length === 0,
      errors
    };
  }
}
```

**4. External Library Examples:**
```javascript
// ✅ Good: Complex functionality - use external library
import { debounce } from 'lodash-es';
import { format, parseISO, addDays } from 'date-fns';
import { z } from 'zod';

// Debouncing with lodash
const debouncedSearch = debounce((query: string) => {
  // Search logic
}, 300);

// Date manipulation with date-fns
const formattedDate = format(new Date(), 'yyyy-MM-dd');
const futureDate = addDays(new Date(), 7);

// Schema validation with Zod
const userSchema = z.object({
  name: z.string().min(1),
  email: z.string().email(),
  age: z.number().min(0).max(120)
});

const validateUser = (data: unknown) => {
  return userSchema.parse(data);
};
```

**5. Hybrid Approach:**
```javascript
// ✅ Good: Hybrid approach - extend external library
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

// Custom store with external library
interface AppState {
  user: User | null;
  theme: 'light' | 'dark';
  setUser: (user: User | null) => void;
  setTheme: (theme: 'light' | 'dark') => void;
  reset: () => void;
}

const useAppStore = create<AppState>()(
  persist(
    (set) => ({
      user: null,
      theme: 'light',
      setUser: (user) => set({ user }),
      setTheme: (theme) => set({ theme }),
      reset: () => set({ user: null, theme: 'light' })
    }),
    {
      name: 'app-storage',
      partialize: (state) => ({ theme: state.theme })
    }
  )
);

// Custom hook wrapping external library
function useAppState() {
  const store = useAppStore();

  return {
    ...store,
    isLoggedIn: !!store.user,
    toggleTheme: () => store.setTheme(store.theme === 'light' ? 'dark' : 'light')
  };
}
```

---

### **Q18: i18n with React - Đa Ngôn Ngữ** 🔥

#### **🔍 Câu Hỏi:**
Multiple language using React i18n?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Internationalization (i18n)**: Hỗ trợ multiple languages trong ứng dụng
  - *Là gì*: Process của việc design và develop ứng dụng để support multiple languages
  - *Tại sao cần*: Reach global audience, improve user experience
  - *Khi nào dùng*: Apps cần support multiple markets, global users

- **🎯 React i18n Libraries**: Các thư viện phổ biến cho React
  - *react-i18next*: Most popular i18n library cho React
  - *react-intl*: FormatJS library với rich formatting features
  - *react-i18n*: Lightweight alternative
  - *Khi nào dùng*: Khi cần i18n support trong React apps

- **⚡ Key Features**: Các tính năng chính của i18n
  - *Translation Management*: Quản lý translations cho multiple languages
  - *Pluralization*: Handle plural forms cho different languages
  - *Date/Number Formatting*: Format dates và numbers theo locale
  - *RTL Support*: Support right-to-left languages

- **✅ Implementation Strategy**: Chiến lược implement i18n
  - *Translation Files*: Organize translations trong separate files
  - *Namespace Organization*: Group translations theo features/pages
  - *Lazy Loading*: Load translations on demand để improve performance
  - *Fallback Language*: Set fallback language khi translation missing

- **⚠️ Common Challenges**: Các thách thức thường gặp
  - *Text Length*: Different languages có different text lengths
  - *Context Awareness*: Same word có different meanings trong different contexts
  - *Pluralization Rules*: Different languages có different plural rules
  - *RTL Layout*: Right-to-left languages cần special layout handling

**1. React i18next Setup:**
```javascript
// i18n.ts - Tối ưu nhất cho internationalization
import i18n from 'i18next'; // i18next core - tối ưu cho i18n functionality
import { initReactI18next } from 'react-i18next'; // React integration - tối ưu cho React apps
import LanguageDetector from 'i18next-browser-languagedetector'; // Language detection - tối ưu cho auto-detection

// Translation resources - Translation resources - tối ưu cho multi-language support
const resources = { // Resources object - tối ưu cho translation management
  en: {
    translation: {
      welcome: 'Welcome',
      hello: 'Hello {{name}}',
      buttons: {
        save: 'Save',
        cancel: 'Cancel',
        delete: 'Delete'
      },
      messages: {
        success: 'Operation completed successfully',
        error: 'An error occurred'
      }
    }
  },
  vi: {
    translation: {
      welcome: 'Chào mừng',
      hello: 'Xin chào {{name}}',
      buttons: {
        save: 'Lưu',
        cancel: 'Hủy',
        delete: 'Xóa'
      },
      messages: {
        success: 'Thao tác hoàn thành thành công',
        error: 'Đã xảy ra lỗi'
      }
    }
  }
};

i18n
  .use(LanguageDetector)
  .use(initReactI18next)
  .init({
    resources,
    fallbackLng: 'en',
    debug: process.env.NODE_ENV === 'development',

    interpolation: {
      escapeValue: false
    },

    detection: {
      order: ['localStorage', 'navigator', 'htmlTag'],
      caches: ['localStorage']
    }
  });

export default i18n;
```

**2. Custom i18n Hook:**
```javascript
// hooks/useTranslation.ts
import { useTranslation as useI18nTranslation } from 'react-i18next';
import { useCallback } from 'react';

export function useTranslation() {
  const { t, i18n } = useI18nTranslation();

  const changeLanguage = useCallback((lng: string) => {
    i18n.changeLanguage(lng);
  }, [i18n]);

  const getCurrentLanguage = useCallback(() => {
    return i18n.language;
  }, [i18n]);

  const getAvailableLanguages = useCallback(() => {
    return i18n.languages;
  }, [i18n]);

  return {
    t,
    changeLanguage,
    getCurrentLanguage,
    getAvailableLanguages,
    isReady: i18n.isInitialized
  };
}
```

**3. Language Switcher Component:**
```javascript
// components/LanguageSwitcher.tsx
import React from 'react';
import { useTranslation } from '../hooks/useTranslation';

const languages = [
  { code: 'en', name: 'English', flag: '🇺🇸' },
  { code: 'vi', name: 'Tiếng Việt', flag: '🇻🇳' },
  { code: 'ja', name: '日本語', flag: '🇯🇵' }
];

export function LanguageSwitcher() {
  const { changeLanguage, getCurrentLanguage } = useTranslation();
  const currentLanguage = getCurrentLanguage();

  return (
    <div className="language-switcher">
      {languages.map((lang) => (
        <button
          key={lang.code}
          onClick={() => changeLanguage(lang.code)}
          className={`language-button ${
            currentLanguage === lang.code ? 'active' : ''
          }`}
          aria-label={`Switch to ${lang.name}`}
        >
          <span className="flag">{lang.flag}</span>
          <span className="name">{lang.name}</span>
        </button>
      ))}
    </div>
  );
}
```

**4. Translation Component:**
```javascript
// components/Translation.tsx
import React from 'react';
import { useTranslation } from '../hooks/useTranslation';

interface TranslationProps {
  i18nKey: string;
  values?: Record<string, any>;
  fallback?: string;
  className?: string;
}

export function Translation({
  i18nKey,
  values,
  fallback,
  className
}: TranslationProps) {
  const { t } = useTranslation();

  return (
    <span className={className}>
      {t(i18nKey, values) || fallback || i18nKey}
    </span>
  );
}

// Usage
<Translation
  i18nKey="hello"
  values={{ name: 'John' }}
  className="greeting"
/>
```

**5. Pluralization:**
```javascript
// Translation with pluralization
const pluralizationResources = {
  en: {
    translation: {
      items: '{{count}} item',
      items_plural: '{{count}} items',
      messages: {
        zero: 'No messages',
        one: '{{count}} message',
        other: '{{count}} messages'
      }
    }
  },
  vi: {
    translation: {
      items: '{{count}} mục',
      items_plural: '{{count}} mục',
      messages: {
        zero: 'Không có tin nhắn',
        one: '{{count}} tin nhắn',
        other: '{{count}} tin nhắn'
      }
    }
  }
};

// Usage in component
function ItemCounter({ count }: { count: number }) {
  const { t } = useTranslation();

  return (
    <div>
      <p>{t('items', { count })}</p>
      <p>{t('messages', { count })}</p>
    </div>
  );
}
```

**6. Namespace Organization:**
```javascript
// Organized translation files
// locales/en/common.json
{
  "buttons": {
    "save": "Save",
    "cancel": "Cancel",
    "delete": "Delete",
    "edit": "Edit"
  },
  "labels": {
    "name": "Name",
    "email": "Email",
    "password": "Password"
  }
}

// locales/en/auth.json
{
  "login": {
    "title": "Login",
    "email": "Email address",
    "password": "Password",
    "submit": "Sign in",
    "forgot": "Forgot password?"
  },
  "register": {
    "title": "Create account",
    "confirmPassword": "Confirm password",
    "submit": "Sign up"
  }
}

// Usage with namespaces
function LoginForm() {
  const { t } = useTranslation(['auth', 'common']);

  return (
    <form>
      <h1>{t('auth:login.title')}</h1>
      <input placeholder={t('auth:login.email')} />
      <input placeholder={t('auth:login.password')} />
      <button>{t('common:buttons.save')}</button>
    </form>
  );
}
```

**7. Lazy Loading Translations:**
```javascript
// Lazy loading translation files
import i18n from 'i18next';
import Backend from 'i18next-http-backend';

i18n
  .use(Backend)
  .use(initReactI18next)
  .init({
    lng: 'en',
    fallbackLng: 'en',

    backend: {
      loadPath: '/locales/{{lng}}/{{ns}}.json'
    },

    ns: ['common', 'auth', 'dashboard'],
    defaultNS: 'common'
  });

// Dynamic language loading
export async function loadLanguage(language: string) {
  try {
    await i18n.loadLanguages(language);
    await i18n.changeLanguage(language);
  } catch (error) {
    console.error(`Failed to load language ${language}:`, error);
  }
}
```

---

### **Q19: Frontend-Backend Communication** 🔥

#### **🔍 Câu Hỏi:**
How frontend communicate with backend? Give the ways communicate, websocket, Rest API?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 REST API**: Representational State Transfer API cho HTTP communication
  - *Là gì*: Architectural style cho web services sử dụng HTTP methods
  - *Tại sao cần*: Standardized way để communicate với backend
  - *Khi nào dùng*: CRUD operations, data fetching, standard web apps

- **🎯 WebSocket**: Real-time bidirectional communication protocol
  - *Là gì*: Protocol cho persistent connection giữa client và server
  - *Tại sao cần*: Real-time updates, instant messaging, live data
  - *Khi nào dùng*: Chat apps, live notifications, real-time dashboards

- **⚡ GraphQL**: Query language và runtime cho APIs
  - *Là gì*: Query language cho APIs với strong typing và introspection
  - *Tại sao cần*: Efficient data fetching, single endpoint, type safety
  - *Khi nào dùng*: Complex data requirements, mobile apps, microservices

- **✅ Server-Sent Events (SSE)**: One-way communication từ server đến client
  - *Là gì*: HTTP-based technology cho server push events
  - *Tại sao cần*: Real-time updates từ server, simpler than WebSocket
  - *Khi nào dùng*: Live feeds, notifications, progress updates

- **⚠️ gRPC**: High-performance RPC framework
  - *Là gì*: Modern RPC framework sử dụng HTTP/2 và Protocol Buffers
  - *Tại sao cần*: High performance, type safety, streaming
  - *Khi nào dùng*: Microservices, high-performance apps, internal APIs

**1. REST API Communication:**
```javascript
// REST API Service - Tối ưu nhất cho HTTP communication
class ApiService {
  private baseURL: string; // Base URL - tối ưu cho API endpoint management
  private token: string | null = null; // Auth token - tối ưu cho authentication

  constructor(baseURL: string) { // Constructor - tối ưu cho service initialization
    this.baseURL = baseURL; // Set base URL - tối ưu cho API configuration
  }

  setToken(token: string) {
    this.token = token;
  }

  private async request<T>(
    endpoint: string,
    options: RequestInit = {}
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...(this.token && { Authorization: `Bearer ${this.token}` }),
      ...options.headers
    };

    const response = await fetch(url, {
      ...options,
      headers
    });

    if (!response.ok) {
      throw new Error(`API Error: ${response.status} ${response.statusText}`);
    }

    return response.json();
  }

  // GET request
  async get<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'GET' });
  }

  // POST request
  async post<T>(endpoint: string, data: any): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  // PUT request
  async put<T>(endpoint: string, data: any): Promise<T> {
    return this.request<T>(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }

  // DELETE request
  async delete<T>(endpoint: string): Promise<T> {
    return this.request<T>(endpoint, { method: 'DELETE' });
  }
}

// Usage
const apiService = new ApiService('https://api.example.com');
const users = await apiService.get<User[]>('/users');
const newUser = await apiService.post<User>('/users', { name: 'John', email: 'john@example.com' });
```

**2. WebSocket Communication:**
```javascript
// WebSocket Service
class WebSocketService { // WebSocket Service - Tối ưu nhất cho real-time communication
  private ws: WebSocket | null = null; // WebSocket instance - tối ưu cho connection management
  private reconnectAttempts = 0; // Reconnect attempts - tối ưu cho connection resilience
  private maxReconnectAttempts = 5; // Max reconnect attempts - tối ưu cho connection limits
  private reconnectInterval = 1000; // Reconnect interval - tối ưu cho retry timing
  private listeners: Map<string, Function[]> = new Map(); // Event listeners - tối ưu cho event management

  constructor(private url: string) {} // Constructor - tối ưu cho service initialization

  connect(): Promise<void> {
    return new Promise((resolve, reject) => {
      this.ws = new WebSocket(this.url);

      this.ws.onopen = () => {
        console.log('WebSocket connected');
        this.reconnectAttempts = 0;
        resolve();
      };

      this.ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          this.handleMessage(data);
        } catch (error) {
          console.error('Failed to parse WebSocket message:', error);
        }
      };

      this.ws.onclose = () => {
        console.log('WebSocket disconnected');
        this.handleReconnect();
      };

      this.ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        reject(error);
      };
    });
  }

  private handleMessage(data: any) {
    const { type, payload } = data;
    const listeners = this.listeners.get(type) || [];
    listeners.forEach(listener => listener(payload));
  }

  private handleReconnect() {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      setTimeout(() => {
        console.log(`Reconnecting... attempt ${this.reconnectAttempts}`);
        this.connect();
      }, this.reconnectInterval * this.reconnectAttempts);
    }
  }

  send(type: string, payload: any) {
    if (this.ws && this.ws.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({ type, payload }));
    }
  }

  subscribe(type: string, listener: Function) {
    if (!this.listeners.has(type)) {
      this.listeners.set(type, []);
    }
    this.listeners.get(type)!.push(listener);

    // Return unsubscribe function
    return () => {
      const listeners = this.listeners.get(type) || [];
      const index = listeners.indexOf(listener);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    };
  }

  disconnect() {
    if (this.ws) {
      this.ws.close();
      this.ws = null;
    }
  }
}

// Usage
const wsService = new WebSocketService('ws://localhost:8080');

// Connect
await wsService.connect();

// Subscribe to messages
const unsubscribe = wsService.subscribe('user-updated', (user) => {
  console.log('User updated:', user);
});

// Send message
wsService.send('join-room', { roomId: 'room-123' });

// Cleanup
unsubscribe();
wsService.disconnect();
```

**3. GraphQL Communication:**
```javascript
// GraphQL Client
class GraphQLClient {
  private endpoint: string;
  private token: string | null = null;

  constructor(endpoint: string) {
    this.endpoint = endpoint;
  }

  setToken(token: string) {
    this.token = token;
  }

  async query<T>(query: string, variables?: any): Promise<T> {
    const response = await fetch(this.endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        ...(this.token && { Authorization: `Bearer ${this.token}` })
      },
      body: JSON.stringify({
        query,
        variables
      })
    });

    const result = await response.json();

    if (result.errors) {
      throw new Error(`GraphQL Error: ${result.errors[0].message}`);
    }

    return result.data;
  }

  async mutation<T>(mutation: string, variables?: any): Promise<T> {
    return this.query<T>(mutation, variables);
  }
}

// GraphQL Queries
const GET_USERS = `
  query GetUsers($limit: Int, $offset: Int) {
    users(limit: $limit, offset: $offset) {
      id
      name
      email
      createdAt
    }
  }
`;

const CREATE_USER = `
  mutation CreateUser($input: UserInput!) {
    createUser(input: $input) {
      id
      name
      email
    }
  }
`;

// Usage
const client = new GraphQLClient('https://api.example.com/graphql');

const users = await client.query(GET_USERS, { limit: 10, offset: 0 });
const newUser = await client.mutation(CREATE_USER, {
  input: { name: 'John', email: 'john@example.com' }
});
```

**4. Server-Sent Events (SSE):**
```javascript
// Server-Sent Events Service
class SSEService {
  private eventSource: EventSource | null = null;
  private listeners: Map<string, Function[]> = new Map();

  connect(url: string) {
    this.eventSource = new EventSource(url);

    this.eventSource.onopen = () => {
      console.log('SSE connection opened');
    };

    this.eventSource.onmessage = (event) => {
      try {
        const data = JSON.parse(event.data);
        this.handleMessage(data);
      } catch (error) {
        console.error('Failed to parse SSE message:', error);
      }
    };

    this.eventSource.onerror = (error) => {
      console.error('SSE error:', error);
    };
  }

  private handleMessage(data: any) {
    const { type, payload } = data;
    const listeners = this.listeners.get(type) || [];
    listeners.forEach(listener => listener(payload));
  }

  subscribe(type: string, listener: Function) {
    if (!this.listeners.has(type)) {
      this.listeners.set(type, []);
    }
    this.listeners.get(type)!.push(listener);

    return () => {
      const listeners = this.listeners.get(type) || [];
      const index = listeners.indexOf(listener);
      if (index > -1) {
        listeners.splice(index, 1);
      }
    };
  }

  disconnect() {
    if (this.eventSource) {
      this.eventSource.close();
      this.eventSource = null;
    }
  }
}

// Usage
const sseService = new SSEService();
sseService.connect('/api/events');

sseService.subscribe('notification', (notification) => {
  console.log('New notification:', notification);
});
```

**5. Communication Patterns:**
```javascript
// Request/Response Pattern
class RequestResponseService {
  private pendingRequests = new Map<string, {
    resolve: Function;
    reject: Function;
    timeout: NodeJS.Timeout;
  }>();

  async request<T>(type: string, payload: any, timeout = 5000): Promise<T> {
    const requestId = this.generateRequestId();

    return new Promise((resolve, reject) => {
      const timeoutId = setTimeout(() => {
        this.pendingRequests.delete(requestId);
        reject(new Error('Request timeout'));
      }, timeout);

      this.pendingRequests.set(requestId, {
        resolve,
        reject,
        timeout: timeoutId
      });

      this.send(type, { requestId, payload });
    });
  }

  private generateRequestId(): string {
    return Math.random().toString(36).substr(2, 9);
  }

  private send(type: string, data: any) {
    // Implementation depends on transport (WebSocket, HTTP, etc.)
  }

  handleResponse(requestId: string, data: any) {
    const request = this.pendingRequests.get(requestId);
    if (request) {
      clearTimeout(request.timeout);
      this.pendingRequests.delete(requestId);
      request.resolve(data);
    }
  }
}

// Pub/Sub Pattern
class PubSubService {
  private subscribers = new Map<string, Set<Function>>();

  subscribe(topic: string, callback: Function) {
    if (!this.subscribers.has(topic)) {
      this.subscribers.set(topic, new Set());
    }
    this.subscribers.get(topic)!.add(callback);

    return () => {
      this.subscribers.get(topic)?.delete(callback);
    };
  }

  publish(topic: string, data: any) {
    const subscribers = this.subscribers.get(topic);
    if (subscribers) {
      subscribers.forEach(callback => callback(data));
    }
  }
}
```


## **Q20: WebSocket & Streaming**

### **🔍 Câu Hỏi:**
WebSocket, Streaming: Websocket, socket IO, Centrifuge?

### **💡 Trả Lời Chi Tiết:**

**1. Socket.IO Implementation:**
```javascript
// Socket.IO Client
import io from 'socket.io-client';

class SocketService {
  private socket: any = null;

  connect(url: string) {
    this.socket = io(url, {
      transports: ['websocket', 'polling'],
      autoConnect: true
    });

    this.socket.on('connect', () => {
      console.log('Connected to server');
    });

    this.socket.on('disconnect', () => {
      console.log('Disconnected from server');
    });
  }

  emit(event: string, data: any) {
    this.socket?.emit(event, data);
  }

  on(event: string, callback: Function) {
    this.socket?.on(event, callback);
  }

  disconnect() {
    this.socket?.disconnect();
  }
}
```

**2. Real-time Data Streaming:**
```javascript
// Real-time data streaming with WebSocket
class DataStreamer {
  private ws: WebSocket | null = null;
  private subscribers: Map<string, Function[]> = new Map();

  connect(url: string) {
    this.ws = new WebSocket(url);

    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.notifySubscribers(data.type, data.payload);
    };
  }

  subscribe(type: string, callback: Function) {
    if (!this.subscribers.has(type)) {
      this.subscribers.set(type, []);
    }
    this.subscribers.get(type)!.push(callback);
  }

  private notifySubscribers(type: string, data: any) {
    const callbacks = this.subscribers.get(type) || [];
    callbacks.forEach(callback => callback(data));
  }
}
```

---

### **Q20: WebSocket & Streaming** 🔥

#### **🔍 Câu Hỏi:**
WebSocket, Streaming: Websocket, socket IO, Centrifuge?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 WebSocket**: Real-time bidirectional communication protocol
  - *Là gì*: Protocol cho persistent connection giữa client và server
  - *Tại sao cần*: Real-time updates, instant messaging, live data
  - *Khi nào dùng*: Chat apps, live notifications, real-time dashboards

- **🎯 Socket.IO**: Library để simplify WebSocket communication
  - *Là gì*: JavaScript library cho real-time bidirectional communication
  - *Tại sao cần*: Fallback mechanisms, easier API, better browser support
  - *Khi nào dùng*: Khi cần WebSocket với fallback support

- **⚡ Centrifuge**: Real-time messaging server và client library
  - *Là gì*: Real-time messaging server với client libraries
  - *Tại sao cần*: Scalable real-time messaging, pub/sub patterns
  - *Khi nào dùng*: Large-scale real-time apps, pub/sub systems

- **✅ Streaming Technologies**: Các công nghệ streaming
  - *Server-Sent Events*: One-way streaming từ server đến client
  - *WebRTC*: Peer-to-peer communication cho video/audio
  - *HTTP/2 Push*: Server push resources trước khi client request
  - *Khi nào dùng*: Live video, audio streaming, real-time data

- **⚠️ Performance Considerations**: Các vấn đề về performance
  - *Connection Management*: Quản lý connections hiệu quả
  - *Message Batching*: Batch messages để reduce overhead
  - *Reconnection Logic*: Handle disconnections gracefully
  - *Memory Management*: Quản lý memory cho long-lived connections

**Trả lời:**
- **🔥 WebSocket**: Giao thức truyền thông hai chiều real-time
  - *Là gì*: Giao thức truyền thông hai chiều qua TCP, duy trì kết nối liên tục
  - *Tại sao cần*: Truyền dữ liệu real-time, ít overhead hơn HTTP
  - *Khi nào dùng*: Chat, live updates, real-time notifications

- **🎯 Socket.IO**: Library JavaScript cho WebSocket với fallback
  - *Là gì*: Wrapper cho WebSocket với auto-reconnection và fallback
  - *Tại sao cần*: Xử lý tương thích browser, auto-reconnection
  - *Khi nào dùng*: Dự án cần tương thích cao, real-time features

**Code Example:**
```javascript
// WebSocket implementation - Triển khai WebSocket
class WebSocketService {
  private ws: WebSocket | null = null;

  connect(url: string) {
    this.ws = new WebSocket(url);

    this.ws.onopen = () => {
      console.log('Connected to server'); // Kết nối thành công
    };

    this.ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      this.handleMessage(data);
    };
  }

  send(data: any) {
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify(data));
    }
  }
}

// Socket.IO implementation - Triển khai Socket.IO
import io from 'socket.io-client';

const socket = io('http://localhost:3000');

socket.on('connect', () => {
  console.log('Connected to server'); // Kết nối thành công
});

socket.emit('message', { text: 'Hello server' }); // Gửi tin nhắn
socket.on('response', (data) => {
  console.log('Server response:', data); // Nhận phản hồi
});
```

#### **🎯 Best Practices - Thực Hành Tốt Nhất:**
- **✅ Sử dụng WebSocket cho real-time data** - Dùng WebSocket cho dữ liệu real-time
- **✅ Implement reconnection logic** - Triển khai logic kết nối lại
- **✅ Handle connection errors gracefully** - Xử lý lỗi kết nối một cách graceful
- **✅ Use Socket.IO cho browser compatibility** - Dùng Socket.IO cho tương thích browser

#### **❌ Common Mistakes - Lỗi Thường Gặp:**
- **❌ Không handle disconnection** - Không xử lý ngắt kết nối
- **❌ Gửi data quá lớn qua WebSocket** - Gửi dữ liệu quá lớn
- **❌ Không cleanup listeners** - Không dọn dẹp event listeners

---

### **Q21: Browser Navigation - URL Processing** 🔥

#### **🔍 Câu Hỏi:**
What happens when you type a URL in the browser's address bar?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 URL Parsing**: Browser parse URL để extract components
  - *Là gì*: Phân tích URL để lấy protocol, domain, path, query parameters
  - *Tại sao cần*: Hiểu được cấu trúc URL để xử lý request
  - *Khi nào xảy ra*: Mỗi khi user nhập URL hoặc click link

- **🎯 DNS Resolution**: Chuyển đổi domain name thành IP address
  - *Là gì*: Process tìm IP address của domain name
  - *Tại sao cần*: Browser cần IP address để connect đến server
  - *Khi nào xảy ra*: Khi domain name chưa được cache

- **⚡ HTTP Request**: Gửi HTTP request đến server
  - *Là gì*: Browser gửi HTTP request với method, headers, body
  - *Tại sao cần*: Lấy resources từ server
  - *Khi nào xảy ra*: Sau khi có IP address

- **✅ Response Processing**: Xử lý response từ server
  - *Là gì*: Parse HTTP response, render content, execute JavaScript
  - *Tại sao cần*: Hiển thị webpage cho user
  - *Khi nào xảy ra*: Khi nhận được response từ server

- **⚠️ Caching**: Lưu trữ resources để tăng performance
  - *Là gì*: Cache HTML, CSS, JS, images để load nhanh hơn
  - *Tại sao cần*: Giảm load time, tiết kiệm bandwidth
  - *Khi nào xảy ra*: Khi resources được cache và còn valid

**1. URL Processing Steps:**
```javascript
// URL parsing and processing - Tối ưu nhất cho URL handling
class URLProcessor {
  static parseURL(url: string) { // Parse URL method - tối ưu cho URL analysis
    const urlObj = new URL(url); // URL constructor - tối ưu cho URL parsing
    return { // Return parsed components - tối ưu cho URL structure
      protocol: urlObj.protocol, // Protocol - tối ưu cho scheme identification
      hostname: urlObj.hostname, // Hostname - tối ưu cho domain extraction
      port: urlObj.port, // Port - tối ưu cho port identification
      pathname: urlObj.pathname, // Pathname - tối ưu cho path extraction
      search: urlObj.search, // Search params - tối ưu cho query string
      hash: urlObj.hash // Hash - tối ưu cho fragment identification
    };
  }

  static validateURL(url: string): boolean {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  }
}

// Browser navigation flow
const navigationFlow = {
  1: 'DNS Resolution - Convert domain to IP',
  2: 'TCP Connection - Establish connection',
  3: 'TLS Handshake - Secure connection (HTTPS)',
  4: 'HTTP Request - Send request to server',
  5: 'Server Processing - Server processes request',
  6: 'HTTP Response - Server sends response',
  7: 'HTML Parsing - Browser parses HTML',
  8: 'Resource Loading - Load CSS, JS, images',
  9: 'Rendering - Render page to screen'
};
```

---

### **Q22: Error Tracking - Sentry, Grafana** 🔥

#### **🔍 Câu Hỏi:**
Had using any tool to tracing in web error? Sentry, Grafana, datadog?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Error Tracking**: Monitoring và tracking errors trong production
  - *Là gì*: Process của việc capture, log, và analyze errors trong production
  - *Tại sao cần*: Catch bugs sớm, improve user experience, debug issues
  - *Khi nào dùng*: Production apps, để monitor và fix issues

- **🎯 Sentry**: Popular error tracking và performance monitoring platform
  - *Là gì*: Platform cho error tracking, performance monitoring, release tracking
  - *Tại sao cần*: Real-time error alerts, detailed error context, performance insights
  - *Khi nào dùng*: Khi cần comprehensive error tracking và monitoring

- **⚡ Grafana**: Open-source analytics và monitoring platform
  - *Là gì*: Platform cho data visualization, monitoring, alerting
  - *Tại sao cần*: Create dashboards, monitor metrics, set up alerts
  - *Khi nào dùng*: Khi cần visualize data và monitor system metrics

- **✅ DataDog**: Cloud-based monitoring và analytics platform
  - *Là gì*: Platform cho infrastructure monitoring, APM, log management
  - *Tại sao cần*: Full-stack monitoring, infrastructure insights, log analysis
  - *Khi nào dùng*: Khi cần comprehensive monitoring cho entire stack

- **⚠️ Error Tracking Benefits**: Lợi ích của error tracking
  - *Proactive Monitoring*: Catch issues trước khi users report
  - *Faster Debugging*: Detailed error context giúp debug nhanh hơn
  - *User Experience*: Improve user experience bằng cách fix issues sớm
  - *Performance Insights*: Monitor performance và identify bottlenecks

**1. Sentry Integration:**
```javascript
// Sentry error tracking - Tối ưu nhất cho error monitoring
import * as Sentry from '@sentry/react'; // Sentry React SDK - tối ưu cho React error tracking

Sentry.init({ // Sentry initialization - tối ưu cho error tracking setup
  dsn: 'YOUR_SENTRY_DSN', // DSN - tối ưu cho Sentry project identification
  environment: process.env.NODE_ENV, // Environment - tối ưu cho environment-specific tracking
  tracesSampleRate: 1.0, // Trace sample rate - tối ưu cho performance monitoring
});

// Custom error boundary
class ErrorBoundary extends React.Component {
  componentDidCatch(error: Error, errorInfo: any) {
    Sentry.captureException(error, {
      contexts: {
        react: {
          componentStack: errorInfo.componentStack
        }
      }
    });
  }
}

// Manual error reporting
try {
  // Risky operation
} catch (error) {
  Sentry.captureException(error);
}
```

**2. Performance Monitoring:**
```javascript
// Performance monitoring
class PerformanceMonitor {
  static trackPageLoad() {
    window.addEventListener('load', () => {
      const navigation = performance.getEntriesByType('navigation')[0];
      Sentry.addBreadcrumb({
        message: 'Page loaded',
        data: {
          loadTime: navigation.loadEventEnd - navigation.loadEventStart,
          domContentLoaded: navigation.domContentLoadedEventEnd - navigation.domContentLoadedEventStart
        }
      });
    });
  }

  static trackUserAction(action: string, data?: any) {
    Sentry.addBreadcrumb({
      message: action,
      data
    });
  }
}
```

---

### **Q23: Micro Frontend & Monorepo** 🔥

#### **🔍 Câu Hỏi:**
Micro Frontend / Monorepo?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Micro Frontend**: Architectural approach cho building frontend apps
  - *Là gì*: Approach chia frontend thành smaller, independent applications
  - *Tại sao cần*: Team autonomy, technology diversity, independent deployments
  - *Khi nào dùng*: Large teams, complex applications, multiple teams

- **🎯 Monorepo**: Single repository chứa multiple projects
  - *Là gì*: Single Git repository chứa multiple related projects
  - *Tại sao cần*: Shared code, consistent tooling, easier refactoring
  - *Khi nào dùng*: Related projects, shared libraries, consistent tooling

- **⚡ Micro Frontend Benefits**: Lợi ích của micro frontend
  - *Team Autonomy*: Teams có thể work independently
  - *Technology Diversity*: Sử dụng different technologies
  - *Independent Deployments*: Deploy features independently
  - *Scalability*: Scale teams và applications independently

- **✅ Monorepo Benefits**: Lợi ích của monorepo
  - *Code Sharing*: Share code giữa projects
  - *Consistent Tooling*: Same tools và configurations
  - *Atomic Changes*: Make changes across multiple projects
  - *Easier Refactoring*: Refactor code across projects

- **⚠️ Challenges**: Các thách thức
  - *Complexity*: Increased complexity trong setup và maintenance
  - *Build Times*: Longer build times với large monorepos
  - *Dependency Management*: Managing dependencies across projects
  - *Team Coordination*: Need better coordination between teams

**1. Module Federation Setup:**
```javascript
// webpack.config.js for Shell App - Tối ưu nhất cho micro frontend
const ModuleFederationPlugin = require('@module-federation/webpack'); // Module Federation - tối ưu cho micro frontend

module.exports = { // Webpack config - tối ưu cho build configuration
  plugins: [ // Plugins array - tối ưu cho plugin management
    new ModuleFederationPlugin({ // Module Federation plugin - tối ưu cho micro frontend setup
      name: 'shell', // Shell app name - tối ưu cho app identification
      remotes: { // Remote apps - tối ưu cho micro frontend integration
        auth: 'auth@http://localhost:3001/remoteEntry.js', // Auth remote - tối ưu cho authentication module
        dashboard: 'dashboard@http://localhost:3002/remoteEntry.js'
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true }
      }
    })
  ]
};

// webpack.config.js for Remote App
module.exports = {
  plugins: [
    new ModuleFederationPlugin({
      name: 'auth',
      filename: 'remoteEntry.js',
      exposes: {
        './Login': './src/Login',
        './Register': './src/Register'
      },
      shared: {
        react: { singleton: true },
        'react-dom': { singleton: true }
      }
    })
  ]
};
```

**2. Nx Monorepo Structure:**
```bash
# Nx workspace structure
apps/
├── shell/                 # Main application
├── auth/                  # Authentication micro frontend
├── dashboard/             # Dashboard micro frontend
└── shared/                # Shared components

libs/
├── ui/                    # Shared UI components
├── utils/                 # Utility functions
└── types/                 # TypeScript types
```

---

### **Q24: File Upload/Download** 🔥

#### **🔍 Câu Hỏi:**
Upload / download behavior?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 File Upload**: Process gửi files từ client đến server
  - *Là gì*: Mechanism để transfer files từ user's device đến server
  - *Tại sao cần*: Users cần upload images, documents, data files
  - *Khi nào dùng*: Profile pictures, document uploads, data imports

- **🎯 File Download**: Process tải files từ server về client
  - *Là gì*: Mechanism để transfer files từ server đến user's device
  - *Tại sao cần*: Users cần tải reports, documents, media files
  - *Khi nào dùng*: Export data, download reports, media files

- **⚡ Upload Strategies**: Các chiến lược upload
  - *Direct Upload*: Upload trực tiếp đến server
  - *Chunked Upload*: Chia file thành chunks để upload
  - *Resumable Upload*: Có thể resume upload nếu bị gián đoạn
  - *Cloud Upload*: Upload đến cloud storage (S3, Cloudinary)

- **✅ Download Strategies**: Các chiến lược download
  - *Direct Download*: Download trực tiếp từ server
  - *Streaming Download*: Stream large files để tránh memory issues
  - *Progressive Download*: Download và hiển thị content progressively
  - *Cloud Download*: Download từ cloud storage với signed URLs

- **⚠️ Security Considerations**: Các vấn đề bảo mật
  - *File Validation*: Validate file types, sizes, content
  - *Virus Scanning*: Scan files để detect malware
  - *Access Control*: Control access đến uploaded files
  - *Storage Security*: Secure storage của files trên server

**1. File Upload with Progress:**
```javascript
// File upload with progress tracking - Tối ưu nhất cho file upload
class FileUploader {
  async uploadFile(file: File, onProgress?: (progress: number) => void) { // Upload method - tối ưu cho file transfer
    const formData = new FormData(); // FormData - tối ưu cho multipart form data
    formData.append('file', file); // Append file - tối ưu cho file attachment

    return new Promise((resolve, reject) => {
      const xhr = new XMLHttpRequest();

      xhr.upload.onprogress = (event) => {
        if (event.lengthComputable && onProgress) {
          const progress = (event.loaded / event.total) * 100;
          onProgress(progress);
        }
      };

      xhr.onload = () => {
        if (xhr.status === 200) {
          resolve(JSON.parse(xhr.responseText));
        } else {
          reject(new Error('Upload failed'));
        }
      };

      xhr.onerror = () => reject(new Error('Upload failed'));

      xhr.open('POST', '/api/upload');
      xhr.send(formData);
    });
  }
}
```

**2. File Download:**
```javascript
// File download utility
class FileDownloader {
  static downloadFile(url: string, filename: string) {
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }

  static downloadBlob(blob: Blob, filename: string) {
    const url = URL.createObjectURL(blob);
    this.downloadFile(url, filename);
    URL.revokeObjectURL(url);
  }
}
```

---

### **Q25: Request Cancellation - AbortController** 🔥

#### **🔍 Câu Hỏi:**
Cancel request api: AbortController?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 AbortController**: API để cancel ongoing requests
  - *Là gì*: Web API cho phép cancel fetch requests và other async operations
  - *Tại sao cần*: Cancel requests không cần thiết, improve performance
  - *Khi nào dùng*: Khi user navigate away, component unmount, timeout

- **🎯 Request Cancellation**: Process hủy ongoing requests
  - *Là gì*: Mechanism để stop ongoing HTTP requests
  - *Tại sao cần*: Tránh unnecessary network traffic, memory leaks
  - *Khi nào dùng*: User actions, component lifecycle, timeout scenarios

- **⚡ AbortSignal**: Signal object để communicate cancellation
  - *Là gì*: Object được sử dụng để signal cancellation
  - *Tại sao cần*: Communicate cancellation state đến async operations
  - *Khi nào dùng*: Khi cần cancel multiple operations cùng lúc

- **✅ Use Cases**: Các trường hợp sử dụng
  - *Component Unmount*: Cancel requests khi component unmount
  - *User Navigation*: Cancel requests khi user navigate away
  - *Timeout*: Cancel requests sau một khoảng thời gian
  - *New Request*: Cancel previous request khi có request mới

- **⚠️ Browser Support**: Hỗ trợ browser
  - *Modern Browsers*: Supported trong modern browsers
  - *Polyfill*: Cần polyfill cho older browsers
  - *Fallback*: Implement fallback cho unsupported browsers
  - *Testing*: Test cancellation behavior trong different browsers

**1. AbortController Implementation:**
```javascript
// Request cancellation with AbortController - Tối ưu nhất cho request management
class CancellableRequest {
  private controller: AbortController | null = null; // AbortController - tối ưu cho request cancellation

  async makeRequest(url: string, options: RequestInit = {}) { // Make request method - tối ưu cho HTTP requests
    // Cancel previous request - Cancel previous request - tối ưu cho request cleanup
    if (this.controller) { // Check controller - tối ưu cho controller validation
      this.controller.abort(); // Abort previous - tối ưu cho request cancellation
    }

    this.controller = new AbortController();

    try {
      const response = await fetch(url, {
        ...options,
        signal: this.controller.signal
      });

      return response.json();
    } catch (error) {
      if (error.name === 'AbortError') {
        console.log('Request was cancelled');
      } else {
        throw error;
      }
    }
  }

  cancel() {
    if (this.controller) {
      this.controller.abort();
      this.controller = null;
    }
  }
}
```

---

### **Q26: Client vs Server Side Rendering** 🔥

#### **🔍 Câu Hỏi:**
Client Side Rendering, Server side rendering, sự khác nhau?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Client-Side Rendering (CSR)**: Render content trong browser
  - *Là gì*: Process render HTML, CSS, JS trong browser
  - *Tại sao cần*: Interactive apps, dynamic content, better UX
  - *Khi nào dùng*: Single Page Applications, interactive dashboards

- **🎯 Server-Side Rendering (SSR)**: Render content trên server
  - *Là gì*: Process render HTML trên server trước khi gửi đến browser
  - *Tại sao cần*: Better SEO, faster initial load, better performance
  - *Khi nào dùng*: Content-heavy sites, SEO-critical apps

- **⚡ Static Site Generation (SSG)**: Pre-render content tại build time
  - *Là gì*: Generate static HTML files tại build time
  - *Tại sao cần*: Fastest loading, CDN-friendly, secure
  - *Khi nào dùng*: Blogs, documentation sites, marketing pages

- **✅ Hybrid Rendering**: Kết hợp multiple rendering strategies
  - *Là gì*: Sử dụng different rendering methods cho different pages
  - *Tại sao cần*: Optimize performance cho different use cases
  - *Khi nào dùng*: Complex apps với mixed requirements

- **⚠️ Trade-offs**: Các trade-offs giữa các approaches
  - *Performance*: CSR có slower initial load, SSR có faster initial load
  - *SEO*: CSR có poor SEO, SSR có better SEO
  - *Interactivity*: CSR có better interactivity, SSR có limited interactivity
  - *Complexity*: CSR đơn giản hơn, SSR phức tạp hơn

**1. CSR vs SSR Comparison:**
```javascript
// Client Side Rendering (CSR) - Tối ưu nhất cho interactive apps
const CSRApp = () => { // CSR component - tối ưu cho client-side rendering
  const [data, setData] = useState(null); // State management - tối ưu cho dynamic content

  useEffect(() => { // useEffect hook - tối ưu cho side effects
    // Data fetched on client - Data fetched on client - tối ưu cho client-side data fetching
    fetchData().then(setData); // Fetch data - tối ưu cho async data loading
  }, []); // Empty dependency array - tối ưu cho component mount effect

  if (!data) return <div>Loading...</div>;

  return <div>{data.content}</div>;
};

// Server Side Rendering (SSR) with Next.js
export async function getServerSideProps() {
  const data = await fetchData(); // Fetched on server

  return {
    props: { data }
  };
}

const SSRPage = ({ data }) => {
  return <div>{data.content}</div>;
};
```

**2. Hydration Process:**
```javascript
// Hydration in SSR
const hydrateApp = () => {
  const root = document.getElementById('root');
  const app = <App />;

  // Hydrate existing HTML
  ReactDOM.hydrate(app, root);
};
```

---

### **Q27: Web Workers - Background Processing** 🔥

#### **🔍 Câu Hỏi:**
Web workers?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Web Workers**: JavaScript threads chạy trong background
  - *Là gì*: JavaScript threads chạy parallel với main thread
  - *Tại sao cần*: Perform heavy computations without blocking UI
  - *Khi nào dùng*: Heavy calculations, data processing, image manipulation

- **🎯 Main Thread vs Worker Thread**: Sự khác biệt giữa main và worker thread
  - *Main Thread*: UI thread, handle user interactions, render DOM
  - *Worker Thread*: Background thread, perform heavy computations
  - *Communication*: Workers communicate với main thread qua messages
  - *Isolation*: Workers không có access đến DOM hoặc window object

- **⚡ Use Cases**: Các trường hợp sử dụng
  - *Data Processing*: Process large datasets, CSV parsing
  - *Image Manipulation*: Resize, filter, process images
  - *Cryptography*: Encrypt/decrypt data, hash calculations
  - *Machine Learning*: Run ML models, data analysis

- **✅ Benefits**: Lợi ích của Web Workers
  - *Non-blocking*: Không block main thread, UI vẫn responsive
  - *Performance*: Utilize multiple CPU cores
  - *Parallel Processing*: Run multiple tasks simultaneously
  - *Better UX*: Smooth user experience với heavy operations

- **⚠️ Limitations**: Các hạn chế của Web Workers
  - *No DOM Access*: Không thể access DOM hoặc window object
  - *Limited APIs*: Chỉ có access đến limited set of APIs
  - *Message Passing*: Communication chỉ qua message passing
  - *Browser Support*: Cần check browser support

**1. Web Worker Implementation:**
```javascript
// main.js - Tối ưu nhất cho Web Worker communication
const worker = new Worker('worker.js'); // Create worker - tối ưu cho background processing

worker.postMessage({ type: 'CALCULATE', data: [1, 2, 3, 4, 5] }); // Send message - tối ưu cho data transfer

worker.onmessage = (event) => { // Message handler - tối ưu cho result processing
  console.log('Result:', event.data); // Log result - tối ưu cho debugging
};

// worker.js
self.onmessage = (event) => {
  const { type, data } = event.data;

  if (type === 'CALCULATE') {
    const result = data.reduce((sum, num) => sum + num, 0);
    self.postMessage(result);
  }
};
```

---

### **Q28: Next.js Advanced Features** 🔥

#### **🔍 Câu Hỏi:**
NextJS và các điểm nổi bật, kèm ví dụ chi tiết?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Next.js Framework**: React framework với full-stack capabilities
  - *Là gì*: Production-ready React framework với built-in features
  - *Tại sao cần*: Simplify React development, better performance, SEO
  - *Khi nào dùng*: Production React apps, SEO-critical sites, full-stack apps

- **🎯 App Router**: New routing system trong Next.js 13+
  - *Là gì*: File-based routing system với improved performance
  - *Tại sao cần*: Better performance, nested layouts, server components
  - *Khi nào dùng*: New Next.js projects, khi cần advanced routing

- **⚡ Server Components**: Components render trên server
  - *Là gì*: React components render trên server, không ship JavaScript
  - *Tại sao cần*: Better performance, smaller bundle size, SEO
  - *Khi nào dùng*: Static content, data fetching, SEO-critical pages

- **✅ Static Site Generation (SSG)**: Pre-render pages tại build time
  - *Là gì*: Generate static HTML files tại build time
  - *Tại sao cần*: Fastest loading, CDN-friendly, secure
  - *Khi nào dùng*: Blogs, documentation, marketing pages

- **⚠️ Advanced Features**: Các tính năng nâng cao
  - *Image Optimization*: Automatic image optimization và lazy loading
  - *Font Optimization*: Automatic font optimization
  - *API Routes*: Built-in API routes cho backend functionality
  - *Middleware*: Request/response middleware cho authentication

**1. App Router (Next.js 13+):**
```javascript
// app/layout.js - Tối ưu nhất cho Next.js App Router
export default function RootLayout({ children }) { // Root layout - tối ưu cho app structure
  return ( // Return JSX - tối ưu cho layout rendering
    <html> // HTML element - tối ưu cho document structure
      <body> // Body element - tối ưu cho content container
        <nav>Navigation</nav> // Navigation - tối ưu cho app navigation
        {children} // Children - tối ưu cho page content
      </body> // Close body - tối ưu cho HTML structure
    </html> // Close html - tối ưu cho document structure
  );
}

// app/page.js
export default function HomePage() {
  return <h1>Home Page</h1>;
}

// app/dashboard/page.js
export default function DashboardPage() {
  return <h1>Dashboard</h1>;
}
```

**2. Server Components:**
```javascript
// Server Component (can fetch data directly)
async function UserProfile({ userId }) {
  const user = await fetch(`/api/users/${userId}`);
  const userData = await user.json();

  return (
    <div>
      <h1>{userData.name}</h1>
      <p>{userData.email}</p>
    </div>
  );
}
```

---

### **Q29: HTTP Status Codes** 🔥

#### **🔍 Câu Hỏi:**
Status code for http request?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 HTTP Status Codes**: Numeric codes indicate result của HTTP request
  - *Là gì*: 3-digit codes indicate success, failure, hoặc other status
  - *Tại sao cần*: Communicate result của request, handle errors properly
  - *Khi nào dùng*: Mọi HTTP request, error handling, API responses

- **🎯 1xx Informational**: Request received, continuing process
  - *100 Continue*: Server received request headers, client should continue
  - *101 Switching Protocols*: Server switching protocols as requested
  - *102 Processing*: Server received request, processing (WebDAV)
  - *Khi nào dùng*: Long-running requests, protocol switching

- **⚡ 2xx Success**: Request successfully received, understood, accepted
  - *200 OK*: Request successful, response body contains result
  - *201 Created*: Request successful, new resource created
  - *204 No Content*: Request successful, no content to return
  - *Khi nào dùng*: Successful operations, resource creation

- **✅ 3xx Redirection**: Further action needed to complete request
  - *301 Moved Permanently*: Resource permanently moved to new URL
  - *302 Found*: Resource temporarily moved to new URL
  - *304 Not Modified*: Resource not modified, use cached version
  - *Khi nào dùng*: URL changes, caching, redirects

- **⚠️ 4xx Client Error**: Request contains bad syntax or cannot be fulfilled
  - *400 Bad Request*: Request syntax invalid or cannot be understood
  - *401 Unauthorized*: Authentication required or failed
  - *404 Not Found*: Resource not found
  - *Khi nào dùng*: Client errors, authentication issues, missing resources

**1. HTTP Status Code Categories:**
```javascript
// HTTP Status Code Handler - Tối ưu nhất cho status code management
class StatusCodeHandler {
  static getStatusMessage(code: number): string { // Get status message - tối ưu cho status interpretation
    const statusCodes = { // Status codes object - tối ưu cho status mapping
      200: 'OK',
      201: 'Created',
      400: 'Bad Request',
      401: 'Unauthorized',
      403: 'Forbidden',
      404: 'Not Found',
      500: 'Internal Server Error'
    };

    return statusCodes[code] || 'Unknown Status';
  }

  static isSuccess(code: number): boolean {
    return code >= 200 && code < 300;
  }

  static isClientError(code: number): boolean {
    return code >= 400 && code < 500;
  }

  static isServerError(code: number): boolean {
    return code >= 500 && code < 600;
  }
}
```

---

### **Q30: Advanced State Management** 🔥

#### **🔍 Câu Hỏi:**
Store management: Redux, Zustand?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 State Management**: Quản lý state trong complex applications
  - *Là gì*: Pattern để manage application state in predictable way
  - *Tại sao cần*: Predictable state updates, easier debugging, better performance
  - *Khi nào dùng*: Complex apps, shared state, need predictable updates

- **🎯 Redux**: Predictable state container cho JavaScript apps
  - *Là gì*: State management library với single source of truth
  - *Tại sao cần*: Predictable state updates, time-travel debugging, middleware
  - *Khi nào dùng*: Large apps, complex state logic, need debugging tools

- **⚡ Zustand**: Lightweight state management library
  - *Là gì*: Small, fast, scalable state management solution
  - *Tại sao cần*: Simple API, TypeScript support, no boilerplate
  - *Khi nào dùng*: Medium apps, simple state logic, need TypeScript

- **✅ Context API**: Built-in React state management
  - *Là gì*: React's built-in solution cho sharing state
  - *Tại sao cần*: No external dependencies, simple API, built-in
  - *Khi nào dùng*: Small to medium apps, simple state sharing

- **⚠️ Other Solutions**: Các giải pháp khác
  - *Jotai*: Atomic state management với minimal re-renders
  - *Recoil*: Experimental state management từ Facebook
  - *Valtio*: Proxy-based state management
  - *Khi nào dùng*: Specific use cases, experimental features

**1. Zustand Store:**
```javascript
// Zustand store - Tối ưu nhất cho lightweight state management
import { create } from 'zustand'; // Zustand create - tối ưu cho store creation

const useStore = create((set) => ({ // Create store - tối ưu cho state management
  count: 0, // Initial state - tối ưu cho state initialization
  increment: () => set((state) => ({ count: state.count + 1 })), // Increment action - tối ưu cho state updates
  decrement: () => set((state) => ({ count: state.count - 1 })), // Decrement action - tối ưu cho state updates
  reset: () => set({ count: 0 }) // Reset action - tối ưu cho state reset
}));

// Usage in component
function Counter() {
  const { count, increment, decrement } = useStore();

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>+</button>
      <button onClick={decrement}>-</button>
    </div>
  );
}
```

**2. Redux Toolkit:**
```javascript
// Redux store with RTK
import { createSlice, configureStore } from '@reduxjs/toolkit';

const counterSlice = createSlice({
  name: 'counter',
  initialState: { value: 0 },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    }
  }
});

export const { increment, decrement } = counterSlice.actions;

const store = configureStore({
  reducer: {
    counter: counterSlice.reducer
  }
});
```

---

### **Q31: Nx Monorepo** 🔥

#### **🔍 Câu Hỏi:**
NX?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Nx Monorepo**: Development toolkit cho monorepos
  - *Là gì*: Smart, fast, extensible build system cho monorepos
  - *Tại sao cần*: Scale development, share code, consistent tooling
  - *Khi nào dùng*: Large teams, multiple projects, shared libraries

- **🎯 Monorepo Benefits**: Lợi ích của monorepo
  - *Code Sharing*: Share code giữa projects, avoid duplication
  - *Consistent Tooling*: Same tools và configurations across projects
  - *Atomic Changes*: Make changes across multiple projects in single commit
  - *Easier Refactoring*: Refactor code across projects easily

- **⚡ Nx Features**: Các tính năng của Nx
  - *Smart Builds*: Only build what changed, incremental builds
  - *Dependency Graph*: Visualize dependencies between projects
  - *Code Generation*: Generate boilerplate code với generators
  - *Testing*: Run tests efficiently across projects

- **✅ Nx Commands**: Các lệnh Nx phổ biến
  - *nx build*: Build specific project hoặc all projects
  - *nx test*: Run tests cho specific project hoặc all projects
  - *nx serve*: Serve specific project trong development
  - *nx generate*: Generate new projects, components, libraries

- **⚠️ Nx Challenges**: Các thách thức của Nx
  - *Learning Curve*: Cần thời gian để học và master
  - *Build Times*: Build times có thể tăng với large monorepos
  - *Dependency Management*: Managing dependencies across projects
  - *Team Coordination*: Need better coordination between teams

**1. Nx Workspace Commands:**
```bash
# Create new app - Tối ưu nhất cho app generation
nx g @nx/react:app my-app # Generate React app - tối ưu cho app creation

# Create new library - Tối ưu nhất cho library generation
nx g @nx/react:lib my-lib

# Run tests
nx test my-app

# Build app
nx build my-app

# Run affected tests
nx affected:test

# Generate dependency graph
nx graph
```

---

### **Q32: React vs Next.js vs React Native Lifecycle** 🔥

#### **🔍 Câu Hỏi:**
Lifecycle của React, NextJS, React Native?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 React Lifecycle**: Component lifecycle trong React
  - *Là gì*: Series of methods được gọi trong component's lifetime
  - *Tại sao cần*: Control component behavior, manage side effects
  - *Khi nào dùng*: Class components, functional components với hooks

- **🎯 Next.js Lifecycle**: Additional lifecycle hooks trong Next.js
  - *Là gì*: Next.js specific lifecycle methods cho pages và apps
  - *Tại sao cần*: Server-side rendering, data fetching, routing
  - *Khi nào dùng*: Next.js pages, API routes, middleware

- **⚡ React Native Lifecycle**: Component lifecycle trong React Native
  - *Là gì*: Lifecycle methods specific cho mobile development
  - *Tại sao cần*: Handle mobile-specific events, navigation, memory
  - *Khi nào dùng*: React Native apps, mobile development

- **✅ Common Lifecycle Methods**: Các lifecycle methods phổ biến
  - *componentDidMount*: Called after component mounts
  - *componentDidUpdate*: Called after component updates
  - *componentWillUnmount*: Called before component unmounts
  - *useEffect*: Hook equivalent cho functional components

- **⚠️ Platform Differences**: Sự khác biệt giữa platforms
  - *React*: Web-specific lifecycle, DOM manipulation
  - *Next.js*: Server-side lifecycle, routing, data fetching
  - *React Native*: Mobile-specific lifecycle, navigation, memory management
  - *Khi nào cần*: Khi develop cho different platforms

**1. React Lifecycle:**
```javascript
// Class component lifecycle - Tối ưu nhất cho React lifecycle management
class MyComponent extends React.Component { // Class component - tối ưu cho lifecycle methods
  componentDidMount() { // Component mounted - tối ưu cho initialization
    // Component mounted - Component mounted - tối ưu cho side effects
  }

  componentDidUpdate(prevProps, prevState) {
    // Component updated
  }

  componentWillUnmount() {
    // Component will unmount
  }
}

// Functional component with hooks
function MyComponent() {
  useEffect(() => {
    // Component mounted
    return () => {
      // Cleanup (unmount)
    };
  }, []);
}
```

---

### **Q33: Storybook - Component Documentation** 🔥

#### **🔍 Câu Hỏi:**
Storybook - define cấu trúc storybook như thế nào để scale?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Storybook**: Tool cho building UI components và pages in isolation
  - *Là gì*: Development environment cho UI components với documentation
  - *Tại sao cần*: Develop components in isolation, document components
  - *Khi nào dùng*: Component libraries, design systems, team collaboration

- **🎯 Storybook Structure**: Cấu trúc Storybook để scale
  - *Là gì*: Organization pattern cho stories, components, documentation
  - *Tại sao cần*: Maintainable, scalable, easy to navigate
  - *Khi nào dùng*: Large component libraries, multiple teams

- **⚡ Story Organization**: Tổ chức stories hiệu quả
  - *Là gì*: Cách organize stories theo components, features, pages
  - *Tại sao cần*: Easy navigation, logical grouping, maintainable
  - *Khi nào dùng*: Khi có nhiều components và stories

- **✅ Documentation Strategy**: Chiến lược documentation
  - *Là gì*: Approach để document components, usage, examples
  - *Tại sao cần*: Help developers understand và use components
  - *Khi nào dùng*: Team collaboration, component libraries

- **⚠️ Scaling Challenges**: Các thách thức khi scale
  - *Performance*: Storybook performance với large number of stories
  - *Organization*: Keeping stories organized và maintainable
  - *Documentation*: Maintaining up-to-date documentation
  - *Team Coordination*: Coordinating between multiple teams

**1. Storybook Configuration:**
```javascript
// .storybook/main.js - Tối ưu nhất cho Storybook configuration
module.exports = { // Storybook config - tối ưu cho story management
  stories: ['../src/**/*.stories.@(js|jsx|ts|tsx)'], // Stories pattern - tối ưu cho story discovery
  addons: [ // Addons array - tối ưu cho functionality extension
    '@storybook/addon-essentials', // Essentials addon - tối ưu cho core features
    '@storybook/addon-docs' // Docs addon - tối ưu cho documentation
  ]
};

// Button.stories.tsx
export default {
  title: 'Components/Button',
  component: Button,
  parameters: {
    docs: {
      description: {
        component: 'A reusable button component'
      }
    }
  }
};

export const Primary = {
  args: {
    variant: 'primary',
    children: 'Button'
  }
};
```

---

### **Q34: Security Best Practices** 🔥

#### **🔍 Câu Hỏi:**
Best Practices cho Security?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Frontend Security**: Bảo mật trong frontend applications
  - *Là gì*: Practices và techniques để protect frontend applications
  - *Tại sao cần*: Protect users, data, và prevent attacks
  - *Khi nào dùng*: Mọi production applications, đặc biệt với user data

- **🎯 Input Validation**: Validate và sanitize user input
  - *Là gì*: Check và clean user input trước khi process
  - *Tại sao cần*: Prevent XSS attacks, injection attacks
  - *Khi nào dùng*: Mọi user input, forms, API calls

- **⚡ Authentication & Authorization**: Xác thực và phân quyền
  - *Là gì*: Verify user identity và control access to resources
  - *Tại sao cần*: Protect sensitive data, control access
  - *Khi nào dùng*: Apps với user accounts, sensitive data

- **✅ Data Protection**: Bảo vệ dữ liệu nhạy cảm
  - *Là gì*: Protect sensitive data trong storage và transmission
  - *Tại sao cần*: Prevent data breaches, protect user privacy
  - *Khi nào dùng*: Apps với user data, payment info, personal info

- **⚠️ Common Vulnerabilities**: Các lỗ hổng bảo mật thường gặp
  - *XSS*: Cross-Site Scripting attacks
  - *CSRF*: Cross-Site Request Forgery attacks
  - *Clickjacking*: UI redressing attacks
  - *Khi nào xảy ra*: Khi không có proper security measures

**1. Security Checklist:**
```javascript
// Security best practices - Tối ưu nhất cho security implementation
const securityChecklist = [ // Security checklist - tối ưu cho security validation
  'Use HTTPS everywhere', // HTTPS - tối ưu cho secure communication
  'Implement CSP headers', // CSP headers - tối ưu cho XSS prevention
  'Validate all inputs', // Input validation - tối ưu cho data integrity
  'Sanitize user data', // Data sanitization - tối ưu cho XSS prevention
  'Use secure cookies', // Secure cookies - tối ưu cho session security
  'Implement rate limiting', // Rate limiting - tối ưu cho DoS prevention
  'Keep dependencies updated', // Dependency updates - tối ưu cho vulnerability patching
  'Use environment variables for secrets'
];
```

---

### **Q35: React Query Advanced** 🔥

#### **🔍 Câu Hỏi:**
React Query And?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 React Query**: Data fetching và caching library cho React
  - *Là gì*: Powerful data synchronization library cho React applications
  - *Tại sao cần*: Simplify data fetching, caching, synchronization
  - *Khi nào dùng*: Apps với complex data requirements, API calls

- **🎯 Key Features**: Các tính năng chính của React Query
  - *Là gì*: Core features như caching, background updates, error handling
  - *Tại sao cần*: Improve performance, user experience, developer experience
  - *Khi nào dùng*: Khi cần manage server state effectively

- **⚡ Advanced Patterns**: Các patterns nâng cao
  - *Là gì*: Advanced usage patterns như infinite queries, mutations
  - *Tại sao cần*: Handle complex data scenarios, optimize performance
  - *Khi nào dùng*: Large applications, complex data requirements

- **✅ Performance Optimization**: Tối ưu performance
  - *Là gì*: Techniques để optimize React Query performance
  - *Tại sao cần*: Better user experience, reduced server load
  - *Khi nào dùng*: Production apps, high-traffic applications

- **⚠️ Common Pitfalls**: Các lỗi thường gặp
  - *Là gì*: Common mistakes và how to avoid them
  - *Tại sao cần*: Prevent bugs, improve code quality
  - *Khi nào xảy ra*: Khi không hiểu rõ React Query concepts

**1. React Query Setup:**
```javascript
// React Query configuration - Tối ưu nhất cho data fetching
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'; // React Query imports - tối ưu cho data management

const queryClient = new QueryClient({ // Query client - tối ưu cho query management
  defaultOptions: { // Default options - tối ưu cho global configuration
    queries: { // Queries config - tối ưu cho query behavior
      staleTime: 5 * 60 * 1000, // 5 minutes - tối ưu cho cache freshness
      cacheTime: 10 * 60 * 1000, // 10 minutes - tối ưu cho cache duration
    },
  },
});

// Usage
function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <MyComponent />
    </QueryClientProvider>
  );
}
```

---

### **Q36: Common Advanced Mistakes** 🔥

#### **🔍 Câu Hỏi:**
Common Mistakes Advanced?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Performance Mistakes**: Các lỗi về performance
  - *Là gì*: Mistakes dẫn đến poor performance, slow loading
  - *Tại sao xảy ra*: Không optimize code, không hiểu performance implications
  - *Khi nào xảy ra*: Khi không có performance testing, optimization

- **🎯 State Management Mistakes**: Các lỗi về state management
  - *Là gì*: Mistakes trong quản lý state, dẫn đến bugs, poor UX
  - *Tại sao xảy ra*: Không hiểu state flow, không có proper patterns
  - *Khi nào xảy ra*: Complex apps, multiple state sources

- **⚡ Security Mistakes**: Các lỗi về bảo mật
  - *Là gì*: Mistakes dẫn đến security vulnerabilities
  - *Tại sao xảy ra*: Không hiểu security best practices, không validate input
  - *Khi nào xảy ra*: Production apps, user data handling

- **✅ Architecture Mistakes**: Các lỗi về kiến trúc
  - *Là gì*: Mistakes trong thiết kế architecture, dẫn đến maintainability issues
  - *Tại sao xảy ra*: Không có proper planning, không follow patterns
  - *Khi nào xảy ra*: Large projects, team development

- **⚠️ Code Quality Mistakes**: Các lỗi về code quality
  - *Là gì*: Mistakes dẫn đến poor code quality, hard to maintain
  - *Tại sao xảy ra*: Không follow best practices, không có code review
  - *Khi nào xảy ra*: Rushed development, lack of standards

**1. Common Mistakes:**
```javascript
// ❌ Bad: Memory leaks - Tối ưu nhất cho memory leak prevention
useEffect(() => { // useEffect hook - tối ưu cho side effects
  const interval = setInterval(() => { // setInterval - tối ưu cho periodic tasks
    // Some logic - Some logic - tối ưu cho business logic
  }, 1000); // 1000ms interval - tối ưu cho timing
  // Missing cleanup - Missing cleanup - tối ưu cho resource management
}, []); // Empty dependency array - tối ưu cho effect timing

// ✅ Good: Proper cleanup
useEffect(() => {
  const interval = setInterval(() => {
    // Some logic
  }, 1000);

  return () => clearInterval(interval);
}, []);

// ❌ Bad: Unnecessary re-renders
function Component({ data }) {
  const expensiveValue = useMemo(() => {
    return data.map(item => item.value * 2);
  }, []); // Missing dependency

  return <div>{expensiveValue}</div>;
}

// ✅ Good: Correct dependencies
function Component({ data }) {
  const expensiveValue = useMemo(() => {
    return data.map(item => item.value * 2);
  }, [data]); // Correct dependency

  return <div>{expensiveValue}</div>;
}
```

---

### **Q37: Clean Code Best Practices** 🔥

#### **🔍 Câu Hỏi:**
Best Practices cho Clean code?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Clean Code Principles**: Các nguyên tắc viết code sạch
  - *Là gì*: Set of principles để write readable, maintainable code
  - *Tại sao cần*: Improve code quality, easier maintenance, better collaboration
  - *Khi nào dùng*: Mọi dự án, đặc biệt quan trọng với team development

- **🎯 Naming Conventions**: Quy tắc đặt tên
  - *Là gì*: Rules và patterns cho naming variables, functions, classes
  - *Tại sao cần*: Code dễ đọc, dễ hiểu, self-documenting
  - *Khi nào dùng*: Mọi code, đặc biệt quan trọng với team

- **⚡ Function Design**: Thiết kế functions hiệu quả
  - *Là gì*: Principles cho writing small, focused, single-purpose functions
  - *Tại sao cần*: Easier testing, debugging, maintenance
  - *Khi nào dùng*: Khi viết functions, methods

- **✅ Code Organization**: Tổ chức code logic
  - *Là gì*: Structure code theo logical patterns, modules
  - *Tại sao cần*: Easy navigation, maintainability, scalability
  - *Khi nào dùng*: Large projects, team development

- **⚠️ Common Anti-patterns**: Các anti-patterns cần tránh
  - *Là gì*: Patterns dẫn đến poor code quality, hard to maintain
  - *Tại sao cần*: Prevent technical debt, improve code quality
  - *Khi nào tránh*: Mọi code, đặc biệt quan trọng với production code

**1. Clean Code Principles:**
```javascript
// ✅ Good: Clean, readable code - Tối ưu nhất cho code readability
function calculateTotalPrice(items) { // Function name - tối ưu cho clarity
  const basePrice = items.reduce((sum, item) => sum + item.price, 0); // Base price calculation - tối ưu cho price aggregation
  const tax = basePrice * 0.1; // Tax calculation - tối ưu cho tax computation
  const discount = basePrice > 100 ? basePrice * 0.05 : 0; // Discount logic - tối ưu cho conditional discount

  return basePrice + tax - discount; // Return statement - tối ưu cho final calculation
}

// ✅ Good: Meaningful names
const isUserLoggedIn = user && user.id;
const hasValidEmail = email && email.includes('@');

// ✅ Good: Single responsibility
function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function formatCurrency(amount) {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(amount);
}
```

---
### **Q38: Domain to UI Rendering Process** 🔥

#### **🔍 Câu Hỏi:**
Quá trình user nhập 1 domain đến khi UI hiển thị trên màn hình thì phải trải qua bao nhiêu giai đoạn và giai đoạn đó là gì?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Browser Navigation Process**: Quá trình từ domain đến UI hiển thị
  - *Là gì*: Series of steps từ khi user nhập URL đến khi page hiển thị
  - *Tại sao cần hiểu*: Optimize performance, debug issues, understand web flow
  - *Khi nào quan trọng*: Performance optimization, troubleshooting, SEO

- **🎯 8 Giai Đoạn Chính**: Các bước trong quá trình navigation
  - *DNS Resolution*: Chuyển đổi domain thành IP address
  - *TCP Connection*: Thiết lập kết nối TCP với server
  - *TLS Handshake*: Thiết lập kết nối bảo mật HTTPS
  - *HTTP Request*: Gửi request đến server
  - *Server Processing*: Server xử lý request và trả response
    - **Server-side Processing**: Route handling, database queries, business logic
    - **Response Generation**: HTML, JSON, or other content generation
    - **Headers & Status**: HTTP status codes, response headers, cookies
  - *HTML Parsing*: Browser parse HTML và build DOM tree
    - **HTML Tokenization**: Chuyển đổi HTML text thành tokens
    - **DOM Tree Construction**: Build Document Object Model tree
    - **CSSOM Building**: Parse CSS và build CSS Object Model
    - **Render Tree Creation**: Combine DOM + CSSOM thành render tree
  - *Resource Loading*: Load CSS, JS, images, fonts
    - **Critical Resources**: CSS, JS blocking rendering
    - **Non-critical Resources**: Images, fonts, async scripts
    - **Resource Prioritization**: Browser tự động prioritize resources
    - **Preloading**: Preload important resources
  - *Rendering*: Render page và hiển thị trên màn hình
    - **Layout (Reflow)**: Calculate positions và sizes của elements
    - **Paint**: Fill pixels với colors, images, text
    - **Composite**: Combine layers thành final image
    - **Display**: Hiển thị final image trên screen

- **⚡ Performance Metrics**: Các chỉ số performance quan trọng
  - *DNS Lookup Time*: Thời gian resolve domain
  - *TCP Connection Time*: Thời gian thiết lập kết nối
  - *TTFB (Time to First Byte)*: Thời gian nhận response đầu tiên
  - *DOM Content Loaded*: Thời gian DOM ready
  - *Page Load Complete*: Thời gian page load hoàn toàn

- **✅ Optimization Strategies**: Các chiến lược tối ưu
  - *DNS Prefetch*: Pre-resolve DNS cho external domains
  - *HTTP/2*: Multiplexing, server push
  - *CDN*: Distribute content globally
  - *Caching*: Browser cache, service workers
  - *Code Splitting*: Load only necessary code

- **⚠️ Common Bottlenecks**: Các điểm nghẽn thường gặp
  - *Slow DNS*: DNS server chậm
  - *Network Latency*: Khoảng cách địa lý
  - *Server Response Time*: Server xử lý chậm
  - *Large Resources*: Images, JS, CSS files lớn
  - *Render Blocking*: CSS, JS blocking rendering

**1. Detailed Process Flow:**
```javascript
// 1. DNS Resolution - Tối ưu nhất cho domain resolution
const dnsResolution = {
  step: 'DNS Lookup', // DNS lookup - tối ưu cho domain resolution
  process: 'Domain → IP Address', // Domain to IP - tối ưu cho address resolution
  time: '50-200ms', // Resolution time - tối ưu cho performance
  optimization: 'DNS Prefetch' // DNS prefetch - tối ưu cho pre-resolution
};

// 2. TCP Connection - Tối ưu nhất cho connection establishment
const tcpConnection = {
  step: 'TCP Handshake', // TCP handshake - tối ưu cho connection setup
  process: '3-way handshake', // 3-way handshake - tối ưu cho reliable connection
  time: '100-300ms', // Connection time - tối ưu cho network performance
  optimization: 'HTTP/2, Keep-Alive' // HTTP/2 - tối ưu cho connection reuse
};

// 3. TLS Handshake - Tối ưu nhất cho secure connection
const tlsHandshake = {
  step: 'TLS Negotiation', // TLS negotiation - tối ưu cho security
  process: 'Certificate validation', // Certificate validation - tối ưu cho trust
  time: '200-500ms', // Handshake time - tối ưu cho security overhead
  optimization: 'TLS 1.3, Session resumption' // TLS 1.3 - tối ưu cho faster handshake
};

// 4. HTTP Request/Response - Tối ưu nhất cho data transfer
const httpRequest = {
  step: 'HTTP Request', // HTTP request - tối ưu cho data request
  process: 'GET /index.html', // GET request - tối ưu cho resource fetching
  time: '100-1000ms', // Request time - tối ưu cho server response
  optimization: 'Compression, HTTP/2' // Compression - tối ưu cho data size
};
```

**2. Server Processing Details:**
```javascript
// Server-side Processing - Tối ưu nhất cho request handling
const serverProcessing = {
  // Route handling - Tối ưu nhất cho URL routing
  routeHandling: {
    step: 'Route Resolution', // Route resolution - tối ưu cho URL matching
    process: 'Match URL to controller', // URL matching - tối ưu cho request routing
    time: '1-10ms', // Route time - tối ưu cho routing complexity
    optimization: 'Route caching, CDN' // Route caching - tối ưu cho repeated requests
  },

  // Database queries - Tối ưu nhất cho data retrieval
  databaseQueries: {
    step: 'Data Fetching', // Data fetching - tối ưu cho data retrieval
    process: 'SQL queries, ORM operations', // Database operations - tối ưu cho data access
    time: '10-500ms', // Query time - tối ưu cho database performance
    optimization: 'Query optimization, caching, indexing' // Query optimization - tối ưu cho database performance
  },

  // Business logic - Tối ưu nhất cho application logic
  businessLogic: {
    step: 'Application Logic', // Application logic - tối ưu cho business rules
    process: 'Data processing, validation', // Data processing - tối ưu cho business logic
    time: '5-100ms', // Logic time - tối ưu cho complexity
    optimization: 'Code optimization, caching' // Code optimization - tối ưu cho performance
  }
};

// Response Generation - Tối ưu nhất cho content creation
const responseGeneration = {
  // HTML generation - Tối ưu nhất cho HTML content
  htmlGeneration: {
    step: 'HTML Creation', // HTML creation - tối ưu cho content generation
    process: 'Template rendering, data binding', // Template rendering - tối ưu cho dynamic content
    time: '5-50ms', // Generation time - tối ưu cho template complexity
    optimization: 'Template caching, SSR' // Template caching - tối ưu cho repeated content
  },

  // Headers & Status - Tối ưu nhất cho HTTP response
  headersStatus: {
    step: 'HTTP Response', // HTTP response - tối ưu cho response formatting
    process: 'Status codes, headers, cookies', // Response formatting - tối ưu cho HTTP compliance
    time: '1-5ms', // Response time - tối ưu cho header complexity
    optimization: 'Header optimization, compression' // Header optimization - tối ưu cho response size
  }
};
```

**3. Browser Rendering Process:**
```javascript
// HTML Parsing - Tối ưu nhất cho DOM construction
const htmlParsing = {
  // HTML Tokenization - Tối ưu nhất cho HTML parsing
  tokenization: {
    step: 'HTML Tokenization', // HTML tokenization - tối ưu cho HTML parsing
    process: 'Convert HTML text to tokens', // Token conversion - tối ưu cho parsing efficiency
    time: '5-20ms', // Tokenization time - tối ưu cho HTML size
    optimization: 'Minify HTML, remove comments' // Minify HTML - tối ưu cho parsing speed
  },

  // DOM Tree Construction - Tối ưu nhất cho DOM building
  domConstruction: {
    step: 'DOM Tree Building', // DOM tree building - tối ưu cho document structure
    process: 'Create element nodes, build tree', // Tree building - tối ưu cho document hierarchy
    time: '10-50ms', // Construction time - tối ưu cho DOM complexity
    optimization: 'Efficient HTML structure' // Efficient structure - tối ưu cho DOM performance
  },

  // CSSOM Building - Tối ưu nhất cho style computation
  cssomBuilding: {
    step: 'CSSOM Creation', // CSSOM creation - tối ưu cho style object model
    process: 'Parse CSS, build style tree', // Style parsing - tối ưu cho style computation
    time: '5-30ms', // CSSOM time - tối ưu cho CSS complexity
    optimization: 'Critical CSS, CSS minification' // Critical CSS - tối ưu cho above-fold rendering
  },

  // Render Tree Creation - Tối ưu nhất cho rendering preparation
  renderTreeCreation: {
    step: 'Render Tree Building', // Render tree building - tối ưu cho rendering preparation
    process: 'Combine DOM + CSSOM', // Tree combination - tối ưu cho rendering efficiency
    time: '5-20ms', // Render tree time - tối ưu cho tree complexity
    optimization: 'Efficient CSS selectors' // Efficient selectors - tối ưu cho style matching
  }
};

**4. Resource Loading Details:**
```javascript
// Resource Loading - Tối ưu nhất cho resource management
const resourceLoading = {
  // Critical Resources - Tối ưu nhất cho blocking resources
  criticalResources: {
    step: 'Critical Resource Loading', // Critical loading - tối ưu cho blocking resources
    process: 'Load CSS, blocking JS', // Blocking resources - tối ưu cho render blocking
    time: '50-200ms', // Critical time - tối ưu cho critical path
    optimization: 'Critical CSS inlining, JS defer/async' // Critical optimization - tối ưu cho render blocking
  },

  // Non-critical Resources - Tối ưu nhất cho non-blocking resources
  nonCriticalResources: {
    step: 'Non-critical Loading', // Non-critical loading - tối ưu cho non-blocking resources
    process: 'Load images, fonts, async scripts', // Non-blocking resources - tối ưu cho parallel loading
    time: '100-1000ms', // Non-critical time - tối ưu cho resource size
    optimization: 'Lazy loading, preloading, compression' // Non-critical optimization - tối ưu cho resource efficiency
  },

  // Resource Prioritization - Tối ưu nhất cho loading priority
  resourcePrioritization: {
    step: 'Resource Prioritization', // Resource prioritization - tối ưu cho loading order
    process: 'Browser auto-prioritize resources', // Auto prioritization - tối ưu cho loading efficiency
    time: 'Real-time', // Prioritization time - tối ưu cho dynamic priority
    optimization: 'Resource hints, preload, prefetch' // Priority optimization - tối ưu cho loading hints
  },

  // Preloading - Tối ưu nhất cho resource preloading
  preloading: {
    step: 'Resource Preloading', // Resource preloading - tối ưu cho early loading
    process: 'Preload important resources', // Early loading - tối ưu cho resource availability
    time: 'Parallel with parsing', // Preload time - tối ưu cho parallel loading
    optimization: 'Preload, prefetch, preconnect' // Preload optimization - tối ưu cho resource hints
  }
};
```

**5. Rendering Pipeline Details:**
```javascript
// Rendering Pipeline - Tối ưu nhất cho visual rendering
const renderingPipeline = {
  // Layout (Reflow) - Tối ưu nhất cho layout calculation
  layout: {
    step: 'Layout Calculation', // Layout calculation - tối ưu cho position calculation
    process: 'Calculate positions, sizes of elements', // Position calculation - tối ưu cho layout computation
    time: '10-50ms', // Layout time - tối ưu cho layout complexity
    optimization: 'Avoid layout thrashing, use CSS transforms' // Layout optimization - tối ưu cho layout performance
  },

  // Paint - Tối ưu nhất cho pixel filling
  paint: {
    step: 'Paint Process', // Paint process - tối ưu cho pixel rendering
    process: 'Fill pixels with colors, images, text', // Pixel filling - tối ưu cho visual rendering
    time: '10-100ms', // Paint time - tối ưu cho visual complexity
    optimization: 'Use CSS transforms, avoid repaints' // Paint optimization - tối ưu cho paint performance
  },

  // Composite - Tối ưu nhất cho layer composition
  composite: {
    step: 'Layer Composition', // Layer composition - tối ưu cho layer combining
    process: 'Combine layers into final image', // Layer combining - tối ưu cho final rendering
    time: '5-20ms', // Composite time - tối ưu cho layer complexity
    optimization: 'GPU acceleration, layer optimization' // Composite optimization - tối ưu cho GPU performance
  },

  // Display - Tối ưu nhất cho screen display
  display: {
    step: 'Screen Display', // Screen display - tối ưu cho final output
    process: 'Display final image on screen', // Final display - tối ưu cho screen rendering
    time: '1-5ms', // Display time - tối ưu cho screen refresh
    optimization: 'VSync, frame rate optimization' // Display optimization - tối ưu cho smooth display
  }
};

// JavaScript Execution - Tối ưu nhất cho interactivity
const jsExecution = {
  step: 'JS Parsing & Execution', // JS execution - tối ưu cho interactivity
  process: 'Parse, Compile, Execute', // JS process - tối ưu cho script processing
  time: '50-500ms', // JS time - tối ưu cho script complexity
  optimization: 'Code splitting, Lazy loading' // Code splitting - tối ưu cho initial load
};

// Rendering - Tối ưu nhất cho visual display
const rendering = {
  step: 'Paint & Composite', // Paint & composite - tối ưu cho visual rendering
  process: 'Layout → Paint → Composite', // Rendering pipeline - tối ưu cho display
  time: '10-100ms', // Rendering time - tối ưu cho visual complexity
  optimization: 'GPU acceleration, Layer optimization' // GPU acceleration - tối ưu cho performance
};
```

**3. Performance Monitoring:**
```javascript
// Performance API - Tối ưu nhất cho performance measurement
const performanceMonitoring = {
  // Navigation timing - Tối ưu nhất cho navigation metrics
  navigationTiming: {
    dnsLookup: performance.timing.domainLookupEnd - performance.timing.domainLookupStart, // DNS lookup time - tối ưu cho DNS performance
    tcpConnect: performance.timing.connectEnd - performance.timing.connectStart, // TCP connection time - tối ưu cho connection performance
    ttfb: performance.timing.responseStart - performance.timing.navigationStart, // TTFB - tối ưu cho server response
    domReady: performance.timing.domContentLoadedEventEnd - performance.timing.navigationStart, // DOM ready - tối ưu cho DOM performance
    pageLoad: performance.timing.loadEventEnd - performance.timing.navigationStart // Page load - tối ưu cho complete load
  },

  // Resource timing - Tối ưu nhất cho resource metrics
  resourceTiming: {
    cssLoad: performance.getEntriesByType('resource').filter(r => r.name.includes('.css')), // CSS load time - tối ưu cho style performance
    jsLoad: performance.getEntriesByType('resource').filter(r => r.name.includes('.js')), // JS load time - tối ưu cho script performance
    imageLoad: performance.getEntriesByType('resource').filter(r => /\.(jpg|png|gif|webp)$/.test(r.name)) // Image load time - tối ưu cho media performance
  }
};
```

**🔥 SO SÁNH TỐI ƯU - Navigation Optimization:**

| Stage | Sub-stage | Time Range | Optimization | Tại sao tối ưu cho use case cụ thể |
|-------|-----------|------------|--------------|-----------------------------------|
| **DNS Resolution** | - | 50-200ms | DNS Prefetch | Tối ưu cho pre-resolution, giảm lookup time |
| **TCP Connection** | - | 100-300ms | HTTP/2, Keep-Alive | Tối ưu cho connection reuse, multiplexing |
| **TLS Handshake** | - | 200-500ms | TLS 1.3, Session resumption | Tối ưu cho faster handshake, session reuse |
| **HTTP Request** | - | 100-1000ms | Compression, CDN | Tối ưu cho data transfer, global distribution |
| **Server Processing** | Route Handling | 1-10ms | Route caching, CDN | Tối ưu cho repeated requests, global distribution |
| | Database Queries | 10-500ms | Query optimization, caching | Tối ưu cho database performance, data access |
| | Business Logic | 5-100ms | Code optimization, caching | Tối ưu cho application performance, logic efficiency |
| | Response Generation | 5-50ms | Template caching, SSR | Tối ưu cho content generation, server-side rendering |
| **HTML Parsing** | Tokenization | 5-20ms | Minify HTML, remove comments | Tối ưu cho parsing speed, smaller payload |
| | DOM Construction | 10-50ms | Efficient HTML structure | Tối ưu cho DOM performance, document hierarchy |
| | CSSOM Building | 5-30ms | Critical CSS, CSS minification | Tối ưu cho above-fold rendering, style computation |
| | Render Tree | 5-20ms | Efficient CSS selectors | Tối ưu cho rendering preparation, style matching |
| **Resource Loading** | Critical Resources | 50-200ms | Critical CSS inlining, JS defer/async | Tối ưu cho render blocking, critical path |
| | Non-critical Resources | 100-1000ms | Lazy loading, preloading | Tối ưu cho resource efficiency, parallel loading |
| | Resource Prioritization | Real-time | Resource hints, preload, prefetch | Tối ưu cho loading hints, dynamic priority |
| | Preloading | Parallel | Preload, prefetch, preconnect | Tối ưu cho early loading, resource availability |
| **Rendering** | Layout (Reflow) | 10-50ms | Avoid layout thrashing, CSS transforms | Tối ưu cho layout performance, position calculation |
| | Paint | 10-100ms | CSS transforms, avoid repaints | Tối ưu cho paint performance, pixel rendering |
| | Composite | 5-20ms | GPU acceleration, layer optimization | Tối ưu cho GPU performance, layer combining |
| | Display | 1-5ms | VSync, frame rate optimization | Tối ưu cho smooth display, screen rendering |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ SAI: Không optimize DNS resolution - Không tối ưu DNS resolution
// Không có DNS prefetch - ❌ Tăng DNS lookup time
<link rel="dns-prefetch" href="//fonts.googleapis.com"> // ❌ Thiếu DNS prefetch

// ✅ ĐÚNG: Optimize DNS resolution - Tối ưu DNS resolution
<link rel="dns-prefetch" href="//fonts.googleapis.com"> // ✅ DNS prefetch - tối ưu cho pre-resolution
<link rel="dns-prefetch" href="//cdn.example.com"> // ✅ CDN prefetch - tối ưu cho resource loading

// ❌ SAI: Render blocking resources - Resources blocking rendering
<link rel="stylesheet" href="styles.css"> // ❌ CSS blocking render - tăng render time
<script src="app.js"></script> // ❌ JS blocking render - tăng render time

// ✅ ĐÚNG: Non-blocking resources - Resources không blocking
<link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'"> // ✅ Preload CSS - tối ưu cho non-blocking
<script src="app.js" defer></script> // ✅ Defer JS - tối ưu cho non-blocking execution

// ❌ SAI: Không monitor performance - Không theo dõi performance
// Không có performance monitoring - ❌ Không biết bottlenecks

// ✅ ĐÚNG: Monitor performance - Theo dõi performance
const observer = new PerformanceObserver((list) => { // Performance observer - tối ưu cho monitoring
  list.getEntries().forEach((entry) => { // Performance entries - tối ưu cho metrics
    console.log(`${entry.name}: ${entry.duration}ms`); // Log performance - tối ưu cho debugging
  });
}); // Performance monitoring - tối ưu cho optimization
observer.observe({entryTypes: ['navigation', 'resource']}); // Observe performance - tối ưu cho tracking
```

#### **✅ Best Practices:**

- **🚀 DNS Optimization**: Use DNS prefetch cho external domains
- **⚡ Connection Optimization**: Use HTTP/2, keep-alive connections
- **🔒 Security**: Use TLS 1.3, session resumption
- **📦 Resource Optimization**: Minify, compress, use CDN
- **🎨 Rendering Optimization**: Critical CSS, code splitting, lazy loading
- **📊 Performance Monitoring**: Use Performance API, monitor Core Web Vitals
- **🔄 Caching Strategy**: Browser cache, service workers, HTTP caching
- **📱 Mobile Optimization**: Optimize for mobile networks, reduce payload

---

## **🎯 Tổng Kết Kiến Thức Frontend Advanced**

### **🔥 Tech Stack Chính:**
- **Build Tools**: Vite (tối ưu nhất), Webpack, Babel
- **Frameworks**: React, Next.js, React Native
- **State Management**: Zustand (đơn giản), Redux (phức tạp), Context API
- **Data Fetching**: React Query, SWR, Axios
- **Styling**: Tailwind CSS, Styled Components, CSS Modules
- **Testing**: Jest, React Testing Library, Cypress
- **Monorepo**: Nx, Lerna, Yarn Workspaces
- **Documentation**: Storybook, Docusaurus

### **📚 Kiến Thức Cốt Lõi:**

#### **1. Module System & Build (Q1-Q4)**
- **ES Modules** > CommonJS (tree shaking tốt hơn)
- **Vite** > Webpack (faster dev server)
- **Tree Shaking**: Loại bỏ dead code, giảm bundle size
- **Compiler vs Transpiler**: TypeScript compiler, Babel transpiler

#### **2. Performance & Web Vitals (Q5-Q7)**
- **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1
- **Caching**: Browser cache, CDN, Service Workers
- **Optimization**: Code splitting, lazy loading, image optimization

#### **3. Development Workflow (Q8-Q10)**
- **Git Flow**: Feature branches, PR reviews, CI/CD
- **Architecture**: Container/Presentational, Custom Hooks
- **Design Patterns**: Observer, Factory, Strategy, Singleton

#### **4. Storage & Security (Q11-Q14)**
- **Storage**: localStorage (persistent), sessionStorage (temporary), IndexedDB (large data)
- **Security**: HTTPS, CSP headers, input validation, XSS/CSRF prevention
- **Authentication**: JWT + Refresh Token, secure storage

#### **5. Testing & Code Quality (Q15-Q17)**
- **Testable Code**: Pure functions, dependency injection, isolated components
- **Tools**: ESLint, Prettier, Husky (git hooks)
- **External vs Self-implement**: Đánh giá cost/benefit

#### **6. Communication & i18n (Q18-Q19)**
- **API Communication**: REST, GraphQL, WebSocket, SSE
- **i18n**: react-i18next, namespace organization, lazy loading

#### **7. Advanced Concepts (Q20-Q25)**
- **WebSocket**: Real-time communication, Socket.IO
- **Browser Navigation**: URL processing, routing
- **Error Tracking**: Sentry, Grafana monitoring
- **Micro Frontend**: Module Federation, Nx monorepo
- **File Handling**: Upload with progress, download strategies
- **Request Cancellation**: AbortController

#### **8. Rendering & Optimization (Q26-Q29)**
- **CSR vs SSR**: Client-side vs Server-side rendering
- **Web Workers**: Background processing, heavy computations
- **Next.js**: App Router, Server Components, ISR
- **HTTP Status**: 2xx (success), 3xx (redirect), 4xx (client error), 5xx (server error)

#### **9. State Management & Tools (Q30-Q33)**
- **State Management**: Zustand (simple), Redux (complex), Context API (built-in)
- **Monorepo**: Nx (enterprise), Lerna (packages), Yarn Workspaces (simple)
- **Lifecycle**: React hooks, Next.js pages, React Native navigation
- **Documentation**: Storybook (components), Docusaurus (docs)

#### **10. Best Practices (Q34-Q37)**
- **Security**: Input validation, HTTPS, secure cookies, rate limiting
- **React Query**: Caching, background updates, error handling
- **Common Mistakes**: Memory leaks, unnecessary re-renders, poor naming
- **Clean Code**: Meaningful names, small functions, proper organization

#### **11. Browser Navigation & Rendering (Q38)**
- **Navigation Process**: DNS → TCP → TLS → HTTP → Server → HTML → Resources → Rendering
- **Performance Metrics**: DNS lookup, TTFB, DOM ready, page load
- **Optimization**: DNS prefetch, HTTP/2, CDN, caching, code splitting
- **Monitoring**: Performance API, Core Web Vitals, resource timing

#### **12. Complex Project Experience (Q39)**
- **Project Scale**: Large codebase, multiple teams, high-traffic applications
- **Architecture**: Micro frontend, scalable design, independent deployment
- **Performance**: Advanced optimization, real-time data, caching strategies
- **Testing**: Comprehensive testing, quality assurance, risk mitigation

### **💡 Key Takeaways:**
1. **Performance First**: Monitor Web Vitals, optimize bundle size
2. **Security Always**: Validate input, use HTTPS, secure storage
3. **Code Quality**: Write testable code, follow clean code principles
4. **Modern Tools**: Use Vite, React Query, Zustand for better DX
5. **Architecture**: Plan for scalability, use design patterns
6. **Testing**: Write tests, use proper tools, maintain quality

### **🚀 Ready for:**
- **Frontend Interviews** (Senior/Lead level)
- **Production Development** (Enterprise apps)
- **Technical Discussions** (Architecture, performance)
- **Code Reviews** (Best practices, security)
- **Team Leadership** (Standards, tooling decisions)

---

### **Q39: Complex Frontend Project Experience** 🔥

#### **🔍 Câu Hỏi:**
Mô tả dự án frontend phức tạp nhất bạn từng làm?

#### **💡 Trả Lời Chi Tiết:**

**Trả lời:**
- **🔥 Complex Frontend Project**: Dự án frontend phức tạp với nhiều thách thức
  - *Là gì*: Large-scale frontend application với complex requirements
  - *Tại sao phức tạp*: Multiple teams, complex business logic, performance requirements
  - *Khi nào gặp*: Enterprise applications, real-time systems, high-traffic platforms

- **🎯 Project Characteristics**: Đặc điểm của dự án phức tạp
  - *Scale*: Large codebase, multiple modules, many developers
  - *Performance*: High performance requirements, real-time updates
  - *Integration*: Multiple APIs, microservices, third-party services
  - *User Experience*: Complex UI/UX, accessibility, internationalization

- **⚡ Technical Challenges**: Các thách thức kỹ thuật
  - *Architecture*: Scalable architecture, state management, data flow
  - *Performance*: Bundle optimization, lazy loading, caching strategies
  - *Real-time*: WebSocket connections, data synchronization, conflict resolution
  - *Testing*: Complex testing scenarios, integration testing, E2E testing

- **✅ Solutions Implemented**: Các giải pháp đã triển khai
  - *Micro Frontend*: Module Federation, independent deployments
  - *State Management*: Redux/Zustand với complex state logic
  - *Performance*: Code splitting, lazy loading, CDN optimization
  - *Monitoring*: Error tracking, performance monitoring, analytics

- **⚠️ Lessons Learned**: Bài học rút ra
  - *Planning*: Proper planning, architecture decisions, team coordination
  - *Communication*: Clear communication, documentation, code reviews
  - *Iterative Development*: Incremental development, continuous integration
  - *User Feedback*: User testing, feedback loops, iterative improvements

**1. Project Overview:**
```javascript
// Complex Trading Platform - Tối ưu nhất cho financial applications
const tradingPlatform = {
  // Project scale - Tối ưu nhất cho large-scale applications
  scale: {
    codebase: '500k+ lines of code', // Large codebase - tối ưu cho enterprise applications
    modules: '15+ micro frontends', // Multiple modules - tối ưu cho modular architecture
    developers: '25+ developers', // Large team - tối ưu cho team collaboration
    users: '100k+ concurrent users' // High traffic - tối ưu cho scalability
  },

  // Technical complexity - Tối ưu nhất cho complex requirements
  complexity: {
    realTimeData: 'WebSocket connections', // Real-time data - tối ưu cho live updates
    stateManagement: 'Complex state logic', // State management - tối ưu cho data flow
    performance: 'Sub-100ms response time', // Performance - tối ưu cho user experience
    integration: '20+ microservices' // Integration - tối ưu cho service architecture
  }
};
```

**2. Architecture Design:**
```javascript
// Micro Frontend Architecture - Tối ưu nhất cho scalable applications
const microFrontendArchitecture = {
  // Shell application - Tối ưu nhất cho application shell
  shell: {
    name: 'Trading Shell', // Shell name - tối ưu cho application container
    responsibilities: ['Routing', 'Authentication', 'Layout'], // Shell responsibilities - tối ưu cho core functionality
    technology: 'React + Module Federation', // Technology stack - tối ưu cho micro frontend
    deployment: 'Independent deployment' // Independent deployment - tối ưu cho team autonomy
  },

  // Micro frontends - Tối ưu nhất cho feature modules
  microFrontends: {
    tradingDashboard: {
      name: 'Trading Dashboard', // Dashboard name - tối ưu cho trading interface
      team: 'Trading Team', // Team ownership - tối ưu cho team responsibility
      technology: 'React + Redux', // Technology - tối ưu cho state management
      features: ['Real-time charts', 'Order management', 'Portfolio view'] // Features - tối ưu cho trading functionality
    },

    marketData: {
      name: 'Market Data', // Market data - tối ưu cho market information
      team: 'Data Team', // Data team - tối ưu cho data expertise
      technology: 'Vue.js + WebSocket', // Technology - tối ưu cho real-time data
      features: ['Live prices', 'Market depth', 'News feed'] // Features - tối ưu cho market data
    },

    userManagement: {
      name: 'User Management', // User management - tối ưu cho user operations
      team: 'Platform Team', // Platform team - tối ưu cho platform services
      technology: 'Angular + NgRx', // Technology - tối ưu cho enterprise features
      features: ['User profiles', 'Permissions', 'Audit logs'] // Features - tối ưu cho user management
    }
  }
};
```

**3. Performance Optimization:**
```javascript
// Performance Optimization Strategies - Tối ưu nhất cho high-performance applications
const performanceOptimization = {
  // Bundle optimization - Tối ưu nhất cho bundle size
  bundleOptimization: {
    codeSplitting: {
      strategy: 'Route-based + Feature-based', // Splitting strategy - tối ưu cho loading efficiency
      result: 'Initial bundle < 200KB', // Bundle size - tối ưu cho fast loading
      implementation: 'Dynamic imports, lazy loading' // Implementation - tối ưu cho code splitting
    },

    treeShaking: {
      strategy: 'ES Modules + sideEffects config', // Tree shaking - tối ưu cho dead code elimination
      result: '40% bundle size reduction', // Size reduction - tối ưu cho performance
      implementation: 'Webpack optimization, library analysis' // Implementation - tối ưu cho tree shaking
    }
  },

  // Caching strategies - Tối ưu nhất cho data caching
  cachingStrategies: {
    browserCache: {
      strategy: 'Service Worker + Cache API', // Browser caching - tối ưu cho offline support
      result: '90% cache hit rate', // Cache hit rate - tối ưu cho performance
      implementation: 'Stale-while-revalidate pattern' // Implementation - tối ưu cho cache strategy
    },

    cdnCache: {
      strategy: 'Multi-region CDN', // CDN caching - tối ưu cho global distribution
      result: '50% faster global load times', // Load time improvement - tối ưu cho user experience
      implementation: 'CloudFront + edge locations' // Implementation - tối ưu cho CDN performance
    }
  },

  // Real-time optimization - Tối ưu nhất cho real-time performance
  realTimeOptimization: {
    websocketManagement: {
      strategy: 'Connection pooling + reconnection', // WebSocket management - tối ưu cho connection stability
      result: '99.9% connection uptime', // Connection uptime - tối ưu cho reliability
      implementation: 'Socket.IO + heartbeat mechanism' // Implementation - tối ưu cho WebSocket reliability
    },

    dataSync: {
      strategy: 'Optimistic updates + conflict resolution', // Data synchronization - tối ưu cho data consistency
      result: 'Sub-50ms data updates', // Update latency - tối ưu cho real-time performance
      implementation: 'CRDT + operational transforms' // Implementation - tối ưu cho conflict resolution
    }
  }
};
```

**4. State Management Complexity:**
```javascript
// Complex State Management - Tối ưu nhất cho complex state logic
const complexStateManagement = {
  // Global state structure - Tối ưu nhất cho application state
  globalState: {
    user: {
      profile: 'User profile data', // User profile - tối ưu cho user information
      permissions: 'Role-based permissions', // Permissions - tối ưu cho access control
      preferences: 'User preferences' // Preferences - tối ưu cho personalization
    },

    trading: {
      portfolio: 'Portfolio data', // Portfolio - tối ưu cho investment data
      orders: 'Active orders', // Orders - tối ưu cho order management
      positions: 'Current positions' // Positions - tối ưu cho position tracking
    },

    market: {
      prices: 'Real-time prices', // Prices - tối ưu cho market data
      depth: 'Market depth data', // Market depth - tối ưu cho order book
      news: 'Market news feed' // News - tối ưu cho market information
    }
  },

  // State synchronization - Tối ưu nhất cho data consistency
  stateSynchronization: {
    realTimeSync: {
      strategy: 'WebSocket + Redux middleware', // Real-time sync - tối ưu cho live updates
      implementation: 'Custom middleware for data updates', // Implementation - tối ưu cho state updates
      conflictResolution: 'Last-write-wins + user confirmation' // Conflict resolution - tối ưu cho data consistency
    },

    offlineSync: {
      strategy: 'Local storage + sync queue', // Offline sync - tối ưu cho offline support
      implementation: 'Redux persist + background sync', // Implementation - tối ưu cho offline functionality
      conflictResolution: 'Timestamp-based resolution' // Conflict resolution - tối ưu cho offline conflicts
    }
  }
};
```

**5. Testing Strategy:**
```javascript
// Comprehensive Testing Strategy - Tối ưu nhất cho quality assurance
const testingStrategy = {
  // Unit testing - Tối ưu nhất cho component testing
  unitTesting: {
    coverage: '90%+ code coverage', // Coverage - tối ưu cho code quality
    tools: 'Jest + React Testing Library', // Testing tools - tối ưu cho React testing
    focus: 'Business logic, utility functions' // Focus areas - tối ưu cho critical code
  },

  // Integration testing - Tối ưu nhất cho integration testing
  integrationTesting: {
    coverage: 'API integration, state management', // Coverage - tối ưu cho integration quality
    tools: 'Cypress + MSW', // Testing tools - tối ưu cho integration testing
    focus: 'User workflows, data flow' // Focus areas - tối ưu cho user scenarios
  },

  // E2E testing - Tối ưu nhất cho end-to-end testing
  e2eTesting: {
    coverage: 'Critical user journeys', // Coverage - tối ưu cho user experience
    tools: 'Playwright + Test containers', // Testing tools - tối ưu cho E2E testing
    focus: 'Trading workflows, real-time updates' // Focus areas - tối ưu cho business critical paths
  },

  // Performance testing - Tối ưu nhất cho performance validation
  performanceTesting: {
    coverage: 'Load testing, stress testing', // Coverage - tối ưu cho performance validation
    tools: 'K6 + Lighthouse CI', // Testing tools - tối ưu cho performance testing
    focus: 'Real-time data handling, concurrent users' // Focus areas - tối ưu cho performance critical areas
  }
};
```

**🔥 SO SÁNH TỐI ƯU - Complex Project Approaches:**

| Aspect | Simple Project | Complex Project | Tại sao tối ưu cho use case cụ thể |
|--------|----------------|-----------------|-----------------------------------|
| **Architecture** | Monolithic | Micro Frontend | Tối ưu cho team autonomy, independent deployment |
| **State Management** | Local state | Global state management | Tối ưu cho data consistency, complex state logic |
| **Performance** | Basic optimization | Advanced optimization | Tối ưu cho high-traffic, real-time requirements |
| **Testing** | Unit tests | Comprehensive testing | Tối ưu cho quality assurance, risk mitigation |
| **Deployment** | Single deployment | CI/CD pipeline | Tối ưu cho continuous delivery, team collaboration |
| **Monitoring** | Basic logging | Advanced monitoring | Tối ưu cho production stability, performance tracking |
| **Scalability** | Single team | Multiple teams | Tối ưu cho large-scale development, team coordination |
| **Maintenance** | Simple maintenance | Complex maintenance | Tối ưu cho long-term sustainability, code quality |

#### **❌ Common Mistakes - Lỗi Thường Gặp:**

```javascript
// ❌ SAI: Không plan architecture từ đầu - Không lên kế hoạch architecture
// Bắt đầu với monolithic architecture - ❌ Khó scale khi project lớn
const badArchitecture = {
  approach: 'Monolithic frontend', // Monolithic - ❌ Khó maintain và scale
  problems: ['Tight coupling', 'Single point of failure', 'Team conflicts'] // Problems - ❌ Architecture issues
};

// ✅ ĐÚNG: Plan architecture từ đầu - Lên kế hoạch architecture
const goodArchitecture = {
  approach: 'Micro frontend architecture', // Micro frontend - ✅ Scalable và maintainable
  benefits: ['Team autonomy', 'Independent deployment', 'Technology diversity'] // Benefits - ✅ Architecture advantages
};

// ❌ SAI: Không optimize performance từ đầu - Không tối ưu performance
// Chỉ optimize khi có vấn đề - ❌ Tăng technical debt
const badPerformance = {
  approach: 'Optimize later', // Optimize later - ❌ Reactive approach
  problems: ['Poor user experience', 'High bounce rate', 'Technical debt'] // Problems - ❌ Performance issues
};

// ✅ ĐÚNG: Performance-first approach - Approach tối ưu performance
const goodPerformance = {
  approach: 'Performance by design', // Performance by design - ✅ Proactive approach
  benefits: ['Better UX', 'Lower bounce rate', 'Scalable architecture'] // Benefits - ✅ Performance advantages
};

// ❌ SAI: Không có testing strategy - Không có chiến lược testing
// Chỉ test khi có bug - ❌ Tăng maintenance cost
const badTesting = {
  approach: 'Test when bugs occur', // Test when bugs - ❌ Reactive testing
  problems: ['High bug rate', 'Poor code quality', 'Maintenance issues'] // Problems - ❌ Quality issues
};

// ✅ ĐÚNG: Comprehensive testing strategy - Chiến lược testing toàn diện
const goodTesting = {
  approach: 'Test-driven development', // TDD - ✅ Proactive testing
  benefits: ['High code quality', 'Fewer bugs', 'Confident refactoring'] // Benefits - ✅ Quality advantages
};
```

#### **✅ Best Practices:**

- **🏗️ Architecture First**: Plan scalable architecture từ đầu
- **⚡ Performance by Design**: Optimize performance từ design phase
- **🧪 Testing Strategy**: Implement comprehensive testing strategy
- **📊 Monitoring & Analytics**: Set up monitoring và analytics từ đầu
- **👥 Team Collaboration**: Establish clear communication và collaboration
- **🔄 CI/CD Pipeline**: Implement automated deployment pipeline
- **📚 Documentation**: Maintain comprehensive documentation
- **🎯 User-Centric**: Focus on user experience và business value
- **🔒 Security**: Implement security best practices
- **📈 Scalability**: Plan for future growth và scalability

---

