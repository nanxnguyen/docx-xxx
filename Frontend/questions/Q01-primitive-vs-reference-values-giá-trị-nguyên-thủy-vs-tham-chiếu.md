# 🚩 Q1: Primitive vs Reference Values - Giá Trị Nguyên Thủy vs Tham Chiếu

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🚩 Q1: Primitive vs Reference Values - Giá Trị Nguyên Thủy vs Tham Chiếu</span></summary>


**⚡ Quick Summary:**
> **Primitive** = Lưu giá trị trực tiếp (stack), copy = tạo bản sao mới  
> **Reference** = Lưu địa chỉ (stack) + data (heap), copy = share cùng địa chỉ

**💡 Ghi Nhớ:**
- 🔢 **7 Primitive**: number, string, boolean, undefined, null, symbol, bigint
- 📦 **1 Reference**: object (bao gồm: array, function, date, map, set...)
- 🎯 **Rule**: Primitive = "copy giá trị", Reference = "copy địa chỉ"

**Trả lời:

- **🔥 Primitive Values (Giá trị nguyên thủy)**: Là các giá trị cơ bản được lưu trữ trực tiếp trong memory stack (lưu trực tiếp trong ngăn xếp bộ nhớ)
- **🎯 Reference Values (Giá trị tham chiếu)**: Là các object được lưu trữ trong heap, chỉ có địa chỉ được lưu trong stack (đối tượng lưu trong heap, chỉ địa chỉ trong stack)
- **✅ Ưu điểm Primitive**: Nhanh hơn, an toàn hơn, không có side effects (không có tác dụng phụ)
- **⚠️ Nhược điểm Reference**: Có thể gây memory leak, thay đổi không mong muốn khi copy (có thể gây rò rỉ bộ nhớ)

**Code Example:**

```typescript
// 🔥 Primitive Values (Giá trị nguyên thủy) - lưu trực tiếp giá trị
let name: string = 'Nguyen Van A'; // string - chuỗi
let age: number = 25; // number - số
let isActive: boolean = true; // boolean - true/false
let data: null = null; // null - rỗng
let info: undefined = undefined; // undefined - chưa định nghĩa
let id: symbol = Symbol('id'); // symbol - duy nhất
let bigNum: bigint = 123n; // bigint - số nguyên lớn

// 🎯 Reference Values (Giá trị tham chiếu) - lưu địa chỉ trong stack, data trong heap
let person: object = { name: 'A', age: 25 }; // object - đối tượng
let numbers: number[] = [1, 2, 3]; // array - mảng
let func: Function = () => console.log('Hi'); // function - hàm

// 🔥 So sánh Primitive vs Reference (So sánh giá trị nguyên thủy vs tham chiếu)
let a: number = 10;
let b: number = a; // b = 10 (copy giá trị - sao chép giá trị)
b = 20; // a vẫn = 10, b = 20 (a không bị ảnh hưởng)

let obj1: object = { x: 10 };
let obj2: object = obj1; // obj2 trỏ đến cùng địa chỉ với obj1 (cùng tham chiếu)
obj2.x = 20; // obj1.x cũng = 20 (cùng reference - cả hai thay đổi)

// 🎯 Practical Example (Ví dụ thực tế)
// Primitive - an toàn
let userName = 'John';
let displayName = userName; // Copy giá trị
displayName = 'Jane';
console.log(userName); // "John" - không thay đổi
console.log(displayName); // "Jane" - chỉ displayName thay đổi

// Reference - cần cẩn thận
let user = { name: 'John', age: 25 }; // khởi tạo object
let userCopy = user; // Copy địa chỉ object
userCopy.name = 'Jane';
console.log(user.name); // "Jane" - user bị thay đổi!
console.log(userCopy.name); // "Jane" - cả hai cùng thay đổi
```

**🎯 Best Practices:**

- **✅ Sử dụng primitive values** khi có thể để tránh side effects
- **✅ Cẩn thận với reference values** khi pass vào functions - có thể bị thay đổi
- **✅ Sử dụng const cho reference values** để tránh reassignment (tránh gán lại)
- **✅ Sử dụng spread operator** để shallow copy: `{...obj}`, `[...array]`
- **✅ Sử dụng deep copy** cho nested objects: `JSON.parse(JSON.stringify(obj))`

**❌ Common Mistakes:**

```typescript
// ❌ Sai: Không hiểu reference copy (không hiểu sao chép tham chiếu)
let arr1 = [1, 2, 3];
let arr2 = arr1; // Copy địa chỉ, không phải giá trị
arr2.push(4); // arr1 cũng bị thay đổi!

// ✅ Đúng: Tạo copy mới (tạo bản sao mới)
let arr1 = [1, 2, 3];
let arr2 = [...arr1]; // shallow copy (sao chép nông)
arr2.push(4); // arr1 không bị ảnh hưởng

// ❌ Sai: So sánh reference values (so sánh giá trị tham chiếu)
let obj1 = { name: 'John' };
let obj2 = { name: 'John' };
console.log(obj1 === obj2); // false - khác địa chỉ

// ✅ Đúng: So sánh nội dung (so sánh nội dung)
console.log(JSON.stringify(obj1) === JSON.stringify(obj2)); // true

// ❌ Sai: Thay đổi object gốc (thay đổi đối tượng gốc)
function updateUser(user: any) {
  user.name = 'Updated'; // Thay đổi object gốc
}

// ✅ Đúng: Tạo object mới (tạo đối tượng mới)
function updateUser(user: any) {
  return { ...user, name: 'Updated' }; // Trả về object mới
}
```

</details>