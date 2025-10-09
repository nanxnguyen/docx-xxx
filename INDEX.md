# 📚 TRADING DOMAIN DOCUMENTATION INDEX

> **Bộ tài liệu đầy đủ về domain chứng khoán cho Developer**
> 
> **Source:** myHSC 4.x Trading Frontend Application
> 
> **Last Updated:** October 2024

---

## 📖 TÀI LIỆU CHÍNH

### 1. 🎯 [README_TRADING_DOCS.md](./README_TRADING_DOCS.md) - **BẮT ĐẦU TỪ ĐÂY**
   - Hướng dẫn sử dụng bộ tài liệu
   - Lộ trình học tập
   - Checklist chuẩn bị phỏng vấn
   - **Đọc đầu tiên!**

### 2. 📊 [TRADING_DOMAIN_KNOWLEDGE.md](./TRADING_DOMAIN_KNOWLEDGE.md) - **TỔNG QUAN**
   - Kiến thức domain tổng hợp
   - Order types (LO, MP, ATO, ATC, MOK, MAK)
   - Trading sessions
   - Order Book & Matching
   - Settlement T+2
   - Corporate Actions
   - Portfolio Management
   - **File chính, đọc thứ 2**

### 3. 💳 [MARGIN_TRADING.md](./MARGIN_TRADING.md) - **CHUYÊN SÂU**
   - Giao dịch ký quỹ (Equity Plus)
   - Margin Ratio & Risk Management
   - Margin Call scenarios
   - Contract Lifecycle
   - Real examples từ myHSC code
   - **Đọc nếu làm Equity Plus**

### 4. 📡 [WEBSOCKET_REALTIME.md](./WEBSOCKET_REALTIME.md) - **KỸ THUẬT**
   - Real-time data handling
   - WebSocket architecture
   - Subscription management
   - Performance optimization
   - Error handling & Reconnection
   - **Đọc nếu làm real-time features**

### 5. 🧮 [TRADING_FORMULAS.md](./TRADING_FORMULAS.md) - **CÔNG THỨC**
   - Các công thức tính toán quan trọng
   - Price calculations
   - Margin calculations
   - P&L calculations
   - Fees & Taxes
   - Quick reference
   - **Tra cứu khi cần tính toán**

### 6. ❓ [INTERVIEW_QUESTIONS_TRADING.md](./INTERVIEW_QUESTIONS_TRADING.md) - **PHỎNG VẤN**
   - Câu hỏi domain knowledge
   - Câu hỏi technical
   - System design questions
   - Coding challenges
   - Behavioral questions
   - **Đọc trước khi phỏng vấn**

---

## 📚 TÀI LIỆU BỔ SUNG

| File | Nội dung | Liên quan |
|------|----------|-----------|
| [FRONTEND_INTERVIEW_QUESTIONS.md](./FRONTEND_INTERVIEW_QUESTIONS.md) | Câu hỏi phỏng vấn Frontend tổng quát | React, TypeScript, Performance |
| [DOCKER_BEST_PRACTICES.md](./DOCKER_BEST_PRACTICES.md) | Docker best practices | DevOps, Deployment |

---

## 🎯 LỘ TRÌNH HỌC TẬP

### Week 1: Domain Knowledge Fundamentals

```bash
Day 1-2: README_TRADING_DOCS.md
         ↓
Day 3-5: TRADING_DOMAIN_KNOWLEDGE.md (Sections 1-6)
         ↓
Day 6-7: TRADING_FORMULAS.md + Practice calculations
```

**Mục tiêu:** Hiểu các khái niệm cơ bản, order types, sessions

### Week 2: Technical Deep Dive

```bash
Day 1-3: WEBSOCKET_REALTIME.md
         ↓
Day 4-5: MARGIN_TRADING.md
         ↓
Day 6-7: Đọc code thực tế trong myHSC
```

**Mục tiêu:** Hiểu architecture patterns, performance optimization

### Week 3: Interview Preparation

```bash
Day 1-3: INTERVIEW_QUESTIONS_TRADING.md
         ↓
Day 4-5: Practice coding challenges
         ↓
Day 6-7: Mock interviews + System design practice
```

**Mục tiêu:** Sẵn sàng cho phỏng vấn

---

## 📊 KNOWLEDGE TREE

```
Trading Domain Knowledge
├── 1. Market Structure
│   ├── HOSE, HNX, UPCOM
│   ├── VN30, VNINDEX
│   └── Derivatives (VN30F)
│
├── 2. Order Management
│   ├── Order Types (LO, MP, ATO, ATC, MOK, MAK)
│   ├── Order Book
│   ├── Matching Algorithm
│   └── Order Status
│
├── 3. Asset Classes
│   ├── Equity (Cổ phiếu)
│   ├── Margin Trading (Ký quỹ)
│   ├── Derivatives (Phái sinh)
│   ├── Bond (Trái phiếu)
│   └── IPO
│
├── 4. Trading Mechanics
│   ├── Trading Sessions
│   ├── Settlement T+2
│   ├── Fees & Taxes
│   └── Corporate Actions
│
├── 5. Risk Management
│   ├── Margin Ratio
│   ├── Margin Call
│   ├── Force Sell
│   └── Stop Loss / Take Profit
│
├── 6. Portfolio Management
│   ├── Position Tracking
│   ├── P&L Calculation
│   ├── ROI Measurement
│   └── Asset Allocation
│
└── 7. Technical Implementation
    ├── WebSocket Real-time
    ├── State Management
    ├── Performance Optimization
    └── Error Handling
```

