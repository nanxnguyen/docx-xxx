# 🔷 Q52: TypeScript Advanced Patterns - Generics, Utility Types, Advanced Patterns

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"TypeScript advanced = Generics, Utility Types, Mapped Types, Conditional Types, Type Guards.**

**🔧 Core Advanced Concepts:**

1. **Generics**:
   - **Purpose**: Type-safe reusable functions/components.
   - **Constraints**: `<T extends Type>` → limit T to specific types.
   ```ts
   function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
     return obj[key]; // Type-safe property access
   }
   const user = { name: 'Alice', age: 30 };
   getProperty(user, 'name'); // Type: string
   ```

2. **Utility Types** (Built-in):
   - **`Partial<T>`**: Tất cả properties optional.
   - **`Required<T>`**: Tất cả properties required.
   - **`Pick<T, K>`**: Lấy subset properties.
   - **`Omit<T, K>`**: Loại bỏ properties.
   - **`Record<K, V>`**: Object với keys K, values V.
   - **`Readonly<T>`**: Immutable properties.
   ```ts
   type User = { id: number; name: string; email: string };
   type PartialUser = Partial<User>; // All optional
   type UserName = Pick<User, 'id' | 'name'>; // Only id, name
   type NoEmail = Omit<User, 'email'>; // Exclude email
   ```

3. **Mapped Types**:
   - Transform existing types.
   ```ts
   type Readonly<T> = { readonly [K in keyof T]: T[K] };
   type Optional<T> = { [K in keyof T]?: T[K] };
   ```

4. **Conditional Types**:
   - `T extends U ? X : Y` → type-level if-else.
   ```ts
   type IsString<T> = T extends string ? true : false;
   type A = IsString<string>; // true
   type B = IsString<number>; // false
   ```

5. **Template Literal Types** (TS 4.1+):
   - String manipulation at type level.
   ```ts
   type EventName<T extends string> = `on${Capitalize<T>}`;
   type ClickEvent = EventName<'click'>; // "onClick"
   ```

6. **Type Guards**:
   - Runtime type checking → narrow types.
   ```ts
   function isString(value: unknown): value is string {
     return typeof value === 'string';
   }
   if (isString(value)) {
     value.toUpperCase(); // TS knows value is string
   }
   ```

7. **Discriminated Unions**:
   - Type-safe state machines.
   ```ts
   type State = 
     | { status: 'loading' }
     | { status: 'success'; data: string }
     | { status: 'error'; error: Error };
   
   function handle(state: State) {
     switch (state.status) {
       case 'loading': return 'Loading...';
       case 'success': return state.data; // TS knows data exists
       case 'error': return state.error.message;
     }
   }
   ```

**🎯 Real-World Use Cases:**

1. **API Response Typing**:
   ```ts
   type ApiResponse<T> = 
     | { success: true; data: T }
     | { success: false; error: string };
   
   async function fetchUser(): Promise<ApiResponse<User>> {
     // ...
   }
   ```

2. **Form State**:
   ```ts
   type FormState<T> = {
     values: T;
     errors: Partial<Record<keyof T, string>>;
     touched: Partial<Record<keyof T, boolean>>;
   };
   ```

3. **Branded Types** (Nominal Typing):
   - Prevent mixing similar types.
   ```ts
   type UserId = string & { __brand: 'UserId' };
   type ProductId = string & { __brand: 'ProductId' };
   
   function getUser(id: UserId) { /*...*/ }
   const userId = '123' as UserId;
   getUser(userId); // OK
   // getUser('456'); // Error: string not assignable to UserId
   ```

**⚠️ Common Mistakes:**
- **any overuse**: Defeat purpose of TypeScript → dùng `unknown` + type guards.
- **Type assertions abuse**: `as` bypass type checking → dùng type guards instead.
- **Missing generic constraints**: `<T>` too broad → dùng `<T extends Type>`.

**💡 Senior Insights:**
- **infer keyword**: Extract types from other types.
  ```ts
  type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
  ```
- **Const assertions**: `as const` → literal types instead of widening.
  ```ts
  const colors = ['red', 'blue'] as const; // Type: readonly ["red", "blue"]
  ```
