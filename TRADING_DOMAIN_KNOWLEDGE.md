# 📚 TRADING DOMAIN KNOWLEDGE - TÀI LIỆU KIẾN THỨC CHỨNG KHOÁN

> **Mục đích:** Tài liệu tổng hợp kiến thức domain chứng khoán cho developers, đặc biệt là chuẩn bị phỏng vấn Trading System.
>
> **Dựa trên:** Codebase myHSC 4.x - Trading Frontend Application

---

## 📋 MỤC LỤC

1. [Giới thiệu chung](#giới-thiệu-chung)
2. [Các loại tài sản](#các-loại-tài-sản)
3. [Order Types - Các loại lệnh](#order-types)
4. [Trading Sessions - Phiên giao dịch](#trading-sessions)
5. [Order Book & Matching Algorithm](#order-book--matching-algorithm)
6. [Settlement T+2](#settlement-t2)
7. [Corporate Actions](#corporate-actions)
8. [Real-time Data & WebSocket](#real-time-data)
9. [Portfolio Management](#portfolio-management)
10. [Interview Questions](#interview-questions)

---

## 🎯 GIỚI THIỆU CHUNG

### Thị trường chứng khoán Việt Nam

```typescript
// Cấu trúc thị trường
interface VietnameseStockMarket {
  exchanges: {
    HOSE: 'Sở Giao dịch Chứng khoán TP.HCM',  // Blue chips
    HNX: 'Sở Giao dịch Chứng khoán Hà Nội',   // Mid-cap
    UPCOM: 'Thị trường OTC',                   // Small-cap
  };

  indices: {
    VN30: 'Top 30 cổ phiếu vốn hóa lớn nhất HOSE',
    VNINDEX: 'Chỉ số toàn bộ HOSE',
    HNX30: 'Top 30 cổ phiếu HNX',
  };

  derivatives: {
    VN30F: 'VN30 Futures',
    VN100F: 'VN100 Futures', // Nếu enable
  };
}
```

---

## 💼 CÁC LOẠI TÀI SẢN

### 1. EQUITY (Cổ phiếu thường)

```typescript
// File: pages/services/equity/
interface EquityOrder {
  symbol: string;        // Mã CP: VNM, HPG, VIC
  side: 'BUY' | 'SELL';
  orderType: 'LO' | 'MP' | 'ATO' | 'ATC' | 'MOK' | 'MAK';
  price: number;         // Giá đặt lệnh
  volume: number;        // Số lượng CP
  accountNo: string;     // Số tài khoản
}
```

**Ví dụ thực tế:**
```typescript
const buyOrder: EquityOrder = {
  symbol: 'VNM',         // Vinamilk
  side: 'BUY',
  orderType: 'LO',       // Limit Order
  price: 85000,          // 85,000đ/CP
  volume: 100,           // 100 cổ phiếu
  accountNo: '0001234567',
  // Tổng giá trị: 8,500,000đ
};
```

### 2. EQUITY PLUS (Margin Trading - Giao dịch ký quỹ)

```typescript
// File: pages/services/equityPlus/
interface MarginAccount {
  equity: number;              // Tài sản ròng
  totalEquityAmount: number;   // Tổng giá trị tài sản
  extraCredit: number;         // Hạn mức tín dụng
  excessEquityAmount: number;  // Tài sản thừa
  marginRatio: number;         // Tỷ lệ ký quỹ (radio)
  buyingPower: number;         // Sức mua
  accountStatus: string;       // Trạng thái: NORMAL, WARNING, FORCE_SELL
}

interface MarginContract {
  contractNo: string;                      // Số hợp đồng
  loanAmount: number;                      // Số tiền vay (principal)
  interestRate: number;                    // Lãi suất
  activeDate: Date;                        // Ngày hiệu lực
  dueDate: Date;                           // Ngày đáo hạn
  totalAmount: number;                     // Tổng tiền phải trả (gốc + lãi)
  interestPeriodAmount: number;            // Lãi kỳ sau thuế
  temporarilyInterestPrincipleAmount: number; // Lãi tạm tính
}
```

**Ví dụ Margin Call:**
```typescript
const checkMarginStatus = (account: MarginAccount) => {
  const { marginRatio, accountStatus } = account;

  if (marginRatio < 0.3) {
    // Margin Call! Phải bổ sung tài sản
    return {
      status: 'FORCE_SELL',
      action: 'Nộp thêm tiền hoặc bán bớt CP trong T+1',
      requiredAmount: calculateRequiredCollateral(account)
    };
  }

  if (marginRatio < 0.5) {
    return { status: 'WARNING', action: 'Cảnh báo: Margin ratio thấp' };
  }

  return { status: 'NORMAL', action: 'OK' };
};
```

### 3. DERIVATIVES (Phái sinh - Futures)

```typescript
// File: pages/trading/futures/
interface FuturesContract {
  symbol: string;          // VN30F2312 (VN30 Future tháng 12/2023)
  side: 'LONG' | 'SHORT'; // Long = Cược lên, Short = Cược xuống
  price: number;
  volume: number;          // Số hợp đồng
  netQty: number;          // Vị thế ròng
  avgPrice: number;        // Giá trung bình
  unrealizedPL: number;    // Lãi/lỗ chưa chốt
  margin: number;          // Ký quỹ
  contractMultiplier: 100000; // 1 điểm = 100,000đ
}

interface FuturesAccount {
  totalEquity: number;        // Tổng tài sản
  marginUsed: number;         // Ký quỹ đã dùng
  availableMargin: number;    // Ký quỹ khả dụng
  unrealizedPL: number;       // Lãi/lỗ chưa chốt
  realizedPL: number;         // Lãi/lỗ đã chốt
  position: FuturesPosition[];
}
```

**Tính P&L Futures:**
```typescript
const calculateFuturesPL = (
  position: FuturesPosition,
  currentPrice: number
) => {
  // netQty > 0: Long position
  // netQty < 0: Short position
  const priceChange = currentPrice - position.avgPrice;
  const unrealizedPL = position.netQty * priceChange * 100000;

  return {
    unrealizedPL,
    roi: (unrealizedPL / (position.avgPrice * Math.abs(position.netQty) * 100000)) * 100
  };
};

// Ví dụ:
// Long 1 VN30F @ 1000, hiện tại 1050
// PL = 1 * (1050 - 1000) * 100,000 = 5,000,000đ
```

### 4. BOND PLUS (Trái phiếu)

```typescript
// File: pages/services/bondPlus/
interface BondOrder {
  bondCode: string;        // Mã TP
  bondName: string;        // Tên TP
  parValue: number;        // Mệnh giá
  couponRate: number;      // Lãi suất danh nghĩa
  volume: number;          // Số lượng
  orderType: 'BUY' | 'SELL';
  price: number;           // Giá giao dịch (% mệnh giá)
  maturityDate: Date;      // Ngày đáo hạn
}
```

### 5. IPO (Phát hành lần đầu)

```typescript
// File: pages/services/ipo/IPORegistration/
interface IPORegistration {
  symbol: string;
  ipoPrice: number;              // Giá phát hành
  registeredVolume: number;      // Số lượng đăng ký
  registrationDate: Date;
  allocationMethod: 'PRO_RATA' | 'FCFS';
  allocatedVolume?: number;      // Số lượng được phân bổ
  refundAmount?: number;         // Số tiền hoàn lại
}
```

---

## 📝 ORDER TYPES - CÁC LOẠI LỆNH

### Định nghĩa từ codebase

```typescript
// File: types/models/ServicesFilters.ts
export enum SERVICE_FILTER_TYPE {
  ATO = 'ATO',  // At The Open
  ATC = 'ATC',  // At The Close
  LO = 'LO',    // Limit Order
  MP = 'MP',    // Market Price
  MOK = 'MOK',  // Match Or Kill
  MAK = 'MAK',  // Match And Kill
  PLO = 'PLO',  // Post Limit Order
}

export enum SERVICE_FILTER_STATUS {
  PENDING = 'PENDING',       // Chờ khớp
  MATCHED = 'MATCHED',       // Đã khớp
  CANCELLED = 'CANCELLED',   // Đã hủy
  REJECTED = 'REJECTED',     // Bị từ chối
  PARTIAL = 'PARTIAL',       // Khớp một phần
}
```

### Chi tiết từng loại lệnh

#### 1. **LO - Limit Order (Lệnh giới hạn)**
```typescript
const limitOrder = {
  type: 'LO',
  description: 'Đặt lệnh với giá cụ thể',
  example: {
    symbol: 'VNM',
    side: 'BUY',
    price: 85000,
    volume: 100,
    note: 'Chỉ mua nếu giá <= 85,000đ'
  },
  matching: 'Khớp khi giá thị trường phù hợp',
  validity: 'Có thể hủy bất kỳ lúc nào (trong phiên LO)'
};
```

#### 2. **MP - Market Price (Lệnh thị trường)**
```typescript
const marketOrder = {
  type: 'MP',
  description: 'Mua/bán ngay với giá tốt nhất hiện tại',
  example: {
    symbol: 'VNM',
    side: 'BUY',
    volume: 100,
    note: 'Không cần nhập giá, khớp ngay'
  },
  matching: 'Khớp ngay lập tức với giá best bid/ask',
  risk: 'Không kiểm soát được giá chính xác'
};
```

#### 3. **ATO - At The Open**
```typescript
const atoOrder = {
  type: 'ATO',
  description: 'Lệnh khớp ở phiên mở cửa (9:00-9:15)',
  example: {
    symbol: 'VNM',
    side: 'BUY',
    volume: 100,
    time: '08:30', // Đặt trước
    matchTime: '09:15', // Khớp lúc này
  },
  matching: 'Khớp định kỳ một lần, giá khớp duy nhất',
  note: 'Có thể kèm giá giới hạn hoặc không giới hạn'
};
```

#### 4. **ATC - At The Close**
```typescript
const atcOrder = {
  type: 'ATC',
  description: 'Lệnh khớp ở phiên đóng cửa (14:30-14:45)',
  matching: 'Khớp định kỳ cuối ngày',
  useCase: 'Tránh rủi ro giá biến động cuối ngày'
};
```

#### 5. **MOK - Match Or Kill**
```typescript
const mokOrder = {
  type: 'MOK',
  description: 'Khớp hết ngay lập tức hoặc hủy toàn bộ',
  example: {
    symbol: 'VNM',
    volume: 1000,
    note: 'Phải khớp đủ 1000 CP một lần, nếu không đủ → Hủy'
  }
};
```

#### 6. **MAK - Match And Kill**
```typescript
const makOrder = {
  type: 'MAK',
  description: 'Khớp được bao nhiêu, hủy phần còn lại',
  example: {
    symbol: 'VNM',
    volume: 1000,
    matched: 600,
    cancelled: 400,
    note: 'Khớp 600 CP, hủy 400 CP còn lại'
  }
};
```

---

## ⏰ TRADING SESSIONS - PHIÊN GIAO DỊCH

### HOSE Trading Sessions

```typescript
// Từ codebase: sessionMarkets store
interface TradingSession {
  sessionId: 'ATO' | 'CONTINUOUS' | 'ATC' | 'PAUSE' | 'CLOSE';
  time: string;
  allowedOrderTypes: string[];
}

const HOSE_SESSIONS: TradingSession[] = [
  {
    sessionId: 'ATO',
    time: '09:00 - 09:15',
    allowedOrderTypes: ['ATO', 'LO'],
    matching: 'PERIODIC', // Khớp định kỳ
    description: 'Phiên khớp lệnh mở cửa'
  },
  {
    sessionId: 'CONTINUOUS',
    time: '09:15 - 11:30, 13:00 - 14:30',
    allowedOrderTypes: ['LO', 'MP', 'MOK', 'MAK', 'PLO'],
    matching: 'CONTINUOUS', // Khớp liên tục
    description: 'Phiên giao dịch liên tục'
  },
  {
    sessionId: 'ATC',
    time: '14:30 - 14:45',
    allowedOrderTypes: ['ATC', 'LO'],
    matching: 'PERIODIC',
    description: 'Phiên khớp lệnh đóng cửa'
  },
  {
    sessionId: 'PAUSE',
    time: '11:30 - 13:00',
    allowedOrderTypes: [],
    description: 'Nghỉ trưa - Không giao dịch'
  }
];
```

### Session Check trong Code

```typescript
// File: pages/trading/futures/FutureOrdersHistory.tsx
const canCancelOrder = useMemo(() => {
  return (
    selectedOrder &&
    CANCELABLE_ORDER_STATUS.includes(selectedOrder.status) &&
    !['ATO', 'ATC', 'PAUSE'].includes(sessionMarkets['DERIVATIVES']?.sessionId)
  );
}, [sessionMarkets, selectedOrder]);

// Không được hủy lệnh trong phiên ATO, ATC, PAUSE
```

---

## 📊 ORDER BOOK & MATCHING ALGORITHM

### Order Book Structure

```typescript
interface OrderBook {
  symbol: string;
  bids: PriceLevel[];  // Lệnh mua (giá giảm dần)
  asks: PriceLevel[];  // Lệnh bán (giá tăng dần)
  lastPrice: number;
  referencePrice: number; // Giá tham chiếu
  ceiling: number;        // Giá trần
  floor: number;          // Giá sàn
}

interface PriceLevel {
  price: number;
  volume: number;
  orders: number; // Số lệnh ở mức giá này
}

// Ví dụ Order Book
const orderBook: OrderBook = {
  symbol: 'VNM',
  bids: [
    { price: 85.2, volume: 1000, orders: 5 },  // Best bid
    { price: 85.1, volume: 2500, orders: 12 },
    { price: 85.0, volume: 5000, orders: 25 }
  ],
  asks: [
    { price: 85.3, volume: 800, orders: 3 },   // Best ask
    { price: 85.4, volume: 1200, orders: 7 },
    { price: 85.5, volume: 3000, orders: 15 }
  ],
  lastPrice: 85.2,
  referencePrice: 85.0,
  ceiling: 90.95,  // 85 * 1.07
  floor: 79.05     // 85 * 0.93
};
```

### Price-Time Priority Algorithm

```typescript
class OrderMatchingEngine {
  // Thuật toán khớp lệnh: Giá - Thời gian ưu tiên
  match() {
    while (this.canMatch()) {
      const bestBuy = this.buyOrders[0];   // Giá mua cao nhất
      const bestSell = this.sellOrders[0]; // Giá bán thấp nhất

      if (bestBuy.price >= bestSell.price) {
        // Xác định giá khớp
        const matchPrice = bestBuy.timestamp < bestSell.timestamp
          ? bestBuy.price    // Lệnh mua vào trước
          : bestSell.price;  // Lệnh bán vào trước

        const matchVolume = Math.min(bestBuy.volume, bestSell.volume);

        this.executeTrade({
          price: matchPrice,
          volume: matchVolume,
          buyer: bestBuy,
          seller: bestSell
        });

        // Cập nhật hoặc xóa lệnh
        this.updateOrders(bestBuy, bestSell, matchVolume);
      } else {
        break; // Không còn lệnh khớp được
      }
    }
  }
}
```

### Price Board Colors

```typescript
// Từ codebase: getChangeValueColor function
const getPriceColor = (
  currentPrice: number,
  referencePrice: number
): string => {
  const ceiling = referencePrice * 1.07;
  const floor = referencePrice * 0.93;

  if (currentPrice === ceiling) return 'PURPLE';    // Tím - Trần
  if (currentPrice === floor) return 'CYAN';        // Xanh dương - Sàn
  if (currentPrice === referencePrice) return 'YELLOW'; // Vàng - Tham chiếu
  if (currentPrice > referencePrice) return 'GREEN';    // Xanh lá - Tăng
  if (currentPrice < referencePrice) return 'RED';      // Đỏ - Giảm

  return 'WHITE';
};
```

---

## 💰 SETTLEMENT T+2

### Timeline

```typescript
interface TradeSettlement {
  tradeDate: Date;      // T
  settlementDate: Date; // T+2
  status: 'PENDING' | 'SETTLED';
}

// Ví dụ timeline
const trade = {
  // T+0: Thứ 2, 15/01/2024
  T0: {
    date: '2024-01-15',
    action: 'Mua 100 VNM @ 85k',
    cashStatus: 'Chưa trừ tiền',
    stockStatus: 'Chưa nhận CP',
    canSell: false
  },

  // T+1: Thứ 3, 16/01/2024
  T1: {
    date: '2024-01-16',
    action: 'Chờ thanh toán',
    cashStatus: 'Chưa trừ tiền',
    stockStatus: 'Đang chuyển quyền',
    canSell: false
  },

  // T+2: Thứ 4, 17/01/2024
  T2: {
    date: '2024-01-17',
    action: 'Thanh toán hoàn tất',
    cashStatus: 'Trừ 8,500,000đ',
    stockStatus: 'Nhận 100 VNM',
    canSell: true,
    note: 'Sở hữu chính thức, có thể bán'
  }
};
```

### Cash Flow Management

```typescript
interface CashAccount {
  availableCash: number;      // Tiền khả dụng
  blockedCash: number;        // Tiền chờ thanh toán
  unsettledBuyAmount: number; // Mua chờ T+2
  unsettledSellAmount: number;// Bán chờ T+2
}

const calculateCashPosition = (account: CashAccount) => {
  return {
    // Tiền có thể sử dụng ngay
    usableCash: account.availableCash,

    // Tiền sẽ nhận (T+2)
    pendingReceive: account.unsettledSellAmount,

    // Tiền sẽ trả (T+2)
    pendingPay: account.unsettledBuyAmount,

    // Dự kiến sau T+2
    projectedCash: account.availableCash
      + account.unsettledSellAmount
      - account.unsettledBuyAmount
  };
};
```

---

## 🎁 CORPORATE ACTIONS

### 1. Dividend (Chia cổ tức)

```typescript
interface Dividend {
  type: 'CASH' | 'STOCK';
  exDate: Date;           // Ngày chốt quyền
  paymentDate: Date;      // Ngày chi trả
  cashDividend?: number;  // Cổ tức tiền mặt/CP
  stockDividend?: number; // Tỷ lệ chia CP
}

// Ví dụ: VNM chia cổ tức
const vnmDividend: Dividend = {
  type: 'CASH',
  exDate: new Date('2024-06-01'),
  paymentDate: new Date('2024-06-15'),
  cashDividend: 1500, // 1,500đ/CP

  // Nếu có 100 CP VNM
  calculation: {
    holdings: 100,
    totalReceived: 100 * 1500, // 150,000đ
  }
};
```

### 2. Stock Split (Chia tách cổ phiếu)

```typescript
interface StockSplit {
  exDate: Date;
  ratio: number; // Tỷ lệ chia tách

  // 1:2 = 1 CP cũ → 2 CP mới
  before: { volume: number, price: number },
  after: { volume: number, price: number }
}

// Ví dụ: HPG chia tách 1:2
const hpgSplit: StockSplit = {
  exDate: new Date('2024-07-01'),
  ratio: 2,

  before: {
    volume: 100,    // 100 CP
    price: 50000    // @ 50k
    // Tổng giá trị: 5,000,000đ
  },

  after: {
    volume: 200,    // 200 CP
    price: 25000    // @ 25k
    // Tổng giá trị: 5,000,000đ (không đổi)
  }
};
```

### 3. Rights Issue (Phát hành thêm cổ phiếu)

```typescript
interface RightsIssue {
  exDate: Date;
  ratio: number;          // Tỷ lệ: 2:1 = 2 CP cũ mua 1 CP mới
  rightsPrice: number;    // Giá ưu đãi

  calculation: {
    oldShares: number,
    rightsReceived: number,
    investmentRequired: number
  }
}

// Ví dụ: VIC phát hành thêm 2:1
const vicRights: RightsIssue = {
  exDate: new Date('2024-08-01'),
  ratio: 0.5,  // 2 CP cũ được mua 1 CP mới
  rightsPrice: 80000,

  calculation: {
    oldShares: 100,        // Có 100 CP
    rightsReceived: 50,    // 100 / 2 = 50 quyền mua
    investmentRequired: 50 * 80000, // 4,000,000đ

    // Nếu thực hiện quyền:
    afterExercise: {
      totalShares: 150,    // 100 + 50
      avgPrice: 86667      // (100*100k + 50*80k) / 150
    }
  }
};
```

---

## 📡 REAL-TIME DATA & WEBSOCKET

### WebSocket Data Streaming

```typescript
// Từ codebase: live-data-manager
interface TickerData {
  ticker: string;
  lastPrice: number;
  change: number;
  changePercent: number;
  high: number;
  low: number;
  open: number;
  close: number;
  volume: number;
  totalVolume: number;
  bid1: number;   // Best bid
  ask1: number;   // Best ask
  bidVol1: number;
  askVol1: number;
}

// WebSocket subscription
const useSubscribeTickers = (
  channel: TChannel,
  symbols: string[]
) => {
  useEffect(() => {
    const subscriptionId = subscribeLiveData(channel, symbols);

    return () => {
      unsubscribeLiveData(subscriptionId);
    };
  }, [channel, symbols]);
};
```

### Reference Counting Pattern

```typescript
// Từ codebase: useSubTrackerStore
class SubscriptionTracker {
  private subscriptions = new Map<string, number>();

  subscribe(symbol: string) {
    const count = this.subscriptions.get(symbol) || 0;
    this.subscriptions.set(symbol, count + 1);

    if (count === 0) {
      // Lần đầu subscribe → Tạo WebSocket connection
      this.createConnection(symbol);
    }
  }

  unsubscribe(symbol: string) {
    const count = this.subscriptions.get(symbol) || 0;

    if (count <= 1) {
      // Không còn ai dùng → Đóng connection
      this.closeConnection(symbol);
      this.subscriptions.delete(symbol);
    } else {
      this.subscriptions.set(symbol, count - 1);
    }
  }
}
```

---

## 📈 PORTFOLIO MANAGEMENT

### Portfolio Calculation

```typescript
// Từ codebase: equity/accountValue
interface Portfolio {
  positions: Position[];
  cash: number;
  totalAssetValue: number;
  totalMarketValue: number;
  totalCost: number;
  unrealizedPL: number;
  realizedPL: number;
  roi: number;
}

interface Position {
  symbol: string;
  volume: number;
  availableVolume: number;  // Khả dụng (đã qua T+2)
  blockVolume: number;      // Bị chặn (chờ T+2)
  avgPrice: number;
  currentPrice: number;
  marketValue: number;
  unrealizedPL: number;
  unrealizedPLPercent: number;
}

const calculatePortfolio = (
  positions: Position[],
  cash: number
): Portfolio => {
  const totalCost = positions.reduce(
    (sum, pos) => sum + (pos.volume * pos.avgPrice),
    0
  );

  const totalMarketValue = positions.reduce(
    (sum, pos) => sum + (pos.volume * pos.currentPrice),
    0
  );

  const unrealizedPL = totalMarketValue - totalCost;
  const totalAssetValue = totalMarketValue + cash;

  return {
    positions,
    cash,
    totalAssetValue,
    totalMarketValue,
    totalCost,
    unrealizedPL,
    realizedPL: 0, // Từ lịch sử giao dịch
    roi: (unrealizedPL / totalCost) * 100
  };
};
```

---

## ❓ INTERVIEW QUESTIONS

### 1. Domain Knowledge

**Q: Giải thích sự khác biệt giữa LO và MP?**
```
A:
- LO (Limit Order): Đặt giá cụ thể, có thể không khớp
- MP (Market Price): Khớp ngay với giá thị trường, không kiểm soát giá
```

**Q: Tại sao có T+2? Tại sao không T+0?**
```
A:
- T+2 cho phép sàn và VSDC xác nhận giao dịch
- Chuyển quyền sở hữu CP cần thời gian
- Giảm rủi ro thanh toán, đảm bảo an toàn
```

**Q: Margin Call là gì? Khi nào xảy ra?**
```
A:
- Xảy ra khi Margin Ratio < Maintenance Margin (30%)
- Nhà đầu tư phải nộp thêm tiền hoặc bán CP
- Nếu không xử lý: Công ty cưỡng chế bán (Force Sell)
```

### 2. Technical Implementation

**Q: Làm sao handle 1000 ticker updates/giây?**
```typescript
A:
1. Virtual Scrolling (AG Grid, react-window)
2. Selective Subscription (chỉ subscribe visible tickers)
3. Throttling với requestAnimationFrame (60fps)
4. React.memo & Zustand selectors
```

**Q: WebSocket disconnect, làm sao reconnect?**
```typescript
A:
1. Auto-reconnect với Exponential Backoff
2. Lưu subscription state
3. Re-subscribe khi reconnect thành công
4. Hiển thị connection status cho user
```

### 3. System Design

**Q: Thiết kế hệ thống real-time price board cho 1000 concurrent users?**
```
A:
1. WebSocket Gateway với Load Balancer
2. Pub/Sub pattern (Redis, Kafka)
3. Caching (Redis) cho market data
4. Client-side: Virtual scrolling, selective subscription
5. Monitoring: Connection count, message rate
```

---

## 📚 TÀI LIỆU THAM KHẢO CHI TIẾT

1. [EQUITY_TRADING.md](./EQUITY_TRADING.md) - Chi tiết giao dịch cổ phiếu
2. [MARGIN_TRADING.md](./MARGIN_TRADING.md) - Giao dịch ký quỹ chuyên sâu
3. [DERIVATIVES_FUTURES.md](./DERIVATIVES_FUTURES.md) - Phái sinh & Futures
4. [BOND_TRADING.md](./BOND_TRADING.md) - Trái phiếu
5. [IPO_PROCESS.md](./IPO_PROCESS.md) - Quy trình IPO
6. [SETTLEMENT_T2.md](./SETTLEMENT_T2.md) - Thanh toán T+2 chi tiết
7. [WEBSOCKET_REALTIME.md](./WEBSOCKET_REALTIME.md) - Real-time data handling

---

## 🎓 GHI CHÚ

- **Source:** myHSC 4.x Trading Frontend
- **Last Updated:** 2024
- **Maintainer:** Development Team

**Tip:** Đọc code thật, debug thật, hiểu flow thật → Phỏng vấn tự tin!

