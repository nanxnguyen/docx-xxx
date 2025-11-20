# 🚨 Q32: Memory Leaks Detection & Prevention

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🚨 Q32: Memory Leaks Detection & Prevention</span></summary>


**Trả lời:**

- **Memory Leaks**: Memory được allocate nhưng không được free
- **Common Causes**: Event listeners, DOM references, closures, timers
- **Detection**: Browser DevTools, memory profiling
- **Prevention**: Proper cleanup, weak references, monitoring
- **Ưu điểm**: Better performance, stable applications
- **Nhược điểm**: Cần careful coding, monitoring overhead

**Code Example:**

```typescript
// Common memory leak patterns

// 1. Event listeners không được cleanup
class Component {
  private element: HTMLElement;

  constructor() {
    this.element = document.createElement('div');
    // Memory leak: không cleanup event listener
    this.element.addEventListener('click', this.handleClick.bind(this));
  }

  private handleClick(): void {
    console.log('Clicked');
  }

  // Fix: Add cleanup method
  destroy(): void {
    this.element.removeEventListener('click', this.handleClick.bind(this));
    this.element.remove();
  }
}

// 2. DOM references
function createMemoryLeak(): void {
  const elements: HTMLElement[] = [];

  for (let i = 0; i < 1000; i++) {
    const element = document.createElement('div');
    elements.push(element); // Keeps reference
  }

  // Fix: Clear references
  elements.length = 0;
}

// 3. Closures giữ references
function createClosureLeak(): void {
  const largeData = new Array(1000000).fill('data');

  return function () {
    // Closure giữ reference đến largeData
    console.log('Closure executed');
  };
}

// Fix: Clear references
function createProperClosure(): () => void {
  const largeData = new Array(1000000).fill('data');

  return function () {
    console.log('Closure executed');
    // Clear reference when done
    largeData.length = 0;
  };
}

// 4. Timers không được clear
function createTimerLeak(): void {
  const interval = setInterval(() => {
    console.log('Timer tick');
  }, 1000);

  // Memory leak: không clear interval
}

// Fix: Clear timers
function createProperTimer(): () => void {
  const interval = setInterval(() => {
    console.log('Timer tick');
  }, 1000);

  return () => clearInterval(interval);
}

// Memory leak detection
class MemoryLeakDetector {
  private static instances: Set<object> = new Set();

  static track(obj: object): void {
    this.instances.add(obj);
  }

  static untrack(obj: object): void {
    this.instances.delete(obj);
  }

  static getInstanceCount(): number {
    return this.instances.size;
  }
}

// Usage
class TrackedComponent {
  constructor() {
    MemoryLeakDetector.track(this);
  }

  destroy(): void {
    MemoryLeakDetector.untrack(this);
  }
}

// Memory profiling
function profileMemory(): void {
  if ('memory' in performance) {
    const memory = (performance as any).memory;
    const used = memory.usedJSHeapSize / 1024 / 1024;
    const total = memory.totalJSHeapSize / 1024 / 1024;

    console.log(`Memory usage: ${used.toFixed(2)}MB / ${total.toFixed(2)}MB`);

    // Alert if memory usage is high
    if (used > 100) {
      console.warn('High memory usage detected!');
    }
  }
}

// Weak references để tránh memory leaks
class WeakReferenceManager {
  private weakMap = new WeakMap<object, any>();

  setReference(obj: object, data: any): void {
    this.weakMap.set(obj, data);
  }

  getReference(obj: object): any {
    return this.weakMap.get(obj);
  }

  // No need to cleanup - WeakMap automatically removes entries
}

// Proper cleanup pattern
class ResourceManager {
  private resources: Set<() => void> = new Set();

  addResource(cleanup: () => void): void {
    this.resources.add(cleanup);
  }

  cleanup(): void {
    this.resources.forEach((cleanup) => cleanup());
    this.resources.clear();
  }
}

// Usage
const manager = new ResourceManager();

// Add event listener
const cleanup1 = addEventListenerWithCleanup();
manager.addResource(cleanup1);

// Add timer
const cleanup2 = createProperTimer();
manager.addResource(cleanup2);

// Later: manager.cleanup(); // Cleanup all resources
```

**Best Practices:**

- Sử dụng WeakMap/WeakSet cho temporary references
- Cleanup event listeners và timers
- Remove DOM references
- Sử dụng resource managers
- Monitor memory usage
- Sử dụng proper cleanup patterns

**Mistakes:**

```typescript
// ❌ Sai: Không cleanup resources
const interval = setInterval(() => {}, 1000);
// Memory leak

// ✅ Đúng: Cleanup resources
const interval = setInterval(() => {}, 1000);
clearInterval(interval); // Cleanup
```

</details>