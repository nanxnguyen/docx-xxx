# 🔌 Q57: WebSocket & Real-time Streaming - WebSocket, Socket.IO, Centrifuge

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🔌 Q57: WebSocket & Real-time Streaming - WebSocket, Socket.IO, Centrifuge</span></summary>


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
// ❌ REST API Polling - KHÔNG hiệu quả
setInterval(() => {
  fetch('/api/market-data')
    .then(res => res.json())
    .then(data => updateUI(data));
}, 1000); // Call API mỗi giây!

/**
 * VẤN ĐỀ:
 * - Tốn băng thông: Mỗi request = headers + body
 * - Latency cao: HTTP handshake mỗi lần
 * - Server load cao: 1000 clients = 1000 requests/giây
 * - Không real-time: Delay tối thiểu 1 giây
 * - Waste resources: Poll ngay cả khi không có data mới
 */

// ✅ WebSocket - Real-time hiệu quả
const ws = new WebSocket('wss://market-data.example.com');

ws.onopen = () => {
  console.log('✅ Connected');
  // Subscribe to channels
  ws.send(JSON.stringify({ 
    type: 'subscribe', 
    symbols: ['VNM', 'HPG', 'VIC'] 
  }));
};

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateUI(data); // ⚡ Update ngay khi có data mới
};

/**
 * ƯU ĐIỂM:
 * ✅ Persistent connection: Kết nối 1 lần, dùng mãi
 * ✅ Push data ngay lập tức: Latency < 10ms
 * ✅ Tiết kiệm băng thông: Không có HTTP headers lặp lại
 * ✅ Server load thấp: Chỉ push khi có data mới
 * ✅ True real-time: Không có polling delay
 */
```

**WebSocket Lifecycle:**

```typescript
// 1. CONNECTING (readyState = 0)
const ws = new WebSocket('wss://api.example.com/stream');
console.log('State:', ws.readyState); // 0 - CONNECTING

// 2. OPEN (readyState = 1)
ws.onopen = () => {
  console.log('State:', ws.readyState); // 1 - OPEN
  console.log('✅ Connected, có thể gửi message');
  
  // Send subscribe message
  ws.send(JSON.stringify({ 
    type: 'subscribe', 
    symbols: ['BTCUSDT', 'ETHUSDT'] 
  }));
};

// 3. MESSAGE - Nhận data từ server
ws.onmessage = (event: MessageEvent) => {
  const data = JSON.parse(event.data);
  console.log('📥 Received:', data);
  
  // Update UI
  updateTickerPrice(data.symbol, data.price);
};

// 4. ERROR - Xử lý lỗi
ws.onerror = (error) => {
  console.error('❌ WebSocket error:', error);
  showNotification('Connection error. Retrying...');
};

