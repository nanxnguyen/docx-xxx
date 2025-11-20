# ⚡ Q58: Build Tools - Vite vs Webpack vs Rollup, SWC vs Babel, Turbopack, esbuild

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">⚡ Q58: Build Tools - Vite vs Webpack vs Rollup, SWC vs Babel, Turbopack, esbuild</span></summary>


**❓ Câu Hỏi:**
So sánh các build tools hiện đại (công cụ build): Vite, Webpack, Rollup, esbuild, Turbopack và transpilers (trình chuyển đổi code): SWC vs Babel. Khi nào nên dùng tool nào?


#### **📊 Build Tools Ecosystem - Tổng Quan Hệ Sinh Thái Công Cụ Build**

```
┌──────────────────────────────────────────────────────────────────────┐
│                    BUILD TOOLS LANDSCAPE 2024                        │
│                 (Bản Đồ Công Cụ Build Năm 2024)                     │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  🏗️ BUNDLERS (Module Bundling - Đóng Gói Module)                    │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  • Webpack     - Lâu đời nhất, config phức tạp (2012)         │ │
│  │                  Như ông già giàu kinh nghiệm                  │ │
│  │  • Rollup      - Chuyên về ESM, tree-shaking tốt nhất (2015)  │ │
│  │                  Như chuyên gia dọn rác code                   │ │
│  │  • Vite        - Hiện đại, dev server siêu nhanh (2020)       │ │
│  │                  Như xe đua F1                                  │ │
│  │  • Turbopack   - Viết bằng Rust, tích hợp Next.js (2022)      │ │
│  │                  Như tên lửa SpaceX                             │ │
│  │  • esbuild     - Tốc độ khủng, viết bằng Go (2020)            │ │
│  │                  Như máy bay siêu thanh                         │ │
│  └────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ⚙️ TRANSPILERS (Code Transformation - Chuyển Đổi Code)             │
│  ┌────────────────────────────────────────────────────────────────┐ │
│  │  • Babel       - Tương thích tốt nhất, nhiều plugin (2014)    │ │
│  │                  Như thông dịch viên chuyên nghiệp             │ │
│  │  • SWC         - Viết bằng Rust, nhanh gấp 20x Babel (2020)   │ │
│  │                  Như thông dịch viên AI siêu tốc               │ │
│  └────────────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

---

#### **1️⃣ SO SÁNH CÁC BUNDLERS (Công Cụ Đóng Gói)**

**📊 Bảng So Sánh Hiệu Suất & Tính Năng:**

| Tính Năng | **Webpack** | **Rollup** | **Vite** | **esbuild** | **Turbopack** |
|---------|-------------|------------|----------|-------------|---------------|
| **Tốc độ Dev** (Chạy dev server) | ⭐⭐ Chậm | ⭐⭐⭐ Trung bình | ⭐⭐⭐⭐⭐ Nhanh | ⭐⭐⭐⭐⭐ Nhanh nhất | ⭐⭐⭐⭐⭐ Nhanh nhất |
| **Tốc độ Build** (Build production) | ⭐⭐ 10 giây | ⭐⭐⭐ 5 giây | ⭐⭐⭐⭐ 2 giây | ⭐⭐⭐⭐⭐ 0.5 giây | ⭐⭐⭐⭐⭐ 1 giây |
| **Tree-shaking** (Loại bỏ code thừa) | ⭐⭐⭐ Tốt | ⭐⭐⭐⭐⭐ Tốt nhất | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐⭐ Tốt |
| **Code Splitting** (Chia nhỏ bundle) | ⭐⭐⭐⭐⭐ Tốt nhất | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐ Cơ bản | ⭐⭐⭐⭐ Tốt |
| **HMR** (Hot Module Reload - Cập nhật nóng) | ⭐⭐⭐ Tốt | ⭐⭐ Chậm | ⭐⭐⭐⭐⭐ Tức thì | ❌ Không có | ⭐⭐⭐⭐⭐ Tức thì |
| **Config** (Độ phức tạp cấu hình) | ⭐⭐ Phức tạp | ⭐⭐⭐⭐ Đơn giản | ⭐⭐⭐⭐⭐ Rất đơn giản | ⭐⭐⭐ Hạn chế | ⭐⭐⭐⭐ Đơn giản |
| **Plugins** (Hệ sinh thái plugin) | ⭐⭐⭐⭐⭐ Khổng lồ | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐⭐ Đang phát triển | ⭐⭐ Hạn chế | ⭐⭐ Mới |
| **Bundle Size** (Kích thước file đóng gói) | ⭐⭐⭐ Tốt | ⭐⭐⭐⭐⭐ Nhỏ nhất | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐⭐ Tốt | ⭐⭐⭐⭐ Tốt |
| **Độ trưởng thành** | ⭐⭐⭐⭐⭐ 12 năm | ⭐⭐⭐⭐⭐ 9 năm | ⭐⭐⭐⭐ 4 năm | ⭐⭐⭐ 4 năm | ⭐⭐ 2 năm |
| **Độ khó học** | ⭐⭐ Khó | ⭐⭐⭐⭐ Dễ | ⭐⭐⭐⭐⭐ Rất dễ | ⭐⭐⭐⭐ Dễ | ⭐⭐⭐ Trung bình |

---

#### **🔹 A. Webpack - "Ông Già Giàu Kinh Nghiệm"**

**💡 Tổng Quan:**
- Bundler lâu đời nhất, cấu hình linh hoạt (12 năm tuổi - ra đời 2012)
- Hệ sinh thái plugin khổng lồ (hàng ngàn plugins)
- Dev server chậm, config phức tạp (có thể 500+ dòng)
- Phù hợp nhất cho app lớn, phức tạp, enterprise

**✅ Điểm Mạnh (Strengths):**
1. **Trưởng Thành & Ổn Định**: 12 năm kiểm nghiệm, production-ready
   - Mọi bugs đã được fix qua nhiều năm
   - Hỗ trợ mọi edge cases
   - Dùng bởi Facebook, Google, Microsoft

2. **Hệ Sinh Thái Plugin Khổng Lồ**: Hàng ngàn plugins có sẵn
   - Muốn gì cũng có plugin: CSS, images, fonts, WebAssembly
   - Cộng đồng lớn, dễ tìm giải pháp

3. **Code Splitting Nâng Cao**: Chiến lược chia nhỏ bundle phức tạp
   - Dynamic imports: `import('./module').then(...)`
   - Split by route, vendor, common chunks
   - Tối ưu load time

4. **Quản Lý Assets Toàn Diện**: Images, fonts, CSS, mọi thứ
   - Import ảnh như module: `import logo from './logo.png'`
   - Optimize images, fonts tự động
   - CSS Modules, SASS, Less

5. **Hỗ Trợ Rộng Rãi**: Làm việc với mọi framework
   - React, Vue, Angular, Svelte, vanilla JS
   - Có template cho tất cả

**❌ Điểm Yếu (Weaknesses):**
1. **Dev Server Chậm**: Bundle toàn bộ app khi start
   - Cold start: ~10 giây (bundle hết 1000 files trước)
   - Lần đầu chạy `npm start` → đợi lâu
   - Không phù hợp cho rapid prototyping

2. **Config Phức Tạp**: webpack.config.js có thể 500+ dòng
   - Loaders, plugins, optimization rules
   - Khó học cho beginners
   - Dễ config sai → bugs khó debug

3. **HMR Chậm**: Re-bundle lại khi thay đổi code
   - Mỗi lần sửa code: 1-2 giây để cập nhật
   - So với Vite (50ms) → cảm giác lag
   - Developer experience không tốt

4. **Bundle Size Lớn**: Nhiều runtime code thừa
   - Webpack runtime + module system
   - File output lớn hơn Rollup ~20-30%
   - Page load chậm hơn

**📌 Khi Nào Dùng Webpack:**
- ✅ **App lớn của doanh nghiệp** (legacy codebases có sẵn)
   - Đã dùng Webpack, không muốn migrate
   - App phức tạp với nhiều requirements đặc biệt
   
- ✅ **Build phức tạp**: Cần config chi tiết
   - Multi-page apps (MPA)
   - Custom loaders, plugins đặc biệt
   - Khi Vite/Rollup không đáp ứng được

- ✅ **Cần plugin cụ thể**: Plugin chỉ có trên Webpack
   - Module Federation (micro-frontends)
   - Specialized loaders

- ✅ **Migration từ dự án cũ**: Đang dùng Webpack rồi
   - Chi phí migrate cao
   - "If it ain't broken, don't fix it"

**🔧 Ví Dụ Config (Webpack Configuration):**

```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
  mode: 'production', // Chế độ: 'development' hoặc 'production'
  entry: './src/index.tsx', // File đầu vào (entry point)
  
  output: {
    path: path.resolve(__dirname, 'dist'), // Thư mục output
    filename: '[name].[contenthash].js', // Tên file output với hash (cache busting)
    clean: true, // Xóa thư mục dist cũ trước khi build
  },
  
  // LOADERS - Xử lý các loại file khác nhau
  module: {
    rules: [
      // Rule 1: Xử lý TypeScript/TSX
      {
        test: /\.(ts|tsx)$/, // Regex: file nào match .ts hoặc .tsx
        use: 'babel-loader', // Dùng babel-loader để transpile
        exclude: /node_modules/, // Bỏ qua node_modules (không cần transpile)
      },
      // Rule 2: Xử lý CSS
      {
        test: /\.css$/, // File .css
        use: [MiniCssExtractPlugin.loader, 'css-loader'], // Extract CSS ra file riêng
        // Chạy từ phải → trái: css-loader → MiniCssExtractPlugin.loader
      },
      // Rule 3: Xử lý Images
      {
        test: /\.(png|svg|jpg|jpeg|gif)$/i, // File ảnh
        type: 'asset/resource', // Copy ảnh vào dist, return URL
      },
    ],
  },
  
  // PLUGINS - Mở rộng chức năng Webpack
  plugins: [
    // Plugin 1: Tạo HTML file tự động
    new HtmlWebpackPlugin({
      template: './public/index.html', // Template HTML
      // Tự động inject <script> tag vào HTML
    }),
    // Plugin 2: Extract CSS ra file riêng
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css', // Tên file CSS với hash
    }),
  ],
  
  // OPTIMIZATION - Tối ưu hóa bundle
  optimization: {
    splitChunks: {
      chunks: 'all', // Chia nhỏ tất cả chunks
      cacheGroups: {
        // Tạo vendor bundle riêng cho node_modules
        vendor: {
          test: /[\\/]node_modules[\\/]/, // Match node_modules
          name: 'vendors', // Tên chunk: vendors.js
          priority: 10, // Ưu tiên cao hơn (chạy trước)
        },
        // Result: app.js (code của bạn) + vendors.js (node_modules)
      },
    },
  },
  
  // RESOLVE - Cấu hình cách resolve modules
  resolve: {
    extensions: ['.tsx', '.ts', '.js'], // Auto-resolve các extension này
    // import './App' → tự tìm App.tsx, App.ts, App.js
  },
};
```

**⏱️ Hiệu Suất Thực Tế (Performance):**
```
Dev Server Start:  ~10 giây (cold start - lần đầu chạy)
                   - Bundle toàn bộ app trước
                   - Parse 1000+ files
                   - Transform với Babel
                   
