# 🔀 Q22: Compare Objects




**⚡ Quick Summary:**
> Compare objects: JSON.stringify, lodash isEqual, hoặc custom recursive compare

**💡 Ghi Nhớ:**
- 🎯 **Shallow**: `JSON.stringify()` - fast nhưng limited
- 🔍 **Deep**: Lodash `isEqual()` - handle circular refs
- ⚠️ **Trap**: `{a:1} === {a:1}` = false (khác reference)

**Trả lời:**

- **Shallow Comparison**: So sánh references và primitive values
- **Deep Comparison**: So sánh tất cả nested properties
- **Hoạt động**: Objects được so sánh bằng reference, không phải value
- **Ưu điểm**: Deep comparison chính xác, shallow comparison nhanh
- **Nhược điểm**: Deep comparison chậm, shallow comparison không chính xác

**Code Example:**

```typescript
// Shallow comparison
const obj1 = { name: 'John', age: 25 };
const obj2 = { name: 'John', age: 25 };
const obj3 = obj1;

console.log(obj1 === obj2); // false (different references)
console.log(obj1 === obj3); // true (same reference)

// Deep comparison function
function deepEqual(obj1: any, obj2: any): boolean {
  if (obj1 === obj2) return true;

  if (obj1 == null || obj2 == null) return false;

  if (typeof obj1 !== typeof obj2) return false;

  if (typeof obj1 !== 'object') return obj1 === obj2;

  if (Array.isArray(obj1) !== Array.isArray(obj2)) return false;

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) return false;

  for (let key of keys1) {
    if (!keys2.includes(key)) return false;
    if (!deepEqual(obj1[key], obj2[key])) return false;
  }

  return true;
}

// Usage
const obj1 = { name: 'John', age: 25, address: { city: 'HCM' } };
const obj2 = { name: 'John', age: 25, address: { city: 'HCM' } };

console.log(deepEqual(obj1, obj2)); // true
```

**Best Practices:**

- Sử dụng deep comparison cho object comparison
- Sử dụng shallow comparison cho performance
- Sử dụng libraries như Lodash cho complex comparisons
- Sử dụng TypeScript cho type safety

