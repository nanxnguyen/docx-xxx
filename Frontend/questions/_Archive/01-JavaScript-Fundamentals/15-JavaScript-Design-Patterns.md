# 🏗️ Q60: JavaScript Design Patterns for Frontend Development

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Design patterns: Singleton (1 instance - 1 thể hiện duy nhất), Observer (subscribe changes - đăng ký theo dõi thay đổi), Factory (create objects - tạo đối tượng), Module (encapsulation - đóng gói), Pub/Sub (event-driven - giao tiếp dựa trên sự kiện), Dependency Injection (loose coupling - liên kết lỏng lẻo). Modern: Hooks patterns (mẫu hooks), Compound Components (component kết hợp)."**

**🔑 6 Essential Patterns (6 Mẫu Thiết Kế Cốt Lõi):**

**1. Singleton - Single Instance (Thể Hiện Duy Nhất):**

- **Use case (Trường hợp sử dụng)**: Database connection (kết nối cơ sở dữ liệu), config object (đối tượng cấu hình), logger (hệ thống ghi log)
- **JS**: Module exports object (auto-singleton - module xuất đối tượng tự động singleton), class với static instance (lớp với thể hiện tĩnh)
- **Caution (Lưu ý)**: Hard to test (khó kiểm thử - do global state - trạng thái toàn cục), avoid unless necessary (tránh trừ khi thực sự cần thiết)

**2. Observer - Subscribe to Changes (Đăng Ký Theo Dõi Thay Đổi):**

- **Use case**: Event listeners (bộ lắng nghe sự kiện), state management (quản lý trạng thái), reactive programming (lập trình phản ứng)
- **Pattern**: Subject maintains observers list (Chủ thể duy trì danh sách người quan sát), notify on change (thông báo khi có thay đổi)
- **Modern**: RxJS Observables, MobX, Vue reactivity (tính phản ứng của Vue)

**3. Pub/Sub (Publish-Subscribe - Xuất Bản/Đăng Ký):**

- **Khác Observer**: Decoupled (tách rời - event bus giữa publisher/subscriber - bus sự kiện giữa người xuất bản và người đăng ký)
- **Use case**: Cross-component communication (giao tiếp giữa các component), analytics events (sự kiện phân tích)
- **Implementation (Triển khai)**: EventEmitter, window.postMessage, Redux

**4. Factory - Object Creation (Tạo Đối Tượng):**

- **Use case**: Create objects without specifying exact class (Tạo đối tượng mà không cần chỉ định lớp cụ thể)
- **Example**: `React.createElement()`, component factories (nhà máy component)
- **Benefits (Lợi ích)**: Flexibility (linh hoạt), hide complexity (ẩn độ phức tạp)

**5. Module Pattern - Encapsulation (Đóng Gói):**

- **ES6 Modules**: `export/import` - native encapsulation (đóng gói tự nhiên)
- **IIFE**: `(function(){ ... })()` - private scope (phạm vi riêng tư - legacy - cũ)
- **Use case**: Libraries (thư viện), utilities (tiện ích), prevent global pollution (ngăn chặn ô nhiễm toàn cục)

**6. Dependency Injection (Tiêm Phụ Thuộc):**

- **Pattern**: Pass dependencies (không hard-code - truyền phụ thuộc, không mã hóa cứng)
- **Use case**: Testing (mock dependencies - kiểm thử với phụ thuộc giả), loose coupling (liên kết lỏng lẻo)
- **React**: Props, Context API, custom hooks (hooks tùy chỉnh)

**🔑 Modern React Patterns (Mẫu React Hiện Đại):**

- **Compound Components (Component Kết Hợp)**: `<Select>` + `<Option>` share state (chia sẻ trạng thái)
- **Render Props (Props Render)**: `<DataProvider render={data => ...} />` - truyền function render như prop
- **Higher-Order Components (HOC - Component Bậc Cao)**: `withAuth(Component)` - bọc component với logic xác thực
- **Custom Hooks (Hooks Tùy Chỉnh)**: `useAuth()`, `useFetch()` - reusable logic (logic tái sử dụng)

**⚠️ Lỗi Thường Gặp (Common Mistakes):**

- Over-engineering (Kỹ thuật quá mức): Dùng patterns không cần thiết → complexity (độ phức tạp)
- Singleton abuse (Lạm dụng Singleton) → global state (trạng thái toàn cục), hard test (khó kiểm thử)
- Observer memory leaks (Rò rỉ bộ nhớ Observer) → forget unsubscribe (quên hủy đăng ký)
- Pub/Sub không type-safe (không an toàn kiểu) → dùng TypeScript event types (kiểu sự kiện TypeScript)

**💡 Kiến Thức Senior (Senior Knowledge):**

- **Strategy Pattern (Mẫu Chiến Lược)**: Interchangeable algorithms (thuật toán có thể thay thế - sort strategies - chiến lược sắp xếp, payment methods - phương thức thanh toán)
- **Command Pattern (Mẫu Lệnh)**: Undo/redo functionality (chức năng hoàn tác/làm lại - Redux actions)
- **Proxy Pattern (Mẫu Proxy)**: ES6 Proxy cho reactivity (tính phản ứng - Vue 3, MobX)
- **Facade Pattern (Mẫu Mặt Tiền)**: Simplify complex APIs (đơn giản hóa API phức tạp - Axios wraps fetch, jQuery wraps DOM)

**❓ Câu Hỏi:**

Giải thích các Design Patterns phổ biến trong JavaScript/TypeScript frontend: Singleton, Observer, Factory, Module, Pub/Sub, Prototype, Dependency Injection. Khi nào nên dùng pattern nào?