HMR:               ~1-2 giây (sau khi sửa code)
                   - Re-bundle phần thay đổi
                   - Inject vào browser
                   
Production Build:  ~10-30 giây (tuỳ kích thước app)
                   - Minify, optimize, tree-shake
                   - Generate source maps
```

---

#### **🔹 B. Rollup - "Chuyên Gia Dọn Rác Code"**

**💡 Tổng Quan:**
- Bundler chuyên về ESM (ES Modules) - ưu tiên module hiện đại
- Tree-shaking tốt nhất (loại bỏ code không dùng hiệu quả nhất)
- Lý tưởng cho libraries (React components, npm packages)
- Config đơn giản, tập trung vào mục đích

**✅ Điểm Mạnh (Strengths):**
1. **Tree-Shaking Tốt Nhất**: Loại bỏ code thừa cực kỳ hiệu quả
   - Phân tích static imports/exports
   - Chỉ giữ lại code thực sự được dùng
   - Bundle size nhỏ hơn Webpack 20-30%
   - Example: Import 1 function từ lodash → chỉ bundle function đó (không cả lib)

2. **Bundle Nhỏ Gọn**: Ít runtime code thừa
   - Không có Webpack runtime overhead
   - Output code gần như vanilla JS
   - Perfect cho performance-critical apps

3. **ESM Native**: Sinh ra để làm việc với ES Modules
   - `import/export` syntax
   - Không cần transform CJS → ESM
   - Future-proof (ESM là tương lai)

4. **Config Đơn Giản**: Dễ hiểu, dễ maintain
   - Ít options hơn Webpack
   - Focused on core features
   - Beginners-friendly

5. **Multiple Output Formats**: Xuất ra nhiều định dạng
   - CJS (CommonJS) - cho Node.js
   - ESM (ES Modules) - cho browsers hiện đại
   - UMD (Universal Module Definition) - cho cả browser & Node
   - IIFE (Immediately Invoked Function Expression) - cho <script> tag
   - → Perfect cho library authors

**❌ Điểm Yếu (Weaknesses):**
1. **Dev Server Chậm**: Không thiết kế cho app development
   - Không có dev server nhanh như Vite
   - Phải bundle lại toàn bộ mỗi lần thay đổi
   - Không phù hợp cho large apps

2. **HMR Hạn Chế**: Cần thêm plugins
   - Không có HMR built-in
   - Phải cài `rollup-plugin-hot` hoặc dùng với Vite
   - DX không tốt như Webpack/Vite

3. **Ecosystem Nhỏ Hơn**: Ít plugins hơn Webpack
   - ~200 plugins (vs Webpack ~5000)
   - Một số use cases không có plugin ready
   - Phải tự viết hoặc workaround

4. **Xử Lý Assets Kém**: Không mạnh như Webpack
   - Images, fonts, CSS không smooth
   - Cần nhiều plugins để xử lý assets
   - Webpack vẫn tốt hơn cho asset-heavy apps

**📌 Khi Nào Dùng Rollup:**
- ✅ **Phát triển Library** (React components, npm packages)
   - Lodash, React, Vue đều dùng Rollup
   - Cần output nhỏ gọn
   - Export nhiều formats (CJS, ESM, UMD)
   
- ✅ **App nhỏ đến trung bình**
   - Không cần dev server nhanh
   - Ưu tiên bundle size nhỏ
   
- ✅ **Bundle size là critical**
   - Performance-sensitive apps
   - Mobile-first apps
   - Muốn tối ưu load time

- ✅ **Publish npm package**
   - Cần tree-shakeable output
   - Support nhiều môi trường (Node, Browser)

**🔧 Ví Dụ Config (Rollup Configuration):**

```javascript
// rollup.config.js
import { defineConfig } from 'rollup';
import typescript from '@rollup/plugin-typescript';
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';

