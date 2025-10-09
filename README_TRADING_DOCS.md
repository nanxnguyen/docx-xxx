# 📚 TRADING DOMAIN DOCUMENTATION - BỘ TÀI LIỆU CHỨNG KHOÁN

> **Tổng hợp kiến thức domain chứng khoán cho Developer**
>
> Dựa trên myHSC 4.x Trading Frontend Application

---

## 📖 DANH SÁCH TÀI LIỆU

### 🎯 Tài liệu chính

| File | Nội dung | Mức độ | File nguồn |
|------|----------|---------|-----------|
| [**TRADING_DOMAIN_KNOWLEDGE.md**](./TRADING_DOMAIN_KNOWLEDGE.md) | **Tổng quan toàn bộ domain** | ⭐⭐⭐ | All |
| [MARGIN_TRADING.md](./MARGIN_TRADING.md) | Giao dịch ký quỹ (Equity Plus) | ⭐⭐⭐ | `pages/services/equityPlus/` |
| [WEBSOCKET_REALTIME.md](./WEBSOCKET_REALTIME.md) | Real-time data & WebSocket | ⭐⭐⭐ | `lib/live-data-manager/` |

### 📝 Tài liệu bổ sung

| File | Nội dung |
|------|----------|
| [FRONTEND_INTERVIEW_QUESTIONS.md](./FRONTEND_INTERVIEW_QUESTIONS.md) | Câu hỏi phỏng vấn Frontend |
| [DOCKER_BEST_PRACTICES.md](./DOCKER_BEST_PRACTICES.md) | Docker best practices |

---

## 🚀 CÁCH SỬ DỤNG

### 1. Đọc theo thứ tự (Recommended)

```bash
# Bước 1: Đọc tổng quan
📖 TRADING_DOMAIN_KNOWLEDGE.md

# Bước 2: Chọn chủ đề cần học sâu
📖 MARGIN_TRADING.md          # Nếu làm việc với Equity Plus
📖 WEBSOCKET_REALTIME.md      # Nếu làm việc với real-time data

# Bước 3: Practice với code thật
💻 Đọc code trong codebase myHSC
```

### 2. Chuẩn bị phỏng vấn

```bash
# Week 1: Domain Knowledge
- Đọc TRADING_DOMAIN_KNOWLEDGE.md
- Hiểu các khái niệm: Order types, Sessions, Settlement
- Làm bài tập tính toán

# Week 2: Technical Deep Dive
- WEBSOCKET_REALTIME.md
- MARGIN_TRADING.md
- Đọc code thực tế

# Week 3: Practice
- Coding challenges
- System design questions
- Review interview questions trong mỗi file
```

### 3. Tra cứu nhanh

```bash
# Tìm kiếm theo keyword
grep -r "Margin Call" documents/
grep -r "WebSocket" documents/

# Xem định nghĩa interface
grep -r "interface.*Order" documents/
```

---

## 📊 KIẾN THỨC CẦN NẮM

### Level 1: Junior Developer (0-1 năm)

- [ ] Hiểu các loại lệnh: LO, MP, ATO, ATC
- [ ] Biết Order Book là gì
- [ ] Hiểu Trading Sessions
- [ ] Biết WebSocket cơ bản
- [ ] Đọc được code React + TypeScript

**Tài liệu:**
- TRADING_DOMAIN_KNOWLEDGE.md (Sections 1-5)
- WEBSOCKET_REALTIME.md (Section 1)

### Level 2: Mid-level Developer (1-3 năm)

- [ ] Hiểu Margin Trading, Margin Call
- [ ] Biết Settlement T+2 workflow
- [ ] Handle WebSocket reconnection
- [ ] Performance optimization (throttling, virtual scrolling)
- [ ] State management (Zustand, Context)

**Tài liệu:**
- MARGIN_TRADING.md (Full)
- WEBSOCKET_REALTIME.md (Sections 2-4)
- TRADING_DOMAIN_KNOWLEDGE.md (Full)

### Level 3: Senior Developer (3+ năm)

- [ ] System design: Real-time price board architecture
- [ ] Subscription management với reference counting
- [ ] Error handling & fault tolerance
- [ ] Portfolio calculation algorithms
- [ ] Corporate actions handling
- [ ] Security & compliance

**Tài liệu:**
- Tất cả tài liệu
- + Đọc source code production
- + Design docs (nếu có)