---

## **📊 DESIGN PATTERNS OVERVIEW**

```
┌──────────────────────────────────────────────────────────────┐
│          JAVASCRIPT DESIGN PATTERNS (Gang of Four + Modern)  │
│          (CÁC MẪU THIẾT KẾ JAVASCRIPT - Gang of Four + Hiện Đại) │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  🏗️ CREATIONAL PATTERNS (Object Creation - Mẫu Tạo Đối Tượng)                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Singleton     - Đảm bảo chỉ 1 instance duy nhất    │ │
│  │  • Factory       - Tạo objects mà không chỉ định class│ │
│  │  • Prototype     - Clone objects từ prototype         │ │
│  │  • Builder       - Xây dựng complex objects từng bước │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  🔗 STRUCTURAL PATTERNS (Object Relationships - Mẫu Quan Hệ Đối Tượng)               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Module        - Encapsulation (Đóng gói), private/public API   │ │
│  │  • Decorator     - Thêm behavior vào objects (Thêm hành vi vào đối tượng)          │ │
│  │  • Facade        - Simplified interface (Giao diện đơn giản hóa)               │ │
│  │  • Proxy         - Control access to objects (Kiểm soát truy cập đối tượng)          │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  📡 BEHAVIORAL PATTERNS (Object Communication - Mẫu Giao Tiếp Đối Tượng)               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Observer      - Subscribe to object changes (Đăng ký theo dõi thay đổi)         │ │
│  │  • Pub/Sub       - Event-driven communication (Giao tiếp dựa trên sự kiện)         │ │
│  │  • Strategy      - Interchangeable algorithms (Thuật toán có thể thay thế)         │ │
│  │  • Command       - Encapsulate requests as objects (Đóng gói yêu cầu thành đối tượng)    │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## **1️⃣ SINGLETON PATTERN - Single Instance**

```typescript
// ===================================================
// 🎯 SINGLETON - Đảm bảo chỉ có 1 instance duy nhất
// ===================================================

/**
 * Use Cases (Trường hợp sử dụng):
 * - Global state management (Quản lý trạng thái toàn cục - Redux store)
 * - Logger service (Dịch vụ ghi log)
 * - Database connection (Kết nối cơ sở dữ liệu)
 * - API client (Ứng dụng khách API)
 * - Configuration manager (Trình quản lý cấu hình)
 */

// ===================================================
// ❌ BAD: Multiple instances (not Singleton)
// ===================================================

class ApiClient {
  constructor(private baseUrl: string) {} // baseUrl: địa chỉ cơ sở của API

  async get(endpoint: string) {
    // endpoint: điểm cuối API
    return fetch(`${this.baseUrl}${endpoint}`); // Gửi request GET
  }
}

// Problem (Vấn đề): Creates new instance every time! (Tạo thể hiện mới mỗi lần!)
const api1 = new ApiClient('https://api.example.com');
const api2 = new ApiClient('https://api.example.com');
// api1 !== api2 (different instances - các thể hiện khác nhau, waste memory - lãng phí bộ nhớ)

// ===================================================
// ✅ GOOD: Singleton Pattern (Classic ES6 Class)
// ===================================================

class ApiClient {
  private static instance: ApiClient; // 👉 Static instance (duy nhất)
  private baseUrl: string;

  // 🔒 Private constructor (cannot use `new` outside class - Không thể new từ bên ngoài)
  private constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  // 🎯 Public method to get the single instance (Lấy instance duy nhất)
  public static getInstance(
    baseUrl: string = 'https://api.example.com'
  ): ApiClient {
    if (!ApiClient.instance) {
      // ❓ Chưa có instance
      ApiClient.instance = new ApiClient(baseUrl); // ✅ Tạo instance mới
    }
    return ApiClient.instance; // 🔁 Trả về instance hiện tại
  }

  async get(endpoint: string) {
    // 📥 GET request (Gửi request GET)
    const response = await fetch(`${this.baseUrl}${endpoint}`); // Gọi fetch API
    return response.json(); // Trả về dữ liệu JSON
  }

  public async post(endpoint: string, data: any) {
    // 📤 POST request (Gửi request POST)
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST', // Phương thức POST
      headers: { 'Content-Type': 'application/json' }, // 📝 JSON header (Header JSON)
      body: JSON.stringify(data), // 📦 Serialize data (Chuyển đổi dữ liệu thành JSON string)
    });
    return response.json(); // Trả về dữ liệu JSON
  }
}

// 📝 Usage
const api1 = ApiClient.getInstance();
const api2 = ApiClient.getInstance();
console.log(api1 === api2); // ✅ true (same instance - Cùng 1 instance!)

// ===================================================
// ✅ MODERN: Singleton with Module (ES6 Modules)
// ===================================================

// 📄 apiClient.ts
class ApiClient {
  constructor(private baseUrl: string) {} // 🎯 Constructor đơn giản

  async get(endpoint: string) {
    // 📥 GET request
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    return response.json();
  }
}

// 📦 Export single instance (Singleton via module caching)
// ES modules được cache tự động, nên chỉ có 1 instance
export const apiClient = new ApiClient('https://api.example.com');

// 📄 app.ts
import { apiClient } from './apiClient'; // 📥 Import instance

// ✅ Always the same instance (ES modules cached by default)
apiClient.get('/users'); // 👥 Lấy danh sách users

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Logger Singleton
// ===================================================

type LogLevel = 'debug' | 'info' | 'warn' | 'error'; // 🏷️ Các mức log

class Logger {
  private static instance: Logger; // 👉 Static instance
  private logs: Array<{ level: LogLevel; message: string; timestamp: Date }> =
    []; // 📊 Lưu tất cả logs