export default defineConfig({
  input: 'src/index.ts', // File đầu vào
  
  // OUTPUT - Xuất ra nhiều formats
  output: [
    // Format 1: CommonJS - cho Node.js
    {
      file: 'dist/bundle.cjs.js', // File output
      format: 'cjs', // CommonJS: require/module.exports
      sourcemap: true, // Tạo source map cho debugging
    },
    // Format 2: ESM - cho browsers hiện đại
    {
      file: 'dist/bundle.esm.js',
      format: 'esm', // ES Modules: import/export
      sourcemap: true,
    },
    // Format 3: UMD - universal (browser + Node)
    {
      file: 'dist/bundle.umd.js',
      format: 'umd', // UMD: chạy mọi nơi
      name: 'MyLibrary', // Tên global variable trong browser
      sourcemap: true,
      // Usage: <script src="bundle.umd.js"></script>
      //        window.MyLibrary.someFunction()
    },
  ],
  
  // PLUGINS - Mở rộng chức năng
  plugins: [
    resolve(), // Resolve node_modules
               // Tìm dependencies trong node_modules
               
    commonjs(), // Convert CJS → ESM
                // Vì Rollup chỉ hiểu ESM, phải convert CJS packages
                
    typescript({ // Compile TypeScript
      tsconfig: './tsconfig.json',
      // Transpile .ts/.tsx → .js
    }),
    
    terser(), // Minify code
              // Nén code: xóa whitespace, rename variables
              // bundle.js (100KB) → bundle.min.js (30KB)
  ],
  
  // EXTERNAL - Không bundle dependencies này
  external: ['react', 'react-dom'], // Peer dependencies
  // Lý do: Library sẽ dùng React của app consumer
  // Không nên bundle React vào library → tăng size, conflict version
});
```

**⏱️ Hiệu Suất Thực Tế (Performance):**
```
Production Build:  ~5 giây
                   - Nhanh hơn Webpack (~10-30s)
                   - Tree-shake hiệu quả
                   
