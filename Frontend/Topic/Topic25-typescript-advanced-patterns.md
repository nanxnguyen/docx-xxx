# 🔷 Topic 25: TypeScript Advanced Patterns - Generics, Utility Types, Advanced Patterns

## 1. ⭐ Senior/Staff Summary

TypeScript advanced không phải là viết type thật phức tạp. Mục tiêu chính là **mô hình hóa constraint của domain**, bắt lỗi sớm ở compile-time, và giữ API boundary rõ ràng giữa UI, data fetching, form, auth, cache và backend contract.

Các key cần nắm:

- **Generics:** viết function/component/hook tái sử dụng nhưng vẫn type-safe.
- **Generic constraints:** giới hạn `T` bằng `extends`, `keyof`, indexed access để tránh generic quá rộng.
- **Conditional types + `infer`:** viết logic if/else ở type level và trích xuất type từ function, promise, array, object.
- **Utility types:** dùng `Partial`, `Required`, `Pick`, `Omit`, `Record`, `Readonly`, `ReturnType`, `Parameters`, `Awaited` đúng ngữ cảnh.
- **Mapped types:** biến đổi shape của object type, ví dụ readonly/optional/error map.
- **Template literal types:** tạo union string type cho routes, events, i18n keys, analytics names.
- **Type guards:** kiểm tra runtime để narrow từ `unknown` sang type an toàn.
- **Discriminated unions:** mô hình hóa state machine như loading/success/error.
- **Declaration files:** khai báo type cho thư viện hoặc global API chưa có type.
- **Strict `tsconfig`:** bật strict mode để tránh bug bị che bởi `any`, nullable và implicit any.
- **Branded types:** phân biệt các primitive giống nhau như `UserId`, `ProductId`, `OrderId`.

⚠️ Senior point: TypeScript chỉ kiểm tra compile-time. Dữ liệu từ API, localStorage, query string, postMessage hoặc user input vẫn cần runtime validation.

## 2. 🧠 Key Mental Model or Key Points

- TypeScript là **static contract layer**, không thay thế validation runtime.
- Generic tốt khi type phụ thuộc input; generic tệ khi chỉ làm code khó đọc hơn.
- `unknown` là boundary type tốt hơn `any`: phải validate trước khi dùng.
- `as` là escape hatch, không phải strategy. Nếu dùng nhiều `as`, thường boundary hoặc model đang yếu.
- Advanced types nên phục vụ API dễ dùng, không biến codebase thành “type puzzle”.
- Trong React, type tốt giúp props, hooks, form state, async state và event handlers rõ hơn, nhưng runtime behavior vẫn do JavaScript quyết định.
- Với team lớn, TypeScript mạnh nhất khi đi cùng strict `tsconfig`, API schema validation, typed query/mutation layer và naming convention nhất quán.

## 3. 📚 Main Concepts

### 3.1. Generics và Generic Constraints

Generic cho phép type phụ thuộc vào input mà không mất thông tin.

❌ Generic quá rộng:

```ts
function getProperty<T>(obj: T, key: string) {
  return obj[key];
  // Error: TypeScript không biết key có tồn tại trong obj không.
}
```

✅ Constraint bằng `keyof`:

```ts
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

const user = { name: "Alice", age: 30 };

const name = getProperty(user, "name"); // string
const age = getProperty(user, "age"); // number
// getProperty(user, "email"); // Error
```

Multiple constraints:

```ts
interface Identifiable {
  id: string | number;
}

interface Timestamped {
  createdAt: Date;
  updatedAt: Date;
}

function touchEntity<T extends Identifiable & Timestamped>(entity: T): T {
  return {
    ...entity,
    updatedAt: new Date(),
  };
}
```

💡 Rule thực tế: nếu function cần đọc field cụ thể, hãy constraint generic bằng field đó thay vì dùng `any`.

### 3.2. Conditional Types và `infer`

Conditional type là if/else ở type level:

```ts
type IsString<T> = T extends string ? true : false;

type A = IsString<string>; // true
type B = IsString<number>; // false
```

Dùng `infer` để trích xuất type:

```ts
type UnwrapPromise<T> = T extends Promise<infer R> ? R : T;

type UserPromise = Promise<{ id: string; name: string }>;
type User = UnwrapPromise<UserPromise>;
```

