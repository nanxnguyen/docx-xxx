# 💽 Topic 17: Browser Storage - `localStorage`, `sessionStorage`, Cookie & IndexedDB

## 1. ⭐ Senior/Staff Summary

Browser có nhiều cơ chế lưu trữ client-side, nhưng không có loại nào “tốt nhất cho mọi thứ”. Chọn đúng storage phụ thuộc vào **dữ liệu có nhạy cảm không**, **có cần gửi server không**, **dung lượng bao nhiêu**, **API sync hay async**, **có cần offline/query/index không**, và **rủi ro security**.

| Storage | Dung lượng thường gặp | Lifetime | API | Gửi server tự động | Use case chính |
|---|---:|---|---|---|---|
| 🍪 Cookie | khoảng 4KB/cookie | Theo `Expires`/`Max-Age` hoặc session | String, sync | ✅ Có | Auth session, CSRF token, server-readable state nhỏ |
| 💾 `localStorage` | thường 5-10MB/origin | Persistent đến khi bị xoá | String, sync | ❌ Không | Theme, language, non-sensitive preferences |
| 📝 `sessionStorage` | thường 5-10MB/origin | Theo tab/session | String, sync | ❌ Không | Draft tạm, wizard state, tab-specific state |
| 🗄️ IndexedDB | lớn hơn nhiều, tùy quota | Persistent đến khi bị xoá/evict | Async database | ❌ Không | Offline data, large datasets, blobs/files, structured cache |

> 🔥 Senior point: **Không lưu access token/sensitive data trong `localStorage`** nếu app có rủi ro XSS. Với auth session, ưu tiên cookie `HttpOnly + Secure + SameSite` do server set.

## 2. 🧠 Key Mental Model or Key Points

- 🍪 **Cookie là dữ liệu HTTP.** Browser tự gửi cookie theo request matching domain/path, nên hợp cho server-side session nhưng tốn bandwidth và cần flag bảo mật.
- 💾 **`localStorage` là key-value sync storage.** Dễ dùng nhưng block main thread, chỉ lưu string, JS đọc được, không phù hợp dữ liệu nhạy cảm.
- 📝 **`sessionStorage` giống `localStorage` nhưng scoped theo tab.** Đóng tab là mất; duplicate tab có thể clone state ban đầu tùy browser.
- 🗄️ **IndexedDB là database async trên browser.** Hợp offline-first, dữ liệu lớn, query theo index, file/blob.
- 🔐 **Client storage không phải nơi tin cậy.** User có thể sửa, xoá, inspect. Server phải validate mọi thứ.
- ⚠️ **Storage quota không cố định.** Browser, device, private mode, storage pressure đều ảnh hưởng.
- ⚛️ **React/SSR:** Browser storage chỉ tồn tại trên client. Đọc storage trong render SSR sẽ lỗi hoặc hydration mismatch.

## 3. 📚 Main Concepts

### 3.1. 🍪 Cookie - “tem dán lên mọi request”

Cookie là cơ chế lưu key-value nhỏ, được browser gửi tự động trong HTTP request nếu domain/path khớp.

**Điểm mạnh**

- Server đọc được tự động.
- Có expiry bằng `Expires` hoặc `Max-Age`.
- Có security flags mạnh: `HttpOnly`, `Secure`, `SameSite`.
- Hợp cho session authentication và CSRF-related state nhỏ.

**Điểm yếu**

- Dung lượng nhỏ.
- Gửi kèm request nên tăng bandwidth.
- Nếu không cấu hình đúng, dễ gặp CSRF/session leakage.
- Cookie đọc bằng JS không thể có `HttpOnly`; `HttpOnly` phải set từ server qua `Set-Cookie`.

Security flags cần nhớ:

