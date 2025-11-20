# 🔗 Q5: || && ?? và Optional Chaining




**⚡ Quick Summary:**
> `||` = OR, `&&` = AND, `??` = nullish coalescing (chỉ null/undefined). `?.` = optional chaining

**💡 Ghi Nhớ:**
- 🎯 **??**: Chỉ check null/undefined (khác || check falsy)
- 🔗 **?.**: Safe navigation - `obj?.prop?.method?.()`
- ⚠️ **Trap**: `0 ?? 1` = 0, nhưng `0 || 1` = 1

**Trả lời:**

```typescript
// || vs ?? (KHÁC BIỆT)
const age1 = 0 || 18; // 18 (0 is falsy)
const age2 = 0 ?? 18; // 0 (0 is not nullish)

const name1 = '' || 'Guest'; // 'Guest' ('' is falsy)
const name2 = '' ?? 'Guest'; // '' ('' is not nullish)

// Optional chaining
const city = user?.address?.city; // Safe navigation
const result = user?.getName?.(); // Safe method call
const item = items?.[0]; // Safe array access

// Best practices
const theme = settings?.theme ?? 'light'; // Dùng ?? cho default
const count = items?.length ?? 0; // Safe với nullish coalescing
const hasEmail = user?.contact?.email && true; // && cho conditional
```

