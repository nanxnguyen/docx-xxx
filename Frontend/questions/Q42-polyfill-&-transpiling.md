# 🔧 Q42: Polyfill & Transpiling

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🔧 Q42: Polyfill & Transpiling</span></summary>


**⚡ Quick Summary:**
> Polyfill = code thay thế feature chưa hỗ trợ. Transpiling = convert modern → old JS (Babel)

**💡 Ghi Nhớ:**
- 🔧 **Polyfill**: Add missing features (Array.includes, Promise...)
- 🔄 **Transpile**: ES6+ → ES5 (Babel, TypeScript)
- 📦 **Bundle**: core-js, @babel/polyfill

**Trả lời:**

- **Polyfill**: Code cung cấp functionality cho older browsers không support feature mới
- **Transpiling**: Convert code từ syntax này sang syntax khác (ES6+ → ES5)
- **Hoạt động**: Polyfill thêm methods/APIs, Transpiling convert syntax
- **Ưu điểm**: Browser compatibility, modern development
- **Nhược điểm**: Bundle size tăng, complexity

**Code Example:**

```typescript
// Polyfill cho Array.includes (ES2016)
if (!Array.prototype.includes) {
  Array.prototype.includes = function (
    searchElement: any,
    fromIndex?: number
  ): boolean {
    const O = Object(this);
    const len = parseInt(O.length) || 0;
    if (len === 0) return false;

    const n = parseInt(fromIndex) || 0;
    let k = n >= 0 ? n : Math.max(len + n, 0);

    while (k < len) {
      if (O[k] === searchElement) return true;
      k++;
    }
    return false;
  };
}

// Polyfill cho Promise (ES2015)
if (!window.Promise) {
  window.Promise = class Promise {
    private state: 'pending' | 'fulfilled' | 'rejected' = 'pending';
    private value: any;
    private reason: any;
    private onFulfilledCallbacks: Function[] = [];
    private onRejectedCallbacks: Function[] = [];

    constructor(executor: (resolve: Function, reject: Function) => void) {
      const resolve = (value: any) => {
        if (this.state === 'pending') {
          this.state = 'fulfilled';
          this.value = value;
          this.onFulfilledCallbacks.forEach((callback) => callback(value));
        }
      };

      const reject = (reason: any) => {
        if (this.state === 'pending') {
          this.state = 'rejected';
          this.reason = reason;
          this.onRejectedCallbacks.forEach((callback) => callback(reason));
        }
      };

      try {
        executor(resolve, reject);
      } catch (error) {
        reject(error);
      }
    }

    then(onFulfilled?: Function, onRejected?: Function): Promise {
      return new Promise((resolve, reject) => {
        if (this.state === 'fulfilled') {
          try {
            const result = onFulfilled ? onFulfilled(this.value) : this.value;
            resolve(result);
          } catch (error) {
            reject(error);
          }
        } else if (this.state === 'rejected') {
          try {
            const result = onRejected ? onRejected(this.reason) : this.reason;
            resolve(result);
          } catch (error) {
            reject(error);
          }
        } else {
          this.onFulfilledCallbacks.push(
            onFulfilled || ((value: any) => resolve(value))
          );
          this.onRejectedCallbacks.push(
            onRejected || ((reason: any) => reject(reason))
          );
        }
      });
    }
  };
}

// Transpiling: ES6+ → ES5
// ES6+ Code
const greet = (name: string): string => `Hello ${name}`;
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers.map((n) => n * 2);

// Transpiled ES5 Code
var greet = function (name) {
  return 'Hello ' + name;
};
var numbers = [1, 2, 3, 4, 5];
var doubled = numbers.map(function (n) {
  return n * 2;
});

// Khi nào cần viết polyfill
function needsPolyfill(): boolean {
  // Check if feature exists
  if (!Array.prototype.includes) {
    console.log('Array.includes needs polyfill');
    return true;
  }

  if (!window.fetch) {
    console.log('Fetch API needs polyfill');
    return true;
  }

  if (!Object.assign) {
    console.log('Object.assign needs polyfill');
    return true;
  }

  return false;
}
```

**Best Practices:**

- Sử dụng polyfill cho missing APIs
- Sử dụng Babel cho transpiling
- Sử dụng core-js cho comprehensive polyfills
- Sử dụng feature detection

**Mistakes:**

```typescript
// ❌ Sai: Không check feature support
const result = [1, 2, 3].includes(2); // Error in IE

// ✅ Đúng: Check feature support
if (Array.prototype.includes) {
  const result = [1, 2, 3].includes(2);
} else {
  // Use alternative or polyfill
  const result = [1, 2, 3].indexOf(2) !== -1;
}
```

</details>