Trích xuất return type của async function:

```ts
async function fetchUser() {
  return { id: "u1", name: "Ada" };
}

type FetchUserResult = Awaited<ReturnType<typeof fetchUser>>;
```

⚠️ Conditional types phân phối trên union:

```ts
type ToArray<T> = T extends unknown ? T[] : never;

type Result = ToArray<string | number>;
// string[] | number[]
```

Nếu không muốn distributive behavior, bọc bằng tuple:

```ts
type ToArrayNonDistributive<T> = [T] extends [unknown] ? T[] : never;

type Result = ToArrayNonDistributive<string | number>;
// (string | number)[]
```

### 3.3. Utility Types Deep Dive

Built-in utility types giúp biến đổi type phổ biến mà không phải tự viết lại.

```ts
type User = {
  id: string;
  name: string;
  email: string;
  role: "admin" | "user";
  createdAt: string;
};

type CreateUserInput = Pick<User, "name" | "email" | "role">;
type UpdateUserInput = Partial<Pick<User, "name" | "email" | "role">>;
type PublicUser = Omit<User, "email">;
type UsersById = Record<string, User>;
type FrozenUser = Readonly<User>;
```

Chọn utility theo intent:

| Utility | Dùng khi | Lưu ý |
|---|---|---|
| `Partial<T>` | update payload, draft form | Không nên dùng cho object phải đầy đủ |
| `Required<T>` | normalize config/defaults | Có thể che giấu field optional có ý nghĩa |
| `Pick<T, K>` | tạo DTO nhỏ hơn | Tốt cho API input/output |
| `Omit<T, K>` | loại field nhạy cảm/nội bộ | Cẩn thận khi domain thay đổi |
| `Record<K, V>` | dictionary/map plain object | Key là string/number/symbol |
| `Readonly<T>` | tránh mutate ngoài ý muốn | Shallow readonly |
| `ReturnType<T>` | lấy return type từ function | Hữu ích cho hooks/selectors |
| `Parameters<T>` | lấy args type từ function | Hữu ích cho wrapper/decorator |
| `Awaited<T>` | unwrap Promise | Hợp với async API |

Custom utility type nên ngắn và có use case rõ:

```ts
type Nullable<T> = T | null;

type DeepPartial<T> = {
  [K in keyof T]?: T[K] extends object ? DeepPartial<T[K]> : T[K];
};

type ValueOf<T> = T[keyof T];
```

⚠️ `DeepPartial` dễ làm type quá lỏng nếu dùng ở API boundary. Với form draft thì hợp lý hơn.

### 3.4. Mapped Types

Mapped type biến đổi từng property trong object type.

```ts
type Optional<T> = {
  [K in keyof T]?: T[K];
};

type ReadonlyFields<T> = {
  readonly [K in keyof T]: T[K];
};
```

Ví dụ thực tế cho form validation:

```ts
type FormErrors<T> = Partial<Record<keyof T, string>>;
type FormTouched<T> = Partial<Record<keyof T, boolean>>;

type FormState<T> = {
  values: T;
  errors: FormErrors<T>;
  touched: FormTouched<T>;
};
```

Mapped type có thể đổi tên key bằng `as`:

```ts
type ApiGetters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K];
};

type UserGetters = ApiGetters<{
  name: string;
  email: string;
}>;
// { getName: () => string; getEmail: () => string }
```

### 3.5. Template Literal Types

Template literal types tạo string union có cấu trúc.

```ts
type EventName<T extends string> = `on${Capitalize<T>}`;

type ClickEvent = EventName<"click">; // "onClick"
```

Ứng dụng frontend:

```ts
type Resource = "user" | "product" | "order";
type Action = "created" | "updated" | "deleted";

type AnalyticsEvent = `${Resource}.${Action}`;

function track(event: AnalyticsEvent) {
  // send analytics
}

track("user.created");
// track("users.create"); // Error
```

Typed route params:

```ts
type Route = "/users/:id" | "/products/:sku";
type RouteName<T extends Route> = T extends `/users/${string}` ? "user" : "product";
```

💡 Dùng cho event names, i18n keys, CSS variant names, route names. Không nên cố parse mọi thứ bằng type-level string nếu runtime parser đã rõ hơn.

### 3.6. Type Guards

Type guard kiểm tra runtime và giúp TypeScript narrow type.