- **tsconfig strict mode**: Enable all strict checks (`strict: true`) → catch bugs early.
- **Declaration files**: `.d.ts` for third-party libraries không có types.

---

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)  
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

// ❌ BAD: No constraints
function getProperty<T>(obj: T, key: string) {
  return obj[key]; // Error: Element implicitly has 'any' type
}

// ✅ GOOD: Constrained generic
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key]; // Type-safe!
}

const user = { name: 'Alice', age: 30 };
const name = getProperty(user, 'name');    // Type: string
const age = getProperty(user, 'age');      // Type: number
// getProperty(user, 'invalid'); // ❌ Error: Argument of type '"invalid"' is not assignable

// ===================================================
// 🎯 **EXTENDING MULTIPLE CONSTRAINTS**
// ===================================================

interface Identifiable {
  id: string | number;
}

interface Timestamped {
  createdAt: Date;
  updatedAt: Date;
}

// ✅ Generic with multiple constraints
function updateEntity<T extends Identifiable & Timestamped>(
  entity: T,
  updates: Partial<T>
): T {
  return {
    ...entity,
    ...updates,
    updatedAt: new Date(), // Type-safe access
  };
}

// ===================================================
// 🔄 **CONDITIONAL TYPES**
// ===================================================

// Basic conditional type
type IsString<T> = T extends string ? true : false;

type A = IsString<string>;  // true
type B = IsString<number>;  // false

// ✅ Extract return type from function
type ReturnTypeOf<T> = T extends (...args: any[]) => infer R ? R : never;

type Func = () => { name: string };
type Result = ReturnTypeOf<Func>; // { name: string }

// ✅ Unwrap Promise type
type Awaited<T> = T extends Promise<infer U> ? U : T;

type AsyncData = Promise<{ data: string }>;
type SyncData = Awaited<AsyncData>; // { data: string }

// ✅ Recursive conditional types
type DeepReadonly<T> = {
  readonly [K in keyof T]: T[K] extends object
    ? DeepReadonly<T[K]>
    : T[K];
};

interface Config {
  server: {
    port: number;
    host: string;
  };
  database: {
    url: string;
  };
}

type ReadonlyConfig = DeepReadonly<Config>;
// All properties (including nested) are readonly
```

### **1.2. Advanced Conditional Types**

```typescript
// ===================================================
// 🎨 **DISTRIBUTIVE CONDITIONAL TYPES**
// ===================================================

type ToArray<T> = T extends any ? T[] : never;

type StrOrNum = string | number;
type ArrOfStrOrNum = ToArray<StrOrNum>; // string[] | number[] (distributive)

// ✅ Non-distributive version
type ToArrayNonDist<T> = [T] extends [any] ? T[] : never;
type ArrOfStrOrNumNonDist = ToArrayNonDist<StrOrNum>; // (string | number)[]

// ===================================================
// 🔍 **INFER KEYWORD** (Extract types)
// ===================================================

// Extract function parameters
type Parameters<T> = T extends (...args: infer P) => any ? P : never;

type Params = Parameters<(a: string, b: number) => void>; // [string, number]

// Extract first array element type
type FirstElement<T> = T extends [infer F, ...any[]] ? F : never;

type First = FirstElement<[string, number, boolean]>; // string

// Extract object property types
type ExtractPropType<T, K extends keyof T> = T[K];

interface User {
  id: number;
  profile: {
    name: string;
    avatar: string;
  };
}

type ProfileType = ExtractPropType<User, 'profile'>; // { name: string; avatar: string }
```

---

## 2. Utility Types Deep Dive

### **2.1. Built-in Utility Types**

```typescript
// ===================================================
// 🛠️ **BUILT-IN UTILITY TYPES**
// ===================================================

interface Todo {
  id: number;
  title: string;
  description: string;
  completed: boolean;
  createdAt: Date;
}

// ✅ Partial<T> - All properties optional
type PartialTodo = Partial<Todo>;
const updateTodo = (id: number, updates: Partial<Todo>) => { /* ... */ };

// ✅ Required<T> - All properties required
type RequiredTodo = Required<Partial<Todo>>;

