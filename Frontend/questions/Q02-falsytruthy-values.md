# 💡 Q2: Falsy/Truthy Values




**⚡ Quick Summary:**
> Falsy: false, 0, '', null, undefined, NaN. Truthy = còn lại

**💡 Ghi Nhớ:**
- ❌ **6 Falsy**: false, 0, '', null, undefined, NaN
- ✅ **Truthy**: Tất cả còn lại ([], {}, '0', 'false'...)
- ⚠️ **Trap**: `[]` và `{}` là truthy!

**Trả lời:**

```typescript
// 8 Falsy Values
console.log(Boolean(false)); // false
console.log(Boolean(0)); // false
console.log(Boolean(-0)); // false
console.log(Boolean(0n)); // false (BigInt)
console.log(Boolean('')); // false (empty string)
console.log(Boolean(null)); // false
console.log(Boolean(undefined)); // false
console.log(Boolean(NaN)); // false

// Truthy Values (tất cả còn lại)
console.log(Boolean([])); // true (empty array)
console.log(Boolean({})); // true (empty object)
console.log(Boolean('0')); // true (string)
console.log(Boolean('false')); // true (string)

// Practical usage
const numbers = [0, 1, 2, 3];
const truthyNumbers = numbers.filter(Boolean); // [1, 2, 3]

function greet(name?: string) {
  return name ? `Hello ${name}` : 'Hello Guest';
}
```

