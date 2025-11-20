# 🧩 Q4: null vs undefined




**⚡ Quick Summary:**
> `null` = intentionally empty. `undefined` = chưa được gán giá trị

**💡 Ghi Nhớ:**
- 🎯 **null**: Lập trình viên set = empty có chủ đích
- ❓ **undefined**: Biến chưa được gán, hoặc function không return
- ⚡ **Check**: `value == null` check cả null và undefined

**Trả lời:**

```typescript
// null - intentional absence
let user: User | null = null; // Explicitly empty
function findUser(id: number): User | null {
  return null; // User not found
}

// undefined - unintentional absence
let age: number; // undefined (uninitialized)
function getProperty(obj: any, key: string) {
  return obj[key]; // undefined if key doesn't exist
}

console.log(typeof null); // "object" (historical bug)
console.log(typeof undefined); // "undefined"

// Nullish coalescing
const name = user?.name ?? 'Guest'; // Only null/undefined → 'Guest'
const theme = settings?.theme ?? 'light';
```

