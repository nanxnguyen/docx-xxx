# 🔌 Q45: WebSocket & Real-time Streaming - WebSocket, Socket.IO, Centrifuge

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"WebSocket = persistent bidirectional TCP connection cho real-time data. Socket.IO = WebSocket wrapper với auto-reconnect + rooms. Centrifuge = scalable pub/sub với Redis for enterprise."**

**🔑 3 Technologies:**

**1. Native WebSocket API:**

- **Protocol**: `ws://` (unencrypted) hoặc `wss://` (SSL/TLS)
- **Persistent connection** - 1 handshake, reuse mãi
- **Bidirectional** - server push data bất cứ lúc nào
- Use case: Trading platforms (real-time prices), chat, live notifications
- Ưu điểm: Low latency (~50ms), less bandwidth than polling

**2. Socket.IO (High-Level Library):**

- **Auto-reconnect** khi connection lost
- **Fallback mechanisms**: WebSocket → HTTP long-polling (nếu WS blocked)
- **Rooms & Namespaces**: Organize connections (chat rooms, user-specific channels)
- **Broadcasting**: Send message to all/specific clients
- **Event-based API**: `socket.emit('event', data)` - cleaner than raw messages

**3. Centrifuge (Scalable Pub/Sub):**

- **Horizontal scaling** - multiple server instances share state via **Redis**
- **Channel subscriptions**: Client subscribe channels, server publish to channels
- **Presence**: Track online users in channels
- **History**: Replay missed messages (offline → online)
- Use case: Large-scale systems (>10k concurrent connections)

**⚠️ Lỗi Thường Gặp:**

- Không handle reconnection → connection lost = app broken
- Send large payloads → slow, dùng binary (ArrayBuffer) thay JSON
- Không authenticate WS connections → security risk
- Memory leak: không cleanup event listeners khi disconnect

**💡 Kiến Thức Senior:**

- **WebSocket vs SSE**: SSE = server → client only (simpler), WS = bidirectional
- **Heartbeat/Ping-Pong**: Detect dead connections (send ping every 30s, expect pong)
- **Binary frames**: `ws.send(arrayBuffer)` nhanh hơn JSON strings (~40%)
- **Backpressure**: Client slow consume → buffer overflow, implement flow control
- **Load balancing**: Sticky sessions (same client → same server) or Redis pub/sub share state

**⚡ Quick Summary:**

> WebSocket = persistent connection, real-time bidirectional communication. Socket.IO = WebSocket + fallback + rooms. Centrifuge = scalable real-time messaging với Redis

**💡 Ghi Nhớ:**

- 🌐 **WebSocket**: Native browser API, low-level, persistent TCP connection
- 🔌 **Socket.IO**: High-level library, auto-reconnect, fallback to polling
- 📡 **Centrifuge**: Enterprise solution, horizontal scaling, Redis pub/sub
- ⚡ **Use Case**: Trading (real-time price), Chat, Live dashboard, Notifications

**Trả lời:**

#### **Phần 1: WebSocket Basics**

**💡 WebSocket là gì?**

WebSocket là giao thức **persistent, bidirectional** communication giữa client và server qua **single TCP connection**.

**Tại sao dùng WebSocket thay vì REST API Polling?**

```typescript
// ❌🚫 REST API Polling - KHÔNG hiệu quả cho real-time data
setInterval(() => {
  fetch('/api/market-data') // 🌐📤 HTTP request mới mỗi lần
    .then((res) => res.json())
    .then((data) => updateUI(data));
}, 1000); // ⏰🔁 Gọi API mỗi giây! (3600 requests/hour per user)

/**
 * 🐞 VẤN ĐỀ VỚI POLLING:
 *
 * 1️⃣ 📡💸 Tốn băng thông: Mỗi request = full HTTP headers + body
 *    - Request headers: ~500 bytes (Cookie, User-Agent, Accept...)
 *    - Response headers: ~300 bytes (Content-Type, Cache-Control...)
 *    - Body: ~1KB data
 *    - Tổng: ~1.8KB mỗi request
 *    - 💥 1000 clients x 1 req/s = 1.8MB/s = 6.48GB/hour chỉ cho headers!
 *
 * 2️⃣ ⏱️🐌 Latency cao: HTTP handshake mỗi lần
 *    - DNS lookup: ~20ms (ấn chạm khi dùng lần đầu)
 *    - TCP handshake (SYN, SYN-ACK, ACK): ~50ms
 *    - TLS handshake (HTTPS): ~100ms
 *    - HTTP request/response: ~30ms
 *    - 💥 Tổng: ~200ms latency cho mỗi request (so với WebSocket: ~10ms)
 *
 * 3️⃣ 🔥💻 Server load cao: 1000 clients = 1000 requests/giây
 *    - Mỗi request tạo new TCP connection (nếu không keep-alive)
 *    - Parse HTTP headers, routing, middleware...
 *    - Database query mỗi lần (nếu không cache)
 *    - 💥 CPU usage cao, scale khó khăn
 *
 * 4️⃣ ⏰❌ Không real-time: Delay tối thiểu 1 giây
 *    - Price thay đổi ở 0.5s → user thấy ở 1.0s → Delay 0.5s
 *    - Giá cổ phiếu chứng khoán thay đổi liên tục → luôn outdated
 *
 * 5️⃣ 🗑️💸 Waste resources: Poll ngay cả khi không có data mới
 *    - 99% requests trả về data giống cũ → lãng phí
 *    - Server vẫn phải xử lý và trả về 304 Not Modified
 *    - Client vẫn tốn CPU parse response
 */

// ✅⚡ WebSocket - Real-time hiệu quả cho bi-directional streaming
const ws = new WebSocket('wss://market-data.example.com');
// 🔐🌐 wss:// = WebSocket Secure (encrypted với TLS, giống HTTPS)
// 💡 Chỉ cần 1 TCP connection, giữ mãi, không tạo lại

ws.onopen = () => {
  console.log('✅🔗 Connected - WebSocket handshake success');
  // 💡 Handshake chỉ 1 lần khi connect, sau đó persistent connection

  // 📤📋 Subscribe to channels (gửi message tới server)
  ws.send(
    JSON.stringify({
      type: 'subscribe', // 🏷️ Action type (custom protocol)
      symbols: ['VNM', 'HPG', 'VIC'], // 📊 Mã cổ phiếu muốn theo dõi
    })
  );
  // 💡 Chỉ gửi message nhỏ (~50 bytes), không có HTTP headers
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data); // 📥📋 Parse JSON data từ server
  updateUI(data); // ⚡🔄 Update UI ngay lập tức khi có data mới (< 10ms latency)
  // 💡 Server chỉ push khi giá thay đổi, không push khi giá giữ nguyên
};

/**
 * ✅ ƯU ĐIỂM WEBSOCKET:
 *
 * 1️⃣ 🔗💾 Persistent connection: Kết nối 1 lần, dùng mãi (giờ, ngày, tuần...)
 *    - Không cần TCP handshake lặp đi lặp lại
 *    - Không cần TLS handshake mỗi request
 *    - Connection overhead chỉ 1 lần khi connect
 *
 * 2️⃣ ⚡📡 Push data ngay lập tức: Latency < 10ms
 *    - Server detect giá thay đổi → push ngay qua persistent connection
 *    - Không cần đợi client poll
 *    - True real-time: Data đến client trong vòng 10ms
 *
 * 3️⃣ 📡💰 Tiết kiệm băng thông: Không có HTTP headers lặp lại
 *    - Message frame: ~6 bytes overhead (WebSocket framing)
 *    - Body: ~100 bytes JSON data (price update)
 *    - Tổng: ~106 bytes per message
 *    - 📊 So sánh: 106 bytes (WS) vs 1800 bytes (HTTP polling) = tiết kiệm 94%!
 *    - 💥 1000 clients x 10 updates/s = 1.06MB/s (thay vì 18MB/s với polling)
 *
 * 4️⃣ 💻👍 Server load thấp: Chỉ push khi có data mới
 *    - Không cần xử lý 1000 requests/s từ polling clients
 *    - Chỉ push 10 price updates/s tới 1000 clients (broadcast)
 *    - CPU usage giảm 90% so với polling
 *
 * 5️⃣ ⏰✅ True real-time: Không có polling delay
 *    - Giá thay đổi → user thấy ngay (< 50ms end-to-end)
 *    - Critical cho trading platforms (mỗi millisecond quan trọng)
 *
 * 6️⃣ 🔄↔️ Bidirectional: Client và Server đều có thể gửi message bất cứ lúc nào
 *    - Không cần chờ request/response cycle
 *    - Client: ws.send() bất kỳ lúc nào
 *    - Server: push bất kỳ lúc nào
 */
```

**WebSocket Lifecycle:**

```typescript
// 🔹 1. CONNECTING (readyState = 0)
const ws = new WebSocket('wss://api.example.com/stream');
// 🔗⏳ Tạo WebSocket instance, bắt đầu handshake process
console.log('State:', ws.readyState); // 0 - CONNECTING
// 💡 Lúc này: TCP connection đang setup, chưa sẵn sàng gửi/nhận data
// ❌ KHÔNG được gọi ws.send() khi readyState = 0 (sẽ throw error)

// 🔹 2. OPEN (readyState = 1)
ws.onopen = () => {
  console.log('State:', ws.readyState); // 1 - OPEN
  console.log(
    '✅🔓 Connected - WebSocket handshake thành công, có thể gửi message'
  );
  // 💡 Handshake flow (HTTP Upgrade):
  // 1️⃣ Client gửi HTTP request với "Upgrade: websocket" header
  // 2️⃣ Server trả về 101 Switching Protocols
  // 3️⃣ TCP connection upgrade thành WebSocket connection
  // 4️⃣ Sẵn sàng bidirectional communication

  // 📤📋 Send subscribe message tới server
  ws.send(
    JSON.stringify({
      type: 'subscribe', // 🏷️ Action type (application-level protocol)
      symbols: ['BTCUSDT', 'ETHUSDT'], // 💰 Crypto trading pairs
    })
  );
  // 💡 ws.send() chấp nhận: string, ArrayBuffer, Blob, ArrayBufferView
  // 🚀 Binary data (ArrayBuffer) nhanh hơn JSON string ~40%
};

// 🔹 3. MESSAGE - Nhận data từ server (server push)
ws.onmessage = (event: MessageEvent) => {
  // 📥📊 event.data có thể là: string (JSON), ArrayBuffer (binary), Blob
  const data = JSON.parse(event.data); // 📋 Parse JSON string → object
  console.log('📥🔔 Received:', data);
  // 💡 Server có thể push bất cứ lúc nào, không cần client request

  // 🔄📊 Update UI với price data mới
  updateTickerPrice(data.symbol, data.price);
  // 🚀 Latency: Server detect change → push → client receive < 10ms
  // 📊 Tần suất: Có thể nhận 100-1000 messages/giây (high-frequency trading)
};

// 🔹 4. ERROR - Xử lý lỗi (network issues, server crash...)
ws.onerror = (error) => {
  console.error('❌🚨 WebSocket error:', error);
  // 💡 onerror CHI TIẾT hạn chế:
  // - Browser không expose chi tiết lỗi (security reasons)
  // - Chỉ biết "có lỗi xảy ra", không biết lỗi gì
  // - onclose event sẽ fire ngay sau onerror (check close code ở đó)

  showNotification('Connection error. Retrying...'); // 📢 Thông báo user
  // 💡 Best practice: Auto-reconnect với exponential backoff
};

// 🔹 5. CLOSE (readyState = 3)
ws.onclose = (event: CloseEvent) => {
  console.log('State:', ws.readyState); // 3 - CLOSED
  console.log('🚪❌ Closed');
  console.log('Code:', event.code); // 🔢 Close code (1000-4999)
  console.log('Reason:', event.reason); // 📝 Close reason string (optional)
  console.log('Was Clean:', event.wasCleanClose); // 🧹 true nếu close frame được gửi/nhận

  /**
   * 📊 CLOSE CODES (RFC 6455):
   *
   * ✅ 1000: Normal Closure
   *    - Client/server close bình thường (user logout, tab close...)
   *    - wasCleanClose = true
   *    - Không cần reconnect
   *
   * 🚪 1001: Going Away
   *    - Page refresh, browser navigation, server shutdown
   *    - wasCleanClose = true
   *    - Có thể reconnect nếu server shutdown tạm thời
   *
   * 💥 1006: Abnormal Closure
   *    - Connection mất đột ngột (network issue, server crash)
   *    - KHÔNG có close frame (wasCleanClose = false)
   *    - NÊN reconnect với exponential backoff
   *
   * 🚫 1008: Policy Violation
   *    - Server reject (authentication failed, invalid token...)
   *    - KHÔNG reconnect (cần user action - re-login)
   *
   * 🚨 1011: Server Error
   *    - Internal server error (uncaught exception, database down...)
   *    - Có thể reconnect (server có thể recover)
   *
   * 🔧 1012: Service Restart
   *    - Server restart/maintenance
   *    - NÊN reconnect sau vài giây
   *
   * 🔐 1015: TLS Handshake Failed
   *    - SSL/TLS certificate issue
   *    - KHÔNG reconnect (cần fix certificate)
   *
   * 💡 Custom codes (4000-4999):
   *    - Application-specific close reasons
   *    - Ví dụ: 4001 = Rate limit exceeded, 4002 = Session expired
   */

  // 🧠🔄 Reconnection logic
  if (shouldReconnect(event.code)) {
    // 💡 NÊN reconnect cho:
    // - 1006 (network issue)
    // - 1011 (server error - tạm thời)
    // - 1012 (service restart)
    scheduleReconnect(); // ⚡ Exponential backoff: 1s, 2s, 4s, 8s, 16s...
  } else {
    // 🚫 KHÔNG reconnect cho:
    // - 1000 (normal closure)
    // - 1008 (auth failed - cần user re-login)
    // - 1015 (TLS issue - cần fix certificate)
    showError('Connection closed. Please refresh or contact support.');
  }
};

// 🧹🗑️ Cleanup khi component unmount (React)
useEffect(() => {
  const ws = new WebSocket(url);
  // ... setup event handlers ...

  return () => {
    // 💡 QUAN TRỌNG: Close connection khi component unmount
    ws.close(1000, 'Component unmounted'); // ✅ Clean close (normal closure)
    // 💡 Nếu không close:
    // - Memory leak (connection vẫn active)
    // - Server vẫn giữ connection (waste resources)
    // - Event handlers vẫn fire (component đã unmount → error)
  };
}, [url]); // 🔄 Re-create connection nếu URL thay đổi
```

- 1001: Going away (page refresh)
- 1006: Abnormal closure (no close frame)
- 1008: Policy violation (auth error)
- 1011: Server error
  \*/

// Reconnect logic
if (shouldReconnect(event.code)) {
scheduleReconnect();
}
};

// Cleanup khi unmount
useEffect(() => {
const ws = new WebSocket(url);

return () => {
ws.close(1000, 'Component unmounted'); // ✅ Clean close
};
}, [url]);

````

---

#### **Phần 2: Production WebSocket Architecture**

**Pattern 1: Reference Counting Subscription Manager**