  private constructor() {} // 🔒 Private constructor

  public static getInstance(): Logger {
    // 🎯 Lấy instance
    if (!Logger.instance) {
      Logger.instance = new Logger();
    }
    return Logger.instance;
  }

  private log(level: LogLevel, message: string) {
    // 📝 Log function chính
    const logEntry = {
      level,
      message,
      timestamp: new Date(), // ⏱️ Thời gian log
    };

    this.logs.push(logEntry); // 📥 Lưu vào array

    // 🎨 Console output with colors (In ra console với màu sắc)
    const colors = {
      debug: '\x1b[36m', // 💙 Cyan - Màu xanh nhạt
      info: '\x1b[32m', // 🟢 Green - Màu xanh lá
      warn: '\x1b[33m', // 🟡 Yellow - Màu vàng
      error: '\x1b[31m', // 🔴 Red - Màu đỏ
    };

    console.log(`${colors[level]}[${level.toUpperCase()}]\x1b[0m ${message}`);
  }

  public debug(message: string) {
    // 💙 Debug level (Mức debug - thông tin gỡ lỗi)
    this.log('debug', message); // Gọi hàm log với level debug
  }

  public info(message: string) {
    // 🟢 Info level (Mức thông tin)
    this.log('info', message); // Gọi hàm log với level info
  }

  public warn(message: string) {
    // 🟡 Warning level (Mức cảnh báo)
    this.log('warn', message); // Gọi hàm log với level warn
  }

  public error(message: string) {
    // 🔴 Error level (Mức lỗi)
    this.log('error', message); // Gọi hàm log với level error
  }

  public getLogs() {
    // 📊 Lấy tất cả logs (Trả về tất cả các log đã ghi)
    return this.logs; // Trả về mảng logs
  }
}

// 📝 Usage
const logger = Logger.getInstance();
logger.info('App started'); // 🟢 [INFO] App started
logger.error('Failed to fetch data'); // 🔴 [ERROR] Failed to fetch data
logger.getLogs(); // 📊 All logs from entire app
```

---

## **2️⃣ OBSERVER PATTERN - Subscribe to Changes**

```typescript
// ===================================================
// 📡 OBSERVER PATTERN - Notify subscribers on changes
// ===================================================

/**
 * Use Cases (Trường hợp sử dụng):
 * - React state management (Quản lý trạng thái React - useState triggers re-render - useState kích hoạt render lại)
 * - Event listeners (Bộ lắng nghe sự kiện - addEventListener)
 * - Real-time data updates (Cập nhật dữ liệu thời gian thực - stock prices - giá cổ phiếu, chat - trò chuyện)
 * - Model-View synchronization (Đồng bộ hóa Model-View)
 */

// ===================================================
// ✅ IMPLEMENTATION: Subject (Observable) + Observers
// ===================================================

interface Observer {
  update(data: any): void; // 🔄 Phương thức nhận update
}

class Subject {
  private observers: Observer[] = []; // 📊 Danh sách observers

  // 🔔 Subscribe to changes (Đăng ký nhận thông báo)
  public subscribe(observer: Observer): void {
    this.observers.push(observer); // 📥 Thêm vào danh sách
  }

  // 🚫 Unsubscribe (Hủy đăng ký)
  public unsubscribe(observer: Observer): void {
    const index = this.observers.indexOf(observer);
    if (index > -1) {
      this.observers.splice(index, 1); // 🗑️ Xóa khỏi danh sách
    }
  }

  // 📢 Notify all observers (Thông báo cho tất cả observers)
  protected notify(data: any): void {
    this.observers.forEach((observer) => observer.update(data)); // 🔁 Gọi update cho từng observer
  }
}

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Stock Price Tracker (Theo dõi giá cổ phiếu)
// ===================================================

class Stock extends Subject {
  private price: number = 0; // 💵 Giá hiện tại
  private name: string; // 🏷️ Tên cổ phiếu

  constructor(name: string, initialPrice: number) {
    super();
    this.name = name;
    this.price = initialPrice;
  }

  public setPrice(newPrice: number): void {
    // 💰 Đổi giá (Cập nhật giá mới)
    console.log(`${this.name} price changed: $${this.price} → $${newPrice}`); // In log thay đổi giá
    this.price = newPrice; // Cập nhật giá mới
    this.notify({ name: this.name, price: newPrice }); // 📢 Thông báo cho observers (Gửi thông báo đến tất cả observers)
  }

  public getPrice(): number {
    // 📊 Lấy giá (Trả về giá hiện tại)
    return this.price; // Trả về giá
  }
}

// 📺 Observer 1: Display widget (Hiển thị)
class PriceDisplay implements Observer {
  constructor(private elementId: string) {} // 🎯 Element ID để hiển thị

  update(data: { name: string; price: number }): void {
    const element = document.getElementById(this.elementId);
    if (element) {
      element.textContent = `${data.name}: $${data.price}`; // 📝 Cập nhật text
    }
  }
}

// 🔔 Observer 2: Alert service (Cảnh báo)
class PriceAlert implements Observer {
  constructor(private threshold: number) {} // 🚨 Ngưỡng giá

  update(data: { name: string; price: number }): void {
    if (data.price > this.threshold) {
      // ❗ Vượt ngưỡng
      alert(`${data.name} exceeded $${this.threshold}!`); // 🔔 Cảnh báo
    }
  }
}

// 📝 Observer 3: Logger (Ghi log)
class PriceLogger implements Observer {
  update(data: { name: string; price: number }): void {
    console.log(
      `[LOG] ${new Date().toISOString()} - ${data.name}: $${data.price}`
    ); // 📊 Ghi log với timestamp
  }
}