Bundle Size:       -30% nhỏ hơn Webpack
                   - Ít runtime code
                   - Tree-shaking tốt hơn
                   
Example:
  Webpack: 150KB (minified)
  Rollup:  105KB (minified) ← Nhỏ hơn 30%
```

---

#### **🔹 C. Vite - Modern, Lightning Fast**

**💡 Overview:**
- Modern dev server (ESM-based)
- Instant server start
- Lightning-fast HMR
- Rollup for production

**✅ Strengths:**
1. **Instant Dev Server**: No bundling, serve ES modules directly
2. **Fast HMR**: <50ms updates
3. **Simple Config**: Minimal setup
4. **Modern Stack**: Built for modern browsers
5. **Great DX**: Out-of-the-box TypeScript, JSX, CSS

**❌ Weaknesses:**
1. **Modern Browsers Only**: Requires ESM support
2. **Smaller Ecosystem**: Newer than Webpack
3. **Production != Dev**: Uses Rollup for prod
4. **Large Projects**: Can slow down with 1000+ modules

**📌 Use Cases:**
- **Modern web apps** (React, Vue, Svelte)
- New projects (greenfield)
- Fast prototyping
- When DX is priority

**🔧 Example Config:**

```typescript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';

export default defineConfig({
  plugins: [react()],
  
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
    },
  },
  
  build: {
    outDir: 'dist',
    sourcemap: true,
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
        },
      },
    },
  },
  
  server: {
    port: 3000,
    open: true,
  },
});
```

**⏱️ Performance:**
```
Dev Server Start:  ~500ms ⚡ (instant!)
HMR:               ~50ms ⚡
Production Build:  ~2-5 seconds (Rollup)
```

**🔥 Why Vite is Fast:**

```typescript
// TRADITIONAL BUNDLER (Webpack)
┌────────────────────────────────────────┐
│ 1. Bundle ALL code                     │
│    ├─ node_modules (5MB)               │
│    ├─ src (1MB)                        │
│    └─ Transform, minify, bundle        │
│    ↓ 10 seconds                        │
│ 2. Start dev server                    │
│ 3. Serve bundle                        │
└────────────────────────────────────────┘

