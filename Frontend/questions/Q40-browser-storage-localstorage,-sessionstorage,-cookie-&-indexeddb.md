# 💽 Q40: Browser Storage - LocalStorage, SessionStorage, Cookie & IndexedDB

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">💽 Q40: Browser Storage - LocalStorage, SessionStorage, Cookie & IndexedDB</span></summary>


**Trả lời:**

Browser cung cấp **4 cách lưu trữ data** ở client-side, mỗi cách phù hợp cho use case khác nhau:

- **Cookie**: Nhỏ (4KB), gửi kèm mỗi HTTP request, có expiry, dùng cho auth tokens
- **LocalStorage**: 5-10MB, persistent (không mất khi đóng tab), sync API, dùng cho settings/preferences
- **SessionStorage**: 5-10MB, mất khi đóng tab, sync API, dùng cho temporary data
- **IndexedDB**: 50MB-unlimited, async, database-like, dùng cho large datasets

#### **📊 So Sánh 4 Loại Storage**

```
┌────────────────────────────────────────────────────────────────────────┐
│                    BROWSER STORAGE COMPARISON                          │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│  Tiêu Chí          │ Cookie    │ LocalStorage │ SessionStorage │ IndexedDB │
│  ─────────────────────────────────────────────────────────────────── │
│  Dung lượng        │ 4KB       │ 5-10MB       │ 5-10MB         │ 50MB+     │
│  Tồn tại           │ Expiry    │ Mãi mãi      │ Đóng tab mất   │ Mãi mãi   │
│  API               │ Sync      │ Sync         │ Sync           │ Async     │
│  Gửi server        │ ✅ Tự động│ ❌ Không     │ ❌ Không       │ ❌ Không  │
│  Complexity        │ Medium    │ Easy         │ Easy           │ Hard      │
│  Use Case          │ Auth      │ Settings     │ Form data      │ Big data  │
│  ─────────────────────────────────────────────────────────────────── │
│                                                                        │
│  🍪 Cookie:        Như tem dán lên thư gửi đi (mọi request)          │
│  💾 LocalStorage:  Như USB drive (cắm mãi mãi)                        │
│  📝 SessionStorage: Như giấy nháp (hết giờ là vứt)                    │
│  🗄️ IndexedDB:     Như kho chứa lớn (chứa cả thùng hàng)             │
└────────────────────────────────────────────────────────────────────────┘
```

---

#### **🍪 1. Cookie - "Tem Dán Lên Mọi Request"**

**Đặc điểm:**
- Dung lượng nhỏ: **4KB** (chỉ lưu được text ngắn)
- Tự động gửi kèm **mọi HTTP request** tới server
- Có **expiry date** (tự động xóa sau thời gian)
- Dùng cho: **Authentication tokens, user tracking**

**Ưu điểm:**
- ✅ Server tự động nhận (không cần JS)
- ✅ Có expiry (tự động dọn dẹp)
- ✅ Secure flag (HTTPS only), HttpOnly (JS không đọc được)

**Nhược điểm:**
- ❌ Nhỏ (4KB) - không lưu nhiều
- ❌ Tốn bandwidth (gửi kèm mọi request)
- ❌ Phức tạp hơn localStorage

**Code Example:**

```typescript
// ============================================
// COOKIE - Ví Dụ Đơn Giản
// ============================================

// 1️⃣ SET Cookie - Lưu token
function setCookie(name: string, value: string, days: number = 7) {
  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Tính expiry
  const expires = `expires=${date.toUTCString()}`;
  
  // Lưu cookie
  document.cookie = `${name}=${value}; ${expires}; path=/; SameSite=Strict`;
  // path=/     → cookie có hiệu lực toàn site
  // SameSite   → bảo mật CSRF
}

// Usage: Lưu auth token
setCookie('authToken', 'abc123xyz', 7); // Hết hạn sau 7 ngày

// 2️⃣ GET Cookie - Đọc token
function getCookie(name: string): string | null {
  // document.cookie = "authToken=abc123; userId=456; theme=dark"
  const cookies = document.cookie.split('; ');
  
  for (const cookie of cookies) {
    const [key, value] = cookie.split('=');
    if (key === name) return value;
  }
  
  return null; // Không tìm thấy
}

// Usage: Đọc auth token
const token = getCookie('authToken');
console.log(token); // "abc123xyz"

// 3️⃣ DELETE Cookie - Xóa token (set expiry = quá khứ)
function deleteCookie(name: string) {
  document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
}

// Usage: Logout - xóa token
deleteCookie('authToken');

// ============================================
// Thực Tế: Cookie Helper Class
// ============================================
class CookieManager {
  // Set cookie
  static set(name: string, value: string, days: number = 7): void {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = `${name}=${value}; expires=${expires}; path=/; SameSite=Strict`;
  }
  
  // Get cookie
  static get(name: string): string | null {
    return document.cookie
      .split('; ')
      .find(row => row.startsWith(name + '='))
      ?.split('=')[1] || null;
  }
  
  // Delete cookie
  static delete(name: string): void {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
  }
}

// Usage: Clean API
CookieManager.set('user', 'John', 30); // Lưu 30 ngày
const user = CookieManager.get('user'); // "John"
CookieManager.delete('user'); // Xóa
```