// ✅ Readonly<T> - All properties readonly
type ReadonlyTodo = Readonly<Todo>;

// ✅ Pick<T, K> - Select specific properties
type TodoPreview = Pick<Todo, 'id' | 'title' | 'completed'>;

// ✅ Omit<T, K> - Exclude specific properties
type TodoWithoutDates = Omit<Todo, 'createdAt'>;

// ✅ Record<K, T> - Object with specific keys and value type
type TodoMap = Record<number, Todo>;
const todos: TodoMap = {
  1: { id: 1, title: 'Learn TS', /* ... */ },
  2: { id: 2, title: 'Build App', /* ... */ },
};

// ✅ Exclude<T, U> - Exclude types from union
type Primitive = string | number | boolean | null | undefined;
type NonNullable = Exclude<Primitive, null | undefined>; // string | number | boolean

// ✅ Extract<T, U> - Extract types from union
type StringOrNumber = Extract<string | number | boolean, string | number>; // string | number

// ✅ NonNullable<T> - Remove null and undefined
type MaybeString = string | null | undefined;
type DefiniteString = NonNullable<MaybeString>; // string

// ✅ ReturnType<T> - Get function return type
const getUser = () => ({ id: 1, name: 'Alice' });
type User = ReturnType<typeof getUser>; // { id: number; name: string }

// ✅ Parameters<T> - Get function parameters
const createUser = (name: string, age: number) => ({ name, age });
type CreateUserParams = Parameters<typeof createUser>; // [string, number]

// ✅ InstanceType<T> - Get instance type of constructor
class Product {
  constructor(public name: string, public price: number) {}
}
type ProductInstance = InstanceType<typeof Product>; // Product
```

### **2.2. Custom Utility Types**

```typescript
// ===================================================
// 🎨 **CUSTOM UTILITY TYPES**
// ===================================================

// ✅ DeepPartial - Recursive partial
type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

interface Config {
  server: {
    port: number;
    host: string;
    ssl: {
      enabled: boolean;
      cert: string;
    };
  };
}

const updateConfig = (config: DeepPartial<Config>) => {
  // Can update any nested property
};

updateConfig({ server: { ssl: { enabled: true } } }); // ✅ Valid

// ✅ Nullable - Add null to all properties
type Nullable<T> = {
  [K in keyof T]: T[K] | null;
};

type NullableUser = Nullable<{ name: string; age: number }>;
// { name: string | null; age: number | null }

// ✅ Optional - Specific properties optional
type Optional<T, K extends keyof T> = Omit<T, K> & Partial<Pick<T, K>>;

type UserWithOptionalEmail = Optional<
  { name: string; email: string; age: number },
  'email'
>;
// { name: string; age: number; email?: string }

// ✅ RequireAtLeastOne - At least one property required
type RequireAtLeastOne<T, Keys extends keyof T = keyof T> = Pick<T, Exclude<keyof T, Keys>> &
  {
    [K in Keys]-?: Required<Pick<T, K>> & Partial<Pick<T, Exclude<Keys, K>>>;
  }[Keys];

type ContactInfo = {
  email?: string;
  phone?: string;
  address?: string;
};

type ValidContact = RequireAtLeastOne<ContactInfo>;
// Must have at least one of email, phone, or address

// ✅ Mutable - Remove readonly
type Mutable<T> = {
  -readonly [K in keyof T]: T[K];
};

type MutableConfig = Mutable<ReadonlyConfig>;

// ✅ PromiseType - Extract Promise value type
type PromiseType<T> = T extends Promise<infer U> ? U : T;

type ApiResponse = Promise<{ data: string }>;
type Data = PromiseType<ApiResponse>; // { data: string }
```

---

## 3. Mapped & Template Literal Types

### **3.1. Mapped Types**

```typescript
// ===================================================
// 🗺️ **MAPPED TYPES**
// ===================================================

// ✅ Basic mapped type
type Readonly<T> = {
  readonly [K in keyof T]: T[K];
};

// ✅ Add prefix to keys
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

interface User {
  name: string;
  age: number;
}

type UserGetters = Getters<User>;
// {
//   getName: () => string;
//   getAge: () => number;
// }