```ts
function isString(value: unknown): value is string {
  return typeof value === "string";
}

function normalize(value: unknown) {
  if (isString(value)) {
    return value.trim().toLowerCase();
  }

  return "";
}
```

Object guard:

```ts
type User = {
  id: string;
  name: string;
};

function isUser(value: unknown): value is User {
  if (typeof value !== "object" || value === null) return false;

  const candidate = value as Record<string, unknown>;

  return typeof candidate.id === "string" && typeof candidate.name === "string";
}
```

⚠️ Guard phải kiểm tra runtime thật. Một guard viết sai nguy hiểm không kém `as`.

```ts
function isUserUnsafe(value: unknown): value is User {
  return true; // ❌ TypeScript tin, runtime vẫn có thể crash
}
```

Trong production, API response phức tạp nên dùng schema validation như Zod, Valibot, Yup hoặc io-ts thay vì tự viết guard dài.

### 3.7. Discriminated Unions

Discriminated union dùng một field chung để mô hình hóa state machine an toàn.

```ts
type AsyncState<T> =
  | { status: "idle" }
  | { status: "loading" }
  | { status: "success"; data: T }
  | { status: "error"; error: Error };

function renderUser(state: AsyncState<{ name: string }>) {
  switch (state.status) {
    case "idle":
      return "Idle";
    case "loading":
      return "Loading";
    case "success":
      return state.data.name;
    case "error":
      return state.error.message;
  }
}
```

Exhaustiveness check:

```ts
function assertNever(value: never): never {
  throw new Error(`Unexpected value: ${JSON.stringify(value)}`);
}

function render<T>(state: AsyncState<T>) {
  switch (state.status) {
    case "idle":
    case "loading":
      return null;
    case "success":
      return state.data;
    case "error":
      return state.error.message;
    default:
      return assertNever(state);
  }
}
```

💡 Đây là pattern rất mạnh cho React UI state vì tránh boolean soup như `isLoading`, `isError`, `data`, `error` không đồng bộ với nhau.

### 3.8. Declaration Files và Ambient Declarations

`.d.ts` dùng để khai báo type cho code JavaScript, thư viện thiếu type hoặc global API.

Ví dụ khai báo module thiếu type:

```ts
// src/types/legacy-analytics.d.ts
declare module "legacy-analytics" {
  export function track(event: string, payload?: Record<string, unknown>): void;
}
```

Khai báo global:

```ts
// src/types/window.d.ts
export {};

declare global {
  interface Window {
    __APP_VERSION__: string;
  }
}
```

⚠️ Tránh khai báo quá rộng:

```ts
declare module "*"; // ❌ Che mất lỗi import/type thật
```

### 3.9. `tsconfig.json` Strict Mode

Nền tảng TypeScript tốt bắt đầu từ `tsconfig`.

```json
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "noImplicitOverride": true,
    "useUnknownInCatchVariables": true
  }
}
```

Ý nghĩa thực tế:

- `strict`: bật nhóm kiểm tra nghiêm ngặt.
- `strictNullChecks`: không cho `null`/`undefined` trôi qua im lặng.
- `noUncheckedIndexedAccess`: `obj[key]` và `arr[index]` có thể là `undefined`.
- `exactOptionalPropertyTypes`: phân biệt property missing với property có value `undefined`.
- `useUnknownInCatchVariables`: `catch (error)` là `unknown`, buộc narrow trước khi dùng.

Migration strategy:

1. Bật strict ở package mới trước.
2. Fix API boundary và shared types trước.
3. Giảm `any` bằng `unknown` + guards/schema.
4. Dùng `// @ts-expect-error` có lý do, không dùng `// @ts-ignore` vô tội vạ.

### 3.10. Branded Types và Nominal Typing

TypeScript mặc định là structural typing: cùng shape thì tương thích. Branded type giúp phân biệt primitive giống nhau.

```ts
type Brand<T, B extends string> = T & { readonly __brand: B };

type UserId = Brand<string, "UserId">;
type ProductId = Brand<string, "ProductId">;

function getUser(id: UserId) {
  return id;
}

const userId = "u1" as UserId;
const productId = "p1" as ProductId;

getUser(userId);
// getUser(productId); // Error
```

Tạo brand ở boundary sau validation:

```ts
function parseUserId(value: string): UserId {
  if (!value.startsWith("user_")) {
    throw new Error("Invalid user id");
  }

  return value as UserId;
}
```

💡 Brand hữu ích cho IDs, currency, ISO date string, feature flag key. Đừng brand mọi string nếu làm code quá nặng.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. Type-safe API client

```ts
type ApiSuccess<T> = {
  ok: true;
  data: T;
};

type ApiFailure = {
  ok: false;
  status: number;
  message: string;
};

type ApiResult<T> = ApiSuccess<T> | ApiFailure;

async function request<T>(
  input: RequestInfo,
  init?: RequestInit,
): Promise<ApiResult<T>> {
  const response = await fetch(input, init);

  if (!response.ok) {
    return {
      ok: false,
      status: response.status,
      message: response.statusText,
    };
  }

  const data = (await response.json()) as T;

  return {
    ok: true,
    data,
  };
}
```

Usage:

```ts
type User = {
  id: string;
  name: string;
};

async function loadUser(id: string) {
  const result = await request<User>(`/api/users/${id}`);

  if (!result.ok) {
    return result.message;
  }

  return result.data.name;
}
```

⚠️ `as T` chỉ là compile-time assertion. Production client nên validate `response.json()` bằng schema trước khi trả `ok: true`.

### 4.2. Type-safe event emitter

```ts
type EventMap = {
  "user:created": { id: string; name: string };
  "user:deleted": { id: string };
  "auth:expired": undefined;
};

class TypedEventEmitter<Events extends Record<string, unknown>> {
  private listeners = new Map<keyof Events, Set<(payload: unknown) => void>>();

  on<K extends keyof Events>(event: K, listener: (payload: Events[K]) => void) {
    const listeners = this.listeners.get(event) ?? new Set();
    listeners.add(listener as (payload: unknown) => void);
    this.listeners.set(event, listeners);

    return () => listeners.delete(listener as (payload: unknown) => void);
  }

  emit<K extends keyof Events>(event: K, payload: Events[K]) {
    this.listeners.get(event)?.forEach((listener) => listener(payload));
  }
}

const emitter = new TypedEventEmitter<EventMap>();

emitter.on("user:created", (payload) => {
  console.log(payload.id, payload.name);
});

emitter.emit("user:created", { id: "u1", name: "Ada" });
// emitter.emit("user:created", { id: "u1" }); // Error
```

### 4.3. Generic React form state

```tsx
type FormState<T extends Record<string, unknown>> = {
  values: T;
  errors: Partial<Record<keyof T, string>>;
  touched: Partial<Record<keyof T, boolean>>;
};

function setFieldValue<T extends Record<string, unknown>, K extends keyof T>(
  state: FormState<T>,
  key: K,
  value: T[K],
): FormState<T> {
  return {
    ...state,
    values: {
      ...state.values,
      [key]: value,
    },
  };
}
```

Usage:

```ts
type LoginForm = {
  email: string;
  password: string;
  rememberMe: boolean;
};

const next = setFieldValue(loginFormState, "rememberMe", true);
// setFieldValue(loginFormState, "rememberMe", "yes"); // Error
```

### 4.4. Discriminated union cho async UI

```tsx
type User = {
  id: string;
  name: string;
};

type UserState =
  | { status: "loading" }
  | { status: "ready"; user: User }
  | { status: "error"; message: string };

function UserPanel({ state }: { state: UserState }) {
  switch (state.status) {
    case "loading":
      return <Spinner />;
    case "ready":
      return <h2>{state.user.name}</h2>;
    case "error":
      return <Alert>{state.message}</Alert>;
  }
}
```

Pattern này tránh state không hợp lệ như `isLoading: false`, `error: null`, nhưng `user` cũng `null` mà UI vẫn render.

### 4.5. Template literal types cho analytics

```ts
type Entity = "user" | "product";
type Verb = "created" | "updated" | "deleted";
type AnalyticsEvent = `${Entity}.${Verb}`;

type AnalyticsPayload = {
  event: AnalyticsEvent;
  properties: Record<string, string | number | boolean>;
};

function track(payload: AnalyticsPayload) {
  navigator.sendBeacon("/analytics", JSON.stringify(payload));
}

track({
  event: "product.updated",
  properties: { productId: "p1" },
});
```