```typescript
/**
 * 🐞 VẤN ĐỀ: Multiple components subscribe to same symbol
 *
 * Scenario trong real app:
 * 📊 Component A (Chart): Subscribe VNM (render price chart)
 * 📋 Component B (Ticker): Subscribe VNM (để hiển thị giá hiện tại)
 * 📊 Component C (Chart): Subscribe HPG (chart khác)
 *
 * ❌🚨 SOLUTION TỒI: Tạo 3 WebSocket connections riêng biệt
 *    - 3 TCP connections (waste network resources)
 *    - 3 TLS handshakes (waste CPU, memory)
 *    - Server phải maintain 3 connections (scale khó khăn)
 *    - Component A và B nhận duplicate VNM data (waste bandwidth)
 *
 * ✅⚡ SOLUTION TỐI ƯU: 1 connection shared, Reference Counting
 *    - 1 TCP connection duy nhất (optimal network usage)
 *    - Track số lượng components subscribe mỗi symbol
 *    - Chỉ subscribe khi counter = 0 → 1 (first subscriber)
 *    - Chỉ unsubscribe khi counter = 1 → 0 (last subscriber leaves)
 *    - Components A và B share VNM data stream (efficient)
 */

interface SubscriptionTracker {
  // 📊 Map<symbol, tracker data>
  subscriptions: Map<string, {
    count: number;          // 🔢 Số lượng components đang subscribe symbol này
    subscribers: Set<string>; // 🏷️ Set các componentId (unique, không duplicate)
  }>;
}

class LiveDataManager {
  private ws: WebSocket | null = null;  // 🔗 Shared WebSocket connection
  private tracker = new Map<string, { count: number; subscribers: Set<string> }>();
  // 💡 tracker structure ví dụ:
  // Map {
  //   "VNM" => { count: 2, subscribers: Set(["comp-A", "comp-B"]) },
  //   "HPG" => { count: 1, subscribers: Set(["comp-C"]) }
  // }

  subscribe(symbols: string[], componentId: string) {
    // 📥📋 Hàm này được gọi từ component's useEffect khi mount
    // 🏷️ componentId: unique ID của component (ví dụ: "chart-VNM-123")

    symbols.forEach(symbol => {
      const current = this.tracker.get(symbol);  // 🔍 Check symbol đã được subscribe chưa

      if (!current) {
        // 🔥🎆 FIRST SUBSCRIBER for this symbol
        // 💡 Chưa có component nào subscribe symbol này trước đó

        this.tracker.set(symbol, {
          count: 1,  // 🔢 Bắt đầu với count = 1
          subscribers: new Set([componentId])  // 🏷️ Set với 1 element
        });

        // 📤🔔 Gửi subscribe message tới server
        this.ws?.send(JSON.stringify({
          type: 'subscribe',  // 🏷️ Action type
          symbol  // 📊 Symbol muốn subscribe (ví dụ: "VNM")
        }));
        // 💡 Server bắt đầu push price updates cho symbol này
        // 🚀 Từ giờ, mọi khi giá VNM thay đổi → server push → onmessage fires
      } else {
        // ⚡🔄 ALREADY SUBSCRIBED - Reuse existing subscription
        // 💡 Đã có component khác subscribe symbol này rồi
        // 🚀 KHÔNG gửi subscribe message nữa (tiết kiệm bandwidth)

        current.count++;  // 🔢 Tăng counter: 1 → 2, 2 → 3...
        current.subscribers.add(componentId);  // 🏷️ Thêm componentId vào Set
        // 💡 Set tự động handle duplicate (nếu componentId giống nhau, không thêm lần 2)

        // 👍 Component mới sẽ tự động nhận data từ shared connection
        // 🚀 onmessage handler broadcast data tới ALL subscribers
      }
    });

    return componentId;  // 🏷️ Return ID để dùng cho unsubscribe sau này
  }

  unsubscribe(componentId: string) {
    // 🗑️🧹 Hàm này được gọi từ component's cleanup (useEffect return)

    this.tracker.forEach((data, symbol) => {
      // 🔍 Duyệt qua ALL symbols để tìm componentId này

      if (data.subscribers.has(componentId)) {
        // ✅ Component này đang subscribe symbol này

        data.subscribers.delete(componentId);  // 🗑️ Xoá componentId ra khỏi Set
        data.count--;  // 🔢 Giảm counter: 3 → 2, 2 → 1, 1 → 0

        if (data.count === 0) {
          // 🗑️🚨 LAST SUBSCRIBER UNMOUNTED
          // 💡 Không còn component nào cần data của symbol này

          this.tracker.delete(symbol);  // 🗑️ Xoá symbol khỏi tracker Map

          // 📤🚫 Gửi unsubscribe message tới server
          this.ws?.send(JSON.stringify({
            type: 'unsubscribe',  // 🏷️ Action type
            symbol  // 📊 Symbol muốn unsubscribe
          }));
          // 💡 Server ngừng push price updates cho symbol này
          // 🚀 Tiết kiệm bandwidth (không gửi data không cần thiết)
          // 💻 Tiết kiệm server CPU (không xử lý updates cho symbol này)
        } else {
          // ⚡👥 Vẫn còn subscribers khác (count > 0)
          // 💡 KHÔNG unsubscribe (components khác vẫn cần data)
          // 🚀 Connection vẫn tiếp tục nhận data cho các components còn lại
        }
      }
    });
  }
}

/**
 * 📊 TIMELINE EXAMPLE - Lifecycle của subscriptions:
 *
 * Time | Event                    | VNM count | HPG count | Action              | Network Traffic
 * -----|--------------------------|-----------|-----------|---------------------|------------------
 * T0   | 🎆 Component A mount    | 0 → 1     | 0         | ✅ Send subscribe  | 📤 {subscribe: "VNM"}
 *      | (Chart VNM)              |           |           | VNM                 |
 *      |                          |           |           |                     |
 * T1   | 🎆 Component B mount    | 1 → 2     | 0         | ⚡ Reuse connection | 🚫 No network (reuse!)
 *      | (Ticker VNM)             |           |           | (không gửi msg)     |
 *      |                          |           |           |                     |
 * T2   | 🎆 Component C mount    | 2         | 0 → 1     | ✅ Send subscribe  | 📤 {subscribe: "HPG"}
 *      | (Chart HPG)              |           |           | HPG                 |
 *      |                          |           |           |                     |
 * T3   | 🗑️ Component A unmount | 2 → 1     | 1         | ⚡ Keep subscription| 🚫 No network (vẫn còn B)
 *      |                          |           |           | (count > 0)         |
 *      |                          |           |           |                     |
 * T4   | 🗑️ Component B unmount | 1 → 0     | 1         | 🗑️ Send unsubscribe| 📤 {unsubscribe: "VNM"}
 *      |                          |           |           | VNM (last sub)      |
 *      |                          |           |           |                     |
 * T5   | 🗑️ Component C unmount | 0         | 1 → 0     | 🗑️ Send unsubscribe| 📤 {unsubscribe: "HPG"}
 *      |                          |           |           | HPG                 |
 *
 * 💡 KẾT QUẢ:
 * - Chỉ gửi 2 subscribe messages (VNM, HPG) thay vì 3
 * - Tiết kiệm 33% network traffic
 * - Components A và B share VNM data (efficient)
 * - Server chỉ maintain 1 connection cho 3 components (scalable)
 *
 * 🚀 BENEFITS:
 * 1️⃣ 📡 Network efficiency: Giảm số lượng messages gửi/nhận
 * 2️⃣ 💻 Server scalability: 1 connection per user (không phải per component)
 * 3️⃣ 💧 Memory efficient: Shared data stream (không duplicate)
 * 4️⃣ 🚀 Fast unmount: Component unmount không ảnh hưởng data của components khác
 */
 * T2   | Component C mounts       | 2 → 3     | ⚡ Reuse connection
 * T3   | Component A unmounts     | 3 → 2     | ✋ Keep connection
 * T4   | Component B unmounts     | 2 → 1     | ✋ Keep connection
 * T5   | Component C unmounts     | 1 → 0     | 🗑️ Unsubscribe, close
 */
````

**Pattern 2: Zustand Store Integration**

```typescript
// File: lib/live-data-manager/stores/useLiveDataStore.ts

/**
 * 📊 ĐỊNH NGHĨA TYPES - Cấu trúc dữ liệu ticker
 */
interface TickerData {
  symbol: string; // 📊 Mã cổ phiếu (VD: "VNM", "HPG")
  lastPrice: number; // 💰 Giá cuối cùng
  change: number; // 📈 Thay đổi (% hoặc số tuyệt đối)
  volume: number; // 📊 Khối lượng giao dịch
  timestamp: number; // ⏰ Thời gian cập nhật (Unix timestamp)
}

/**
 * 🏪 STORE INTERFACE - Định nghĩa state và actions của Zustand store
 */
interface LiveDataStore {
  tickerData: Record<string, TickerData>; // 📊 Map<symbol, tickerData> - Lưu data của tất cả symbols
  updateTickerData: (data: TickerData) => void; // ✏️ Cập nhật 1 ticker đơn lẻ
  batchUpdate: (updates: TickerData[]) => void; // 📦 Cập nhật nhiều tickers cùng lúc (hiệu quả hơn)
}

/**
 * 🏪 ZUSTAND STORE - Global state management cho live market data
 *
 * 💡 Zustand là state management library nhẹ, không cần Provider wrapper
 * 💡 Store này được dùng bởi TẤT CẢ components cần live data
 * 💡 Components subscribe vào store → tự động re-render khi data thay đổi
 */
const useLiveDataStore = create<LiveDataStore>((set) => ({
  tickerData: {}, // 📊 Khởi tạo empty object (chưa có data)

  /**
   * ✏️ UPDATE SINGLE TICKER - Cập nhật 1 symbol tại một thời điểm
   *
   * @param data - TickerData của 1 symbol cần cập nhật
   *
   * 💡 Cách hoạt động:
   * 1. Nhận data mới của 1 symbol (VD: VNM)
   * 2. Merge vào state hiện tại (giữ nguyên các symbols khác)
   * 3. Zustand tự động notify tất cả components đang subscribe
   * 4. Components re-render nếu selector của chúng thay đổi
   */
  updateTickerData: (data) =>
    set((state) => ({
      tickerData: {
        ...state.tickerData, // 📋 Giữ nguyên tất cả symbols cũ
        [data.symbol]: data, // ✏️ Ghi đè/Thêm mới symbol này
      },
    })),

  /**
   * 📦 BATCH UPDATE - Cập nhật nhiều symbols cùng lúc (HIỆU QUẢ HƠN)
   *
   * @param updates - Array các TickerData cần cập nhật
   *
   * 💡 TẠI SAO BATCH UPDATE TỐT HƠN?
   * - updateTickerData: Mỗi lần gọi → 1 state update → 1 re-render
   * - batchUpdate: 1 lần gọi → 1 state update → 1 re-render (cho tất cả updates)
   * - Nếu có 100 updates: batchUpdate chỉ trigger 1 re-render thay vì 100!
   *
   * 🚀 Use case: Server gửi batch data (100 tickers trong 1 message)
   */
  batchUpdate: (updates) =>
    set((state) => {
      const newData = { ...state.tickerData }; // 📋 Clone state hiện tại

      // 🔄 Loop qua tất cả updates và merge vào newData
      updates.forEach((data) => {
        newData[data.symbol] = data; // ✏️ Ghi đè từng symbol
      });

      return { tickerData: newData }; // ✅ Return state mới (1 lần duy nhất)
      // 💡 Zustand so sánh state cũ vs mới → notify subscribers → re-render
    }),
}));

/**
 * 📥 WEBSOCKET MESSAGE HANDLER - Xử lý messages từ WebSocket
 *
 * 💡 Hàm này được gọi mỗi khi nhận message từ server
 * 💡 Phân biệt single update vs batch update để dùng đúng method
 */
ws.onmessage = (event) => {
  const data = JSON.parse(event.data); // 📋 Parse JSON string → object/array

  if (Array.isArray(data)) {
    // 📦 BATCH UPDATE - Server gửi array các tickers
    // VD: [{symbol: "VNM", price: 85000}, {symbol: "HPG", price: 45000}, ...]
    useLiveDataStore.getState().batchUpdate(data);
    // 🚀 1 state update → 1 re-render cho tất cả components
  } else {
    // ✏️ SINGLE UPDATE - Server gửi 1 ticker đơn lẻ
    // VD: {symbol: "VNM", price: 85000, change: 2.5, ...}
    useLiveDataStore.getState().updateTickerData(data);
    // 🚀 1 state update → 1 re-render cho components subscribe symbol này
  }
};
```

**Pattern 3: React Hook Integration**

```typescript
// File: lib/live-data-manager/hooks/useLiveMarketData.ts

/**
 * 🎣 CUSTOM HOOK: useLiveMarketData
 *
 * 💡 Hook này quản lý WebSocket connection cho toàn bộ app
 * 💡 Chỉ cần gọi 1 lần ở component root (App.tsx)
 * 💡 Tất cả components khác dùng chung connection này
 *
 * @returns wsRef - Reference đến WebSocket instance (để dùng ở components khác nếu cần)
 */
const useLiveMarketData = () => {
  const wsRef = useRef<WebSocket | null>(null);
  // 💾 useRef: Lưu WebSocket instance, không trigger re-render khi thay đổi
  // 💡 Dùng ref thay vì state vì không cần re-render khi connection thay đổi

  const updateStore = useLiveDataStore((state) => state.updateTickerData);
  // 📊 Lấy function updateTickerData từ Zustand store
  // 💡 Selector này chỉ re-create khi store thay đổi (hiếm khi)

  useEffect(() => {
    // 🎆 EFFECT CHẠY KHI COMPONENT MOUNT
    // 💡 Chỉ chạy 1 lần khi component mount (dependencies = [])

    const ws = new WebSocket('wss://market.example.com/stream');
    // 🔗 Tạo WebSocket connection mới
    wsRef.current = ws; // 💾 Lưu vào ref để dùng ở nơi khác

    ws.onopen = () => {
      console.log('✅ WebSocket connected');

      // 🔄 RE-SUBSCRIBE sau khi reconnect
      // 💡 Nếu đây là reconnect (không phải lần đầu), cần subscribe lại các symbols đang active
      const activeSymbols = getActiveSubscriptions();
      // 📋 Lấy danh sách symbols đang được subscribe (từ LiveDataManager hoặc global state)

      if (activeSymbols.length > 0) {
        // ✅ Có symbols cần subscribe → gửi subscribe message
        ws.send(
          JSON.stringify({
            type: 'subscribe', // 🏷️ Action type
            symbols: activeSymbols, // 📊 Array symbols cần subscribe
          })
        );
        // 💡 Server sẽ bắt đầu push data cho các symbols này
      }
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data); // 📋 Parse JSON → object
      updateStore(data); // ✏️ Cập nhật Zustand store → trigger re-render cho components
      // 💡 Components đang subscribe store sẽ tự động nhận data mới
    };

    ws.onerror = (error) => {
      console.error('❌ WebSocket error:', error);
      // 💡 Browser không expose chi tiết lỗi (security)
      // 🚨 onclose sẽ fire ngay sau onerror → check close code ở đó
    };

    ws.onclose = (event) => {
      console.log('🔌 WebSocket closed:', event.code);

      // 🔄 AUTO-RECONNECT với exponential backoff
      if (shouldReconnect(event.code)) {
        // ✅ Nên reconnect (network issue, server restart...)
        setTimeout(() => {
          console.log('🔄 Reconnecting...');
          // 🔄 Re-run effect để tạo connection mới
          // 💡 useEffect sẽ chạy lại → tạo WebSocket mới
        }, getReconnectDelay());
        // ⏰ Delay tăng exponentially: 1s → 2s → 4s → 8s...
      }
    };

    return () => {
      // 🧹 CLEANUP khi component unmount
      ws.close(1000, 'Component cleanup'); // ✅ Clean close (normal closure)
      // 💡 Nếu không close: memory leak + server vẫn giữ connection
    };
  }, []); // 🔄 Dependencies = [] → chỉ chạy 1 lần khi mount

  return wsRef; // 📤 Return ref để components khác có thể dùng nếu cần
};

/**
 * 💡 COMPONENT USAGE - Cách dùng hook trong component
 */
const StockWatchlist = () => {
  // 🎆 Initialize WebSocket manager (chỉ cần gọi 1 lần)
  useLiveMarketData();
  // 💡 Hook này setup WebSocket connection và event handlers
  // 💡 Tất cả components trong app dùng chung connection này

  // 📥 Subscribe to symbols (gửi subscribe message tới server)
  useSubscribeTickers('ticker', ['VNM', 'HPG', 'VIC']);
  // 💡 Hook này gửi subscribe message qua WebSocket
  // 💡 Server bắt đầu push data cho các symbols này

  // 📊 Get data from store (selective subscription)
  const tickerData = useLiveDataStore(
    (state) => state.tickerData, // ⚡ Selector: chỉ lấy tickerData
    shallow // 🔍 Shallow compare: chỉ re-render nếu object reference thay đổi
    // 💡 Tránh re-render không cần thiết khi state khác thay đổi
  );
  // 💡 Component này chỉ re-render khi tickerData thay đổi
  // 💡 Không re-render khi state khác trong store thay đổi

  return (
    <div>
      {Object.entries(tickerData).map(([symbol, data]) => (
        // 🔄 Map qua tất cả tickers trong store
        <StockRow key={symbol} symbol={symbol} data={data} />
        // 📊 Render mỗi ticker thành 1 row
      ))}
    </div>
  );
};
```

---

#### **Phần 3: Performance Optimization**

**Optimization 1: Throttling với requestAnimationFrame**

```typescript
/**
 * 🐞 VẤN ĐỀ: Nhận 1000 price updates/giây từ WebSocket
 *
 * 💥 TÁC ĐỘNG:
 * - Update React state 1000 lần/giây → 1000 re-renders
 * - Browser chỉ refresh UI 60fps (60 lần/giây)
 * - 940 updates lãng phí (user không thấy được)
 * - High CPU usage (React reconciliation overhead)
 * - UI lag, frame drops (jank)
 *
 * ✅ GIẢI PHÁP: Throttle UI updates với requestAnimationFrame
 * - Browser call RAF callback trước mỗi frame (~16.67ms @ 60fps)
 * - Chỉ update UI 60 lần/giây (match screen refresh rate)
 * - Lưu data mới nhất vào ref (không trigger re-render)
 * - RAF loop đọc ref và update state (1 re-render per frame)
 * - Tối ưu: 1000 messages → 60 UI updates (giảm 94%!)
 */

const useThrottledWebSocket = () => {
  const [data, setData] = useState<TickerData | null>(null);
  // 📊 State để trigger re-render (React component sẽ re-render khi setData)

  const latestDataRef = useRef<TickerData | null>(null);
  // 💾 Ref để lưu data mới nhất (update ref KHÔNG trigger re-render)
  // 💡 WebSocket push 1000 messages/s → latestDataRef được ghi đè 1000 lần
  // 🚀 Chỉ giữ message mới nhất, discard 999 messages cũ (acceptable cho price data)

  const rafIdRef = useRef<number | null>(null);
  // 🎬 Ref lưu RAF ID để cancel khi cleanup

  // 🔄📺 UI update loop - chạy tối đa 60fps
  const updateUI = useCallback(() => {
    if (latestDataRef.current) {
      // ✅ Có data mới chờ update

      setData(latestDataRef.current); // 📊 Update React state → trigger re-render
      // 💡 Chỉ call setData 1 lần per frame (~60 times/s)
      // 🚀 Component re-render smooth 60fps

      latestDataRef.current = null; // 🧹 Clear ref (mark as "processed")
      // 💡 Nếu không clear: RAF cycle tiếp theo sẽ update lại với cùng data (waste)
    }
    // 🔁 Schedule next RAF cycle
    rafIdRef.current = requestAnimationFrame(updateUI);
    // 💡 Browser sẽ call updateUI trước next frame (~16.67ms sau)
    // 🚀 Tạo vòng lặp vô hạn: updateUI → RAF → updateUI → RAF...
  }, []);

  useEffect(() => {
    // 🎆 Start animation loop khi component mount
    rafIdRef.current = requestAnimationFrame(updateUI);
    // 💡 Khởi động RAF loop ngay (không đợi data)

    return () => {
      // 🧹🗑️ Cleanup khi component unmount
      if (rafIdRef.current) {
        cancelAnimationFrame(rafIdRef.current); // 🚫 Dừng RAF loop
        // 💡 Nếu không cancel: RAF callback vẫn fire sau khi component unmount → error
        // 🚀 Prevent memory leak
      }
    };
  }, [updateUI]); // 🔄 Re-create loop nếu updateUI function thay đổi (hiếm khi xảy ra)

  // 📥📫 WebSocket message handler
  const onMessage = useCallback((event: MessageEvent) => {
    const parsed = JSON.parse(event.data); // 📋 Parse JSON string → object

    // ⚡💾 Chỉ STORE data vào ref, KHÔNG update state ngay
    latestDataRef.current = parsed;
    // 💡 Ghi đè ref (instant, không trigger re-render)
    // 🚀 Nếu nhận 1000 messages/s: latestDataRef được ghi đè 1000 lần
    // 📊 RAF loop sẽ đọc latestDataRef mỗi frame và update state
    // 🚀 Kết quả: 1000 writes (cheap) → 60 reads + updates (expensive)

    // 🚫 KHÔNG gọi setData(parsed) ở đây!
    // ❌ Nếu gọi: 1000 setData/s → 1000 re-renders → UI freeze
  }, []);

  return { data, onMessage };
};

/**
 * 📊 KẾT QUẢ PERFORMANCE:
 *
 * ❌🐌 BEFORE (no throttling):
 * - WebSocket: 1000 messages/s
 * - React: 1000 setData() calls/s
 * - Re-renders: 1000 times/s
 * - CPU usage: ~80% (React reconciliation + DOM updates)
 * - UI: Lag, frame drops (16ms frame budget exceeded)
 * - User experience: Janky, unresponsive
 *
 * ✅⚡ AFTER (RAF throttling):
 * - WebSocket: 1000 messages/s (unchanged)
 * - Ref writes: 1000 times/s (cheap, no re-render)
 * - React: 60 setData() calls/s (match 60fps)
 * - Re-renders: 60 times/s (optimal)
 * - CPU usage: ~15% (giảm 81%!)
 * - UI: Smooth 60fps, no frame drops
 * - User experience: Buttery smooth
 *
 * 🚀 ƯU ĐIỂM:
 * 1️⃣ 💻 CPU efficiency: Giảm 81% CPU usage
 * 2️⃣ 📺 Smooth UI: Always 60fps (no jank)
 * 3️⃤ 📊 Show latest data: User luôn thấy giá mới nhất
 * 4️⃣ 🔋 Battery friendly: Mobile devices tốn ít pin hơn
 * 5️⃣ 🧠 Simple code: useRef + RAF (không cần lib)
 *
 * 💡 TRADE-OFFS:
 * - "Miss" 940 intermediate values (~94% data)
 * - ✅ Acceptable cho price display (user chỉ cần giá mới nhất)
 * - ❌ KHOONG acceptable cho order book (cần mọi update để calculate depth)
 */