// VITE (ESM-based)
┌────────────────────────────────────────┐
│ 1. Start dev server IMMEDIATELY ⚡      │
│    ↓ 500ms                             │
│ 2. Browser requests /src/App.tsx       │
│ 3. Transform ONLY requested file       │
│    ↓ 50ms                              │
│ 4. Serve ESM module                    │
│                                        │
│ ✅ Pre-bundle node_modules (esbuild)   │
│ ✅ Transform on-demand (lazy)          │
│ ✅ Native ESM (no bundling in dev)     │
└────────────────────────────────────────┘
```

---

#### **🔹 D. esbuild - Extreme Speed (Go-based)**

**💡 Overview:**
- Written in Go (100x faster than JS)
- Extreme build speed
- Limited plugin ecosystem
- Used internally by Vite

**✅ Strengths:**
1. **Blazing Fast**: 10-100x faster than Webpack
2. **Built-in**: TS, JSX, CSS, minification
3. **Simple API**: Easy to use
4. **Parallel Processing**: Multi-threaded

**❌ Weaknesses:**
1. **Limited Plugins**: Small ecosystem
2. **No HMR**: Not designed for dev server
3. **Basic Features**: Less advanced than Webpack
4. **Go Required**: For plugin development

**📌 Use Cases:**
- **Build step in Vite/Turbopack**
- Minification tool
- Transpiling TypeScript
- CI/CD builds (speed critical)

**🔧 Example:**

```typescript
// esbuild.config.js
const esbuild = require('esbuild');