### 4.6. Branded IDs ở API boundary

```ts
type Brand<T, B extends string> = T & { readonly __brand: B };
type UserId = Brand<string, "UserId">;

function toUserId(value: string): UserId {
  if (!/^user_[a-z0-9]+$/i.test(value)) {
    throw new Error("Invalid UserId");
  }

  return value as UserId;
}

function navigateToUser(id: UserId) {
  return `/users/${id}`;
}

const id = toUserId("user_123");
navigateToUser(id);
```

## 5. 🏭 Production Notes / React Implications

- **API boundary:** TypeScript không validate JSON. Dùng schema validation ở boundary rồi mới cast/brand type.
- **React props:** Generic components tốt khi API component thật sự phụ thuộc type data, ví dụ table columns, form fields, select options.
- **Async state:** Discriminated union tốt hơn nhiều boolean rời rạc vì loại bỏ state không hợp lệ.
- **Forms:** `Partial<Record<keyof T, string>>` hợp cho errors/touched, nhưng validate runtime vẫn cần schema.
- **Memoization:** Type không làm `useMemo`/`useCallback` tự nhanh hơn. Nó chỉ giúp callback/value đúng contract.
- **Maintainability:** Nếu type quá khó đọc, hãy tách thành tên có nghĩa hoặc giảm abstraction.
- **Security:** Không tin type từ client hoặc API. Auth/permission/data shape vẫn phải kiểm tra ở runtime/server.
- **SSR/Next.js:** Data qua server/client boundary phải serializable; tránh truyền class instance, function, `Map`, `Set` nếu framework không hỗ trợ.
- **Testing:** Unit test runtime guards/schema và behavior chính; TypeScript chỉ test compile-time. Có thể dùng `tsd` hoặc `expect-type` cho thư viện type-heavy.

## 6. ⚠️ Common Pitfalls

- ❌ Lạm dụng `any`, làm mất toàn bộ lợi ích TypeScript.
- ❌ Dùng `as` để ép mọi lỗi thay vì sửa type/model/boundary.
- ❌ Generic không constraint khiến API nhận type quá rộng.
- ❌ Viết conditional/mapped type quá phức tạp làm team khó maintain.
- ❌ Tin rằng `type User` đồng nghĩa API response runtime chắc chắn là `User`.
- ❌ Dùng `Partial<T>` cho object cần đầy đủ field.
- ❌ Quên `Readonly<T>` chỉ shallow readonly.
- ❌ Tạo `.d.ts` quá rộng như `declare module "*"` khiến lỗi thật biến mất.
- ❌ Tắt `strictNullChecks` rồi phải xử lý crash do `undefined`.
- ❌ Brand bằng `as` ở mọi nơi thay vì chỉ brand sau validation.
- ❌ Dùng `@ts-ignore` lâu dài; nên dùng `@ts-expect-error` kèm lý do khi thật sự cần.

## 7. ✅ Decision Guide or Checklist

### Chọn pattern nào?

| Nhu cầu | Pattern | Lý do |
|---|---|---|
| Function/component reusable giữ type input | Generics | Không mất type inference |
| Generic cần field cụ thể | `T extends ...`, `K extends keyof T` | Bắt lỗi key/property sai |
| Transform object type | Mapped types | Tạo errors/touched/readonly/optional map |
| Lấy type từ function/promise | `ReturnType`, `Parameters`, `Awaited`, `infer` | Tránh duplicate type |
| State loading/success/error | Discriminated union | Loại bỏ state không hợp lệ |
| Validate `unknown` | Type guards hoặc schema | Narrow runtime data an toàn |
| Event/route/i18n key có format | Template literal types | Giảm typo |
| Phân biệt nhiều loại ID string | Branded types | Tránh truyền nhầm ID |
| Thư viện thiếu type | `.d.ts` | Bổ sung type contract |
| Project lớn | strict `tsconfig` | Bắt lỗi sớm và nhất quán |

### Checklist trước khi merge

```txt
□ Có dùng any không? Có thể đổi sang unknown + guard/schema không?
□ Generic có constraint đủ chặt không?
□ Có duplicate type có thể lấy bằng ReturnType/Awaited/Parameters không?
□ API response đã validate runtime chưa?
□ Async UI state có thể rơi vào state không hợp lệ không?
□ Utility type có làm object quá lỏng không?
□ Branded type có được tạo ở boundary sau validation không?
□ .d.ts có quá rộng và che mất lỗi import thật không?
□ tsconfig strict flags có đang bật không?
□ Type abstraction có dễ đọc với team không?
```