```

**Optimization 2: Selective Re-rendering**

```typescript
/**
 * ❌ BAD PATTERN: Update entire store → Tất cả components re-render
 *
 * 🐞 VẤN ĐỀ:
 * - Mỗi lần update → replace toàn bộ tickers object
 * - Zustand so sánh: object cũ !== object mới → notify TẤT CẢ subscribers
 * - Components subscribe tickers → re-render dù chỉ 1 symbol thay đổi
 * - Performance kém: 1000 components re-render khi chỉ 1 symbol update
 */
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateAll: (newTickers) => set({ tickers: newTickers }),
  // 💥 Tất cả components subscribe tickers sẽ re-render!
  // 💥 Dù chỉ 1 symbol trong newTickers thay đổi
}));

/**
 * ✅ GOOD PATTERN: Selective update + selector
 *
 * 🚀 GIẢI PHÁP:
 * - Chỉ update symbol cụ thể (merge vào state cũ)
 * - Components dùng selector để chỉ subscribe symbol mình cần
 * - Zustand chỉ notify components có selector thay đổi
 * - Performance tốt: Chỉ 1 component re-render khi symbol đó update
 */
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateTicker: (symbol, data) =>
    set((state) => ({
      tickers: {
        ...state.tickers, // 📋 Giữ nguyên các symbols khác
        [symbol]: data, // ✏️ Chỉ update symbol này
      },
    })),
  // 💡 Zustand so sánh: Chỉ symbol này thay đổi → chỉ notify components subscribe symbol này
}));

/**
 * 💡 COMPONENT PATTERN: Selective subscription với selector
 *
 * 🎯 Mỗi component chỉ subscribe symbol mình cần
 * 🚀 Chỉ re-render khi symbol đó thay đổi
 */
const StockRow = ({ symbol }) => {
  // ⚡ SELECTOR: Chỉ lấy data của symbol này
  const data = useLiveDataStore(
    (state) => state.tickers[symbol], // 📊 Selector function: trả về tickerData[symbol]
    shallow // 🔍 Shallow compare: chỉ re-render nếu reference thay đổi
    // 💡 Nếu symbol khác update → selector này trả về cùng reference → không re-render
  );

  // ✅ Chỉ re-render khi symbol này update
  // ❌ Không re-render khi symbols khác update
  // 🚀 Performance: 1000 rows → chỉ 1 row re-render khi 1 symbol update

  return (
    <div>
      {symbol}: {data?.price}
    </div>
  );
};
```

**Optimization 3: Virtual Scrolling**

```typescript
/**
 * ❌ BAD PATTERN: Render tất cả rows → Performance kém
 *
 * 🐞 VẤN ĐỀ:
 * - Render 1000 DOM nodes cùng lúc → chậm
 * - Browser phải maintain 1000 elements trong DOM → tốn memory
 * - Scroll lag vì phải reflow/repaint nhiều elements
 * - Initial render chậm: 500ms+ để render 1000 rows
 */
const Watchlist = ({ data }) => {
  return data.map((item) => <StockRow data={item} />);
  // 💥 1000 DOM nodes → Slow render, high memory
  // 💥 User chỉ thấy ~20 rows trên màn hình nhưng render 1000 rows!
};

/**
 * ✅ GOOD PATTERN: Virtual scrolling - Chỉ render visible rows
 *
 * 🚀 GIẢI PHÁP:
 * - Chỉ render ~20 rows visible trên màn hình
 * - Khi scroll → unmount rows cũ, mount rows mới
 * - Giữ tổng height của list để scrollbar đúng
 * - Performance: 20 DOM nodes thay vì 1000
 */
import { AgGridReact } from 'ag-grid-react';

const Watchlist = ({ data }) => {
  // 📋 Column definitions (memoized để tránh re-create)
  const columnDefs = useMemo(
    () => [
      { field: 'symbol', headerName: 'Symbol' }, // 📊 Cột mã cổ phiếu
      { field: 'lastPrice', headerName: 'Price' }, // 💰 Cột giá
      { field: 'change', headerName: 'Change' }, // 📈 Cột thay đổi
    ],
    []
  ); // 🔄 Chỉ tạo 1 lần khi component mount

  return (
    <AgGridReact
      rowData={data} // 📊 Tất cả data (1000 rows)
      columnDefs={columnDefs} // 📋 Định nghĩa cột
      // 🚀 AG Grid tự động dùng virtual scrolling
      // 💡 Chỉ render ~20 visible rows thay vì 1000
      // 💡 Khi scroll → tự động render rows mới, unmount rows cũ
    />
  );
};

/**
 * 📊 PERFORMANCE COMPARISON:
 *
 * ❌ No virtual scrolling:
 * - DOM nodes: 1000 elements
 * - Initial render: ~500ms
 * - Memory: ~50MB (1000 React components)
 * - Scroll FPS: ~30fps (lag)
 *
 * ✅ Virtual scrolling:
 * - DOM nodes: ~20 elements (chỉ visible)
 * - Initial render: ~16ms (60fps)
 * - Memory: ~1MB (20 React components)
 * - Scroll FPS: 60fps (smooth)
 *
 * 🚀 KẾT QUẢ:
 * - Render time: Giảm 97% (500ms → 16ms)
 * - Memory: Giảm 98% (50MB → 1MB)
 * - Scroll performance: Tăng 100% (30fps → 60fps)
 */
```

**Optimization 4: Batch Updates**

```typescript
// ❌🐌 BAD: Update từng ticker một (individual updates)
ws.onmessage = (event) => {
  const data = JSON.parse(event.data); // 📋 1 ticker data
  updateTicker(data.symbol, data); // 📊 Update store ngay
  // 💥 VẤN ĐỀ:
  // - Nếu nhận 100 messages trong 16ms (1 frame @ 60fps)
  // - 100 updateTicker() calls → 100 store updates
  // - Zustand notify subscribers 100 lần
  // - Components re-render 100 lần trong 1 frame
  // - 💥 Exceed 16ms frame budget → frame drop → jank
};

// ✅⚡ GOOD: Batch updates (collect → flush)
let batchQueue: TickerData[] = []; // 📦 Queue chứa pending updates
let batchTimer: NodeJS.Timeout | null = null; // ⏰ Timer để flush queue

ws.onmessage = (event) => {
  const data = JSON.parse(event.data); // 📋 Parse message
  batchQueue.push(data); // 📦➕ Thêm vào queue (không update store)
  // 💡 Chỉ collect data, chưa xử lý

  if (!batchTimer) {
    // ⏰ Lần đầu tiên trong batch → schedule flush
    batchTimer = setTimeout(() => {
      // 📦💨 Flush queue sau 16ms (1 frame @ 60fps)
      // 💡 16ms = thời gian 1 frame, browser refresh UI mỗi 16ms

      batchUpdateTickers(batchQueue); // 🔄 Batch update store 1 lần
      // 💡 batchUpdateTickers nhận array 100 items, update store 1 lần duy nhất
      // 🚀 Zustand notify subscribers 1 lần (thay vì 100 lần)
      // ✅ Components re-render 1 lần per frame (optimal)

      batchQueue = []; // 🧹 Clear queue
      batchTimer = null; // 🧹 Reset timer
      // 💡 Chuẩn bị cho batch tiếp theo
    }, 16); // ⏰ 16ms = 1 frame @ 60fps
    // 💡 Nếu messages đến trong 16ms window → cùng batch
    // 🚀 Nếu messages đến sau 16ms → batch mới
  }
  // 💡 Nếu batchTimer đang chạy: chỉ push vào queue, không schedule timer mới
  // 🚀 Mọi messages trong 16ms window đều vào cùng batch
};

/**
 * 📊 IMPLEMENTATION: batchUpdateTickers
 *
 * 💡 Hàm này nhận array các ticker updates và update store 1 lần duy nhất
 * 🚀 Hiệu quả hơn update từng ticker một (100 updates → 1 re-render)
 */
const batchUpdateTickers = (updates: TickerData[]) => {
  useLiveDataStore.setState((state) => {
    // 📋 Clone state hiện tại (không mutate state cũ)
    const newTickers = { ...state.tickers };
    // 💡 Spread operator tạo shallow copy → không ảnh hưởng state cũ

    // 🔄 Loop qua tất cả updates và merge vào newTickers
    updates.forEach((data) => {
      newTickers[data.symbol] = data; // ✏️ Ghi đè/Thêm mới từng symbol
    });
    // 💡 Loop qua 100 items, nhưng chỉ update state 1 lần (bên ngoài loop)
    // 💡 Nếu update từng ticker: 100 lần setState → 100 re-renders
    // 🚀 Batch update: 1 lần setState → 1 re-render

    return { tickers: newTickers }; // ✅ Return new state
    // 🚀 Zustand detect state change và notify subscribers 1 lần duy nhất
    // 💡 Components chỉ re-render 1 lần thay vì 100 lần
  });
};

/**
 * 📊 PERFORMANCE COMPARISON:
 *
 * ❌ INDIVIDUAL UPDATES (no batching):
 * Timeline trong 1 frame (16ms):
 * 0ms:  Message 1 → updateTicker('VNM') → re-render
 * 0.5ms: Message 2 → updateTicker('HPG') → re-render
 * 1ms:  Message 3 → updateTicker('VIC') → re-render
 * ...
 * 15ms: Message 100 → updateTicker('FPT') → re-render
 *
 * Kết quả:
 * - 100 store updates trong 16ms
 * - 100 re-renders trong 16ms
 * - Tổng thời gian: ~25ms (vượt 16ms frame budget)
 * - Frame drop → UI jank
 *
 * ✅ BATCH UPDATES:
 * Timeline:
 * 0ms:   Message 1 → push to queue, schedule timer
 * 0.5ms: Message 2 → push to queue (timer đang chạy)
 * 1ms:   Message 3 → push to queue
 * ...
 * 15ms:  Message 100 → push to queue
 * 16ms:  Timer fires → batchUpdate(100 items) → 1 re-render
 *
 * Kết quả:
 * - 1 store update
 * - 1 re-render
 * - Tổng thời gian: ~3ms (trong frame budget)
 * - Smooth 60fps
 *
 * 🚀 ƯU ĐIỂM:
 * - Giảm 99% số re-renders (100 → 1)
 * - Giảm 88% thời gian xử lý (25ms → 3ms)
 * - Always đáp ứng frame budget (smooth UI)
 * - Low CPU, low battery consumption
 */
```

---

#### **Phần 4: Error Handling & Reconnection**

**Exponential Backoff Reconnection:**

```typescript
class ResilientWebSocket {
  private ws: WebSocket | null = null;  // 🔗 Current WebSocket instance
  private url: string;  // 🌐 WebSocket server URL
  private reconnectAttempts = 0;  // 🔢 Đếm số lần reconnect (reset về 0 khi connect success)
  private maxAttempts = 5;  // 🚫 Max reconnect attempts (sau đó give up)
  private baseDelay = 1000;  // ⏰ Base delay 1 giây (tăng exponentially)
  private activeSubscriptions: string[] = [];  // 📋 Lưu symbols đang subscribe
  // 💡 activeSubscriptions để re-subscribe sau khi reconnect thành công

  constructor(url: string) {
    this.url = url;  // 🌐 Lưu URL để dùng cho reconnect
    this.connect();  // 🎆 Connect ngay khi tạo instance
  }

  connect() {
    try {
      this.ws = new WebSocket(this.url);  // 🔗 Tạo WebSocket connection mới
      // 💡 Throw error nếu URL invalid hoặc network unavailable

      this.ws.onopen = () => {
        console.log('✅🎉 Connected successfully');
        this.reconnectAttempts = 0;  // 🧹🔢 Reset counter về 0
        // 💡 QUAN TRỌNG: Reset để lần disconnect tiếp theo bắt đầu lại từ 1s delay
        // 🚀 Nếu không reset: lần reconnect sau sẽ có delay rất lớn (exponential)

        // 🔄📋 Re-subscribe to previous channels (restore state)
        this.resubscribeAll();
        // 💡 User không bị mất data sau reconnect (seamless experience)
      };

      this.ws.onmessage = this.handleMessage.bind(this);
      // 📥 Bind để giữ context của class (this)

      this.ws.onerror = (error) => {
        console.error('❌🚨 WebSocket error:', error);
        // 💡 onerror không expose chi tiết lỗi (browser security)
        // 🚀 onclose sẽ fire ngay sau với close code (check ở đó)
      };

      this.ws.onclose = (event) => {
        console.log(`🚪❌ Closed: ${event.code} - ${event.reason}`);
        // 💡 event.code: Close code (1000-4999)
        // 📝 event.reason: Optional string mô tả lý do

        if (this.shouldReconnect(event.code)) {
          // ✅🔄 Nên reconnect (network issue, server restart...)
          this.scheduleReconnect();
          // 💡 Schedule reconnect với exponential backoff
        } else {
          // 🚫 Không nên reconnect (normal close, auth failed, max attempts...)
          this.notifyUser('Connection closed. Please refresh.');
          // 📢 Thông báo user cần action (refresh page, re-login...)
        }
      };
    } catch (error) {
      // 🚨 WebSocket constructor throw error (invalid URL, blocked by CSP...)
      console.error('❌ Failed to create WebSocket:', error);
      this.scheduleReconnect();  // 🔄 Thử reconnect
    }
  }

  private shouldReconnect(code: number): boolean {
    // 🧠 Logic quyết định có nên reconnect hay không

    // 🚫 Normal closure (1000) or auth errors (1008) → KHÔNG reconnect
    if (code === 1000 || code === 1008) return false;
    // 💡 1000: User logout, tab close (intentional)
    // 💡 1008: Authentication failed → cần user re-login

    // 🚫 Max attempts reached → KHÔNG reconnect nữa (give up)
    if (this.reconnectAttempts >= this.maxAttempts) {
      console.error('❌🚫 Max reconnection attempts reached');
      // 💡 Đã thử 5 lần mà vẫn fail → có vấn đề nghiêm trọng
      // 🚀 Prevent infinite reconnect loop (waste resources)
      return false;
    }

    // ✅ Các cases khác → NÊN reconnect
    // 💡 1006: Network issue (WiFi disconnect, server crash)
    // 💡 1011: Server error (temporary, có thể recover)
    // 💡 1012: Service restart (server đang restart)
    return true;
  }

  private scheduleReconnect() {
    // ⚡📊 Exponential backoff algorithm: delay = baseDelay * 2^attempts
    const delay = this.baseDelay * Math.pow(2, this.reconnectAttempts);
    // 💡 Tính toán:
    // - Attempt 0: 1000 * 2^0 = 1000ms = 1s
    // - Attempt 1: 1000 * 2^1 = 2000ms = 2s
    // - Attempt 2: 1000 * 2^2 = 4000ms = 4s
    // - Attempt 3: 1000 * 2^3 = 8000ms = 8s
    // - Attempt 4: 1000 * 2^4 = 16000ms = 16s
    // - Attempt 5: maxAttempts reached → give up

    console.log(
      `🔄⏰ Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1}/${this.maxAttempts})`
    );
    // 📢 Thông báo user về reconnect progress

    setTimeout(() => {
      // ⏳ Đợi delay rồi mới reconnect
      this.reconnectAttempts++;  // 🔢 Increment counter TRƯỚC khi connect
      // 💡 Nếu increment sau connect(): onopen reset về 0 → mất track

      this.connect();  // 🔄 Thử connect lại
      // 💡 Nếu success: onopen reset counter về 0
      // 💡 Nếu fail: onclose → scheduleReconnect lại với delay lớn hơn
    }, delay);
  }

  private resubscribeAll() {
    // 🔄📋 Re-subscribe tất cả symbols sau khi reconnect
    if (this.activeSubscriptions.length > 0) {
      // ✅ Có subscriptions cần restore

      this.ws?.send(JSON.stringify({
        type: 'subscribe',  // 🏷️ Action type
        symbols: this.activeSubscriptions  // 📋 Array symbols đang active
      }));
      // 💡 Server sẽ bắt đầu push data cho các symbols này
      // 🚀 User không bị mất data stream sau reconnect (seamless)
    }
  }

  subscribe(symbols: string[]) {
    // 📥📋 Subscribe to new symbols

    // 📦 Merge với activeSubscriptions (dùng Set để avoid duplicates)
    this.activeSubscriptions = [...new Set([...this.activeSubscriptions, ...symbols])];
    // 💡 [...new Set(array)] = deduplicate array
    // 🚀 Nếu symbol đã subscribe rồi, không thêm lần 2

    if (this.ws?.readyState === WebSocket.OPEN) {
      // ✅ Connection đang OPEN → gửi subscribe ngay
      this.ws.send(JSON.stringify({
        type: 'subscribe',
        symbols
      }));
    }
    // 💡 Nếu connection KHÔNG OPEN (CONNECTING, CLOSING, CLOSED):
    // - Không gửi message (sẽ throw error)
    // - Chỉ lưu vào activeSubscriptions
    // - resubscribeAll() sẽ gửi khi reconnect thành công
  }

  // 🗑️ Unsubscribe method (tương tự subscribe)
  unsubscribe(symbols: string[]) {
    this.activeSubscriptions = this.activeSubscriptions.filter(
      s => !symbols.includes(s)  // 🗑️ Xóa symbols khỏi active list
    );

    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({
        type: 'unsubscribe',
        symbols
      }));
    }
  }
}

