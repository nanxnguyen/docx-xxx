# 💳 MARGIN TRADING (EQUITY PLUS) - GIAO DỊCH KÝ QUỸ

> **File nguồn:** `pages/services/equityPlus/`
>
> **Mục đích:** Tài liệu chi tiết về giao dịch ký quỹ (vay tiền mua cổ phiếu)

---

## 📋 MỤC LỤC

1. [Khái niệm cơ bản](#khái-niệm-cơ-bản)
2. [Margin Account Structure](#margin-account-structure)
3. [Margin Contract Lifecycle](#margin-contract-lifecycle)
4. [Margin Ratio & Risk Management](#margin-ratio--risk-management)
5. [Use Cases trong myHSC](#use-cases-trong-myhsc)
6. [Interview Questions](#interview-questions)

---

## 🎯 KHÁI NIỆM CƠ BẢN

### Margin Trading là gì?

**Định nghĩa:** Vay tiền từ công ty chứng khoán để mua cổ phiếu, tạo đòn bẩy tài chính.

```typescript
// Ví dụ đơn giản
const normalTrading = {
  capital: 100_000_000,      // Có 100 triệu
  buyingPower: 100_000_000,  // Mua được 100 triệu
  leverage: '1x'
};

const marginTrading = {
  capital: 100_000_000,       // Có 100 triệu
  marginRatio: 0.5,           // Ký quỹ 50%
  buyingPower: 200_000_000,   // Mua được 200 triệu (vay thêm 100tr)
  leverage: '2x',
  risk: 'Cao hơn - Có thể mất nhiều hơn vốn ban đầu'
};
```

### Lợi ích & Rủi ro

**Lợi ích:**
- Tăng sức mua (buying power)
- Đòn bẩy lợi nhuận

**Rủi ro:**
- Đòn bẩy lỗ (loss cũng x2)
- Margin Call
- Force Sell (cưỡng chế bán)
- Lãi vay

---

## 📊 MARGIN ACCOUNT STRUCTURE

### Interface từ codebase

```typescript
// File: pages/services/equityPlus/
interface MarginAccount {
  // Tài sản & Giá trị
  totalEquityAmount: number;      // Tổng tài sản (assets)
  totalLoanAmount: number;        // Tổng nợ vay

  // Ký quỹ
  marginRatio: number;            // Tỷ lệ ký quỹ (radio)
  collateralLimitAmount: number;  // Hạn mức ký quỹ
  extraCredit: number;            // Hạn mức tín dụng thêm

  // Tài sản thừa/thiếu
  excessEquityAmount: number;     // Tài sản thừa (excess)
  deficitEquityAmount: number;    // Tài sản thiếu (deficit)

  // Trạng thái
  accountStatus: 'NORMAL' | 'WARNING' | 'FORCE_SELL';
}
```

### Các chỉ số quan trọng

#### 1. **Total Equity Amount (Tổng tài sản)**

```typescript
const calculateTotalEquity = (
  stockValue: number,     // Giá trị CP
  cash: number,           // Tiền mặt
  loan: number            // Nợ vay
): number => {
  return stockValue + cash - loan;
};

// Ví dụ:
const account = {
  stockValue: 180_000_000,   // CP trị giá 180tr
  cash: 20_000_000,          // Tiền mặt 20tr
  loan: 100_000_000,         // Nợ 100tr

  totalEquity: 180_000_000 + 20_000_000 - 100_000_000, // 100tr
};
```

#### 2. **Margin Ratio (Tỷ lệ ký quỹ)**

```typescript
const calculateMarginRatio = (
  totalEquity: number,
  stockValue: number
): number => {
  return (totalEquity / stockValue) * 100;
};

// Ví dụ:
const marginRatio = (100_000_000 / 200_000_000) * 100; // 50%

// Trong code myHSC:
// File: EquityPlusUpdateCollateral/component/UpdateCollateralRequest.tsx
{
  label: t('Margin Ratio'),
  oldValue: safeNumber(currentValue?.radio) ? `${currentValue?.radio}%` : '-',
  newValue: safeNumber(afterValue?.radio) ? `${afterValue?.radio}%` : '-',
}
```

#### 3. **Excess Equity Amount (Tài sản thừa)**

```typescript
const calculateExcessEquity = (
  totalEquity: number,
  requiredMargin: number    // Ký quỹ duy trì tối thiểu
): number => {
  return totalEquity - requiredMargin;
};

// Nếu > 0: Còn dư, an toàn
// Nếu < 0: Thiếu, nguy hiểm
```

---

## 🔄 MARGIN CONTRACT LIFECYCLE

### 1. Create Contract (Tạo hợp đồng vay)

```typescript
// File: EquityPlusCreateContract/component/CreateContractRequest.tsx
interface CreateMarginContractRequest {
  // Thông tin vay
  loanAmount: number;           // Số tiền vay (principal)
  termDateId: string;           // Kỳ hạn (30, 60, 90 ngày...)
  activeDate: Date;             // Ngày giải ngân

  // Lãi suất
  interestRate: number;         // Lãi suất (%/năm)
  interestPeriodAmount: number; // Lãi kỳ sau thuế

  // Thanh toán
  dueDate: Date;                // Ngày đáo hạn
  totalAmount: number;          // Tổng phải trả (gốc + lãi)
}

// Tính toán lãi
const calculateInterest = (
  principal: number,
  annualRate: number,
  termDays: number
): number => {
  const dailyRate = annualRate / 365;
  const interestBeforeTax = principal * dailyRate * termDays;
  const tax = interestBeforeTax * 0.05; // Thuế 5%
  return interestBeforeTax - tax;
};

// Ví dụ:
const contract = {
  principal: 100_000_000,    // Vay 100tr
  annualRate: 0.12,          // Lãi 12%/năm
  termDays: 90,              // 90 ngày

  interest: calculateInterest(100_000_000, 0.12, 90),
  // = 100tr * (12%/365) * 90 * 0.95 = ~2,815,068đ

  totalAmount: 100_000_000 + 2_815_068, // 102,815,068đ
};
```

### 2. Extend Contract (Gia hạn hợp đồng)

```typescript
// File: EquityPlusExtendContract/
interface ExtendContractRequest {
  contractId: string;
  contractNo: string;
  remainingAmount: number;      // Số tiền còn lại
  period: string;               // Kỳ hạn mới

  // Tính toán lại
  newInterestRate: number;
  newDueDate: Date;
  newTotalAmount: number;
}

// Flow:
// 1. Hợp đồng cũ gần đáo hạn
// 2. Chọn kỳ hạn mới
// 3. Tính lại lãi suất
// 4. Gia hạn (không cần trả gốc ngay)
```

### 3. Settlement Contract (Thanh toán hợp đồng)

```typescript
// File: EquityPlusSettlementContract/
interface SettlementContractRequest {
  contractId: string;
  settlementAmount: number;     // Số tiền thanh toán
  settlementType: 'FULL' | 'PARTIAL';

  // Partial settlement
  remainingPrincipal?: number;
  remainingInterest?: number;
}

// Full Settlement:
const fullSettlement = {
  totalDue: 102_815_068,        // Tổng nợ
  paymentAmount: 102_815_068,   // Trả đủ
  remainingDebt: 0,
  status: 'CLOSED'
};

// Partial Settlement:
const partialSettlement = {
  totalDue: 102_815_068,
  paymentAmount: 50_000_000,    // Trả 1 phần
  remainingDebt: 52_815_068,
  status: 'ACTIVE',
  note: 'Phải trả nốt trước đáo hạn'
};
```

### 4. Update Collateral (Bổ sung tài sản)

```typescript
// File: EquityPlusUpdateCollateral/
interface UpdateCollateralRequest {
  amount: number;               // Số tiền bổ sung
  autoUpdate: boolean;          // Tự động tính toán

  // Before & After comparison
  before: {
    totalEquityAmount: number,
    marginRatio: number,
    excessEquityAmount: number,
    accountStatus: string
  },

  after: {
    totalEquityAmount: number,
    marginRatio: number,
    excessEquityAmount: number,
    accountStatus: string
  }
}

// Use case: Margin Call → Bổ sung tài sản để tránh force sell
```

---

## ⚠️ MARGIN RATIO & RISK MANAGEMENT

### Margin Levels

```typescript
enum MarginLevel {
  SAFE = 'SAFE',           // > 50%
  WARNING = 'WARNING',     // 30% - 50%
  MARGIN_CALL = 'MARGIN_CALL', // < 30%
  FORCE_SELL = 'FORCE_SELL'    // < 20%
}

const getMarginLevel = (marginRatio: number): MarginLevel => {
  if (marginRatio >= 0.5) return MarginLevel.SAFE;
  if (marginRatio >= 0.3) return MarginLevel.WARNING;
  if (marginRatio >= 0.2) return MarginLevel.MARGIN_CALL;
  return MarginLevel.FORCE_SELL;
};
```

### Margin Call Scenario

```typescript
// Kịch bản: Giá CP giảm → Margin Call
const scenario = {
  initial: {
    cash: 100_000_000,
    loan: 100_000_000,
    stockValue: 200_000_000,  // Mua 200tr CP
    totalEquity: 100_000_000, // 200tr - 100tr nợ
    marginRatio: 0.5,         // 50% - An toàn
    status: 'NORMAL'
  },

  afterPriceDown: {
    cash: 100_000_000,
    loan: 100_000_000,
    stockValue: 140_000_000,  // Giá giảm 30%!
    totalEquity: 40_000_000,  // 140tr - 100tr
    marginRatio: 0.286,       // 28.6% - MARGIN CALL!
    status: 'MARGIN_CALL',

    action: {
      option1: 'Nộp thêm tiền',
      option2: 'Bán bớt CP',
      deadline: 'T+1',
      ifNotAction: 'Force Sell by broker'
    }
  },

  solution1_AddCash: {
    addCash: 20_000_000,      // Nộp thêm 20tr
    newTotalEquity: 60_000_000,
    newMarginRatio: 0.429,    // 42.9% - OK
    status: 'WARNING'
  },

  solution2_SellStock: {
    sellStockValue: 40_000_000, // Bán 40tr CP
    newStockValue: 100_000_000,
    newTotalEquity: 40_000_000, // 100tr stock + 40tr cash - 100tr loan
    newMarginRatio: 0.4,        // 40% - OK
    status: 'WARNING'
  }
};
```

### Force Sell Protection

```typescript
// File: EquityPlusUpdateCollateral/component/UpdateCollateralRequest.tsx
const [isForceSell, setIsForceSell] = useState<boolean>(false);

const handleNextStep = () => {
  if (isForceSell) {
    setIsOpenForceSellModal(true);
    return;
  }
  nextStep();
};

// Modal cảnh báo force sell
<ForceSellWarningModal
  open={isOpenForceSellModal}
  onClose={handleCloseForceSellModal}
  message="Tài khoản có nguy cơ bị cưỡng chế bán. Vui lòng bổ sung tài sản."
/>
```

---

## 💡 USE CASES TRONG MYHSC

### 1. Xem thông tin tài khoản Equity Plus

```typescript
// File: EquityPlusAccount/index.tsx
const EquityPlusAccount = () => {
  const equityPlusAccount = useGetEquityPlusAccount();
  const { data: listContractEPActive } = useGetListEPActive({
    accountId: equityPlusAccount?.id || '',
    size: NUMBER_PAGE_SIZE_MAX,
  });

  return (
    <Box>
      <OverviewInfoBox data={equityPlusAccount} />
      <CollateralInfoBox data={equityPlusAccount} />
      <ActiveContractsList contracts={listContractEPActive} />
    </Box>
  );
};
```

### 2. Tạo hợp đồng vay mới

```typescript
// File: EquityPlusCreateContract/
const CreateContractRequest = () => {
  const [loanAmount, setLoanAmount] = useState('');
  const [termDateId, setTermDateId] = useState('');

  const { mutate: calculateAmount } = useCalculateAmount();

  // Debounce calculate để không spam API
  const debounceHandleLoanAmountChange = useCallback(
    debounce((value: string, termId: string) => {
      handleCalculateAmount({ loanAmount: value, termDateId: termId });
    }, DEBOUNCE_DELAY_CHANGE),
    []
  );

  const handleCalculateAmount = ({ termDateId, loanAmount }) => {
    const payload = {
      accountId: equityAccount?.id || '',
      termDateId,
      principal: Number(loanAmount),
      startDate: moment(activeDate).format(ISO_DATE_FORMAT),
      clientTypeCode: userProfile.clientTypeCode,
    };

    calculateAmount(payload, {
      onSuccess: (res) => {
        setValue(EPFormField.DueDate, res.dueDate);
        setValue(EPFormField.TotalAmount, res.totalAmount);
        setValue(EPFormField.InterestPeriodAmount, res.interestAmountAfterTax);
        setValue(EPFormField.InterestRate, res.interestPeriodRate);
      }
    });
  };
};
```

### 3. Xử lý Margin Call

```typescript
const handleMarginCall = (account: MarginAccount) => {
  if (account.marginRatio < 0.3) {
    // Tính số tiền cần bổ sung
    const requiredEquity = account.stockValue * 0.3; // 30% minimum
    const deficit = requiredEquity - account.totalEquityAmount;

    return {
      status: 'MARGIN_CALL',
      deficit,
      actions: [
        {
          type: 'ADD_CASH',
          amount: deficit,
          note: 'Nộp tiền để đưa margin ratio về 30%'
        },
        {
          type: 'SELL_STOCK',
          value: deficit / 0.7,  // Bán CP để giảm nợ
          note: 'Bán CP để giảm tỷ lệ vay'
        }
      ],
      deadline: 'T+1',
      consequence: 'Force sell if not action taken'
    };
  }

  return { status: 'OK' };
};
```

---

## ❓ INTERVIEW QUESTIONS

### Q1: Giải thích Margin Trading vs Normal Trading?

```typescript
Answer:
- Normal: Mua CP bằng 100% tiền của mình
- Margin: Vay tiền công ty CK để mua nhiều CP hơn

Ưu điểm Margin:
- Tăng đòn bẩy (leverage 2x)
- Lợi nhuận cao hơn (nếu giá tăng)

Nhược điểm:
- Rủi ro cao (lỗ cũng x2)
- Phải trả lãi vay
- Có thể bị Margin Call, Force Sell
```

### Q2: Margin Call xảy ra khi nào? Xử lý thế nào?

```typescript
Answer:
Xảy ra khi: Margin Ratio < Maintenance Margin (thường 30%)

Xử lý:
1. Option 1: Nộp thêm tiền
2. Option 2: Bán bớt CP
3. Deadline: T+1
4. Nếu không xử lý: Công ty CK cưỡng chế bán (Force Sell)

Code example:
if (marginRatio < 0.3) {
  showMarginCallWarning();
  calculateRequiredCollateral();
  setDeadline('T+1');
}
```

### Q3: Làm sao tính lãi vay Margin?

```typescript
Answer:
Formula:
lãi = số tiền vay × (lãi suất/365) × số ngày × (1 - thuế 5%)

Ví dụ:
- Vay: 100tr
- Lãi suất: 12%/năm
- Kỳ hạn: 90 ngày
- Lãi = 100tr × (0.12/365) × 90 × 0.95
      = 2,815,068đ

Trong code:
const interest = principal * (annualRate / 365) * termDays * 0.95;
```

### Q4: Force Sell hoạt động như thế nào?

```typescript
Answer:
1. Margin Ratio < 20% (hoặc hết deadline Margin Call)
2. Công ty CK tự động bán CP của khách
3. Bán theo giá thị trường (có thể lỗ)
4. Thu hồi nợ vay
5. Trả lại phần còn lại cho khách (nếu có)

Impact:
- Khách hàng mất quyền kiểm soát
- Có thể bán đúng lúc thị trường giảm
- Lỗ nặng hơn nếu giá thấp

Protect:
- Monitor margin ratio thường xuyên
- Set alert khi < 40%
- Sẵn sàng cash để bổ sung
```

### Q5: Code challenge - Calculate Buying Power

```typescript
Question:
Cho:
- Cash: 100tr
- Current stocks value: 50tr
- Current loan: 20tr
- Margin ratio requirement: 50%

Tính buying power (sức mua)?

Answer:
const calculateBuyingPower = (
  cash: number,
  stockValue: number,
  loan: number,
  marginRatio: number
): number => {
  const totalEquity = stockValue + cash - loan;
  const maxStockValue = totalEquity / marginRatio;
  const currentValue = stockValue + cash;
  const buyingPower = maxStockValue - currentValue;

  return buyingPower;
};

// Solution:
const result = calculateBuyingPower(100_000_000, 50_000_000, 20_000_000, 0.5);

// Total equity = 50tr + 100tr - 20tr = 130tr
// Max stock value = 130tr / 0.5 = 260tr
// Current value = 50tr + 100tr = 150tr
// Buying power = 260tr - 150tr = 110tr

// → Có thể mua thêm 110tr CP
```

---

## 📚 TÀI LIỆU THAM KHẢO

- myHSC Source: `pages/services/equityPlus/`
- HSC Margin Trading Rules
- VSD Regulations on Margin Trading

---

**Note:** Đây là kiến thức thực tế từ codebase production. Hãy hiểu flow, đọc code, và practice!

