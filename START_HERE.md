# 🚀 START HERE - BẮT ĐẦU TỪ ĐÂY

> **Chào mừng đến với bộ tài liệu Trading Domain Knowledge!**

---

## ⚡ QUICK START

### Bạn đang tìm gì?

#### 📖 Tôi muốn học domain chứng khoán từ đầu
→ **Đọc:** [INDEX.md](./INDEX.md) → [README_TRADING_DOCS.md](./README_TRADING_DOCS.md) → [TRADING_DOMAIN_KNOWLEDGE.md](./TRADING_DOMAIN_KNOWLEDGE.md)

#### 💼 Tôi chuẩn bị phỏng vấn Trading System
→ **Đọc:** [INTERVIEW_QUESTIONS_TRADING.md](./INTERVIEW_QUESTIONS_TRADING.md)

#### 🧮 Tôi cần tra cứu công thức tính toán
→ **Đọc:** [TRADING_FORMULAS.md](./TRADING_FORMULAS.md)

#### 📡 Tôi đang implement WebSocket real-time
→ **Đọc:** [WEBSOCKET_REALTIME.md](./WEBSOCKET_REALTIME.md)

#### 💳 Tôi đang làm tính năng Margin Trading
→ **Đọc:** [MARGIN_TRADING.md](./MARGIN_TRADING.md)

#### 🗺️ Tôi muốn xem toàn bộ tài liệu
→ **Đọc:** [INDEX.md](./INDEX.md)

---

## 📚 BỘ TÀI LIỆU (7 FILES)

### 🎯 Core Documents

1. **[INDEX.md](./INDEX.md)** - Mục lục tổng hợp, lộ trình học tập
2. **[README_TRADING_DOCS.md](./README_TRADING_DOCS.md)** - Hướng dẫn sử dụng bộ tài liệu
3. **[TRADING_DOMAIN_KNOWLEDGE.md](./TRADING_DOMAIN_KNOWLEDGE.md)** (22KB) - Kiến thức domain tổng hợp
4. **[MARGIN_TRADING.md](./MARGIN_TRADING.md)** (14KB) - Giao dịch ký quỹ chuyên sâu
5. **[WEBSOCKET_REALTIME.md](./WEBSOCKET_REALTIME.md)** (18KB) - Real-time data handling
6. **[TRADING_FORMULAS.md](./TRADING_FORMULAS.md)** (11KB) - Công thức tính toán
7. **[INTERVIEW_QUESTIONS_TRADING.md](./INTERVIEW_QUESTIONS_TRADING.md)** (14KB) - Câu hỏi phỏng vấn

**Total:** ~100KB kiến thức domain chứng khoán

---

## 🎯 LỘ TRÌNH ĐỀ XUẤT

### Lộ trình 1: Học từ đầu (3 tuần)

```
Week 1: Fundamentals
├── Day 1-2: INDEX.md + README_TRADING_DOCS.md
├── Day 3-5: TRADING_DOMAIN_KNOWLEDGE.md
└── Day 6-7: TRADING_FORMULAS.md + Practice

Week 2: Technical
├── Day 1-3: WEBSOCKET_REALTIME.md
├── Day 4-5: MARGIN_TRADING.md
└── Day 6-7: Đọc code myHSC

Week 3: Interview Prep
├── Day 1-3: INTERVIEW_QUESTIONS_TRADING.md
├── Day 4-5: Coding challenges
└── Day 6-7: Mock interviews
```

### Lộ trình 2: Chuẩn bị phỏng vấn (1 tuần)

```
Day 1-2: TRADING_DOMAIN_KNOWLEDGE.md (Đọc nhanh)
Day 3-4: INTERVIEW_QUESTIONS_TRADING.md (Focus)
Day 5-6: Practice coding challenges
Day 7: Mock interview
```

### Lộ trình 3: Implement feature (Theo nhu cầu)

```
Implement WebSocket → WEBSOCKET_REALTIME.md
Implement Margin → MARGIN_TRADING.md
Calculate P&L → TRADING_FORMULAS.md
```

---

## 📊 KIẾN THỨC BẮT BUỘC

### Minimum để hiểu code myHSC:

- ✅ Order types: LO, MP, ATO, ATC
- ✅ Trading sessions: ATO, Continuous, ATC
- ✅ Basic WebSocket lifecycle
- ✅ React hooks, Zustand
- ✅ TypeScript interfaces