/**
 * 📊 RECONNECTION TIMELINE EXAMPLE:
 *
 * Time   | Event                        | Attempt | Delay  | Action
 * -------|------------------------------|---------|--------|-------------------------
 * T0     | ✅ Initial connect success   | 0       | -      | Working normally
 * T10    | 💥 Server crash (code 1006)  | 0       | -      | Connection lost
 * T10    | 🔄 Schedule reconnect        | 0       | 1s     | setTimeout(1000ms)
 * T11    | 🔄 Reconnect attempt 1       | 0 → 1   | -      | connect() called
 * T11    | ❌ Connection refused         | 1       | -      | Server still down
 * T11    | 🔄 Schedule reconnect        | 1       | 2s     | setTimeout(2000ms)
 * T13    | 🔄 Reconnect attempt 2       | 1 → 2   | -      | connect() called
 * T13    | ❌ Connection refused         | 2       | -      | Server still down
 * T13    | 🔄 Schedule reconnect        | 2       | 4s     | setTimeout(4000ms)
 * T17    | 🔄 Reconnect attempt 3       | 2 → 3   | -      | connect() called
 * T17    | ❌ Connection refused         | 3       | -      | Server still down
 * T17    | 🔄 Schedule reconnect        | 3       | 8s     | setTimeout(8000ms)
 * T25    | 🔄 Reconnect attempt 4       | 3 → 4   | -      | connect() called
 * T25    | ❌ Connection refused         | 4       | -      | Server still down
 * T25    | 🔄 Schedule reconnect        | 4       | 16s    | setTimeout(16000ms)
 * T41    | 🔄 Reconnect attempt 5       | 4 → 5   | -      | connect() called
 * T41    | ❌ Connection refused         | 5       | -      | Server still down
 * T41    | 🚫 Max attempts reached     | 5       | -      | Give up, notify user
 *
 * Total time: 41 seconds (1 + 2 + 4 + 8 + 16 = 31s delays + 10s events)
 *
 * 💡 TẠI SAO DÙNG EXPONENTIAL BACKOFF?
 *
 * ❌🐌 LINEAR BACKOFF (1s, 1s, 1s, 1s...):
 * - 1000 clients reconnect cùng lúc mỗi giây
 * - Server restart → bị 1000 connections cùng lúc → crash lại
 * - "Thundering herd problem"
 *
 * ✅⚡ EXPONENTIAL BACKOFF (1s, 2s, 4s, 8s...):
 * - Clients reconnect ở thời điểm khác nhau (spread out)
 * - Client 1: retry @ T1, T3, T7, T15...
 * - Client 2: retry @ T1.5, T3.5, T7.5, T15.5...
 * - Server có thời gian recover (không bị overwhelm)
 * - Higher success rate
 *
 * 🚀 ƯU ĐIỂM:
 * 1️⃣ 💻 Server-friendly: Tránh thundering herd (1000 clients cùng retry)
 * 2️⃣ 📡 Network-friendly: Giảm traffic khi network unstable
 * 3️⃣ 🔋 Battery-friendly: Mobile device không retry liên tục
 * 4️⃣ ⏰ Time to recover: Server có thời gian restart properly
 * 5️⃣ 🚫 Prevent infinite loop: maxAttempts → give up nếu fail nhiều
 */
      }));
    }
  }

  private handleMessage(event: MessageEvent) {
    const data = JSON.parse(event.data);
    // Process message
  }

  close() {
    this.ws?.close(1000, 'Normal closure');
  }
}

/**
 * RECONNECTION TIMELINE:
 *
 * T0: Connection lost
 * T0 + 1s: Attempt 1 (baseDelay * 2^0)
 * T0 + 3s: Attempt 2 (baseDelay * 2^1 = 2s)
 * T0 + 7s: Attempt 3 (baseDelay * 2^2 = 4s)
 * T0 + 15s: Attempt 4 (baseDelay * 2^3 = 8s)
 * T0 + 31s: Attempt 5 (baseDelay * 2^4 = 16s) - Final
 */
```

**Connection Status UI:**

```typescript
const ConnectionStatus = () => {
  const [status, setStatus] = useState<
    'connected' | 'connecting' | 'disconnected'
  >('connecting');
  const [reconnectAttempt, setReconnectAttempt] = useState(0);

  useEffect(() => {
    const ws = getWebSocketInstance();

    const handleOpen = () => {
      setStatus('connected');
      setReconnectAttempt(0);
    };

    const handleClose = () => {
      setStatus('disconnected');
    };

    const handleReconnecting = (attempt: number) => {
      setStatus('connecting');
      setReconnectAttempt(attempt);
    };

    ws.addEventListener('open', handleOpen);
    ws.addEventListener('close', handleClose);
    ws.addEventListener('reconnecting', handleReconnecting);

    return () => {
      ws.removeEventListener('open', handleOpen);
      ws.removeEventListener('close', handleClose);
      ws.removeEventListener('reconnecting', handleReconnecting);
    };
  }, []);

  return (
    <div className={`connection-status ${status}`}>
      {status === 'connected' && (
        <span className="text-green-500">🟢 Connected</span>
      )}
      {status === 'connecting' && (
        <span className="text-yellow-500">
          🟡 Connecting...{' '}
          {reconnectAttempt > 0 && `(Attempt ${reconnectAttempt}/5)`}
        </span>
      )}
      {status === 'disconnected' && (
        <span className="text-red-500">
          🔴 Disconnected
          <button onClick={() => window.location.reload()}>Refresh</button>
        </span>
      )}
    </div>
  );
};
```

---

#### **Phần 5: Socket.IO - High-Level WebSocket Library**

**Socket.IO Features:**

```typescript
/**
 * SOCKET.IO = WebSocket + Fallback + Rooms + Auto-reconnect + Binary support
 *
 * ✅ Advantages:
 * - Auto-reconnection with exponential backoff
 * - Fallback to HTTP long-polling (IE11, corporate firewalls)
 * - Rooms & Namespaces (multi-tenancy)
 * - Acknowledgements (confirm message received)
 * - Binary support (images, files)
 * - Broadcasting
 *
 * ❌ Disadvantages:
 * - Heavier than native WebSocket (~50KB)
 * - Not compatible with standard WebSocket servers
 * - Requires Socket.IO server
 */

// Client
import { io } from 'socket.io-client';

// 🔗🌐 Tạo Socket.IO client connection
const socket = io('https://api.example.com', {
  // 💡 Socket.IO configuration options

  // 🔄⚡ Auto-reconnection (DEFAULT: true)
  reconnection: true, // ✅ Tự động reconnect khi disconnect
  reconnectionDelay: 1000, // ⏰ Delay 1s trước lần reconnect đầu
  reconnectionDelayMax: 5000, // ⏰ Max delay 5s (exponential backoff cap)
  reconnectionAttempts: 5, // 🔢 Max 5 lần reconnect (sau đó give up)
  // 💡 Delay tăng exponentially: 1s, 2s, 4s, 5s (cap), 5s...

  // ⏱️ Timeout
  timeout: 20000, // ⏰ 20s timeout cho connect handshake
  // 💡 Nếu không connect được trong 20s → trigger connect_error event

  // 🔄 Transports (fallback mechanism)
  transports: ['websocket', 'polling'],
  // 💡 Thử WebSocket trước (fast, real-time)
  // 💡 Nếu WebSocket fail (firewall, proxy block) → fallback to HTTP long-polling
  // 🚀 Chạy được mọi nơi (tương thích IE11, corporate networks)

  // 🔐 Authentication
  auth: {
    token: 'Bearer xyz123', // 🔑 JWT token gửi khi connect
    // 💡 Server-side middleware sẽ verify token trước khi accept connection
  },
});

// ✅⚡ Auto-reconnection events
socket.on('connect', () => {
  console.log('✅🎉 Connected with socket ID:', socket.id);
  // 💡 socket.id = unique ID cho connection này (generated by server)
  // 🔄 Mỗi lần reconnect → socket.id MỚI (server tạo new ID)

  // 🔄📋 Auto re-subscribe sau reconnect
  socket.emit('subscribe', { symbols: ['VNM', 'HPG'] });
  // 💡 QUAN TRỌNG: Phải re-subscribe sau mỗi reconnect!
  // 🚀 Server không giữ subscriptions khi client disconnect
});

socket.on('disconnect', (reason) => {
  console.log('🚪❌ Disconnected. Reason:', reason);
  // 💡 reason có thể là:
  // - "io server disconnect": Server chủ động disconnect (auth fail, kick user...)
  // - "io client disconnect": Client gọi socket.disconnect()
  // - "ping timeout": Server không respond heartbeat (network issue)
  // - "transport close": Connection mất (WiFi disconnect, server crash)
  // - "transport error": WebSocket/polling error

  // ✅🔄 Socket.IO sẽ TỰ ĐỘNG reconnect!
  // 💡 Không cần code reconnection logic như raw WebSocket
  // 🚀 connect event sẽ fire khi reconnect thành công
});

// ✅ Rooms - Join specific channels
socket.emit('join-room', 'market-data');

// ✅ Listen to events
socket.on('ticker-update', (data) => {
  console.log('Ticker update:', data);
});

// ✅ Acknowledgements
socket.emit('place-order', orderData, (response) => {
  if (response.success) {
    console.log('Order placed:', response.orderId);
  } else {
    console.error('Order failed:', response.error);
  }
});

// ✅ Binary support
socket.emit('upload-chart', imageBlob);

// Cleanup
socket.disconnect();
```

**Server-side (Node.js):**

```typescript
import { Server } from 'socket.io';

const io = new Server(3000, {
  cors: {
    origin: 'https://example.com',
    credentials: true,
  },
});

// Middleware - Authentication
io.use((socket, next) => {
  const token = socket.handshake.auth.token;

  if (isValidToken(token)) {
    next();
  } else {
    next(new Error('Authentication error'));
  }
});

// Connection
io.on('connection', (socket) => {
  console.log('Client connected:', socket.id);

  // Join room
  socket.on('join-room', (room) => {
    socket.join(room);
    console.log(`${socket.id} joined ${room}`);
  });

  // Subscribe to symbols
  socket.on('subscribe', (data) => {
    const { symbols } = data;

    symbols.forEach((symbol: string) => {
      socket.join(`ticker:${symbol}`);
    });

    // Broadcast to this client
    socket.emit('subscribed', { symbols });
  });

  // Broadcast ticker updates to room
  setInterval(() => {
    const tickerData = getLatestTicker('VNM');

    // Send to all clients in room
    io.to('ticker:VNM').emit('ticker-update', tickerData);
  }, 1000);

  // Disconnect
  socket.on('disconnect', () => {
    console.log('Client disconnected:', socket.id);
  });
});
```

---

#### **Phần 5.1: Socket.IO Deep Dive - Architecture & Advanced Patterns**

**🏗️ Socket.IO Architecture Internals:**

```typescript
/**
 * 🏗️ SOCKET.IO ARCHITECTURE - 3 LAYERS:
 *
 * Layer 1: ENGINE.IO (Transport Layer)
 * ├── 🔄 Connection establishment & upgrade
 * ├── ❤️ Heartbeat/ping-pong (keep-alive)
 * ├── 🔀 Transport switching (polling → WebSocket)
 * └── 📦 Packet encoding/decoding
 *
 * Layer 2: SOCKET.IO (Protocol Layer)
 * ├── 🏷️ Namespaces (logical separation)
 * ├── 🛠️ Rooms (dynamic groups)
 * ├── 📨 Events & Acknowledgements
 * └── 🔄 Middleware & Hooks
 *
 * Layer 3: APPLICATION (Your Code)
 * ├── 📡 Event handlers
 * ├── 🔐 Business logic
 * └── 💾 State management
 */

/**
 * 🔄 CONNECTION LIFECYCLE - Chi tiết từng bước:
 *
 * Phase 1: HANDSHAKE (HTTP Upgrade)
 * ┌─────────────────────────────────────────────────────────┐
 * │ Client                           Server                 │
 * ├─────────────────────────────────────────────────────────┤
 * │ 1️⃣ HTTP GET /socket.io/?EIO=4&transport=polling         │
 * │    → Request session ID                                 │
 * │                                  ← 200 OK               │
 * │                                  {sid: "abc123", ...}   │
 * │                                                          │
 * │ 2️⃣ HTTP POST /socket.io/?EIO=4&sid=abc123              │
 * │    → Send auth data (handshake.auth)                   │
 * │                                  ← 200 OK               │
 * │                                  (auth verified)        │
 * │                                                          │
 * │ 3️⃣ Upgrade to WebSocket                                 │
 * │    → GET /socket.io/?EIO=4&sid=abc123&transport=websocket│
 * │    Upgrade: websocket                                   │
 * │                                  ← 101 Switching         │
 * │                                  (WebSocket established) │
 * └─────────────────────────────────────────────────────────┘
 *
 * ⏱️ Timeline:
 * - Step 1 (polling handshake): ~50ms
 * - Step 2 (auth): ~20ms
 * - Step 3 (WebSocket upgrade): ~30ms
 * - Total: ~100ms from io() call to 'connect' event
 *
 * 💡 TẠI SAO BẮT ĐẦU VỚI POLLING?
 * - WebSocket có thể bị block bởi proxy/firewall
 * - Polling luôn work (HTTP standard)
 * - Nếu WebSocket available → upgrade ngay (fast)
 * - Nếu WebSocket blocked → tiếp tục dùng polling (compatible)
 */

// 🏷️📂 NAMESPACES - Logical separation of connections
/**
 * NAMESPACES = Separate communication channels trên cùng 1 connection
 *
 * Use cases:
 * - Multi-tenant apps (mỗi tenant 1 namespace)
 * - Feature separation (/chat, /notifications, /market-data)
 * - Version separation (/v1, /v2)
 * - Permission-based access (admin vs user namespaces)
 */

// Server-side: Create namespaces
import { Server } from 'socket.io';

const io = new Server(3000);

// 🏷️ Default namespace (tự động tạo)
const mainNamespace = io.of('/'); // Hoặc io (shorthand)
// 💡 Client connect mà không specify namespace → vào default '/'

// 🏷️ Custom namespace: /admin
const adminNamespace = io.of('/admin');
adminNamespace.use((socket, next) => {
  // 🔐 Middleware chỉ cho namespace này
  const user = socket.handshake.auth.user;
  if (user.role === 'admin') {
    next(); // ✅ Allow
  } else {
    next(new Error('❌ Admin access only')); // 🚫 Reject
  }
});

adminNamespace.on('connection', (socket) => {
  console.log('👑 Admin connected:', socket.id);

  // 📊 Admin-specific events
  socket.on('view-all-users', () => {
    // Return sensitive data (chỉ admin được xem)
    socket.emit('user-list', getAllUsers());
  });
});

// 🏷️ Custom namespace: /chat
const chatNamespace = io.of('/chat');
chatNamespace.on('connection', (socket) => {
  console.log('💬 Chat user connected:', socket.id);

  socket.on('send-message', (message) => {
    // Broadcast to all users in /chat namespace
    chatNamespace.emit('new-message', message);
  });
});

// Client-side: Connect to specific namespace
import { io } from 'socket.io-client';

// Connect to /admin namespace
const adminSocket = io('https://api.example.com/admin', {
  auth: { user: { role: 'admin', token: 'xyz' } },
});

// Connect to /chat namespace
const chatSocket = io('https://api.example.com/chat');

/**
 * 💡 NAMESPACE vs ROOMS - Khi nào dùng gì?
 *
 * ┌──────────────┬────────────────────┬────────────────────┐
 * │              │ NAMESPACES         │ ROOMS              │
 * ├──────────────┼────────────────────┼────────────────────┤
 * │ Scope        │ Global (app-level) │ Local (per socket) │
 * │ Created      │ Server code        │ Runtime (dynamic)  │
 * │ Middleware   │ ✅ Per-namespace   │ ❌ No middleware   │
 * │ Use case     │ Feature separation │ Dynamic groups     │
 * │ Example      │ /admin, /chat      │ room123, user456   │
 * └──────────────┴────────────────────┴────────────────────┘
 *
 * 🎯 NAMESPACES:
 * - Permanent, defined in code
 * - Different middleware/auth per namespace
 * - Separate event handlers
 * - Example: /admin (restricted), /public (open)
 *
 * 🎯 ROOMS:
 * - Temporary, created/destroyed at runtime
 * - Users join/leave dynamically
 * - Share same namespace
 * - Example: Chat rooms, game lobbies, user-specific rooms
 */

// 🛠️📦 ROOMS - Dynamic groups trong namespace

// Server-side: Room management
io.on('connection', (socket) => {
  // ✅ Join room
  socket.on('join-chat', (roomId) => {
    socket.join(roomId); // 📥 Add socket to room
    // 💡 1 socket có thể join NHIỀU rooms cùng lúc
    // 💡 Room tự động tạo nếu chưa tồn tại

    console.log(`✅ ${socket.id} joined room ${roomId}`);

    // 📢 Notify others in room
    socket.to(roomId).emit('user-joined', {
      userId: socket.id,
      timestamp: Date.now(),
    });
    // 💡 socket.to(room) = broadcast to room EXCEPT sender
  });

  // 🚪 Leave room
  socket.on('leave-chat', (roomId) => {
    socket.leave(roomId); // 📤 Remove socket from room

    console.log(`🚪 ${socket.id} left room ${roomId}`);

    socket.to(roomId).emit('user-left', {
      userId: socket.id,
    });
  });

  // 💬 Send message to room
  socket.on('chat-message', ({ roomId, message }) => {
    // 📡 Broadcast to ALL in room (including sender)
    io.to(roomId).emit('new-message', {
      from: socket.id,
      message,
      timestamp: Date.now(),
    });
    // 💡 io.to(room) = broadcast to ALL in room (including sender)
    // 💡 socket.to(room) = broadcast to ALL EXCEPT sender
  });

  // 🔍 Get rooms a socket is in
  console.log('Current rooms:', socket.rooms);
  // 💡 socket.rooms = Set { socket.id, 'room1', 'room2', ... }
  // 💡 socket.id luôn có trong socket.rooms (mỗi socket tự join room của chính nó)

  // 🔍 Get all sockets in a room
  const socketsInRoom = await io.in('room1').fetchSockets();
  console.log('Sockets in room1:', socketsInRoom.length);
  // 💡 fetchSockets() returns array of Socket instances

  // 🗑️ Auto-leave on disconnect
  socket.on('disconnect', () => {
    // 💡 Socket tự động leave ALL rooms khi disconnect
    // 💡 Không cần manually leave
  });
});

/**
 * 📡 BROADCASTING STRATEGIES - 7 cách broadcast messages:
 */

// 1️⃣ Broadcast to ALL clients (global)
io.emit('announcement', 'Server maintenance in 5 minutes');
// 💡 Gửi tới TẤT CẢ clients trong TẤT CẢ namespaces
// 🎯 Use case: System-wide announcements

// 2️⃣ Broadcast to ALL in namespace
io.of('/chat').emit('system-message', 'Chat service updated');
// 💡 Gửi tới TẤT CẢ clients trong namespace /chat
// 🎯 Use case: Feature-specific announcements

// 3️⃣ Broadcast to ALL EXCEPT sender
socket.broadcast.emit('user-typing', { user: socket.id });
// 💡 Gửi tới TẤT CẢ clients TRỪ socket hiện tại
// 🎯 Use case: "User X is typing..." (không gửi cho chính user đó)

// 4️⃣ Broadcast to specific room
io.to('room123').emit('room-update', data);
// 💡 Gửi tới TẤT CẢ clients trong room123 (including sender nếu trong room)
// 🎯 Use case: Chat messages, game state updates