// 5. CLOSE (readyState = 3)
ws.onclose = (event: CloseEvent) => {
  console.log('State:', ws.readyState); // 3 - CLOSED
  console.log('Code:', event.code);
  console.log('Reason:', event.reason);
  
  /**
   * CLOSE CODES:
   * 1000: Normal closure
   * 1001: Going away (page refresh)
   * 1006: Abnormal closure (no close frame)
   * 1008: Policy violation (auth error)
   * 1011: Server error
   */
  
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
```

---

#### **Phần 2: Production WebSocket Architecture**

**Pattern 1: Reference Counting Subscription Manager**

```typescript
/**
 * PROBLEM: Multiple components subscribe to same symbol
 * 
 * Component A: Subscribe VNM
 * Component B: Subscribe VNM
 * Component C: Subscribe HPG
 * 
 * ❌ BAD: 3 WebSocket connections (waste resources)
 * ✅ GOOD: 1 connection, reference counting
 */

interface SubscriptionTracker {
  subscriptions: Map<string, {
    count: number;
    subscribers: Set<string>;
  }>;
}

class LiveDataManager {
  private ws: WebSocket | null = null;
  private tracker = new Map<string, { count: number; subscribers: Set<string> }>();

  subscribe(symbols: string[], componentId: string) {
    symbols.forEach(symbol => {
      const current = this.tracker.get(symbol);

      if (!current) {
        // 🔥 First subscriber → Send subscribe message
        this.tracker.set(symbol, {
          count: 1,
          subscribers: new Set([componentId])
        });
        
        this.ws?.send(JSON.stringify({
          type: 'subscribe',
          symbol
        }));
      } else {
        // ⚡ Already subscribed → Just increment counter
        current.count++;
        current.subscribers.add(componentId);
        
        // Không gửi subscribe message nữa!
      }
    });

    return componentId;
  }

  unsubscribe(componentId: string) {
    this.tracker.forEach((data, symbol) => {
      if (data.subscribers.has(componentId)) {
        data.subscribers.delete(componentId);
        data.count--;

        if (data.count === 0) {
          // 🗑️ No more subscribers → Unsubscribe
          this.tracker.delete(symbol);
          
          this.ws?.send(JSON.stringify({
            type: 'unsubscribe',
            symbol
          }));
        }
      }
    });
  }
}

/**
 * TIMELINE EXAMPLE:
 * 
 * Time | Event                    | VNM count | Action
 * -----|--------------------------|-----------|------------------
 * T0   | Component A mounts       | 0 → 1     | ✅ Send subscribe
 * T1   | Component B mounts       | 1 → 2     | ⚡ Reuse connection
 * T2   | Component C mounts       | 2 → 3     | ⚡ Reuse connection
 * T3   | Component A unmounts     | 3 → 2     | ✋ Keep connection
 * T4   | Component B unmounts     | 2 → 1     | ✋ Keep connection
 * T5   | Component C unmounts     | 1 → 0     | 🗑️ Unsubscribe, close
 */
```

**Pattern 2: Zustand Store Integration**

```typescript
// File: lib/live-data-manager/stores/useLiveDataStore.ts

interface TickerData {
  symbol: string;
  lastPrice: number;
  change: number;
  volume: number;
  timestamp: number;
}

interface LiveDataStore {
  tickerData: Record<string, TickerData>;
  updateTickerData: (data: TickerData) => void;
  batchUpdate: (updates: TickerData[]) => void;
}

const useLiveDataStore = create<LiveDataStore>((set) => ({
  tickerData: {},
  
  // Update single ticker
  updateTickerData: (data) => set((state) => ({
    tickerData: {
      ...state.tickerData,
      [data.symbol]: data
    }
  })),
  
  // Batch update (better performance)
  batchUpdate: (updates) => set((state) => {
    const newData = { ...state.tickerData };
    updates.forEach(data => {
      newData[data.symbol] = data;
    });
    return { tickerData: newData };
  })
}));

// WebSocket message handler
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  
  if (Array.isArray(data)) {
    // Batch update
    useLiveDataStore.getState().batchUpdate(data);
  } else {
    // Single update
    useLiveDataStore.getState().updateTickerData(data);
  }
};
```

**Pattern 3: React Hook Integration**

```typescript
// File: lib/live-data-manager/hooks/useLiveMarketData.ts

const useLiveMarketData = () => {
  const wsRef = useRef<WebSocket | null>(null);
  const updateStore = useLiveDataStore(state => state.updateTickerData);

  useEffect(() => {
    const ws = new WebSocket('wss://market.example.com/stream');
    wsRef.current = ws;

    ws.onopen = () => {
      console.log('✅ WebSocket connected');
      // Re-subscribe to active symbols after reconnect
      const activeSymbols = getActiveSubscriptions();
      if (activeSymbols.length > 0) {
        ws.send(JSON.stringify({
          type: 'subscribe',
          symbols: activeSymbols
        }));
      }
    };

    ws.onmessage = (event) => {
      const data = JSON.parse(event.data);
      updateStore(data); // Update Zustand store
    };

    ws.onerror = (error) => {
      console.error('❌ WebSocket error:', error);
    };

    ws.onclose = (event) => {
      console.log('🔌 WebSocket closed:', event.code);
      // Auto-reconnect
      if (shouldReconnect(event.code)) {
        setTimeout(() => {
          console.log('🔄 Reconnecting...');
          // Re-run effect to reconnect
        }, getReconnectDelay());
      }
    };

    return () => {
      ws.close(1000, 'Component cleanup');
    };
  }, []);

  return wsRef;
};