**File:** TRADING_DOMAIN_KNOWLEDGE.md (Sections 1-5)

### Để phỏng vấn pass:

- ✅ Margin Call, Settlement T+2
- ✅ WebSocket reconnection strategy
- ✅ Performance optimization (throttling, virtual scrolling)
- ✅ System design: Real-time price board

**File:** INTERVIEW_QUESTIONS_TRADING.md

---

## 🔥 TOP 10 CÂU HỎI PHỎNG VẤN

1. Giải thích LO vs MP?
2. Margin Call là gì? Khi nào xảy ra?
3. Settlement T+2 hoạt động thế nào?
4. Làm sao handle 1000 ticker updates/giây?
5. WebSocket reconnection strategy?
6. Memory leak với WebSocket subscriptions?
7. Tính P&L Futures khác gì Equity?
8. Order Book matching algorithm?
9. Design real-time price board cho 1000 users?
10. Giá cổ phiếu dùng Number hay String?

**Chi tiết:** [INTERVIEW_QUESTIONS_TRADING.md](./INTERVIEW_QUESTIONS_TRADING.md)

---

## 🧮 TOP 5 CÔNG THỨC QUAN TRỌNG

1. **Margin Ratio:** `(equity / stockValue) × 100`
2. **Unrealized P&L:** `(current - avg) × volume`
3. **Buying Power:** `equity / marginRatio - currentValue`
4. **Futures P&L:** `(price diff) × qty × 100k`
5. **Break-even Price:** `avgPrice × (1 + fees + tax)`

**Chi tiết:** [TRADING_FORMULAS.md](./TRADING_FORMULAS.md)

---

## 💡 TIPS

### Đọc tài liệu hiệu quả:

1. **Đọc theo thứ tự:** Không skip
2. **Ghi chú:** Viết ra điểm quan trọng
3. **Practice:** Làm code examples
4. **Review:** Đọc lại sau 1 tuần

### Học code myHSC:

1. **Clone repo:** Chạy được local
2. **Debug:** Set breakpoints, follow flow
3. **Modify:** Thử thay đổi code
4. **Document:** Viết note cho bản thân

### Chuẩn bị phỏng vấn:

1. **Domain first:** Hiểu nghiệp vụ
2. **Technical second:** Hiểu implementation
3. **System design:** Vẽ diagrams
4. **Mock interview:** Practice nói

---

## 🎓 LEARNING RESOURCES

### From myHSC Codebase

```typescript
// Real-time data
trading-workspace/apps/trading-frontend/src/lib/live-data-manager/

// Margin trading
trading-workspace/apps/trading-frontend/src/pages/services/equityPlus/

// Order management
trading-workspace/apps/trading-frontend/src/pages/services/equity/

// Futures
trading-workspace/apps/trading-frontend/src/pages/trading/futures/
```

### External Links

- [HSC Website](https://www.hsc.com.vn/)
- [HOSE](https://www.hsx.vn/)
- [WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)
- [AG Grid Docs](https://www.ag-grid.com/)

---

## ✅ CHECKLIST

### Before reading:

- [ ] Clone myHSC repo
- [ ] Setup development environment
- [ ] Open VS Code với source code

### After reading:

- [ ] Hiểu 6 loại order
- [ ] Biết tính Margin Ratio
- [ ] Implement WebSocket với reconnection
- [ ] Pass coding challenges
- [ ] Ready for interview

---

## 🚀 BẮT ĐẦU NGAY

**Recommended starting point:**

```bash
1. Đọc file này (START_HERE.md) ✅
2. Mở INDEX.md để xem overview
3. Đọc README_TRADING_DOCS.md
4. Bắt đầu TRADING_DOMAIN_KNOWLEDGE.md
```

---

## 📞 NEED HELP?

- **Domain questions:** Đọc TRADING_DOMAIN_KNOWLEDGE.md
- **Technical questions:** Đọc WEBSOCKET_REALTIME.md
- **Interview prep:** Đọc INTERVIEW_QUESTIONS_TRADING.md
- **Quick reference:** Đọc TRADING_FORMULAS.md

---

**Good luck! 🍀**

**Next:** [INDEX.md](./INDEX.md) →