// Usage (Cách sử dụng)
const appleStock = new Stock('AAPL', 150); // Tạo cổ phiếu Apple với giá ban đầu $150

const display = new PriceDisplay('stock-display'); // Widget hiển thị giá
const alert = new PriceAlert(200); // Cảnh báo khi giá vượt $200
const logger = new PriceLogger(); // Ghi log giá

// Subscribe observers (Đăng ký các observer)
appleStock.subscribe(display); // Đăng ký widget hiển thị
appleStock.subscribe(alert); // Đăng ký cảnh báo
appleStock.subscribe(logger); // Đăng ký logger

// Update price → all observers notified! (Cập nhật giá → tất cả observer được thông báo!)
appleStock.setPrice(180); // Display updates (hiển thị cập nhật), logger logs (logger ghi log)
appleStock.setPrice(210); // Display updates, alert fires (cảnh báo kích hoạt), logger logs

// Unsubscribe (Hủy đăng ký)
appleStock.unsubscribe(alert); // Hủy đăng ký cảnh báo
appleStock.setPrice(220); // Only display and logger notified (Chỉ hiển thị và logger được thông báo)
```

---

## **3️⃣ PUB/SUB PATTERN - Event-Driven Communication**

```typescript
// ===================================================
// 📢 PUB/SUB PATTERN - Decoupled Event System
// ===================================================

/**
 * Difference from Observer (Khác biệt so với Observer):
 * - Observer: Subject knows its observers (Chủ thể biết các observer của nó - tight coupling - liên kết chặt chẽ)
 * - Pub/Sub: Publishers/Subscribers don't know each other (Người xuất bản/Người đăng ký không biết nhau - loose coupling - liên kết lỏng lẻo)
 *
 * Use Cases (Trường hợp sử dụng):
 * - Global events (Sự kiện toàn cục - analytics tracking - theo dõi phân tích)
 * - Cross-component communication (Giao tiếp giữa các component)
 * - Microservices messaging (Nhắn tin giữa các microservice)
 */

// ===================================================
// ✅ IMPLEMENTATION: Event Bus (Pub/Sub Mediator - Trung gian sự kiện)
// ===================================================

type EventCallback = (data?: any) => void; // 🔗 Callback function cho sự kiện

class EventBus {
  private events: Map<string, EventCallback[]> = new Map(); // 📊 Lưu danh sách events và callbacks

  // 🔔 Subscribe to event (Đăng ký lắng nghe sự kiện)
  public on(event: string, callback: EventCallback): () => void {
    if (!this.events.has(event)) {
      // ❓ Chưa có event này
      this.events.set(event, []); // 🆕 Tạo array mới
    }

    this.events.get(event)!.push(callback); // 📥 Thêm callback vào danh sách

    // 🔁 Return unsubscribe function (Trả về hàm hủy đăng ký)
    return () => this.off(event, callback);
  }

  // 🚫 Unsubscribe from event (Hủy đăng ký)
  public off(event: string, callback: EventCallback): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      const index = callbacks.indexOf(callback);
      if (index > -1) {
        callbacks.splice(index, 1); // 🗑️ Xóa callback
      }
    }
  }

  // 📢 Publish event (Phát sự kiện)
  public emit(event: string, data?: any): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.forEach((callback) => callback(data)); // 🔁 Gọi tất cả callbacks
    }
  }

  // 1️⃣ Subscribe once (auto-unsubscribe after first call - Tự động hủy sau lần đầu)
  public once(event: string, callback: EventCallback): void {
    const onceCallback = (data?: any) => {
      callback(data);
      this.off(event, onceCallback); // 🚫 Tự động hủy sau khi chạy
    };
    this.on(event, onceCallback);
  }
}

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Shopping Cart (Giỏ hàng)
// ===================================================

// 🌐 Global event bus
const eventBus = new EventBus();

// 📤 Publisher: ProductCard component
class ProductCard {
  addToCart(product: { id: string; name: string; price: number }) {
    eventBus.emit('product:added', product); // 📢 Phát sự kiện
  }
}

// 📥 Subscriber 1: CartWidget (Widget giỏ hàng)
class CartWidget {
  private itemCount: number = 0; // 📊 Số lượng sản phẩm

  constructor() {
    eventBus.on('product:added', (product) => {
      // 🔔 Lắng nghe sự kiện
      this.itemCount++; // ➡️ Tăng số lượng
      this.updateUI(); // 🔄 Cập nhật UI
      console.log(`Cart updated: ${this.itemCount} items`);
    });
  }

  private updateUI() {
    const badge = document.getElementById('cart-badge');
    if (badge) {
      badge.textContent = String(this.itemCount); // 📝 Cập nhật badge
    }
  }
}

// 📊 Subscriber 2: Analytics (Phân tích)
class Analytics {
  constructor() {
    eventBus.on('product:added', (product) => {
      // 🔔 Lắng nghe
      this.trackEvent('add_to_cart', {
        // 📊 Theo dõi sự kiện
        product_id: product.id,
        product_name: product.name,
        price: product.price,
      });
    });
  }

  private trackEvent(eventName: string, data: any) {
    console.log(`[Analytics] ${eventName}:`, data);
    // 📤 Send to Google Analytics, Mixpanel, etc.
  }
}

// 🔔 Subscriber 3: Toast Notification (Thông báo)
class ToastNotifier {
  constructor() {
    eventBus.on('product:added', (product) => {
      // 🔔 Lắng nghe
      this.showToast(`${product.name} added to cart!`); // 🔔 Hiển thị thông báo
    });
  }