## 8. 🗣️ Short Interview Answer

Theo em, TypeScript advanced nên được dùng để mô hình hóa constraint thật của hệ thống, không phải để viết type càng phức tạp càng tốt. Với generics, em thường bắt đầu từ use case như typed API client, form state, table columns hoặc event emitter; nếu generic cần đọc property thì phải constraint bằng `keyof` hoặc interface cụ thể để giữ type-safe.

Em dùng utility types như `Pick`, `Omit`, `Partial`, `Record`, `ReturnType`, `Awaited` để tránh duplicate type và diễn đạt intent rõ hơn. Với async UI, em thích discriminated union vì nó biến loading/success/error thành state machine an toàn, tránh nhiều boolean rời rạc. Với dữ liệu từ API, em không tin TypeScript compile-time; em sẽ validate bằng schema hoặc type guard trước rồi mới dùng type trong app.

Điểm senior quan trọng là biết dừng đúng lúc. Nếu mapped type, conditional type hoặc template literal type làm API dễ dùng và bắt lỗi thật thì tốt. Nếu nó làm code khó đọc, khó debug, hoặc cần quá nhiều `as`, em sẽ đơn giản hóa model hoặc đẩy validation về runtime boundary.

## 9. 🧾 Ghi nhớ nhanh

- Generic giữ type information khi viết function/component reusable.
- Constraint bằng `extends`, `keyof`, `T[K]` để tránh generic quá rộng.
- Conditional type là if/else ở type level; `infer` dùng để trích xuất type.
- Utility types giúp giảm duplicate, nhưng dùng sai có thể làm type quá lỏng.
- Mapped types biến đổi property; template literal types kiểm soát string format.
- Type guards narrow `unknown` ở runtime; guard sai vẫn nguy hiểm.
- Discriminated union rất hợp cho async state và state machine UI.
- `.d.ts` nên cụ thể, tránh `declare module "*"` nếu không bắt buộc.
- `strict: true` là baseline cho codebase TypeScript nghiêm túc.
- Branded type hữu ích cho ID/currency/date string, nhưng nên tạo sau validation.

## 10. 📖 Giải thích các thuật ngữ trong topic

- `Generic`: Type parameter cho phép function/type/component hoạt động với nhiều kiểu mà vẫn giữ type safety.
- `Generic constraint`: Ràng buộc generic bằng `extends` để type phải có shape nhất định.
- `keyof`: Tạo union các key của object type.
- `Indexed access type`: Truy cập type của property bằng `T[K]`.
- `Conditional type`: Type dạng `T extends U ? X : Y`.
- `infer`: Từ khóa trích xuất type bên trong conditional type.
- `Utility type`: Type built-in giúp biến đổi type, ví dụ `Partial`, `Pick`, `Omit`.
- `Mapped type`: Type lặp qua `keyof T` để tạo object type mới.
- `Template literal type`: Type dùng cú pháp template string để tạo string literal union.
- `Type guard`: Function runtime trả về predicate như `value is User` để narrow type.
- `Discriminated union`: Union type có field chung làm discriminator, ví dụ `status`.
- `Exhaustiveness check`: Kỹ thuật dùng `never` để đảm bảo switch xử lý đủ union cases.
- `Declaration file`: File `.d.ts` khai báo type cho JavaScript/global/module.
- `Ambient declaration`: Khai báo type cho thứ tồn tại ở runtime nhưng không import trực tiếp trong TypeScript.
- `Strict mode`: Nhóm compiler options nghiêm ngặt giúp bắt lỗi sớm.
- `Branded type`: Kỹ thuật thêm brand vào primitive để tạo nominal-like type.
- `Structural typing`: Type tương thích dựa trên shape, không dựa trên tên type.
- `Runtime validation`: Kiểm tra dữ liệu khi chạy thật, cần cho API/user input/localStorage.
- `API boundary`: Ranh giới dữ liệu đi vào/ra app, nơi cần validate và normalize.
- `Type inference`: Khả năng TypeScript tự suy luận type từ code.