// ✅ Filter properties by type
type FilterByType<T, ValueType> = {
  [K in keyof T as T[K] extends ValueType ? K : never]: T[K];
};

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
}

type StringProperties = FilterByType<Product, string>;
// { name: string; description: string }

type NumberProperties = FilterByType<Product, number>;
// { id: number; price: number }

// ✅ Transform property types
type Stringify<T> = {
  [K in keyof T]: string;
};

type StringifiedProduct = Stringify<Product>;
// { id: string; name: string; price: string; description: string }
```

### **3.2. Template Literal Types**

```typescript
// ===================================================
// 📝 **TEMPLATE LITERAL TYPES** (TypeScript 4.1+)
// ===================================================

// ✅ Basic template literals
type Color = 'red' | 'blue' | 'green';
type Quantity = 'one' | 'two' | 'three';

type ColoredQuantity = `${Quantity} ${Color}`;
// 'one red' | 'one blue' | 'one green' | 'two red' | ...

// ✅ Event handler types
type EventNames = 'click' | 'focus' | 'blur';
type EventHandlers = {
  [K in EventNames as `on${Capitalize<K>}`]: (event: Event) => void;
};

// {
//   onClick: (event: Event) => void;
//   onFocus: (event: Event) => void;
//   onBlur: (event: Event) => void;
// }

// ✅ CSS properties
type CSSProp = 'margin' | 'padding';
type Direction = 'top' | 'right' | 'bottom' | 'left';

type CSSProperties = `${CSSProp}-${Direction}`;
// 'margin-top' | 'margin-right' | ... | 'padding-left'

// ✅ API routes
type HTTPMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';
type Resource = 'users' | 'products' | 'orders';

type APIRoute = `${Lowercase<HTTPMethod>} /api/${Resource}`;
// 'get /api/users' | 'post /api/users' | ...

// ✅ Type-safe path builder
type Join<T extends string[], D extends string = '/'> = T extends [
  infer F extends string,
  ...infer R extends string[]
]
  ? R extends []
    ? F
    : `${F}${D}${Join<R, D>}`
  : '';

type Path = Join<['api', 'v1', 'users', 'profile']>; // 'api/v1/users/profile'
```

---

## 4. Type Guards & Discriminated Unions

### **4.1. Type Guards**

```typescript
// ===================================================
// 🛡️ **TYPE GUARDS**
// ===================================================

// ✅ User-defined type guard
interface Cat {
  meow: () => void;
}

interface Dog {
  bark: () => void;
}

function isCat(animal: Cat | Dog): animal is Cat {
  return 'meow' in animal;
}

function makeSound(animal: Cat | Dog) {
  if (isCat(animal)) {
    animal.meow(); // TypeScript knows it's Cat
  } else {
    animal.bark(); // TypeScript knows it's Dog
  }
}

// ✅ Type predicate with generics
function isOfType<T>(
  value: unknown,
  check: (val: any) => boolean
): value is T {
  return check(value);
}

const isString = (val: unknown): val is string => typeof val === 'string';
const isNumber = (val: unknown): val is number => typeof val === 'number';

// ✅ Array type guard
function isStringArray(value: unknown): value is string[] {
  return Array.isArray(value) && value.every(item => typeof item === 'string');
}

// ✅ Non-null assertion guard
function assertDefined<T>(value: T | null | undefined): asserts value is T {
  if (value === null || value === undefined) {
    throw new Error('Value is null or undefined');
  }
}

const user: User | null = getUser();
assertDefined(user);
user.name; // ✅ TypeScript knows user is not null
```

### **4.2. Discriminated Unions**

```typescript
// ===================================================
// 🎭 **DISCRIMINATED UNIONS** (Tagged Unions)
// ===================================================

// ✅ API Response types
interface SuccessResponse {
  type: 'success';
  data: { id: number; name: string };
}

interface ErrorResponse {
  type: 'error';
  error: { code: string; message: string };
}

interface LoadingResponse {
  type: 'loading';
}

type APIResponse = SuccessResponse | ErrorResponse | LoadingResponse;

