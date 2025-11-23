# 🪞 Q21: JavaScript Proxy




**⚡ Quick Summary:**
> Proxy = intercept object operations (get, set, delete...). Reflect = default behaviors

**💡 Ghi Nhớ:**
- 🎭 **Proxy**: Wrap object, intercept mọi operation
- 🔍 **Use Cases**: Validation, logging, reactive data (Vue 3)
- ⚡ **Traps**: get, set, has, deleteProperty, apply, construct...

**Trả lời:**

- **Proxy**: Object để intercept và customize operations
- **Hoạt động**: Wrap target object và intercept property access
- **Ưu điểm**: Powerful metaprogramming, validation, logging
- **Nhược điểm**: Performance overhead, complexity

**Code Example:**

```typescript
// Basic proxy
const target = { name: 'John', age: 25 };
const proxy = new Proxy(target, {
  get(target, property) {
    console.log(`Getting ${String(property)}`);
    return target[property as keyof typeof target];
  },
  set(target, property, value) {
    console.log(`Setting ${String(property)} to ${value}`);
    target[property as keyof typeof target] = value;
    return true;
  },
});

console.log(proxy.name); // Getting name, John
proxy.age = 26; // Setting age to 26

// Validation proxy
const userProxy = new Proxy(
  {},
  {
    set(target, property, value) {
      if (property === 'age' && (typeof value !== 'number' || value < 0)) {
        throw new Error('Age must be a positive number');
      }
      if (property === 'name' && typeof value !== 'string') {
        throw new Error('Name must be a string');
      }
      target[property as keyof typeof target] = value;
      return true;
    },
  }
);

userProxy.name = 'John'; // OK
userProxy.age = 25; // OK
// userProxy.age = -5; // Error: Age must be a positive number

// Logging proxy
const loggingProxy = new Proxy(
  {},
  {
    get(target, property) {
      console.log(`Accessing property: ${String(property)}`);
      return target[property as keyof typeof target];
    },
    set(target, property, value) {
      console.log(`Setting property: ${String(property)} = ${value}`);
      target[property as keyof typeof target] = value;
      return true;
    },
  }
);
```

**Best Practices:**

- Sử dụng proxy cho validation
- Sử dụng proxy cho logging
- Sử dụng proxy cho metaprogramming
- Sử dụng proper error handling

