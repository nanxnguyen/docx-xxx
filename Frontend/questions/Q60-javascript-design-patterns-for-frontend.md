# 🏗️ Q60: JavaScript Design Patterns for Frontend Development

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Design patterns: Singleton (1 instance), Observer (subscribe changes), Factory (create objects), Module (encapsulation), Pub/Sub (event-driven), Dependency Injection (loose coupling). Modern: Hooks patterns, Compound Components."**

**🔑 6 Essential Patterns:**

**1. Singleton - Single Instance:**
- **Use case**: Database connection, config object, logger
- **JS**: Module exports object (auto-singleton), class với static instance
- **Caution**: Hard to test (global state), avoid unless necessary

**2. Observer - Subscribe to Changes:**
- **Use case**: Event listeners, state management, reactive programming
- **Pattern**: Subject maintains observers list, notify on change
- **Modern**: RxJS Observables, MobX, Vue reactivity

**3. Pub/Sub (Publish-Subscribe):**
- **Khác Observer**: Decoupled (event bus giữa publisher/subscriber)
- **Use case**: Cross-component communication, analytics events
- **Implementation**: EventEmitter, window.postMessage, Redux

**4. Factory - Object Creation:**
- **Use case**: Create objects without specifying exact class
- **Example**: `React.createElement()`, component factories
- **Benefits**: Flexibility, hide complexity

**5. Module Pattern - Encapsulation:**
- **ES6 Modules**: `export/import` - native encapsulation
- **IIFE**: `(function(){ ... })()` - private scope (legacy)
- **Use case**: Libraries, utilities, prevent global pollution

**6. Dependency Injection:**
- **Pattern**: Pass dependencies (không hard-code)
- **Use case**: Testing (mock dependencies), loose coupling
- **React**: Props, Context API, custom hooks

**🔑 Modern React Patterns:**

- **Compound Components**: `<Select>` + `<Option>` share state
- **Render Props**: `<DataProvider render={data => ...} />`
- **Higher-Order Components** (HOC): `withAuth(Component)`
- **Custom Hooks**: `useAuth()`, `useFetch()` - reusable logic

**⚠️ Lỗi Thường Gặp:**
- Over-engineering: Dùng patterns không cần thiết → complexity
- Singleton abuse → global state, hard test
- Observer memory leaks → forget unsubscribe
- Pub/Sub không type-safe → dùng TypeScript event types

**💡 Kiến Thức Senior:**
- **Strategy Pattern**: Interchangeable algorithms (sort strategies, payment methods)
- **Command Pattern**: Undo/redo functionality (Redux actions)
- **Proxy Pattern**: ES6 Proxy cho reactivity (Vue 3, MobX)
- **Facade Pattern**: Simplify complex APIs (Axios wraps fetch, jQuery wraps DOM)

**❓ Câu Hỏi:**

Giải thích các Design Patterns phổ biến trong JavaScript/TypeScript frontend: Singleton, Observer, Factory, Module, Pub/Sub, Prototype, Dependency Injection. Khi nào nên dùng pattern nào?

---

## **📊 DESIGN PATTERNS OVERVIEW**