esbuild.build({
  entryPoints: ['src/index.tsx'],
  bundle: true,
  outfile: 'dist/bundle.js',
  minify: true,
  sourcemap: true,
  target: ['es2020'],
  loader: {
    '.ts': 'ts',
    '.tsx': 'tsx',
  },
  external: ['react', 'react-dom'],
}).catch(() => process.exit(1));
```

**⏱️ Performance:**
```
Production Build:  ~500ms ⚡⚡⚡ (10x faster than Webpack!)
Bundle Size:       Similar to Rollup
```

---

#### **🔹 E. Turbopack - Next.js Native (Rust-based)**

**💡 Overview:**
- Rust-based bundler
- Built by Vercel for Next.js
- Incremental computation
- Replaces Webpack in Next.js

**✅ Strengths:**
1. **Extreme Speed**: Rust-based, 10x faster than Webpack
2. **Incremental**: Caches everything
3. **Next.js Native**: Deep integration
4. **Future-proof**: Modern architecture

**❌ Weaknesses:**
1. **Next.js Only**: Not standalone (yet)
2. **New**: Immature, bugs
3. **Limited Plugins**: Small ecosystem
4. **Rust Required**: For customization

**📌 Use Cases:**
- **Next.js apps** (experimental)
- Large Next.js projects
- When build speed is critical

**🔧 Example:**

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  experimental: {
    turbo: {
      // Enable Turbopack
      loaders: {
        '.svg': ['@svgr/webpack'],
      },
    },
  },
};

module.exports = nextConfig;
```

**⏱️ Performance:**
```
Dev Server (Next.js):
- Webpack:  ~10 seconds
- Turbopack: ~1 second ⚡⚡⚡ (10x faster!)

HMR:
- Webpack:  ~1-2 seconds
- Turbopack: ~50ms ⚡⚡⚡
```

---

#### **2️⃣ TRANSPILERS COMPARISON**

**📊 Babel vs SWC:**

| Feature | **Babel** | **SWC** |
|---------|-----------|---------|
| **Speed** | ⭐⭐ Baseline | ⭐⭐⭐⭐⭐ 20x faster |
| **Language** | JavaScript | Rust |
| **Plugin Ecosystem** | ⭐⭐⭐⭐⭐ Huge | ⭐⭐⭐ Growing |
| **Compatibility** | ⭐⭐⭐⭐⭐ Best | ⭐⭐⭐⭐ Good |
| **Preset Support** | ⭐⭐⭐⭐⭐ Many | ⭐⭐⭐ Basic |
| **Maturity** | ⭐⭐⭐⭐⭐ 10y | ⭐⭐⭐ 4y |
| **Minification** | ❌ No | ✅ Yes |
| **TypeScript** | ✅ Via preset | ✅ Built-in |

---

#### **🔹 A. Babel - The Standard**

**✅ Strengths:**
1. **Plugin Ecosystem**: 1000+ plugins
2. **Presets**: @babel/preset-env, @babel/preset-react, etc.
3. **Compatibility**: Support old browsers (IE11)
4. **Customization**: Fine-grained control
5. **Stable**: Production-proven

**❌ Weaknesses:**
1. **Slow**: JavaScript-based (single-threaded)
2. **Complex Config**: Many presets/plugins
3. **Large**: Increases build time significantly

**🔧 Example:**

