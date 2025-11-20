# 📦 Q7: Deep Copy vs Shallow Copy

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">📦 Q7: Deep Copy vs Shallow Copy</span></summary>


**⚡ Quick Summary:**
> **Shallow Copy** = Copy level đầu tiên, nested object vẫn share reference  
> **Deep Copy** = Copy toàn bộ, nested object cũng được copy

**💡 Ghi Nhớ:**
- 📝 **Shallow**: `{...obj}`, `[...arr]`, `Object.assign()` - chỉ copy 1 tầng
- 🔍 **Deep**: `JSON.parse(JSON.stringify())`, `structuredClone()`, libraries
- ⚠️ **Trap**: Shallow copy nested object → vẫn share reference!

**Trả lời:**

- **Shallow Copy**: Copy cấp đầu tiên, nested objects vẫn share reference
- **Deep Copy**: Copy toàn bộ, tạo ra object hoàn toàn mới
- **Ưu điểm**: Deep copy an toàn hơn, shallow copy nhanh hơn
- **Nhược điểm**: Deep copy tốn memory và thời gian hơn

**Code Example:**

```typescript
// Shallow Copy - chỉ copy cấp đầu
let original: { name: string; address: { city: string } } = {
  name: 'Nguyen Van A',
  address: { city: 'Ho Chi Minh' },
};

// Các cách shallow copy
let shallow1 = { ...original }; // Spread operator
let shallow2 = Object.assign({}, original); // Object.assign
let shallow3 = original.slice(); // Array slice (cho arrays)

// Vấn đề với shallow copy
shallow1.name = 'Nguyen Van B'; // ✅ OK - primitive
shallow1.address.city = 'Ha Noi'; // ❌ Ảnh hưởng original!

console.log(original.address.city); // "Ha Noi" - bị thay đổi!

// Deep Copy - copy toàn bộ
function deepCopy<T>(obj: T): T {
  if (obj === null || typeof obj !== 'object') return obj;
  if (obj instanceof Date) return new Date(obj.getTime()) as any;
  if (obj instanceof Array) return obj.map((item) => deepCopy(item)) as any;
  if (typeof obj === 'object') {
    const copy: any = {};
    Object.keys(obj).forEach((key) => {
      copy[key] = deepCopy((obj as any)[key]);
    });
    return copy;
  }
  return obj;
}

let deepCopied = deepCopy(original);
deepCopied.address.city = 'Da Nang'; // ✅ Không ảnh hưởng original
console.log(original.address.city); // "Ho Chi Minh" - không đổi

// Sử dụng JSON (có hạn chế)
let jsonDeepCopy = JSON.parse(JSON.stringify(original));
// ❌ Mất functions, undefined, symbols, dates
```

**Best Practices:**

- Sử dụng shallow copy cho simple objects
- Sử dụng deep copy cho nested objects
- Sử dụng `structuredClone()` (modern browsers)
- Sử dụng libraries như Lodash `cloneDeep()`

**Mistakes:**

```typescript
// ❌ Sai: Nghĩ spread operator là deep copy
let obj = { a: { b: 1 } };
let copy = { ...obj };
copy.a.b = 2; // obj.a.b cũng = 2!

// ✅ Đúng: Sử dụng deep copy
let copy = structuredClone(obj); // hoặc custom deep copy function
```

</details>