| Flag | Ý nghĩa | Vì sao quan trọng |
|---|---|---|
| `HttpOnly` | JavaScript không đọc được cookie | Giảm impact của XSS với session token |
| `Secure` | Chỉ gửi qua HTTPS | Tránh lộ cookie qua HTTP |
| `SameSite=Strict` | Không gửi cross-site navigation phần lớn trường hợp | CSRF protection mạnh, nhưng có thể ảnh hưởng OAuth |
| `SameSite=Lax` | Gửi trong top-level navigation an toàn hơn | Default thực tế phổ biến cho session |
| `SameSite=None; Secure` | Cho cross-site cookie | Cần cho embedded/third-party flow, rủi ro cao hơn |
| `Path`/`Domain` | Giới hạn phạm vi cookie | Giảm cookie gửi thừa |
| `Max-Age`/`Expires` | Vòng đời cookie | Tự hết hạn |

> ✅ Auth session production thường là server set cookie: `Set-Cookie: session=...; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=...`

### 3.2. 💾 `localStorage` - persistent key-value storage

`localStorage` lưu string theo origin và tồn tại sau khi đóng tab/browser.

```ts
localStorage.setItem("theme", "dark");
const theme = localStorage.getItem("theme");
localStorage.removeItem("theme");
```

Object phải serialize:

```ts
type Preferences = {
  theme: "light" | "dark";
  language: "vi" | "en";
};

const preferences: Preferences = { theme: "dark", language: "vi" };

localStorage.setItem("preferences", JSON.stringify(preferences));

const raw = localStorage.getItem("preferences");
const parsed = raw ? (JSON.parse(raw) as Preferences) : null;
```

**Dùng tốt cho**

- Theme, language, display density.
- Dismissed banners.
- Non-sensitive user preferences.
- Small client-only cache không quan trọng.

**Không dùng cho**

- Access token, refresh token, PII, permission quyết định bảo mật.
- Dữ liệu lớn hoặc đọc/ghi liên tục trong hot path.
- Data cần query/index.

> ⚠️ `localStorage` là synchronous API. Đọc/ghi nhiều hoặc parse JSON lớn có thể block main thread.

### 3.3. 📝 `sessionStorage` - tab-scoped temporary storage

`sessionStorage` có API giống `localStorage`, nhưng lifetime theo tab/session.

```ts
sessionStorage.setItem("checkoutStep", "shipping");
const step = sessionStorage.getItem("checkoutStep");
```

Phù hợp cho:

- Wizard state tạm trong một tab.
- Draft form không cần giữ sau khi đóng tab.
- UI state theo tab, ví dụ filter tạm.
- OAuth/redirect state ngắn hạn nếu không cần server đọc.

Không phù hợp cho:

- Dữ liệu cần share giữa tabs.
- Persistent preferences.
- Sensitive tokens.

> 💡 `sessionStorage` không bắn `storage` event giữa tab giống `localStorage` theo cách hữu ích, vì mỗi tab có session riêng.

### 3.4. 🗄️ IndexedDB - database async trong browser

IndexedDB là object database async, hỗ trợ transactions, object stores, indexes, cursor, structured clone, Blob/File.

Phù hợp cho:

- Offline-first app.
- Large datasets: catalog, messages, maps, documents.
- File/blob cache.
- Queue mutation khi offline.
- Client-side search/filter cần index.

Không nên dùng IndexedDB nếu chỉ lưu một preference nhỏ. API native khá verbose; production thường dùng wrapper như Dexie hoặc localForage.

Ví dụ native tối giản:

```ts
function openDatabase(): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open("app-db", 1);

    request.onupgradeneeded = () => {
      const db = request.result;
      const store = db.createObjectStore("notes", { keyPath: "id" });
      store.createIndex("updatedAt", "updatedAt");
    };

    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}
```

> ✅ IndexedDB là async nên tốt hơn `localStorage` cho dữ liệu lớn, nhưng cần handle versioning, transaction error và migration.

### 3.5. 📣 Storage event và sync giữa tabs

Khi một tab thay đổi `localStorage`, tab khác cùng origin có thể nhận `storage` event.

```ts
window.addEventListener("storage", (event) => {
  if (event.key === "theme") {
    console.log("Theme changed in another tab:", event.newValue);
  }
});
```

Điểm cần nhớ:

- Event thường không fire trong chính tab đã gọi `setItem`.
- Chỉ dùng cho sync state nhỏ như logout/theme.
- Với sync phức tạp, cân nhắc `BroadcastChannel`.

### 3.6. 📦 Quota, eviction và private mode

