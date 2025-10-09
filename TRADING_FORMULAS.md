# 🧮 TRADING FORMULAS & CALCULATIONS - CÔNG THỨC TÍNH TOÁN

> **Quick reference cho các công thức quan trọng trong Trading System**

---

## 📋 MỤC LỤC

1. [Price & Value](#price--value)
2. [Margin Trading](#margin-trading)
3. [Portfolio & P&L](#portfolio--pl)
4. [Futures](#futures)
5. [Fees & Taxes](#fees--taxes)

---

## 💰 PRICE & VALUE

### 1. Market Value (Giá trị thị trường)

```typescript
marketValue = volume × currentPrice

// Ví dụ:
const position = {
  symbol: 'VNM',
  volume: 100,
  currentPrice: 85000
};

const marketValue = 100 * 85000; // 8,500,000đ
```

### 2. Price Change Percent

```typescript
changePercent = ((currentPrice - referencePrice) / referencePrice) × 100

// Ví dụ:
const vnm = {
  referencePrice: 85000,  // Giá tham chiếu
  currentPrice: 88000     // Giá hiện tại
};

const change = ((88000 - 85000) / 85000) * 100; // +3.53%
```

### 3. Ceiling & Floor Price

```typescript
// HOSE: ±7%
ceiling = referencePrice × 1.07
floor = referencePrice × 0.93

// HNX: ±10%
ceiling = referencePrice × 1.10
floor = referencePrice × 0.90

// Ví dụ HOSE:
const prices = {
  reference: 85000,
  ceiling: 85000 * 1.07,   // 90,950đ
  floor: 85000 * 0.93      // 79,050đ
};
```

### 4. Average Price

```typescript
avgPrice = totalCost / totalVolume

// Ví dụ - Mua nhiều lần:
const trades = [
  { volume: 100, price: 85000 },  // 8,500,000đ
  { volume: 50, price: 87000 },   // 4,350,000đ
  { volume: 150, price: 84000 }   // 12,600,000đ
];

const totalCost = 8_500_000 + 4_350_000 + 12_600_000; // 25,450,000đ
const totalVolume = 100 + 50 + 150; // 300 CP
const avgPrice = 25_450_000 / 300; // 84,833đ/CP
```

---

## 💳 MARGIN TRADING

### 1. Margin Ratio (Tỷ lệ ký quỹ)

```typescript
marginRatio = (totalEquity / totalStockValue) × 100

// Trong đó:
totalEquity = totalStockValue + cash - loan

// Ví dụ:
const account = {
  stockValue: 200_000_000,
  cash: 10_000_000,
  loan: 100_000_000
};

const totalEquity = 200_000_000 + 10_000_000 - 100_000_000; // 110tr
const marginRatio = (110_000_000 / 200_000_000) * 100; // 55%
```

### 2. Buying Power (Sức mua)

```typescript
buyingPower = totalEquity / marginRatio - currentValue

// Với margin ratio requirement = 50%:
const account = {
  totalEquity: 100_000_000,
  currentStockValue: 50_000_000,
  currentCash: 50_000_000,
  marginRatio: 0.5
};

const maxStockValue = 100_000_000 / 0.5; // 200tr
const currentValue = 50_000_000 + 50_000_000; // 100tr
const buyingPower = 200_000_000 - 100_000_000; // 100tr

// Có thể mua thêm 100tr CP
```

### 3. Required Collateral (Tài sản cần bổ sung khi Margin Call)

```typescript
requiredCollateral = (stockValue × maintenanceMargin) - currentEquity

// Ví dụ - Margin Call:
const account = {
  stockValue: 140_000_000,
  currentEquity: 40_000_000,
  maintenanceMargin: 0.3  // 30%
};

const required = (140_000_000 * 0.3) - 40_000_000;
// = 42tr - 40tr = 2tr cần bổ sung
```

### 4. Interest Calculation (Lãi vay)

```typescript
// Lãi kỳ
interest = principal × (annualRate / 365) × days × (1 - taxRate)

// Ví dụ:
const loan = {
  principal: 100_000_000,   // Vay 100tr
  annualRate: 0.12,         // 12%/năm
  days: 90,                 // 90 ngày
  taxRate: 0.05             // Thuế 5%
};

const dailyRate = 0.12 / 365;
const interestBeforeTax = 100_000_000 * dailyRate * 90;
const tax = interestBeforeTax * 0.05;
const interest = interestBeforeTax - tax; // 2,815,068đ

// Tổng phải trả
const totalAmount = 100_000_000 + 2_815_068; // 102,815,068đ
```

### 5. Excess Equity (Tài sản thừa)

```typescript
excessEquity = totalEquity - requiredMargin

// Ví dụ:
const account = {
  totalEquity: 100_000_000,
  stockValue: 150_000_000,
  marginRatio: 0.5
};

const requiredMargin = 150_000_000 * 0.5; // 75tr
const excessEquity = 100_000_000 - 75_000_000; // 25tr thừa
```

---

## 📈 PORTFOLIO & P&L

### 1. Unrealized P&L (Lãi/lỗ chưa chốt)

```typescript
unrealizedPL = (currentPrice - avgPrice) × volume

// Ví dụ:
const position = {
  symbol: 'VNM',
  volume: 100,
  avgPrice: 85000,
  currentPrice: 90000
};

const pl = (90000 - 85000) * 100; // +500,000đ
const plPercent = ((90000 - 85000) / 85000) * 100; // +5.88%
```

### 2. Realized P&L (Lãi/lỗ đã chốt)

```typescript
realizedPL = (sellPrice - avgBuyPrice) × soldVolume - fees

// Ví dụ:
const trade = {
  buyPrice: 85000,
  sellPrice: 90000,
  volume: 100,
  buyFee: 17000,      // 0.2%
  sellFee: 18000,     // 0.2%
  tax: 9000           // 0.1% (sell only)
};

const grossPL = (90000 - 85000) * 100; // 500,000đ
const netPL = grossPL - 17000 - 18000 - 9000; // 456,000đ
```

### 3. Portfolio Total Value

```typescript
totalPortfolioValue = Σ(position.volume × position.currentPrice) + cash

// Ví dụ:
const portfolio = {
  positions: [
    { symbol: 'VNM', volume: 100, currentPrice: 85000 },
    { symbol: 'HPG', volume: 200, currentPrice: 25000 },
    { symbol: 'VIC', volume: 50, currentPrice: 100000 }
  ],
  cash: 50_000_000
};

const stockValue =
  (100 * 85000) +    // VNM: 8,500,000
  (200 * 25000) +    // HPG: 5,000,000
  (50 * 100000);     // VIC: 5,000,000
  // = 18,500,000

const totalValue = 18_500_000 + 50_000_000; // 68,500,000đ
```

### 4. ROI (Return on Investment)

```typescript
roi = (unrealizedPL / totalCost) × 100

// Ví dụ:
const portfolio = {
  totalCost: 20_000_000,      // Vốn bỏ ra
  currentValue: 25_000_000    // Giá trị hiện tại
};

const pl = 25_000_000 - 20_000_000;
const roi = (5_000_000 / 20_000_000) * 100; // +25%
```

---

## 📊 FUTURES

### 1. Futures P&L

```typescript
pl = (currentPrice - avgPrice) × netQty × contractMultiplier

// Ví dụ - Long VN30F:
const position = {
  symbol: 'VN30F2312',
  side: 'LONG',
  avgPrice: 1000,
  currentPrice: 1050,
  netQty: 1,
  contractMultiplier: 100000
};

const pl = (1050 - 1000) * 1 * 100000; // +5,000,000đ
```

### 2. Required Margin (Ký quỹ yêu cầu)

```typescript
requiredMargin = price × volume × contractMultiplier × marginRate

// Ví dụ:
const order = {
  price: 1000,
  volume: 1,
  contractMultiplier: 100000,
  marginRate: 0.2  // 20%
};

const margin = 1000 * 1 * 100000 * 0.2; // 20,000,000đ
```

### 3. Futures Contract Value

```typescript
contractValue = indexPrice × contractMultiplier

// Ví dụ VN30F:
const contract = {
  indexPrice: 1000,
  contractMultiplier: 100000
};

const value = 1000 * 100000; // 100,000,000đ
```

---

## 💸 FEES & TAXES

### 1. Brokerage Fee (Phí môi giới)

```typescript
brokerageFee = orderValue × feeRate

// HOSE:
const fee = {
  buy: orderValue * 0.0015,   // 0.15%
  sell: orderValue * 0.0015   // 0.15%
};

// Ví dụ:
const order = {
  price: 85000,
  volume: 100
};

const orderValue = 85000 * 100; // 8,500,000đ
const buyFee = 8_500_000 * 0.0015; // 12,750đ
```

### 2. Tax (Thuế)

```typescript
// Thuế bán (Sell only)
tax = sellValue × 0.001  // 0.1%

// Ví dụ:
const sell = {
  price: 90000,
  volume: 100
};

const sellValue = 90000 * 100; // 9,000,000đ
const tax = 9_000_000 * 0.001; // 9,000đ
```

### 3. Total Transaction Cost

```typescript
totalCost = orderValue + buyFee

totalProceeds = sellValue - sellFee - tax

netProfit = totalProceeds - totalCost

// Ví dụ đầy đủ:
const trade = {
  // Buy
  buyPrice: 85000,
  buyVolume: 100,
  buyValue: 8_500_000,
  buyFee: 12_750,
  totalCost: 8_512_750,

  // Sell
  sellPrice: 90000,
  sellVolume: 100,
  sellValue: 9_000_000,
  sellFee: 13_500,
  sellTax: 9_000,
  totalProceeds: 8_977_500,

  // P&L
  netProfit: 8_977_500 - 8_512_750  // 464,750đ
};
```

---

## 🎁 CORPORATE ACTIONS

### 1. Cash Dividend

```typescript
totalDividend = holdings × dividendPerShare

// Ví dụ:
const dividend = {
  symbol: 'VNM',
  holdings: 100,
  dividendPerShare: 1500
};

const total = 100 * 1500; // 150,000đ
```

### 2. Stock Split

```typescript
// 1:2 split
newVolume = oldVolume × splitRatio
newPrice = oldPrice / splitRatio

// Ví dụ:
const split = {
  oldVolume: 100,
  oldPrice: 50000,
  splitRatio: 2
};

const newVolume = 100 * 2; // 200 CP
const newPrice = 50000 / 2; // 25,000đ

// Giá trị không đổi:
// Old: 100 × 50k = 5,000,000đ
// New: 200 × 25k = 5,000,000đ ✓
```

### 3. Rights Issue

```typescript
// 2:1 rights (2 cũ mua 1 mới)
rightsReceived = holdings / ratio
investmentRequired = rightsReceived × rightsPrice
newAvgPrice = (oldCost + newCost) / totalVolume

// Ví dụ:
const rights = {
  oldHoldings: 100,
  oldPrice: 100000,
  ratio: 2,
  rightsPrice: 80000
};

const rightsReceived = 100 / 2; // 50 quyền
const newCost = 50 * 80000; // 4,000,000đ
const oldCost = 100 * 100000; // 10,000,000đ
const totalVolume = 100 + 50; // 150 CP
const newAvgPrice = (10_000_000 + 4_000_000) / 150; // 93,333đ/CP
```

---

## 📊 QUICK REFERENCE TABLE

| Công thức | Formula | Ví dụ |
|-----------|---------|-------|
| Market Value | `volume × price` | 100 × 85k = 8.5tr |
| Margin Ratio | `(equity / stockValue) × 100` | (100tr / 200tr) × 100 = 50% |
| Unrealized P&L | `(current - avg) × volume` | (90k - 85k) × 100 = 500k |
| Buy Fee | `value × 0.15%` | 8.5tr × 0.0015 = 12,750đ |
| Sell Tax | `value × 0.1%` | 9tr × 0.001 = 9,000đ |
| Futures P&L | `(price diff) × qty × 100k` | 50 × 1 × 100k = 5tr |

---

## 💡 COMMON CALCULATIONS

### Break-even Price

```typescript
// Tính giá hòa vốn (bao gồm phí)
breakEvenPrice = avgBuyPrice × (1 + buyFeeRate + sellFeeRate + taxRate)

// Ví dụ:
const be = 85000 * (1 + 0.0015 + 0.0015 + 0.001);
// = 85000 × 1.004 = 85,340đ

// Phải bán >= 85,340đ mới có lãi
```

### Position Sizing

```typescript
// Tính số CP có thể mua với vốn cho trước
maxVolume = Math.floor(availableCash / (price × (1 + feeRate)))

// Ví dụ:
const maxVol = Math.floor(10_000_000 / (85000 * 1.0015));
// = Math.floor(10_000_000 / 85_127.5)
// = 117 CP
```

### Stop Loss / Take Profit

```typescript
// Stop loss -5%
stopLoss = avgPrice × (1 - 0.05)

// Take profit +10%
takeProfit = avgPrice × (1 + 0.10)

// Ví dụ:
const trade = {
  avgPrice: 85000,
  stopLoss: 85000 × 0.95,   // 80,750đ
  takeProfit: 85000 × 1.10  // 93,500đ
};
```

---

## 🎯 PRACTICE EXERCISES

### Exercise 1: Portfolio Calculation

```typescript
Given:
- VNM: 100 CP @ avg 85k, current 90k
- HPG: 200 CP @ avg 25k, current 23k
- Cash: 50tr

Calculate:
1. Total market value
2. Unrealized P&L
3. ROI%
```

<details>
<summary>Answer</summary>

```typescript
// 1. Market value
VNM: 100 × 90k = 9,000,000
HPG: 200 × 23k = 4,600,000
Total stock: 13,600,000
Total value: 13,600,000 + 50,000,000 = 63,600,000đ

// 2. Unrealized P&L
VNM: (90k - 85k) × 100 = +500,000
HPG: (23k - 25k) × 200 = -400,000
Total P&L: +100,000đ

// 3. ROI
Cost: (100 × 85k) + (200 × 25k) = 13,500,000
ROI: (100,000 / 13,500,000) × 100 = 0.74%
```
</details>

### Exercise 2: Margin Call

```typescript
Given:
- Stock value: 150tr
- Loan: 100tr
- Cash: 10tr
- Maintenance margin: 30%

Is there a margin call? How much to add?
```

<details>
<summary>Answer</summary>

```typescript
// Total equity
Equity = 150tr + 10tr - 100tr = 60tr

// Margin ratio
Ratio = (60tr / 150tr) × 100 = 40%

// Check
40% > 30% → OK, No margin call! ✓

// If price drops to 120tr:
New equity = 120tr + 10tr - 100tr = 30tr
New ratio = (30tr / 120tr) × 100 = 25% ❌

Required = 120tr × 0.3 = 36tr
Deficit = 36tr - 30tr = 6tr cần bổ sung
```
</details>

---

**Tip:** Lưu file này để tra cứu nhanh khi code hoặc phỏng vấn!

