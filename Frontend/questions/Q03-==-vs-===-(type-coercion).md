# 🔍 Q3: == vs === (Type Coercion)




**⚡ Quick Summary:**
> `==` coerce types, `===` không coerce. Luôn dùng `===`

**💡 Ghi Nhớ:**
- 🎯 **===**: Strict equality - không convert type
- ⚠️ **==**: Loose equality - convert type trước khi so sánh
- 📌 **Rule**: Luôn dùng `===` trừ khi check `== null`

**Trả lời:**

```typescript
// == vs === Examples
console.log(5 == '5'); // true (type coercion)
console.log(5 === '5'); // false (no type coercion)

console.log(0 == false); // true
console.log(0 === false); // false

console.log(null == undefined); // true (special case)
console.log(null === undefined); // false

// Best practice: Dùng === mặc định
if (user.age === 25) { /* Rõ ràng */ }

// Exception: Check cả null và undefined
if (value == null) { /* Check both null and undefined */ }
```