Storage quota phụ thuộc browser/device/origin. Không giả định “luôn còn chỗ”.

```ts
async function logStorageEstimate() {
  if (!navigator.storage?.estimate) return;

  const estimate = await navigator.storage.estimate();
  console.log({
    usage: estimate.usage,
    quota: estimate.quota,
  });
}
```

Browser có thể evict storage khi device thiếu dung lượng, đặc biệt với data không được persist. Có thể request persistent storage:

```ts
async function requestPersistence() {
  if (!navigator.storage?.persist) return false;
  return navigator.storage.persist();
}
```

> ⚠️ Private/incognito mode có quota thấp hơn hoặc behavior khác. Luôn handle lỗi khi storage unavailable/full.

### 3.7. 🧰 Cache API khác gì Browser Storage?

Cache API thường dùng với Service Worker để cache HTTP `Request`/`Response`, không phải general key-value app state.

| Nhu cầu | Chọn |
|---|---|
| Cache HTML/CSS/JS/image/API response cho offline | Cache API |
| Lưu user preferences nhỏ | `localStorage` |
| Lưu session/tab draft | `sessionStorage` |
| Lưu database offline có query/index | IndexedDB |
| Server cần đọc session trên request | Cookie |

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Typed `localStorage` helper có error handling

```ts
type StorageResult<T> =
  | { ok: true; value: T }
  | { ok: false; error: "missing" | "parse-error" | "quota" | "unavailable" };

export function readJson<T>(key: string): StorageResult<T> {
  try {
    const raw = window.localStorage.getItem(key);
    if (raw === null) return { ok: false, error: "missing" };

    return { ok: true, value: JSON.parse(raw) as T };
  } catch {
    return { ok: false, error: "parse-error" };
  }
}

export function writeJson<T>(key: string, value: T): StorageResult<T> {
  try {
    window.localStorage.setItem(key, JSON.stringify(value));
    return { ok: true, value };
  } catch (error) {
    if (error instanceof DOMException && error.name === "QuotaExceededError") {
      return { ok: false, error: "quota" };
    }

    return { ok: false, error: "unavailable" };
  }
}
```

### 4.2. ✅ React hook đọc storage an toàn với SSR

```tsx
function useStoredTheme() {
  const [theme, setTheme] = React.useState<"light" | "dark">("light");

  React.useEffect(() => {
    const stored = window.localStorage.getItem("theme");
    if (stored === "light" || stored === "dark") {
      setTheme(stored);
    }
  }, []);

  const updateTheme = React.useCallback((nextTheme: "light" | "dark") => {
    setTheme(nextTheme);
    window.localStorage.setItem("theme", nextTheme);
  }, []);

  return { theme, setTheme: updateTheme };
}
```

> 💡 Không đọc `localStorage` trực tiếp trong render server. Dùng `useEffect`, client-only boundary, hoặc initial value từ server.

### 4.3. ✅ Cookie helper cho non-HttpOnly cookie

```ts
function setClientCookie(name: string, value: string, maxAgeSeconds: number) {
  document.cookie = [
    `${encodeURIComponent(name)}=${encodeURIComponent(value)}`,
    `Max-Age=${maxAgeSeconds}`,
    "Path=/",
    "SameSite=Lax",
    location.protocol === "https:" ? "Secure" : "",
  ]
    .filter(Boolean)
    .join("; ");
}

function getClientCookie(name: string): string | null {
  const encodedName = `${encodeURIComponent(name)}=`;

  return (
    document.cookie
      .split("; ")
      .find((row) => row.startsWith(encodedName))
      ?.slice(encodedName.length) ?? null
  );
}
```

⚠️ Client-side cookie không thể set `HttpOnly`. Auth/session cookie nên được set từ server.

### 4.4. ✅ IndexedDB với Dexie-style abstraction

Native IndexedDB dài; trong production thường dùng wrapper. Ví dụ concept:

```ts
type Note = {
  id: string;
  title: string;
  body: string;
  updatedAt: number;
};

interface NotesRepository {
  get(id: string): Promise<Note | undefined>;
  put(note: Note): Promise<void>;
  listRecent(limit: number): Promise<Note[]>;
}
```