// Component usage
const StockWatchlist = () => {
  // Initialize WebSocket manager
  useLiveMarketData();

  // Subscribe to symbols
  useSubscribeTickers('ticker', ['VNM', 'HPG', 'VIC']);

  // Get data from store (selective subscription)
  const tickerData = useLiveDataStore(
    state => state.tickerData,
    shallow // Shallow compare để avoid unnecessary re-renders
  );

  return (
    <div>
      {Object.entries(tickerData).map(([symbol, data]) => (
        <StockRow key={symbol} symbol={symbol} data={data} />
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
 * PROBLEM: Nhận 1000 updates/giây từ WebSocket
 * SOLUTION: Throttle UI updates với requestAnimationFrame (60fps)
 */

const useThrottledWebSocket = () => {
  const [data, setData] = useState<TickerData | null>(null);
  const latestDataRef = useRef<TickerData | null>(null);
  const rafIdRef = useRef<number | null>(null);

  // Update UI loop - chạy tối đa 60fps
  const updateUI = useCallback(() => {
    if (latestDataRef.current) {
      setData(latestDataRef.current); // Update state
      latestDataRef.current = null; // Clear
    }
    rafIdRef.current = requestAnimationFrame(updateUI);
  }, []);

  useEffect(() => {
    // Start animation loop
    rafIdRef.current = requestAnimationFrame(updateUI);

    return () => {
      if (rafIdRef.current) {
        cancelAnimationFrame(rafIdRef.current);
      }
    };
  }, [updateUI]);

  // WebSocket message handler
  const onMessage = useCallback((event: MessageEvent) => {
    const parsed = JSON.parse(event.data);
    
    // ⚡ Chỉ store data, KHÔNG update state ngay
    // Đợi RAF cycle tiếp theo
    latestDataRef.current = parsed;
  }, []);

  return { data, onMessage };
};

/**
 * RESULT:
 * ❌ Before: 1000 updates/giây → Lag UI, high CPU
 * ✅ After: 60 updates/giây → Smooth, low CPU
 */
```

**Optimization 2: Selective Re-rendering**

```typescript
// ❌ BAD: Update entire store → All components re-render
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateAll: (newTickers) => set({ tickers: newTickers })
  // Tất cả components subscribe tickers sẽ re-render!
}));

// ✅ GOOD: Selective update + selector
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateTicker: (symbol, data) => set((state) => ({
    tickers: {
      ...state.tickers,
      [symbol]: data // Chỉ update 1 symbol
    }
  }))
}));

// Component chỉ subscribe symbol mình cần
const StockRow = ({ symbol }) => {
  const data = useLiveDataStore(
    state => state.tickers[symbol], // ⚡ Selector - chỉ lấy 1 symbol
    shallow // Shallow compare
  );

  // ✅ Chỉ re-render khi symbol này update
  // ❌ Không re-render khi symbols khác update
};
```

**Optimization 3: Virtual Scrolling**

```typescript
// ❌ BAD: Render all 1000 rows
const Watchlist = ({ data }) => {
  return data.map(item => <StockRow data={item} />); 
  // 1000 DOM nodes → Slow render, high memory
};

// ✅ GOOD: Virtual scrolling with AG Grid
import { AgGridReact } from 'ag-grid-react';

