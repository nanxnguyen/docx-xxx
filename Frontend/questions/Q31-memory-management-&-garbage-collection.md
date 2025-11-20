# 🧹 Q31: Memory Management & Garbage Collection

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🧹 Q31: Memory Management & Garbage Collection</span></summary>


**Trả lời:**

- **Memory Management**: JavaScript tự động quản lý memory thông qua Garbage Collection
- **Garbage Collection**: Process tự động free memory không còn được sử dụng
- **Mark and Sweep**: Algorithm chính để detect và collect garbage
- **Ưu điểm**: Automatic memory management, developer không cần manual free
- **Nhược điểm**: Có thể gây performance issues, unpredictable timing

**Code Example:**

```typescript
// Memory allocation
function createLargeObject(): object {
  return {
    data: new Array(1000000).fill('large data'),
    timestamp: Date.now(),
  };
}

// Object lifecycle
let largeObject = createLargeObject();
console.log('Object created');

// Object becomes eligible for GC when no references
largeObject = null;
console.log('Object reference removed');

// Garbage Collection triggers
function triggerGC(): void {
  // Force garbage collection (if available)
  if (window.gc) {
    window.gc();
  }
}

// Memory monitoring
function monitorMemory(): void {
  if ('memory' in performance) {
    const memory = (performance as any).memory;
    console.log('Used:', memory.usedJSHeapSize / 1024 / 1024, 'MB');
    console.log('Total:', memory.totalJSHeapSize / 1024 / 1024, 'MB');
    console.log('Limit:', memory.jsHeapSizeLimit / 1024 / 1024, 'MB');
  }
}

// Weak references (don't prevent GC)
const weakMap = new WeakMap();
const weakSet = new WeakSet();

function useWeakReferences(): void {
  const obj = { data: 'important' };

  // These don't prevent garbage collection
  weakMap.set(obj, 'metadata');
  weakSet.add(obj);

  // obj can be garbage collected even with weak references
  // weakMap and weakSet will automatically remove the entries
}

// Memory leaks examples
function createMemoryLeak(): void {
  const elements: HTMLElement[] = [];

  // Memory leak: keeping references to DOM elements
  for (let i = 0; i < 1000; i++) {
    const element = document.createElement('div');
    elements.push(element); // Keeps reference
  }

  // Elements won't be garbage collected
}

// Proper cleanup
function properCleanup(): void {
  const elements: HTMLElement[] = [];

  for (let i = 0; i < 1000; i++) {
    const element = document.createElement('div');
    elements.push(element);
  }

  // Cleanup: remove references
  elements.length = 0;
  // Now elements can be garbage collected
}

// Event listener cleanup
function addEventListenerWithCleanup(): () => void {
  const handler = (event: Event) => {
    console.log('Event:', event);
  };

  document.addEventListener('click', handler);

  // Return cleanup function
  return () => {
    document.removeEventListener('click', handler);
  };
}

const cleanup = addEventListenerWithCleanup();
// Later: cleanup(); // Remove event listener
```

**Best Practices:**

- Sử dụng WeakMap/WeakSet cho temporary references
- Cleanup event listeners
- Remove DOM references khi không cần
- Monitor memory usage
- Sử dụng proper cleanup functions

**Mistakes:**

```typescript
// ❌ Sai: Không cleanup event listeners
document.addEventListener('click', handler);
// Memory leak nếu không removeEventListener

// ✅ Đúng: Cleanup event listeners
const cleanup = () => document.removeEventListener('click', handler);
cleanup(); // Remove listener
```

</details>