Repository boundary giúp UI không phụ thuộc trực tiếp vào IndexedDB implementation. Sau này có thể đổi từ native IndexedDB sang Dexie/localForage mà ít ảnh hưởng component.

### 4.5. ✅ Sync logout giữa tabs bằng `storage`

```ts
function broadcastLogout() {
  localStorage.setItem("auth:logout", String(Date.now()));
}

function listenForLogout(onLogout: () => void) {
  function handleStorage(event: StorageEvent) {
    if (event.key === "auth:logout") {
      onLogout();
    }
  }

  window.addEventListener("storage", handleStorage);
  return () => window.removeEventListener("storage", handleStorage);
}
```

## 5. 🏭 Production Notes / React Implications

- 🔐 **Auth:** Prefer `HttpOnly + Secure + SameSite` cookies for session. Không lưu token nhạy cảm trong `localStorage`.
- 🧨 **XSS:** Nếu attacker chạy được JS, họ đọc được `localStorage`, `sessionStorage`, non-HttpOnly cookies và IndexedDB.
- 🛡️ **CSRF:** Cookie auth cần `SameSite`, CSRF token hoặc server-side CSRF mitigation tùy flow.
- ⚛️ **React hydration:** Đọc storage sau mount hoặc inject server initial state để tránh mismatch.
- 🚀 **Performance:** `localStorage`/`sessionStorage` sync và JSON parse/stringify có thể block render. Cache parsed value trong memory nếu dùng nhiều.
- 🗄️ **Offline:** IndexedDB + Service Worker + Cache API thường đi cùng nhau cho offline-first.
- 🧹 **Schema migration:** Dữ liệu persistent cần versioning và migration; nếu parse fail, clear/reset gracefully.
- 📦 **Quota:** Luôn catch `QuotaExceededError`. Với IndexedDB lớn, hiển thị UX dọn cache hoặc retry.
- 🧪 **Testing:** Mock storage trong unit tests, test private mode/unavailable storage, malformed JSON, quota failure, multi-tab sync.
- ♿ **UX:** Nếu storage fail, app vẫn nên degrade được: default settings, retry, hoặc server source of truth.

## 6. ⚠️ Common Pitfalls

- ❌ Lưu access token/refresh token/PII trong `localStorage`.
- ❌ Nghĩ client storage là trusted source; user có thể sửa mọi thứ.
- ❌ Đọc `localStorage` trong SSR render gây crash hoặc hydration mismatch.
- ❌ Không catch `JSON.parse`, làm app crash vì dữ liệu cũ/malformed.
- ❌ Không handle `QuotaExceededError`.
- ❌ Lưu object lớn vào `localStorage` rồi parse trong render path.
- ❌ Dùng cookie cho data lớn, làm mọi request nặng hơn.
- ❌ Quên cookie `Secure`, `HttpOnly`, `SameSite`.
- ❌ Dùng IndexedDB cho preference nhỏ làm complexity tăng không cần thiết.
- ❌ Không version schema IndexedDB/local persisted data.
- ❌ Dùng `localStorage.clear()` trong app shared origin, xoá nhầm key của module khác.
- ❌ Tin `storage` event fire trong cùng tab thay đổi data.

## 7. ✅ Decision Guide or Checklist

### Chọn storage nào?

| Nhu cầu | Chọn | Lý do |
|---|---|---|
| Server cần tự đọc session trên request | Cookie | Browser tự gửi kèm HTTP request |
| Auth session production | Server-set `HttpOnly` cookie | JS không đọc được token |
| Theme/language/preference nhỏ | `localStorage` | Persistent, dễ dùng |
| Draft tạm theo tab | `sessionStorage` | Đóng tab là mất, không share tab |
| Offline data lớn/query/index | IndexedDB | Async database, store object/blob |
| Cache HTTP response/assets | Cache API | Thiết kế cho Request/Response |
| Sync logout/theme giữa tabs | `localStorage` event hoặc `BroadcastChannel` | Cross-tab communication |
| Sensitive data client-side | Tránh lưu, hoặc mã hóa + threat model rõ | Browser storage không phải secure vault |

### Checklist trước khi lưu dữ liệu