const Watchlist = ({ data }) => {
  const columnDefs = useMemo(() => [
    { field: 'symbol', headerName: 'Symbol' },
    { field: 'lastPrice', headerName: 'Price' },
    { field: 'change', headerName: 'Change' }
  ], []);

  return (
    <AgGridReact
      rowData={data}
      columnDefs={columnDefs}
      // AG Grid tự động dùng virtual scrolling
      // Chỉ render ~20 visible rows thay vì 1000
    />
  );
};

/**
 * PERFORMANCE:
 * ❌ No virtual scrolling: 1000 rows → 500ms render
 * ✅ Virtual scrolling: 20 rows → 16ms render (60fps)
 */
```

**Optimization 4: Batch Updates**

```typescript
// ❌ BAD: Update từng ticker một
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateTicker(data.symbol, data); // 100 calls → 100 re-renders
};

// ✅ GOOD: Batch updates
let batchQueue: TickerData[] = [];
let batchTimer: NodeJS.Timeout | null = null;

ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  batchQueue.push(data);

  if (!batchTimer) {
    batchTimer = setTimeout(() => {
      // Batch update after 16ms (60fps)
      batchUpdateTickers(batchQueue);
      batchQueue = [];
      batchTimer = null;
    }, 16);
  }
};

// 100 updates → 1 batch update → 1 re-render
```

---

#### **Phần 4: Error Handling & Reconnection**

**Exponential Backoff Reconnection:**

```typescript
class ResilientWebSocket {
  private ws: WebSocket | null = null;
  private url: string;
  private reconnectAttempts = 0;
  private maxAttempts = 5;
  private baseDelay = 1000; // 1 second
  private activeSubscriptions: string[] = [];

  constructor(url: string) {
    this.url = url;
    this.connect();
  }

  connect() {
    try {
      this.ws = new WebSocket(this.url);

      this.ws.onopen = () => {
        console.log('✅ Connected');
        this.reconnectAttempts = 0; // Reset counter

        // Re-subscribe to previous channels
        this.resubscribeAll();
      };

      this.ws.onmessage = this.handleMessage.bind(this);

      this.ws.onerror = (error) => {
        console.error('❌ WebSocket error:', error);
      };

      this.ws.onclose = (event) => {
        console.log(`🔌 Closed: ${event.code} - ${event.reason}`);

        if (this.shouldReconnect(event.code)) {
          this.scheduleReconnect();
        } else {
          this.notifyUser('Connection closed. Please refresh.');
        }
      };
    } catch (error) {
      console.error('Failed to create WebSocket:', error);
      this.scheduleReconnect();
    }
  }

  private shouldReconnect(code: number): boolean {
    // Normal closure or auth errors → Don't reconnect
    if (code === 1000 || code === 1008) return false;

    // Max attempts reached
    if (this.reconnectAttempts >= this.maxAttempts) {
      console.error('❌ Max reconnection attempts reached');
      return false;
    }

    return true;
  }

  private scheduleReconnect() {
    // Exponential backoff: 1s, 2s, 4s, 8s, 16s
    const delay = this.baseDelay * Math.pow(2, this.reconnectAttempts);

    console.log(
      `🔄 Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1}/${this.maxAttempts})`
    );

    setTimeout(() => {
      this.reconnectAttempts++;
      this.connect();
    }, delay);
  }

  private resubscribeAll() {
    if (this.activeSubscriptions.length > 0) {
      this.ws?.send(JSON.stringify({
        type: 'subscribe',
        symbols: this.activeSubscriptions
      }));
    }
  }

