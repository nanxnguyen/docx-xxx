# ❓ TRADING SYSTEM INTERVIEW QUESTIONS

> **Tổng hợp câu hỏi phỏng vấn thực tế cho vị trí Trading System Developer**

---

## 📋 PHÂN LOẠI CÂU HỎI

- [Domain Knowledge](#domain-knowledge) - Kiến thức nghiệp vụ
- [Technical Implementation](#technical-implementation) - Kỹ thuật triển khai
- [System Design](#system-design) - Thiết kế hệ thống
- [Coding Challenges](#coding-challenges) - Bài tập code
- [Behavioral](#behavioral) - Câu hỏi hành vi

---

## 🎯 DOMAIN KNOWLEDGE

### Q1: Giải thích sự khác biệt giữa LO, MP, ATO, ATC?

**Answer:**

| Type | Tên | Đặc điểm | Use case |
|------|-----|----------|----------|
| LO | Limit Order | Đặt giá cụ thể, có thể không khớp | Kiểm soát giá |
| MP | Market Price | Khớp ngay với giá thị trường | Ưu tiên tốc độ |
| ATO | At The Open | Khớp phiên mở cửa 9:00-9:15 | Tham gia giá mở cửa |
| ATC | At The Close | Khớp phiên đóng cửa 14:30-14:45 | Giá đóng cửa |

**Code example:**
\`\`\`typescript
const order = {
  symbol: 'VNM',
  side: 'BUY',
  orderType: 'LO',
  price: 85000,  // LO cần giá, MP không cần
  volume: 100
};
\`\`\`

---

### Q2: Margin Call là gì? Khi nào xảy ra?

**Answer:**

**Định nghĩa:** Cảnh báo khi tài sản ký quỹ thấp hơn mức duy trì tối thiểu.

**Khi nào:** `marginRatio < maintenanceMargin (30%)`

**Xử lý:**
1. Option 1: Nộp thêm tiền
2. Option 2: Bán bớt CP
3. Deadline: T+1
4. Không xử lý → Force Sell

**Code:**
\`\`\`typescript
const checkMarginCall = (account: MarginAccount) => {
  if (account.marginRatio < 0.3) {
    return {
      status: 'MARGIN_CALL',
      action: 'Add collateral or sell stocks',
      deadline: 'T+1',
      requiredAmount: calculateDeficit(account)
    };
  }
  return { status: 'OK' };
};
\`\`\`

---

### Q3: Settlement T+2 hoạt động như thế nào?

**Answer:**

**Timeline:**
- **T+0 (Trade date):** Đặt lệnh, khớp lệnh
  - Cash: Chưa trừ/cộng
  - Stocks: Chưa nhận/mất
  - Can sell: ❌ No

- **T+1:** Chờ thanh toán
  - Chuyển quyền sở hữu
  - Can sell: ❌ No

- **T+2 (Settlement date):** Thanh toán
  - Cash: Trừ/cộng chính thức
  - Stocks: Nhận/mất chính thức
  - Can sell: ✅ Yes

**Impact:**
- Cần quản lý cash flow T+0, T+1, T+2
- Không thể bán CP chưa về (blocked volume)
- Mua → Bán cùng ngày = Day trading (cần tài khoản đặc biệt)

---

### Q4: Tính P&L của Futures khác gì Equity?

**Answer:**

**Equity P&L:**
\`\`\`typescript
pl = (sellPrice - buyPrice) × volume
\`\`\`

**Futures P&L:**
\`\`\`typescript
pl = (currentPrice - avgPrice) × netQty × contractMultiplier
//                                           ↑ 100,000
\`\`\`

**Ví dụ:**
\`\`\`typescript
// Equity: Mua 100 VNM @ 85k, bán 90k
const equityPL = (90000 - 85000) * 100; // +500,000đ

// Futures: Long 1 VN30F @ 1000, hiện tại 1050
const futuresPL = (1050 - 1000) * 1 * 100000; // +5,000,000đ
// → Đòn bẩy cao hơn!
\`\`\`

---

### Q5: Order Book matching algorithm?

**Answer:**

**Price-Time Priority:**
1. Sắp xếp buy orders: Giá cao → thấp, thời gian sớm → muộn
2. Sắp xếp sell orders: Giá thấp → cao, thời gian sớm → muộn
3. Khớp best buy vs best sell
4. Giá khớp: Lệnh vào trước dùng giá đó

**Code:**
\`\`\`typescript
class OrderMatcher {
  match() {
    while (this.canMatch()) {
      const bestBuy = this.buyOrders[0];
      const bestSell = this.sellOrders[0];

      if (bestBuy.price >= bestSell.price) {
        const price = bestBuy.time < bestSell.time
          ? bestBuy.price
          : bestSell.price;

        const volume = Math.min(bestBuy.volume, bestSell.volume);

        this.executeTrade({ price, volume });
        this.updateOrders(bestBuy, bestSell, volume);
      } else {
        break;
      }
    }
  }
}
\`\`\`

---

## 💻 TECHNICAL IMPLEMENTATION

### Q6: Làm sao handle 1000 ticker updates/giây?

**Answer:**

**Problem:** WebSocket nhận 1000 updates/s, UI chỉ render 60fps

**Solutions:**

1. **Throttle với requestAnimationFrame:**
\`\`\`typescript
const latestData = useRef({});
const rafId = useRef();

ws.onmessage = (event) => {
  latestData.current[symbol] = data; // Store only, don't setState
};

const updateUI = () => {
  setData(latestData.current); // Update 60fps
  rafId.current = requestAnimationFrame(updateUI);
};
\`\`\`

2. **Virtual Scrolling:**
\`\`\`typescript
// Chỉ render visible rows (20/1000)
<AgGridReact rowData={data} />
\`\`\`

3. **Selective Subscription:**





\`\`\`typescript
// Chỉ subscribe symbols đang hiển thị
const visibleSymbols = getVisibleRows();
useSubscribe(visibleSymbols);
\`\`\`

4. **Batch Updates:**
\`\`\`typescript
// Update batch thay vì từng symbol
updateMany(updates) {
  setState(state => ({ ...state, ...updates }));
}
\`\`\`

---

### Q7: WebSocket reconnection strategy?

**Answer:**

**Exponential Backoff:**

\`\`\`typescript
class ResilientWebSocket {
  private attempts = 0;
  private maxAttempts = 5;

  reconnect() {
    if (this.attempts >= this.maxAttempts) {
      this.notifyUser('Connection lost');
      return;
    }

    // 1s, 2s, 4s, 8s, 16s
    const delay = 1000 * Math.pow(2, this.attempts);

    setTimeout(() => {
      this.attempts++;
      this.connect();
    }, delay);
  }

  onOpen() {
    this.attempts = 0; // Reset
    this.resubscribeAll(); // Re-subscribe
  }
}
\`\`\`

**Benefits:**
- Tránh spam server
- Tăng delay tự động khi mạng yếu
- Có giới hạn attempts

---

### Q8: Memory leak với WebSocket subscriptions?

**Answer:**

**Problem:**
\`\`\`typescript
// ❌ Component A, B, C cùng subscribe 'VNM'
// → 3 WebSocket connections!
const ComponentA = () => {
  useEffect(() => {
    const ws = new WebSocket(url); // Leak!
  }, []);
};
\`\`\`

**Solution - Reference Counting:**

\`\`\`typescript
class SubscriptionTracker {
  private counts = new Map<string, number>();

  subscribe(symbol: string) {
    const count = this.counts.get(symbol) || 0;
    this.counts.set(symbol, count + 1);

    if (count === 0) {
      // First subscriber → Create connection
      this.createConnection(symbol);
    }
  }

  unsubscribe(symbol: string) {
    const count = this.counts.get(symbol) || 0;

    if (count <= 1) {
      // Last subscriber → Close connection
      this.closeConnection(symbol);
      this.counts.delete(symbol);
    } else {
      this.counts.set(symbol, count - 1);
    }
  }
}

// Timeline:
// Component A mounts   → VNM count: 0 → 1 (Create WS)
// Component B mounts   → VNM count: 1 → 2 (Reuse WS)
// Component A unmounts → VNM count: 2 → 1 (Keep WS)
// Component B unmounts → VNM count: 1 → 0 (Close WS)
\`\`\`

---

### Q9: Prevent double order submission?

**Answer:**

\`\`\`typescript
const OrderButton = () => {
  const [isSubmitting, setIsSubmitting] = useState(false);
  const lastSubmitTime = useRef(0);
  const cooldown = 3000; // 3s

  const handleSubmit = async () => {
    const now = Date.now();

    // Check cooldown
    if (now - lastSubmitTime.current < cooldown) {
      toast.error('Please wait 3 seconds');
      return;
    }

    // Prevent double click
    if (isSubmitting) return;

    try {
      setIsSubmitting(true);
      await api.placeOrder(order);
      lastSubmitTime.current = now;
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <button onClick={handleSubmit} disabled={isSubmitting}>
      {isSubmitting ? 'Submitting...' : 'Place Order'}
    </button>
  );
};
\`\`\`

---

### Q10: Giá cổ phiếu dùng Number hay String?

**Answer:**

**String hoặc Decimal library!**

**Problem với Number:**
\`\`\`javascript
0.1 + 0.2 === 0.3 // false ❌
0.1 + 0.2 // 0.30000000000000004
\`\`\`

**Solution:**

\`\`\`typescript
// Option 1: String
interface StockPrice {
  symbol: string;
  price: string; // "85000.50"
}

// Option 2: Decimal.js
import Decimal from 'decimal.js';

const price = new Decimal("85000.50");
const total = price.times(100).toFixed(2); // "8500050.00"
\`\`\`

**Trong code myHSC:**
\`\`\`typescript
// API trả về string
const tickerData: TickerData = {
  ticker: "VNM",
  lastPrice: "85000.50" // String!
};

// Parse khi cần tính toán
const numPrice = parseFloat(tickerData.lastPrice);
\`\`\`

---

## 🏗️ SYSTEM DESIGN

### Q11: Design real-time price board for 1000 concurrent users

**Answer:**

**Requirements:**
- 1000 users
- Each watches 50 symbols
- Updates 1-2 times/giây
- Latency < 500ms

**Architecture:**

\`\`\`
┌──────────┐         ┌─────────────────┐
│ Client A │◄────────┤                 │
├──────────┤  WS     │  Load Balancer  │
│ Client B │◄────────┤                 │
├──────────┤         └────────┬────────┘
│ Client C │                  │
└──────────┘         ┌────────▼────────┐
                     │  WS Gateway 1   │
                     ├─────────────────┤
                     │  WS Gateway 2   │
                     └────────┬────────┘
                              │
                     ┌────────▼────────┐
                     │  Message Queue  │◄──── Market Data Provider
                     │  (Kafka/Redis)  │
                     └────────┬────────┘
                              │
                     ┌────────▼────────┐
                     │  Redis Cache    │
                     │  (Hot Data)     │
                     └─────────────────┘
\`\`\`

**Components:**

1. **WebSocket Gateway:**
   - Handle 500 connections each
   - Manage subscriptions
   - Broadcast updates

2. **Message Queue:**
   - Pub/Sub pattern
   - Decouple data source from clients
   - Buffer spikes

3. **Redis Cache:**
   - Store latest price data
   - Fast read (< 1ms)
   - TTL 5 seconds

4. **Client-side:**
   - Virtual scrolling
   - Throttle updates 60fps
   - Selective subscription

**Scaling:**
- Horizontal: Add more WS gateways
- Vertical: Increase gateway capacity
- Database: Read replicas

---

### Q12: Caching strategy cho market data?

**Answer:**

**Cache Levels:**

1. **L1 - Client Cache (Browser)**
\`\`\`typescript
// Zustand store
const cache = {
  tickers: Map<string, TickerData>,
  ttl: 60000, // 1 minute
  lastUpdate: timestamp
};
\`\`\`

2. **L2 - CDN/Edge Cache**
\`\`\`
- Static content: Charts, layouts
- Cache-Control: max-age=3600
\`\`\`

3. **L3 - Application Cache (Redis)**
\`\`\`typescript
// Hot data
redis.setex('ticker:VNM', 5, JSON.stringify(data));

// Cold data
redis.setex('historical:VNM:2024-01', 86400, data);
\`\`\`

4. **L4 - Database**
\`\`\`
- Historical data
- Reference data
- User portfolios
\`\`\`

**Cache Invalidation:**
\`\`\`typescript
// Time-based
if (Date.now() - cache.lastUpdate > TTL) {
  fetch();
}

// Event-based
ws.onmessage = (data) => {
  cache.update(data);
};
\`\`\`

---

## 🧑‍💻 CODING CHALLENGES

### C1: Implement Order Book

\`\`\`typescript
class OrderBook {
  private bids: Map<number, number>; // price → volume
  private asks: Map<number, number>;

  addOrder(order: Order) {
    // TODO: Add to bid/ask map
  }

  removeOrder(orderId: string) {
    // TODO: Remove from map
  }

  getBestBid(): { price: number, volume: number } | null {
    // TODO: Return highest bid
  }

  getBestAsk(): { price: number, volume: number } | null {
    // TODO: Return lowest ask
  }

  match(): Trade[] {
    // TODO: Match orders
  }
}
\`\`\`

### C2: Calculate Portfolio Value

\`\`\`typescript
interface Position {
  symbol: string;
  volume: number;
  avgPrice: number;
}

function calculatePortfolio(
  positions: Position[],
  prices: Map<string, number>,
  cash: number
): {
  totalValue: number,
  unrealizedPL: number,
  roi: number
} {
  // TODO: Implement
}

// Test
const result = calculatePortfolio(
  [
    { symbol: 'VNM', volume: 100, avgPrice: 85000 },
    { symbol: 'HPG', volume: 200, avgPrice: 25000 }
  ],
  new Map([['VNM', 90000], ['HPG', 23000]]),
  50_000_000
);
\`\`\`

### C3: WebSocket Throttling

\`\`\`typescript
function throttleWebSocket(
  ws: WebSocket,
  maxUpdatesPerSecond: number
): WebSocket {
  // TODO: Implement throttling
  // Return proxied WebSocket that limits onmessage calls
}
\`\`\`

---

## 🎭 BEHAVIORAL

### B1: Kể về lần bạn fix bug critical trong production

**Framework STAR:**
- **S**ituation: Bug gì, impact như thế nào
- **T**ask: Nhiệm vụ của bạn
- **A**ction: Bạn làm gì
- **R**esult: Kết quả

**Example:**
\`\`\`
S: WebSocket disconnect mass, 500 users mất realtime data
T: Tìm nguyên nhân và fix ASAP
A:
  1. Check logs → Phát hiện memory leak
  2. Review code → Thấy không cleanup subscriptions
  3. Hotfix: Add cleanup trong useEffect
  4. Deploy canary → Test 10% users
  5. Full rollout
R: Fix trong 2 giờ, 0 downtime, add monitoring
\`\`\`

### B2: Trade-off giữa feature mới vs stability?

**Answer:**
- **Trading system = Stability first**
- Feature có thể delay, bug không thể
- Risk assessment matrix
- Gradual rollout, feature flags
- Extensive testing

---

## 🎯 TIPS PHỎNG VẤN

1. **Hiểu domain:** Biết LO, MP, Margin Call, T+2
2. **Practice code:** Implement Order Book, Portfolio calc
3. **System design:** Vẽ architecture diagram
4. **Ask questions:** Không hiểu → Hỏi ngay
5. **Think aloud:** Nói ra suy nghĩ khi code

**Good luck! 🍀**