---

#### **💾 2. LocalStorage - "USB Drive - Lưu Mãi Mãi"**

**Đặc điểm:**
- Dung lượng lớn: **5-10MB** (tuỳ browser)
- **Persistent** - không mất khi đóng tab/browser
- **Sync API** - dễ dùng
- Dùng cho: **User settings, preferences, cache data**

**Ưu điểm:**
- ✅ Dễ dùng (getItem/setItem)
- ✅ Lưu mãi mãi (không tự xóa)
- ✅ Dung lượng lớn (5-10MB)

**Nhược điểm:**
- ❌ Sync API (block main thread nếu dùng nhiều)
- ❌ Chỉ lưu string (phải JSON.stringify object)
- ❌ Không secure (JS đọc được → XSS risk)

**Code Example:**

```typescript
// ============================================
// LOCALSTORAGE - Ví Dụ Đơn Giản
// ============================================

// 1️⃣ LƯU DATA (setItem)
// Lưu string
localStorage.setItem('username', 'John Doe');

// Lưu object (phải stringify)
const user = { id: 1, name: 'John', role: 'admin' };
localStorage.setItem('user', JSON.stringify(user));

// Lưu array
const cart = [
  { id: 1, name: 'iPhone', price: 999 },
  { id: 2, name: 'AirPods', price: 199 },
];
localStorage.setItem('cart', JSON.stringify(cart));

// 2️⃣ ĐỌC DATA (getItem)
// Đọc string
const username = localStorage.getItem('username');
console.log(username); // "John Doe"

// Đọc object (phải parse)
const userStr = localStorage.getItem('user');
const userObj = userStr ? JSON.parse(userStr) : null;
console.log(userObj); // { id: 1, name: 'John', role: 'admin' }

// Đọc array
const cartStr = localStorage.getItem('cart');
const cartArray = cartStr ? JSON.parse(cartStr) : [];
console.log(cartArray); // [{ id: 1, ... }, { id: 2, ... }]

// 3️⃣ XÓA DATA
// Xóa 1 item
localStorage.removeItem('username');

// Xóa tất cả
localStorage.clear();

// 4️⃣ CHECK TỒN TẠI
if (localStorage.getItem('user')) {
  console.log('User logged in');
} else {
  console.log('Guest');
}

// ============================================
// Thực Tế: LocalStorage Helper
// ============================================
class LocalStorageHelper {
  // Set data (tự động stringify)
  static set<T>(key: string, value: T): void {
    try {
      const serialized = JSON.stringify(value);
      localStorage.setItem(key, serialized);
    } catch (error) {
      console.error('LocalStorage set error:', error);
    }
  }
  
  // Get data (tự động parse)
  static get<T>(key: string, defaultValue: T | null = null): T | null {
    try {
      const item = localStorage.getItem(key);
      return item ? JSON.parse(item) : defaultValue;
    } catch (error) {
      console.error('LocalStorage get error:', error);
      return defaultValue;
    }
  }
  
  // Remove item
  static remove(key: string): void {
    localStorage.removeItem(key);
  }
  
  // Clear all
  static clear(): void {
    localStorage.clear();
  }
}

// Usage: Clean API
interface User {
  id: number;
  name: string;
  role: string;
}

const user: User = { id: 1, name: 'John', role: 'admin' };
LocalStorageHelper.set('user', user); // Tự stringify

const savedUser = LocalStorageHelper.get<User>('user'); // Tự parse
console.log(savedUser?.name); // "John"

LocalStorageHelper.remove('user'); // Xóa

// ============================================
// Use Case Thực Tế: Theme Switcher
// ============================================
function saveTheme(theme: 'light' | 'dark') {
  localStorage.setItem('theme', theme);
  document.body.className = theme; // Apply theme
}

function loadTheme() {
  const theme = localStorage.getItem('theme') || 'light';
  document.body.className = theme;
}

// On page load
loadTheme();

// On theme button click
document.getElementById('themeBtn')?.addEventListener('click', () => {
  const current = localStorage.getItem('theme') || 'light';
  const newTheme = current === 'light' ? 'dark' : 'light';
  saveTheme(newTheme);
});
```