  private showToast(message: string) {
    console.log(`🔔 ${message}`);
    // 💬 Show toast UI
  }
}

// Usage (Cách sử dụng)
const productCard = new ProductCard(); // Component thẻ sản phẩm
const cartWidget = new CartWidget(); // Widget giỏ hàng
const analytics = new Analytics(); // Dịch vụ phân tích
const toastNotifier = new ToastNotifier(); // Dịch vụ thông báo

// Add product → all subscribers notified! (Thêm sản phẩm → tất cả người đăng ký được thông báo!)
productCard.addToCart({ id: '123', name: 'Laptop', price: 999 }); // Thêm laptop vào giỏ
// Output (Kết quả):
// [Analytics] add_to_cart: { product_id: '123', ... } // Phân tích ghi nhận
// Cart updated: 1 items // Giỏ hàng cập nhật: 1 sản phẩm
// 🔔 Laptop added to cart! // Thông báo: Laptop đã được thêm vào giỏ!

// ===================================================
// 🎯 REACT EXAMPLE: Custom Event Hook
// ===================================================

import { useEffect } from 'react';

// Custom hook for event subscription (Hook tùy chỉnh để đăng ký sự kiện)
function useEventBus(event: string, callback: EventCallback) {
  useEffect(() => {
    const unsubscribe = eventBus.on(event, callback); // Đăng ký sự kiện
    return unsubscribe; // Cleanup on unmount (Dọn dẹp khi component bị gỡ)
  }, [event, callback]); // Phụ thuộc: event và callback
}

// React component (Component React)
function CartBadge() {
  const [count, setCount] = useState(0); // Trạng thái đếm số lượng

  useEventBus('product:added', () => {
    // Lắng nghe sự kiện thêm sản phẩm
    setCount((prev) => prev + 1); // Tăng số lượng lên 1
  });

  return <span className="badge">{count}</span>; // Hiển thị số lượng
}
```

---

## **4️⃣ FACTORY PATTERN - Object Creation**

```typescript
// ===================================================
// 🏭 FACTORY PATTERN - Create objects without specifying class
// ===================================================

/**
 * Use Cases (Trường hợp sử dụng):
 * - Create different types of objects based on input (Tạo các loại đối tượng khác nhau dựa trên đầu vào)
 * - Encapsulate complex creation logic (Đóng gói logic tạo phức tạp)
 * - Plugin systems (Hệ thống plugin - load different implementations - tải các triển khai khác nhau)
 */

// ===================================================
// ❌ BAD: Conditional object creation (messy)
// ===================================================

function createButton(type: string) {
  if (type === 'primary') {
    return {
      render() {
        return '<button class="btn-primary">Click</button>';
      },
    };
  } else if (type === 'secondary') {
    return {
      render() {
        return '<button class="btn-secondary">Click</button>';
      },
    };
  } else if (type === 'danger') {
    return {
      render() {
        return '<button class="btn-danger">Click</button>';
      },
    };
  }
  // Gets messy with many types! (Trở nên lộn xộn với nhiều loại!)
}

// ===================================================
// ✅ GOOD: Factory Pattern (Mẫu Factory)
// ===================================================

interface Button {
  // Interface định nghĩa contract cho Button
  render(): string; // 🎨 Render HTML (Trả về HTML của button)
  onClick(): void; // 🖌️ Xử lý click (Xử lý sự kiện click)
}

class PrimaryButton implements Button {
  // Button chính (màu xanh lá)
  render(): string {
    // 🟢 Button xanh lá (primary) - Trả về HTML button chính
    return '<button class="btn-primary">Click</button>'; // HTML button với class primary
  }

  onClick(): void {
    // 🖌️ Primary action (Hành động chính)
    console.log('Primary action'); // In log: hành động chính
  }
}

class SecondaryButton implements Button {
  // Button phụ (màu xanh)
  render(): string {
    // 🔵 Button xanh (secondary) - Trả về HTML button phụ
    return '<button class="btn-secondary">Click</button>'; // HTML button với class secondary
  }

  onClick(): void {
    // 🖌️ Secondary action (Hành động phụ)
    console.log('Secondary action'); // In log: hành động phụ
  }
}

class DangerButton implements Button {
  // Button nguy hiểm (màu đỏ)
  render(): string {
    // 🔴 Button đỏ (danger) - Trả về HTML button nguy hiểm
    return '<button class="btn-danger">Delete</button>'; // HTML button với class danger
  }

  onClick(): void {
    // ⚠️ Danger action - cần confirm (Hành động nguy hiểm - cần xác nhận)
    if (confirm('Are you sure?')) {
      // ❓ Xác nhận (Hiển thị hộp thoại xác nhận)
      console.log('Deleted!'); // 🗑️ Xóa (In log: đã xóa)
    }
  }
}

// Factory class (Lớp Factory - Nhà máy tạo button)
class ButtonFactory {
  static createButton(type: 'primary' | 'secondary' | 'danger'): Button {
    switch (
      type // Kiểm tra loại button
    ) {
      case 'primary':
        return new PrimaryButton(); // Tạo button chính
      case 'secondary':
        return new SecondaryButton(); // Tạo button phụ
      case 'danger':
        return new DangerButton(); // Tạo button nguy hiểm
      default:
        throw new Error(`Unknown button type: ${type}`); // Lỗi: loại button không xác định
    }
  }
}

// Usage (Cách sử dụng)
const btn1 = ButtonFactory.createButton('primary'); // Tạo button chính
const btn2 = ButtonFactory.createButton('danger'); // Tạo button nguy hiểm

