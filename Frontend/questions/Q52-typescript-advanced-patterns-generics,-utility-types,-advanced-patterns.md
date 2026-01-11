# 🔷 Q52: TypeScript Advanced Patterns - Generics, Utility Types, Advanced Patterns

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"TypeScript advanced = Generics, Utility Types, Mapped Types, Conditional Types, Type Guards.**

**🔧 Core Advanced Concepts:**

1. **Generics** (📦 Kiểu dữ liệu tổng quát):

   - **Purpose**: Type-safe reusable functions/components (Tái sử dụng an toàn).
   - **Constraints**: `<T extends Type>` → limit T to specific types (Giới hạn T chỉ cho kiểu cụ thể).

   ```ts
   function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
     return obj[key]; // ✅ Type-safe property access (Truy cập thuộc tính an toàn)
   }
   const user = { name: 'Alice', age: 30 }; // 👤 User object
   getProperty(user, 'name'); // 🎯 Type: string - TS biết chính xác kiểu!
   ```

2. **Utility Types** (🛠️ Công cụ built-in của TypeScript):

   - **`Partial<T>`**: Tất cả properties optional (❔ Tất cả thuộc tính optional).
   - **`Required<T>`**: Tất cả properties required (⚠️ Bắt buộc tất cả).
   - **`Pick<T, K>`**: Lấy subset properties (🎯 Chọn một số thuộc tính).
   - **`Omit<T, K>`**: Loại bỏ properties (🗑️ Loại bỏ thuộc tính).
   - **`Record<K, V>`**: Object với keys K, values V (📋 Tạo object map).
   - **`Readonly<T>`**: Immutable properties (🔒 Không thể thay đổi).

   ```ts
   type User = { id: number; name: string; email: string }; // 👤 User type
   type PartialUser = Partial<User>; // ❔ All optional - Tất cả optional
   type UserName = Pick<User, 'id' | 'name'>; // 🎯 Only id, name - Chỉ lấy 2 field
   type NoEmail = Omit<User, 'email'>; // 🗑️ Exclude email - Loại bỏ email
   ```

3. **Mapped Types** (🗺️ Biến đổi types):

   - Transform existing types (Biến đổi type cũ thành type mới).

   ```ts
   type Readonly<T> = { readonly [K in keyof T]: T[K] }; // 🔒 Tất cả readonly
   type Optional<T> = { [K in keyof T]?: T[K] }; // ❔ Tất cả optional
   ```

4. **Conditional Types** (❓ Type có điều kiện - if/else cho types):

   - `T extends U ? X : Y` → type-level if-else (If/else ở level type).

   ```ts
   type IsString<T> = T extends string ? true : false; // ❓ Kiểm tra có phải string?
   type A = IsString<string>; // ✅ true - Là string
   type B = IsString<number>; // ❌ false - Không phải string
   ```

5. **Template Literal Types** (📝 TS 4.1+ - Xử lý chuỗi ở type level):

   - String manipulation at type level (Thao tác chuỗi trên type).

   ```ts
   type EventName<T extends string> = `on${Capitalize<T>}`; // 🏷️ Tạo tên event handler
   type ClickEvent = EventName<'click'>; // 👆 "onClick" - Viết hoa chữ đầu
   ```

6. **Type Guards** (🛡️ Bảo vệ type - Kiểm tra runtime):

   - Runtime type checking → narrow types (Kiểm tra kiểu lúc runtime, thu hẹp type).

   ```ts
   function isString(value: unknown): value is string {
     // 🛡️ Type guard function
     return typeof value === 'string'; // ❓ Kiểm tra runtime
   }
   if (isString(value)) {
     // ✅ Nếu là string
     value.toUpperCase(); // 🎯 TS biết value là string - An toàn!
   }
   ```

7. **Discriminated Unions** (🎭 Tagged Unions - State machine an toàn):

   - Type-safe state machines (Quản lý state an toàn).

   ```ts
   type State = // 🎭 3 trạng thái khác nhau

       | { status: 'loading' } // ⏳ Đang loading
       | { status: 'success'; data: string } // ✅ Thành công + có data
       | { status: 'error'; error: Error }; // ❌ Lỗi + có error object

   function handle(state: State) {
     switch (
       state.status // 🎯 Switch theo discriminator
     ) {
       case 'loading':
         return 'Loading...'; // ⏳ Chỉ có status
       case 'success':
         return state.data; // ✅ TS biết data tồn tại!
       case 'error':
         return state.error.message; // ❌ TS biết error tồn tại!
     }
   }
   ```

**🎯 Real-World Use Cases:**

1. **API Response Typing** (🌐 Type hóa API response):

   ```ts
   type ApiResponse<T> = // 📦 Generic response wrapper

       | { success: true; data: T } // ✅ Thành công + data
       | { success: false; error: string }; // ❌ Thất bại + error message

   async function fetchUser(): Promise<ApiResponse<User>> {
     // 👤 Fetch user
     // ... (Gọi API và trả về ApiResponse<User>)
   }
   ```

2. **Form State** (📝 Quản lý state của form):

   ```ts
   type FormState<T> = {
     // 📦 Generic form state
     values: T; // 📋 Giá trị của các field
     errors: Partial<Record<keyof T, string>>; // ❌ Lỗi validation (optional)
     touched: Partial<Record<keyof T, boolean>>; // 👆 Field đã touch (optional)
   };
   ```

3. **Branded Types** (🏷️ Nominal Typing - Ngăn trộn lẫn types giống nhau):

   - Prevent mixing similar types (Ngăn chặn dùng lẫn types giống nhau).

   ```ts
   type UserId = string & { __brand: 'UserId' }; // 🏷️ Brand UserId
   type ProductId = string & { __brand: 'ProductId' }; // 🏷️ Brand ProductId

   function getUser(id: UserId) {
     /*...*/
   } // 👤 Chỉ nhận UserId
   const userId = '123' as UserId; // 🏷️ Cast thành UserId
   getUser(userId); // ✅ OK - Đúng kiểu
   // getUser('456'); // ❌ Error: string not assignable to UserId - Sai kiểu!
   ```

**⚠️ Common Mistakes** (Lỗi thường gặp):

- **any overuse** (❌ Lạm dụng `any`): Defeat purpose of TypeScript → dùng `unknown` + type guards (Phá hủy mục đích của TS, hãy dùng `unknown`).
- **Type assertions abuse** (❌ Lạm dụng `as`): `as` bypass type checking → dùng type guards instead (`as` bỏ qua kiểm tra, dùng type guards).
- **Missing generic constraints** (❌ Thiếu constraints): `<T>` too broad → dùng `<T extends Type>` (`<T>` quá rộng, cần giới hạn).

**💡 Senior Insights** (Kiến thức nâng cao cho Senior):

- **infer keyword** (🔍 Trích xuất types): Extract types from other types (Rút type ra từ type khác).
  ```ts
  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never; // 🔍 Rút return type
  ```
- **Const assertions** (🔒 `as const`): `as const` → literal types instead of widening (Giữ nguyên literal type, không mở rộng).
  ```ts
  const colors = ['red', 'blue'] as const; // 🔒 Type: readonly ["red", "blue"] - Không mở rộng thành string[]
  ```
- **tsconfig strict mode** (⚠️ Chế độ nghiêm ngặt): Enable all strict checks (`strict: true`) → catch bugs early (Bắt lỗi sớm).
- **Declaration files** (📝 `.d.ts`): `.d.ts` for third-party libraries không có types (Cho thư viện bên thứ 3 không có types).

---

> **Câu hỏi phỏng vấn Senior Frontend Developer** > **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)
> **Thời gian trả lời:** 15-20 phút

---

## 📋 **Mục Lục**