---

## 🎓 LEARNING PATHS

### Path 1: Frontend Developer → Trading Frontend

**Prerequisites:** React, TypeScript, State Management

1. ✅ TRADING_DOMAIN_KNOWLEDGE.md
2. ✅ WEBSOCKET_REALTIME.md
3. ✅ TRADING_FORMULAS.md
4. ✅ Practice với myHSC code
5. ✅ INTERVIEW_QUESTIONS_TRADING.md

**Duration:** 2-3 weeks

### Path 2: Backend Developer → Trading Domain Expert

**Prerequisites:** API design, Database, System architecture

1. ✅ TRADING_DOMAIN_KNOWLEDGE.md
2. ✅ MARGIN_TRADING.md
3. ✅ TRADING_FORMULAS.md
4. ✅ System design questions
5. ✅ INTERVIEW_QUESTIONS_TRADING.md

**Duration:** 2 weeks

### Path 3: Junior → Interview Ready

**Full Stack:**

1. ✅ README_TRADING_DOCS.md (Overview)
2. ✅ TRADING_DOMAIN_KNOWLEDGE.md (Full)
3. ✅ TRADING_FORMULAS.md (Practice)
4. ✅ WEBSOCKET_REALTIME.md (Technical)
5. ✅ MARGIN_TRADING.md (Optional)
6. ✅ Code myHSC features
7. ✅ INTERVIEW_QUESTIONS_TRADING.md
8. ✅ Mock interviews

**Duration:** 3-4 weeks

---

## 🔍 QUICK SEARCH

### By Topic

| Topic | Files |
|-------|-------|
| **Order Types** | TRADING_DOMAIN_KNOWLEDGE.md (Section 3) |
| **Margin Trading** | MARGIN_TRADING.md (Full) |
| **WebSocket** | WEBSOCKET_REALTIME.md (Full) |
| **Formulas** | TRADING_FORMULAS.md (All) |
| **Interview Q&A** | INTERVIEW_QUESTIONS_TRADING.md (All) |
| **Settlement** | TRADING_DOMAIN_KNOWLEDGE.md (Section 6) |
| **Corporate Actions** | TRADING_DOMAIN_KNOWLEDGE.md (Section 7) |

### By Code Location

| Feature | Code Path | Documentation |
|---------|-----------|---------------|
| Order Placement | `pages/services/equity/` | TRADING_DOMAIN_KNOWLEDGE.md |
| Margin Account | `pages/services/equityPlus/` | MARGIN_TRADING.md |
| Real-time Data | `lib/live-data-manager/` | WEBSOCKET_REALTIME.md |
| Futures Trading | `pages/trading/futures/` | TRADING_DOMAIN_KNOWLEDGE.md |
| IPO Registration | `pages/services/ipo/` | TRADING_DOMAIN_KNOWLEDGE.md |

---

## 💡 TIPS & BEST PRACTICES

### Reading Tips

1. **Đọc theo thứ tự:** README → TRADING_DOMAIN → Chuyên sâu
2. **Ghi chú:** Viết ra những điểm quan trọng
3. **Code examples:** Chạy thử code examples
4. **Practice:** Làm bài tập trong mỗi file

### Coding Tips

1. **Đọc code production:** Hiểu flow thực tế
2. **Debug:** Chạy app và debug từng bước
3. **Refactor:** Thử refactor một feature nhỏ
4. **Review:** Review code của người khác

### Interview Tips

1. **STAR method:** Structure answers (Situation-Task-Action-Result)
2. **Think aloud:** Nói ra suy nghĩ khi code
3. **Ask questions:** Hỏi khi không hiểu requirements
4. **Draw diagrams:** Vẽ architecture khi system design

---

## 📞 SUPPORT

### Questions?

1. Review tài liệu liên quan
2. Search trong code myHSC
3. Hỏi team lead hoặc senior dev

### Contributing

Nếu phát hiện lỗi hoặc muốn bổ sung:
1. Tạo issue
2. Đề xuất cải tiến
3. Update documentation

---

## 📅 CHANGELOG

### October 2024 - Initial Release

**Files Created:**
- ✅ README_TRADING_DOCS.md
- ✅ TRADING_DOMAIN_KNOWLEDGE.md (22KB)
- ✅ MARGIN_TRADING.md (14KB)
- ✅ WEBSOCKET_REALTIME.md (18KB)
- ✅ TRADING_FORMULAS.md (17KB)
- ✅ INTERVIEW_QUESTIONS_TRADING.md (24KB)
- ✅ INDEX.md (This file)

**Total:** 7 comprehensive documents, ~100KB of knowledge

---

## 🎯 GOALS

- ✅ Comprehensive domain knowledge coverage
- ✅ Real code examples from myHSC
- ✅ Interview preparation materials
- ✅ Quick reference formulas
- ✅ Practical coding challenges

---

## 🌟 FINAL NOTE

> **"The best way to learn trading domain is to:**
> 1. **Read the docs** 📖
> 2. **Understand the code** 💻
> 3. **Practice calculations** 🧮
> 4. **Build features** 🚀
> 5. **Ask questions** ❓"
> 
> — Senior Trading Dev

**Happy Learning! 🎓**

---

**Start your journey:** [README_TRADING_DOCS.md](./README_TRADING_DOCS.md) 👈