// 5️⃣ Broadcast to room EXCEPT sender
socket.to('room123').emit('user-action', { user: socket.id });
// 💡 Gửi tới clients trong room123 TRỪ sender
// 🎯 Use case: "User X joined the chat" (không gửi cho chính user đó)

// 6️⃣ Broadcast to multiple rooms
io.to(['room1', 'room2', 'room3']).emit('multi-room-event', data);
// 💡 Gửi tới clients trong BẤT KỲ room nào trong list
// 🎯 Use case: Notify multiple chat rooms cùng lúc

// 7️⃣ Broadcast to specific socket (unicast)
io.to(socketId).emit('private-message', data);
// 💡 Gửi tới 1 socket cụ thể (socket.id làm room name)
// 🎯 Use case: Direct messages, notifications cá nhân

/**
 * 📨 ACKNOWLEDGEMENTS - Request/Response pattern
 *
 * Flow:
 * Client ──emit('event', data, callback)──> Server
 *        <──────call callback(response)────── Server
 *
 * 💡 Benefits:
 * - Biết message đã được server nhận (delivery confirmation)
 * - Nhận response/result từ server (RPC-style)
 * - Timeout handling (nếu không nhận callback)
 * - Error handling (server trả về error)
 */

// Server-side: Handle with acknowledgement
io.on('connection', (socket) => {
  socket.on('place-order', (orderData, callback) => {
    // 💡 callback = function được client truyền vào
    // 🎯 Server xử lý order và call callback với result

    try {
      // 🔄 Process order (validate, save to DB...)
      const orderId = processOrder(orderData);

      // ✅ Success - call callback with result
      callback({
        success: true,
        orderId,
        message: 'Order placed successfully',
      });
      // 💡 Client sẽ nhận response này trong callback function
    } catch (error) {
      // ❌ Error - call callback with error
      callback({
        success: false,
        error: error.message,
      });
    }
  });
});

// Client-side: Emit with acknowledgement
socket.emit(
  'place-order',
  { symbol: 'VNM', quantity: 100, price: 85000 },
  (response) => {
    // 💡 Callback được gọi khi server respond

    if (response.success) {
      console.log('✅ Order ID:', response.orderId);
      showNotification('Order placed!', 'success');
      // 🎯 Update UI, disable button...
    } else {
      console.error('❌ Order failed:', response.error);
      showNotification(response.error, 'error');
    }
  }
);

// ⏱️ Timeout handling - Nếu server không respond
const TIMEOUT = 5000; // 5 seconds
let ackReceived = false;

const timeoutId = setTimeout(() => {
  if (!ackReceived) {
    console.error('❌ Order timeout - no response from server');
    showNotification('Request timeout. Please try again.', 'error');
  }
}, TIMEOUT);

socket.emit('place-order', orderData, (response) => {
  ackReceived = true;
  clearTimeout(timeoutId); // ✅ Cancel timeout

  // Handle response...
});

/**
 * 🔐 MIDDLEWARE PATTERNS - Authentication & Authorization
 */

// Pattern 1: Global middleware (ALL namespaces)
io.use((socket, next) => {
  // 🔐 Verify JWT token
  const token = socket.handshake.auth.token;

  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    socket.data.user = decoded; // 💾 Store user data in socket
    // 💡 socket.data = custom data storage cho socket này
    // 🎯 Accessible trong tất cả event handlers

    next(); // ✅ Allow connection
  } catch (error) {
    next(new Error('Authentication failed')); // ❌ Reject
  }
});

// Pattern 2: Namespace-specific middleware
const adminNamespace = io.of('/admin');
adminNamespace.use((socket, next) => {
  // 🔐 Check admin role
  if (socket.data.user?.role === 'admin') {
    next();
  } else {
    next(new Error('Admin access required'));
  }
});

// Pattern 3: Chained middleware
io.use(loggerMiddleware);
io.use(authMiddleware);
io.use(rateLimitMiddleware);
// 💡 Execute theo thứ tự: logger → auth → rateLimit
// 💡 Nếu 1 middleware reject (next(error)) → stop chain

function loggerMiddleware(socket, next) {
  console.log('📝 Connection from:', socket.handshake.address);
  next();
}

function authMiddleware(socket, next) {
  const token = socket.handshake.auth.token;
  if (isValidToken(token)) {
    next();
  } else {
    next(new Error('Invalid token'));
  }
}

function rateLimitMiddleware(socket, next) {
  const ip = socket.handshake.address;
  if (isRateLimited(ip)) {
    next(new Error('Rate limit exceeded'));
  } else {
    next();
  }
}

// Pattern 4: Per-event middleware (khi subscribe event)
io.on('connection', (socket) => {
  // 🛡️ Protect specific events
  socket.use((packet, next) => {
    const [eventName, ...args] = packet;

    // 🔐 Check permission for event
    if (eventName === 'admin-action' && socket.data.user?.role !== 'admin') {
      next(new Error('Unauthorized')); // ❌ Block event
    } else {
      next(); // ✅ Allow event
    }
  });
});

/**
 * 📦 BINARY DATA - Efficient file/image transfer
 */

// Client: Upload image
const fileInput = document.querySelector('input[type="file"]');
fileInput.addEventListener('change', (event) => {
  const file = event.target.files[0];

  // 📤 Send as Blob (Socket.IO auto-detect binary)
  socket.emit('upload-image', file, (response) => {
    console.log('Upload result:', response);
  });
  // 💡 Socket.IO automatically encode binary as separate packet
  // 🚀 More efficient than Base64 (no 33% size overhead)
});

// Server: Receive binary
socket.on('upload-image', (blob, callback) => {
  // 💾 Save to storage (S3, local disk...)
  const filename = `upload_${Date.now()}.jpg`;
  fs.writeFileSync(`./uploads/${filename}`, blob);

  callback({ success: true, filename });
});

// Client: Download image
socket.on('image-ready', (imageBlob) => {
  // 🖼️ Display image from Blob
  const url = URL.createObjectURL(imageBlob);
  const img = document.createElement('img');
  img.src = url;
  document.body.appendChild(img);
});
```

---

#### **Phần 5.2: Socket.IO Best Practices**

**🏆 Production-Ready Patterns:**

```typescript
/**
 * 1️⃣ CONNECTION POOLING & REUSE
 *
 * ❌ BAD: Tạo connection mới mỗi component
 */
const ChatComponent = () => {
  useEffect(() => {
    const socket = io('https://api.example.com'); // ❌ New connection
    // 💥 10 components = 10 connections (waste resources)

    return () => socket.disconnect();
  }, []);
};

/**
 * ✅ GOOD: Singleton pattern - 1 connection cho toàn app
 */

// lib/socket/socket-manager.ts
class SocketManager {
  private static instance: SocketManager;
  private socket: Socket | null = null;

  private constructor() {} // 🔒 Private constructor (singleton)

  static getInstance(): SocketManager {
    if (!SocketManager.instance) {
      SocketManager.instance = new SocketManager();
    }
    return SocketManager.instance;
  }

  connect(url: string, options?: any): Socket {
    if (!this.socket) {
      this.socket = io(url, options);
      this.setupEventHandlers();
    }
    return this.socket;
  }

  getSocket(): Socket | null {
    return this.socket;
  }

  private setupEventHandlers() {
    this.socket?.on('connect', () => {
      console.log('✅ Connected:', this.socket?.id);
    });

    this.socket?.on('disconnect', (reason) => {
      console.log('🚪 Disconnected:', reason);
    });
  }

  disconnect() {
    this.socket?.disconnect();
    this.socket = null;
  }
}

export const socketManager = SocketManager.getInstance();

// Usage trong components
import { socketManager } from '@/lib/socket/socket-manager';

const ChatComponent = () => {
  useEffect(() => {
    const socket = socketManager.getSocket();

    socket?.on('chat-message', handleMessage);

    return () => {
      socket?.off('chat-message', handleMessage); // ✅ Cleanup listeners only
      // ❌ KHÔNG disconnect (shared connection)
    };
  }, []);
};

/**
 * 2️⃣ EVENT LISTENER CLEANUP - Tránh memory leaks
 */

// ❌ BAD: Không cleanup listeners
useEffect(() => {
  socket.on('ticker-update', handleUpdate);
  // 💥 Mỗi lần component re-render → thêm listener mới
  // 💥 Sau 10 re-renders → 10 duplicate listeners
}, []); // Missing cleanup!

// ✅ GOOD: Always cleanup trong useEffect return
useEffect(() => {
  const handleUpdate = (data) => {
    console.log('Update:', data);
  };

  socket.on('ticker-update', handleUpdate);

  return () => {
    socket.off('ticker-update', handleUpdate); // ✅ Remove listener
    // 💡 socket.off(event, handler) removes specific handler
    // 💡 socket.off(event) removes ALL handlers for event
  };
}, []);

// ✅ BETTER: useSocketEvent hook (reusable)
function useSocketEvent<T>(event: string, handler: (data: T) => void) {
  const socketManager = useSocketManager();

  useEffect(() => {
    const socket = socketManager.getSocket();
    if (!socket) return;

    socket.on(event, handler);

    return () => {
      socket.off(event, handler);
    };
  }, [event, handler]);
}

// Usage
const ChatComponent = () => {
  const handleMessage = useCallback((message: ChatMessage) => {
    console.log('New message:', message);
  }, []);

  useSocketEvent('chat-message', handleMessage); // ✅ Auto cleanup
};

/**
 * 3️⃣ ERROR HANDLING - Graceful degradation
 */

// ✅ COMPREHENSIVE error handling
const socket = io('https://api.example.com', {
  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 1000,
});

// 🚨 Connection errors
socket.on('connect_error', (error) => {
  console.error('❌ Connection error:', error.message);

  // 🎯 User-friendly error messages
  if (error.message === 'Authentication failed') {
    showNotification('Login expired. Please refresh.', 'error');
    redirectToLogin();
  } else if (error.message.includes('timeout')) {
    showNotification('Connection timeout. Retrying...', 'warning');
  } else {
    showNotification('Connection failed. Please check your internet.', 'error');
  }
});

// 🚨 Event-level errors
socket.on('error', (error) => {
  console.error('❌ Socket error:', error);
  // 💡 Generic errors (network issues, protocol errors...)
});

// 🚨 Acknowledgement timeout
function emitWithTimeout<T>(
  event: string,
  data: any,
  timeout: number = 5000
): Promise<T> {
  return new Promise((resolve, reject) => {
    let ackReceived = false;

    // ⏱️ Setup timeout
    const timer = setTimeout(() => {
      if (!ackReceived) {
        reject(new Error(`Timeout waiting for ${event} acknowledgement`));
      }
    }, timeout);

    // 📤 Emit with callback
    socket.emit(event, data, (response: T) => {
      ackReceived = true;
      clearTimeout(timer);
      resolve(response);
    });
  });
}

// Usage với try-catch
try {
  const result = await emitWithTimeout('place-order', orderData, 5000);
  console.log('✅ Order placed:', result);
} catch (error) {
  console.error('❌ Order failed:', error);
  showNotification('Order timeout. Please try again.', 'error');
}

/**
 * 4️⃣ RECONNECTION STATE MANAGEMENT
 */

interface SocketState {
  connected: boolean;
  reconnecting: boolean;
  reconnectAttempt: number;
}

const useSocketState = () => {
  const [state, setState] = useState<SocketState>({
    connected: false,
    reconnecting: false,
    reconnectAttempt: 0,
  });

  useEffect(() => {
    const socket = socketManager.getSocket();
    if (!socket) return;

    const handleConnect = () => {
      setState({ connected: true, reconnecting: false, reconnectAttempt: 0 });
    };

    const handleDisconnect = () => {
      setState((prev) => ({ ...prev, connected: false }));
    };

    const handleReconnectAttempt = (attempt: number) => {
      setState({
        connected: false,
        reconnecting: true,
        reconnectAttempt: attempt,
      });
    };

    socket.on('connect', handleConnect);
    socket.on('disconnect', handleDisconnect);
    socket.io.on('reconnect_attempt', handleReconnectAttempt);

    return () => {
      socket.off('connect', handleConnect);
      socket.off('disconnect', handleDisconnect);
      socket.io.off('reconnect_attempt', handleReconnectAttempt);
    };
  }, []);

  return state;
};

// UI Component
const ConnectionStatus = () => {
  const { connected, reconnecting, reconnectAttempt } = useSocketState();

  if (connected) {
    return <Badge color="green">🟢 Connected</Badge>;
  }

  if (reconnecting) {
    return (
      <Badge color="yellow">
        🟡 Reconnecting... (Attempt {reconnectAttempt}/5)
      </Badge>
    );
  }

  return (
    <Badge color="red">
      🔴 Disconnected
      <button onClick={() => window.location.reload()}>Refresh</button>
    </Badge>
  );
};

/**
 * 5️⃣ SECURITY BEST PRACTICES
 */

// ✅ 1. Always use HTTPS/WSS in production
const socket = io('https://api.example.com', {
  // ✅ https (not http)
  // 💡 Browser sẽ upgrade to wss:// automatically
  // 🔐 Encrypted connection (TLS/SSL)
});

// ✅ 2. Validate & sanitize ALL inputs
socket.on('chat-message', (message) => {
  // 🛡️ Sanitize HTML (prevent XSS)
  const sanitized = DOMPurify.sanitize(message.text);

  // 🛡️ Validate structure
  if (!message.userId || !message.timestamp) {
    console.error('Invalid message format');
    return;
  }

  displayMessage(sanitized);
});

// ✅ 3. Rate limiting (server-side)
io.use((socket, next) => {
  const ip = socket.handshake.address;

  if (rateLimiter.isLimited(ip)) {
    next(new Error('Rate limit exceeded. Try again later.'));
  } else {
    next();
  }
});

// ✅ 4. Token expiration & refresh
const socket = io('https://api.example.com', {
  auth: async (callback) => {
    // 🔄 Fetch fresh token every connect/reconnect
    const token = await getAuthToken();
    callback({ token });
  },
});

// ✅ 5. Validate permissions (server-side)
socket.on('admin-action', (data) => {
  // 🔐 Check user role
  if (socket.data.user?.role !== 'admin') {
    socket.emit('error', { message: 'Unauthorized' });
    return;
  }

  // Process admin action...
});

/**
 * 6️⃣ PERFORMANCE OPTIMIZATION
 */

// ✅ 1. Use binary encoding for large data
socket.emit(
  'large-dataset',
  {
    _placeholder: true,
    num: 0, // Reference to binary attachment
  },
  largeArrayBuffer
); // Send as binary
// 💡 Socket.IO auto-detect binary và encode separately
// 🚀 Faster than JSON (~40% smaller)

// ✅ 2. Batch multiple events
const eventQueue: any[] = [];
let flushTimer: NodeJS.Timeout | null = null;

function queueEvent(event: string, data: any) {
  eventQueue.push({ event, data });

  if (!flushTimer) {
    flushTimer = setTimeout(() => {
      // 📦 Send all events in 1 batch
      socket.emit('batch', eventQueue);
      eventQueue.length = 0;
      flushTimer = null;
    }, 16); // 60fps
  }
}

// ✅ 3. Compress messages (server config)
const io = new Server(3000, {
  perMessageDeflate: {
    // ✅ Enable compression
    threshold: 1024, // Only compress messages > 1KB
  },
});
// 💡 Reduce bandwidth ~60% for text messages
// ⚠️ CPU overhead (trade-off)

// ✅ 4. Selective broadcasting (avoid broadcast storms)
io.on('connection', (socket) => {
  socket.on('user-typing', ({ roomId }) => {
    // ✅ Throttle typing indicators
    throttle(() => {
      socket.to(roomId).emit('user-typing', { userId: socket.id });
    }, 1000); // Max 1 typing event per second
  });
});

/**
 * 7️⃣ TESTING STRATEGIES
 */

// Unit test với mock socket
import { createMockSocket } from 'socket.io-client-mock';

describe('Chat Component', () => {
  it('should handle incoming messages', () => {
    const mockSocket = createMockSocket();
    render(<ChatComponent socket={mockSocket} />);

    // 📨 Simulate incoming message
    mockSocket.emit('chat-message', {
      userId: 'user1',
      text: 'Hello!',
    });

    // ✅ Assert message displayed
    expect(screen.getByText('Hello!')).toBeInTheDocument();
  });
});

// Integration test với real Socket.IO server
import { createServer } from 'http';
import { Server } from 'socket.io';
import { io as clientIO } from 'socket.io-client';

describe('Socket.IO Integration', () => {
  let ioServer: Server;
  let httpServer: any;

  beforeAll((done) => {
    httpServer = createServer();
    ioServer = new Server(httpServer);
    httpServer.listen(3001, done);
  });

  afterAll(() => {
    ioServer.close();
    httpServer.close();
  });

  it('should connect and receive messages', (done) => {
    const client = clientIO('http://localhost:3001');

    client.on('connect', () => {
      // ✅ Connected
      client.emit('test-event', { data: 'test' });
    });

    client.on('response', (data) => {
      expect(data).toBe('received');
      client.disconnect();
      done();
    });
  });
});

/**
 * 8️⃣ MONITORING & DEBUGGING
 */

// ✅ 1. Enable debug logs (development)
const socket = io('https://api.example.com', {
  debug: true, // ✅ Log all events to console
});

// ✅ 2. Custom logger
socket.onAny((event, ...args) => {
  console.log('📨 Event:', event, args);

  // 📊 Send to analytics
  analytics.track('socket_event', {
    event,
    timestamp: Date.now(),
  });
});

// ✅ 3. Performance monitoring
const startTime = Date.now();

socket.emit('api-call', data, (response) => {
  const latency = Date.now() - startTime;

  console.log(`⏱️ API call latency: ${latency}ms`);

  // 📊 Track latency metrics
  if (latency > 1000) {
    console.warn('⚠️ Slow response detected');
  }
});

// ✅ 4. Error tracking (Sentry integration)
socket.on('error', (error) => {
  Sentry.captureException(error, {
    tags: {
      socketId: socket.id,
      transport: socket.io.engine.transport.name,
    },
  });
});

/**
 * 📋 CHECKLIST - Production deployment:
 *
 * ✅ Security:
 *    - [ ] Use HTTPS/WSS only
 *    - [ ] Implement authentication middleware
 *    - [ ] Validate all inputs
 *    - [ ] Rate limiting enabled
 *    - [ ] Token expiration handled
 *
 * ✅ Performance:
 *    - [ ] Connection pooling (singleton)
 *    - [ ] Event listener cleanup
 *    - [ ] Batch updates where possible
 *    - [ ] Enable compression (perMessageDeflate)
 *    - [ ] Use binary for large data
 *
 * ✅ Reliability:
 *    - [ ] Auto-reconnection configured
 *    - [ ] Acknowledgement timeouts
 *    - [ ] Error handling comprehensive
 *    - [ ] Graceful degradation
 *    - [ ] Fallback to polling works
 *
 * ✅ Monitoring:
 *    - [ ] Logging enabled (production: error only)
 *    - [ ] Performance metrics tracked
 *    - [ ] Error reporting (Sentry/etc)
 *    - [ ] Connection state visible to users
 *
 * ✅ Testing:
 *    - [ ] Unit tests for components
 *    - [ ] Integration tests for flows
 *    - [ ] Load testing (artillery/k6)
 *    - [ ] Failover testing (kill server)
 */