---

#### **📝 3. SessionStorage - "Giấy Nháp - Đóng Tab Là Mất"**

**Đặc điểm:**
- Dung lượng: **5-10MB** (giống localStorage)
- **Mất khi đóng tab** (không persistent)
- **Sync API** - giống localStorage
- Dùng cho: **Form data, wizard steps, temporary state**

**Ưu điểm:**
- ✅ API giống localStorage (dễ học)
- ✅ Tự động dọn dẹp (đóng tab = xóa)
- ✅ Mỗi tab có storage riêng

**Nhược điểm:**
- ❌ Mất khi đóng tab (không persistent)
- ❌ Không share giữa tabs
- ❌ Sync API (block main thread)

**Code Example:**

```typescript
// ============================================
// SESSIONSTORAGE - Ví Dụ Đơn Giản
// ============================================

// API GIỐNG HỆT LOCALSTORAGE, CHỈ KHÁC TÊN!

// 1️⃣ LƯU DATA
sessionStorage.setItem('formData', JSON.stringify({
  step: 1,
  name: 'John',
  email: 'john@example.com'
}));

// 2️⃣ ĐỌC DATA
const formDataStr = sessionStorage.getItem('formData');
const formData = formDataStr ? JSON.parse(formDataStr) : null;
console.log(formData?.step); // 1

// 3️⃣ XÓA DATA
sessionStorage.removeItem('formData');
sessionStorage.clear(); // Xóa tất cả

// ============================================
// Use Case: Multi-Step Form (Wizard)
// ============================================
interface FormState {
  currentStep: number;
  data: {
    name?: string;
    email?: string;
    address?: string;
  };
}

class FormWizard {
  private static KEY = 'wizardState';
  
  // Lưu state hiện tại
  static saveState(state: FormState): void {
    sessionStorage.setItem(this.KEY, JSON.stringify(state));
  }
  
  // Đọc state (auto-load khi refresh page)
  static loadState(): FormState | null {
    const data = sessionStorage.getItem(this.KEY);
    return data ? JSON.parse(data) : null;
  }
  
  // Xóa state (sau khi submit)
  static clearState(): void {
    sessionStorage.removeItem(this.KEY);
  }
}

// Usage:
// Step 1: Save form data
FormWizard.saveState({
  currentStep: 1,
  data: { name: 'John', email: 'john@example.com' }
});

// User refresh page → auto-restore
const state = FormWizard.loadState();
if (state) {
  console.log(`Resume from step ${state.currentStep}`);
  // Fill form với data đã lưu
}

// Step 3: Submit success → clear
FormWizard.clearState();

// ============================================
// So Sánh LocalStorage vs SessionStorage
// ============================================

// Scenario 1: User settings (dùng localStorage)
localStorage.setItem('language', 'vi'); // Lưu mãi mãi
// → User quay lại sau 1 tháng vẫn thấy tiếng Việt

// Scenario 2: Shopping cart (dùng localStorage)
localStorage.setItem('cart', JSON.stringify(items)); // Lưu mãi mãi
// → User đóng tab rồi mở lại, cart vẫn còn

// Scenario 3: Form draft (dùng sessionStorage)
sessionStorage.setItem('draft', JSON.stringify(formData)); // Mất khi đóng tab
// → User đóng tab = mất draft (không spam localStorage)

// Scenario 4: Search filters (dùng sessionStorage)
sessionStorage.setItem('filters', JSON.stringify(filters)); // Per-tab
// → Mỗi tab có filter riêng, không conflict
```