---

## 💡 INTERVIEW PREP CHECKLIST

### Domain Knowledge

- [ ] Giải thích được 6 loại order (LO, MP, ATO, ATC, MOK, MAK)
- [ ] Vẽ được Order Book
- [ ] Tính được Margin Ratio
- [ ] Giải thích Margin Call scenario
- [ ] Hiểu Settlement T+2 timeline
- [ ] Biết các Corporate Actions (Dividend, Stock Split, Rights Issue)

### Technical Skills

- [ ] Implement WebSocket connection với reconnection
- [ ] Handle 1000 ticker updates/giây
- [ ] Subscription management với reference counting
- [ ] Virtual scrolling implementation
- [ ] State management optimization
- [ ] Error handling best practices

### Coding Challenges

```typescript
// 1. Calculate Portfolio
calculatePortfolio(positions, cash) → Portfolio

// 2. Margin Ratio
calculateMarginRatio(equity, stockValue) → number

// 3. WebSocket Throttling
throttleUpdates(stream, fps) → throttledStream

// 4. Order Book Matching
matchOrders(buyOrders, sellOrders) → trades[]
```

### System Design

- [ ] Design real-time price board for 1000 users
- [ ] Design WebSocket gateway architecture
- [ ] Design caching strategy for market data
- [ ] Design notification system for Margin Call

---

## 🔗 LIÊN KẾT HỮU ÍCH

### Documentation

- [TypeScript Handbook](https://www.typescriptlang.org/docs/)
- [React Documentation](https://react.dev/)
- [Zustand](https://github.com/pmndrs/zustand)
- [AG Grid](https://www.ag-grid.com/)

### Market Data APIs

- [Binance WebSocket Streams](https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams)
- [WebSocket API MDN](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

### Vietnam Stock Market

- [HSC](https://www.hsc.com.vn/)
- [HOSE](https://www.hsx.vn/)
- [HNX](https://www.hnx.vn/)
- [VSD - Vietnam Securities Depository](https://www.vsd.vn/)

---

## 📝 GHI CHÚ

### Thuật ngữ tiếng Anh - Tiếng Việt

| English | Tiếng Việt |
|---------|------------|
| Equity | Cổ phiếu thường |
| Margin Trading | Giao dịch ký quỹ |
| Derivatives | Phái sinh |
| Futures | Hợp đồng tương lai |
| Settlement | Thanh toán, quyết toán |
| Order Book | Sổ lệnh |
| Bid | Giá mua |
| Ask | Giá bán |
| Spread | Chênh lệch giá mua-bán |
| Ticker | Mã chứng khoán |
| Portfolio | Danh mục đầu tư |
| P&L (Profit & Loss) | Lãi/lỗ |
| Unrealized P&L | Lãi/lỗ chưa chốt |
| Realized P&L | Lãi/lỗ đã chốt |
| Margin Call | Cảnh báo ký quỹ |
| Force Sell | Cưỡng chế bán |
| Collateral | Tài sản đảm bảo |
| Leverage | Đòn bẩy |

### Quy ước trong code

```typescript
// Naming conventions
interface Order { }        // PascalCase for interfaces
const placeOrder = () => {}  // camelCase for functions
const ORDER_STATUS = {}      // UPPER_CASE for constants

// File naming
ComponentName.tsx          // React components
useCustomHook.ts           // React hooks
utils.ts                   // Utility functions
types.ts                   // Type definitions
index.ts                   // Barrel exports

// Comments
// FIXME: Bug cần fix
// TODO: Feature cần thêm
// NOTE: Ghi chú quan trọng
// @deprecated: Code cũ, không dùng nữa
```

---

## 🎓 CONTRIBUTORS

- Development Team - myHSC 4.x
- Trading Domain Experts
- Frontend Engineers

---

## 📅 CHANGELOG

- **2024-10**: Initial documentation
  - TRADING_DOMAIN_KNOWLEDGE.md
  - MARGIN_TRADING.md
  - WEBSOCKET_REALTIME.md

---

## 💬 FEEDBACK

Nếu có câu hỏi hoặc cần bổ sung tài liệu, vui lòng:
1. Tạo issue trong project
2. Hoặc liên hệ team lead

---

**Happy Learning! 🚀**

> "The best way to learn is to read the code, understand the flow, and practice!" - Senior Dev Wisdom