```

---

#### **Phần 6: Centrifuge - Enterprise Real-time Messaging**

**Centrifuge Features:**

```typescript
/**
 * 🏆 CENTRIFUGE = Enterprise-grade real-time messaging platform
 *
 * ✅ ADVANTAGES (vượt trội so với Socket.IO):
 *
 * 1️⃣ 🚀📊 HORIZONTAL SCALING:
 *    - Socket.IO: 1 server handle tất (single point of failure)
 *    - Socket.IO + Redis: Broadcast qua Redis pub/sub (basic scaling)
 *    - Centrifuge: Built-in Redis/KeyDB/Nats (advanced scaling)
 *    - 💡 Centrifugo server instances share state qua Redis
 *    - 🚀 1 million+ connections across một cluster (enterprise-ready)
 *
 * 2️⃣ 🔐🏷️ TOKEN-BASED AUTH với EXPIRATION:
 *    - Socket.IO: Auth 1 lần khi connect (token không expire)
 *    - Centrifuge: Token có expiration, auto-refresh trước khi expire
 *    - 💡 Security: Nếu token leak, chỉ dùng được trong vài phút
 *    - 🚀 getToken() callback fetch new token khi cần
 *
 * 3️⃣ 👥✅ PRESENCE TRACKING:
 *    - Track online users trong channel real-time
 *    - Biết user nào đang xem chart, typing...
 *    - 💡 Use case: Chat (show "3 users online"), collaborative editing
 *
 * 4️⃣ 📦📋 MESSAGE HISTORY:
 *    - Lưu 100-1000 messages gần nhất (configurable TTL)
 *    - User mới join → replay history → không bị mất data
 *    - 💡 Use case: User refresh page → lấy lại 100 price updates cuối
 *    - 🚀 Không cần query database cho recent data
 *
 * 5️⃣ 🔐🔑 CHANNEL PERMISSIONS:
 *    - Private channels: Chỉ users có permission mới subscribe được
 *    - Token chứa channel permissions (JWT claims)
 *    - Server verify permissions trước khi accept subscribe
 *    - 💡 Use case: Premium users xem real-time data, free users không
 *
 * 6️⃣ 📦 BINARY SUPPORT:
 *    - Protobuf encoding (nhanh hơn JSON ~5x)
 *    - MessagePack encoding
 *    - 🚀 High-frequency data (1000+ msgs/s) nên dùng binary
 *
 * 7️⃣ 🛠️ MULTIPLE SDKs:
 *    - JavaScript, Go, Python, Java, Swift, Dart...
 *    - Mobile apps (iOS, Android) + Web + Backend cùng protocol
 *    - 🚀 Consistent API across platforms
 *
 * ❌ DISADVANTAGES:
 *
 * 1️⃣ 🔧 COMPLEX SETUP:
 *    - Cần chạy Centrifugo server (separate service)
 *    - Cần Redis/KeyDB/Nats cho scaling (thêm infrastructure)
 *    - Config file (centrifugo.json) với namespaces, permissions...
 *    - 💡 Socket.IO: Chỉ cần install npm package, chạy trong Node.js app
 *
 * 2️⃣ 📚 LEARNING CURVE:
 *    - Concepts: channels, namespaces, presence, history, tokens...
 *    - Token generation (JWT với claims)
 *    - Centrifugo server operations (deploy, monitor, scale)
 *
 * 3️⃣ 🚀 OVERKILL cho SMALL APPS:
 *    - Nếu chỉ cần simple real-time (1000 users) → Socket.IO đủ
 *    - Nếu không cần presence, history → raw WebSocket đủ
 *
 * 🎯 USE CASES (Khi NÀO dùng Centrifuge?):
 *
 * ✅ TRADING PLATFORMS:
 *    - 100,000+ concurrent users
 *    - High throughput (1000+ msgs/s per user)
 *    - Horizontal scaling across data centers
 *    - Message history (user refresh → replay)
 *
 * ✅ CHAT APPLICATIONS:
 *    - Presence tracking (online users)
 *    - Message history (scroll up để xem old messages)
 *    - Private channels (1-1 chat, group permissions)
 *
 * ✅ LIVE DASHBOARDS:
 *    - Millions of connections (IoT devices, monitoring)
 *    - Horizontal scaling (multiple Centrifugo instances)
 *    - Channel-based routing (device123 → channel "device:123")
 *
 * ✅ MULTIPLAYER GAMES:
 *    - Presence (players in room)
 *    - History (game state replay)
 *    - Low latency (WebSocket persistent connection)
 */

import Centrifuge from 'centrifuge';

// 🔗🌐 Tạo Centrifuge client connection
const centrifuge = new Centrifuge('ws://localhost:8000/connection/websocket', {
  // 🔐🔑 Token-based auth với auto-refresh
  getToken: async () => {
    // 📥 Fetch new token từ backend
    const response = await fetch('/api/centrifuge-token');
    const { token } = await response.json();
    // 🔑 Token structure (JWT):
    // {
    //   "sub": "user123",  // User ID
    //   "exp": 1234567890,  // Expiration timestamp
    //   "channels": ["market:*"]  // Allowed channels (permissions)
    // }
    return token;
    // 💡 Centrifuge tự động call getToken() khi:
    // - Lần đầu connect
    // - Token sắp expire (trước 30s)
    // - Reconnect sau disconnect
    // 🚀 Auto token refresh (không cần code manually)
  },

  // 🛠️ Debug mode (log events to console)
  debug: true, // ✅ Bật debug trong development, tắt trong production
});

// 🔗 Connect to Centrifugo server
centrifuge.connect();
// 💡 Async connection (không block), sẽ fire 'connect' event khi thành công

// 📥📋 Subscribe to channel (channel = topic/room)
const subscription = centrifuge.subscribe('market:stocks', {
  // 💡 Channel naming convention: "namespace:resource"
  // 🚀 "market:stocks" = namespace "market", resource "stocks"

  // 📥📊 On publish - Nhận message mới
  publish: (ctx) => {
    console.log('📥🔔 New message:', ctx.data);
    // 💡 ctx.data = message payload (object, array, string...)
    // 💡 ctx.offset = message sequence number (dùng cho history)

    updateTickerData(ctx.data); // 🔄 Update UI với data mới
    // 🚀 Real-time: Server publish → all subscribers nhận instantly
  },

  // ✅🎉 On subscribe success
  subscribe: (ctx) => {
    console.log('✅🎆 Subscribed to channel successfully');
    // 💡 ctx.positioned = true nếu server track message sequence (history enabled)
    // 💡 ctx.recoverable = true nếu có thể recover missed messages

    // 👥🔍 Get presence (danh sách online users trong channel)
    subscription.presence().then((result) => {
      console.log('👥📋 Online users:', result.clients);
      // 💡 result.clients = array of client objects:
      // [
      //   { client: "abc123", user: "user1", info: { name: "John" } },
      //   { client: "def456", user: "user2", info: { name: "Jane" } }
      // ]
      // 🚀 Hiển thị "15 users watching this chart"
    });

    // 📦📋 Get history (last N messages)
    subscription.history({ limit: 100 }).then((result) => {
      console.log('📦📊 Message history:', result.publications);
      // 💡 result.publications = array of past messages (newest first):
      // [
      //   { offset: 1005, data: { symbol: "VNM", price: 85000 } },
      //   { offset: 1004, data: { symbol: "HPG", price: 45000 } },
      //   ...
      // ]
      // 🚀 User mới vào/refresh → replay 100 price updates cuối
      // 💡 Không cần query REST API cho initial data
    });
  },

  // 🚪❌ On unsubscribe
  unsubscribe: (ctx) => {
    console.log('🚪 Unsubscribed from channel');
    // 💡 ctx.code = unsubscribe reason code
    // 💡 ctx.reason = reason string
  },
});

// 📤📊 Publish to channel (client → server → all subscribers)
await subscription.publish({
  symbol: 'VNM', // 📊 Stock symbol
  price: 85000, // 💰 Current price
  change: 2.5, // 📈 % change
});
// 💡 Nếu channel config "publish: true" → client có thể publish
// 💡 Nếu "publish: false" (default) → chỉ server có thể publish (secure)
// 🚀 Use case: Chat app (users gửi messages), collaborative editing

// 👥🔔 Presence tracking - Theo dõi users join/leave
subscription.on('presence', (ctx) => {
  console.log('🎆 User event:', ctx);
  // 💡 ctx.type = "join" hoặc "leave"
  // 💡 ctx.client = client ID
  // 💡 ctx.user = user ID
  // 💡 ctx.info = custom user info (name, avatar...)

  if (ctx.type === 'join') {
    console.log(`✅👋 ${ctx.info.name} joined the channel`);
    // 🚀 Hiển thị notification "John joined"
  } else {
    console.log(`🚪👋 ${ctx.info.name} left the channel`);
    // 🚀 Hiển thị "Jane left"
  }
});

// 🧹🗑️ Cleanup khi component unmount
subscription.unsubscribe(); // 🚫 Unsubscribe khỏi channel
centrifuge.disconnect(); // 🚪 Close connection
// 💡 Nếu không cleanup: memory leak + server vẫn giữ connection

/**
 * 🚀 HORIZONTAL SCALING VỚI REDIS:
 *
 * Architecture:
 *
 *   Client 1 ───────────────┐
 *   Client 2 ───────────────┤
 *                                  │
 *                          Centrifugo Server 1
 *                                  │
 *                                  │
 *                          Redis Pub/Sub  ←── Shared message bus
 *                                  │
 *                                  │
 *                          Centrifugo Server 2
 *                                  │
 *   Client 3 ───────────────┤
 *   Client 4 ───────────────┘
 *
 * Flow:
 * 1️⃣ Client 1 subscribe "market:stocks" và connect tới Server 1
 * 2️⃣ Client 3 subscribe "market:stocks" và connect tới Server 2
 * 3️⃣ Backend publish message tới Server 1 API
 * 4️⃣ Server 1 broadcast message qua Redis pub/sub
 * 5️⃣ Redis forward message tới Server 2
 * 6️⃣ Server 2 push message tới Client 3 qua WebSocket
 *
 * 💡 KẾT QUẢ:
 * - Client 1 (Server 1) và Client 3 (Server 2) đều nhận message
 * - Clients không biết có nhiều servers (transparent)
 * - Load balanced: 50% clients → Server 1, 50% → Server 2
 * - High availability: Nếu Server 1 down, Client 1 reconnect tới Server 2
 *
 * 🚀 SCALABILITY:
 * - 1 server: 10,000 connections
 * - 10 servers: 100,000 connections
 * - 100 servers: 1,000,000 connections
 * - Redis có thể handle millions msgs/s (bottleneck không phải Centrifugo)
 */
```

**Server-side (Centrifugo):**

```json
// centrifugo.json
{
  "v3_use_offset": true,
  "token_hmac_secret_key": "secret-key",
  "api_key": "api-key",
  "admin_password": "admin-password",
  "admin_secret": "admin-secret",
  "namespaces": [
    {
      "name": "market",
      "publish": true,
      "presence": true,
      "history_size": 100,
      "history_ttl": "60s"
    }
  ]
}
```

---

#### **Phần 6.1: Centrifugo Best Practices & Deep Dive**

**🎯 Advanced Centrifugo Patterns:**

```typescript
/**
 * 🏗️ KIẾN TRÚC PATTERN 1: QUẢN LÝ KẾT NỐI TẬP TRUNG
 *
 * ❌ VẤN ĐỀ:
 * - Nhiều components subscribe các channels khác nhau
 * - Mỗi component tạo 1 Centrifuge instance riêng
 * - Kết quả: Có 10 components → 10 connections → lãng phí tài nguyên!
 *
 * ✅ GIẢI PHÁP:
 * - Singleton Pattern: Chỉ có DUY NHẤT 1 instance CentrifugeManager trong toàn app
 * - Manager này quản lý 1 connection duy nhất đến Centrifugo server
 * - Tất cả components dùng chung connection này
 * - Tiết kiệm tài nguyên, dễ quản lý, tránh duplicate subscriptions
 */

// lib/centrifuge/CentrifugeManager.ts
import Centrifuge, {
  Subscription, // Đại diện cho 1 subscription đến 1 channel
  PublicationContext, // Context của message nhận được (data, offset, tags...)
  SubscriptionState, // Trạng thái subscription (subscribed, subscribing, unsubscribed...)
} from 'centrifuge';

// 📋 Interface định nghĩa các callback functions khi subscribe channel
interface SubscriptionOptions {
  onPublish?: (ctx: PublicationContext) => void; // Callback khi nhận message mới
  onSubscribe?: () => void; // Callback khi subscribe thành công
  onUnsubscribe?: () => void; // Callback khi unsubscribe
  onError?: (error: Error) => void; // Callback khi có lỗi
}

class CentrifugeManager {
  // 🔒 SINGLETON PATTERN: Chỉ 1 instance duy nhất
  private static instance: CentrifugeManager;

  // 🌐 Connection đến Centrifugo server (chỉ 1 connection cho toàn app)
  private centrifuge: Centrifuge | null = null;

  // 📋 Map lưu tất cả subscriptions đang active (key = channel name)
  private subscriptions: Map<string, Subscription> = new Map();

  // 🔢 Reference counting: Đếm số components đang subscribe mỗi channel
  // VD: {"market:VNM": 3} = có 3 components đang subscribe channel này
  private refCount: Map<string, number> = new Map();

  // 🔄 Đếm số lần reconnect (để giới hạn không reconnect vô hạn)
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 10; // Tối đa 10 lần reconnect

  // 🔒 Constructor là PRIVATE → không ai gọi new CentrifugeManager() được từ bên ngoài
  private constructor() {}

  /**
   * 🎯 LẤY INSTANCE DUY NHẤT (Singleton Pattern)
   *
   * Cách dùng: const manager = CentrifugeManager.getInstance();
   * Lần 1 gọi: Tạo instance mới
   * Lần 2-N gọi: Trả về instance đã tạo (không tạo mới)
   *
   * ➡️ KẾT QUẢ: Dù gọi 100 lần ở 100 nơi khác nhau, vẫn chỉ có 1 instance!
   */
  static getInstance(): CentrifugeManager {
    if (!CentrifugeManager.instance) {
      CentrifugeManager.instance = new CentrifugeManager();
    }
    return CentrifugeManager.instance;
  }

  /**
   * 🔗 KHỞI TẠO KẾT NỐI đến Centrifugo server
   *
   * @param url - WebSocket URL của Centrifugo server (ws:// hoặc wss://)
   * @param options - Tùy chọn nâng cao (getToken, callbacks...)
   *
   * 💡 GỌI 1 LẦN DUY NHẤT khi app khởi động (thường ở App.tsx hoặc main.tsx)
   */
  init(
    url: string,
    options?: {
      getToken?: () => Promise<string>; // Function lấy JWT token từ backend
      onConnected?: () => void; // Callback khi kết nối thành công
      onDisconnected?: () => void; // Callback khi mất kết nối
    }
  ) {
    // ⚠️ Nếu đã init rồi thì không init lại (tránh duplicate connections)
    if (this.centrifuge) {
      console.warn('⚠️ Centrifuge đã được khởi tạo rồi, không init lại');
      return this.centrifuge;
    }

    // 🚀 TẠO CENTRIFUGE CLIENT với config nâng cao
    this.centrifuge = new Centrifuge(url, {
      // 🔐 CHIẾN LƯỢC LẤY TOKEN (tự động refresh khi token sắp hết hạn)
      // Centrifugo sẽ gọi function này khi:
      // 1. Lần đầu kết nối
      // 2. Token sắp hết hạn (trước 30 giây)
      // 3. Reconnect sau khi mất kết nối
      getToken: async () => {
        try {
          // Gọi function getToken từ options (do app truyền vào)
          // HOẶC gọi hàm fetchTokenFromBackend mặc định
          const token = options?.getToken
            ? await options.getToken()
            : await this.fetchTokenFromBackend();

          console.log('🔑 Lấy token thành công');
          this.reconnectAttempts = 0; // Reset số lần reconnect về 0
          return token;
        } catch (error) {
          console.error('❌ Lấy token thất bại:', error);
          throw error; // Throw error → Centrifugo sẽ retry
        }
      },

      // 🔄 CẤU HÌNH RECONNECTION (tự động kết nối lại khi mất kết nối)
      minReconnectDelay: 1000, // Lần đầu mất kết nối → chờ 1 giây rồi reconnect
      maxReconnectDelay: 30000, // Tối đa chờ 30 giây giữa các lần reconnect
      // ➡️ Exponential backoff: 1s → 2s → 4s → 8s → 16s → 30s (max)

      // 📊 CẤU HÌNH PROTOCOL (cách encode/decode messages)
      protocol: 'protobuf', // ✅ Dùng binary Protobuf (nhanh hơn JSON ~5x, nhỏ hơn ~40%)
      // Nếu không config: mặc định dùng JSON (chậm hơn nhưng dễ debug)

      // 🐛 CHẾ ĐỘ DEBUG (log tất cả events ra console)
      debug: process.env.NODE_ENV === 'development', // Chỉ bật debug khi dev, tắt ở production
    });

    // 📡 Global event handlers
    this.setupEventHandlers(options);

    // 🚀 Connect
    this.centrifuge.connect();

    return this.centrifuge;
  }

  /**
   * 📡 Setup global event listeners
   */
  private setupEventHandlers(options?: any) {
    if (!this.centrifuge) return;

    // ✅ Connected
    this.centrifuge.on('connected', (ctx) => {
      console.log('✅ Centrifuge connected:', {
        client: ctx.client,
        transport: ctx.transport,
        version: ctx.version,
      });

      this.reconnectAttempts = 0;
      options?.onConnected?.();

      // 📊 Track connection metrics
      this.trackMetric('connection_established', {
        transport: ctx.transport,
        latency: ctx.latency,
      });
    });

    // 🔌 Disconnected
    this.centrifuge.on('disconnected', (ctx) => {
      console.warn('🔌 Centrifuge disconnected:', {
        code: ctx.code,
        reason: ctx.reason,
        reconnect: ctx.reconnect,
      });

      options?.onDisconnected?.();

      // 📊 Track disconnection
      this.trackMetric('connection_lost', {
        code: ctx.code,
        reason: ctx.reason,
      });
    });

    // 🔄 Connecting (reconnection attempts)
    this.centrifuge.on('connecting', (ctx) => {
      this.reconnectAttempts++;

      console.log(
        `🔄 Reconnecting... (attempt ${this.reconnectAttempts}/${this.maxReconnectAttempts})`
      );

      // 🚨 Too many failed attempts → force refresh
      if (this.reconnectAttempts >= this.maxReconnectAttempts) {
        console.error(
          '❌ Max reconnect attempts reached. Please refresh page.'
        );
        this.showReconnectError();
      }
    });

    // 🚨 Error events
    this.centrifuge.on('error', (ctx) => {
      console.error('❌ Centrifuge error:', ctx.error);

      // 📊 Track errors
      this.trackMetric('connection_error', {
        error: ctx.error.message,
        type: ctx.type,
      });
    });
  }