---

#### **🗄️ 4. IndexedDB - "Kho Chứa Lớn - Database Trên Browser"**

**Đặc điểm:**
- Dung lượng: **50MB - unlimited** (chrome: 60% disk)
- **Async API** - không block UI
- **Database-like**: tables, indexes, queries, transactions
- Dùng cho: **Large datasets, offline apps, caching**

**Ưu điểm:**
- ✅ Dung lượng lớn (GB nếu user cho phép)
- ✅ Async (không block UI)
- ✅ Indexes, queries (như SQL)
- ✅ Transactions (ACID)

**Nhược điểm:**
- ❌ API phức tạp (callback hell)
- ❌ Khó học
- ❌ Overkill cho data nhỏ

**Code Example:**

```typescript
// ============================================
// INDEXEDDB - Ví Dụ Đơn Giản (Simplified với Promise)
// ============================================

// 1️⃣ MỞ DATABASE
function openDB(dbName: string, version: number = 1): Promise<IDBDatabase> {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open(dbName, version);
    
    // onupgradeneeded: Chạy khi tạo DB lần đầu hoặc upgrade version
    request.onupgradeneeded = (event) => {
      const db = (event.target as IDBOpenDBRequest).result;
      
      // Tạo "table" (gọi là objectStore)
      if (!db.objectStoreNames.contains('users')) {
        const store = db.createObjectStore('users', { keyPath: 'id' });
        // keyPath: 'id' → dùng field 'id' làm primary key
        
        // Tạo index (giống SQL index)
        store.createIndex('email', 'email', { unique: true });
        store.createIndex('name', 'name', { unique: false });
      }
    };
    
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

// 2️⃣ THÊM DATA (INSERT)
async function addUser(db: IDBDatabase, user: any): Promise<void> {
  return new Promise((resolve, reject) => {
    // Tạo transaction (như BEGIN TRANSACTION trong SQL)
    const tx = db.transaction('users', 'readwrite'); // readwrite = có thể ghi
    const store = tx.objectStore('users');
    
    // Thêm data
    const request = store.add(user);
    
    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

// 3️⃣ ĐỌC DATA (SELECT)
async function getUser(db: IDBDatabase, id: number): Promise<any> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readonly'); // readonly = chỉ đọc
    const store = tx.objectStore('users');
    
    const request = store.get(id); // Tìm theo primary key
    
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

// 4️⃣ ĐỌC TẤT CẢ (SELECT *)
async function getAllUsers(db: IDBDatabase): Promise<any[]> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readonly');
    const store = tx.objectStore('users');
    
    const request = store.getAll(); // Lấy tất cả
    
    request.onsuccess = () => resolve(request.result);
    request.onerror = () => reject(request.error);
  });
}

// 5️⃣ CẬP NHẬT (UPDATE)
async function updateUser(db: IDBDatabase, user: any): Promise<void> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readwrite');
    const store = tx.objectStore('users');
    
    const request = store.put(user); // put = thêm hoặc update
    
    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

// 6️⃣ XÓA (DELETE)
async function deleteUser(db: IDBDatabase, id: number): Promise<void> {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('users', 'readwrite');
    const store = tx.objectStore('users');
    
    const request = store.delete(id);
    
    request.onsuccess = () => resolve();
    request.onerror = () => reject(request.error);
  });
}

// ============================================
// USAGE - Sử Dụng Thực Tế
// ============================================
async function demo() {
  // Mở database
  const db = await openDB('MyAppDB', 1);
  
  // Thêm users
  await addUser(db, { id: 1, name: 'John', email: 'john@example.com' });
  await addUser(db, { id: 2, name: 'Jane', email: 'jane@example.com' });
  
  // Đọc 1 user
  const user = await getUser(db, 1);
  console.log(user); // { id: 1, name: 'John', email: 'john@example.com' }
  
  // Đọc tất cả users
  const users = await getAllUsers(db);
  console.log(users); // [{ id: 1, ... }, { id: 2, ... }]
  
  // Update user
  await updateUser(db, { id: 1, name: 'John Doe', email: 'john@example.com' });
  
  // Xóa user
  await deleteUser(db, 2);
  
  // Đóng database
  db.close();
}

demo();

// ============================================
// Use Case Thực Tế: Offline App
// ============================================
class OfflineCache {
  private db: IDBDatabase | null = null;
  
  async init() {
    this.db = await openDB('OfflineCache', 1);
  }
  
  // Cache API response
  async cacheArticle(article: any) {
    if (!this.db) return;
    await addUser(this.db, article);
  }
  
  // Get từ cache
  async getArticle(id: number) {
    if (!this.db) return null;
    return await getUser(this.db, id);
  }
}

// Usage:
const cache = new OfflineCache();
await cache.init();

// Online: Fetch từ API + cache
const article = await fetch('/api/article/1').then(r => r.json());
await cache.cacheArticle(article);

// Offline: Đọc từ cache
const cached = await cache.getArticle(1);
```

