# 🔒 Q6: Immutable vs Mutable

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🔒 Q6: Immutable vs Mutable</span></summary>


**⚡ Quick Summary:**
> **Mutable** = Có thể sửa trực tiếp  
> **Immutable** = Không sửa được, phải tạo mới

**💡 Ghi Nhớ:**
- 🔒 **Immutable**: string, number, boolean, null, undefined, symbol, bigint (primitives)
- 🔓 **Mutable**: object, array, function, date, map, set (references)
- 🎯 **Rule**: Primitive = immutable, Reference = mutable

**Trả lời:**

- **Immutable**: Không thể thay đổi sau khi tạo, tạo ra giá trị mới khi modify
- **Mutable**: Có thể thay đổi trực tiếp giá trị hiện tại
- **Ưu điểm**: Immutable an toàn hơn, dễ debug, tránh side effects
- **Nhược điểm**: Immutable tốn memory hơn, performance chậm hơn

**Code Example:**

```typescript
// Mutable - có thể thay đổi trực tiếp
let mutableArray: number[] = [1, 2, 3];
mutableArray.push(4); // Thay đổi array gốc
mutableArray[0] = 10; // Thay đổi phần tử

let mutableObject: { name: string; age: number } = { name: 'A', age: 25 };
mutableObject.age = 26; // Thay đổi object gốc

// Immutable - tạo giá trị mới
let immutableArray: readonly number[] = [1, 2, 3] as const;
// immutableArray.push(4);   // ❌ Error: Cannot modify readonly array

// Tạo array mới thay vì modify
let newArray: number[] = [...immutableArray, 4]; // [1, 2, 3, 4]
let updatedArray: number[] = immutableArray.map((x) => x * 2); // [2, 4, 6]

// Immutable object với spread operator
let immutableObj: { name: string; age: number } = { name: 'A', age: 25 };
let newObj: { name: string; age: number } = { ...immutableObj, age: 26 };
```

**Best Practices:**

- Sử dụng `readonly` cho arrays và objects khi có thể
- Sử dụng spread operator để tạo copy
- Sử dụng `Object.freeze()` để làm immutable object
- Sử dụng libraries như Immer cho complex immutable operations

**Mistakes:**

```typescript
// ❌ Sai: Modify trực tiếp
let users = [{ name: 'A', age: 25 }];
users[0].age = 26; // Modify trực tiếp

// ✅ Đúng: Tạo object mới
let users = [{ name: 'A', age: 25 }];
let updatedUsers = users.map((user) =>
  user.name === 'A' ? { ...user, age: 26 } : user
);
```

</details>