```javascript
// babel.config.js
module.exports = {
  presets: [
    ['@babel/preset-env', {
      targets: '> 0.25%, not dead',
      useBuiltIns: 'usage',
      corejs: 3,
    }],
    '@babel/preset-react',
    '@babel/preset-typescript',
  ],
  plugins: [
    '@babel/plugin-proposal-class-properties',
    '@babel/plugin-proposal-optional-chaining',
  ],
};
```

---

#### **🔹 B. SWC - The Speed Demon**

**✅ Strengths:**
1. **20x Faster**: Rust-based, parallel processing
2. **Built-in Minification**: No need for Terser
3. **TypeScript Native**: No extra config
4. **Compatible**: Drop-in replacement for Babel
5. **Used by**: Next.js, Vite, Turbopack

**❌ Weaknesses:**
1. **Smaller Ecosystem**: Fewer plugins
2. **Less Mature**: Newer, potential bugs
3. **Limited Presets**: Basic compared to Babel

**🔧 Example:**

```json
// .swcrc
{
  "jsc": {
    "parser": {
      "syntax": "typescript",
      "tsx": true
    },
    "transform": {
      "react": {
        "runtime": "automatic"
      }
    },
    "target": "es2020"
  },
  "module": {
    "type": "es6"
  },
  "minify": true
}
```

**⏱️ Performance:**
```
Transpile 1000 files:
- Babel: ~10 seconds
- SWC:   ~500ms ⚡⚡⚡ (20x faster!)
```

---

#### **3️⃣ Decision Matrix - Khi Nào Dùng Gì?**

```typescript
// =====================================
// BUILD TOOL SELECTION GUIDE
// =====================================

const selectBuildTool = (project: Project): BuildTool => {
  // 1. NEW PROJECT → Vite
  if (project.isNew && project.framework !== 'Next.js') {
    return 'Vite'; // ⚡ Best DX, fast, modern
  }
  
  // 2. NEXT.JS → Turbopack (experimental)
  if (project.framework === 'Next.js') {
    return 'Turbopack'; // 🚀 Native, fastest
  }
  
  // 3. LIBRARY → Rollup
  if (project.type === 'library') {
    return 'Rollup'; // 📦 Best tree-shaking, multiple outputs
  }
  
  // 4. LEGACY/ENTERPRISE → Webpack
  if (project.hasLegacyCode || project.complexRequirements) {
    return 'Webpack'; // 🏗️ Mature, configurable, plugins
  }
  
  // 5. CI/CD BUILD ONLY → esbuild
  if (project.needsSpeed && !project.needsDevServer) {
    return 'esbuild'; // ⚡⚡⚡ Fastest builds
  }
  
  // Default: Vite
  return 'Vite';
};

// TRANSPILER SELECTION
const selectTranspiler = (project: Project): Transpiler => {
  // 1. SPEED CRITICAL → SWC
  if (project.prioritizeSpeed) {
    return 'SWC'; // ⚡ 20x faster
  }
  
  // 2. OLD BROWSER SUPPORT → Babel
  if (project.targets.includes('IE11')) {
    return 'Babel'; // 🌐 Best compatibility
  }
  
  // 3. COMPLEX TRANSFORMATIONS → Babel
  if (project.needsCustomPlugins) {
    return 'Babel'; // 🔌 Huge ecosystem
  }
  
  // Default: SWC (modern projects)
  return 'SWC';
};
```

---

#### **4️⃣ Real-World Benchmarks**

**🏁 Build Time Comparison (Same Project):**