console.log(btn1.render()); // <button class="btn-primary">...</button> // In HTML của button
btn2.onClick(); // Shows confirm dialog (Hiển thị hộp thoại xác nhận)

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Notification Factory
// ===================================================

interface Notification {
  // Interface định nghĩa contract cho Notification
  send(message: string): void; // Phương thức gửi thông báo với nội dung message
}

class EmailNotification implements Notification {
  // Thông báo qua Email
  constructor(private email: string) {} // email: địa chỉ email người nhận

  send(message: string): void {
    console.log(`📧 Email sent to ${this.email}: ${message}`); // Gửi email đến địa chỉ
    // Send email via SMTP/API (Gửi email qua SMTP/API)
  }
}

class SMSNotification implements Notification {
  // Thông báo qua SMS
  constructor(private phone: string) {} // phone: số điện thoại người nhận

  send(message: string): void {
    console.log(`📱 SMS sent to ${this.phone}: ${message}`); // Gửi SMS đến số điện thoại
    // Send SMS via Twilio/API (Gửi SMS qua Twilio/API)
  }
}

class PushNotification implements Notification {
  // Thông báo đẩy
  constructor(private deviceToken: string) {} // deviceToken: token thiết bị

  send(message: string): void {
    console.log(`🔔 Push sent to ${this.deviceToken}: ${message}`); // Gửi thông báo đẩy đến thiết bị
    // Send push via Firebase/OneSignal (Gửi thông báo đẩy qua Firebase/OneSignal)
  }
}

class NotificationFactory {
  // Factory tạo các loại Notification
  static create(
    // Phương thức tĩnh tạo Notification
    type: 'email' | 'sms' | 'push', // Loại thông báo: email, sms, hoặc push
    recipient: string // Người nhận: email, số điện thoại, hoặc device token
  ): Notification {
    switch (
      type // Kiểm tra loại thông báo
    ) {
      case 'email':
        return new EmailNotification(recipient); // Tạo EmailNotification
      case 'sms':
        return new SMSNotification(recipient); // Tạo SMSNotification
      case 'push':
        return new PushNotification(recipient); // Tạo PushNotification
      default:
        throw new Error(`Unknown notification type: ${type}`); // Lỗi: loại không xác định
    }
  }
}

// Usage (Cách sử dụng)
const notifier1 = NotificationFactory.create('email', 'user@example.com'); // Tạo thông báo email
const notifier2 = NotificationFactory.create('sms', '+1234567890'); // Tạo thông báo SMS

notifier1.send('Your order has shipped!'); // Gửi email: Đơn hàng của bạn đã được gửi!
notifier2.send('Your verification code is 123456'); // Gửi SMS: Mã xác minh của bạn là 123456
```

---

## **5️⃣ MODULE PATTERN - Encapsulation**

```typescript
// ===================================================
// 📦 MODULE PATTERN - Private/Public API
// ===================================================

/**
 * Use Cases (Trường hợp sử dụng):
 * - Create private scope (Tạo phạm vi riêng tư - before ES6 modules - trước ES6 modules)
 * - Encapsulate implementation details (Đóng gói chi tiết triển khai)
 * - Expose only public API (Chỉ hiển thị API công khai)
 */

// ===================================================
// ❌ PROBLEM: No Encapsulation (Global Variables)
// ===================================================

var counter = 0;

function increment() {
  counter++;
}

function getCount() {
  return counter;
}

// Problem (Vấn đề): `counter` is globally accessible! (`counter` có thể truy cập toàn cục!)
counter = 999; // ❌ Can be modified directly! (Có thể sửa đổi trực tiếp!)

// ===================================================
// ✅ SOLUTION: Module Pattern (IIFE - Immediately Invoked Function Expression)
// ===================================================

const CounterModule = (function () {
  // IIFE - Immediately Invoked Function Expression (Biểu thức hàm được gọi ngay)
  // Private variable (closure) (Biến riêng tư - closure)
  let counter = 0; // Biến đếm, không thể truy cập từ bên ngoài

  // Private function (Hàm riêng tư)
  function log(message: string) {
    console.log(`[Counter] ${message}`); // Ghi log với prefix [Counter]
  }

  // Public API (API công khai - chỉ những gì được return mới có thể truy cập)
  return {
    increment() {
      // Tăng counter
      counter++;
      log(`Incremented to ${counter}`); // Ghi log: Tăng lên giá trị mới
    },

    decrement() {
      // Giảm counter
      counter--;
      log(`Decremented to ${counter}`); // Ghi log: Giảm xuống giá trị mới
    },

    getCount() {
      // Lấy giá trị counter
      return counter;
    },

    reset() {
      // Đặt lại counter về 0
      counter = 0;
      log('Reset to 0'); // Ghi log: Đặt lại về 0
    },
  };
})(); // Gọi hàm ngay lập tức

// Usage (Cách sử dụng)
CounterModule.increment(); // [Counter] Incremented to 1 (Tăng lên 1)
CounterModule.increment(); // [Counter] Incremented to 2 (Tăng lên 2)
console.log(CounterModule.getCount()); // 2 (In ra giá trị: 2)

// ❌ Cannot access private variables (Không thể truy cập biến riêng tư)
console.log(CounterModule.counter); // undefined (Không tồn tại)
console.log(CounterModule.log); // undefined (Không tồn tại)

// ===================================================
// ✅ MODERN: ES6 Modules (Built-in Encapsulation)
// ===================================================

// counter.ts
let counter = 0; // Biến riêng tư (không export)

function log(message: string) {
  // Hàm riêng tư (không export)
  console.log(`[Counter] ${message}`);
}