---

#### **🎯 Khi Nào Dùng Storage Nào?**

```typescript
// ============================================
// DECISION TREE - Chọn Storage Phù Hợp
// ============================================

function selectStorage(requirement: Requirement): Storage {
  // 1. Cần gửi server? → Cookie
  if (requirement.sendToServer) {
    return 'Cookie'; // Auth tokens, session IDs
  }
  
  // 2. Data lớn (>5MB)? → IndexedDB
  if (requirement.size > 5_000_000) {
    return 'IndexedDB'; // Images, videos, large datasets
  }
  
  // 3. Cần persistent (lưu mãi mãi)? → LocalStorage
  if (requirement.persistent) {
    return 'LocalStorage'; // Settings, preferences, cart
  }
  
  // 4. Temporary (đóng tab = mất)? → SessionStorage
  if (requirement.temporary) {
    return 'SessionStorage'; // Form drafts, wizard steps
  }
  
  // Default: LocalStorage
  return 'LocalStorage';
}

// ============================================
// Use Cases Thực Tế
// ============================================

// ✅ Cookie:
// - Authentication tokens (JWT)
// - Session IDs
// - User tracking, analytics

// ✅ LocalStorage:
// - User settings (theme, language)
// - Shopping cart
// - Cached data (API responses)
// - Recently viewed items

// ✅ SessionStorage:
// - Multi-step form data
// - Wizard progress
// - Search filters (per-tab)
// - Temporary state

// ✅ IndexedDB:
// - Offline apps (PWA)
// - Large datasets (1000+ items)
// - Images, videos
// - Full-text search indexes
```

---

#### **📋 Best Practices (Thực Hành Tốt)**

```typescript
// 1️⃣ ALWAYS TRY-CATCH (storage có thể full hoặc disabled)
function safeSetItem(key: string, value: any) {
  try {
    localStorage.setItem(key, JSON.stringify(value));
  } catch (error) {
    if (error instanceof DOMException && error.name === 'QuotaExceededError') {
      console.error('Storage full!');
      // Clear old data hoặc notify user
    }
  }
}

// 2️⃣ CHECK AVAILABILITY
function isLocalStorageAvailable(): boolean {
  try {
    const test = '__test__';
    localStorage.setItem(test, test);
    localStorage.removeItem(test);
    return true;
  } catch {
    return false; // User disabled hoặc browser không support
  }
}

// 3️⃣ NAMESPACE KEYS (tránh conflict)
const STORAGE_PREFIX = 'myapp_';

function setAppData(key: string, value: any) {
  localStorage.setItem(STORAGE_PREFIX + key, JSON.stringify(value));
}

function getAppData(key: string) {
  const item = localStorage.getItem(STORAGE_PREFIX + key);
  return item ? JSON.parse(item) : null;
}

// Usage:
setAppData('user', { name: 'John' }); // Lưu: "myapp_user"

// 4️⃣ VERSIONING (để migration)
interface StorageData<T> {
  version: number;
  data: T;
}

function setVersionedData<T>(key: string, data: T, version: number = 1) {
  const wrapper: StorageData<T> = { version, data };
  localStorage.setItem(key, JSON.stringify(wrapper));
}

function getVersionedData<T>(key: string, currentVersion: number): T | null {
  const item = localStorage.getItem(key);
  if (!item) return null;
  
  const wrapper: StorageData<T> = JSON.parse(item);
  
  if (wrapper.version !== currentVersion) {
    // Migration logic here
    console.warn('Old data version, migrating...');
    return null;
  }
  
  return wrapper.data;
}

// 5️⃣ EXPIRY for LocalStorage (giống cookie)
interface CachedData<T> {
  data: T;
  expiry: number; // timestamp
}

function setWithExpiry<T>(key: string, value: T, ttlMs: number) {
  const item: CachedData<T> = {
    data: value,
    expiry: Date.now() + ttlMs,
  };
  localStorage.setItem(key, JSON.stringify(item));
}

function getWithExpiry<T>(key: string): T | null {
  const itemStr = localStorage.getItem(key);
  if (!itemStr) return null;
  
  const item: CachedData<T> = JSON.parse(itemStr);
  
  // Check expiry
  if (Date.now() > item.expiry) {
    localStorage.removeItem(key); // Expired, xóa đi
    return null;
  }
  
  return item.data;
}

// Usage: Cache API response trong 1 giờ
setWithExpiry('apiCache', { users: [...] }, 60 * 60 * 1000); // 1 hour

const cached = getWithExpiry('apiCache');
if (cached) {
  console.log('Use cache');
} else {
  console.log('Cache expired, fetch new');
}
```

