# 📥 Q33: Dynamic Import & Module System

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">📥 Q33: Dynamic Import & Module System</span></summary>


**Trả lời:**

- **Dynamic Import**: Import modules at runtime thay vì compile time
- **Module System**: ES6 modules, CommonJS, AMD
- **Hoạt động**: Dynamic import trả về Promise, cho phép lazy loading
- **Ưu điểm**: Code splitting, lazy loading, better performance
- **Nhược điểm**: Complexity, async handling required

**Code Example:**

```typescript
// Static import (compile time)
import { utils } from './utils';
import React from 'react';

// Dynamic import (runtime)
async function loadModule(): Promise<void> {
  try {
    // Dynamic import trả về Promise
    const module = await import('./heavy-module');
    const result = module.default();
    console.log('Module loaded:', result);
  } catch (error) {
    console.error('Failed to load module:', error);
  }
}

// Conditional loading
async function loadModuleConditionally(condition: boolean): Promise<void> {
  if (condition) {
    const { heavyFunction } = await import('./heavy-module');
    heavyFunction();
  }
}

// Lazy loading components
async function loadComponent(): Promise<React.ComponentType> {
  const module = await import('./LazyComponent');
  return module.default;
}

// Code splitting với dynamic import
function createRouteLoader(routeName: string) {
  return async () => {
    switch (routeName) {
      case 'home':
        return await import('./routes/Home');
      case 'about':
        return await import('./routes/About');
      case 'contact':
        return await import('./routes/Contact');
      default:
        throw new Error(`Unknown route: ${routeName}`);
    }
  };
}

// Usage
const homeLoader = createRouteLoader('home');
const HomeComponent = await homeLoader();

// Dynamic import với error handling
async function safeImport(modulePath: string): Promise<any> {
  try {
    const module = await import(modulePath);
    return module;
  } catch (error) {
    console.error(`Failed to import ${modulePath}:`, error);
    return null;
  }
}

// Lazy loading với React
const LazyComponent = React.lazy(() => import('./LazyComponent'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <LazyComponent />
    </Suspense>
  );
}

// Module system comparison
// ES6 Modules
export const name = 'John';
export default function greet() {}

// CommonJS
module.exports = {
  name: 'John',
  greet: function () {},
};

// AMD
define(['dependency'], function (dependency) {
  return {
    name: 'John',
    greet: function () {},
  };
});

// Dynamic import với multiple modules
async function loadMultipleModules(): Promise<void> {
  const [module1, module2, module3] = await Promise.all([
    import('./module1'),
    import('./module2'),
    import('./module3'),
  ]);

  console.log('All modules loaded');
}

// Khi nào nên dùng dynamic import
function shouldUseDynamicImport(): boolean {
  // 1. Large modules không cần ngay
  // 2. Conditional loading
  // 3. Code splitting
  // 4. Lazy loading
  return true;
}
```

**Best Practices:**

- Sử dụng dynamic import cho large modules
- Sử dụng cho conditional loading
- Sử dụng cho code splitting
- Sử dụng proper error handling
- Sử dụng với React.lazy cho components

**Mistakes:**

```typescript
// ❌ Sai: Không handle errors
const module = await import('./module');
// Có thể throw error

// ✅ Đúng: Handle errors
try {
  const module = await import('./module');
} catch (error) {
  console.error('Import failed:', error);
}
```

</details>