  /**
   * 📥 SUBSCRIBE VÀO CHANNEL với REFERENCE COUNTING
   *
   * ❌ VẤN ĐỀ NẾU KHÔNG DÙNG REFERENCE COUNTING:
   *
   * Tình huống:
   * - Component A subscribe "market:VNM" → Tạo subscription mới
   * - Component B cũng subscribe "market:VNM" → Tạo subscription mới NỮA? ❌ Duplicate!
   * - Component A unmount → unsubscribe → Component B mất data? ❌ Bug!
   *
   * ✅ GIẢI PHÁP: REFERENCE COUNTING (Đếm số components đang dùng)
   *
   * Flow:
   * 1️⃣ Component A mount:
   *    - refCount["market:VNM"] = 0 → 1
   *    - Tạo subscription MỚI (vì là subscriber đầu tiên)
   *
   * 2️⃣ Component B mount:
   *    - refCount["market:VNM"] = 1 → 2
   *    - DÙNG LẠI subscription có sẵn (không tạo mới)
   *
   * 3️⃣ Component A unmount:
   *    - refCount["market:VNM"] = 2 → 1
   *    - GIỮ NGUYÊN subscription (vì còn B đang dùng)
   *
   * 4️⃣ Component B unmount:
   *    - refCount["market:VNM"] = 1 → 0
   *    - XÓA subscription (vì không còn ai dùng)
   *
   * ➡️ KẾT QUẢ: Không bao giờ có duplicate subscriptions!
   *
   * @param channel - Tên channel muốn subscribe (VD: "market:VNM")
   * @param options - Callbacks (onPublish, onSubscribe, onError...)
   * @returns Function để cleanup (gọi khi component unmount)
   */
  subscribe(channel: string, options: SubscriptionOptions): () => void {
    // 📈 TĂNG SỐ ĐẾM: Thêm 1 component đang dùng channel này
    const currentCount = this.refCount.get(channel) || 0; // Lấy số hiện tại (hoặc 0 nếu chưa có)
    this.refCount.set(channel, currentCount + 1); // Tăng lên 1

    console.log(
      `📥 Subscribe vào ${channel} (số components đang dùng: ${
        currentCount + 1
      })`
    );

    // 🔍 KIỂM TRA: Subscription này đã tồn tại chưa?
    let subscription = this.subscriptions.get(channel);

    if (!subscription) {
      // 🆕 TRƯỜNG HỢP 1: Chưa có subscription → Tạo mới
      // (Đây là component ĐẦU TIÊN subscribe channel này)
      console.log(`🆕 Tạo subscription mới cho ${channel}`);
      subscription = this.createSubscription(channel, options);
      this.subscriptions.set(channel, subscription); // Lưu vào Map
    } else {
      // ♻️ TRƯỜNG HỢP 2: Đã có subscription → Dùng lại
      // (Đã có component khác subscribe rồi, chỉ cần attach thêm listener)
      console.log(`♻️ Dùng lại subscription có sẵn cho ${channel}`);

      // 🔗 Gắn thêm listener của component này vào subscription
      // (Khi có message mới, TẤT CẢ components đều nhận được)
      if (options.onPublish) {
        subscription.on('publication', options.onPublish);
      }
    }

    // 🧹 TRẢ VỀ CLEANUP FUNCTION
    // Component gọi function này trong useEffect cleanup:
    // useEffect(() => {
    //   const cleanup = manager.subscribe(...);
    //   return cleanup;  // ← Gọi khi component unmount
    // }, []);
    return () => {
      this.unsubscribe(channel, options.onPublish);
    };
  }

  /**
   * 🆕 Create new subscription
   */
  private createSubscription(
    channel: string,
    options: SubscriptionOptions
  ): Subscription {
    if (!this.centrifuge) {
      throw new Error('Centrifuge not initialized');
    }

    const subscription = this.centrifuge.newSubscription(channel, {
      // 📥 Publication handler
      ...(options.onPublish && {
        getToken: async () => {
          // 🔐 Channel-specific token (nếu channel là private)
          return await this.fetchChannelToken(channel);
        },
      }),
    });

    // 📡 Event handlers
    subscription.on('publication', (ctx) => {
      console.log(`📨 [${channel}] New message:`, ctx.data);
      options.onPublish?.(ctx);
    });

    subscription.on('subscribed', (ctx) => {
      console.log(`✅ [${channel}] Subscribed successfully`, {
        recovered: ctx.recovered,
        positioned: ctx.positioned,
        recoverable: ctx.recoverable,
      });

      options.onSubscribe?.();

      // 📊 Fetch history nếu available
      if (ctx.recoverable) {
        this.fetchHistory(channel, subscription);
      }
    });

    subscription.on('unsubscribed', (ctx) => {
      console.log(`🚪 [${channel}] Unsubscribed`, {
        code: ctx.code,
        reason: ctx.reason,
      });

      options.onUnsubscribe?.();
    });

    subscription.on('error', (ctx) => {
      console.error(`❌ [${channel}] Subscription error:`, ctx.error);
      options.onError?.(ctx.error);
    });

    // 🚀 Subscribe immediately
    subscription.subscribe();

    return subscription;
  }

  /**
   * 🧹 UNSUBSCRIBE KHỎI CHANNEL (với reference counting)
   *
   * Flow:
   * - Giảm refCount xuống 1
   * - Nếu refCount = 0 (không còn ai dùng) → Xóa subscription thật
   * - Nếu refCount > 0 (còn components khác dùng) → Chỉ remove listener của component này
   *
   * @param channel - Channel cần unsubscribe
   * @param handler - Function handler của component (để remove listener)
   */
  private unsubscribe(channel: string, handler?: Function) {
    const currentCount = this.refCount.get(channel) || 0;

    // ⚠️ KIỂM TRA BẤT THƯỜNG: Gọi unsubscribe mà không có subscriber?
    if (currentCount <= 0) {
      console.warn(
        `⚠️ Lỗi: Gọi unsubscribe nhưng ${channel} không có subscriber nào!`
      );
      return; // Bỏ qua, không làm gì
    }

    // 📉 GIẢM SỐ ĐẾM: Bớt 1 component đang dùng
    const newCount = currentCount - 1;
    this.refCount.set(channel, newCount);

    console.log(
      `🔽 Unsubscribe khỏi ${channel} (còn ${newCount} components đang dùng)`
    );

    const subscription = this.subscriptions.get(channel);

    if (newCount === 0) {
      // 🗑️ TRƯỜNG HỢP 1: Đây là component CUỐI CÙNG → Xóa subscription thật
      console.log(
        `🗑️ Không còn ai dùng ${channel} → Xóa subscription khỏi server`
      );

      subscription?.unsubscribe();
      subscription?.removeAllListeners();
      this.subscriptions.delete(channel);
      this.refCount.delete(channel);
    } else if (handler && subscription) {
      // 🔗 Remove specific handler (still have other subscribers)
      subscription.off('publication', handler);
    }
  }

  /**
   * 📦 Fetch message history
   */
  private async fetchHistory(channel: string, subscription: Subscription) {
    try {
      const result = await subscription.history({
        limit: 100,
        reverse: true, // Oldest → newest
      });

      console.log(`📦 [${channel}] History fetched:`, {
        count: result.publications.length,
        offset: result.offset,
      });

      // 🔄 Process historical messages
      result.publications.forEach((pub) => {
        // Emit as publication event để components nhận
        subscription.emit('publication', {
          data: pub.data,
          offset: pub.offset,
          tags: pub.tags,
        } as PublicationContext);
      });
    } catch (error) {
      console.error(`❌ Failed to fetch history for ${channel}:`, error);
    }
  }

  /**
   * 📤 Publish to channel
   */
  async publish(channel: string, data: any): Promise<void> {
    const subscription = this.subscriptions.get(channel);

    if (!subscription) {
      throw new Error(`Not subscribed to channel: ${channel}`);
    }

    try {
      const result = await subscription.publish(data);
      console.log(`📤 Published to ${channel}:`, result);
    } catch (error) {
      console.error(`❌ Publish failed for ${channel}:`, error);
      throw error;
    }
  }

  /**
   * 👥 Get presence info
   */
  async getPresence(channel: string): Promise<any> {
    const subscription = this.subscriptions.get(channel);

    if (!subscription) {
      throw new Error(`Not subscribed to channel: ${channel}`);
    }

    try {
      const result = await subscription.presence();
      console.log(`👥 [${channel}] Presence:`, result.clients);
      return result;
    } catch (error) {
      console.error(`❌ Presence fetch failed for ${channel}:`, error);
      throw error;
    }
  }