---

#### **❌ Common Mistakes (Lỗi Thường Gặp)**

```typescript
// ❌ LỖI 1: Lưu object trực tiếp (không stringify)
localStorage.setItem('user', { name: 'John' }); // ❌ Lưu "[object Object]"

// ✅ ĐÚNG: Stringify trước
localStorage.setItem('user', JSON.stringify({ name: 'John' }));

// ❌ LỖI 2: Quên parse khi đọc
const user = localStorage.getItem('user'); // ❌ user là string!
console.log(user.name); // undefined

// ✅ ĐÚNG: Parse sau khi đọc
const userStr = localStorage.getItem('user');
const user = userStr ? JSON.parse(userStr) : null;
console.log(user?.name); // "John"

// ❌ LỖI 3: Lưu sensitive data vào localStorage
localStorage.setItem('password', 'secret123'); // ❌ Không secure!

// ✅ ĐÚNG: Chỉ lưu non-sensitive data
// Sensitive data (passwords, credit cards) → server session hoặc httpOnly cookie

// ❌ LỖI 4: Không check quota exceeded
for (let i = 0; i < 10000; i++) {
  localStorage.setItem(`key${i}`, 'x'.repeat(1000)); // ❌ Có thể full!
}

// ✅ ĐÚNG: Try-catch
try {
  localStorage.setItem('key', largeData);
} catch (error) {
  if (error.name === 'QuotaExceededError') {
    console.error('Storage full, clearing old data');
    localStorage.clear();
  }
}

// ❌ LỖI 5: Dùng IndexedDB cho data nhỏ
await openDB(...); // ❌ Overkill cho lưu 1 string
await addUser(db, { name: 'John' });

// ✅ ĐÚNG: LocalStorage cho data nhỏ
localStorage.setItem('name', 'John'); // Đơn giản hơn nhiều

// ❌ LỖI 6: Quên đóng IndexedDB connection
const db = await openDB('MyDB', 1);
// ... use db
// ❌ Không đóng → memory leak

// ✅ ĐÚNG: Luôn đóng
const db = await openDB('MyDB', 1);
try {
  // ... use db
} finally {
  db.close(); // Always close
}
```

---

#### **💡 Summary (Tóm Tắt)**

**Cookie 🍪**
- **4KB**, gửi kèm mọi request, có expiry
- **Dùng cho**: Auth tokens, session IDs
- **API**: `document.cookie`

**LocalStorage 💾**
- **5-10MB**, lưu mãi mãi, sync API
- **Dùng cho**: Settings, preferences, cart
- **API**: `localStorage.getItem/setItem`

**SessionStorage 📝**
- **5-10MB**, mất khi đóng tab, sync API
- **Dùng cho**: Form drafts, temporary state
- **API**: `sessionStorage.getItem/setItem`

**IndexedDB 🗄️**
- **50MB+**, async, database-like
- **Dùng cho**: Large datasets, offline apps
- **API**: `indexedDB.open`, transactions, objectStores

**Key Takeaway:**
- Data nhỏ + simple → **LocalStorage/SessionStorage**
- Gửi server → **Cookie**
- Data lớn + complex → **IndexedDB**
- Luôn **try-catch**, **check availability**, **namespace keys**

---
</details>