function handleResponse(response: APIResponse) {
  switch (response.type) {
    case 'success':
      console.log(response.data); // ✅ TypeScript knows data exists
      break;
    case 'error':
      console.error(response.error); // ✅ TypeScript knows error exists
      break;
    case 'loading':
      console.log('Loading...'); // ✅ No extra properties
      break;
    default:
      const _exhaustive: never = response; // ✅ Exhaustiveness check
      return _exhaustive;
  }
}

// ✅ State machine with discriminated unions
type State =
  | { status: 'idle' }
  | { status: 'loading'; startTime: number }
  | { status: 'success'; data: string }
  | { status: 'error'; error: Error };

function reducer(state: State, action: Action): State {
  switch (state.status) {
    case 'idle':
      if (action.type === 'FETCH_START') {
        return { status: 'loading', startTime: Date.now() };
      }
      return state;
    case 'loading':
      if (action.type === 'FETCH_SUCCESS') {
        return { status: 'success', data: action.payload };
      }
      if (action.type === 'FETCH_ERROR') {
        return { status: 'error', error: action.error };
      }
      return state;
    // ... other cases
  }
}
```

---

## 5. Declaration Files & Ambient Declarations

### **5.1. Declaration Files (.d.ts)**

```typescript
// ===================================================
// 📄 **DECLARATION FILES**
// ===================================================

// types/global.d.ts
declare global {
  interface Window {
    dataLayer: any[];
    gtag: (...args: any[]) => void;
    Stripe?: any;
  }

  namespace NodeJS {
    interface ProcessEnv {
      VITE_API_URL: string;
      VITE_SENTRY_DSN: string;
      NODE_ENV: 'development' | 'production' | 'test';
    }
  }
}

export {}; // Make this a module

// ===================================================
// 🔧 **MODULE AUGMENTATION**
// ===================================================

// types/react-query.d.ts
import '@tanstack/react-query';

declare module '@tanstack/react-query' {
  interface Register {
    defaultError: { message: string; code: string };
  }
}

// ===================================================
// 📦 **THIRD-PARTY LIBRARY TYPES**
// ===================================================

// types/legacy-lib.d.ts
declare module 'legacy-lib' {
  export function doSomething(value: string): number;
  
  export interface Config {
    apiKey: string;
    timeout: number;
  }
  
  export class Client {
    constructor(config: Config);
    request<T>(endpoint: string): Promise<T>;
  }
}

// ===================================================
// 🌐 **AMBIENT DECLARATIONS**
// ===================================================

// types/env.d.ts
/// <reference types="vite/client" />