export function increment() {
  // Hàm công khai (export)
  counter++;
  log(`Incremented to ${counter}`); // Gọi hàm log riêng tư
}

export function decrement() {
  // Hàm công khai (export)
  counter--;
  log(`Decremented to ${counter}`); // Gọi hàm log riêng tư
}

export function getCount() {
  // Hàm công khai (export)
  return counter; // Trả về biến riêng tư
}

// app.ts
import { increment, getCount } from './counter'; // Import các hàm công khai

increment(); // ✅ Works (Hoạt động - tăng counter lên 1)
console.log(getCount()); // 1 (In ra: 1)

// ❌ Cannot import private variables (Không thể import biến riêng tư)
import { counter } from './counter'; // Error: 'counter' is not exported (Lỗi: 'counter' không được export)

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Local Storage Manager
// ===================================================

const StorageManager = (function () {
  // Module quản lý localStorage
  const PREFIX = 'app_'; // Tiền tố cho tất cả keys (riêng tư)

  function getKey(key: string): string {
    // Hàm riêng tư: thêm prefix vào key
    return PREFIX + key; // Trả về key với prefix
  }

  function handleError(error: Error) {
    // Hàm riêng tư: xử lý lỗi
    console.error('[Storage] Error:', error.message); // In lỗi ra console
  }

  return {
    // Public API (API công khai)
    set(key: string, value: any): void {
      // Lưu giá trị vào localStorage
      try {
        const serialized = JSON.stringify(value); // Chuyển đổi object thành JSON string
        localStorage.setItem(getKey(key), serialized); // Lưu vào localStorage với key có prefix
      } catch (error) {
        handleError(error as Error); // Xử lý lỗi nếu có
      }
    },

    get<T>(key: string): T | null {
      // Lấy giá trị từ localStorage
      try {
        const item = localStorage.getItem(getKey(key)); // Lấy item từ localStorage
        return item ? JSON.parse(item) : null; // Parse JSON nếu có, không thì null
      } catch (error) {
        handleError(error as Error); // Xử lý lỗi nếu có
        return null; // Trả về null nếu lỗi
      }
    },

    remove(key: string): void {
      // Xóa giá trị khỏi localStorage
      localStorage.removeItem(getKey(key)); // Xóa item với key có prefix
    },

    clear(): void {
      // Xóa tất cả items có prefix
      Object.keys(localStorage) // Lấy tất cả keys trong localStorage
        .filter((key) => key.startsWith(PREFIX)) // Lọc chỉ những key có prefix
        .forEach((key) => localStorage.removeItem(key)); // Xóa từng key
    },
  };
})(); // Gọi hàm ngay lập tức

// Usage (Cách sử dụng)
StorageManager.set('user', { name: 'John', age: 30 }); // Lưu user vào localStorage
const user = StorageManager.get<{ name: string; age: number }>('user'); // Lấy user từ localStorage
console.log(user); // { name: 'John', age: 30 } (In ra object user)

// ❌ Cannot access private functions (Không thể truy cập hàm riêng tư)
StorageManager.getKey('user'); // Error (Lỗi - hàm không tồn tại)
StorageManager.PREFIX; // undefined (Không tồn tại - biến riêng tư)
```

---

## **6️⃣ DEPENDENCY INJECTION - Loose Coupling**

```typescript
// ===================================================
// 💉 DEPENDENCY INJECTION - Invert Dependencies
// ===================================================

/**
 * Use Cases (Trường hợp sử dụng):
 * - Testability (Khả năng kiểm thử - inject mocks - tiêm mock objects)
 * - Flexibility (Tính linh hoạt - swap implementations - thay đổi triển khai)
 * - Loose coupling (Liên kết lỏng lẻo - depend on abstractions - phụ thuộc vào trừu tượng)
 */

// ===================================================
// ❌ BAD: Tight Coupling (Hard to Test)
// ===================================================

class UserService {
  private api: ApiClient; // Phụ thuộc vào ApiClient

  constructor() {
    // ❌ Hardcoded dependency (tight coupling) (Phụ thuộc mã hóa cứng - liên kết chặt chẽ)
    this.api = new ApiClient('https://api.example.com'); // Tạo ApiClient trực tiếp trong constructor
  }

  async getUser(id: string) {
    // Lấy thông tin user
    return this.api.get(`/users/${id}`); // Gọi API để lấy user
  }
}

// Problem (Vấn đề): Cannot test without real API! (Không thể kiểm thử mà không có API thật!)
const userService = new UserService();
// Always uses real ApiClient (Luôn sử dụng ApiClient thật - không thể mock)

// ===================================================
// ✅ GOOD: Dependency Injection (Loose Coupling)
// ===================================================

interface IApiClient {
  // Interface định nghĩa contract cho API client
  get(endpoint: string): Promise<any>; // Phương thức GET
  post(endpoint: string, data: any): Promise<any>; // Phương thức POST
}

class ApiClient implements IApiClient {
  // Triển khai thật của API client
  constructor(private baseUrl: string) {} // baseUrl: địa chỉ cơ sở API

  async get(endpoint: string) {
    // Gửi request GET
    const response = await fetch(`${this.baseUrl}${endpoint}`); // Gọi fetch API
    return response.json(); // Trả về JSON
  }

  async post(endpoint: string, data: any) {
    // Gửi request POST
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST', // Phương thức POST
      headers: { 'Content-Type': 'application/json' }, // Header JSON
      body: JSON.stringify(data), // Body dạng JSON string
    });
    return response.json(); // Trả về JSON
  }
}