```
Project: React app (500 components, 2MB source)

DEV SERVER START:
┌──────────────┬───────────┬──────────────┐
│ Tool         │ Time      │ Comparison   │
├──────────────┼───────────┼──────────────┤
│ Webpack      │ 10s       │ Baseline     │
│ Rollup       │ 8s        │ 1.25x faster │
│ Vite         │ 500ms     │ 20x faster ⚡│
│ esbuild      │ 300ms     │ 33x faster ⚡│
│ Turbopack    │ 1s        │ 10x faster ⚡│
└──────────────┴───────────┴──────────────┘

PRODUCTION BUILD:
┌──────────────┬───────────┬──────────────┐
│ Tool         │ Time      │ Bundle Size  │
├──────────────┼───────────┼──────────────┤
│ Webpack      │ 30s       │ 500KB        │
│ Rollup       │ 15s       │ 450KB ✅      │
│ Vite         │ 10s       │ 460KB        │
│ esbuild      │ 2s ⚡      │ 470KB        │
│ Turbopack    │ 5s        │ 460KB        │
└──────────────┴───────────┴──────────────┘

HMR (Hot Module Replacement):
┌──────────────┬───────────┐
│ Tool         │ Update    │
├──────────────┼───────────┤
│ Webpack      │ 1-2s      │
│ Vite         │ 50ms ⚡    │
│ Turbopack    │ 50ms ⚡    │
└──────────────┴───────────┘
```

---

#### **5️⃣ Migration Guide**

**🔄 Webpack → Vite:**

```typescript
// 1. Install Vite
npm install vite @vitejs/plugin-react

// 2. Create vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  
  // Migrate Webpack aliases
  resolve: {
    alias: {
      '@': '/src',
    },
  },
  
  // Migrate Webpack env vars
  define: {
    'process.env': {},
  },
});

// 3. Update index.html
// Move from public/ to root
// Change <script src="/src/index.tsx" type="module">

// 4. Update package.json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}

// 5. Replace Webpack-specific code
// - require() → import
// - require.context() → import.meta.glob()
// - process.env → import.meta.env
```

**🔄 Babel → SWC:**

```bash
# 1. Install SWC
npm install @swc/core @swc/cli

# 2. Create .swcrc (see example above)

# 3. Update build scripts
# package.json
{
  "scripts": {
    "build": "swc src -d dist"
  }
}

# 4. Update bundler config
# If using Webpack
{
  test: /\.(ts|tsx)$/,
  use: {
    loader: 'swc-loader',
  },
}

# If using Vite (already uses esbuild, but can switch)
# vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc'; // SWC version

export default defineConfig({
  plugins: [react()],
});
```

---

#### **🔥 Best Practices**

**✅ DO:**
1. **Choose based on needs**:
   - New project → Vite
   - Library → Rollup
   - Legacy → Webpack
   - Next.js → Turbopack

2. **Use SWC for transpilation** (unless need Babel plugins)

3. **Enable caching**:
   ```javascript
   // Webpack
   cache: {
     type: 'filesystem',
   }
   
   // Vite (auto-cached)
   ```

4. **Monitor bundle size**:
   ```bash
   npm install -D webpack-bundle-analyzer
   ```

5. **Use source maps in production**:
   ```javascript
   build: {
     sourcemap: true, // Debug production issues
   }
   ```

**❌ DON'T:**
1. **Over-configure**: Keep config simple
2. **Ignore warnings**: Fix deprecations early
3. **Skip optimization**: Enable minification, tree-shaking
4. **Mix tools**: Don't use Webpack + Vite together
5. **Forget to update**: Keep tools updated

---

#### **🎯 Kết Luận**

**Recommendation Matrix:**

| Scenario | Bundler | Transpiler | Reason |
|----------|---------|------------|--------|
| **New React/Vue app** | Vite | SWC | Fast DX, modern |
| **Next.js app** | Turbopack | SWC | Native integration |
| **Library/Package** | Rollup | SWC | Small bundles |
| **Legacy enterprise** | Webpack | Babel | Compatibility |
| **CI/CD builds** | esbuild | SWC | Speed |

**💡 Key Takeaways:**

1. **Vite is the new standard** for modern web apps (React, Vue, Svelte)
2. **Webpack still relevant** for complex/legacy projects
3. **Rollup best for libraries** (tree-shaking, multiple outputs)
4. **esbuild = speed** (use as build step, not full bundler)
5. **Turbopack = future** (Next.js only for now)
6. **SWC replacing Babel** (20x faster, same features)

**🚀 Future Trends:**
- Rust-based tools (SWC, Turbopack) gaining traction
- Native ESM everywhere (no bundling in dev)
- Build tools merging (Vite uses Rollup + esbuild)
- Zero-config becoming standard

---