```
┌──────────────────────────────────────────────────────────────┐
│          JAVASCRIPT DESIGN PATTERNS (Gang of Four + Modern)  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  🏗️ CREATIONAL PATTERNS (Object Creation)                    │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Singleton     - Đảm bảo chỉ 1 instance duy nhất    │ │
│  │  • Factory       - Tạo objects mà không chỉ định class│ │
│  │  • Prototype     - Clone objects từ prototype         │ │
│  │  • Builder       - Xây dựng complex objects từng bước │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  🔗 STRUCTURAL PATTERNS (Object Relationships)               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Module        - Encapsulation, private/public API   │ │
│  │  • Decorator     - Thêm behavior vào objects          │ │
│  │  • Facade        - Simplified interface               │ │
│  │  • Proxy         - Control access to objects          │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                              │
│  📡 BEHAVIORAL PATTERNS (Object Communication)               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  • Observer      - Subscribe to object changes         │ │
│  │  • Pub/Sub       - Event-driven communication         │ │
│  │  • Strategy      - Interchangeable algorithms         │ │
│  │  • Command       - Encapsulate requests as objects    │ │
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
 * Use Cases:
 * - Global state management (Redux store)
 * - Logger service
 * - Database connection
 * - API client
 * - Configuration manager
 */

// ===================================================
// ❌ BAD: Multiple instances (not Singleton)
// ===================================================

class ApiClient {
  constructor(private baseUrl: string) {}

  async get(endpoint: string) {
    return fetch(`${this.baseUrl}${endpoint}`);
  }
}

// Problem: Creates new instance every time!
const api1 = new ApiClient('https://api.example.com');
const api2 = new ApiClient('https://api.example.com');
// api1 !== api2 (different instances, waste memory)

// ===================================================
// ✅ GOOD: Singleton Pattern (Classic ES6 Class)
// ===================================================

class ApiClient {
  private static instance: ApiClient;  // 👉 Static instance (duy nhất)
  private baseUrl: string;

  // 🔒 Private constructor (cannot use `new` outside class - Không thể new từ bên ngoài)
  private constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  // 🎯 Public method to get the single instance (Lấy instance duy nhất)
  public static getInstance(baseUrl: string = 'https://api.example.com'): ApiClient {
    if (!ApiClient.instance) {  // ❓ Chưa có instance
      ApiClient.instance = new ApiClient(baseUrl);  // ✅ Tạo instance mới
    }
    return ApiClient.instance;  // 🔁 Trả về instance hiện tại
  }

  public async get(endpoint: string) {  // 📥 GET request
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    return response.json();
  }

  public async post(endpoint: string, data: any) {  // 📤 POST request
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },  // 📝 JSON header
      body: JSON.stringify(data)  // 📦 Serialize data
    });
    return response.json();
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
  constructor(private baseUrl: string) {}  // 🎯 Constructor đơn giản

  async get(endpoint: string) {  // 📥 GET request
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    return response.json();
  }
}

// 📦 Export single instance (Singleton via module caching)
// ES modules được cache tự động, nên chỉ có 1 instance
export const apiClient = new ApiClient('https://api.example.com');

// 📄 app.ts
import { apiClient } from './apiClient';  // 📥 Import instance

// ✅ Always the same instance (ES modules cached by default)
apiClient.get('/users');  // 👥 Lấy danh sách users

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Logger Singleton
// ===================================================

type LogLevel = 'debug' | 'info' | 'warn' | 'error';  // 🏷️ Các mức log

class Logger {
  private static instance: Logger;  // 👉 Static instance
  private logs: Array<{ level: LogLevel; message: string; timestamp: Date }> = [];  // 📊 Lưu tất cả logs

  private constructor() {}  // 🔒 Private constructor

  public static getInstance(): Logger {  // 🎯 Lấy instance
    if (!Logger.instance) {
      Logger.instance = new Logger();
    }
    return Logger.instance;
  }

  private log(level: LogLevel, message: string) {  // 📝 Log function chính
    const logEntry = {
      level,
      message,
      timestamp: new Date()  // ⏱️ Thời gian log
    };

    this.logs.push(logEntry);  // 📥 Lưu vào array

    // 🎨 Console output with colors (In ra console với màu sắc)
    const colors = {
      debug: '\x1b[36m', // 💙 Cyan - Màu xanh nhạt
      info: '\x1b[32m', // 🟢 Green - Màu xanh lá
      warn: '\x1b[33m', // 🟡 Yellow - Màu vàng
      error: '\x1b[31m' // 🔴 Red - Màu đỏ
    };

    console.log(
      `${colors[level]}[${level.toUpperCase()}]\x1b[0m ${message}`
    );
  }

  public debug(message: string) {  // 💙 Debug level
    this.log('debug', message);
  }

  public info(message: string) {  // 🟢 Info level
    this.log('info', message);
  }

  public warn(message: string) {  // 🟡 Warning level
    this.log('warn', message);
  }

  public error(message: string) {  // 🔴 Error level
    this.log('error', message);
  }

  public getLogs() {  // 📊 Lấy tất cả logs
    return this.logs;
  }
}

// 📝 Usage
const logger = Logger.getInstance();
logger.info('App started');  // 🟢 [INFO] App started
logger.error('Failed to fetch data');  // 🔴 [ERROR] Failed to fetch data
logger.getLogs(); // 📊 All logs from entire app
```

---

## **2️⃣ OBSERVER PATTERN - Subscribe to Changes**

```typescript
// ===================================================
// 📡 OBSERVER PATTERN - Notify subscribers on changes
// ===================================================

/**
 * Use Cases:
 * - React state management (useState triggers re-render)
 * - Event listeners (addEventListener)
 * - Real-time data updates (stock prices, chat)
 * - Model-View synchronization
 */

// ===================================================
// ✅ IMPLEMENTATION: Subject (Observable) + Observers
// ===================================================

interface Observer {
  update(data: any): void;  // 🔄 Phương thức nhận update
}

class Subject {
  private observers: Observer[] = [];  // 📊 Danh sách observers

  // 🔔 Subscribe to changes (Đăng ký nhận thông báo)
  public subscribe(observer: Observer): void {
    this.observers.push(observer);  // 📥 Thêm vào danh sách
  }

  // 🚫 Unsubscribe (Hủy đăng ký)
  public unsubscribe(observer: Observer): void {
    const index = this.observers.indexOf(observer);
    if (index > -1) {
      this.observers.splice(index, 1);  // 🗑️ Xóa khỏi danh sách
    }
  }

  // 📢 Notify all observers (Thông báo cho tất cả observers)
  protected notify(data: any): void {
    this.observers.forEach((observer) => observer.update(data));  // 🔁 Gọi update cho từng observer
  }
}

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Stock Price Tracker (Theo dõi giá cổ phiếu)
// ===================================================

class Stock extends Subject {
  private price: number = 0;  // 💵 Giá hiện tại
  private name: string;       // 🏷️ Tên cổ phiếu

  constructor(name: string, initialPrice: number) {
    super();
    this.name = name;
    this.price = initialPrice;
  }

  public setPrice(newPrice: number): void {  // 💰 Đổi giá
    console.log(`${this.name} price changed: $${this.price} → $${newPrice}`);
    this.price = newPrice;
    this.notify({ name: this.name, price: newPrice });  // 📢 Thông báo cho observers
  }

  public getPrice(): number {  // 📊 Lấy giá
    return this.price;
  }
}

// 📺 Observer 1: Display widget (Hiển thị)
class PriceDisplay implements Observer {
  constructor(private elementId: string) {}  // 🎯 Element ID để hiển thị

  update(data: { name: string; price: number }): void {
    const element = document.getElementById(this.elementId);
    if (element) {
      element.textContent = `${data.name}: $${data.price}`;  // 📝 Cập nhật text
    }
  }
}

// 🔔 Observer 2: Alert service (Cảnh báo)
class PriceAlert implements Observer {
  constructor(private threshold: number) {}  // 🚨 Ngưỡng giá

  update(data: { name: string; price: number }): void {
    if (data.price > this.threshold) {  // ❗ Vượt ngưỡng
      alert(`${data.name} exceeded $${this.threshold}!`);  // 🔔 Cảnh báo
    }
  }
}

// 📝 Observer 3: Logger (Ghi log)
class PriceLogger implements Observer {
  update(data: { name: string; price: number }): void {
    console.log(`[LOG] ${new Date().toISOString()} - ${data.name}: $${data.price}`);  // 📊 Ghi log với timestamp
  }
}

// Usage
const appleStock = new Stock('AAPL', 150);

const display = new PriceDisplay('stock-display');
const alert = new PriceAlert(200);
const logger = new PriceLogger();

// Subscribe observers
appleStock.subscribe(display);
appleStock.subscribe(alert);
appleStock.subscribe(logger);

// Update price → all observers notified!
appleStock.setPrice(180); // Display updates, logger logs
appleStock.setPrice(210); // Display updates, alert fires, logger logs

// Unsubscribe
appleStock.unsubscribe(alert);
appleStock.setPrice(220); // Only display and logger notified
```

---

## **3️⃣ PUB/SUB PATTERN - Event-Driven Communication**

```typescript
// ===================================================
// 📢 PUB/SUB PATTERN - Decoupled Event System
// ===================================================

/**
 * Difference from Observer:
 * - Observer: Subject knows its observers (tight coupling)
 * - Pub/Sub: Publishers/Subscribers don't know each other (loose coupling)
 * 
 * Use Cases:
 * - Global events (analytics tracking)
 * - Cross-component communication
 * - Microservices messaging
 */

// ===================================================
// ✅ IMPLEMENTATION: Event Bus (Pub/Sub Mediator - Trung gian sự kiện)
// ===================================================

type EventCallback = (data?: any) => void;  // 🔗 Callback function cho sự kiện

class EventBus {
  private events: Map<string, EventCallback[]> = new Map();  // 📊 Lưu danh sách events và callbacks

  // 🔔 Subscribe to event (Đăng ký lắng nghe sự kiện)
  public on(event: string, callback: EventCallback): () => void {
    if (!this.events.has(event)) {  // ❓ Chưa có event này
      this.events.set(event, []);  // 🆕 Tạo array mới
    }

    this.events.get(event)!.push(callback);  // 📥 Thêm callback vào danh sách

    // 🔁 Return unsubscribe function (Trả về hàm hủy đăng ký)
    return () => this.off(event, callback);
  }

  // 🚫 Unsubscribe from event (Hủy đăng ký)
  public off(event: string, callback: EventCallback): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      const index = callbacks.indexOf(callback);
      if (index > -1) {
        callbacks.splice(index, 1);  // 🗑️ Xóa callback
      }
    }
  }

  // 📢 Publish event (Phát sự kiện)
  public emit(event: string, data?: any): void {
    const callbacks = this.events.get(event);
    if (callbacks) {
      callbacks.forEach((callback) => callback(data));  // 🔁 Gọi tất cả callbacks
    }
  }

  // 1️⃣ Subscribe once (auto-unsubscribe after first call - Tự động hủy sau lần đầu)
  public once(event: string, callback: EventCallback): void {
    const onceCallback = (data?: any) => {
      callback(data);
      this.off(event, onceCallback);  // 🚫 Tự động hủy sau khi chạy
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
    eventBus.emit('product:added', product);  // 📢 Phát sự kiện
  }
}

// 📥 Subscriber 1: CartWidget (Widget giỏ hàng)
class CartWidget {
  private itemCount: number = 0;  // 📊 Số lượng sản phẩm

  constructor() {
    eventBus.on('product:added', (product) => {  // 🔔 Lắng nghe sự kiện
      this.itemCount++;  // ➡️ Tăng số lượng
      this.updateUI();   // 🔄 Cập nhật UI
      console.log(`Cart updated: ${this.itemCount} items`);
    });
  }

  private updateUI() {
    const badge = document.getElementById('cart-badge');
    if (badge) {
      badge.textContent = String(this.itemCount);  // 📝 Cập nhật badge
    }
  }
}

// 📊 Subscriber 2: Analytics (Phân tích)
class Analytics {
  constructor() {
    eventBus.on('product:added', (product) => {  // 🔔 Lắng nghe
      this.trackEvent('add_to_cart', {  // 📊 Theo dõi sự kiện
        product_id: product.id,
        product_name: product.name,
        price: product.price
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
    eventBus.on('product:added', (product) => {  // 🔔 Lắng nghe
      this.showToast(`${product.name} added to cart!`);  // 🔔 Hiển thị thông báo
    });
  }

  private showToast(message: string) {
    console.log(`🔔 ${message}`);
    // 💬 Show toast UI
  }
}

// Usage
const productCard = new ProductCard();
const cartWidget = new CartWidget();
const analytics = new Analytics();
const toastNotifier = new ToastNotifier();

// Add product → all subscribers notified!
productCard.addToCart({ id: '123', name: 'Laptop', price: 999 });
// Output:
// [Analytics] add_to_cart: { product_id: '123', ... }
// Cart updated: 1 items
// 🔔 Laptop added to cart!

// ===================================================
// 🎯 REACT EXAMPLE: Custom Event Hook
// ===================================================

import { useEffect } from 'react';

// Custom hook for event subscription
function useEventBus(event: string, callback: EventCallback) {
  useEffect(() => {
    const unsubscribe = eventBus.on(event, callback);
    return unsubscribe; // Cleanup on unmount
  }, [event, callback]);
}

// React component
function CartBadge() {
  const [count, setCount] = useState(0);

  useEventBus('product:added', () => {
    setCount((prev) => prev + 1);
  });

  return <span className="badge">{count}</span>;
}
```

---

## **4️⃣ FACTORY PATTERN - Object Creation**

```typescript
// ===================================================
// 🏭 FACTORY PATTERN - Create objects without specifying class
// ===================================================

/**
 * Use Cases:
 * - Create different types of objects based on input
 * - Encapsulate complex creation logic
 * - Plugin systems (load different implementations)
 */

// ===================================================
// ❌ BAD: Conditional object creation (messy)
// ===================================================

function createButton(type: string) {
  if (type === 'primary') {
    return {
      render() {
        return '<button class="btn-primary">Click</button>';
      }
    };
  } else if (type === 'secondary') {
    return {
      render() {
        return '<button class="btn-secondary">Click</button>';
      }
    };
  } else if (type === 'danger') {
    return {
      render() {
        return '<button class="btn-danger">Click</button>';
      }
    };
  }
  // Gets messy with many types!
}

// ===================================================
// ✅ GOOD: Factory Pattern (Mẫu Factory)
// ===================================================

interface Button {
  render(): string;   // 🎨 Render HTML
  onClick(): void;    // 🖌️ Xử lý click
}

class PrimaryButton implements Button {
  render(): string {  // 🟢 Button xanh lá (primary)
    return '<button class="btn-primary">Click</button>';
  }

  onClick(): void {  // 🖌️ Primary action
    console.log('Primary action');
  }
}

class SecondaryButton implements Button {
  render(): string {  // 🔵 Button xanh (secondary)
    return '<button class="btn-secondary">Click</button>';
  }

  onClick(): void {  // 🖌️ Secondary action
    console.log('Secondary action');
  }
}

class DangerButton implements Button {
  render(): string {  // 🔴 Button đỏ (danger)
    return '<button class="btn-danger">Delete</button>';
  }

  onClick(): void {  // ⚠️ Danger action - cần confirm
    if (confirm('Are you sure?')) {  // ❓ Xác nhận
      console.log('Deleted!');  // 🗑️ Xóa
    }
  }
}

// Factory class
class ButtonFactory {
  static createButton(type: 'primary' | 'secondary' | 'danger'): Button {
    switch (type) {
      case 'primary':
        return new PrimaryButton();
      case 'secondary':
        return new SecondaryButton();
      case 'danger':
        return new DangerButton();
      default:
        throw new Error(`Unknown button type: ${type}`);
    }
  }
}

// Usage
const btn1 = ButtonFactory.createButton('primary');
const btn2 = ButtonFactory.createButton('danger');

console.log(btn1.render()); // <button class="btn-primary">...</button>
btn2.onClick(); // Shows confirm dialog

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Notification Factory
// ===================================================

interface Notification {
  send(message: string): void;
}

class EmailNotification implements Notification {
  constructor(private email: string) {}

  send(message: string): void {
    console.log(`📧 Email sent to ${this.email}: ${message}`);
    // Send email via SMTP/API
  }
}

class SMSNotification implements Notification {
  constructor(private phone: string) {}

  send(message: string): void {
    console.log(`📱 SMS sent to ${this.phone}: ${message}`);
    // Send SMS via Twilio/API
  }
}

class PushNotification implements Notification {
  constructor(private deviceToken: string) {}

  send(message: string): void {
    console.log(`🔔 Push sent to ${this.deviceToken}: ${message}`);
    // Send push via Firebase/OneSignal
  }
}

class NotificationFactory {
  static create(
    type: 'email' | 'sms' | 'push',
    recipient: string
  ): Notification {
    switch (type) {
      case 'email':
        return new EmailNotification(recipient);
      case 'sms':
        return new SMSNotification(recipient);
      case 'push':
        return new PushNotification(recipient);
      default:
        throw new Error(`Unknown notification type: ${type}`);
    }
  }
}

// Usage
const notifier1 = NotificationFactory.create('email', 'user@example.com');
const notifier2 = NotificationFactory.create('sms', '+1234567890');

notifier1.send('Your order has shipped!');
notifier2.send('Your verification code is 123456');
```

---

## **5️⃣ MODULE PATTERN - Encapsulation**

```typescript
// ===================================================
// 📦 MODULE PATTERN - Private/Public API
// ===================================================

/**
 * Use Cases:
 * - Create private scope (before ES6 modules)
 * - Encapsulate implementation details
 * - Expose only public API
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

// Problem: `counter` is globally accessible!
counter = 999; // ❌ Can be modified directly!

// ===================================================
// ✅ SOLUTION: Module Pattern (IIFE - Immediately Invoked Function Expression)
// ===================================================

const CounterModule = (function () {
  // Private variable (closure)
  let counter = 0;

  // Private function
  function log(message: string) {
    console.log(`[Counter] ${message}`);
  }

  // Public API
  return {
    increment() {
      counter++;
      log(`Incremented to ${counter}`);
    },

    decrement() {
      counter--;
      log(`Decremented to ${counter}`);
    },

    getCount() {
      return counter;
    },

    reset() {
      counter = 0;
      log('Reset to 0');
    }
  };
})();

// Usage
CounterModule.increment(); // [Counter] Incremented to 1
CounterModule.increment(); // [Counter] Incremented to 2
console.log(CounterModule.getCount()); // 2

// ❌ Cannot access private variables
console.log(CounterModule.counter); // undefined
console.log(CounterModule.log); // undefined

// ===================================================
// ✅ MODERN: ES6 Modules (Built-in Encapsulation)
// ===================================================

// counter.ts
let counter = 0;

function log(message: string) {
  console.log(`[Counter] ${message}`);
}

export function increment() {
  counter++;
  log(`Incremented to ${counter}`);
}

export function decrement() {
  counter--;
  log(`Decremented to ${counter}`);
}

export function getCount() {
  return counter;
}

// app.ts
import { increment, getCount } from './counter';

increment(); // ✅ Works
console.log(getCount()); // 1

// ❌ Cannot import private variables
import { counter } from './counter'; // Error: 'counter' is not exported

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: Local Storage Manager
// ===================================================

const StorageManager = (function () {
  const PREFIX = 'app_';

  function getKey(key: string): string {
    return PREFIX + key;
  }

  function handleError(error: Error) {
    console.error('[Storage] Error:', error.message);
  }

  return {
    set(key: string, value: any): void {
      try {
        const serialized = JSON.stringify(value);
        localStorage.setItem(getKey(key), serialized);
      } catch (error) {
        handleError(error as Error);
      }
    },

    get<T>(key: string): T | null {
      try {
        const item = localStorage.getItem(getKey(key));
        return item ? JSON.parse(item) : null;
      } catch (error) {
        handleError(error as Error);
        return null;
      }
    },

    remove(key: string): void {
      localStorage.removeItem(getKey(key));
    },

    clear(): void {
      Object.keys(localStorage)
        .filter((key) => key.startsWith(PREFIX))
        .forEach((key) => localStorage.removeItem(key));
    }
  };
})();

// Usage
StorageManager.set('user', { name: 'John', age: 30 });
const user = StorageManager.get<{ name: string; age: number }>('user');
console.log(user); // { name: 'John', age: 30 }

// ❌ Cannot access private functions
StorageManager.getKey('user'); // Error
StorageManager.PREFIX; // undefined
```

---

## **6️⃣ DEPENDENCY INJECTION - Loose Coupling**

```typescript
// ===================================================
// 💉 DEPENDENCY INJECTION - Invert Dependencies
// ===================================================

/**
 * Use Cases:
 * - Testability (inject mocks)
 * - Flexibility (swap implementations)
 * - Loose coupling (depend on abstractions)
 */

// ===================================================
// ❌ BAD: Tight Coupling (Hard to Test)
// ===================================================

class UserService {
  private api: ApiClient;

  constructor() {
    // ❌ Hardcoded dependency (tight coupling)
    this.api = new ApiClient('https://api.example.com');
  }

  async getUser(id: string) {
    return this.api.get(`/users/${id}`);
  }
}

// Problem: Cannot test without real API!
const userService = new UserService();
// Always uses real ApiClient

// ===================================================
// ✅ GOOD: Dependency Injection (Loose Coupling)
// ===================================================

interface IApiClient {
  get(endpoint: string): Promise<any>;
  post(endpoint: string, data: any): Promise<any>;
}

class ApiClient implements IApiClient {
  constructor(private baseUrl: string) {}

  async get(endpoint: string) {
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    return response.json();
  }

  async post(endpoint: string, data: any) {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    return response.json();
  }
}

class UserService {
  // ✅ Inject dependency via constructor
  constructor(private api: IApiClient) {}

  async getUser(id: string) {
    return this.api.get(`/users/${id}`);
  }

  async createUser(data: any) {
    return this.api.post('/users', data);
  }
}

// Production: Inject real API client
const apiClient = new ApiClient('https://api.example.com');
const userService = new UserService(apiClient);

// Testing: Inject mock API client
class MockApiClient implements IApiClient {
  async get(endpoint: string) {
    return { id: '123', name: 'Test User' }; // Fake data
  }

  async post(endpoint: string, data: any) {
    return { success: true };
  }
}

const mockApi = new MockApiClient();
const testUserService = new UserService(mockApi);

// ✅ Test without real API!
const user = await testUserService.getUser('123');
console.log(user); // { id: '123', name: 'Test User' }

// ===================================================
// 🔥 REAL-WORLD EXAMPLE: DI Container
// ===================================================

class DIContainer {
  private services: Map<string, any> = new Map();

  // Register service
  register<T>(name: string, factory: () => T): void {
    this.services.set(name, factory);
  }

  // Resolve service (singleton pattern)
  resolve<T>(name: string): T {
    const factory = this.services.get(name);
    if (!factory) {
      throw new Error(`Service not registered: ${name}`);
    }

    // Call factory function to create instance
    return factory();
  }
}

// Usage
const container = new DIContainer();

// Register services
container.register('apiClient', () => new ApiClient('https://api.example.com'));
container.register('userService', () => {
  const api = container.resolve<ApiClient>('apiClient');
  return new UserService(api);
});

// Resolve services
const userService = container.resolve<UserService>('userService');
await userService.getUser('123');
```

---

## **🎯 WHEN TO USE WHAT?**

| Pattern              | **Use Case**                                      | **Example**                      |
| -------------------- | ------------------------------------------------- | -------------------------------- |
| **Singleton**        | Global state, single instance needed              | Logger, API client, Config       |
| **Observer**         | One-to-many notifications                         | React state, event listeners     |
| **Pub/Sub**          | Decoupled event system                            | Analytics, cross-component comm  |
| **Factory**          | Create objects based on type                      | Buttons, notifications, plugins  |
| **Module**           | Encapsulation (private/public API)                | localStorage wrapper, utilities  |
| **Dependency Injection** | Loose coupling, testability                   | Services with API dependencies   |

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

**💡 Key Takeaways:**

1. **Use Singleton** for global services (logger, API client)
2. **Use Observer/Pub-Sub** for reactive programming (events, state)
3. **Use Factory** for object creation with multiple types
4. **Use Module** for encapsulation (ES6 modules standard now)
5. **Use DI** for testable, loosely coupled code

---