  /**
   * 🔑 Fetch token from backend
   */
  private async fetchTokenFromBackend(): Promise<string> {
    const response = await fetch('/api/centrifuge/token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('authToken')}`,
      },
    });

    if (!response.ok) {
      throw new Error(`Token fetch failed: ${response.status}`);
    }

    const { token } = await response.json();
    return token;
  }

  /**
   * 🔐 Fetch channel-specific token (private channels)
   */
  private async fetchChannelToken(channel: string): Promise<string> {
    const response = await fetch('/api/centrifuge/channel-token', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${localStorage.getItem('authToken')}`,
      },
      body: JSON.stringify({ channel }),
    });

    if (!response.ok) {
      throw new Error(`Channel token fetch failed: ${response.status}`);
    }

    const { token } = await response.json();
    return token;
  }

  /**
   * 📊 Track metrics (integrate with analytics)
   */
  private trackMetric(event: string, data: any) {
    // Integration với analytics service
    if (window.analytics) {
      window.analytics.track(event, {
        ...data,
        timestamp: Date.now(),
      });
    }
  }

  /**
   * 🚨 Show reconnect error to user
   */
  private showReconnectError() {
    // Show toast/modal to user
    if (window.showNotification) {
      window.showNotification({
        type: 'error',
        title: 'Connection Lost',
        message: 'Unable to reconnect. Please refresh the page.',
        action: {
          label: 'Refresh',
          onClick: () => window.location.reload(),
        },
      });
    }
  }

  /**
   * 🧹 Cleanup all subscriptions
   */
  destroy() {
    console.log('🧹 Destroying CentrifugeManager');

    // Unsubscribe all channels
    this.subscriptions.forEach((subscription, channel) => {
      console.log(`🗑️ Unsubscribing from ${channel}`);
      subscription.unsubscribe();
      subscription.removeAllListeners();
    });

    this.subscriptions.clear();
    this.refCount.clear();

    // Disconnect
    this.centrifuge?.disconnect();
    this.centrifuge = null;
  }

  /**
   * 📊 Get connection stats
   */
  getStats() {
    return {
      connected: this.centrifuge?.state === 'connected',
      subscriptions: this.subscriptions.size,
      channels: Array.from(this.subscriptions.keys()),
      refCounts: Object.fromEntries(this.refCount),
      reconnectAttempts: this.reconnectAttempts,
    };
  }
}

export const centrifugeManager = CentrifugeManager.getInstance();

/**
 * 🎣 REACT HOOK: useCentrifugeSubscription
 */

import { useEffect, useCallback, useState } from 'react';
import { PublicationContext } from 'centrifuge';

interface UseCentrifugeOptions<T> {
  channel: string;
  onMessage?: (data: T) => void;
  enabled?: boolean; // Conditional subscription
}

export function useCentrifugeSubscription<T = any>({
  channel,
  onMessage,
  enabled = true,
}: UseCentrifugeOptions<T>) {
  const [data, setData] = useState<T | null>(null);
  const [error, setError] = useState<Error | null>(null);
  const [subscribed, setSubscribed] = useState(false);

  // 📥 Stable callback reference
  const handleMessage = useCallback(
    (ctx: PublicationContext) => {
      const messageData = ctx.data as T;
      setData(messageData);
      onMessage?.(messageData);
    },
    [onMessage]
  );

  useEffect(() => {
    if (!enabled) {
      console.log(`⏸️ Subscription to ${channel} disabled`);
      return;
    }

    console.log(`🎣 Hook: Subscribing to ${channel}`);

    // ✅ Subscribe
    const unsubscribe = centrifugeManager.subscribe(channel, {
      onPublish: handleMessage,
      onSubscribe: () => setSubscribed(true),
      onUnsubscribe: () => setSubscribed(false),
      onError: (err) => setError(err),
    });

    // 🧹 Cleanup
    return () => {
      console.log(`🧹 Hook: Cleaning up ${channel}`);
      unsubscribe();
    };
  }, [channel, enabled, handleMessage]);

  // 📤 Publish helper
  const publish = useCallback(
    async (data: any) => {
      try {
        await centrifugeManager.publish(channel, data);
      } catch (err) {
        setError(err as Error);
        throw err;
      }
    },
    [channel]
  );

  // 👥 Presence helper
  const getPresence = useCallback(async () => {
    try {
      return await centrifugeManager.getPresence(channel);
    } catch (err) {
      setError(err as Error);
      throw err;
    }
  }, [channel]);

  return {
    data,
    error,
    subscribed,
    publish,
    getPresence,
  };
}

/**
 * 💡 USAGE EXAMPLES
 */

// Example 1: Simple subscription
const TickerComponent = ({ symbol }: { symbol: string }) => {
  const { data, subscribed } = useCentrifugeSubscription<TickerData>({
    channel: `market:${symbol}`,
    onMessage: (ticker) => {
      console.log('New ticker:', ticker);
    },
  });

  if (!subscribed) {
    return <div>Connecting...</div>;
  }

  return (
    <div>
      <h3>{symbol}</h3>
      <p>Price: {data?.price}</p>
      <p>Change: {data?.change}%</p>
    </div>
  );
};

// Example 2: Conditional subscription (chỉ subscribe khi user active)
const OptimizedTickerComponent = ({ symbol }: { symbol: string }) => {
  const [isVisible, setIsVisible] = useState(true);

  // 🎯 Only subscribe when component is visible
  const { data } = useCentrifugeSubscription({
    channel: `market:${symbol}`,
    enabled: isVisible, // ✅ Stop subscription when hidden
  });

  useEffect(() => {
    const handleVisibility = () => {
      setIsVisible(!document.hidden);
    };

    document.addEventListener('visibilitychange', handleVisibility);
    return () =>
      document.removeEventListener('visibilitychange', handleVisibility);
  }, []);

  return <div>Price: {data?.price}</div>;
};

// Example 3: Multiple subscriptions
const MultiSymbolWatchlist = ({ symbols }: { symbols: string[] }) => {
  return (
    <div>
      {symbols.map((symbol) => (
        <TickerComponent key={symbol} symbol={symbol} />
      ))}
    </div>
  );
  // ✅ Each component subscribes independently
  // ✅ CentrifugeManager handles ref counting automatically
  // ✅ No duplicate subscriptions!
};

// Example 4: Publish with acknowledgement
const ChatInput = ({ channel }: { channel: string }) => {
  const { publish, error } = useCentrifugeSubscription({ channel });
  const [message, setMessage] = useState('');

  const handleSend = async () => {
    try {
      await publish({ text: message, timestamp: Date.now() });
      setMessage(''); // ✅ Clear input
    } catch (err) {
      alert('Failed to send message');
    }
  };

  return (
    <div>
      <input value={message} onChange={(e) => setMessage(e.target.value)} />
      <button onClick={handleSend}>Send</button>
      {error && <p>Error: {error.message}</p>}
    </div>
  );
};

// Example 5: Presence tracking
const OnlineUsers = ({ channel }: { channel: string }) => {
  const { getPresence } = useCentrifugeSubscription({ channel });
  const [users, setUsers] = useState<any[]>([]);

  useEffect(() => {
    const fetchPresence = async () => {
      const presence = await getPresence();
      setUsers(presence.clients);
    };

    fetchPresence();

    // 🔄 Refresh every 30s
    const interval = setInterval(fetchPresence, 30000);
    return () => clearInterval(interval);
  }, [getPresence]);

  return (
    <div>
      <h4>👥 Online ({users.length})</h4>
      <ul>
        {users.map((user) => (
          <li key={user.client}>
            {user.user} - {user.info?.name}
          </li>
        ))}
      </ul>
    </div>
  );
};
```

---

**🔐 Advanced: Private Channels & Permissions:**

```typescript
/**
 * 🔐 PATTERN 2: PRIVATE CHANNELS với GRANULAR PERMISSIONS
 *
 * Scenario: Trading platform
 * - Free users: Xem delayed data (15 phút delay)
 * - Premium users: Xem real-time data
 * - VIP users: Xem real-time + level 2 order book
 *
 * Solution: Channel permissions trong JWT token
 */

// Backend: Generate token với channel permissions
import jwt from 'jsonwebtoken';

interface UserProfile {
  id: string;
  email: string;
  tier: 'free' | 'premium' | 'vip';
}

function generateCentrifugoToken(user: UserProfile): string {
  const now = Math.floor(Date.now() / 1000);

  // 🔑 Build channel permissions based on user tier
  const channels: string[] = [];

  switch (user.tier) {
    case 'free':
      // ✅ Free: Delayed data only
      channels.push('market:delayed:*');
      break;

    case 'premium':
      // ✅ Premium: Real-time price data
      channels.push('market:delayed:*');
      channels.push('market:realtime:*');
      break;

    case 'vip':
      // ✅ VIP: Everything
      channels.push('market:delayed:*');
      channels.push('market:realtime:*');
      channels.push('market:orderbook:*');
      channels.push('market:private:*');
      break;
  }

  const payload = {
    sub: user.id, // Subject (user ID)
    exp: now + 3600, // Expire in 1 hour
    iat: now, // Issued at

    // 🎯 Centrifugo-specific claims
    channels, // Allowed channels

    // 📊 Custom user info (visible in presence)
    info: {
      email: user.email,
      tier: user.tier,
      name: user.email.split('@')[0], // Display name
    },
  };

  return jwt.sign(payload, process.env.CENTRIFUGO_SECRET!, {
    algorithm: 'HS256',
  });
}

// API endpoint: POST /api/centrifuge/token
app.post('/api/centrifuge/token', authenticateUser, (req, res) => {
  const user = req.user as UserProfile;

  const token = generateCentrifugoToken(user);

  res.json({
    token,
    expiresIn: 3600, // Client biết token expire sau 1h
  });
});

/**
 * 🔒 CHANNEL-SPECIFIC TOKENS (Subscribe token)
 *
 * Problem: User có general token nhưng muốn subscribe private channel
 * - General token: Chứa wildcard permissions (market:realtime:*)
 * - Private channel: Cần specific permission (portfolio:user123)
 *
 * Solution: Channel-specific token khi subscribe
 */

// Backend: Generate subscribe token for specific channel
app.post('/api/centrifuge/channel-token', authenticateUser, (req, res) => {
  const user = req.user as UserProfile;
  const { channel } = req.body;

  // 🔐 Verify user has permission for this channel
  if (channel.startsWith('portfolio:')) {
    const userId = channel.split(':')[1];

    if (userId !== user.id) {
      return res.status(403).json({ error: 'Unauthorized' });
    }
  }

  // 🔑 Generate channel-specific token
  const now = Math.floor(Date.now() / 1000);
  const payload = {
    client: req.body.client, // Client ID from Centrifuge
    channel, // Specific channel
    exp: now + 3600,
    iat: now,
  };

  const token = jwt.sign(payload, process.env.CENTRIFUGO_SECRET!, {
    algorithm: 'HS256',
  });

  res.json({ token });
});

/**
 * Frontend: Subscribe to private channel
 */

const PortfolioComponent = ({ userId }: { userId: string }) => {
  const channel = `portfolio:${userId}`;

  // 🔒 Hook tự động fetch channel token khi subscribe
  const { data, error } = useCentrifugeSubscription<PortfolioData>({
    channel,
    onMessage: (portfolio) => {
      console.log('Portfolio updated:', portfolio);
    },
  });

  if (error) {
    return <div>❌ Access denied: {error.message}</div>;
  }

  return (
    <div>
      <h3>Your Portfolio</h3>
      <p>Total value: ${data?.totalValue}</p>
      <p>P&L: {data?.profitLoss}%</p>
    </div>
  );
};

/**
 * 🎯 Centrifugo server config với namespaces
 */

// centrifugo.json
const centrifugoConfig = {
  v3_use_offset: true,
  token_hmac_secret_key: process.env.CENTRIFUGO_SECRET,
  api_key: process.env.CENTRIFUGO_API_KEY,

  namespaces: [
    // 📊 Public delayed data - No auth required
    {
      name: 'market:delayed',
      publish: false, // ❌ Clients cannot publish
      subscribe_for_client: true, // ✅ Free access
      presence: false,
      history_size: 100,
      history_ttl: '300s', // 5 min TTL
    },

    // 🚀 Real-time data - Premium+ only
    {
      name: 'market:realtime',
      publish: false,
      subscribe_for_client: false, // 🔒 Require token permission
      presence: true, // ✅ Show who's watching
      history_size: 1000,
      history_ttl: '60s',
      force_recovery: true, // ✅ Auto-recovery on reconnect
    },

    // 📖 Order book - VIP only
    {
      name: 'market:orderbook',
      publish: false,
      subscribe_for_client: false, // 🔒 VIP only
      presence: false,
      history_size: 500,
      history_ttl: '30s',
    },

    // 🔐 Private portfolio - User-specific
    {
      name: 'portfolio',
      publish: false,
      subscribe_for_client: false, // 🔒 Require channel-specific token
      presence: false,
      history_size: 50,
      history_ttl: '120s',
    },
  ],
};
```

---

**⚡ Performance Optimization:**

```typescript
/**
 * 🚀 PATTERN 3: BATCHING & THROTTLING
 *
 * Problem: High-frequency updates (1000 msg/s) → UI lag
 * Solution: Batch updates và throttle renders
 */

interface TickerUpdate {
  symbol: string;
  price: number;
  volume: number;
  timestamp: number;
}

class TickerBatchProcessor {
  private batch: Map<string, TickerUpdate> = new Map();
  private flushTimer: NodeJS.Timeout | null = null;
  private onFlush: (updates: TickerUpdate[]) => void;

  constructor(onFlush: (updates: TickerUpdate[]) => void) {
    this.onFlush = onFlush;
  }

  /**
   * 📥 Add update to batch
   */
  addUpdate(update: TickerUpdate) {
    // 📝 Overwrite previous update for same symbol (keep latest)
    this.batch.set(update.symbol, update);

    // ⏱️ Schedule flush (debounced)
    if (this.flushTimer) {
      clearTimeout(this.flushTimer);
    }

    this.flushTimer = setTimeout(() => {
      this.flush();
    }, 16); // 60 FPS (~16ms)
  }

  /**
   * 🚀 Flush batch to UI
   */
  private flush() {
    if (this.batch.size === 0) return;

    const updates = Array.from(this.batch.values());

    console.log(`🚀 Flushing ${updates.length} updates`);

    // 🔄 Update UI với batched data
    this.onFlush(updates);

    // 🧹 Clear batch
    this.batch.clear();
    this.flushTimer = null;
  }

  /**
   * 🧹 Cleanup
   */
  destroy() {
    if (this.flushTimer) {
      clearTimeout(this.flushTimer);
    }
    this.batch.clear();
  }
}

/**
 * React Component với batching
 */

const HighFrequencyTickerList = ({ symbols }: { symbols: string[] }) => {
  const [tickers, setTickers] = useState<Map<string, TickerUpdate>>(new Map());

  // 📦 Batch processor
  const batchProcessor = useRef<TickerBatchProcessor | null>(null);

  useEffect(() => {
    // 🆕 Create batch processor
    batchProcessor.current = new TickerBatchProcessor((updates) => {
      // 🔄 Update state với batched data
      setTickers((prev) => {
        const next = new Map(prev);
        updates.forEach((update) => {
          next.set(update.symbol, update);
        });
        return next;
      });
    });

    // 🧹 Cleanup
    return () => {
      batchProcessor.current?.destroy();
    };
  }, []);

  // 📥 Subscribe to all symbols
  useCentrifugeSubscription({
    channel: 'market:realtime:*',
    onMessage: (update: TickerUpdate) => {
      // 📦 Add to batch (không update UI immediately)
      batchProcessor.current?.addUpdate(update);
    },
  });

  return (
    <div>
      <h3>Live Tickers ({tickers.size})</h3>

      {/* 🎯 Virtual scrolling cho large lists */}
      <FixedSizeList
        height={600}
        itemCount={tickers.size}
        itemSize={50}
        width="100%"
      >
        {({ index, style }) => {
          const ticker = Array.from(tickers.values())[index];
          return (
            <div style={style}>
              {ticker.symbol}: ${ticker.price}
            </div>
          );
        }}
      </FixedSizeList>
    </div>
  );
};

/**
 * 🎯 PATTERN 4: SELECTIVE SUBSCRIPTIONS
 *
 * Problem: User xem watchlist 100 symbols nhưng chỉ quan tâm top 10 visible
 * Solution: Subscribe chỉ visible symbols, lazy-load others
 */

const VirtualizedWatchlist = ({ symbols }: { symbols: string[] }) => {
  const [visibleRange, setVisibleRange] = useState({ start: 0, end: 10 });

  // 📥 Subscribe chỉ visible symbols
  const visibleSymbols = symbols.slice(visibleRange.start, visibleRange.end);

  return (
    <div>
      {visibleSymbols.map((symbol) => (
        <TickerRow key={symbol} symbol={symbol} />
      ))}

      {/* 🔄 Update visible range on scroll */}
      <IntersectionObserver onChange={(range) => setVisibleRange(range)} />
    </div>
  );
};

const TickerRow = ({ symbol }: { symbol: string }) => {
  // ✅ Each row subscribes independently
  const { data } = useCentrifugeSubscription({
    channel: `market:realtime:${symbol}`,
  });

  return (
    <div>
      {symbol}: {data?.price}
    </div>
  );
  // 🚀 When row scrolls out → useEffect cleanup → unsubscribe
  // 🚀 When row scrolls in → subscribe again
};
```

---

**📊 Monitoring & Debugging:**

```typescript
/**
 * 🔍 PATTERN 5: COMPREHENSIVE MONITORING
 */

class CentrifugeMonitor {
  private metrics: {
    messagesReceived: number;
    messagesSent: number;
    bytesReceived: number;
    bytesSent: number;
    reconnections: number;
    errors: number;
    latency: number[];
  } = {
    messagesReceived: 0,
    messagesSent: 0,
    bytesReceived: 0,
    bytesSent: 0,
    reconnections: 0,
    errors: 0,
    latency: [],
  };

  private startTime = Date.now();

  /**
   * 📊 Track message received
   */
  trackMessageReceived(size: number) {
    this.metrics.messagesReceived++;
    this.metrics.bytesReceived += size;
  }

  /**
   * 📤 Track message sent
   */
  trackMessageSent(size: number) {
    this.metrics.messagesSent++;
    this.metrics.bytesSent += size;
  }

  /**
   * ⏱️ Track latency (RTT)
   */
  trackLatency(latency: number) {
    this.metrics.latency.push(latency);

    // Keep only last 100 samples
    if (this.metrics.latency.length > 100) {
      this.metrics.latency.shift();
    }
  }

  /**
   * 📊 Get statistics
   */
  getStats() {
    const uptime = Date.now() - this.startTime;
    const avgLatency =
      this.metrics.latency.length > 0
        ? this.metrics.latency.reduce((a, b) => a + b, 0) /
          this.metrics.latency.length
        : 0;

    return {
      uptime: Math.floor(uptime / 1000), // seconds
      messagesReceived: this.metrics.messagesReceived,
      messagesSent: this.metrics.messagesSent,
      bytesReceived: this.formatBytes(this.metrics.bytesReceived),
      bytesSent: this.formatBytes(this.metrics.bytesSent),
      reconnections: this.metrics.reconnections,
      errors: this.metrics.errors,
      avgLatency: Math.round(avgLatency),
      messagesPerSecond: Math.round(
        this.metrics.messagesReceived / (uptime / 1000)
      ),
    };
  }

  private formatBytes(bytes: number): string {
    if (bytes < 1024) return bytes + ' B';
    if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(2) + ' KB';
    return (bytes / (1024 * 1024)).toFixed(2) + ' MB';
  }

  /**
   * 🐛 Debug panel component
   */
  renderDebugPanel() {
    const stats = this.getStats();

    return (
      <div
        style={{
          position: 'fixed',
          bottom: 0,
          right: 0,
          background: 'rgba(0,0,0,0.8)',
          color: 'white',
          padding: '10px',
          fontSize: '12px',
          fontFamily: 'monospace',
          zIndex: 9999,
        }}
      >
        <div>🔌 Centrifuge Monitor</div>
        <div>⏱️ Uptime: {stats.uptime}s</div>
        <div>
          📥 Messages RX: {stats.messagesReceived} ({stats.messagesPerSecond}/s)
        </div>
        <div>📤 Messages TX: {stats.messagesSent}</div>
        <div>💾 Data RX: {stats.bytesReceived}</div>
        <div>💾 Data TX: {stats.bytesSent}</div>
        <div>🔄 Reconnections: {stats.reconnections}</div>
        <div>❌ Errors: {stats.errors}</div>
        <div>⚡ Latency: {stats.avgLatency}ms</div>
      </div>
    );
  }
}

// Usage
const monitor = new CentrifugeMonitor();

// Attach to CentrifugeManager
centrifugeManager.on('message', (data) => {
  monitor.trackMessageReceived(JSON.stringify(data).length);
});

// React component
const DebugPanel = () => {
  const [stats, setStats] = useState(monitor.getStats());

  useEffect(() => {
    const interval = setInterval(() => {
      setStats(monitor.getStats());
    }, 1000);

    return () => clearInterval(interval);
  }, []);

  return monitor.renderDebugPanel();
};
```

---

**🚀 Production Deployment Checklist:**

```typescript
/**
 * ✅ PRODUCTION CHECKLIST
 *
 * 1️⃣ SECURITY:
 *    ✅ Use HTTPS/WSS only (no HTTP in production)
 *    ✅ Token expiration configured (max 1 hour)
 *    ✅ Token refresh implemented (auto-refresh before expire)
 *    ✅ Channel permissions validated on server
 *    ✅ Rate limiting enabled (per IP, per user)
 *    ✅ Input validation & sanitization
 *
 * 2️⃣ PERFORMANCE:
 *    ✅ Binary protocol enabled (Protobuf)
 *    ✅ Message batching implemented
 *    ✅ UI throttling (60 FPS max)
 *    ✅ Virtual scrolling for large lists
 *    ✅ Lazy subscription (subscribe only visible)
 *    ✅ Reference counting (no duplicate subs)
 *
 * 3️⃣ RELIABILITY:
 *    ✅ Auto-reconnection configured (exponential backoff)
 *    ✅ Max reconnect attempts (10)
 *    ✅ Message history enabled (replay on reconnect)
 *    ✅ Offline detection (show UI indicator)
 *    ✅ Graceful degradation (fallback to polling?)
 *
 * 4️⃣ MONITORING:
 *    ✅ Connection metrics tracked (uptime, reconnections)
 *    ✅ Message throughput monitored (msg/s)
 *    ✅ Latency tracked (avg, p95, p99)
 *    ✅ Error logging (Sentry integration)
 *    ✅ Analytics integration (connection events)
 *
 * 5️⃣ SCALING:
 *    ✅ Redis configured (cluster mode)
 *    ✅ Multiple Centrifugo instances (load balanced)
 *    ✅ Health checks configured (/health endpoint)
 *    ✅ Auto-scaling rules (CPU > 70% → add instance)
 *
 * 6️⃣ TESTING:
 *    ✅ Unit tests (components, hooks)
 *    ✅ Integration tests (full flow)
 *    ✅ Load testing (artillery, k6)
 *    ✅ Failover testing (kill instances)
 *    ✅ Token expiration testing
 */

// Load testing với k6
import { check } from 'k6';
import ws from 'k6/ws';

export const options = {
  stages: [
    { duration: '30s', target: 100 }, // Ramp up to 100 users
    { duration: '1m', target: 1000 }, // Ramp up to 1000
    { duration: '2m', target: 1000 }, // Stay at 1000
    { duration: '30s', target: 0 }, // Ramp down
  ],
};

export default function () {
  const url = 'wss://api.example.com/connection/websocket';
  const token = 'xxx'; // Fetch from auth endpoint

  const res = ws.connect(
    url,
    { headers: { Authorization: `Bearer ${token}` } },
    (socket) => {
      socket.on('open', () => {
        console.log('Connected');

        // Subscribe to channel
        socket.send(
          JSON.stringify({
            method: 1, // Subscribe
            params: {
              channel: 'market:realtime:VNM',
            },
          })
        );
      });

      socket.on('message', (data) => {
        check(data, {
          'message received': (d) => d.length > 0,
        });
      });

      socket.on('error', (e) => {
        console.error('Error:', e);
      });

      socket.setTimeout(() => {
        socket.close();
      }, 60000); // Close after 1 min
    }
  );

  check(res, { 'status is 101': (r) => r && r.status === 101 });
}
```

---

#### **Phần 7: So Sánh WebSocket vs Socket.IO vs Centrifuge**

```typescript
/**
 * ┌────────────────┬────────────────┬────────────────┬────────────────┐
 * │                │  WEBSOCKET     │  SOCKET.IO     │  CENTRIFUGE    │
 * ├────────────────┼────────────────┼────────────────┼────────────────┤
 * │ Complexity     │ ⭐ Low         │ ⭐⭐ Medium    │ ⭐⭐⭐ High     │
 * │ Size           │ Native         │ ~50KB          │ ~20KB          │
 * │ Auto-reconnect │ ❌ Manual      │ ✅ Built-in    │ ✅ Built-in    │
 * │ Fallback       │ ❌ No          │ ✅ Long-poll   │ ✅ SSE         │
 * │ Rooms          │ ❌ Manual      │ ✅ Built-in    │ ✅ Channels    │
 * │ Scaling        │ ❌ Single      │ ⚠️ Redis       │ ✅ Redis/Nats  │
 * │ Binary         │ ✅ Yes         │ ✅ Yes         │ ✅ Yes         │
 * │ Presence       │ ❌ Manual      │ ⚠️ Custom      │ ✅ Built-in    │
 * │ History        │ ❌ Manual      │ ❌ No          │ ✅ Built-in    │
 * │ Auth           │ ❌ Manual      │ ⚠️ Custom      │ ✅ JWT Token   │
 * │ Server         │ Any WS server  │ Socket.IO srv  │ Centrifugo     │
 * │ Use Case       │ Simple apps    │ Medium apps    │ Enterprise     │
 * └────────────────┴────────────────┴────────────────┴────────────────┘
 *
 * 🎯 DECISION TREE:
 *
 * Simple app, basic real-time (chat, notifications)
 *   → Native WebSocket
 *
 * Need auto-reconnect, rooms, fallback (IE11 support)
 *   → Socket.IO
 *
 * Enterprise, millions of connections, horizontal scaling
 *   → Centrifuge
 *
 * Trading platform, high throughput, low latency
 *   → Centrifuge (with Redis/KeyDB)
 */
```

---

#### **Phần 8: Best Practices**

```typescript
/**
 * ✅ DO:
 */

// 1. Always cleanup WebSocket on unmount
useEffect(() => {
  const ws = new WebSocket(url);

  return () => {
    ws.close(1000, 'Component unmounted');
  };
}, []);

// 2. Use reference counting for subscriptions
const subscribe = (symbol: string) => {
  refCount[symbol] = (refCount[symbol] || 0) + 1;

  if (refCount[symbol] === 1) {
    ws.send(JSON.stringify({ type: 'subscribe', symbol }));
  }
};

// 3. Throttle UI updates với requestAnimationFrame
const latestData = useRef({});
const updateUI = () => {
  setData(latestData.current);
  rafId = requestAnimationFrame(updateUI);
};

// 4. Handle reconnection với exponential backoff
const delay = baseDelay * Math.pow(2, attempts);

// 5. Show connection status to users
<ConnectionStatus status={wsStatus} />;

// 6. Batch updates
let batch = [];
const flushBatch = () => {
  updateStore(batch);
  batch = [];
};
setTimeout(flushBatch, 16); // 60fps

// 7. Use virtual scrolling for large lists
<AgGridReact rowData={data} />; // Auto virtual scrolling

/**
 * ❌ DON'T:
 */

// 1. Don't create multiple WebSocket connections for same data
// Use reference counting!

// 2. Don't update UI on every message
// Throttle với RAF!

// 3. Don't forget to unsubscribe
// Memory leak!

// 4. Don't render all items in large lists
// Use virtual scrolling!

// 5. Don't ignore close codes
// Check if should reconnect!

// 6. Don't use == for subscription checking
// Use Set or Map!
```

---