class UserService {
  // ✅ Inject dependency via constructor (Tiêm phụ thuộc qua constructor)
  constructor(private api: IApiClient) {} // Nhận IApiClient (interface) thay vì class cụ thể

  async getUser(id: string) {
    // Lấy thông tin user
    return this.api.get(`/users/${id}`); // Gọi API GET
  }

  async createUser(data: any) {
    // Tạo user mới
    return this.api.post('/users', data); // Gọi API POST
  }
}

// Production (Môi trường sản xuất): Inject real API client (Tiêm API client thật)
const apiClient = new ApiClient('https://api.example.com'); // Tạo ApiClient thật
const userService = new UserService(apiClient); // Tiêm vào UserService

// Testing (Kiểm thử): Inject mock API client (Tiêm API client giả)
class MockApiClient implements IApiClient {
  // API client giả cho testing
  async get(endpoint: string) {
    return { id: '123', name: 'Test User' }; // Fake data (Dữ liệu giả)
  }

  async post(endpoint: string, data: any) {
    return { success: true }; // Trả về thành công giả
  }
}

const mockApi = new MockApiClient(); // Tạo mock API client
const testUserService = new UserService(mockApi); // Tiêm mock vào UserService

// ✅ Test without real API! (Kiểm thử mà không cần API thật!)
const user = await testUserService.getUser('123'); // Lấy user (sử dụng mock)
console.log(user); // { id: '123', name: 'Test User' } (Dữ liệu giả từ mock)

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: DI Container
// ===================================================

class DIContainer {
  // Container quản lý Dependency Injection
  private services: Map<string, any> = new Map(); // Map lưu trữ các service factories

  // Register service (Đăng ký service)
  register<T>(name: string, factory: () => T): void {
    // name: tên service, factory: hàm tạo service
    this.services.set(name, factory); // Lưu factory vào Map
  }

  // Resolve service (singleton pattern) (Giải quyết service - mẫu singleton)
  resolve<T>(name: string): T {
    // name: tên service cần lấy
    const factory = this.services.get(name); // Lấy factory từ Map
    if (!factory) {
      throw new Error(`Service not registered: ${name}`); // Lỗi nếu service chưa đăng ký
    }

    // Call factory function to create instance (Gọi hàm factory để tạo instance)
    return factory(); // Trả về instance được tạo
  }
}

// Usage (Cách sử dụng)
const container = new DIContainer(); // Tạo DI container

// Register services (Đăng ký các service)
container.register('apiClient', () => new ApiClient('https://api.example.com')); // Đăng ký ApiClient
container.register('userService', () => {
  // Đăng ký UserService
  const api = container.resolve<ApiClient>('apiClient'); // Lấy ApiClient từ container
  return new UserService(api); // Tạo UserService với ApiClient đã inject
});

// Resolve services (Lấy service từ container)
const userService = container.resolve<UserService>('userService'); // Lấy UserService
await userService.getUser('123'); // Sử dụng service
```

---

## **🎯 WHEN TO USE WHAT?**

| Pattern (Mẫu)            | **Use Case (Trường hợp sử dụng)**                                                  | **Example (Ví dụ)**                                                    |
| ------------------------ | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **Singleton**            | Global state (Trạng thái toàn cục), single instance needed (cần thể hiện duy nhất) | Logger (Ghi log), API client (Ứng dụng khách API), Config (Cấu hình)   |
| **Observer**             | One-to-many notifications (Thông báo một-nhiều)                                    | React state (Trạng thái React), event listeners (Bộ lắng nghe sự kiện) |
| **Pub/Sub**              | Decoupled event system (Hệ thống sự kiện tách rời)                                 | Analytics (Phân tích), cross-component comm (Giao tiếp giữa component) |
| **Factory**              | Create objects based on type (Tạo đối tượng dựa trên loại)                         | Buttons (Nút bấm), notifications (Thông báo), plugins (Plugin)         |
| **Module**               | Encapsulation (Đóng gói - private/public API)                                      | localStorage wrapper (Bọc localStorage), utilities (Tiện ích)          |
| **Dependency Injection** | Loose coupling (Liên kết lỏng lẻo), testability (Khả năng kiểm thử)                | Services with API dependencies (Dịch vụ có phụ thuộc API)              |

---

**🎯 TÓM TẮT Q60 - JAVASCRIPT DESIGN PATTERNS**

**✅ Creational Patterns:**

- **Singleton**: 1 instance duy nhất (Logger, API client)
- **Factory**: Tạo objects theo type (Buttons, Notifications)

**✅ Behavioral Patterns:**

- **Observer**: Subscribe to changes (React state, stock prices)
- **Pub/Sub**: Event-driven communication (Analytics, cart updates)

**✅ Structural Patterns:**

- **Module**: Encapsulation with private/public API (IIFE or ES6 modules)
- **Dependency Injection**: Loose coupling, testability (inject mocks)

**💡 Key Takeaways (Điểm Quan Trọng):**

1. **Use Singleton (Sử dụng Singleton)** for global services (cho dịch vụ toàn cục - logger - ghi log, API client - ứng dụng khách API)
2. **Use Observer/Pub-Sub (Sử dụng Observer/Pub-Sub)** for reactive programming (cho lập trình phản ứng - events - sự kiện, state - trạng thái)
3. **Use Factory (Sử dụng Factory)** for object creation with multiple types (cho việc tạo đối tượng với nhiều loại)
4. **Use Module (Sử dụng Module)** for encapsulation (cho đóng gói - ES6 modules standard now - ES6 modules là chuẩn hiện tại)
5. **Use DI (Sử dụng Dependency Injection)** for testable, loosely coupled code (cho code có thể kiểm thử, liên kết lỏng lẻo)

---
