# 📡 WEBSOCKET & REAL-TIME DATA HANDLING

> **File nguồn:** `lib/live-data-manager/`, `lib/binance-data-manager/`
>
> **Mục đích:** Tài liệu về xử lý dữ liệu real-time trong Trading System

---

## 📋 MỤC LỤC

1. [WebSocket Basics](#websocket-basics)
2. [Architecture Pattern](#architecture-pattern)
3. [Subscription Management](#subscription-management)
4. [Performance Optimization](#performance-optimization)
5. [Error Handling & Reconnection](#error-handling--reconnection)
6. [Interview Questions](#interview-questions)

---

## 🌐 WEBSOCKET BASICS

### Tại sao dùng WebSocket?

```typescript
// ❌ REST API Polling - Không hiệu quả
setInterval(() => {
  fetch('/api/market-data')
    .then(res => res.json())
    .then(data => updateUI(data));
}, 1000); // Call API mỗi giây!
// Vấn đề:
// - Tốn băng thông
// - Latency cao
// - Server load cao
// - Không real-time thực sự

// ✅ WebSocket - Real-time
const ws = new WebSocket('wss://market-data');
ws.onmessage = (event) => {
  const data = JSON.parse(event.data);
  updateUI(data); // Update ngay khi có data mới
};
// Ưu điểm:
// - Kết nối duy trì (persistent connection)
// - Push data ngay lập tức
// - Latency thấp
// - Tiết kiệm băng thông
```

### WebSocket Lifecycle

```typescript
interface WebSocketLifecycle {
  // 1. CONNECTING
  CONNECTING: () => {
    const ws = new WebSocket('wss://api.example.com/stream');
    console.log('State:', ws.readyState); // 0 - CONNECTING
  },

  // 2. OPEN
  OPEN: (ws: WebSocket) => {
    ws.onopen = () => {
      console.log('State:', ws.readyState); // 1 - OPEN
      // Có thể gửi message
      ws.send(JSON.stringify({ type: 'subscribe', symbols: ['VNM', 'HPG'] }));
    };
  },

  // 3. MESSAGE
  MESSAGE: (ws: WebSocket) => {
    ws.onmessage = (event: MessageEvent) => {
      const data = JSON.parse(event.data);
      console.log('Received:', data);
    };
  },

  // 4. ERROR
  ERROR: (ws: WebSocket) => {
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  },

  // 5. CLOSING/CLOSED
  CLOSE: (ws: WebSocket) => {
    ws.onclose = (event: CloseEvent) => {
      console.log('State:', ws.readyState); // 3 - CLOSED
      console.log('Code:', event.code);
      console.log('Reason:', event.reason);

      // Reconnect logic
      if (shouldReconnect(event.code)) {
        reconnect();
      }
    };
  }
}
```

---

## 🏗️ ARCHITECTURE PATTERN

### live-data-manager Pattern (myHSC Production)

```typescript
// File: lib/live-data-manager/
/**
 * Architecture:
 *
 * Component A ─┐
 * Component B ─┼─→ useLiveMarketData() ─→ WebSocket Manager
 * Component C ─┘                            ↓
 *                                    Subscription Tracker
 *                                            ↓
 *                                      Zustand Store
 *                                            ↓
 *                                    Components (auto re-render)
 */

// 1. WebSocket Manager
class LiveDataManager {
  private ws: WebSocket | null = null;
  private subscribers = new Map<string, Set<string>>();

  connect(url: string) {
    this.ws = new WebSocket(url);
    this.ws.onmessage = this.handleMessage;
    this.ws.onclose = this.handleClose;
  }

  subscribe(channel: string, symbols: string[]) {
    const subscriptionId = generateId();

    // Reference counting
    symbols.forEach(symbol => {
      if (!this.subscribers.has(symbol)) {
        this.subscribers.set(symbol, new Set());
        this.sendSubscribe(symbol);
      }
      this.subscribers.get(symbol)!.add(subscriptionId);
    });

    return subscriptionId;
  }

  unsubscribe(subscriptionId: string) {
    // Cleanup subscriptions
    this.subscribers.forEach((subs, symbol) => {
      subs.delete(subscriptionId);
      if (subs.size === 0) {
        this.sendUnsubscribe(symbol);
        this.subscribers.delete(symbol);
      }
    });
  }
}

// 2. Zustand Store
interface LiveDataStore {
  tickerData: Record<string, TickerData>;
  updateTickerData: (data: TickerData) => void;
}

const useLiveDataStore = create<LiveDataStore>((set) => ({
  tickerData: {},
  updateTickerData: (data) => set((state) => ({
    tickerData: {
      ...state.tickerData,
      [data.ticker]: data
    }
  }))
}));

// 3. React Hook
const useSubscribeTickers = (
  channel: TChannel,
  symbols: string[]
) => {
  useEffect(() => {
    const subscriptionId = liveDataManager.subscribe(channel, symbols);

    return () => {
      liveDataManager.unsubscribe(subscriptionId);
    };
  }, [channel, symbols]);
};

// 4. Component Usage
const StockWatchlist = () => {
  // Initialize manager
  useLiveMarketData();

  // Subscribe to symbols
  useSubscribeTickers('ticker', ['VNM', 'HPG', 'VIC']);

  // Get data from store
  const tickerData = useLiveDataStore(state => state.tickerData);

  return (
    <div>
      {Object.entries(tickerData).map(([symbol, data]) => (
        <Row key={symbol} data={data} />
      ))}
    </div>
  );
};
```

### binance-data-manager Pattern (Testing/Demo)

```typescript
// File: lib/binance-data-manager/
/**
 * Simplified version for testing Binance WebSocket
 */

// 1. Hook-based Manager
const useBinanceTickerManager = (symbols: string[]) => {
  const wsRef = useRef<WebSocket | null>(null);
  const updateStore = useBinanceDataStore(state => state.updateTickerData);

  useEffect(() => {
    // Build streams: btcusdt@ticker, ethusdt@ticker
    const streams = symbols.map(s => `${s.toLowerCase()}@ticker`);
    const url = `wss://stream.binance.com:9443/stream?streams=${streams.join('/')}`;

    wsRef.current = new WebSocket(url);

    wsRef.current.onmessage = (event) => {
      const { stream, data } = JSON.parse(event.data);
      const mapped = mapBinanceData(data);
      updateStore(mapped);
    };

    return () => {
      wsRef.current?.close();
    };
  }, [symbols]);
};

// 2. AG Grid Integration
const BinanceAGGrid = ({ symbols }: Props) => {
  // Manager hook
  useBinanceTickerManager(symbols);

  // Subscribe with tracker
  useBinanceSubscribeTickers('ticker', symbols);

  // Get data
  const tickerData = useBinanceDataStore(state => state.tickerData);

  // Prepare for AG Grid
  const rowData = useMemo(() =>
    symbols.map(symbol => ({
      symbol,
      ...tickerData[symbol]
    })),
    [symbols, tickerData]
  );

  return <AgGridReact rowData={rowData} ... />;
};
```

---

## 🎯 SUBSCRIPTION MANAGEMENT

### Reference Counting Pattern

```typescript
// File: lib/live-data-manager/stores/useSubTrackerStore.ts
/**
 * Problem: Multiple components subscribe to same symbol
 * Solution: Reference counting to manage subscriptions efficiently
 */

interface SubscriptionTracker {
  subscriptions: Map<string, {
    count: number;
    subscribers: Set<string>;
  }>;
}

const useSubTrackerStore = create<SubscriptionTracker>((set, get) => ({
  subscriptions: new Map(),

  // Component A subscribes to 'VNM'
  addSubscription: (symbol: string, componentId: string) => {
    const current = get().subscriptions.get(symbol);

    if (!current) {
      // First subscriber → Create WebSocket connection
      set(state => ({
        subscriptions: new Map(state.subscriptions).set(symbol, {
          count: 1,
          subscribers: new Set([componentId])
        })
      }));

      // Send subscribe message to server
      sendSubscribeMessage(symbol);
    } else {
      // Already subscribed → Just increment counter
      current.count++;
      current.subscribers.add(componentId);

      // Reuse existing connection, no new subscribe message
    }
  },

  // Component A unmounts, unsubscribes from 'VNM'
  removeSubscription: (symbol: string, componentId: string) => {
    const current = get().subscriptions.get(symbol);

    if (!current) return;

    current.subscribers.delete(componentId);
    current.count--;

    if (current.count === 0) {
      // No more subscribers → Close WebSocket connection
      get().subscriptions.delete(symbol);
      sendUnsubscribeMessage(symbol);
    }
  }
}));

// Timeline example:
/**
 * Time | Event                    | VNM count | Action
 * -----|--------------------------|-----------|------------------
 * T0   | Component A mounts       | 0 → 1     | Send subscribe
 * T1   | Component B mounts       | 1 → 2     | Reuse connection
 * T2   | Component C mounts       | 2 → 3     | Reuse connection
 * T3   | Component A unmounts     | 3 → 2     | Keep connection
 * T4   | Component B unmounts     | 2 → 1     | Keep connection
 * T5   | Component C unmounts     | 1 → 0     | Send unsubscribe, close
 */
```

### Batch Subscription

```typescript
// ❌ BAD: Subscribe one by one
symbols.forEach(symbol => {
  ws.send(JSON.stringify({ type: 'subscribe', symbol }));
  // 100 symbols = 100 messages!
});

// ✅ GOOD: Batch subscribe
const batchSubscribe = (symbols: string[]) => {
  // Group into batches of 50
  const batches = chunk(symbols, 50);

  batches.forEach(batch => {
    ws.send(JSON.stringify({
      type: 'subscribe',
      symbols: batch
    }));
  });
};

// 100 symbols = 2 messages (50 + 50)
```

---

## ⚡ PERFORMANCE OPTIMIZATION

### 1. Throttling with requestAnimationFrame

```typescript
// Problem: Nhận 1000 updates/giây, UI chỉ render 60fps
// Solution: Throttle với requestAnimationFrame

const useThrottledWebSocket = () => {
  const [data, setData] = useState<TickerData | null>(null);
  const latestDataRef = useRef<TickerData | null>(null);
  const rafIdRef = useRef<number | null>(null);

  // Update UI loop (60fps max)
  const updateUI = useCallback(() => {
    if (latestDataRef.current) {
      setData(latestDataRef.current);
      latestDataRef.current = null; // Clear after update
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

    // Just store, don't update state yet
    // Wait for next RAF cycle
    latestDataRef.current = parsed;
  }, []);

  return { data, onMessage };
};

// Result: Max 60 updates/giây instead of 1000
```

### 2. Selective Re-rendering

```typescript
// ❌ BAD: Update entire store → All components re-render
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateAll: (newTickers) => set({ tickers: newTickers })
}));

// Component re-renders even if its symbol hasn't changed!

// ✅ GOOD: Selective update + selector
const useLiveDataStore = create((set) => ({
  tickers: {},
  updateTicker: (symbol, data) => set((state) => ({
    tickers: {
      ...state.tickers,
      [symbol]: data
    }
  }))
}));

// Component only subscribes to its symbol
const StockRow = ({ symbol }) => {
  const data = useLiveDataStore(
    state => state.tickers[symbol], // Selector
    shallow // Shallow compare
  );

  // Only re-renders when this specific symbol updates
};
```

### 3. Virtual Scrolling

```typescript
// ❌ BAD: Render all 1000 rows
const Watchlist = ({ data }) => {
  return data.map(item => <Row data={item} />); // 1000 DOM nodes!
};

// ✅ GOOD: Virtual scrolling with AG Grid
import { AgGridReact } from 'ag-grid-react';

const Watchlist = ({ data }) => {
  return (
    <AgGridReact
      rowData={data}
      // AG Grid automatically uses virtual scrolling
      // Only renders ~20 visible rows
    />
  );
};

// Performance:
// - No virtual scrolling: 1000 rows → 500ms render
// - Virtual scrolling: 20 rows → 16ms render (60fps)
```

### 4. Memoization

```typescript
// Memoize row component
const StockRow = React.memo(({ symbol }) => {
  const data = useLiveDataStore(
    state => state.tickers[symbol]
  );

  return <div>{symbol}: {data?.lastPrice}</div>;
}, (prevProps, nextProps) => {
  // Custom comparison
  return prevProps.symbol === nextProps.symbol;
});

// Memoize column definitions
const columnDefs = useMemo(() => [
  { field: 'symbol', headerName: 'Symbol' },
  { field: 'lastPrice', headerName: 'Price' },
  // ...
], []); // Empty deps → Only compute once
```

---

## 🛡️ ERROR HANDLING & RECONNECTION

### Exponential Backoff Reconnection

```typescript
class ResilientWebSocket {
  private ws: WebSocket | null = null;
  private reconnectAttempts = 0;
  private maxAttempts = 5;
  private baseDelay = 1000; // 1 second

  connect(url: string) {
    try {
      this.ws = new WebSocket(url);

      this.ws.onopen = () => {
        console.log('✅ Connected');
        this.reconnectAttempts = 0; // Reset on success
        this.resubscribeAll(); // Re-subscribe to previous channels
      };

      this.ws.onmessage = this.handleMessage;

      this.ws.onerror = (error) => {
        console.error('❌ WebSocket error:', error);
      };

      this.ws.onclose = (event) => {
        console.log('Connection closed:', event.code, event.reason);

        // Auto-reconnect với exponential backoff
        if (this.shouldReconnect(event.code)) {
          this.scheduleReconnect();
        }
      };
    } catch (error) {
      console.error('Failed to create WebSocket:', error);
      this.scheduleReconnect();
    }
  }

  private shouldReconnect(code: number): boolean {
    // Don't reconnect on normal closure or auth errors
    if (code === 1000 || code === 1008) return false;

    // Limit reconnect attempts
    return this.reconnectAttempts < this.maxAttempts;
  }

  private scheduleReconnect() {
    if (this.reconnectAttempts >= this.maxAttempts) {
      console.error('❌ Max reconnection attempts reached');
      this.notifyUser('Connection lost. Please refresh.');
      return;
    }

    // Exponential backoff: 1s, 2s, 4s, 8s, 16s
    const delay = this.baseDelay * Math.pow(2, this.reconnectAttempts);

    console.log(`🔄 Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1}/${this.maxAttempts})`);

    setTimeout(() => {
      this.reconnectAttempts++;
      this.connect(this.url);
    }, delay);
  }

  private resubscribeAll() {
    // Re-subscribe to all channels after reconnect
    const subscriptions = this.getActiveSubscriptions();
    subscriptions.forEach(({ channel, symbols }) => {
      this.subscribe(channel, symbols);
    });
  }
}

// Timeline:
/**
 * T0: Connection lost
 * T0 + 1s: Attempt 1
 * T0 + 3s: Attempt 2 (1s + 2s)
 * T0 + 7s: Attempt 3 (1s + 2s + 4s)
 * T0 + 15s: Attempt 4 (1s + 2s + 4s + 8s)
 * T0 + 31s: Attempt 5 (final)
 */
```

### Connection Status UI

```typescript
const ConnectionStatus = () => {
  const [status, setStatus] = useState<'connected' | 'connecting' | 'disconnected'>('connecting');

  useEffect(() => {
    const ws = getWebSocketInstance();

    const handleOpen = () => setStatus('connected');
    const handleClose = () => setStatus('disconnected');

    ws.addEventListener('open', handleOpen);
    ws.addEventListener('close', handleClose);

    return () => {
      ws.removeEventListener('open', handleOpen);
      ws.removeEventListener('close', handleClose);
    };
  }, []);

  return (
    <div className={`status ${status}`}>
      {status === 'connected' && '🟢 Connected'}
      {status === 'connecting' && '🟡 Connecting...'}
      {status === 'disconnected' && '🔴 Disconnected'}
    </div>
  );
};
```

---

## ❓ INTERVIEW QUESTIONS

### Q1: WebSocket vs REST API Polling?

```
Answer:
WebSocket:
- Ưu: Real-time, low latency, efficient
- Nhược: Phức tạp hơn, cần handle reconnection

REST Polling:
- Ưu: Đơn giản, dễ implement
- Nhược: Latency cao, tốn băng thông, không real-time

Use WebSocket khi: Trading, chat, live dashboard
Use REST khi: Static data, không cần real-time
```

### Q2: Làm sao handle 1000 ticker updates/giây?

```typescript
Answer:
1. Throttle với requestAnimationFrame (60fps)
2. Batch updates thay vì update từng ticker
3. Virtual scrolling (chỉ render visible rows)
4. Memoization (React.memo, useMemo)
5. Selective subscription (chỉ subscribe visible tickers)

Code:
const latestData = useRef({});
const rafId = useRef();

ws.onmessage = (event) => {
  latestData.current[symbol] = data; // Store only
};

const updateUI = () => {
  setData(latestData.current); // Update 60fps
  rafId.current = requestAnimationFrame(updateUI);
};
```

### Q3: Memory leak với WebSocket?

```typescript
Answer:
Causes:
1. Không close WebSocket khi unmount
2. Không remove event listeners
3. Subscribe nhiều lần không cleanup

Solution:
useEffect(() => {
  const ws = new WebSocket(url);

  return () => {
    ws.close(); // ✅ Cleanup
  };
}, []);

// Reference counting:
const tracker = new Map();
subscribe(symbol) {
  if (count === 0) createConnection();
  count++;
}
unsubscribe(symbol) {
  count--;
  if (count === 0) closeConnection();
}
```

### Q4: Reconnection strategy?

```typescript
Answer:
Exponential Backoff:
- Attempt 1: 1s
- Attempt 2: 2s
- Attempt 3: 4s
- Attempt 4: 8s
- Max: 5 attempts → Give up

Code:
const delay = baseDelay * Math.pow(2, attempt);
setTimeout(() => reconnect(), delay);

+ Re-subscribe sau khi reconnect
+ Show connection status cho user
+ Limit max attempts
```

---

## 📚 TÀI LIỆU THAM KHẢO

- myHSC Source: `lib/live-data-manager/`, `lib/binance-data-manager/`
- WebSocket API: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
- AG Grid Virtual Scrolling: https://www.ag-grid.com/javascript-data-grid/dom-virtualisation/

---

**Practice:** Đọc code `useLiveMarketData.ts` và `useBinanceTickerManager.ts` để hiểu flow thực tế!