interface ImportMetaEnv {
  readonly VITE_API_URL: string;
  readonly VITE_APP_TITLE: string;
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
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
// 🏷️ **BRANDED TYPES** (Nominal Typing Simulation)
// ===================================================

// ✅ Create branded types
type Brand<K, T> = K & { __brand: T };

type UserId = Brand<string, 'UserId'>;
type ProductId = Brand<string, 'ProductId'>;
type Email = Brand<string, 'Email'>;

// ✅ Constructor functions
function createUserId(id: string): UserId {
  return id as UserId;
}

function createEmail(email: string): Email {
  if (!email.includes('@')) {
    throw new Error('Invalid email');
  }
  return email as Email;
}

// ✅ Type-safe functions
function getUser(id: UserId): Promise<User> {
  return fetch(`/api/users/${id}`).then(r => r.json());
}

function getProduct(id: ProductId): Promise<Product> {
  return fetch(`/api/products/${id}`).then(r => r.json());
}

// ✅ Usage
const userId = createUserId('user-123');
const productId = 'product-456' as ProductId;

getUser(userId); // ✅ OK
// getUser(productId); // ❌ Error: Type 'ProductId' is not assignable to type 'UserId'

// ✅ Numeric branded types
type PositiveNumber = Brand<number, 'Positive'>;
type Percentage = Brand<number, 'Percentage'>;

function createPercentage(value: number): Percentage {
  if (value < 0 || value > 100) {
    throw new Error('Percentage must be between 0 and 100');
  }
  return value as Percentage;
}

function applyDiscount(price: number, discount: Percentage): number {
  return price * (1 - discount / 100);
}

const discount = createPercentage(15);
applyDiscount(100, discount); // ✅ OK
// applyDiscount(100, 15); // ❌ Error
```

---

## 8. Real-World Use Cases

### **8.1. Type-Safe API Client**

```typescript
// ===================================================
// 🌐 **TYPE-SAFE API CLIENT**
// ===================================================

// Define API schema
interface APISchema {
  'GET /users': {
    request: { limit?: number; offset?: number };
    response: { users: User[]; total: number };
  };
  'POST /users': {
    request: { name: string; email: string };
    response: { user: User };
  };
  'GET /users/:id': {
    request: { id: string };
    response: { user: User };
  };
}

// Extract method and path
type APIEndpoint = keyof APISchema;
type Method<E extends APIEndpoint> = E extends `${infer M} ${string}` ? M : never;
type Path<E extends APIEndpoint> = E extends `${string} ${infer P}` ? P : never;

// Type-safe API client
class APIClient {
  async request<E extends APIEndpoint>(
    endpoint: E,
    params: APISchema[E]['request']
  ): Promise<APISchema[E]['response']> {
    const [method, path] = endpoint.split(' ');
    // ... implementation
  }
}

// ✅ Usage
const api = new APIClient();

const { users } = await api.request('GET /users', { limit: 10 }); // ✅ Type-safe
// await api.request('GET /users', { invalidParam: true }); // ❌ Error
```

### **8.2. Type-Safe Event Emitter**

```typescript
// ===================================================
// 📡 **TYPE-SAFE EVENT EMITTER**
// ===================================================

interface EventMap {
  'user:login': { userId: string; timestamp: number };
  'user:logout': { userId: string };
  'cart:add': { productId: string; quantity: number };
  'cart:remove': { productId: string };
}

class TypedEventEmitter<Events extends Record<string, any>> {
  private listeners = new Map<keyof Events, Set<Function>>();

  on<K extends keyof Events>(
    event: K,
    callback: (data: Events[K]) => void
  ): () => void {
    if (!this.listeners.has(event)) {
      this.listeners.set(event, new Set());
    }
    this.listeners.get(event)!.add(callback);

    return () => this.off(event, callback);
  }

  off<K extends keyof Events>(
    event: K,
    callback: (data: Events[K]) => void
  ): void {
    this.listeners.get(event)?.delete(callback);
  }

  emit<K extends keyof Events>(event: K, data: Events[K]): void {
    this.listeners.get(event)?.forEach(callback => callback(data));
  }
}

// ✅ Usage
const emitter = new TypedEventEmitter<EventMap>();

emitter.on('user:login', (data) => {
  console.log(data.userId, data.timestamp); // ✅ Autocomplete works!
});

emitter.emit('user:login', { userId: '123', timestamp: Date.now() }); // ✅ Type-safe
// emitter.emit('user:login', { invalidProp: true }); // ❌ Error
```

---

## 📚 **Best Practices Summary**

```typescript
// ===================================================
// ✅ **TYPESCRIPT BEST PRACTICES**
// ===================================================

const TYPESCRIPT_BEST_PRACTICES = {
  strictMode: [
    '✅ Enable all strict flags in tsconfig.json',
    '✅ Use "noImplicitAny" to catch type errors',
    '✅ Enable "strictNullChecks" for null safety',
    '✅ Use "noUncheckedIndexedAccess" for array safety',
  ],

  typeDesign: [
    '✅ Prefer interfaces for object shapes',
    '✅ Use type aliases for unions/intersections',
    '✅ Leverage discriminated unions for state machines',
    '✅ Use branded types for domain primitives',
    '✅ Avoid "any" - use "unknown" instead',
  ],

  generics: [
    '✅ Constrain generics with "extends"',
    '✅ Infer types with conditional types',
    '✅ Use utility types (Partial, Pick, Omit)',
    '✅ Create custom utility types for common patterns',
  ],

  performance: [
    '✅ Use "skipLibCheck" for faster compilation',
    '✅ Use "incremental" builds',
    '✅ Split large types into smaller composable ones',
    '✅ Avoid deep recursion in mapped types',
  ],
};
```

---

**🎯 Remember:** "TypeScript's type system is Turing complete - you can compute types at compile time!"