  subscribe(symbols: string[]) {
    this.activeSubscriptions = [...new Set([...this.activeSubscriptions, ...symbols])];
    
    if (this.ws?.readyState === WebSocket.OPEN) {
      this.ws.send(JSON.stringify({
        type: 'subscribe',
        symbols
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
  const [status, setStatus] = useState<'connected' | 'connecting' | 'disconnected'>('connecting');
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
          🟡 Connecting... {reconnectAttempt > 0 && `(Attempt ${reconnectAttempt}/5)`}
        </span>
      )}
      {status === 'disconnected' && (
        <span className="text-red-500">
          🔴 Disconnected
          <button onClick={() => window.location.reload()}>
            Refresh
          </button>
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

const socket = io('https://api.example.com', {
  // Auto-reconnection
  reconnection: true,
  reconnectionDelay: 1000,
  reconnectionDelayMax: 5000,
  reconnectionAttempts: 5,
  
  // Timeout
  timeout: 20000,
  
  // Transports
  transports: ['websocket', 'polling'], // Try WebSocket first, fallback to polling
  
  // Auth
  auth: {
    token: 'Bearer xyz123'
  }
});

// ✅ Auto-reconnection
socket.on('connect', () => {
  console.log('✅ Connected:', socket.id);
  // Auto re-subscribe after reconnect
  socket.emit('subscribe', { symbols: ['VNM', 'HPG'] });
});

socket.on('disconnect', (reason) => {
  console.log('🔌 Disconnected:', reason);
  // Socket.IO will auto-reconnect!
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
    credentials: true
  }
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

#### **Phần 6: Centrifuge - Enterprise Real-time Messaging**

**Centrifuge Features:**

```typescript
/**
 * CENTRIFUGE = Real-time messaging platform với horizontal scaling
 * 
 * ✅ Advantages:
 * - Horizontal scaling với Redis, KeyDB, Nats
 * - Channel subscription với permissions
 * - Presence (online users tracking)
 * - History (message replay)
 * - Token-based auth với expiration
 * - Binary support
 * - Multiple SDKs (JS, Go, Python, Java...)
 * 
 * ❌ Disadvantages:
 * - Complex setup (need Centrifugo server)
 * - Learning curve
 * - Overkill cho small apps
 * 
 * 🎯 Use Cases:
 * - Trading platforms (high throughput)
 * - Chat applications (presence, history)
 * - Live dashboards (millions of connections)
 * - Multiplayer games
 */

import Centrifuge from 'centrifuge';

const centrifuge = new Centrifuge('ws://localhost:8000/connection/websocket', {
  // Token-based auth
  getToken: async () => {
    const response = await fetch('/api/centrifuge-token');
    const { token } = await response.json();
    return token;
  },
  
  // Auto-resubscribe
  debug: true
});

// Connect
centrifuge.connect();

// Subscribe to channel
const subscription = centrifuge.subscribe('market:stocks', {
  // On publish
  publish: (ctx) => {
    console.log('New message:', ctx.data);
    updateTickerData(ctx.data);
  },
  
  // On subscribe success
  subscribe: (ctx) => {
    console.log('✅ Subscribed to channel');
    
    // Get presence (online users)
    subscription.presence().then(result => {
      console.log('Online users:', result.clients);
    });
    
    // Get history (last messages)
    subscription.history({ limit: 100 }).then(result => {
      console.log('Message history:', result.publications);
    });
  },
  
  // On unsubscribe
  unsubscribe: (ctx) => {
    console.log('🔌 Unsubscribed');
  }
});

// Publish to channel (server-side)
await subscription.publish({
  symbol: 'VNM',
  price: 85000,
  change: 2.5
});

// Presence tracking
subscription.on('presence', (ctx) => {
  console.log('User joined:', ctx.info);
});

// Cleanup
subscription.unsubscribe();
centrifuge.disconnect();
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
<ConnectionStatus status={wsStatus} />

// 6. Batch updates
let batch = [];
const flushBatch = () => {
  updateStore(batch);
  batch = [];
};
setTimeout(flushBatch, 16); // 60fps

// 7. Use virtual scrolling for large lists
<AgGridReact rowData={data} /> // Auto virtual scrolling

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


</details>