1. [Generic Constraints & Conditional Types](#1-generic-constraints--conditional-types)
2. [Utility Types Deep Dive](#2-utility-types-deep-dive)
3. [Mapped & Template Literal Types](#3-mapped--template-literal-types)
4. [Type Guards & Discriminated Unions](#4-type-guards--discriminated-unions)
5. [Declaration Files & Ambient Declarations](#5-declaration-files--ambient-declarations)
6. [tsconfig.json Optimization](#6-tsconfigjson-optimization)
7. [Branded Types & Nominal Typing](#7-branded-types--nominal-typing)
8. [Real-World Use Cases](#8-real-world-use-cases)

---

## 1. Generic Constraints & Conditional Types

### **1.1. Generic Constraints**

```typescript
// ===================================================
// 🔒 **GENERIC CONSTRAINTS**
// ===================================================

// ❌ BAD: No constraints (TỒI - Không có ràng buộc)
function getProperty<T>(obj: T, key: string) {
  // 💡 Function generic không có constraint (Generic function without constraint)
  // 💡 key: string - Quá rộng, không đảm bảo key tồn tại trong obj
  // (key: string - Too broad, doesn't ensure key exists in obj)
  return obj[key];
  // ❌ Error: Element implicitly has 'any' type
  // (Lỗi: Phần tử ngầm định có kiểu 'any')
  // 💡 TypeScript không biết key có tồn tại trong obj không
  // (TypeScript doesn't know if key exists in obj)
}

// ✅ GOOD: Constrained generic (TỐT - Generic có ràng buộc)
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  // 💡 T: Type của object (Type of object)
  // 💡 K extends keyof T: K phải là một key của T (K must be a key of T)
  // 💡 Return type: T[K] - Type của property K trong T (Type of property K in T)
  return obj[key];
  // ✅ Type-safe! - An toàn về kiểu!
  // 💡 TypeScript biết chắc chắn key tồn tại và trả về đúng type
  // (TypeScript knows key exists and returns correct type)
}

const user = { name: 'Alice', age: 30 };
// 💡 user: { name: string; age: number } (user object với 2 properties)

const name = getProperty(user, 'name');
// ✅ Type: string - TypeScript tự động suy luận type là string
// (Type: string - TypeScript automatically infers type as string)
// 💡 Vì 'name' là key của user và user.name có type string
// (Because 'name' is a key of user and user.name has type string)

const age = getProperty(user, 'age');
// ✅ Type: number - TypeScript tự động suy luận type là number
// (Type: number - TypeScript automatically infers type as number)

// getProperty(user, 'invalid');
// ❌ Error: Argument of type '"invalid"' is not assignable to parameter of type '"name" | "age"'
// (Lỗi: '"invalid"' không phải là key hợp lệ của user)
// 💡 TypeScript bắt lỗi vì 'invalid' không tồn tại trong user
// (TypeScript catches error because 'invalid' doesn't exist in user)

// ===================================================
// 🎯 **EXTENDING MULTIPLE CONSTRAINTS**
// ===================================================

interface Identifiable {
  // 💡 Interface: Object có thể nhận diện (Interface: Object that can be identified)
  id: string | number;
  // 🔑 ID: string hoặc number (ID: string or number)
}

interface Timestamped {
  // 💡 Interface: Object có timestamp (Interface: Object with timestamp)
  createdAt: Date;
  // 📅 Ngày tạo (Created date)
  updatedAt: Date;
  // 📅 Ngày cập nhật (Updated date)
}

// ✅ Generic with multiple constraints (Generic với nhiều ràng buộc)
function updateEntity<T extends Identifiable & Timestamped>(
  // 💡 T extends Identifiable & Timestamped: T phải có cả 2 interfaces
  // (T extends Identifiable & Timestamped: T must have both interfaces)
  // 💡 & = intersection type - Kết hợp cả 2 interfaces
  // (& = intersection type - Combines both interfaces)
  entity: T,
  // 📦 Entity cần update (Entity to update)
  updates: Partial<T>
  // 📝 Updates: Partial<T> - Tất cả properties đều optional
  // (Updates: Partial<T> - All properties are optional)
  // 💡 Chỉ cần truyền properties muốn update
  // (Only need to pass properties to update)
): T {
  // 💡 Return type: T - Trả về cùng type với entity
  // (Return type: T - Returns same type as entity)
  return {
    ...entity,
    // 📦 Spread entity - Giữ nguyên tất cả properties cũ
    // (Spread entity - Keep all old properties)
    ...updates,
    // 📝 Spread updates - Ghi đè properties mới
    // (Spread updates - Override with new properties)
    updatedAt: new Date(),
    // 📅 Type-safe access - TypeScript biết updatedAt tồn tại vì T extends Timestamped
    // (Type-safe access - TypeScript knows updatedAt exists because T extends Timestamped)
    // 💡 Tự động update updatedAt khi entity thay đổi
    // (Automatically update updatedAt when entity changes)
  };
}

// ===================================================
// 🔄 **CONDITIONAL TYPES**
// ===================================================

// Basic conditional type (Conditional type cơ bản)
type IsString<T> = T extends string ? true : false;
// 💡 Conditional type: Nếu T extends string → true, ngược lại → false
// (Conditional type: If T extends string → true, otherwise → false)
// 💡 T extends string: Kiểm tra T có phải là string hoặc subtype của string không
// (T extends string: Check if T is string or subtype of string)

type A = IsString<string>;
// ✅ true - string extends string (string là string)
// (true - string extends string)

type B = IsString<number>;
// ❌ false - number không extends string (number không phải string)
// (false - number doesn't extend string)

// ✅ Extract return type from function (Rút return type từ function)
type ReturnTypeOf<T> = T extends (...args: any[]) => infer R ? R : never;
// 💡 Conditional type với infer keyword
// (Conditional type with infer keyword)
// 💡 T extends (...args: any[]) => infer R: Kiểm tra T có phải là function không
// (T extends (...args: any[]) => infer R: Check if T is a function)
// 💡 infer R: Rút return type R từ function type T
// (infer R: Extract return type R from function type T)
// 💡 Nếu T là function → return R, ngược lại → never
// (If T is function → return R, otherwise → never)

type Func = () => { name: string };
// 💡 Function type trả về object { name: string }
// (Function type returning object { name: string })

type Result = ReturnTypeOf<Func>;
// ✅ { name: string } - Rút được return type!
// ({ name: string } - Extracted return type!)
// 💡 TypeScript tự động suy luận return type từ Func
// (TypeScript automatically infers return type from Func)

// ✅ Unwrap Promise type (Mở Promise type)
type Awaited<T> = T extends Promise<infer U> ? U : T;
// 💡 Conditional type: Nếu T là Promise → lấy type bên trong, ngược lại → giữ nguyên T
// (Conditional type: If T is Promise → get inner type, otherwise → keep T)
// 💡 infer U: Rút type U từ Promise<U>
// (infer U: Extract type U from Promise<U>)

type AsyncData = Promise<{ data: string }>;
// 💡 Promise type chứa object { data: string }
// (Promise type containing object { data: string })

type SyncData = Awaited<AsyncData>;
// ✅ { data: string } - Mở được Promise, lấy type bên trong!
// ({ data: string } - Unwrapped Promise, got inner type!)
// 💡 Tương đương với await Promise → lấy giá trị bên trong
// (Equivalent to await Promise → get inner value)

// ✅ Recursive conditional types (Conditional types đệ quy)
type DeepReadonly<T> = {
  // 💡 DeepReadonly: Làm tất cả properties (kể cả nested) thành readonly
  // (DeepReadonly: Make all properties including nested readonly)
  readonly [K in keyof T]: // ([K in keyof T]: Mapped type - Loop through all keys of T) // 💡 [K in keyof T]: Mapped type - Loop qua tất cả keys của T
  // 💡 readonly: Thêm readonly modifier cho mỗi property
  // (readonly: Add readonly modifier for each property)
  T[K] extends object
    ? DeepReadonly<T[K]>
    : // 💡 Nếu T[K] là object → đệ quy DeepReadonly cho nested object
      // (If T[K] is object → recursively apply DeepReadonly to nested object)
      // 💡 Đảm bảo nested objects cũng được làm readonly
      // (Ensures nested objects are also made readonly)
      T[K];
  // 💡 Nếu T[K] không phải object → giữ nguyên type
  // (If T[K] is not object → keep original type)
};

interface Config {
  // 💡 Config interface với nested objects
  // (Config interface with nested objects)
  server: {
    // 🌐 Server config (nested object)
    port: number;
    // 🔌 Port number
    host: string;
    // 🏠 Host string
  };
  database: {
    // 💾 Database config (nested object)
    url: string;
    // 🔗 Database URL
  };
}

type ReadonlyConfig = DeepReadonly<Config>;
// ✅ All properties (including nested) are readonly
// (Tất cả properties kể cả nested đều readonly)
// 💡 Kết quả:
// (Result:)
// {
//   readonly server: {
//     readonly port: number;
//     readonly host: string;
//   };
//   readonly database: {
//     readonly url: string;
//   };
// }
// 💡 Tất cả properties ở mọi level đều readonly!
// (All properties at every level are readonly!)
```

### **1.2. Advanced Conditional Types**

```typescript
// ===================================================
// 🎨 **DISTRIBUTIVE CONDITIONAL TYPES** (Conditional Types phân phối)
// ===================================================

type ToArray<T> = T extends any ? T[] : never;
// 📦 Biến mỗi type thành array (Convert each type to array)
// 💡 T extends any: Luôn true, nhưng có tính chất distributive
// (T extends any: Always true, but has distributive property)
// 💡 Distributive: Áp dụng conditional type cho từng member trong union
// (Distributive: Apply conditional type to each member in union)

type StrOrNum = string | number;
// 🔀 Union type: string hoặc number (Union type: string or number)

type ArrOfStrOrNum = ToArray<StrOrNum>;
// 🎨 string[] | number[] (distributive - Phân phối!)
// (string[] | number[] - distributive!)
// 💡 Distributive behavior: ToArray<string | number> = ToArray<string> | ToArray<number>
// (Distributive behavior: ToArray<string | number> = ToArray<string> | ToArray<number>)
// 💡 Kết quả: string[] | number[] (không phải (string | number)[])
// (Result: string[] | number[] - not (string | number)[])

// ✅ Non-distributive version (Không phân phối - Giữ nguyên union)
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;
// 📦 Wrap trong tuple để ngăn distribute (Wrap in tuple to prevent distribution)
// 💡 [T] extends [any]: Wrap T trong tuple → mất tính distributive
// ([T] extends [any]: Wrap T in tuple → loses distributive property)
// 💡 Conditional type chỉ áp dụng cho toàn bộ union, không phân phối
// (Conditional type only applies to entire union, doesn't distribute)

type ArrOfStrOrNumNonDist = ToArrayNonDist<StrOrNum>;
// 🎯 (string | number)[] - Giữ nguyên union!
// ((string | number)[] - Keep union intact!)
// 💡 Kết quả: Array chứa string hoặc number (không phải string[] | number[])
// (Result: Array containing string or number - not string[] | number[])

// ===================================================
// 🔍 **INFER KEYWORD** (Extract types - Rút types ra)
// ===================================================

// Extract function parameters (Rút parameters từ function)
type Parameters<T> = T extends (...args: infer P) => any ? P : never;
// 🔍 infer P = rút parameters (infer P = extract parameters)
// 💡 T extends (...args: infer P) => any: Kiểm tra T có phải là function không
// (T extends (...args: infer P) => any: Check if T is a function)
// 💡 infer P: Rút type của parameters array P từ function type T
// (infer P: Extract type of parameters array P from function type T)
// 💡 Nếu T là function → return P (parameters tuple), ngược lại → never
// (If T is function → return P - parameters tuple, otherwise → never)

type Params = Parameters<(a: string, b: number) => void>;
// 🎯 [string, number] - Rút được params!
// ([string, number] - Extracted params!)
// 💡 Function có 2 params: string và number → tuple [string, number]
// (Function has 2 params: string and number → tuple [string, number])

// Extract first array element type (Lấy type của phần tử đầu tiên)
type FirstElement<T> = T extends [infer F, ...any[]] ? F : never;
// 🔍 infer F = rút phần tử đầu (infer F = extract first element)
// 💡 T extends [infer F, ...any[]]: Kiểm tra T có phải là tuple/array không
// (T extends [infer F, ...any[]]: Check if T is tuple/array)
// 💡 infer F: Rút type của phần tử đầu tiên F
// (infer F: Extract type of first element F)
// 💡 ...any[]: Phần còn lại của array (rest elements)
// (...any[]: Rest of array - rest elements)

type First = FirstElement<[string, number, boolean]>;
// 🎯 string - Phần tử đầu!
// (string - First element!)
// 💡 Tuple [string, number, boolean] → rút được string
// (Tuple [string, number, boolean] → extracted string)

// Extract object property types (Truy cập type của property)
type ExtractPropType<T, K extends keyof T> = T[K];
// 🎯 Lấy type của property K (Get type of property K)
// 💡 T[K]: Indexed access type - Truy cập type của property K trong T
// (T[K]: Indexed access type - Access type of property K in T)
// 💡 K extends keyof T: K phải là key hợp lệ của T
// (K extends keyof T: K must be valid key of T)

interface User {
  // 👤 User interface (User interface)
  id: number;
  // 🔢 ID (ID)
  profile: {
    // 📋 Nested profile (Nested profile object)
    name: string;
    // 📝 Name (Name)
    avatar: string;
    // 🖼️ Avatar URL (Avatar URL)
  };
}

type ProfileType = ExtractPropType<User, 'profile'>;
// 🎯 { name: string; avatar: string } - Rút được profile type!
// ({ name: string; avatar: string } - Extracted profile type!)
// 💡 User['profile'] → type của property 'profile' trong User
// (User['profile'] → type of property 'profile' in User)
// 💡 Kết quả: { name: string; avatar: string }
// (Result: { name: string; avatar: string })
```

---

## 2. Utility Types Deep Dive

### **2.1. Built-in Utility Types**

```typescript
// ===================================================
// 🛠️ **BUILT-IN UTILITY TYPES** (Công cụ built-in của TS)
// ===================================================

interface Todo {
  // 📋 Todo interface
  id: number; // 🔢 ID
  title: string; // 📝 Tiêu đề
  description: string; // 📖 Mô tả
  completed: boolean; // ✅ Đã hoàn thành?
  createdAt: Date; // 📅 Ngày tạo
}

// ✅ Partial<T> - All properties optional (Tất cả thuộc tính thành optional)
type PartialTodo = Partial<Todo>;
// ❔ Tất cả field có thể undefined (All fields can be undefined)
// 💡 Partial<Todo> = { id?: number; title?: string; description?: string; ... }
// (Partial<Todo> = { id?: number; title?: string; description?: string; ... })
// 💡 Tất cả properties đều có dấu ? (All properties have ? modifier)

const updateTodo = (id: number, updates: Partial<Todo>) => {
  /* ... */
};
// ✏️ Cập nhật một vài field (Update some fields)
// 💡 updates: Chỉ cần truyền properties muốn update, không cần tất cả
// (updates: Only need to pass properties to update, not all)
// 💡 Ví dụ: updateTodo(1, { title: 'New title' }) - Chỉ update title
// (Example: updateTodo(1, { title: 'New title' }) - Only update title)

// ✅ Required<T> - All properties required (Bắt buộc tất cả)
type RequiredTodo = Required<Partial<Todo>>;
// ⚠️ Biến tất cả thành required (Convert all to required)
// 💡 Required<Partial<Todo>>: Lấy Partial<Todo> (tất cả optional) → làm tất cả required
// (Required<Partial<Todo>>: Take Partial<Todo> - all optional → make all required)
// 💡 Kết quả: Tất cả properties đều bắt buộc (không có ?)
// (Result: All properties are required - no ? modifier)

// ✅ Readonly<T> - All properties readonly (Không thể thay đổi)
type ReadonlyTodo = Readonly<Todo>;
// 🔒 Immutable - Không thể modify (Immutable - Cannot modify)
// 💡 Readonly<Todo> = { readonly id: number; readonly title: string; ... }
// (Readonly<Todo> = { readonly id: number; readonly title: string; ... })
// 💡 Tất cả properties đều có readonly modifier
// (All properties have readonly modifier)
// 💡 Không thể gán lại giá trị sau khi khởi tạo
// (Cannot reassign values after initialization)

// ✅ Pick<T, K> - Select specific properties (Chọn một số properties)
type TodoPreview = Pick<Todo, 'id' | 'title' | 'completed'>;
// 🎯 Chỉ lấy 3 field (Only take 3 fields)
// 💡 Pick<Todo, 'id' | 'title' | 'completed'> = { id: number; title: string; completed: boolean }
// (Pick<Todo, 'id' | 'title' | 'completed'> = { id: number; title: string; completed: boolean })
// 💡 Chỉ giữ lại các properties được chỉ định, loại bỏ các properties khác
// (Only keep specified properties, remove others)

// ✅ Omit<T, K> - Exclude specific properties (Loại bỏ properties)
type TodoWithoutDates = Omit<Todo, 'createdAt'>;
// 🗑️ Bo qua createdAt (Exclude createdAt)
// 💡 Omit<Todo, 'createdAt'> = { id: number; title: string; description: string; completed: boolean }
// (Omit<Todo, 'createdAt'> = { id: number; title: string; description: string; completed: boolean })
// 💡 Loại bỏ 'createdAt' property, giữ lại tất cả properties khác
// (Remove 'createdAt' property, keep all other properties)

// ✅ Record<K, T> - Object with specific keys and value type (Tạo object map)
type TodoMap = Record<number, Todo>;
// 📋 Map ID → Todo (Map ID → Todo)
// 💡 Record<number, Todo> = { [key: number]: Todo }
// (Record<number, Todo> = { [key: number]: Todo })
// 💡 Object với keys là number, values là Todo
// (Object with number keys, Todo values)

const todos: TodoMap = {
  1: { id: 1, title: 'Learn TS' /* ... */ },
  // 🔑 Key 1: Todo object (Key 1: Todo object)
  2: { id: 2, title: 'Build App' /* ... */ },
  // 🔑 Key 2: Todo object (Key 2: Todo object)
};
// 💡 todos là object map: number → Todo
// (todos is object map: number → Todo)

// ✅ Exclude<T, U> - Exclude types from union (Loại bỏ types từ union)
type Primitive = string | number | boolean | null | undefined;
// 📦 Tất cả primitive types (All primitive types)
// 💡 Union của các primitive types (Union of primitive types)

type NonNullable = Exclude<Primitive, null | undefined>;
// 🎯 string | number | boolean - Loại null/undefined
// (string | number | boolean - Remove null/undefined)
// 💡 Exclude loại bỏ null và undefined từ union
// (Exclude removes null and undefined from union)
// 💡 Kết quả: Chỉ còn string | number | boolean
// (Result: Only string | number | boolean remain)

// ✅ Extract<T, U> - Extract types from union (Lấy ra types từ union)
type StringOrNumber = Extract<string | number | boolean, string | number>;
// 🎯 string | number - Chỉ lấy 2 kiểu này
// (string | number - Only take these 2 types)
// 💡 Extract chỉ giữ lại các types có trong cả 2 unions
// (Extract only keeps types present in both unions)
// 💡 string | number | boolean ∩ string | number = string | number
// (string | number | boolean ∩ string | number = string | number)

// ✅ NonNullable<T> - Remove null and undefined (Loại bỏ null và undefined)
type MaybeString = string | null | undefined;
// ❓ Có thể null/undefined (Can be null/undefined)
// 💡 Union type có thể là string, null, hoặc undefined
// (Union type can be string, null, or undefined)

type DefiniteString = NonNullable<MaybeString>;
// 🎯 string - Chắc chắn là string!
// (string - Definitely string!)
// 💡 NonNullable loại bỏ null và undefined
// (NonNullable removes null and undefined)
// 💡 Kết quả: Chỉ còn string (không thể null/undefined)
// (Result: Only string remains - cannot be null/undefined)

// ✅ ReturnType<T> - Get function return type (Lấy kiểu trả về của function)
const getUser = () => ({ id: 1, name: 'Alice' });
// 🛠️ Function trả về object (Function returning object)
// 💡 Function không có params, trả về { id: number; name: string }
// (Function with no params, returns { id: number; name: string })

type User = ReturnType<typeof getUser>;
// 🎯 { id: number; name: string } - Rút type từ function!
// ({ id: number; name: string } - Extracted type from function!)
// 💡 ReturnType tự động suy luận return type từ function
// (ReturnType automatically infers return type from function)
// 💡 typeof getUser: Lấy type của function (Get type of function)

// ✅ Parameters<T> - Get function parameters (Lấy parameters của function)
const createUser = (name: string, age: number) => ({ name, age });
// 🛠️ Function có 2 params (Function with 2 params)
// 💡 Function nhận name: string và age: number
// (Function receives name: string and age: number)

type CreateUserParams = Parameters<typeof createUser>;
// 🎯 [string, number] - Rút params!
// ([string, number] - Extracted params!)
// 💡 Parameters tự động suy luận parameters tuple từ function
// (Parameters automatically infers parameters tuple from function)
// 💡 Kết quả: Tuple [string, number] (thứ tự giống function params)
// (Result: Tuple [string, number] - same order as function params)

// ✅ InstanceType<T> - Get instance type of constructor (Lấy instance type của class)
class Product {
  // 🏭 Product class (Product class)
  constructor(public name: string, public price: number) {}
  // 🛠️ Constructor (Constructor)
  // 💡 public: Tự động tạo properties name và price
  // (public: Automatically creates name and price properties)
}

type ProductInstance = InstanceType<typeof Product>;
// 🎯 Product - Instance type!
// (Product - Instance type!)
// 💡 InstanceType lấy type của instance được tạo từ constructor
// (InstanceType gets type of instance created from constructor)
// 💡 typeof Product: Lấy type của class constructor
// (typeof Product: Get type of class constructor)
// 💡 Kết quả: Product (type của instance, không phải constructor)
// (Result: Product - type of instance, not constructor)
```

### **2.2. Custom Utility Types**

```typescript
// ===================================================
// 🎨 **CUSTOM UTILITY TYPES** (Tạo utility types riêng)
// ===================================================

// ✅ DeepPartial - Recursive partial (Partial đệ quy cho nested objects)
type DeepPartial<T> = {
  // 💡 DeepPartial: Làm tất cả properties (kể cả nested) thành optional
  // (DeepPartial: Make all properties including nested optional)
  [K in keyof T]?: // ([K in keyof T]?: Mapped type with ? modifier - All keys are optional) // 💡 [K in keyof T]?: Mapped type với ? modifier - Tất cả keys đều optional
  T[K] extends object ? DeepPartial<T[K]> : T[K];
  // 🔄 Đệ quy nếu là object (Recursive if object)
  // 💡 Nếu T[K] là object → đệ quy DeepPartial cho nested object
  // (If T[K] is object → recursively apply DeepPartial to nested object)
  // 💡 Nếu T[K] không phải object → giữ nguyên type
  // (If T[K] is not object → keep original type)
};

interface Config {
  // ⚙️ Config có nested objects (Config with nested objects)
  server: {
    // 🌐 Server config (nested object)
    port: number;
    // 🔌 Port (Port number)
    host: string;
    // 🏠 Host (Host string)
    ssl: {
      // 🔒 SSL config (nested object trong server)
      enabled: boolean;
      // ✅ Bật/tắt SSL (Enable/disable SSL)
      cert: string;
      // 📜 Certificate (Certificate string)
    };
  };
}

const updateConfig = (config: DeepPartial<Config>) => {
  // 📝 Tất cả properties (kể cả nested) đều optional!
  // (All properties including nested are optional!)
  // 💡 DeepPartial<Config> cho phép update bất kỳ property nào ở bất kỳ level nào
  // (DeepPartial<Config> allows updating any property at any level)
  // Can update any nested property (Có thể update bất kỳ property nào)
};

updateConfig({ server: { ssl: { enabled: true } } });
// ✅ Valid - Chỉ update 1 nested field!
// (Valid - Only update 1 nested field!)
// 💡 Chỉ cần truyền properties muốn update, không cần tất cả
// (Only need to pass properties to update, not all)
// 💡 TypeScript tự động suy luận type an toàn cho nested updates
// (TypeScript automatically infers safe types for nested updates)

// ✅ Nullable - Add null to all properties (Thêm null cho tất cả properties)
type Nullable<T> = {
  [K in keyof T]: T[K] | null; // ❓ Mỗi property có thể null
};

type NullableUser = Nullable<{ name: string; age: number }>; // 👤 User có thể có field null
// { name: string | null; age: number | null } (Tất cả đều nullable!)

// ✅ Optional - Specific properties optional (Chọn properties nào optional)
type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>; // 🎯 Omit rồi Partial

type UserWithOptionalEmail = Optional<
  { name: string; email: string; age: number }, // 📋 Original type
  'email' // 📧 Chỉ email là optional
>;
// { name: string; age: number; email?: string } (Chỉ email optional!)

// ✅ RequireAtLeastOne - At least one property required (Ít nhất 1 property bắt buộc)
type RequireAtLeastOne<T, Keys extends keyof T = keyof T> = Pick<
  T,
  Exclude<keyof T, Keys>
> &
  {
    // 🎯 Complex type: Ít nhất 1 trong các Keys phải có
    [K in Keys]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<Keys, K>>>;
  }[Keys];

type ContactInfo = {
  // 📞 Contact info
  email?: string; // 📧 Email (optional)
  phone?: string; // 📱 Phone (optional)
  address?: string; // 🏠 Address (optional)
};

type ValidContact = RequireAtLeastOne<ContactInfo>; // ⚠️ PHẢI có ít nhất 1 trong 3!
// Must have at least one of email, phone, or address (Phải có ít nhất 1 cách liên lạc)

// ✅ Mutable - Remove readonly (Bỏ readonly modifier)
type Mutable<T> = {
  -readonly [K in keyof T]: T[K]; // 🔓 Bỏ readonly bằng dấu trừ (-)
};

type MutableConfig = Mutable<ReadonlyConfig>; // 📝 Biến readonly thành mutable!

// ✅ PromiseType - Extract Promise value type (Lấy type bên trong Promise)
type PromiseType<T> = T extends Promise<infer U> ? U : T; // 🔍 Unwrap Promise

type ApiResponse = Promise<{ data: string }>; // 📦 Promise chứa object
type Data = PromiseType<ApiResponse>; // 🎯 { data: string } - Lấy được type bên trong!
```

---

## 3. Mapped & Template Literal Types

### **3.1. Mapped Types**

```typescript
// ===================================================
// 🗺️ **MAPPED TYPES** (Biến đổi types bằng mapping)
// ===================================================

// ✅ Basic mapped type (Mapped type cơ bản)
type Readonly<T> = {
  // 🔒 Readonly utility
  readonly [K in keyof T]: T[K]; // 🔑 Loop qua tất cả keys, thêm readonly
};

// ✅ Add prefix to keys (Thêm prefix vào tên keys)
type Getters<T> = {
  // 🔧 Tạo getters tự động
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]; // 🏷️ Rename key: name → getName
};

interface User {
  // 👤 User interface
  name: string; // 📝 Name
  age: number; // 🔢 Age
}

type UserGetters = Getters<User>; // 🔧 Auto-generate getters
// {  // 🎯 Kết quả:
//   getName: () => string;  // 📝 name → getName
//   getAge: () => number;   // 🔢 age → getAge
// }

// ✅ Filter properties by type (Lọc properties theo type)
type FilterByType<T, ValueType> = {
  // 🔍 Chỉ giữ properties có type = ValueType
  [K in keyof T as T[K] extends ValueType ? K : never]: T[K]; // ❓ Conditional: giữ K nếu đúng type
};

interface Product {
  // 🏭 Product interface
  id: number; // 🔢 ID
  name: string; // 📝 Name
  price: number; // 💰 Price
  description: string; // 📖 Description
}

type StringProperties = FilterByType<Product, string>; // 🎯 Chỉ lấy string properties
// { name: string; description: string } (Chỉ có 2 fields string!)

type NumberProperties = FilterByType<Product, number>; // 🎯 Chỉ lấy number properties
// { id: number; price: number } (Chỉ có 2 fields number!)

// ✅ Transform property types (Biến đổi type của properties)
type Stringify<T> = {
  // 🔄 Biến tất cả thành string
  [K in keyof T]: string; // 📝 Mọi property đều thành string
};

type StringifiedProduct = Stringify<Product>; // 📝 All properties → string
// { id: string; name: string; price: string; description: string } (Tất cả đều string!)
```

### **3.2. Template Literal Types**

```typescript
// ===================================================
// 📝 **TEMPLATE LITERAL TYPES** (TypeScript 4.1+ - Xử lý chuỗi ở type level)
// ===================================================

// ✅ Basic template literals (Template literals cơ bản)
type Color = 'red' | 'blue' | 'green'; // 🎨 3 màu
type Quantity = 'one' | 'two' | 'three'; // 🔢 3 số lượng

type ColoredQuantity = `${Quantity} ${Color}`; // 🎯 Kết hợp 2 unions
// 'one red' | 'one blue' | 'one green' | 'two red' | ... (🎨 3x3 = 9 combinations!)

// ✅ Event handler types (Tạo event handlers tự động)
type EventNames = 'click' | 'focus' | 'blur'; // 👆 3 events
type EventHandlers = {
  // 🛠️ Auto-generate handlers
  [K in EventNames as `on${Capitalize<K>}`]: (event: Event) => void; // 🏷️ Viết hoa chữ đầu
};

// {  // 🎯 Kết quả:
//   onClick: (event: Event) => void;  // 👆 click → onClick
//   onFocus: (event: Event) => void;  // 🎯 focus → onFocus
//   onBlur: (event: Event) => void;   // 🎯 blur → onBlur
// }

// ✅ CSS properties (Tạo CSS properties tự động)
type CSSProp = 'margin' | 'padding'; // 📏 2 properties
type Direction = 'top' | 'right' | 'bottom' | 'left'; // 🧭 4 hướng

type CSSProperties = `${CSSProp}-${Direction}`; // 🎯 Kết hợp
// 'margin-top' | 'margin-right' | ... | 'padding-left' (🎨 2x4 = 8 properties!)

// ✅ API routes (Tạo API routes type-safe)
type HTTPMethod = 'GET' | 'POST' | 'PUT' | 'DELETE'; // 🌐 4 HTTP methods
type Resource = 'users' | 'products' | 'orders'; // 📦 3 resources

type APIRoute = `${Lowercase<HTTPMethod>} /api/${Resource}`; // 🔡 Viết thường method
// 'get /api/users' | 'post /api/users' | ... (🎯 4x3 = 12 routes!)

// ✅ Type-safe path builder (Nối chuỗi thành path an toàn)
type Join<T extends string[], D extends string = '/'> = T extends [
  // 🔗 Join array of strings
  infer F extends string, // 🔍 Lấy phần tử đầu
  ...infer R extends string[] // 📦 Lấy phần còn lại
]
  ? R extends [] // ❓ Nếu không còn phần tử nào
    ? F // ✅ Trả về phần tử đầu
    : `${F}${D}${Join<R, D>}` // 🔁 Recursive: F + delimiter + Join phần còn lại
  : ''; // 🎯 Empty string nếu array rỗng

type Path = Join<['api', 'v1', 'users', 'profile']>; // 🎯 'api/v1/users/profile' - Nối bằng /!
```

---

## 4. Type Guards & Discriminated Unions

### **4.1. Type Guards**

```typescript
// ===================================================
// 🛡️ **TYPE GUARDS** (Bảo vệ type - Kiểm tra runtime)
// ===================================================

// ✅ User-defined type guard (Type guard tự định nghĩa)
interface Cat {
  // 🐱 Cat interface
  meow: () => void; // 🔊 Phương thức keu meo meo
}

interface Dog {
  // 🐶 Dog interface
  bark: () => void; // 🔊 Phương thức sủa gậm gậm
}

function isCat(animal: Cat | Dog): animal is Cat {
  // 🛡️ Type guard function - "animal is Cat" là type predicate
  // (Type guard function - "animal is Cat" is type predicate)
  // 💡 Return type: animal is Cat - Type predicate, TypeScript sẽ narrow type
  // (Return type: animal is Cat - Type predicate, TypeScript will narrow type)
  // 💡 Nếu return true → TypeScript biết animal là Cat
  // (If return true → TypeScript knows animal is Cat)
  return 'meow' in animal;
  // ❓ Kiểm tra có method meow không? (Check if has meow method?)
  // 💡 'meow' in animal: Kiểm tra property 'meow' có tồn tại trong animal không
  // ('meow' in animal: Check if property 'meow' exists in animal)
  // 💡 Nếu có meow → là Cat, ngược lại → là Dog
  // (If has meow → is Cat, otherwise → is Dog)
}

function makeSound(animal: Cat | Dog) {
  // 🔊 Function nhận Cat hoặc Dog (Function receives Cat or Dog)
  // 💡 animal: Cat | Dog - Union type, TypeScript không biết chắc là Cat hay Dog
  // (animal: Cat | Dog - Union type, TypeScript doesn't know if Cat or Dog)

  if (isCat(animal)) {
    // ❓ Nếu là Cat (If is Cat)
    // 💡 Sau khi gọi isCat(animal), TypeScript narrow type từ Cat | Dog → Cat
    // (After calling isCat(animal), TypeScript narrows type from Cat | Dog → Cat)
    animal.meow();
    // 🎯 TypeScript biết chắc chắn là Cat - Có meow()!
    // (TypeScript knows definitely is Cat - Has meow()!)
    // 💡 TypeScript tự động suy luận animal là Cat trong block này
    // (TypeScript automatically infers animal is Cat in this block)
  } else {
    // 🐶 Không thì là Dog (Otherwise is Dog)
    // 💡 TypeScript narrow type từ Cat | Dog → Dog (loại trừ Cat)
    // (TypeScript narrows type from Cat | Dog → Dog - excludes Cat)
    animal.bark();
    // 🎯 TypeScript biết chắc chắn là Dog - Có bark()!
    // (TypeScript knows definitely is Dog - Has bark()!)
    // 💡 TypeScript tự động suy luận animal là Dog trong block này
    // (TypeScript automatically infers animal is Dog in this block)
  }
}

// ✅ Type predicate with generics (Type guard với generics)
function isOfType<T>( // 📦 Generic type guard
  value: unknown, // ❓ Giá trị cần kiểm tra (unknown type)
  check: (val: any) => boolean // 🔍 Hàm kiểm tra
): value is T {
  // 🛡️ Type predicate - "value is T"
  return check(value); // 🎯 Trả về kết quả kiểm tra
}

const isString = (val: unknown): val is string => typeof val === 'string'; // 📝 Kiểm tra string
const isNumber = (val: unknown): val is number => typeof val === 'number'; // 🔢 Kiểm tra number

// ✅ Array type guard (Kiểm tra array và type của elements)
function isStringArray(value: unknown): value is string[] {
  // 📋 Kiểm tra array of strings
  return (
    Array.isArray(value) && value.every((item) => typeof item === 'string')
  ); // ❓ Là array và mọi item là string?
}

// ✅ Non-null assertion guard (Assertion function - Throw nếu null/undefined)
function assertDefined<T>(value: T | null | undefined): asserts value is T {
  // 🛡️ "asserts value is T" - Assert type
  if (value === null || value === undefined) {
    // ❓ Nếu là null hoặc undefined
    throw new Error('Value is null or undefined'); // ❌ Throw error!
  } // ✅ Nếu không throw, TS biết value không null/undefined
}

const user: User | null = getUser(); // 👤 User có thể null
assertDefined(user); // 🛡️ Assert user không null (throw nếu null)
user.name; // ✅ TypeScript biết chắc chắn user không null - An toàn!
```

### **4.2. Discriminated Unions**

```typescript
// ===================================================
// 🎭 **DISCRIMINATED UNIONS** (Tagged Unions - Union với discriminator)
// ===================================================

// ✅ API Response types (Các kiểu response khác nhau)
interface SuccessResponse {
  // ✅ Success response
  type: 'success'; // 🏷️ Discriminator - Đánh dấu kiểu là success
  data: { id: number; name: string }; // 📦 Data khi thành công
}

interface ErrorResponse {
  // ❌ Error response
  type: 'error'; // 🏷️ Discriminator - Đánh dấu kiểu là error
  error: { code: string; message: string }; // 🚨 Error info
}

interface LoadingResponse {
  // ⏳ Loading response
  type: 'loading'; // 🏷️ Discriminator - Đánh dấu kiểu là loading
}

type APIResponse = SuccessResponse | ErrorResponse | LoadingResponse; // 🔀 Union của 3 kiểu

function handleResponse(response: APIResponse) {
  // 🛠️ Xử lý response (Handle response)
  // 💡 response: APIResponse - Union type của 3 response types
  // (response: APIResponse - Union type of 3 response types)

  switch (response.type) {
    // 🎯 Switch theo discriminator "type" (Switch by discriminator "type")
    // 💡 response.type là discriminator - TypeScript dùng để narrow type
    // (response.type is discriminator - TypeScript uses to narrow type)

    case 'success':
      // ✅ Nếu thành công (If success)
      // 💡 TypeScript narrow type: APIResponse → SuccessResponse
      // (TypeScript narrows type: APIResponse → SuccessResponse)
      console.log(response.data);
      // 🎯 TS biết response.data tồn tại!
      // (TS knows response.data exists!)
      // 💡 TypeScript tự động biết response có property 'data' vì type là 'success'
      // (TypeScript automatically knows response has 'data' property because type is 'success')
      break;

    case 'error':
      // ❌ Nếu lỗi (If error)
      // 💡 TypeScript narrow type: APIResponse → ErrorResponse
      // (TypeScript narrows type: APIResponse → ErrorResponse)
      console.error(response.error);
      // 🎯 TS biết response.error tồn tại!
      // (TS knows response.error exists!)
      // 💡 TypeScript tự động biết response có property 'error' vì type là 'error'
      // (TypeScript automatically knows response has 'error' property because type is 'error')
      break;

    case 'loading':
      // ⏳ Nếu đang loading (If loading)
      // 💡 TypeScript narrow type: APIResponse → LoadingResponse
      // (TypeScript narrows type: APIResponse → LoadingResponse)
      console.log('Loading...');
      // 🎯 TS biết không có properties khác!
      // (TS knows no other properties exist!)
      // 💡 TypeScript biết LoadingResponse chỉ có 'type', không có properties khác
      // (TypeScript knows LoadingResponse only has 'type', no other properties)
      break;

    default:
      // 🛡️ Exhaustiveness check (Kiểm tra đầy đủ)
      // 💡 Nếu thêm case mới vào APIResponse mà quên xử lý → TypeScript báo lỗi
      // (If add new case to APIResponse but forget to handle → TypeScript reports error)
      const _exhaustive: never = response;
      // ✅ Đảm bảo xử lý hết các cases!
      // (Ensures all cases are handled!)
      // 💡 never type: Không thể assign bất kỳ giá trị nào
      // (never type: Cannot assign any value)
      // 💡 Nếu response không phải never → TypeScript báo lỗi (thiếu case)
      // (If response is not never → TypeScript reports error - missing case)
      return _exhaustive;
  }
}

// ✅ State machine with discriminated unions (State machine an toàn với discriminated unions)
type State = // 🎭 4 states khác nhau

    | { status: 'idle' } // 💭 Idle state - Chỉ có status
    | { status: 'loading'; startTime: number } // ⏳ Loading state - Có thêm startTime
    | { status: 'success'; data: string } // ✅ Success state - Có data
    | { status: 'error'; error: Error }; // ❌ Error state - Có error object

function reducer(state: State, action: Action): State {
  // 🔄 Reducer function
  switch (
    state.status // 🎯 Switch theo discriminator "status"
  ) {
    case 'idle': // 💭 Nếu đang idle
      if (action.type === 'FETCH_START') {
        // 🚀 Nếu action là bắt đầu fetch
        return { status: 'loading', startTime: Date.now() }; // ⏳ Chuyển sang loading
      }
      return state; // 🔄 Giữ nguyên state
    case 'loading': // ⏳ Nếu đang loading
      if (action.type === 'FETCH_SUCCESS') {
        // ✅ Nếu fetch thành công
        return { status: 'success', data: action.payload }; // ✅ Chuyển sang success
      }
      if (action.type === 'FETCH_ERROR') {
        // ❌ Nếu fetch lỗi
        return { status: 'error', error: action.error }; // ❌ Chuyển sang error
      }
      return state; // 🔄 Giữ nguyên state
    // ... other cases (Các cases khác)
  }
}
```

---

## 5. Declaration Files & Ambient Declarations

### **5.1. Declaration Files (.d.ts)**

```typescript
// ===================================================
// 📄 **DECLARATION FILES** (File .d.ts - Khai báo types)
// ===================================================

// types/global.d.ts (Khai báo global types)
declare global {
  // 🌐 Global namespace
  interface Window {
    // 💻 Mở rộng Window interface
    dataLayer: any[]; // 📦 Google Analytics dataLayer
    gtag: (...args: any[]) => void; // 📊 Google Analytics gtag function
    Stripe?: any; // 💳 Stripe SDK (optional)
  }

  namespace NodeJS {
    // 🟢 Node.js namespace
    interface ProcessEnv {
      // 🔑 Environment variables types
      VITE_API_URL: string; // 🌐 API URL (required)
      VITE_SENTRY_DSN: string; // 🚨 Sentry DSN (required)
      NODE_ENV: 'development' | 'production' | 'test'; // 🎯 Môi trường (literal types)
    }
  }
}

export {}; // ⚠️ Make this a module (Để file này là module, không phải script)

// ===================================================
// 🔧 **MODULE AUGMENTATION** (Mở rộng module có sẵn)
// ===================================================

// types/react-query.d.ts (Mở rộng react-query)
import '@tanstack/react-query'; // 📦 Import module cần mở rộng

declare module '@tanstack/react-query' {
  // 🔧 Declare module để mở rộng
  interface Register {
    // 📝 Mở rộng Register interface
    defaultError: { message: string; code: string }; // 🚨 Thêm default error type
  }
}

// ===================================================
// 📦 **THIRD-PARTY LIBRARY TYPES** (Types cho thư viện bên thứ 3)
// ===================================================

// types/legacy-lib.d.ts (Khai báo types cho library không có types)
declare module 'legacy-lib' {
  // 📦 Module không có types built-in
  export function doSomething(value: string): number; // 🛠️ Khai báo function

  export interface Config {
    // ⚙️ Khai báo interface
    apiKey: string; // 🔑 API key
    timeout: number; // ⏱️ Timeout
  }

  export class Client {
    // 🏭 Khai báo class
    constructor(config: Config); // 🛠️ Constructor
    request<T>(endpoint: string): Promise<T>; // 🌐 Method
  }
}

// ===================================================
// 🌐 **AMBIENT DECLARATIONS** (Khai báo môi trường)
// ===================================================

// types/env.d.ts (Types cho environment variables)
/// <reference types="vite/client" />  // 🔗 Reference Vite types

interface ImportMetaEnv {
  // 🔑 Vite environment variables
  readonly VITE_API_URL: string; // 🌐 API URL (readonly)
  readonly VITE_APP_TITLE: string; // 🏷️ App title (readonly)
}

interface ImportMeta {
  // 📦 ImportMeta interface
  readonly env: ImportMetaEnv; // 🔑 Env object
}
```

---

## 6. tsconfig.json Optimization

### **6.1. Strict Mode Configuration**

```json
// ===================================================
// ⚙️ **TSCONFIG.JSON** (Production-ready)
// ===================================================

{
  "compilerOptions": {
    // ✅ Language & Environment
    "target": "ES2022",
    "lib": ["ES2022", "DOM", "DOM.Iterable"],
    "jsx": "react-jsx",
    "module": "ESNext",
    "moduleResolution": "bundler",

    // ✅ Type Checking (STRICT MODE)
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,

    // ✅ Module Resolution
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"],
      "@utils/*": ["src/utils/*"],
      "@hooks/*": ["src/hooks/*"],
      "@types/*": ["src/types/*"]
    },
    "resolveJsonModule": true,
    "allowImportingTsExtensions": true,

    // ✅ Emit
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "removeComments": true,
    "importHelpers": true,
    "downlevelIteration": true,
    "isolatedModules": true,

    // ✅ Interop
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,

    // ✅ Type Acquisition
    "skipLibCheck": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist", "**/*.spec.ts", "**/*.test.ts"]
}
```

---

## 7. Branded Types & Nominal Typing

### **7.1. Branded Types**

```typescript
// ===================================================
// 🏷️ **BRANDED TYPES** (Nominal Typing Simulation - Ngăn trộn lẫn types)
// ===================================================

// ✅ Create branded types (Tạo branded types)
type Brand<K, T> = K & { __brand: T }; // 🏷️ Thêm brand property ảo

type UserId = Brand<string, 'UserId'>; // 🏷️ String nhưng có brand 'UserId'
type ProductId = Brand<string, 'ProductId'>; // 🏷️ String nhưng có brand 'ProductId'
type Email = Brand<string, 'Email'>; // 🏷️ String nhưng có brand 'Email'

// ✅ Constructor functions (Hàm tạo branded types)
function createUserId(id: string): UserId {
  // 🛠️ Tạo UserId
  return id as UserId; // 🎯 Cast thành UserId
}

function createEmail(email: string): Email {
  // 📧 Tạo Email
  if (!email.includes('@')) {
    // ❓ Validate có @
    throw new Error('Invalid email'); // ❌ Throw nếu không hợp lệ
  }
  return email as Email; // 🎯 Cast thành Email
}

// ✅ Type-safe functions (Hàm an toàn với branded types)
function getUser(id: UserId): Promise<User> {
  // 👤 Chỉ nhận UserId, KHÔNG nhận string thường!
  return fetch(`/api/users/${id}`).then((r) => r.json()); // 🌐 Fetch user
}

function getProduct(id: ProductId): Promise<Product> {
  // 🏭 Chỉ nhận ProductId
  return fetch(`/api/products/${id}`).then((r) => r.json()); // 🌐 Fetch product
}

// ✅ Usage (Sử dụng)
const userId = createUserId('user-123'); // 🏷️ Tạo UserId hợp lệ
const productId = 'product-456' as ProductId; // 🏷️ Cast thành ProductId

getUser(userId); // ✅ OK - Đúng type!
// getUser(productId); // ❌ Error: Type 'ProductId' is not assignable to type 'UserId' - Không thể dùng nhầm!

// ✅ Numeric branded types (Branded types cho số)
type PositiveNumber = Brand<number, 'Positive'>; // 🔢 Số dương
type Percentage = Brand<number, 'Percentage'>; // 📊 Phần trăm (0-100)

function createPercentage(value: number): Percentage {
  // 🛠️ Tạo Percentage
  if (value < 0 || value > 100) {
    // ❓ Validate 0-100
    throw new Error('Percentage must be between 0 and 100'); // ❌ Throw nếu ngoài phạm vi
  }
  return value as Percentage; // 🎯 Cast thành Percentage
}

function applyDiscount(price: number, discount: Percentage): number {
  // 💰 Áp dụng giảm giá
  return price * (1 - discount / 100); // 📊 Tính giá sau giảm
}

const discount = createPercentage(15); // 🏷️ Tạo 15% discount
applyDiscount(100, discount); // ✅ OK - Đúng type!
// applyDiscount(100, 15); // ❌ Error - Phải là Percentage, không phải number thường!
```

---

## 8. Real-World Use Cases

### **8.1. Type-Safe API Client**

```typescript
// ===================================================
// 🌐 **TYPE-SAFE API CLIENT** (API client an toàn với types)
// ===================================================

// Define API schema (Khai báo schema cho API)
interface APISchema {
  // 📋 API schema - Map endpoint → request/response types
  'GET /users': {
    // 👥 Endpoint: GET /users
    request: { limit?: number; offset?: number }; // ❓ Request params (optional)
    response: { users: User[]; total: number }; // 📦 Response type
  };
  'POST /users': {
    // ➕ Endpoint: POST /users
    request: { name: string; email: string }; // 📝 Request body (required)
    response: { user: User }; // 👤 Response type
  };
  'GET /users/:id': {
    // 🔍 Endpoint: GET /users/:id
    request: { id: string }; // 🔑 Request params
    response: { user: User }; // 👤 Response type
  };
}

// Extract method and path (Rút method và path từ endpoint string)
type APIEndpoint = keyof APISchema; // 🔑 'GET /users' | 'POST /users' | ...
type Method<E extends APIEndpoint> = E extends `${infer M} ${string}`
  ? M
  : never; // 🔍 Rút method
type Path<E extends APIEndpoint> = E extends `${string} ${infer P}` ? P : never; // 🗺️ Rút path

// Type-safe API client (API client với type safety hoàn toàn!)
class APIClient {
  // 🛠️ API Client class
  async request<E extends APIEndpoint>( // 🎯 Generic method
    endpoint: E, // 🌐 Endpoint (VD: 'GET /users')
    params: APISchema[E]['request'] // 📝 Params phải đúng type!
  ): Promise<APISchema[E]['response']> {
    // 📦 Response type tự động suy luận!
    const [method, path] = endpoint.split(' '); // 🔊 Tách method và path
    // ... implementation (Thực thi gọi API)
  }
}

// ✅ Usage (Sử dụng)
const api = new APIClient(); // 🛠️ Tạo instance

const { users } = await api.request('GET /users', { limit: 10 }); // ✅ Type-safe - TS biết users là User[]!
// await api.request('GET /users', { invalidParam: true }); // ❌ Error - invalidParam không tồn tại trong schema!
```

### **8.2. Type-Safe Event Emitter**

```typescript
// ===================================================
// 📡 **TYPE-SAFE EVENT EMITTER** (Event emitter an toàn)
// ===================================================

interface EventMap {
  // 📋 Event map - Map event name → data type
  'user:login': { userId: string; timestamp: number }; // 🔐 Login event
  'user:logout': { userId: string }; // 🚪 Logout event
  'cart:add': { productId: string; quantity: number }; // 🛒 Add to cart event
  'cart:remove': { productId: string }; // 🗑️ Remove from cart event
}

class TypedEventEmitter<Events extends Record<string, any>> {
  // 📦 Generic EventEmitter
  private listeners = new Map<keyof Events, Set<Function>>(); // 📋 Map lưu listeners

  on<K extends keyof Events>( // 🎯 Đăng ký listener
    event: K, // 🏷️ Event name (type-safe!)
    callback: (data: Events[K]) => void // 🔔 Callback với data type chính xác!
  ): () => void {
    // 🔄 Trả về unsubscribe function
    if (!this.listeners.has(event)) {
      // ❓ Nếu chưa có Set cho event này
      this.listeners.set(event, new Set()); // 🆕 Tạo Set mới
    }
    this.listeners.get(event)!.add(callback); // ➕ Thêm callback vào Set

    return () => this.off(event, callback); // 🔄 Trả về hàm unsubscribe
  }

  off<K extends keyof Events>( // 🗑️ Hủy đăng ký listener
    event: K, // 🏷️ Event name
    callback: (data: Events[K]) => void // 🔔 Callback cần xóa
  ): void {
    this.listeners.get(event)?.delete(callback); // 🗑️ Xóa callback
  }

  emit<K extends keyof Events>(event: K, data: Events[K]): void {
    // 📢 Phát event
    this.listeners.get(event)?.forEach((callback) => callback(data)); // 🔔 Gọi tất cả callbacks
  }
}

// ✅ Usage (Sử dụng)
const emitter = new TypedEventEmitter<EventMap>(); // 🛠️ Tạo emitter với EventMap

emitter.on('user:login', (data) => {
  // 🔔 Đăng ký listener
  console.log(data.userId, data.timestamp); // ✅ Autocomplete works! - TS biết data.userId và data.timestamp!
});

emitter.emit('user:login', { userId: '123', timestamp: Date.now() }); // ✅ Type-safe - Phải đúng structure!
// emitter.emit('user:login', { invalidProp: true }); // ❌ Error - invalidProp không tồn tại!
```

---

## 📚 **Best Practices Summary**

```typescript
// ===================================================
// ✅ **TYPESCRIPT BEST PRACTICES** (Thực hành tốt nhất)
// ===================================================

const TYPESCRIPT_BEST_PRACTICES = {
  // 📋 Danh sách best practices
  strictMode: [
    // ⚠️ Chế độ nghiêm ngặt
    '✅ Enable all strict flags in tsconfig.json', // 🔧 Bật tất cả strict flags
    '✅ Use "noImplicitAny" to catch type errors', // 🚫 Bắt lỗi any ngầm định
    '✅ Enable "strictNullChecks" for null safety', // 🛡️ Kiểm tra null/undefined
    '✅ Use "noUncheckedIndexedAccess" for array safety', // 📋 An toàn khi truy cập array
  ],

  typeDesign: [
    // 🎨 Thiết kế types
    '✅ Prefer interfaces for object shapes', // 📝 Dùng interfaces cho objects
    '✅ Use type aliases for unions/intersections', // 🔀 Dùng type cho unions
    '✅ Leverage discriminated unions for state machines', // 🎭 Dùng discriminated unions cho states
    '✅ Use branded types for domain primitives', // 🏷️ Dùng branded types cho domain
    '✅ Avoid "any" - use "unknown" instead', // ❌ Tránh any - dùng unknown
  ],

  generics: [
    // 📦 Generics
    '✅ Constrain generics with "extends"', // 🔒 Ràng buộc generics
    '✅ Infer types with conditional types', // 🔍 Dùng infer để rút types
    '✅ Use utility types (Partial, Pick, Omit)', // 🛠️ Dùng utility types built-in
    '✅ Create custom utility types for common patterns', // 🎨 Tạo utility types riêng
  ],

  performance: [
    // ⚡ Hiệu suất
    '✅ Use "skipLibCheck" for faster compilation', // 🚀 Compile nhanh hơn
    '✅ Use "incremental" builds', // 🔄 Build tăng dần
    '✅ Split large types into smaller composable ones', // 🧩 Chia nhỏ types
    '✅ Avoid deep recursion in mapped types', // ⚠️ Tránh đệ quy sâu
  ],
};
```

---

**🎯 Remember:** "TypeScript's type system is Turing complete - you can compute types at compile time!"