```txt
□ Dữ liệu có nhạy cảm không?
□ Server có cần đọc tự động trên request không?
□ Dữ liệu cần sống bao lâu?
□ Có cần share giữa tabs không?
□ Dung lượng có thể lớn không?
□ API sync có ảnh hưởng render/hot path không?
□ Có cần query/index/offline không?
□ Có schema version và migration chưa?
□ Có catch parse/quota/unavailable storage chưa?
□ SSR/hydration có đọc storage đúng client-only chưa?
□ Có kế hoạch clear/logout/privacy không?
```

## 8. 🗣️ Short Interview Answer

Theo em, browser storage nên chọn theo use case chứ không chọn theo thói quen. Cookie nhỏ nhưng được gửi tự động lên server, nên phù hợp cho session/auth nếu được set bằng `HttpOnly`, `Secure`, `SameSite`. `localStorage` persistent và dễ dùng cho theme hoặc preference, nhưng là sync API và JavaScript đọc được nên không nên lưu token nhạy cảm. `sessionStorage` giống localStorage nhưng scoped theo tab, hợp cho draft hoặc wizard tạm.

Với dữ liệu lớn hoặc offline-first, em sẽ dùng IndexedDB vì nó async, hỗ trợ object store, index, transaction và Blob/File. Trong production em luôn nghĩ thêm về XSS, CSRF, quota, private mode, schema migration và SSR/hydration. Điểm quan trọng là client storage không đáng tin cậy; server vẫn phải validate mọi dữ liệu quan trọng.

## 9. 🧾 Ghi nhớ nhanh

- Cookie tự gửi server; `localStorage`, `sessionStorage`, IndexedDB thì không.
- Auth session nên dùng server-set `HttpOnly + Secure + SameSite` cookie.
- `localStorage` persistent nhưng sync và JS đọc được.
- `sessionStorage` theo tab, đóng tab là mất.
- IndexedDB async, hợp dữ liệu lớn/offline/query/blob.
- `localStorage` chỉ lưu string, object phải `JSON.stringify`.
- Luôn catch `JSON.parse` và `QuotaExceededError`.
- Không đọc browser storage trong SSR render.
- `storage` event hữu ích để sync giữa tabs, nhưng không fire trong cùng tab.
- Cache API dành cho HTTP responses, không thay thế IndexedDB/localStorage cho app state.

## 10. 📖 Giải thích các thuật ngữ trong topic

- `Origin`: Bộ ba scheme + host + port, ví dụ `https://example.com:443`.
- `Cookie`: Key-value nhỏ do browser lưu và gửi kèm HTTP request phù hợp.
- `HttpOnly`: Cookie flag khiến JavaScript không đọc được cookie.
- `Secure`: Cookie flag chỉ gửi qua HTTPS.
- `SameSite`: Cookie flag kiểm soát cookie có được gửi trong cross-site request không.
- `CSRF`: Tấn công lợi dụng browser tự gửi cookie để thực hiện request ngoài ý muốn.
- `XSS`: Tấn công chạy JavaScript độc hại trong site, có thể đọc browser storage JS-accessible.
- `localStorage`: Persistent synchronous key-value storage theo origin.
- `sessionStorage`: Synchronous key-value storage theo tab/session.
- `IndexedDB`: Async object database trong browser.
- `Object store`: “Bảng” trong IndexedDB để lưu object.
- `Index`: Cấu trúc giúp query IndexedDB theo field khác key chính.
- `Transaction`: Nhóm thao tác IndexedDB được commit/rollback cùng nhau.
- `Quota`: Giới hạn dung lượng storage browser cho origin.
- `Eviction`: Browser xoá dữ liệu storage khi thiếu dung lượng hoặc theo policy.
- `Storage event`: Event bắn ở tab khác khi `localStorage` thay đổi.
- `BroadcastChannel`: API giao tiếp giữa tabs/windows cùng origin.
- `Cache API`: API cache HTTP Request/Response, thường dùng với Service Worker.
- `Hydration mismatch`: Lỗi khi HTML server render không khớp render đầu tiên trên client.
- `Schema migration`: Quá trình nâng version dữ liệu đã lưu khi shape thay đổi.
