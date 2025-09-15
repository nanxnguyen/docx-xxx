# 📚 Câu Hỏi Frontend Interview - Từ Cơ Bản Đến Senior

> **Tổng cộng: 23 câu hỏi cơ bản/trung cấp + 6 câu nâng cao + 7 câu React advanced + 10 câu TypeScript + 15 câu CSS/HTML + 9 câu kinh nghiệm = 70 câu hỏi**
>
> **Tất cả examples được viết bằng TypeScript với chú thích tiếng Việt**

## 🚀 **Quick Navigation**
- 📋 [Mục Lục Tổng Kết](#📋-mục-lục-tổng-kết)
- 🟢 [Câu Hỏi Cơ Bản](#câu-hỏi-cơ-bản-junior-level)
- 🟡 [Câu Hỏi Trung Cấp](#câu-hỏi-trung-cấp-mid-level)
- 🔴 [Câu Hỏi Nâng Cao](#câu-hỏi-nâng-cao-senior-level)
- 🚀 [React Advanced Topics](#🚀-react-advanced-topics--modern-features---7-câu)
- 💙 [TypeScript Advanced](#💙-typescript-advanced-topics)
- 🎨 [CSS & HTML Advanced](#🎨-css--html-advanced-topics)
- 💼 [Câu Hỏi Kinh Nghiệm](#💼-câu-hỏi-kinh-nghiệm--thực-tế)

## 📋 Mục Lục Tổng Kết

> **💡 TIP:** Click vào bất kỳ câu hỏi nào để jump trực tiếp đến nội dung. Sử dụng "Back to Top" để quay lại đây!

### 🟢 **Câu Hỏi Cơ Bản (Junior Level) - 16 câu**

#### **JavaScript Core Fundamentals (12 câu)**
- **[Q1](#q1-primitive-values-vs-reference-values-trong-javascript)**: Primitive Values vs Reference Values trong JavaScript?
- **[Q2](#q2-sự-khác-biệt-giữa-var-let-và-const)**: Sự khác biệt giữa `var`, `let`, và `const`?
- **[Q3](#q3-es5-vs-es6-features-và-modern-javascript)**: ES5 vs ES6+ features và modern JavaScript?
- **[Q4](#q4-hoisting-trong-javascript---cách-hoạt-động)**: Hoisting trong JavaScript - Cách hoạt động?
- **[Q5](#q5-event-loop-hoạt-động-như-thế-nào-giải-thích-đơn-giản)**: Event Loop hoạt động như thế nào? (Giải thích đơn giản)
- **[Q6](#q6-closure-và-data-privacy-trong-javascript)**: Closure và Data Privacy trong JavaScript?
- **[Q7](#q7-dom-và-event-handling-chi-tiết)**: DOM và Event Handling chi tiết?
- **[Q8](#q8-falsytruthy--vs--null-vs-undefined)**: Falsy/Truthy, == vs ===, null vs undefined?
- **[Q10](#q10-arrow-functions-vs-regular-functions-và-this-binding)**: Arrow Functions vs Regular Functions và `this` binding?
- **[Q11](#q11-asyncawait-vs-promises-vs-callbacks)**: Async/Await vs Promises vs Callbacks?
- **[Q12](#q12-cách-remove-property-từ-object-và-so-sánh-objects)**: Cách remove property từ object và so sánh objects?
- **[Q14](#q14-loop-performance-và-browser-rendering-paint-repaint-reflow)**: Loop Performance và Browser Rendering (Paint, Repaint, Reflow)?
- **[Q15](#q15-axios-interceptors-và-advanced-error-handling)**: Axios Interceptors và Advanced Error Handling?
- **[Q16](#q16-strict-mode-và-javascript-classes)**: Strict Mode và JavaScript Classes?

#### **React Fundamentals (7 câu)**
- **[Q17](#q17-react-hooks-chi-tiết---usestate-useeffect-useref)**: React Hooks chi tiết - useState, useEffect, useRef?
- **[Q18](#q18-component-lifecycle-và-useeffect-coverage)**: Component Lifecycle và useEffect coverage?
- **[Q19](#q19-purecomponent-vs-reactmemo-và-optimization)**: PureComponent vs React.memo và optimization?
- **[Q20](#q20-virtual-dom-và-key-trong-lists)**: Virtual DOM và Key trong Lists?
- **[Q21](#q21-useref-vs-usestate-state-vs-props)**: useRef vs useState, state vs props?
- **[Q22](#q22-usememo-vs-usecallback-chi-tiết)**: useMemo vs useCallback chi tiết?
- **[Q23](#q23-parent-re-renders-thì-child-có-re-render-cách-optimize)**: Parent re-renders thì child có re-render? Cách optimize?

### 🟡 **Câu Hỏi Trung Cấp (Mid-Level) - 7 câu**
- **[Q4](#q4-usestate-hook-hoạt-động-như-thế-nào)**: useState Hook hoạt động như thế nào?
- **[Q5](#q5-useeffect-hook-và-lifecycle-methods-tương-ứng)**: useEffect Hook và lifecycle methods tương ứng?
- **[Q6](#q6-custom-hooks---cách-tạo-và-sử-dụng)**: Custom Hooks - Cách tạo và sử dụng?
- **[Q7](#q7-context-api-vs-redux---khi-nào-nên-sử-dụng)**: Context API vs Redux - Khi nào nên sử dụng?
- **[Q8](#q8-reactmemo-usememo-usecallback---khi-nào-và-cách-sử-dụng)**: React.memo, useMemo, useCallback - Khi nào và cách sử dụng?
- **[Q9](#q9-code-splitting-và-lazy-loading-trong-react)**: Code Splitting và Lazy Loading trong React?
- **[Q10](#q10-higher-order-components-hoc-vs-render-props-vs-custom-hooks)**: Higher-Order Components (HOC) vs Render Props vs Custom Hooks?

### 🔴 **Câu Hỏi Nâng Cao (Senior/Expert Level) - 6 câu**
- **[Q16](#q16-thiết-kế-kiến-trúc-micro-frontend-cho-ứng-dụng-scale-lớn)**: Thiết kế kiến trúc Micro-frontend cho ứng dụng scale lớn?
- **[Q17](#q17-implement-advanced-caching-strategies-cho-production-apps)**: Implement advanced caching strategies cho production apps?
- **[Q18](#q18-design-pattern-cho-large-scale-react-applications)**: Design Pattern cho large-scale React applications?
- **[Q19](#q19-memory-leaks-detection-và-optimization-trong-react-apps)**: Memory leaks detection và optimization trong React apps?
- **[Q20](#q20-implement-comprehensive-security-measures-cho-frontend-apps)**: Implement comprehensive security measures cho frontend apps?
- **[Q21](#q21-advanced-debugging-và-production-monitoring)**: Advanced debugging và production monitoring?

### 🚀 **React Advanced Topics & Modern Features - 7 câu**
- **[Q24](#q24-react-concurrent-mode-và-suspense---cách-hoạt-động-và-ứng-dụng)**: React Concurrent Mode và Suspense - Cách hoạt động và ứng dụng?
- **[Q25](#q25-react-18-features-và-migration-strategies)**: React 18 features và migration strategies?
- **[Q26](#q26-solid-principles-áp-dụng-trong-react-components)**: SOLID principles áp dụng trong React components?
- **[Q27](#q27-code-organization-và-folder-structure-cho-large-react-apps)**: Code organization và folder structure cho large React apps?
- **[Q28](#q28-deep-dive-react-performance-optimization-techniques)**: Deep dive React performance optimization techniques?
- **[Q29](#q29-testing-strategies-cho-react-applications)**: Testing strategies cho React applications?
- **[Q30](#q30-accessibility-a11y-best-practices-trong-react)**: Accessibility (A11y) best practices trong React?

### 💙 **TypeScript Advanced Topics - 10 câu**
- **[TS1](#ts1-utility-types-trong-typescript---cách-sử-dụng-và-ứng-dụng)**: Utility Types trong TypeScript - Cách sử dụng và ứng dụng?
- **[TS2](#ts2-as-const-vs-enum---khi-nào-sử-dụng-cái-nào)**: `as const` vs `enum` - Khi nào sử dụng cái nào?
- **[TS3](#ts3-type-vs-interface---sự-khác-biệt-và-best-practices)**: `type` vs `interface` - Sự khác biệt và best practices?
- **[TS4](#ts4-browser-có-thể-chạy-typescript-không---tại-sao)**: Browser có thể chạy TypeScript không? Tại sao?
- **[TS5](#ts5-type-narrowing-trong-typescript---cách-hoạt-động)**: Type Narrowing trong TypeScript - Cách hoạt động?
- **[TS6](#ts6-unknown-vs-any---sự-khác-biệt-và-khi-nào-sử-dụng)**: `unknown` vs `any` - Sự khác biệt và khi nào sử dụng?
- **[TS7](#ts7-decorator-trong-typescript---khái-niệm-và-ứng-dụng)**: Decorator trong TypeScript - Khái niệm và ứng dụng?
- **[TS8](#ts8-generics-trong-typescript---concept-và-examples)**: Generics trong TypeScript - Concept và Examples?
- **[TS9](#ts9-static-typing-typeof-keyof---advanced-type-operations)**: Static Typing, `typeof`, `keyof` - Advanced Type Operations?
- **[TS10](#ts10-oop-trong-typescript---abstract-class-implement-extend)**: OOP trong TypeScript - Abstract Class, Implement, Extend?

### 🎨 **CSS & HTML Advanced Topics - 15 câu**
- **[CSS1](#css1-em-rem-vs-px---khi-nào-sử-dụng-cái-nào)**: `em` (parent) vs `rem` (root) vs `px` - Khi nào sử dụng cái nào?
- **[CSS2](#css2-css-solutions---module-css-styled-components-inline-styles)**: CSS Solutions - Module CSS, Styled Components, Inline Styles?
- **[CSS3](#css3-css-specificity---cách-tính-và-best-practices)**: CSS Specificity - Cách tính và best practices?
- **[CSS4](#css4-position-absolute-vs-relative-vs-static-vs-fixed)**: Position: absolute vs relative vs static vs fixed?
- **[CSS5](#css5-css-variables-vs-scss-vs-bem-methodology)**: CSS Variables vs SCSS vs BEM Methodology?
- **[CSS6](#css6-div-vs-span---semantic-differences-và-use-cases)**: `div` vs `span` - Semantic differences và use cases?
- **[CSS7](#css7-margin-vs-padding-và-box-model-concepts)**: Margin vs Padding và Box Model concepts?
- **[CSS8](#css8-build-theme-system---css-variables-và-design-tokens)**: Build Theme System - CSS Variables và Design Tokens?
- **[CSS9](#css9-css-reset-vs-normalize---tại-sao-cần-và-cách-sử-dụng)**: CSS Reset vs Normalize - Tại sao cần và cách sử dụng?
- **[CSS10](#css10-pseudo-classes-và-pseudo-elements-trong-css)**: Pseudo-classes và Pseudo-elements trong CSS?
- **[CSS11](#css11-display-none-vs-visibility-hidden---performance-impact)**: `display: none` vs `visibility: hidden` - Performance Impact?
- **[CSS12](#css12-flexbox-vs-css-grid---khi-nào-sử-dụng-cái-nào)**: Flexbox vs CSS Grid - Khi nào sử dụng cái nào?
- **[CSS13](#css13-css-frameworks---tailwind-vs-mui-vs-ant-design)**: CSS Frameworks - Tailwind vs MUI vs Ant Design?
- **[CSS14](#css14-html5-semantic-elements---modern-web-standards)**: HTML5 Semantic Elements - Modern Web Standards?
- **[CSS15](#css15-script-defer-vs-async---performance-optimization)**: Script `defer` vs `async` - Performance Optimization?

## 🎯 **Phân loại theo chủ đề:**

### **JavaScript Core (13 câu)**
[Q1](#q1-primitive-values-vs-reference-values-trong-javascript), [Q2](#q2-sự-khác-biệt-giữa-var-let-và-const), [Q3](#q3-es5-vs-es6-features-và-modern-javascript), [Q4](#q4-hoisting-trong-javascript---cách-hoạt-động), [Q5](#q5-event-loop-hoạt-động-như-thế-nào-giải-thích-đơn-giản), [Q6](#q6-closure-và-data-privacy-trong-javascript), [Q7](#q7-dom-và-event-handling-chi-tiết), [Q8](#q8-falsytruthy--vs--null-vs-undefined), [Q10](#q10-arrow-functions-vs-regular-functions-và-this-binding), [Q11](#q11-asyncawait-vs-promises-vs-callbacks), [Q12](#q12-cách-remove-property-từ-object-và-so-sánh-objects), [Q14](#q14-loop-performance-và-browser-rendering-paint-repaint-reflow), [Q15](#q15-axios-interceptors-và-advanced-error-handling), [Q16](#q16-strict-mode-và-javascript-classes)

### **React Hooks & State Management (11 câu)**
**Junior Level:** [Q17](#q17-react-hooks-chi-tiết---usestate-useeffect-useref), [Q18](#q18-component-lifecycle-và-useeffect-coverage), [Q19](#q19-purecomponent-vs-reactmemo-và-optimization), [Q21](#q21-useref-vs-usestate-state-vs-props), [Q22](#q22-usememo-vs-usecallback-chi-tiết), [Q23](#q23-parent-re-renders-thì-child-có-re-render-cách-optimize)

**Mid Level:** [Q4-Mid](#q4-usestate-hook-hoạt-động-như-thế-nào), [Q5-Mid](#q5-useeffect-hook-và-lifecycle-methods-tương-ứng), [Q6-Mid](#q6-custom-hooks---cách-tạo-và-sử-dụng), [Q7-Mid](#q7-context-api-vs-redux---khi-nào-nên-sử-dụng), [Q8-Mid](#q8-reactmemo-usememo-usecallback---khi-nào-và-cách-sử-dụng)

### **React Performance & Optimization (6 câu)**
**Junior:** [Q19](#q19-purecomponent-vs-reactmemo-và-optimization), [Q20](#q20-virtual-dom-và-key-trong-lists), [Q22](#q22-usememo-vs-usecallback-chi-tiết), [Q23](#q23-parent-re-renders-thì-child-có-re-render-cách-optimize)

**Expert:** [Q19-Expert](#q19-memory-leaks-detection-và-optimization-trong-react-apps), [Q28](#q28-deep-dive-react-performance-optimization-techniques)

### **Architecture & Patterns (7 câu)**
**Mid Level:** [Q9-Mid](#q9-code-splitting-và-lazy-loading-trong-react), [Q10-Mid](#q10-higher-order-components-hoc-vs-render-props-vs-custom-hooks)

**Senior/Expert:** [Q16-Expert](#q16-thiết-kế-kiến-trúc-micro-frontend-cho-ứng-dụng-scale-lớn), [Q18-Expert](#q18-design-pattern-cho-large-scale-react-applications)

**Advanced:** [Q24](#q24-react-concurrent-mode-và-suspense---cách-hoạt-động-và-ứng-dụng), [Q26](#q26-solid-principles-áp-dụng-trong-react-components), [Q27](#q27-code-organization-và-folder-structure-cho-large-react-apps)

### **Security & Testing (4 câu)**
**Expert:** [Q20-Expert](#q20-implement-comprehensive-security-measures-cho-frontend-apps), [Q21-Expert](#q21-advanced-debugging-và-production-monitoring)

**Advanced:** [Q29](#q29-testing-strategies-cho-react-applications), [Q30](#q30-accessibility-a11y-best-practices-trong-react)

### **Advanced React Features (7 câu)**
[Q24](#q24-react-concurrent-mode-và-suspense---cách-hoạt-động-và-ứng-dụng), [Q25](#q25-react-18-features-và-migration-strategies), [Q26](#q26-solid-principles-áp-dụng-trong-react-components), [Q27](#q27-code-organization-và-folder-structure-cho-large-react-apps), [Q28](#q28-deep-dive-react-performance-optimization-techniques), [Q29](#q29-testing-strategies-cho-react-applications), [Q30](#q30-accessibility-a11y-best-practices-trong-react)

### **TypeScript Advanced (10 câu)**
[TS1](#ts1-utility-types-trong-typescript---cách-sử-dụng-và-ứng-dụng), [TS2](#ts2-as-const-vs-enum---khi-nào-sử-dụng-cái-nào), [TS3](#ts3-type-vs-interface---sự-khác-biệt-và-best-practices), [TS4](#ts4-browser-có-thể-chạy-typescript-không---tại-sao), [TS5](#ts5-type-narrowing-trong-typescript---cách-hoạt-động), [TS6](#ts6-unknown-vs-any---sự-khác-biệt-và-khi-nào-sử-dụng), [TS7](#ts7-decorator-trong-typescript---khái-niệm-và-ứng-dụng), [TS8](#ts8-generics-trong-typescript---concept-và-examples), [TS9](#ts9-static-typing-typeof-keyof---advanced-type-operations), [TS10](#ts10-oop-trong-typescript---abstract-class-implement-extend)

### **CSS & HTML Advanced (15 câu)**
[CSS1](#css1-em-rem-vs-px---khi-nào-sử-dụng-cái-nào), [CSS2](#css2-css-solutions---module-css-styled-components-inline-styles), [CSS3](#css3-css-specificity---cách-tính-và-best-practices), [CSS4](#css4-position-absolute-vs-relative-vs-static-vs-fixed), [CSS5](#css5-css-variables-vs-scss-vs-bem-methodology), [CSS6](#css6-div-vs-span---semantic-differences-và-use-cases), [CSS7](#css7-margin-vs-padding-và-box-model-concepts), [CSS8](#css8-build-theme-system---css-variables-và-design-tokens), [CSS9](#css9-css-reset-vs-normalize---tại-sao-cần-và-cách-sử-dụng), [CSS10](#css10-pseudo-classes-và-pseudo-elements-trong-css), [CSS11](#css11-display-none-vs-visibility-hidden---performance-impact), [CSS12](#css12-flexbox-vs-css-grid---khi-nào-sử-dụng-cái-nào), [CSS13](#css13-css-frameworks---tailwind-vs-mui-vs-ant-design), [CSS14](#css14-html5-semantic-elements---modern-web-standards), [CSS15](#css15-script-defer-vs-async---performance-optimization)

### **Experience & Practical (9 câu)**
[EXP1](#exp1-mô-tả-dự-án-frontend-phức-tạp-nhất-bạn-từng-làm), [EXP2](#exp2-xử-lý-performance-issue-trong-production-như-thế-nào), [EXP3](#exp3-debugging-và-troubleshooting-trong-môi-trường-thực-tế), [EXP4](#exp4-làm-việc-với-team-và-code-review-process), [EXP5](#exp5-migration-và-upgrade-project-strategies), [EXP6](#exp6-xử-lý-legacy-code-và-technical-debt), [EXP7](#exp7-production-deployment-và-monitoring-experience), [EXP8](#exp8-những-thách-thức-lớn-nhất-khi-scale-application), [EXP9](#exp9-trend-và-technologies-mới-bạn-quan-tâm)

---

## 💼 **Câu Hỏi Kinh Nghiệm & Thực Tế (9 câu)**
- **[EXP1](#exp1-mô-tả-dự-án-frontend-phức-tạp-nhất-bạn-từng-làm)**: Mô tả dự án frontend phức tạp nhất bạn từng làm?
- **[EXP2](#exp2-xử-lý-performance-issue-trong-production-như-thế-nào)**: Xử lý performance issue trong production như thế nào?
- **[EXP3](#exp3-debugging-và-troubleshooting-trong-môi-trường-thực-tế)**: Debugging và troubleshooting trong môi trường thực tế?
- **[EXP4](#exp4-làm-việc-với-team-và-code-review-process)**: Làm việc với team và code review process?
- **[EXP5](#exp5-migration-và-upgrade-project-strategies)**: Migration và upgrade project strategies?
- **[EXP6](#exp6-xử-lý-legacy-code-và-technical-debt)**: Xử lý legacy code và technical debt?
- **[EXP7](#exp7-production-deployment-và-monitoring-experience)**: Production deployment và monitoring experience?
- **[EXP8](#exp8-những-thách-thức-lớn-nhất-khi-scale-application)**: Những thách thức lớn nhất khi scale application?
- **[EXP9](#exp9-trend-và-technologies-mới-bạn-quan-tâm)**: Trend và technologies mới bạn quan tâm?


## Other
NPM và các thư viện dùng cho frontend phổ biến và tin cậy, giới thiệu các nhiều các tốt
JS: lodash,
mã hoá: crtypro, bryppt,....
drag: ...,
image,...
hook: ...
Theme:,...

---

## Câu Hỏi Cơ Bản (Junior Level)

**📌 [⬆️ Back to Top](#📚-câu-hỏi-frontend-interview---từ-cơ-bản-đến-senior) | [📋 Mục Lục](#📋-mục-lục-tổng-kết)**

### 1. JavaScript Core Fundamentals

#### Q1: Primitive Values vs Reference Values trong JavaScript?

**Trả lời:**

**💡 Khái niệm cốt lõi:**
- **🔢 Primitive Values (Kiểu nguyên thủy)**:
  - 📦 **Lưu trữ theo GIÁ TRỊ** (pass by value)
  - 🔒 **IMMUTABLE** - không thể thay đổi
  - 📍 **Stored in STACK** - truy cập nhanh
- **🏠 Reference Values (Kiểu tham chiếu)**:
  - 📮 **Lưu trữ theo ĐỊA CHỈ** (pass by reference)
  - 🔓 **MUTABLE** - có thể thay đổi
  - 🗄️ **Stored in HEAP** - linh hoạt nhưng chậm hơn

**🧠 GHI NHỚ:**
- **Primitive = Copy the VALUE** 📄→📄
- **Reference = Copy the ADDRESS** 📮→📮

```typescript
// 1. Primitive Values (Kiểu nguyên thủy)
// Bao gồm: number, string, boolean, null, undefined, symbol, bigint
let a: number = 5;
let b: number = a; // Sao chép giá trị (không phải tham chiếu)
a = 10;
console.log(a, b); // 10, 5 - b không bị ảnh hưởng

let str1: string = "hello";
let str2: string = str1; // Sao chép giá trị
str1 = "world";
console.log(str1, str2); // "world", "hello" - str2 không đổi

// 2. Reference Values (Kiểu tham chiếu)
// Bao gồm: object, array, function, Date, RegExp...
interface User {
  name: string;
  age?: number;
}

let obj1: User = { name: "John" };
let obj2: User = obj1; // Sao chép tham chiếu (không phải giá trị)
obj1.name = "Jane";
console.log(obj1.name, obj2.name); // "Jane", "Jane" - cả 2 đều thay đổi

let arr1: number[] = [1, 2, 3];
let arr2: number[] = arr1; // Sao chép tham chiếu
arr1.push(4);
console.log(arr1, arr2); // [1,2,3,4], [1,2,3,4] - cả 2 đều thay đổi

// 3. Shallow Copy vs Deep Copy
// Shallow Copy (Sao chép nông) - chỉ sao chép cấp đầu tiên
interface Address {
  street: string;
  city: string;
}

interface UserProfile {
  name: string;
  address: Address;
  hobbies: string[];
}

const original: UserProfile = {
  name: "John",
  address: {
    street: "123 Main St",
    city: "NYC"
  },
  hobbies: ["reading", "coding"]
};

// Các cách Shallow Copy
const shallowCopy1: UserProfile = { ...original }; // Spread operator
const shallowCopy2: UserProfile = Object.assign({}, original);

shallowCopy1.name = "Jane"; // ✅ OK - không ảnh hưởng original
shallowCopy1.address.city = "LA"; // ❌ Vấn đề - ảnh hưởng original
console.log(original.address.city); // "LA" - đã bị thay đổi vì address là reference

// Deep Copy methods (Sao chép sâu)
// Method 1: JSON (hạn chế - không hoạt động với functions, dates, undefined...)
const deepCopy1: UserProfile = JSON.parse(JSON.stringify(original));

// Method 2: Custom recursive function
function deepCopy<T>(obj: T): T {
  if (obj === null || typeof obj !== "object") return obj;

  if (obj instanceof Date) return new Date(obj.getTime());
  if (obj instanceof Array) return obj.map(item => deepCopy(item));

  if (typeof obj === "object") {
    const copy = {};
    Object.keys(obj).forEach(key => {
      copy[key] = deepCopy(obj[key]);
    });
    return copy;
  }
}

const deepCopy2 = deepCopy(original);

// Method 3: Using Lodash
// const deepCopy3 = _.cloneDeep(original);

// Method 4: Using structuredClone (modern browsers)
const deepCopy4 = structuredClone(original);

// Test deep copy
deepCopy2.address.city = "Chicago";
console.log(original.address.city); // "NYC" - không bị ảnh hưởng

// 4. Spread Operator (...) Use Cases
// Array spreading
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2]; // [1,2,3,4,5,6]

// Object spreading
const obj1 = { a: 1, b: 2 };
const obj2 = { c: 3, d: 4 };
const combined = { ...obj1, ...obj2 }; // {a:1, b:2, c:3, d:4}

// Function arguments
function sum(a, b, c) {
  return a + b + c;
}
const numbers = [1, 2, 3];
console.log(sum(...numbers)); // 6

// Copying arrays/objects (shallow)
const originalArray = [1, 2, 3];
const copiedArray = [...originalArray];

// Rest parameters
function collectArgs(first, ...rest) {
  console.log(first); // 1
  console.log(rest);  // [2, 3, 4, 5]
}
collectArgs(1, 2, 3, 4, 5);

// Destructuring with rest
const [first, second, ...others] = [1, 2, 3, 4, 5];
console.log(others); // [3, 4, 5]

const { name, ...restProps } = { name: "John", age: 30, city: "NYC" };
console.log(restProps); // { age: 30, city: "NYC" }
```

#### Q2: Sự khác biệt giữa `var`, `let`, và `const`?

**Trả lời:**

**📊 So sánh nhanh:**

| Đặc điểm | `var` | `let` | `const` |
|----------|-------|-------|---------|
| **🏠 Scope** | Function | Block | Block |
| **⬆️ Hoisting** | ✅ undefined | ❌ TDZ | ❌ TDZ |
| **🔄 Re-declare** | ✅ Được | ❌ Error | ❌ Error |
| **✏️ Re-assign** | ✅ Được | ✅ Được | ❌ Error |
| **⚡ TDZ** | ❌ Không | ✅ Có | ✅ Có |

**🧠 GHI NHỚ:**
- **`var`** = **V**ery **A**nnoyíng **R**ules (cũ, tránh dùng)
- **`let`** = **L**et me change **E**verything **T**ime (có thể thay đổi)
- **`const`** = **CONST**ant (không đổi, nhưng object bên trong có thể đổi)

```typescript
// var example - Function-scoped và có hoisting
function varExample(): void {
  console.log(x); // undefined (biến đã được hoisted nhưng chưa assign giá trị)
  var x: number = 1;
  if (true) {
    var x = 2; // same variable
  }
  console.log(x); // 2
}

// let example - Block-scoped với temporal dead zone
function letExample(): void {
  // console.log(y); // ReferenceError: Cannot access 'y' before initialization
  let y: number = 1;
  if (true) {
    let y: number = 2; // Biến khác (block scope khác nhau)
    console.log(y); // 2
  }
  console.log(y); // 1
}

// const example - Block-scoped và không thể reassign
interface Person {
  name: string;
}

function constExample(): void {
  const z: Person = { name: 'John' };
  // z = {}; // ❌ TypeError: Assignment to constant variable
  z.name = 'Jane'; // ✅ OK - có thể thay đổi properties của object
  console.log(z); // { name: 'Jane' }
}
```

#### Q3: ES5 vs ES6+ features và modern JavaScript?

**Trả lời:**

```typescript
// ES5 Features (2009)
// 1. Array methods
var numbers = [1, 2, 3, 4, 5];
var doubled = numbers.map(function(n) { return n * 2; });
var evens = numbers.filter(function(n) { return n % 2 === 0; });
var sum = numbers.reduce(function(acc, n) { return acc + n; }, 0);

// 2. Object methods
var obj = { name: 'John', age: 30 };
var keys = Object.keys(obj);
var hasName = obj.hasOwnProperty('name');

// 3. Function bind
function greet() {
  console.log('Hello ' + this.name);
}
var boundGreet = greet.bind({ name: 'John' });

// ES6+ Features (2015+)
// 1. Let/Const và Block Scope
let x = 10;
const y = 20;

if (true) {
  let x = 30; // Different variable
  console.log(x); // 30
}
console.log(x); // 10

// 2. Arrow Functions
const add = (a, b) => a + b;
const square = x => x * x;
const greet = name => {
  console.log(`Hello ${name}`);
};

// 3. Template Literals
const name = 'John';
const message = `Hello ${name}, today is ${new Date().toDateString()}`;

// 4. Destructuring
const person = { name: 'John', age: 30, city: 'NYC' };
const { name, age } = person;
const { name: personName, age: personAge } = person; // Renaming

const numbers = [1, 2, 3, 4, 5];
const [first, second, ...rest] = numbers;

// 5. Default Parameters
function greet(name = 'Guest', greeting = 'Hello') {
  console.log(`${greeting}, ${name}!`);
}

// 6. Rest/Spread Operators
function sum(...numbers) {
  return numbers.reduce((a, b) => a + b, 0);
}

const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5]; // [1, 2, 3, 4, 5]

// 7. Enhanced Object Literals
const name = 'John';
const age = 30;

const person = {
  name, // Shorthand property
  age,
  greet() { // Method shorthand
    console.log(`Hello, I'm ${this.name}`);
  },
  [`dynamic_${age}`]: 'value' // Computed property names
};

// 8. Classes
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, I'm ${this.name}`);
  }

  static createAdult(name) {
    return new Person(name, 18);
  }
}

class Employee extends Person {
  constructor(name, age, position) {
    super(name, age);
    this.position = position;
  }

  work() {
    console.log(`${this.name} is working as ${this.position}`);
  }
}

// 9. Modules (ES6)
// export const PI = 3.14159;
// export default function calculate() {}
// import calculate, { PI } from './math.js';

// 10. Set và Map
const uniqueNumbers = new Set([1, 2, 2, 3, 3, 4]); // {1, 2, 3, 4}
uniqueNumbers.add(5);
uniqueNumbers.has(3); // true
uniqueNumbers.delete(2);

const userRoles = new Map();
userRoles.set('john', 'admin');
userRoles.set('jane', 'user');
userRoles.get('john'); // 'admin'
userRoles.has('jane'); // true

// 11. WeakSet và WeakMap (garbage collection friendly)
const weakSet = new WeakSet();
const obj1 = {};
const obj2 = {};
weakSet.add(obj1);
weakSet.add(obj2);
// Tự động remove khi objects bị garbage collected

const weakMap = new WeakMap();
const element = document.getElementById('myElement');
weakMap.set(element, { clickCount: 0 });
// Tự động cleanup khi element bị removed

// ES7+ Features
// 12. Async/Await (ES2017)
async function fetchUserData(userId) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    const user = await response.json();
    return user;
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}

// 13. Optional Chaining (ES2020)
const user = {
  profile: {
    social: {
      twitter: '@john'
    }
  }
};

const twitter = user?.profile?.social?.twitter; // Safe access
const followers = user?.profile?.social?.followers?.count; // undefined, no error

// 14. Nullish Coalescing (ES2020)
const username = user.name ?? 'Guest'; // Only null/undefined, not falsy
const port = process.env.PORT ?? 3000;

// 15. Private Class Fields (ES2022)
class Counter {
  #count = 0; // Private field

  increment() {
    this.#count++;
  }

  getCount() {
    return this.#count;
  }
}

const counter = new Counter();
// counter.#count; // SyntaxError - cannot access private field
```

#### Q4: Hoisting trong JavaScript - Cách hoạt động?

**Trả lời:**

```typescript
// 1. Variable Hoisting
console.log(x); // undefined (not ReferenceError)
var x = 5;

// Equivalent to:
var x; // hoisted to top, initialized with undefined
console.log(x); // undefined
x = 5;

// Let/Const Hoisting - Temporal Dead Zone
console.log(y); // ReferenceError: Cannot access 'y' before initialization
let y = 10;

console.log(z); // ReferenceError: Cannot access 'z' before initialization
const z = 20;

// 2. Function Hoisting
// Function declarations are fully hoisted
sayHello(); // "Hello!" - works!

function sayHello() {
  console.log("Hello!");
}

// Function expressions are NOT hoisted
sayGoodbye(); // TypeError: sayGoodbye is not a function

var sayGoodbye = function() {
  console.log("Goodbye!");
};

// 3. Class Hoisting - Temporal Dead Zone
const instance = new MyClass(); // ReferenceError

class MyClass {
  constructor() {
    this.name = 'MyClass';
  }
}

// 4. Advanced Hoisting Examples
function example() {
  console.log(typeof foo); // "function" - function hoisted
  console.log(typeof bar); // "undefined" - var hoisted, not assignment
  console.log(typeof baz); // ReferenceError - let in TDZ

  function foo() {
    return 'foo';
  }

  var bar = function() {
    return 'bar';
  };

  let baz = function() {
    return 'baz';
  };
}

// 5. Hoisting with Same Name
var myFunc = function() {
  console.log('Expression');
};

function myFunc() {
  console.log('Declaration');
}

myFunc(); // "Expression" - function expression overwrites declaration
```

#### Q5: Event Loop hoạt động như thế nào? (Giải thích đơn giản)

**Trả lời:**

**🏢 Giải thích Event Loop như một văn phòng:**
- **📚 Call Stack**: Bàn làm việc chính (làm từng việc một, theo thứ tự)
- **🌐 Web APIs**: Phòng máy móc (timer, DOM events, HTTP requests)
- **📋 Callback Queue**: Hàng đợi công việc thường
- **⚡ Microtask Queue**: Hàng đợi VIP (Promise, async/await)

```typescript
// 🎯 Event Loop - CƠ CHẾ HOẠT ĐỘNG CỦA JAVASCRIPT (Single-threaded)

console.log('1️⃣ Bắt đầu');
// ⬆️ 🔥 THỰC THI NGAY: Vào Call Stack, in ra màn hình

setTimeout(() => {
  console.log('4️⃣ Timeout');
  // ⬆️ 📋 VÀO CALLBACK QUEUE: Timer 0ms → Web API → Callback Queue → đợi
}, 0);

Promise.resolve().then(() => {
  console.log('3️⃣ Promise');
  // ⬆️ ⚡ VÀO MICROTASK QUEUE: Promise resolve → Microtask Queue (ưu tiên)
});

console.log('2️⃣ Kết thúc');
// ⬆️ 🔥 THỰC THI NGAY: Vào Call Stack, in ra màn hình

// 📊 OUTPUT THỰC TẾ: "1️⃣ Bắt đầu" → "2️⃣ Kết thúc" → "3️⃣ Promise" → "4️⃣ Timeout"

/*
🔍 QUY TRÌNH TỪNG BƯỚC:
1. 📚 Call Stack xử lý: console.log('1️⃣') ✅ IN RA NGAY
2. ⏰ setTimeout → 🌐 Web API (timer 0ms) → 📋 Callback Queue (đợi)
3. 🤝 Promise.resolve() → ⚡ Microtask Queue (chờ)
4. 📚 Call Stack xử lý: console.log('2️⃣') ✅ IN RA NGAY
5. 📚 Call Stack trống → Event Loop kiểm tra ⚡ Microtask Queue trước → ✅ IN '3️⃣'
6. ⚡ Microtask Queue trống → Event Loop kiểm tra 📋 Callback Queue → ✅ IN '4️⃣'
*/

// Quy trình làm việc của Event Loop:
// 1. Làm hết việc trong Call Stack trước
// 2. Kiểm tra Microtask Queue, làm hết
// 3. Mới đến Callback Queue
// 4. Lặp lại

// 🧩 VÍ DỤ PHỨC TẠP HỞN - THỨ TỰ THỰC THI:
console.log('🏁 Start');
// ⬆️ BƯỚC 1: Call Stack → IN NGAY

setTimeout(() => console.log('⏰ Timeout 1'), 0);
// ⬆️ BƯỚC 2: Web API → Callback Queue (vị trí thứ 1)

Promise.resolve()
  .then(() => {
    console.log('✅ Promise 1');
    // ⬆️ BƯỚC 5: Microtask Queue → thực thi → tạo Promise mới
    return Promise.resolve();
  })
  .then(() => console.log('✅ Promise 2'));
// ⬆️ BƯỚC 3: Microtask Queue (chain promise)

setTimeout(() => console.log('⏰ Timeout 2'), 0);
// ⬆️ BƯỚC 4: Web API → Callback Queue (vị trí thứ 2)

console.log('🏁 End');
// ⬆️ BƯỚC 6: Call Stack → IN NGAY

/*
📊 OUTPUT THỰC TẾ:
🏁 Start          → 📚 Call Stack (ngay lập tức)
🏁 End            → 📚 Call Stack (ngay lập tức)
✅ Promise 1      → ⚡ Microtask Queue (ưu tiên cao)
✅ Promise 2      → ⚡ Microtask Queue (promise chain)
⏰ Timeout 1      → 📋 Callback Queue (sau cùng)
⏰ Timeout 2      → 📋 Callback Queue (sau cùng)

💡 GHI NHỚ: MICROTASK QUEUE LUÔN ĐƯỢC XỬ LÝ TRƯỚC CALLBACK QUEUE!
*/

// Web APIs trong Browser:
// - setTimeout/setInterval → Callback Queue
// - DOM Events → Callback Queue
// - Promise.then/catch/finally → Microtask Queue
// - async/await → Microtask Queue
// - queueMicrotask() → Microtask Queue

// Thực tế hoạt động:
function demonstrateEventLoop() {
  console.log('🏁 Start');

  // Callback Queue
  setTimeout(() => console.log('⏰ Timer'), 0);

  // Microtask Queue
  Promise.resolve().then(() => console.log('✅ Promise'));

  // Call Stack
  console.log('🏁 Sync code');

  // Microtask Queue
  queueMicrotask(() => console.log('⚡ Microtask'));
}

demonstrateEventLoop();
// Output:
// 🏁 Start
// 🏁 Sync code
// ✅ Promise
// ⚡ Microtask
// ⏰ Timer
```

#### Q6: Closure và Data Privacy trong JavaScript?

**Trả lời:**

**🔐 Closure là gì?**
- **Closure = Function + Lexical Environment** (môi trường từ vựng)
- **Function có thể "nhớ" và truy cập biến từ scope bên ngoài**
- **Tạo ra Data Privacy** - biến private không thể truy cập từ bên ngoài

```typescript
// 🏭 1. CLOSURE FACTORY PATTERN - Tạo ra Data Privacy
function createCounter(): {
  increment(): number;
  decrement(): number;
  getCount(): number;
} {
  // 🔒 PRIVATE VARIABLE - chỉ có thể truy cập từ bên trong
  let count: number = 0;

  // 🏠 RETURN OBJECT với các method có Closure
  return {
    increment(): number {
      count++; // 🎯 CLOSURE: truy cập biến count từ outer scope
      return count;
    },
    decrement(): number {
      count--; // 🎯 CLOSURE: truy cập biến count từ outer scope
      return count;
    },
    getCount(): number {
      return count; // 🎯 CLOSURE: đọc biến count từ outer scope
    }
    // ❌ count KHÔNG THỂ truy cập trực tiếp từ bên ngoài - TRUE PRIVACY!
  };
}

const counter = createCounter();
console.log(counter.increment()); // ✅ 1
console.log(counter.increment()); // ✅ 2
console.log(counter.getCount());  // ✅ 2
console.log(counter.count);       // ❌ undefined - PRIVATE!

/*
🧠 TẠI SAO CLOSURE HOẠT ĐỘNG?
1. createCounter() tạo ra một execution context với biến count
2. Các inner functions (increment, decrement, getCount) được tạo trong context này
3. Khi createCounter() return object, các function vẫn "nhớ" biến count
4. Biến count vẫn "sống" trong memory vì các function vẫn reference đến nó
5. Đây chính là CLOSURE - function + environment của nó được preserve
*/

// 2. Module Pattern với IIFE
const CalculatorModule = (function() {
  let result = 0; // Private state

  function add(x) {
    result += x;
    return this;
  }

  function multiply(x) {
    result *= x;
    return this;
  }

  function getResult() {
    return result;
  }

  function reset() {
    result = 0;
    return this;
  }

  // Public API
  return {
    add,
    multiply,
    getResult,
    reset
  };
})();

CalculatorModule.add(5).multiply(2).add(3);
console.log(CalculatorModule.getResult()); // 13

// 3. Factory Functions với Closure
function createUser(name, email) {
  let isActive = true; // Private
  let loginAttempts = 0; // Private

  return {
    getName() {
      return name;
    },
    getEmail() {
      return email;
    },
    login(password) {
      if (loginAttempts >= 3) {
        isActive = false;
        throw new Error('Account locked');
      }

      if (password === 'correct') {
        loginAttempts = 0;
        return 'Login successful';
      } else {
        loginAttempts++;
        throw new Error('Invalid password');
      }
    },
    isAccountActive() {
      return isActive;
    }
  };
}

const user = createUser('John', 'john@email.com');
console.log(user.getName()); // 'John'
// console.log(user.isActive); // undefined - private!

// 4. Currying với Closure
function createMultiplier(multiplier) {
  return function(number) {
    return number * multiplier;
  };
}

const double = createMultiplier(2);
const triple = createMultiplier(3);

console.log(double(5)); // 10
console.log(triple(5)); // 15

// Advanced Currying
function curry(fn) {
  return function curried(...args) {
    if (args.length >= fn.length) {
      return fn.apply(this, args);
    } else {
      return function(...nextArgs) {
        return curried(...args, ...nextArgs);
      };
    }
  };
}

function add(a, b, c) {
  return a + b + c;
}

const curriedAdd = curry(add);
console.log(curriedAdd(1)(2)(3)); // 6
console.log(curriedAdd(1, 2)(3)); // 6
console.log(curriedAdd(1)(2, 3)); // 6

// 5. Event Handlers với Closure
function setupEventListeners() {
  const buttons = document.querySelectorAll('button');

  buttons.forEach((button, index) => {
    button.addEventListener('click', function() {
      // Closure captures 'index' and 'button'
      console.log(`Button ${index} clicked`);
    });
  });
}

// 6. Memoization với Closure
function memoize(fn) {
  const cache = new Map();

  return function(...args) {
    const key = JSON.stringify(args);

    if (cache.has(key)) {
      console.log('Cache hit!');
      return cache.get(key);
    }

    console.log('Computing...');
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  };
}

const expensiveOperation = memoize(function(n) {
  let result = 0;
  for (let i = 0; i < n; i++) {
    result += i;
  }
  return result;
});

console.log(expensiveOperation(1000)); // Computing... result
console.log(expensiveOperation(1000)); // Cache hit! result
```

#### Q7: DOM và Event Handling chi tiết?

**Trả lời:**

```typescript
// 1. Event Bubbling vs Event Capturing
/*
Event flow: Capturing → Target → Bubbling
         window
           ↓
        document
           ↓
         <html>
           ↓
         <body>
           ↓
        <div>      ← Event Capturing (từ trên xuống)
           ↓
       <button>    ← Target Element
           ↑
        <div>      ← Event Bubbling (từ dưới lên)
*/

// HTML:
// <div id="parent">
//   <button id="child">Click me</button>
// </div>

const parent = document.getElementById('parent');
const child = document.getElementById('child');

// Event Bubbling (default)
parent.addEventListener('click', () => {
  console.log('Parent clicked (bubbling)');
});

child.addEventListener('click', () => {
  console.log('Child clicked');
});

// Event Capturing
parent.addEventListener('click', () => {
  console.log('Parent clicked (capturing)');
}, true); // true = capturing phase

// Click child button → Output:
// "Parent clicked (capturing)"
// "Child clicked"
// "Parent clicked (bubbling)"

// 2. stopPropagation vs preventDefault
child.addEventListener('click', (event) => {
  event.stopPropagation(); // Stops event bubbling
  console.log('Child clicked - no bubbling');
});

// preventDefault - ngăn default behavior
const link = document.querySelector('a');
link.addEventListener('click', (event) => {
  event.preventDefault(); // Ngăn navigation
  console.log('Link clicked but no navigation');
});

const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault(); // Ngăn form submission
  console.log('Form submitted via AJAX instead');
});

// 3. event.target vs event.currentTarget
const container = document.getElementById('container');

container.addEventListener('click', (event) => {
  console.log('target:', event.target.tagName); // Element được click
  console.log('currentTarget:', event.currentTarget.tagName); // Element có event listener
});

// Click <span> inside <div> container:
// target: SPAN (element actually clicked)
// currentTarget: DIV (element with listener)

// 4. Event Delegation
const todoList = document.getElementById('todoList');

// Thay vì add listener cho mỗi item
todoList.addEventListener('click', (event) => {
  if (event.target.classList.contains('delete-btn')) {
    // Handle delete
    event.target.closest('li').remove();
  } else if (event.target.classList.contains('edit-btn')) {
    // Handle edit
    const todoItem = event.target.closest('li');
    enableEdit(todoItem);
  }
});

// Advantages:
// - Performance: 1 listener instead of many
// - Dynamic content: works for newly added items
// - Memory efficient

// 5. DOM Query Methods
// Single element
const element = document.getElementById('myId');
const element2 = document.querySelector('.my-class');
const element3 = document.querySelector('div[data-id="123"]');

// Multiple elements
const elements = document.getElementsByClassName('my-class');
const elements2 = document.getElementsByTagName('div');
const elements3 = document.querySelectorAll('.my-class');

// Modern approach - querySelectorAll
const buttons = document.querySelectorAll('button[data-action]');
buttons.forEach(button => {
  const action = button.dataset.action;
  button.addEventListener('click', () => handleAction(action));
});

// 6. DOM Manipulation
// Creating elements
const newDiv = document.createElement('div');
newDiv.className = 'new-item';
newDiv.textContent = 'Hello World';
newDiv.setAttribute('data-id', '123');

// Adding elements
const parent = document.getElementById('parent');
parent.appendChild(newDiv);
parent.insertBefore(newDiv, parent.firstChild);

// Modern approach
parent.insertAdjacentHTML('beforeend', '<div>New content</div>');
parent.insertAdjacentElement('afterbegin', newDiv);

// Removing elements
element.remove(); // Modern
parent.removeChild(element); // Legacy

// 7. Event Performance Optimization
// Debouncing search input
function debounce(func, delay) {
  let timeoutId;
  return function(...args) {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(() => func.apply(this, args), delay);
  };
}

const searchInput = document.getElementById('search');
const debouncedSearch = debounce((event) => {
  console.log('Searching for:', event.target.value);
  // Perform search API call
}, 300);

searchInput.addEventListener('input', debouncedSearch);

// Throttling scroll events
function throttle(func, delay) {
  let inThrottle;
  return function(...args) {
    if (!inThrottle) {
      func.apply(this, args);
      inThrottle = true;
      setTimeout(() => inThrottle = false, delay);
    }
  };
}

const throttledScroll = throttle(() => {
  console.log('Scroll position:', window.scrollY);
}, 100);

window.addEventListener('scroll', throttledScroll);

// 8. Custom Events
// Creating custom events
const customEvent = new CustomEvent('userLogin', {
  detail: {
    userId: 123,
    username: 'john'
  },
  bubbles: true
});

// Listening for custom events
document.addEventListener('userLogin', (event) => {
  console.log('User logged in:', event.detail);
});

// Dispatching custom events
document.dispatchEvent(customEvent);

// Real-world example: Component communication
class TodoComponent {
  constructor(element) {
    this.element = element;
    this.setupEvents();
  }

  setupEvents() {
    this.element.addEventListener('click', (e) => {
      if (e.target.classList.contains('complete-btn')) {
        this.completeTodo(e.target.closest('[data-todo-id]'));
      }
    });
  }

  completeTodo(todoElement) {
    const todoId = todoElement.dataset.todoId;

    // Update UI
    todoElement.classList.add('completed');

    // Emit custom event
    const event = new CustomEvent('todoCompleted', {
      detail: { todoId },
      bubbles: true
    });

    this.element.dispatchEvent(event);
  }
}

// Listen for todo completion
document.addEventListener('todoCompleted', (event) => {
  console.log(`Todo ${event.detail.todoId} completed`);
  updateStats();
});
```

#### Q8: Falsy/Truthy, == vs ===, null vs undefined?

**Trả lời:**

**🎯 Khái niệm cốt lõi:**

**❌ FALSY VALUES (8 giá trị duy nhất):**
```
false, 0, -0, 0n, "", null, undefined, NaN
```
**📝 Cách nhớ:** **F**alse **0** **""** **N**ull **U**ndefined **NaN** = **FO"NUN**

**✅ TRUTHY VALUES:** Tất cả còn lại (bao gồm `[]`, `{}`, `"0"`, `"false"`)

**⚖️ == vs === :**
- **`==`** = **L**oose **E**quality (có **type coercion** - chuyển đổi kiểu)
- **`===`** = **S**trict **E**quality (**KHÔNG** chuyển đổi kiểu)

**🧠 GHI NHỚ:**
- **`===`** = **S**ame **S**ame **S**ame (type + value)
- **`==`** = **E**quality with **E**xtra steps (conversion)

```typescript
// 1. Falsy Values - chỉ có 8 giá trị falsy
const falsyValues = [
  false,        // Boolean false
  0,           // Number zero
  -0,          // Negative zero
  0n,          // BigInt zero
  "",          // Empty string
  null,        // null
  undefined,   // undefined
  NaN          // Not a Number
];

// Tất cả các giá trị khác đều là truthy
const truthyValues = [
  true,
  1,
  -1,
  "0",         // String "0" is truthy!
  "false",     // String "false" is truthy!
  [],          // Empty array is truthy!
  {},          // Empty object is truthy!
  function(){} // Functions are truthy
];

// 2. == vs === (Type Coercion)
// === (Strict equality) - không convert type
console.log(5 === "5");        // false
console.log(true === 1);       // false
console.log(null === undefined); // false

// == (Loose equality) - có type conversion
console.log(5 == "5");         // true (string "5" → number 5)
console.log(true == 1);        // true (boolean true → number 1)
console.log(false == 0);       // true (boolean false → number 0)
console.log(null == undefined); // true (special case)

// Weird cases với ==
console.log("" == 0);          // true
console.log("" == false);      // true
console.log(" " == 0);         // true
console.log("0" == false);     // true
console.log([] == 0);          // true
console.log([] == false);      // true
console.log([1] == 1);         // true
console.log([1, 2] == "1,2");  // true

// Recommendation: Always use ===
// Exception: checking for null/undefined
if (value == null) {
  // This checks for both null AND undefined
}
// Equivalent to:
if (value === null || value === undefined) {
  // More explicit
}

// 3. null vs undefined
let declaredButNotAssigned; // undefined
let explicitlyNull = null;   // null

console.log(typeof undefined); // "undefined"
console.log(typeof null);      // "object" (famous JS bug)

// When you get undefined:
console.log(obj.nonExistentProperty); // undefined
console.log(arr[999]);                // undefined
function noReturn() {}
console.log(noReturn());              // undefined

// When you get null:
document.getElementById('nonExistent'); // null
JSON.parse('{"key": null}').key;       // null
/regex/.exec('no match');              // null

// Best practices:
// - Use undefined for "not set" or "not initialized"
// - Use null for "intentionally empty" or "no value"

// 4. Optional Chaining với nullish values
const user = {
  profile: null
};

// Old way
const city = user && user.profile && user.profile.address && user.profile.address.city;

// New way - Optional Chaining
const city2 = user?.profile?.address?.city; // undefined

// With arrays
const firstHobby = user?.hobbies?.[0];

// With functions
const result = user?.calculateSomething?.();

// 5. Nullish Coalescing (??) vs OR (||)
const value1 = null ?? "default";     // "default"
const value2 = undefined ?? "default"; // "default"
const value3 = 0 ?? "default";        // 0 (not "default"!)
const value4 = "" ?? "default";       // "" (not "default"!)
const value5 = false ?? "default";    // false (not "default"!)

// Compare with OR operator
const value6 = null || "default";     // "default"
const value7 = undefined || "default"; // "default"
const value8 = 0 || "default";        // "default" (different!)
const value9 = "" || "default";       // "default" (different!)
const value10 = false || "default";   // "default" (different!)

// Use cases:
// ?? when you want to handle only null/undefined
const port = process.env.PORT ?? 3000; // 0 is valid port

// || when you want to handle all falsy values
const username = user.name || "Guest"; // empty string should become "Guest"

// 6. typeof operator detailed
console.log(typeof 42);           // "number"
console.log(typeof "hello");      // "string"
console.log(typeof true);         // "boolean"
console.log(typeof undefined);    // "undefined"
console.log(typeof null);         // "object" (bug!)
console.log(typeof {});           // "object"
console.log(typeof []);           // "object" (arrays are objects)
console.log(typeof function(){}); // "function"
console.log(typeof Symbol());     // "symbol"
console.log(typeof 123n);         // "bigint"

// Better type checking
function getType(value) {
  if (value === null) return 'null';
  if (Array.isArray(value)) return 'array';
  return typeof value;
}

console.log(getType(null));    // "null"
console.log(getType([]));      // "array"
console.log(getType({}));      // "object"

// Advanced type checking
function isObject(value) {
  return value !== null && typeof value === 'object' && !Array.isArray(value);
}

function isPrimitive(value) {
  return value == null || /^[sbn]/.test(typeof value);
  // s: string, b: boolean, n: number
}
```

#### Q10: Arrow Functions vs Regular Functions và `this` binding?

**Trả lời:**

**🎯 Sự khác biệt cốt lõi:**

**📊 So sánh nhanh:**

| Đặc điểm | Arrow Function `=>` | Regular Function `function` |
|----------|-------------------|---------------------------|
| **🎯 `this` binding** | Lexical (inherited) | Dynamic (call-time) |
| **⬆️ Hoisting** | ❌ Không | ✅ Có |
| **🏗️ Constructor** | ❌ Không thể `new` | ✅ Có thể `new` |
| **📦 `arguments`** | ❌ Không có | ✅ Có |
| **🎨 Syntax** | Ngắn gọn | Dài hơn |

**🧠 GHI NHỚ:**
- **Arrow** = **A**lways **R**emember **R**oot **O**bject **W**hen binding (lexical this)
- **Regular** = **R**eal-time **this** (dynamic binding)

**🔑 GOLDEN RULE:** Arrow function "mượn" `this` từ nơi nó được ĐỊNH NGHĨA, không phải nơi được GỌI

```typescript
// 1. Regular Functions vs Arrow Functions
// Regular function
function regularFunction() {
  console.log('Regular function');
  console.log(this); // Dynamic this binding
}

// Arrow function
const arrowFunction = () => {
  console.log('Arrow function');
  console.log(this); // Lexical this binding
};

// 2. `this` binding differences
const obj = {
  name: 'Object',

  // Regular method
  regularMethod: function() {
    console.log(this.name); // "Object"

    // Nested regular function
    function nested() {
      console.log(this.name); // undefined (this = window/global)
    }
    nested();

    // Nested arrow function
    const nestedArrow = () => {
      console.log(this.name); // "Object" (inherits parent this)
    };
    nestedArrow();
  },

  // Arrow method (not recommended)
  arrowMethod: () => {
    console.log(this.name); // undefined (this = window/global)
  }
};

obj.regularMethod();
obj.arrowMethod();

// 3. call, apply, bind
function greet(greeting, punctuation) {
  return `${greeting} ${this.name}${punctuation}`;
}

const person = { name: 'John' };

// call - arguments individually
console.log(greet.call(person, 'Hello', '!')); // "Hello John!"

// apply - arguments as array
console.log(greet.apply(person, ['Hi', '.'])); // "Hi John."

// bind - creates new function with bound this
const boundGreet = greet.bind(person);
console.log(boundGreet('Hey', '?')); // "Hey John?"

// Partial application with bind
const sayHello = greet.bind(person, 'Hello');
console.log(sayHello('!')); // "Hello John!"

// 4. Real-world examples
class EventHandler {
  constructor(name) {
    this.name = name;
    this.count = 0;
  }

  // Problem with regular function
  setupRegularHandler() {
    document.getElementById('btn1').addEventListener('click', function() {
      this.count++; // Error: this is undefined
      console.log(`${this.name} clicked ${this.count} times`);
    });
  }

  // Solution 1: Arrow function
  setupArrowHandler() {
    document.getElementById('btn2').addEventListener('click', () => {
      this.count++; // Works: this refers to EventHandler instance
      console.log(`${this.name} clicked ${this.count} times`);
    });
  }

  // Solution 2: bind
  setupBoundHandler() {
    const handler = function() {
      this.count++;
      console.log(`${this.name} clicked ${this.count} times`);
    }.bind(this);

    document.getElementById('btn3').addEventListener('click', handler);
  }

  // Solution 3: Store reference
  setupReferenceHandler() {
    const self = this;
    document.getElementById('btn4').addEventListener('click', function() {
      self.count++;
      console.log(`${self.name} clicked ${self.count} times`);
    });
  }
}

// 5. React examples
class ReactComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = { count: 0 };

    // Method needs binding
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState({ count: this.state.count + 1 });
  }

  // Arrow function method (automatically bound)
  handleClickArrow = () => {
    this.setState({ count: this.state.count + 1 });
  };

  render() {
    return (
      <div>
        {/* Need to bind in JSX */}
        <button onClick={this.handleClick.bind(this)}>Click 1</button>

        {/* Or use arrow function in JSX (creates new function each render) */}
        <button onClick={() => this.handleClick()}>Click 2</button>

        {/* Pre-bound method */}
        <button onClick={this.handleClick}>Click 3</button>

        {/* Arrow function method */}
        <button onClick={this.handleClickArrow}>Click 4</button>
      </div>
    );
  }
}

// 6. Advanced this binding
function Calculator() {
  this.result = 0;

  return {
    add: function(n) {
      this.result += n;
      return this;
    },

    multiply: function(n) {
      this.result *= n;
      return this;
    },

    getResult: function() {
      return this.result;
    }
  };
}

const calc = new Calculator();
// Method chaining works because 'this' refers to returned object
console.log(calc.add(5).multiply(2).getResult()); // 10

// 7. Arrow functions limitations
// Cannot be constructor
const ArrowConstructor = () => {};
// new ArrowConstructor(); // TypeError

// No arguments object
function regularFunc() {
  console.log(arguments); // [1, 2, 3]
}

const arrowFunc = (...args) => {
  console.log(args); // Use rest parameters instead
};

regularFunc(1, 2, 3);
arrowFunc(1, 2, 3);

// 8. Best practices
// Use arrow functions for:
// - Callbacks and higher-order functions
// - Lexical this binding needed
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2); // Arrow function appropriate

// Use regular functions for:
// - Object methods
// - Constructor functions
// - When you need dynamic this
const object = {
  value: 42,
  getValue: function() { // Regular function appropriate
    return this.value;
  }
};
```

#### Q11: Async/Await vs Promises vs Callbacks?

**Trả lời:**

**🎯 Evolution of Asynchronous JavaScript:**

**📈 TIMELINE:** Callbacks → Promises → Async/Await

**📊 So sánh nhanh:**

| Đặc điểm | Callbacks | Promises | Async/Await |
|----------|-----------|----------|-------------|
| **📅 Ra đời** | ES5 (2009) | ES6 (2015) | ES8 (2017) |
| **😵 Callback Hell** | ❌ Có | ✅ Không | ✅ Không |
| **🔧 Error Handling** | ❌ Khó | ✅ .catch() | ✅ try/catch |
| **📖 Readability** | ❌ Khó đọc | 🆗 Tốt hơn | ✅ Rất dễ đọc |
| **🔄 Chaining** | ❌ Pyramid | ✅ .then() | ✅ Sequential |

**🧠 GHI NHỚ:**
- **Callbacks** = **C**allback **H**ell **A**waiting **O**nly **S**yntax (cũ)
- **Promises** = **P**romise **T**o **H**andle **A**sync (better)
- **Async/Await** = **A**lmost **S**ynchronous **S**yntax (best)

```typescript
// 1. Callbacks (Old way)
function fetchUserCallback(id, callback) {
  setTimeout(() => {
    if (id > 0) {
      callback(null, { id, name: `User ${id}` });
    } else {
      callback(new Error('Invalid ID'));
    }
  }, 1000);
}

// Callback hell
fetchUserCallback(1, (err, user) => {
  if (err) {
    console.error(err);
    return;
  }

  fetchUserPosts(user.id, (err, posts) => {
    if (err) {
      console.error(err);
      return;
    }

    fetchPostComments(posts[0].id, (err, comments) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log('Finally got comments:', comments);
    });
  });
});

// 2. Promises (Better)
function fetchUserPromise(id) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (id > 0) {
        resolve({ id, name: `User ${id}` });
      } else {
        reject(new Error('Invalid ID'));
      }
    }, 1000);
  });
}

function fetchUserPosts(userId) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([{ id: 1, title: 'Post 1', userId }]);
    }, 1000);
  });
}

function fetchPostComments(postId) {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([{ id: 1, text: 'Comment 1', postId }]);
    }, 1000);
  });
}

// Promise chaining
fetchUserPromise(1)
  .then(user => {
    console.log('User:', user);
    return fetchUserPosts(user.id);
  })
  .then(posts => {
    console.log('Posts:', posts);
    return fetchPostComments(posts[0].id);
  })
  .then(comments => {
    console.log('Comments:', comments);
  })
  .catch(error => {
    console.error('Error:', error);
  });

// 3. Async/Await (Best)
async function fetchUserData(id) {
  try {
    const user = await fetchUserPromise(id);
    console.log('User:', user);

    const posts = await fetchUserPosts(user.id);
    console.log('Posts:', posts);

    const comments = await fetchPostComments(posts[0].id);
    console.log('Comments:', comments);

    return { user, posts, comments };
  } catch (error) {
    console.error('Error:', error);
    throw error;
  }
}

// Usage
fetchUserData(1)
  .then(data => console.log('All data:', data))
  .catch(error => console.error('Failed:', error));

// 4. Promise.all - Parallel execution
async function fetchMultipleUsers(ids) {
  try {
    // All requests happen in parallel
    const users = await Promise.all(
      ids.map(id => fetchUserPromise(id))
    );

    console.log('All users:', users);
    return users;
  } catch (error) {
    // If any fails, all fail
    console.error('One user fetch failed:', error);
  }
}

fetchMultipleUsers([1, 2, 3]);

// 5. Promise.allSettled - Don't fail fast
async function fetchMultipleUsersSettled(ids) {
  const results = await Promise.allSettled(
    ids.map(id => fetchUserPromise(id))
  );

  const successful = results
    .filter(result => result.status === 'fulfilled')
    .map(result => result.value);

  const failed = results
    .filter(result => result.status === 'rejected')
    .map(result => result.reason);

  console.log('Successful:', successful);
  console.log('Failed:', failed);

  return { successful, failed };
}

fetchMultipleUsersSettled([1, -1, 2, -2]);

// 6. Promise.race - First to complete
async function fetchWithTimeout(id, timeout = 5000) {
  const fetchPromise = fetchUserPromise(id);
  const timeoutPromise = new Promise((_, reject) => {
    setTimeout(() => reject(new Error('Timeout')), timeout);
  });

  try {
    const result = await Promise.race([fetchPromise, timeoutPromise]);
    return result;
  } catch (error) {
    console.error('Fetch failed or timed out:', error);
    throw error;
  }
}

// 7. Promise.any - First successful
async function fetchFromMultipleSources(id) {
  const sources = [
    fetch(`/api/v1/users/${id}`),
    fetch(`/api/v2/users/${id}`),
    fetch(`/backup/users/${id}`)
  ];

  try {
    const response = await Promise.any(sources);
    return await response.json();
  } catch (error) {
    console.error('All sources failed:', error);
  }
}

// 8. Advanced error handling
async function robustFetch(url, retries = 3) {
  for (let i = 0; i < retries; i++) {
    try {
      const response = await fetch(url);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      return await response.json();
    } catch (error) {
      console.log(`Attempt ${i + 1} failed:`, error.message);

      if (i === retries - 1) {
        throw error;
      }

      // Exponential backoff
      await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000));
    }
  }
}

// 9. Async generators
async function* fetchPaginatedData(baseUrl) {
  let page = 1;
  let hasMore = true;

  while (hasMore) {
    try {
      const response = await fetch(`${baseUrl}?page=${page}`);
      const data = await response.json();

      yield data.items;

      hasMore = data.hasNextPage;
      page++;
    } catch (error) {
      console.error('Failed to fetch page:', page, error);
      break;
    }
  }
}

// Usage
async function processAllData() {
  for await (const items of fetchPaginatedData('/api/items')) {
    console.log('Processing batch:', items.length);
    // Process items
  }
}

// 10. AbortController for cancellation
async function fetchWithAbort(url, timeoutMs = 5000) {
  const controller = new AbortController();

  // Set timeout
  const timeoutId = setTimeout(() => controller.abort(), timeoutMs);

  try {
    const response = await fetch(url, {
      signal: controller.signal
    });

    clearTimeout(timeoutId);
    return await response.json();
  } catch (error) {
    clearTimeout(timeoutId);

    if (error.name === 'AbortError') {
      console.log('Fetch was aborted');
    } else {
      console.error('Fetch failed:', error);
    }
    throw error;
  }
}

// Manual cancellation
const controller = new AbortController();
fetchWithAbort('/api/data', { signal: controller.signal });

// Cancel after 2 seconds
setTimeout(() => controller.abort(), 2000);
```

#### Q12: Cách remove property từ object và so sánh objects?

**Trả lời:**

```typescript
// 1. Remove property từ object
const user = {
  id: 1,
  name: 'John',
  email: 'john@example.com',
  password: 'secret',
  role: 'admin'
};

// Method 1: delete operator
delete user.password;
console.log(user); // { id: 1, name: 'John', email: 'john@example.com', role: 'admin' }

// Method 2: Destructuring + Rest (immutable)
const { password, ...userWithoutPassword } = user;
console.log(userWithoutPassword); // { id: 1, name: 'John', email: 'john@example.com', role: 'admin' }
console.log(user); // Original object unchanged

// Method 3: Omit function
function omit(obj, ...keys) {
  const result = { ...obj };
  keys.forEach(key => delete result[key]);
  return result;
}

const publicUser = omit(user, 'password', 'role');
console.log(publicUser); // { id: 1, name: 'John', email: 'john@example.com' }

// Method 4: Pick function (opposite of omit)
function pick(obj, ...keys) {
  return keys.reduce((result, key) => {
    if (key in obj) {
      result[key] = obj[key];
    }
    return result;
  }, {});
}

const basicUser = pick(user, 'id', 'name');
console.log(basicUser); // { id: 1, name: 'John' }

// Method 5: Using Object.fromEntries
function removeProperties(obj, ...propsToRemove) {
  return Object.fromEntries(
    Object.entries(obj).filter(([key]) => !propsToRemove.includes(key))
  );
}

const filteredUser = removeProperties(user, 'password', 'role');

// 2. So sánh objects
// Shallow comparison
function shallowEqual(obj1, obj2) {
  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) {
    return false;
  }

  for (let key of keys1) {
    if (obj1[key] !== obj2[key]) {
      return false;
    }
  }

  return true;
}

const obj1 = { a: 1, b: 2 };
const obj2 = { a: 1, b: 2 };
const obj3 = { a: 1, b: { c: 3 } };
const obj4 = { a: 1, b: { c: 3 } };

console.log(shallowEqual(obj1, obj2)); // true
console.log(shallowEqual(obj3, obj4)); // false (different object references)

// Deep comparison
function deepEqual(obj1, obj2) {
  if (obj1 === obj2) {
    return true;
  }

  if (obj1 == null || obj2 == null) {
    return false;
  }

  if (typeof obj1 !== typeof obj2) {
    return false;
  }

  if (typeof obj1 !== 'object') {
    return obj1 === obj2;
  }

  if (Array.isArray(obj1) !== Array.isArray(obj2)) {
    return false;
  }

  const keys1 = Object.keys(obj1);
  const keys2 = Object.keys(obj2);

  if (keys1.length !== keys2.length) {
    return false;
  }

  for (let key of keys1) {
    if (!keys2.includes(key)) {
      return false;
    }

    if (!deepEqual(obj1[key], obj2[key])) {
      return false;
    }
  }

  return true;
}

console.log(deepEqual(obj3, obj4)); // true
console.log(deepEqual([1, [2, 3]], [1, [2, 3]])); // true

// 3. So sánh big numbers/decimals
// Problem với floating point
console.log(0.1 + 0.2 === 0.3); // false!
console.log(0.1 + 0.2); // 0.30000000000000004

// Solution 1: Number.EPSILON
function floatEqual(a, b, epsilon = Number.EPSILON) {
  return Math.abs(a - b) < epsilon;
}

console.log(floatEqual(0.1 + 0.2, 0.3)); // true

// Solution 2: toFixed
function compareDecimals(a, b, precision = 10) {
  return parseFloat(a.toFixed(precision)) === parseFloat(b.toFixed(precision));
}

console.log(compareDecimals(0.1 + 0.2, 0.3)); // true

// Solution 3: BigInt for large integers
const bigInt1 = BigInt("123456789012345678901234567890");
const bigInt2 = BigInt("123456789012345678901234567890");

console.log(bigInt1 === bigInt2); // true

// For decimal precision with BigInt
function decimalToBigInt(decimal, precision = 18) {
  const factor = BigInt(10 ** precision);
  return BigInt(Math.round(decimal * (10 ** precision)));
}

function compareBigDecimals(a, b, precision = 18) {
  return decimalToBigInt(a, precision) === decimalToBigInt(b, precision);
}

// 4. String combination methods
const firstName = 'John';
const lastName = 'Doe';
const age = 30;

// Method 1: Concatenation
const name1 = firstName + ' ' + lastName;

// Method 2: Template literals (recommended)
const greeting = `Hello, my name is ${firstName} ${lastName} and I'm ${age} years old.`;

// Method 3: join
const fullName = [firstName, lastName].join(' ');

// Method 4: concat
const name2 = firstName.concat(' ', lastName);

// Performance comparison for large operations
function combineStringsConcat(arr) {
  let result = '';
  for (let str of arr) {
    result += str;
  }
  return result;
}

function combineStringsJoin(arr) {
  return arr.join('');
}

// join() is generally faster for many strings
const manyStrings = new Array(10000).fill('test');
console.time('concat');
combineStringsConcat(manyStrings);
console.timeEnd('concat');

console.time('join');
combineStringsJoin(manyStrings);
console.timeEnd('join');

// 5. Advanced object operations
class ObjectUtils {
  static merge(target, ...sources) {
    return sources.reduce((acc, source) => {
      Object.keys(source).forEach(key => {
        if (source[key] && typeof source[key] === 'object' && !Array.isArray(source[key])) {
          acc[key] = this.merge(acc[key] || {}, source[key]);
        } else {
          acc[key] = source[key];
        }
      });
      return acc;
    }, { ...target });
  }

  static flatten(obj, prefix = '') {
    return Object.keys(obj).reduce((acc, key) => {
      const value = obj[key];
      const newKey = prefix ? `${prefix}.${key}` : key;

      if (value && typeof value === 'object' && !Array.isArray(value)) {
        Object.assign(acc, this.flatten(value, newKey));
      } else {
        acc[newKey] = value;
      }

      return acc;
    }, {});
  }

  static unflatten(obj) {
    const result = {};

    Object.keys(obj).forEach(key => {
      const keys = key.split('.');
      let current = result;

      keys.forEach((k, index) => {
        if (index === keys.length - 1) {
          current[k] = obj[key];
        } else {
          current[k] = current[k] || {};
          current = current[k];
        }
      });
    });

    return result;
  }
}

const nested = {
  user: {
    profile: {
      name: 'John',
      address: {
        city: 'New York'
      }
    }
  }
};

const flattened = ObjectUtils.flatten(nested);
console.log(flattened); // { 'user.profile.name': 'John', 'user.profile.address.city': 'New York' }

const restored = ObjectUtils.unflatten(flattened);
console.log(restored); // Original nested structure
```

#### Q14: Loop Performance và Browser Rendering (Paint, Repaint, Reflow)?

**Trả lời:**

```typescript
// 1. Loop Performance Comparison
const data = Array.from({ length: 100000 }, (_, i) => i);

// for loop - Fastest
console.time('for loop');
let sum1 = 0;
for (let i = 0; i < data.length; i++) {
  sum1 += data[i];
}
console.timeEnd('for loop');

// for...of - Good performance
console.time('for...of');
let sum2 = 0;
for (const item of data) {
  sum2 += item;
}
console.timeEnd('for...of');

// forEach - Slower due to function calls
console.time('forEach');
let sum3 = 0;
data.forEach(item => {
  sum3 += item;
});
console.timeEnd('forEach');

// for...in - Slowest (don't use for arrays)
console.time('for...in');
let sum4 = 0;
for (const index in data) {
  sum4 += data[index];
}
console.timeEnd('for...in');

// Performance ranking: for > for...of > forEach > for...in

// 2. Optimized Array Methods
// map - Creates new array
const doubled = data.map(x => x * 2);

// reduce - Single value
const total = data.reduce((acc, curr) => acc + curr, 0);

// filter - Filtered array
const evens = data.filter(x => x % 2 === 0);

// find - First match
const found = data.find(x => x > 50000);

// some/every - Boolean checks
const hasLarge = data.some(x => x > 90000);
const allPositive = data.every(x => x >= 0);

// 3. Paint, Repaint, Reflow trong trình duyệt
/*
Browser Rendering Process:
1. Parse HTML/CSS → DOM/CSSOM
2. Layout (Reflow) → Calculate positions
3. Paint → Fill pixels
4. Composite → Layer combination
*/

// REFLOW (Layout) - Most expensive
// Changes that affect layout/geometry
function causeReflow() {
  const element = document.getElementById('box');

  // These properties trigger reflow:
  element.style.width = '200px';     // Size changes
  element.style.height = '200px';
  element.style.margin = '10px';     // Spacing changes
  element.style.padding = '5px';
  element.style.border = '1px solid black';
  element.style.fontSize = '16px';   // Text size changes

  // Reading these properties also triggers reflow:
  console.log(element.offsetWidth);
  console.log(element.offsetHeight);
  console.log(element.scrollTop);
  console.log(element.clientWidth);
}

// REPAINT (Paint) - Medium cost
// Changes that affect appearance but not layout
function causeRepaint() {
  const element = document.getElementById('box');

  // These properties trigger repaint only:
  element.style.backgroundColor = 'red';
  element.style.color = 'white';
  element.style.borderColor = 'blue';
  element.style.visibility = 'hidden'; // vs display: none (reflow)
}

// COMPOSITE ONLY - Cheapest
// Changes that only affect compositing
function compositeOnly() {
  const element = document.getElementById('box');

  // These properties are GPU accelerated:
  element.style.transform = 'translateX(100px)'; // Use transform, not left/top
  element.style.opacity = '0.5';
  element.style.filter = 'blur(5px)';
}

// 4. Performance Optimization Techniques
// Batch DOM operations
function badPerformance() {
  const list = document.getElementById('list');

  // Bad: Causes multiple reflows
  for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Item ${i}`;
    list.appendChild(item); // Reflow on each append
  }
}

function goodPerformance() {
  const list = document.getElementById('list');
  const fragment = document.createDocumentFragment();

  // Good: Batch operations
  for (let i = 0; i < 1000; i++) {
    const item = document.createElement('li');
    item.textContent = `Item ${i}`;
    fragment.appendChild(item); // No reflow
  }

  list.appendChild(fragment); // Single reflow
}

// Use CSS classes instead of individual styles
function animateElement() {
  const element = document.getElementById('box');

  // Bad: Multiple style changes
  element.style.width = '200px';
  element.style.height = '200px';
  element.style.backgroundColor = 'red';
  element.style.transform = 'rotate(45deg)';

  // Good: Single class change
  element.className = 'animated-box';
}

// CSS for above:
/*
.animated-box {
  width: 200px;
  height: 200px;
  background-color: red;
  transform: rotate(45deg);
  transition: all 0.3s ease;
}
*/

// 5. Measuring Performance
function measureRenderPerformance() {
  // Performance API
  const observer = new PerformanceObserver((list) => {
    for (const entry of list.getEntries()) {
      console.log('Performance entry:', entry);
    }
  });

  observer.observe({ entryTypes: ['measure', 'navigation', 'paint'] });

  // Custom measurements
  performance.mark('start-operation');

  // Expensive operation
  for (let i = 0; i < 1000; i++) {
    document.getElementById('test').style.left = i + 'px';
  }

  performance.mark('end-operation');
  performance.measure('operation-duration', 'start-operation', 'end-operation');
}

// 6. RequestAnimationFrame for smooth animations
function smoothAnimation() {
  const element = document.getElementById('box');
  let position = 0;

  function animate() {
    position += 2;
    element.style.transform = `translateX(${position}px)`;

    if (position < 300) {
      requestAnimationFrame(animate); // 60fps
    }
  }

  requestAnimationFrame(animate);
}

// vs bad animation
function badAnimation() {
  const element = document.getElementById('box');
  let position = 0;

  const interval = setInterval(() => {
    position += 2;
    element.style.left = position + 'px'; // Causes reflow

    if (position >= 300) {
      clearInterval(interval);
    }
  }, 16); // Trying to match 60fps
}

// 7. Virtual Scrolling for large lists
class VirtualList {
  constructor(container, items, itemHeight = 50) {
    this.container = container;
    this.items = items;
    this.itemHeight = itemHeight;
    this.containerHeight = container.clientHeight;
    this.visibleCount = Math.ceil(this.containerHeight / itemHeight) + 1;
    this.startIndex = 0;

    this.setupContainer();
    this.render();
    this.bindEvents();
  }

  setupContainer() {
    this.container.style.overflowY = 'scroll';
    this.container.style.height = this.containerHeight + 'px';

    // Create spacer for total height
    this.spacer = document.createElement('div');
    this.spacer.style.height = (this.items.length * this.itemHeight) + 'px';
    this.container.appendChild(this.spacer);

    // Create visible items container
    this.visibleContainer = document.createElement('div');
    this.visibleContainer.style.position = 'absolute';
    this.visibleContainer.style.top = '0';
    this.visibleContainer.style.width = '100%';
    this.container.appendChild(this.visibleContainer);
  }

  render() {
    const fragment = document.createDocumentFragment();

    for (let i = 0; i < this.visibleCount && this.startIndex + i < this.items.length; i++) {
      const item = document.createElement('div');
      item.style.height = this.itemHeight + 'px';
      item.textContent = this.items[this.startIndex + i];
      fragment.appendChild(item);
    }

    this.visibleContainer.innerHTML = '';
    this.visibleContainer.appendChild(fragment);
    this.visibleContainer.style.transform = `translateY(${this.startIndex * this.itemHeight}px)`;
  }

  bindEvents() {
    this.container.addEventListener('scroll', () => {
      const newStartIndex = Math.floor(this.container.scrollTop / this.itemHeight);

      if (newStartIndex !== this.startIndex) {
        this.startIndex = newStartIndex;
        this.render();
      }
    });
  }
}

// Usage
const items = Array.from({ length: 10000 }, (_, i) => `Item ${i}`);
const virtualList = new VirtualList(document.getElementById('list'), items);
```

#### Q15: Axios Interceptors và Advanced Error Handling?

**Trả lời:**

```typescript
// 1. Basic Axios Interceptors
import axios from 'axios';

// Request Interceptor
axios.interceptors.request.use(
  (config) => {
    // Add auth token
    const token = localStorage.getItem('authToken');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Add request timestamp
    config.metadata = { startTime: new Date() };

    console.log('Request sent:', config);
    return config;
  },
  (error) => {
    console.error('Request error:', error);
    return Promise.reject(error);
  }
);

// Response Interceptor
axios.interceptors.response.use(
  (response) => {
    // Calculate request duration
    const endTime = new Date();
    const duration = endTime - response.config.metadata.startTime;
    console.log(`Request took ${duration}ms`);

    return response;
  },
  (error) => {
    // Handle common errors
    if (error.response?.status === 401) {
      // Redirect to login
      localStorage.removeItem('authToken');
      window.location.href = '/login';
    }

    return Promise.reject(error);
  }
);

// 2. Advanced Interceptor Setup
class ApiClient {
  constructor(baseURL) {
    this.client = axios.create({
      baseURL,
      timeout: 10000,
      headers: {
        'Content-Type': 'application/json'
      }
    });

    this.setupInterceptors();
  }

  setupInterceptors() {
    // Request interceptor
    this.client.interceptors.request.use(
      this.handleRequest.bind(this),
      this.handleRequestError.bind(this)
    );

    // Response interceptor
    this.client.interceptors.response.use(
      this.handleResponse.bind(this),
      this.handleResponseError.bind(this)
    );
  }

  handleRequest(config) {
    // Add loading state
    this.setLoading(true);

    // Add auth
    const token = this.getAuthToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Add request ID for tracking
    config.headers['X-Request-ID'] = this.generateRequestId();

    // Add API version
    config.headers['X-API-Version'] = '1.0';

    return config;
  }

  handleRequestError(error) {
    this.setLoading(false);
    this.showError('Request failed to send');
    return Promise.reject(error);
  }

  handleResponse(response) {
    this.setLoading(false);

    // Log successful requests
    console.log('✅ API Success:', {
      url: response.config.url,
      method: response.config.method.toUpperCase(),
      status: response.status,
      data: response.data
    });

    return response;
  }

  async handleResponseError(error) {
    this.setLoading(false);

    const { response, request, message } = error;

    if (response) {
      // Server responded with error
      await this.handleServerError(response);
    } else if (request) {
      // Network error
      this.handleNetworkError();
    } else {
      // Other error
      this.handleGenericError(message);
    }

    return Promise.reject(error);
  }

  async handleServerError(response) {
    const { status, data } = response;

    switch (status) {
      case 400:
        this.showError('Invalid request data');
        break;

      case 401:
        await this.handleUnauthorized();
        break;

      case 403:
        this.showError('Access denied');
        break;

      case 404:
        this.showError('Resource not found');
        break;

      case 409:
        this.showError('Conflict: Resource already exists');
        break;

      case 422:
        this.handleValidationErrors(data.errors);
        break;

      case 429:
        this.handleRateLimit(response.headers);
        break;

      case 500:
        this.showError('Server error. Please try again later.');
        break;

      case 503:
        this.showError('Service temporarily unavailable');
        break;

      default:
        this.showError(`Unexpected error: ${status}`);
    }
  }

  async handleUnauthorized() {
    // Try to refresh token
    try {
      await this.refreshToken();
      // Retry original request
      return true;
    } catch (refreshError) {
      // Redirect to login
      this.logout();
      return false;
    }
  }

  handleNetworkError() {
    if (!navigator.onLine) {
      this.showError('No internet connection');
    } else {
      this.showError('Network error. Please check your connection.');
    }
  }

  handleValidationErrors(errors) {
    Object.keys(errors).forEach(field => {
      const messages = errors[field];
      this.showFieldError(field, messages.join(', '));
    });
  }

  handleRateLimit(headers) {
    const retryAfter = headers['retry-after'];
    this.showError(`Rate limit exceeded. Retry after ${retryAfter} seconds.`);
  }

  // Utility methods
  getAuthToken() {
    return localStorage.getItem('authToken');
  }

  generateRequestId() {
    return Math.random().toString(36).substr(2, 9);
  }

  setLoading(loading) {
    // Update global loading state
    window.dispatchEvent(new CustomEvent('loadingChange', { detail: loading }));
  }

  showError(message) {
    // Show toast/notification
    window.dispatchEvent(new CustomEvent('showError', { detail: message }));
  }

  showFieldError(field, message) {
    // Show field-specific error
    window.dispatchEvent(new CustomEvent('fieldError', {
      detail: { field, message }
    }));
  }

  async refreshToken() {
    const refreshToken = localStorage.getItem('refreshToken');
    const response = await axios.post('/auth/refresh', { refreshToken });
    localStorage.setItem('authToken', response.data.accessToken);
    return response.data;
  }

  logout() {
    localStorage.removeItem('authToken');
    localStorage.removeItem('refreshToken');
    window.location.href = '/login';
  }
}

// 3. Request/Response Transformation
const api = new ApiClient('/api/v1');

// Transform request data
api.client.interceptors.request.use((config) => {
  // Convert camelCase to snake_case for API
  if (config.data && typeof config.data === 'object') {
    config.data = transformKeys(config.data, camelToSnake);
  }

  // Convert query params
  if (config.params) {
    config.params = transformKeys(config.params, camelToSnake);
  }

  return config;
});

// Transform response data
api.client.interceptors.response.use((response) => {
  // Convert snake_case to camelCase
  if (response.data && typeof response.data === 'object') {
    response.data = transformKeys(response.data, snakeToCamel);
  }

  return response;
});

// Key transformation utilities
function transformKeys(obj, transformer) {
  if (Array.isArray(obj)) {
    return obj.map(item => transformKeys(item, transformer));
  }

  if (obj && typeof obj === 'object') {
    return Object.keys(obj).reduce((result, key) => {
      const transformedKey = transformer(key);
      result[transformedKey] = transformKeys(obj[key], transformer);
      return result;
    }, {});
  }

  return obj;
}

function camelToSnake(str) {
  return str.replace(/[A-Z]/g, letter => `_${letter.toLowerCase()}`);
}

function snakeToCamel(str) {
  return str.replace(/_([a-z])/g, (_, letter) => letter.toUpperCase());
}

// 4. Request Retry Logic
api.client.interceptors.response.use(null, async (error) => {
  const config = error.config;

  // Don't retry if already retried max times
  if (!config || !config.retry || config.retryCount >= config.retry) {
    return Promise.reject(error);
  }

  // Increment retry count
  config.retryCount = config.retryCount || 0;
  config.retryCount++;

  // Exponential backoff
  const delay = Math.pow(2, config.retryCount) * 1000;
  await new Promise(resolve => setTimeout(resolve, delay));

  // Retry request
  return api.client.request(config);
});

// 5. Request Caching
class CachedApiClient extends ApiClient {
  constructor(baseURL) {
    super(baseURL);
    this.cache = new Map();
    this.setupCaching();
  }

  setupCaching() {
    // Cache GET requests
    this.client.interceptors.request.use((config) => {
      if (config.method === 'get' && config.cache !== false) {
        const cacheKey = this.getCacheKey(config);
        const cached = this.cache.get(cacheKey);

        if (cached && !this.isCacheExpired(cached)) {
          // Return cached response
          config.adapter = () => Promise.resolve(cached.response);
        }
      }

      return config;
    });

    // Store responses in cache
    this.client.interceptors.response.use((response) => {
      if (response.config.method === 'get' && response.config.cache !== false) {
        const cacheKey = this.getCacheKey(response.config);
        const ttl = response.config.cacheTTL || 300000; // 5 minutes default

        this.cache.set(cacheKey, {
          response,
          timestamp: Date.now(),
          ttl
        });
      }

      return response;
    });
  }

  getCacheKey(config) {
    return `${config.method}:${config.url}:${JSON.stringify(config.params)}`;
  }

  isCacheExpired(cached) {
    return Date.now() - cached.timestamp > cached.ttl;
  }

  clearCache() {
    this.cache.clear();
  }
}

// 6. Usage Examples
const cachedApi = new CachedApiClient('/api/v1');

// Basic requests
async function fetchUser(id) {
  try {
    const response = await cachedApi.client.get(`/users/${id}`, {
      retry: 3,
      cache: true,
      cacheTTL: 600000 // 10 minutes
    });
    return response.data;
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}

// Parallel requests
async function fetchUserData(userId) {
  try {
    const [user, posts, followers] = await Promise.all([
      cachedApi.client.get(`/users/${userId}`),
      cachedApi.client.get(`/users/${userId}/posts`),
      cachedApi.client.get(`/users/${userId}/followers`)
    ]);

    return {
      user: user.data,
      posts: posts.data,
      followers: followers.data
    };
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    throw error;
  }
}
```

#### Q16: Strict Mode và JavaScript Classes?

**Trả lời:**

```typescript
// 1. Strict Mode trong JavaScript
'use strict'; // Global strict mode

function normalFunction() {
  // Non-strict mode behavior
  undeclaredVar = 10; // Creates global variable
  return undeclaredVar;
}

function strictFunction() {
  'use strict'; // Function-level strict mode

  // undeclaredVar = 10; // ReferenceError in strict mode

  // Other strict mode changes:

  // 1. 'this' is undefined in functions (not window)
  console.log(this); // undefined

  // 2. Can't delete variables, functions, or arguments
  var x = 10;
  // delete x; // SyntaxError

  // 3. Duplicate parameter names not allowed
  // function duplicate(a, a) {} // SyntaxError

  // 4. Octal literals not allowed
  // var octal = 077; // SyntaxError

  // 5. Can't assign to read-only properties
  var obj = {};
  Object.defineProperty(obj, 'prop', { value: 10, writable: false });
  // obj.prop = 20; // TypeError
}

// 2. ES6 Classes - Modern approach
class User {
  // Private fields (ES2022)
  #password;
  #loginAttempts = 0;

  // Public fields
  isActive = true;

  // Static field
  static maxLoginAttempts = 3;

  constructor(username, email, password) {
    this.username = username;
    this.email = email;
    this.#password = password;
    this.createdAt = new Date();
  }

  // Public method
  login(password) {
    if (this.#loginAttempts >= User.maxLoginAttempts) {
      throw new Error('Account locked');
    }

    if (this.#checkPassword(password)) {
      this.#loginAttempts = 0;
      this.lastLogin = new Date();
      return true;
    } else {
      this.#loginAttempts++;
      return false;
    }
  }

  // Private method
  #checkPassword(password) {
    return this.#password === password;
  }

  // Getter
  get profile() {
    return {
      username: this.username,
      email: this.email,
      isActive: this.isActive,
      createdAt: this.createdAt
    };
  }

  // Setter
  set email(newEmail) {
    if (this.#validateEmail(newEmail)) {
      this._email = newEmail;
    } else {
      throw new Error('Invalid email format');
    }
  }

  get email() {
    return this._email;
  }

  #validateEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  // Static method
  static createGuest() {
    return new User('guest', 'guest@example.com', 'temporary');
  }

  // Method override example
  toString() {
    return `User: ${this.username} (${this.email})`;
  }
}

// 3. Inheritance
class AdminUser extends User {
  constructor(username, email, password, permissions = []) {
    super(username, email, password); // Call parent constructor
    this.permissions = permissions;
    this.isAdmin = true;
  }

  // Override parent method
  login(password) {
    const success = super.login(password); // Call parent method

    if (success) {
      console.log(`Admin ${this.username} logged in`);
      this.auditLog('login');
    }

    return success;
  }

  // New method
  auditLog(action) {
    console.log(`[AUDIT] ${this.username} performed: ${action} at ${new Date()}`);
  }

  addPermission(permission) {
    if (!this.permissions.includes(permission)) {
      this.permissions.push(permission);
    }
  }

  hasPermission(permission) {
    return this.permissions.includes(permission);
  }
}

// 4. Mixins Pattern
const Serializable = {
  serialize() {
    return JSON.stringify(this);
  },

  deserialize(json) {
    const data = JSON.parse(json);
    Object.assign(this, data);
    return this;
  }
};

const Timestamped = {
  updateTimestamp() {
    this.updatedAt = new Date();
  },

  getAge() {
    return Date.now() - this.createdAt.getTime();
  }
};

// Apply mixins
Object.assign(User.prototype, Serializable, Timestamped);

// 5. Abstract Base Class Pattern
class Shape {
  constructor(color) {
    if (new.target === Shape) {
      throw new Error('Cannot instantiate abstract class');
    }
    this.color = color;
  }

  // Abstract method
  area() {
    throw new Error('Must implement area method');
  }

  // Concrete method
  describe() {
    return `A ${this.color} shape with area ${this.area()}`;
  }
}

class Circle extends Shape {
  constructor(color, radius) {
    super(color);
    this.radius = radius;
  }

  area() {
    return Math.PI * this.radius ** 2;
  }
}

class Rectangle extends Shape {
  constructor(color, width, height) {
    super(color);
    this.width = width;
    this.height = height;
  }

  area() {
    return this.width * this.height;
  }
}

// 6. Factory Pattern with Classes
class CarFactory {
  static types = {
    sedan: 'Sedan',
    suv: 'SUV',
    hatchback: 'Hatchback'
  };

  static create(type, options) {
    switch (type) {
      case CarFactory.types.sedan:
        return new Sedan(options);
      case CarFactory.types.suv:
        return new SUV(options);
      case CarFactory.types.hatchback:
        return new Hatchback(options);
      default:
        throw new Error(`Unknown car type: ${type}`);
    }
  }
}

class Car {
  constructor({ make, model, year, color }) {
    this.make = make;
    this.model = model;
    this.year = year;
    this.color = color;
    this.mileage = 0;
  }

  start() {
    console.log(`${this.make} ${this.model} started`);
  }

  drive(distance) {
    this.mileage += distance;
    console.log(`Drove ${distance} miles. Total: ${this.mileage} miles`);
  }
}

class Sedan extends Car {
  constructor(options) {
    super(options);
    this.type = 'sedan';
    this.fuelEfficiency = 30; // mpg
  }
}

class SUV extends Car {
  constructor(options) {
    super(options);
    this.type = 'suv';
    this.fuelEfficiency = 20; // mpg
    this.has4WD = true;
  }
}

class Hatchback extends Car {
  constructor(options) {
    super(options);
    this.type = 'hatchback';
    this.fuelEfficiency = 35; // mpg
  }
}

// 7. Performance Optimized Classes
class OptimizedDataProcessor {
  constructor() {
    this.cache = new Map();
    this.results = [];

    // Bind methods to avoid recreating functions
    this.process = this.process.bind(this);
    this.getResults = this.getResults.bind(this);
  }

  // Use static methods when no instance data needed
  static validateData(data) {
    return Array.isArray(data) && data.length > 0;
  }

  // Memoized method
  expensiveCalculation(input) {
    if (this.cache.has(input)) {
      return this.cache.get(input);
    }

    // Simulate expensive operation
    const result = input.split('').reverse().join('').repeat(1000);
    this.cache.set(input, result);

    return result;
  }

  // Batch processing
  process(dataArray) {
    if (!OptimizedDataProcessor.validateData(dataArray)) {
      throw new Error('Invalid data');
    }

    // Process in chunks to avoid blocking
    const chunkSize = 100;
    const chunks = this.createChunks(dataArray, chunkSize);

    return new Promise((resolve) => {
      this.processChunks(chunks, 0, resolve);
    });
  }

  createChunks(array, size) {
    const chunks = [];
    for (let i = 0; i < array.length; i += size) {
      chunks.push(array.slice(i, i + size));
    }
    return chunks;
  }

  processChunks(chunks, index, callback) {
    if (index >= chunks.length) {
      callback(this.results);
      return;
    }

    // Process chunk
    const chunk = chunks[index];
    chunk.forEach(item => {
      this.results.push(this.expensiveCalculation(item));
    });

    // Use setTimeout to yield control
    setTimeout(() => {
      this.processChunks(chunks, index + 1, callback);
    }, 0);
  }

  getResults() {
    return [...this.results]; // Return copy to prevent mutation
  }

  clear() {
    this.cache.clear();
    this.results.length = 0;
  }
}

// 8. Usage Examples
// Create instances
const user = new User('john', 'john@example.com', 'password123');
const admin = new AdminUser('admin', 'admin@example.com', 'admin123', ['read', 'write', 'delete']);

// Test functionality
console.log(user.login('password123')); // true
console.log(user.profile); // { username: 'john', ... }

admin.addPermission('manage_users');
console.log(admin.hasPermission('delete')); // true

// Serialization
const serialized = user.serialize();
const newUser = new User('', '', '').deserialize(serialized);

// Factory pattern
const sedan = CarFactory.create(CarFactory.types.sedan, {
  make: 'Toyota',
  model: 'Camry',
  year: 2023,
  color: 'blue'
});

sedan.start();
sedan.drive(100);

// Optimized processing
const processor = new OptimizedDataProcessor();
processor.process(['data1', 'data2', 'data3']).then(results => {
  console.log('Processing complete:', results.length);
});
```

### 2. React Fundamentals

#### Q17: React Hooks chi tiết - useState, useEffect, useRef?

**Trả lời:**

**Giải thích:**
- **useState**: Quản lý state trong functional component
- **useEffect**: Xử lý side effects (thay thế lifecycle methods)
- **useRef**: Tham chiếu DOM elements hoặc lưu giá trị mutable

```typescript
// 🎯 1. useState - QUẢN LÝ STATE TRONG FUNCTIONAL COMPONENT
import React, { useState, useCallback, useMemo, useEffect, useRef } from 'react';

// 📋 Interface định nghĩa kiểu dữ liệu cho user
interface User {
  name: string;
  age: number;
}

function Counter(): JSX.Element {
  // 🔢 useState với PRIMITIVE TYPE
  const [count, setCount] = useState<number>(0);
  // ⬆️ Syntax: [currentValue, setterFunction] = useState(initialValue)

  // 📦 useState với OBJECT TYPE - cần interface cho TypeScript
  const [user, setUser] = useState<User>({ name: '', age: 0 });

  // ❌❌❌ CÁCH SAI - MUTATE STATE TRỰC TIẾP (Đừng bao giờ làm!)
  const handleWrongUpdate = (): void => {
    user.name = 'John'; // 🚨 NGUY HIỂM: thay đổi trực tiếp object gốc
    setUser(user); // 🚨 React KHÔNG DETECT được thay đổi vì reference không đổi!
    // Result: Component sẽ KHÔNG re-render!
  };

  // ✅✅✅ CÁCH ĐÚNG - IMMUTABLE UPDATE (Luôn làm như này!)
  const handleCorrectUpdate = (): void => {
    setUser(prev => ({
      ...prev, // 📄 SPREAD: Sao chép tất cả properties cũ
      name: 'John' // 🎯 UPDATE: Chỉ thay đổi property cần thiết
    }));
    // Result: React detect thay đổi → Component re-render!
  };

  // 🚀 FUNCTIONAL UPDATES - Tối ưu cho performance
  const increment = useCallback((): void => {
    setCount(prev => prev + 1);
    // ⬆️ 💡 WHY BETTER: Tránh stale closure, luôn dùng giá trị mới nhất
    // ❌ Thay vì: setCount(count + 1) - có thể dùng giá trị cũ
  }, []);

  // ⚡ LAZY INITIAL STATE - Tối ưu cho expensive calculations
  const [expensiveValue] = useState<number>(() => {
    console.log('🏃‍♂️ CHỈ CHẠY 1 LẦN khi component mount');
    // 💰 Expensive calculation chỉ chạy lần đầu, không chạy lại mỗi re-render
    return Array.from({ length: 1000 }, (_, i) => i).reduce((a, b) => a + b, 0);
  });
  // ⬆️ 💡 Nếu không dùng arrow function: useState(expensiveCalculation())
  //     thì calculation sẽ chạy EVERY RENDER!

  return (
    <div>
      <p>Count: {count}</p>
      <p>Expensive value: {expensiveValue}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={handleCorrectUpdate}>Update User</button>
    </div>
  );
}

// 2. useEffect - Xử lý side effects và cleanup
interface UserProfileProps {
  userId: number;
}

interface UserData {
  id: number;
  name: string;
  email: string;
}

function UserProfile({ userId }: UserProfileProps): JSX.Element {
  // State với kiểu union type (có thể null hoặc UserData)
  const [user, setUser] = useState<UserData | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // useEffect với dependencies - chỉ chạy khi userId thay đổi
  useEffect(() => {
    let cancelled = false; // Flag để tránh memory leak khi component unmount

    async function fetchUser(): Promise<void> {
      try {
        setLoading(true);
        setError(null);

        const response = await fetch(`/api/users/${userId}`);
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const userData: UserData = await response.json();

        // Kiểm tra component còn được mount không (tránh memory leak)
        if (!cancelled) {
          setUser(userData);
        }
      } catch (err) {
        if (!cancelled) {
          setError(err instanceof Error ? err.message : 'Có lỗi xảy ra');
        }
      } finally {
        if (!cancelled) {
          setLoading(false);
        }
      }
    }

    // Chỉ fetch khi có userId
    if (userId) {
      fetchUser();
    }

    // Cleanup function - chạy khi component unmount hoặc trước effect tiếp theo
    return () => {
      cancelled = true; // Đánh dấu để hủy các async operations
    };
  }, [userId]); // Dependency array - effect chỉ chạy lại khi userId thay đổi

  // Effect với cleanup - subscriptions, timers
  useEffect(() => {
    const timer = setInterval(() => {
      console.log('Timer tick');
    }, 1000);

    const subscription = eventBus.subscribe('userUpdate', (data) => {
      setUser(data);
    });

    // Cleanup function runs on unmount or before next effect
    return () => {
      clearInterval(timer);
      subscription.unsubscribe();
    };
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>{user?.name}</h1>
      <p>{user?.email}</p>
    </div>
  );
}

// 3. useRef - Mutable references và DOM access
function TextInput() {
  const inputRef = useRef(null);
  const countRef = useRef(0); // Mutable value không trigger re-render
  const prevCountRef = useRef();
  const [count, setCount] = useState(0);

  // Store previous value
  useEffect(() => {
    prevCountRef.current = count;
  });

  const focusInput = () => {
    inputRef.current?.focus();
  };

  const handleClick = () => {
    countRef.current += 1; // Doesn't trigger re-render
    console.log('Clicked times:', countRef.current);

    setCount(prev => prev + 1); // Triggers re-render
  };

  return (
    <div>
      <input ref={inputRef} type="text" />
      <button onClick={focusInput}>Focus Input</button>

      <p>Current: {count}</p>
      <p>Previous: {prevCountRef.current}</p>
      <p>Click count (no re-render): {countRef.current}</p>
      <button onClick={handleClick}>Click</button>
    </div>
  );
}
```

#### Q18: Component Lifecycle và useEffect coverage?

**Trả lời:**

```typescript
// 1. Class Component Lifecycle Complete
class UserProfileClass extends React.Component {
  constructor(props) {
    super(props);
    this.state = { user: null, loading: true, error: null };
    console.log('1. Constructor - Component được khởi tạo');
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    console.log('2. getDerivedStateFromProps - Sync state với props');
    if (nextProps.userId !== prevState.prevUserId) {
      return { prevUserId: nextProps.userId, user: null, loading: true };
    }
    return null;
  }

  componentDidMount() {
    console.log('3. componentDidMount - Component đã mount');
    this.fetchUser();
    this.timer = setInterval(() => console.log('Timer tick'), 1000);
  }

  shouldComponentUpdate(nextProps, nextState) {
    console.log('4. shouldComponentUpdate - Có nên update không?');
    return (
      nextProps.userId !== this.props.userId ||
      nextState.user !== this.state.user
    );
  }

  getSnapshotBeforeUpdate(prevProps, prevState) {
    console.log('5. getSnapshotBeforeUpdate - Trước khi DOM update');
    if (prevProps.userId !== this.props.userId) {
      return { scrollPosition: window.scrollY };
    }
    return null;
  }

  componentDidUpdate(prevProps, prevState, snapshot) {
    console.log('6. componentDidUpdate - Sau khi update');
    if (prevProps.userId !== this.props.userId) {
      this.fetchUser();
    }
    if (snapshot !== null) {
      window.scrollTo(0, snapshot.scrollPosition);
    }
  }

  componentWillUnmount() {
    console.log('7. componentWillUnmount - Component sắp unmount');
    if (this.timer) clearInterval(this.timer);
    if (this.abortController) this.abortController.abort();
  }

  componentDidCatch(error, errorInfo) {
    console.log('8. componentDidCatch - Bắt lỗi từ children');
    this.setState({ error: error.message });
  }

  fetchUser = async () => {
    try {
      this.abortController = new AbortController();
      const response = await fetch(`/api/users/${this.props.userId}`, {
        signal: this.abortController.signal
      });
      const user = await response.json();
      this.setState({ user, loading: false, error: null });
    } catch (error) {
      if (error.name !== 'AbortError') {
        this.setState({ error: error.message, loading: false });
      }
    }
  };

  render() {
    console.log('Render - Component đang render');
    const { user, loading, error } = this.state;

    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    return <div><h1>{user?.name}</h1><p>{user?.email}</p></div>;
  }
}

// 2. Functional Component với Hooks (Lifecycle equivalent)
function UserProfileFunction({ userId }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const abortControllerRef = useRef();

  // ⚡ componentDidMount + componentDidUpdate equivalent
  useEffect(() => {
    console.log('Mount/Update effect');

    async function fetchUser() {
      try {
        setLoading(true);
        setError(null);

        if (abortControllerRef.current) {
          abortControllerRef.current.abort();
        }

        abortControllerRef.current = new AbortController();
        const response = await fetch(`/api/users/${userId}`, {
          signal: abortControllerRef.current.signal
        });

        const userData = await response.json();
        setUser(userData);
        setLoading(false);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message);
          setLoading(false);
        }
      }
    }

    if (userId) fetchUser();

    // ⚡ componentWillUnmount equivalent (cleanup)
    return () => {
      console.log('Cleanup function');
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
      }
    };
  }, [userId]); // Dependencies = shouldComponentUpdate logic

  // ⚡ componentDidMount only (empty dependency array)
  useEffect(() => {
    console.log('Mount only effect');
    const timer = setInterval(() => console.log('Timer tick'), 1000);
    return () => clearInterval(timer);
  }, []);

  // ⚡ componentDidUpdate only (skip first render)
  const isFirstRender = useRef(true);
  useEffect(() => {
    if (isFirstRender.current) {
      isFirstRender.current = false;
      return;
    }
    console.log('Update only effect');
    document.title = `User: ${user?.name || 'Loading...'}`;
  });

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;
  return <div><h1>{user?.name}</h1><p>{user?.email}</p></div>;
}

// 3. useEffect Lifecycle Coverage Summary
/*
✅ useEffect(() => {}, []) = componentDidMount
✅ useEffect(() => {}, [dep]) = componentDidUpdate (when dep changes)
✅ useEffect(() => { return () => {} }, []) = componentWillUnmount
✅ useEffect(() => {}) = componentDidMount + componentDidUpdate (every render)
❌ getSnapshotBeforeUpdate = Không có equivalent
❌ componentDidCatch = Chỉ có Error Boundary (Class only)
❌ getDerivedStateFromError = Chỉ có Error Boundary (Class only)
*/

// 4. When will cleanup function run?
function CleanupExample() {
  useEffect(() => {
    console.log('Effect runs');

    return () => {
      console.log('Cleanup runs:');
      console.log('1. Before next effect (if dependencies changed)');
      console.log('2. On component unmount');
    };
  }, [dependency]);

  // Multiple effects - each has its own cleanup
  useEffect(() => {
    const timer = setInterval(() => {}, 1000);
    return () => clearInterval(timer); // Cleanup timer
  }, []);

  useEffect(() => {
    const subscription = subscribe();
    return () => subscription.unsubscribe(); // Cleanup subscription
  }, []);
}

// 5. Error Boundary (Class Component only)
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
    this.setState({ error, errorInfo });

    // Send to error reporting service
    this.logErrorToService(error, errorInfo);
  }

  logErrorToService = (error, errorInfo) => {
    // Send to Sentry, LogRocket, etc.
    console.log('Sending to error service:', { error, errorInfo });
  };

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-boundary">
          <h2>Something went wrong!</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
            <br />
            {this.state.errorInfo.componentStack}
          </details>
        </div>
      );
    }
    return this.props.children;
  }
}

// 6. Functional Components CAN'T handle all use cases
/*
❌ Error Boundaries - Chỉ Class Components có thể catch errors
❌ getSnapshotBeforeUpdate - Không có hook equivalent
❌ componentDidCatch - Chỉ có trong Class Components

✅ Mọi thứ khác đều có thể làm với Hooks
*/
```

#### Q19: PureComponent vs React.memo và optimization?

**Trả lời:**

**🎯 React Performance Optimization Tools:**

**📊 So sánh PureComponent vs React.memo:**

| Đặc điểm | `PureComponent` | `React.memo` |
|----------|-----------------|--------------|
| **🏗️ Component Type** | Class Component | Functional Component |
| **🔍 So sánh** | Shallow compare props + state | Shallow compare props only |
| **⚙️ Custom Compare** | ❌ Không | ✅ Custom function |
| **📅 Ra đời** | React 15.3 (2016) | React 16.6 (2018) |
| **🚀 Performance** | Tốt | Tốt hơn (less overhead) |

**🧠 GHI NHỚ:**
- **PureComponent** = **P**ure **C**lass **C**omponent (old school)
- **React.memo** = **M**emoize **F**unctional **C**omponent (modern)
- **Shallow Compare** = So sánh **1 cấp** (không deep compare)

**⚡ KHI NÀO SỬ DỤNG:**
- ✅ Component re-render thường xuyên với cùng props
- ✅ Component có expensive render logic
- ❌ Props thay đổi thường xuyên
- ❌ Component đã render nhanh sẵn

```typescript
// 1. PureComponent - Class Component với shallow comparison
import React, { PureComponent, Component, memo, useState, useCallback, useMemo } from 'react';

// ❌ Regular Component - always re-renders
class RegularComponent extends Component {
  render() {
    console.log('RegularComponent rendered');
    return <div>{this.props.name} - {this.props.count}</div>;
  }
}

// ✅ PureComponent - shallow comparison of props and state
class PureComponentExample extends PureComponent {
  render() {
    console.log('PureComponent rendered');
    return <div>{this.props.name} - {this.props.count}</div>;
  }
}

// ✅ Manual shouldComponentUpdate
class ManualComponent extends Component {
  shouldComponentUpdate(nextProps, nextState) {
    return (
      nextProps.name !== this.props.name ||
      nextProps.count !== this.props.count
    );
  }

  render() {
    console.log('ManualComponent rendered');
    return <div>{this.props.name} - {this.props.count}</div>;
  }
}

// 2. React.memo - Functional Component equivalent
// ❌ Regular Functional Component - always re-renders
function RegularFunction({ name, count }) {
  console.log('RegularFunction rendered');
  return <div>{name} - {count}</div>;
}

// ✅ React.memo - shallow comparison
const MemoizedFunction = memo(function MemoizedFunction({ name, count }) {
  console.log('MemoizedFunction rendered');
  return <div>{name} - {count}</div>;
});

// ✅ React.memo with custom comparison
const CustomMemoFunction = memo(function CustomMemoFunction({ user, settings }) {
  console.log('CustomMemoFunction rendered');
  return <div>{user.name} - {settings.theme}</div>;
}, (prevProps, nextProps) => {
  // Return true if props are equal (DON'T re-render)
  // Return false if props are different (DO re-render)
  return (
    prevProps.user.id === nextProps.user.id &&
    prevProps.user.name === nextProps.user.name &&
    prevProps.settings.theme === nextProps.settings.theme
  );
});

// 3. Why we use PureComponent/React.memo?
function ParentComponent() {
  const [count, setCount] = useState(0);
  const [otherState, setOtherState] = useState('');

  // Expensive data
  const expensiveData = { name: 'John', age: 30 };

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>
      <button onClick={() => setOtherState('changed')}>Change Other State</button>

      {/* ❌ Will re-render even when props haven't changed */}
      <RegularFunction name="John" count={100} />

      {/* ✅ Only re-renders when props actually change */}
      <MemoizedFunction name="John" count={100} />

      {/* ❌ Problem: new object reference every render */}
      <MemoizedFunction name={expensiveData.name} count={expensiveData.age} />
    </div>
  );
}

// 4. Common optimization pitfalls
function ProblematicParent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>

      {/* ❌ New object every render - memo won't help */}
      <MemoizedFunction user={{ name: 'John' }} />

      {/* ❌ New function every render - memo won't help */}
      <MemoizedChild onUpdate={() => console.log('updated')} />

      {/* ❌ New array every render - memo won't help */}
      <MemoizedList items={['a', 'b', 'c']} />
    </div>
  );
}

// 5. Proper optimization techniques
function OptimizedParent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState(['a', 'b', 'c']);

  // ✅ Stable object reference
  const user = useMemo(() => ({ name: 'John', id: 1 }), []);

  // ✅ Stable function reference
  const handleUpdate = useCallback(() => {
    console.log('updated');
  }, []);

  // ✅ Memoize expensive computations
  const expensiveValue = useMemo(() => {
    return items.map(item => item.toUpperCase()).join('-');
  }, [items]);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Count: {count}</button>

      {/* ✅ Won't re-render unnecessarily */}
      <MemoizedFunction user={user} />
      <MemoizedChild onUpdate={handleUpdate} />
      <MemoizedList items={items} />

      <div>Expensive value: {expensiveValue}</div>
    </div>
  );
}

// 6. When NOT to use memo
// ❌ Don't use memo if props change frequently
const FrequentlyChangingComponent = memo(function FrequentlyChangingComponent({ timestamp }) {
  return <div>Time: {timestamp}</div>; // timestamp changes every second
});

// ❌ Don't use memo for simple components
const SimpleComponent = memo(function SimpleComponent({ text }) {
  return <span>{text}</span>; // Too simple, memo overhead not worth it
});

// ❌ Don't use memo if parent always passes new props
function BadParent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      {/* memo is useless here because data is always new */}
      <MemoizedFunction data={{ value: Math.random() }} />
    </div>
  );
}

// 7. Advanced optimization patterns
const ExpensiveChild = memo(function ExpensiveChild({ data, onProcess }) {
  console.log('ExpensiveChild rendering');

  // Expensive computation only when data changes
  const processedData = useMemo(() => {
    console.log('Processing data...');
    return data.map(item => ({
      ...item,
      processed: true,
      timestamp: Date.now()
    }));
  }, [data]);

  return (
    <div>
      <h3>Processed Items: {processedData.length}</h3>
      <button onClick={() => onProcess(processedData)}>Process</button>
      <ul>
        {processedData.map(item => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
});

function SmartParent() {
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' }
  ]);
  const [otherState, setOtherState] = useState(0);

  // ✅ Stable callback
  const handleProcess = useCallback((processedData) => {
    console.log('Processed:', processedData);
  }, []);

  // ✅ Add item without changing reference of existing items
  const addItem = useCallback(() => {
    setItems(prev => [...prev, {
      id: Date.now(),
      name: `Item ${prev.length + 1}`
    }]);
  }, []);

  return (
    <div>
      <button onClick={() => setOtherState(prev => prev + 1)}>
        Other State: {otherState}
      </button>
      <button onClick={addItem}>Add Item</button>

      {/* Won't re-render when otherState changes */}
      <ExpensiveChild data={items} onProcess={handleProcess} />
    </div>
  );
}

// 8. Performance measurement
function PerformanceExample() {
  const [count, setCount] = useState(0);

  // Measure component re-renders
  const renderCount = useRef(0);
  renderCount.current++;

  console.log(`Component rendered ${renderCount.current} times`);

  // Use React DevTools Profiler to measure:
  // - Render time
  // - Number of re-renders
  // - Props that caused re-render

  return (
    <div>
      <p>Render count: {renderCount.current}</p>
      <button onClick={() => setCount(count + 1)}>
        Count: {count}
      </button>
    </div>
  );
}
```

#### Q20: Virtual DOM và Key trong Lists?

**Trả lời:**

**Giải thích:**
- **Virtual DOM**: Bản sao ảo của Real DOM trong bộ nhớ, giúp React tối ưu việc cập nhật UI
- **Key trong Lists**: Giúp React nhận diện các item trong list để tối ưu quá trình re-render
- **Tại sao không dùng index**: Index có thể thay đổi khi thêm/xóa item, gây ra bugs

```typescript
// 🎭 1. VIRTUAL DOM CONCEPT - Tại sao React nhanh?

/*
🏠 REAL DOM vs 🎭 VIRTUAL DOM COMPARISON:

🏠 REAL DOM (Browser's Native):
❌ HEAVY: Mỗi element = complex object với 100+ properties
❌ SLOW: Mỗi thay đổi → immediate browser re-render
❌ EXPENSIVE: Update 1 element → có thể trigger reflow/repaint whole page
❌ SYNCHRONOUS: Block UI thread khi update
❌ INEFFICIENT: Không có optimization cho multiple updates

🎭 VIRTUAL DOM (React's JavaScript Objects):
✅ LIGHTWEIGHT: Chỉ là plain JavaScript objects với vài properties
✅ FAST: So sánh objects trong memory (microseconds)
✅ SMART: Batch multiple updates → 1 DOM operation cuối cùng
✅ ASYNCHRONOUS: Không block UI thread
✅ OPTIMIZED: Diffing algorithm tìm minimal changes

🔄 DIFFING ALGORITHM WORKFLOW:
1. 📝 State thay đổi → React tạo Virtual DOM tree mới
2. 🔍 So sánh (Diff) Virtual DOM cũ vs Virtual DOM mới
3. 🎯 Tìm ra MINIMAL changes cần thiết (chỉ những gì thực sự khác)
4. 📦 Batch tất cả updates lại → 1 DOM operation duy nhất
5. 🚀 Browser chỉ re-render/repaint những gì thay đổi

💡 PERFORMANCE EXAMPLE:
- List 1000 items, thay đổi 1 item:
  - Không Virtual DOM: Re-render cả 1000 items ❌
  - Có Virtual DOM: Chỉ update 1 item đó ✅ (99.9% faster!)
*/

// 2. Tại sao Keys quan trọng trong Lists
interface User {
  id: number;
  name: string;
  email: string;
}

function BadListExample(): JSX.Element {
  const [users, setUsers] = useState<User[]>([
    { id: 1, name: 'John', email: 'john@email.com' },
    { id: 2, name: 'Jane', email: 'jane@email.com' },
    { id: 3, name: 'Bob', email: 'bob@email.com' }
  ]);

  const addUser = (): void => {
    const newUser: User = {
      id: Date.now(),
      name: 'New User',
      email: 'new@email.com'
    };
    setUsers([newUser, ...users]); // Thêm vào đầu list
  };

  const removeUser = (id: number): void => {
    setUsers(users.filter(user => user.id !== id));
  };

  return (
    <div>
      <button onClick={addUser}>Add User</button>

      {/* ❌❌❌ BAD EXAMPLE - Using index as key */}
      <h3>🚨 Bad Example (index as key):</h3>
      {users.map((user, index) => (
        <UserRow
          key={index} // 🚨 NGUY HIỂM: index thay đổi khi add/remove items
          user={user}
          onRemove={removeUser}
        />
      ))}
      {/*
      🐛 VẤN ĐỀ KHI DÙNG INDEX:
      - Thêm user ở đầu → tất cả index thay đổi → React nghĩ tất cả items đều thay đổi
      - Xóa user ở giữa → các index sau bị shift → React re-render không cần thiết
      - State của component có thể bị mix-up (input values, focus, etc.)
      */}

      {/* ❌❌ WORSE EXAMPLE - No key at all */}
      <h3>💀 Worse Example (no key):</h3>
      {users.map((user) => (
        <UserRow // 💀 TỆ NHẤT: React sẽ dùng index internally + warning
          user={user}
          onRemove={removeUser}
        />
      ))}
      {/*
      💀 KẾT QUẢ KHI KHÔNG CÓ KEY:
      - React warning trong console: "Each child should have unique key prop"
      - Performance tệ nhất có thể
      - Bugs không thể predict được với component state
      */}

      {/* ✅✅✅ GOOD EXAMPLE - Using stable unique ID */}
      <h3>✨ Good Example (stable ID as key):</h3>
      {users.map((user) => (
        <UserRow
          key={user.id} // ✅ PERFECT: stable, unique, không thay đổi theo thời gian
          user={user}
          onRemove={removeUser}
        />
      ))}
      {/*
      🎯 TẠI SAO user.id LÀ KEY TỐT NHẤT:
      - user.id không bao giờ thay đổi → React biết chính xác item nào là item nào
      - Thêm/xóa items → React chỉ update đúng những item cần thiết
      - Component state được preserve correctly (input focus, scroll position, etc.)
      - Performance optimization tối đa với O(1) lookup
      */}
    </div>
  );
}

function UserRow({ user, onRemove }) {
  const [isEditing, setIsEditing] = useState(false);
  const [localName, setLocalName] = useState(user.name);

  // This component has internal state
  // Wrong keys can cause state to be associated with wrong items

  return (
    <div style={{ border: '1px solid #ccc', margin: '5px', padding: '10px' }}>
      {isEditing ? (
        <input
          value={localName}
          onChange={(e) => setLocalName(e.target.value)}
          onBlur={() => setIsEditing(false)}
        />
      ) : (
        <span onClick={() => setIsEditing(true)}>
          {user.name} - {user.email}
        </span>
      )}
      <button onClick={() => onRemove(user.id)}>Remove</button>
    </div>
  );
}

// 3. Virtual DOM Reconciliation Process
/*
Step 1: State Change
setUsers([newUser, ...users])

Step 2: Virtual DOM Creation
React creates new Virtual DOM tree

Step 3: Diffing Algorithm
React compares old Virtual DOM with new Virtual DOM

Step 4: Reconciliation
React identifies minimal changes needed

Step 5: Real DOM Update
React applies only necessary changes to Real DOM
*/

// 4. Key Reconciliation Examples
function ReconciliationExample() {
  const [items, setItems] = useState([
    { id: 'a', text: 'Item A' },
    { id: 'b', text: 'Item B' },
    { id: 'c', text: 'Item C' }
  ]);

  // Scenario 1: Add item to beginning
  const addToBeginning = () => {
    setItems([{ id: 'new', text: 'New Item' }, ...items]);
  };

  // With index keys: React thinks all items changed
  // key=0: 'New Item' (was 'Item A')
  // key=1: 'Item A' (was 'Item B')
  // key=2: 'Item B' (was 'Item C')
  // key=3: 'Item C' (new)
  // Result: ALL items re-rendered

  // With ID keys: React knows only one item added
  // key='new': 'New Item' (new)
  // key='a': 'Item A' (unchanged)
  // key='b': 'Item B' (unchanged)
  // key='c': 'Item C' (unchanged)
  // Result: Only ONE item rendered

  return (
    <div>
      <button onClick={addToBeginning}>Add to Beginning</button>

      {/* Performance comparison */}
      <div>
        <h4>With Index Keys (Bad Performance):</h4>
        {items.map((item, index) => (
          <ExpensiveComponent key={index} item={item} />
        ))}

        <h4>With ID Keys (Good Performance):</h4>
        {items.map((item) => (
          <ExpensiveComponent key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}

function ExpensiveComponent({ item }) {
  const renderCount = useRef(0);
  renderCount.current++;

  // Simulate expensive computation
  const expensiveValue = useMemo(() => {
    console.log(`Computing expensive value for ${item.text}`);
    let result = 0;
    for (let i = 0; i < 100000; i++) {
      result += i;
    }
    return result;
  }, [item.text]);

  return (
    <div style={{ background: renderCount.current > 1 ? 'red' : 'green' }}>
      {item.text} (Render #{renderCount.current}) - Expensive: {expensiveValue}
    </div>
  );
}

// 5. When Index Keys are Acceptable
function StaticListExample() {
  // ✅ OK to use index when:
  // - List is static (never changes)
  // - Items don't have unique IDs
  // - No reordering, adding, or removing

  const staticItems = ['Apple', 'Banana', 'Cherry']; // Never changes

  return (
    <ul>
      {staticItems.map((item, index) => (
        <li key={index}>{item}</li> // ✅ OK: list never changes
      ))}
    </ul>
  );
}

// 6. Complex Key Scenarios
function ComplexKeyExample() {
  const [todos, setTodos] = useState([
    { id: 1, text: 'Learn React', completed: false, category: 'learning' },
    { id: 2, text: 'Buy groceries', completed: true, category: 'personal' },
    { id: 3, text: 'Walk dog', completed: false, category: 'personal' }
  ]);

  // Grouped rendering
  const groupedTodos = useMemo(() => {
    return todos.reduce((groups, todo) => {
      if (!groups[todo.category]) {
        groups[todo.category] = [];
      }
      groups[todo.category].push(todo);
      return groups;
    }, {});
  }, [todos]);

  return (
    <div>
      {Object.entries(groupedTodos).map(([category, categoryTodos]) => (
        <div key={category}> {/* ✅ Category as key */}
          <h3>{category}</h3>
          {categoryTodos.map((todo) => (
            <div key={todo.id}> {/* ✅ Todo ID as key */}
              <input
                type="checkbox"
                checked={todo.completed}
                onChange={() => toggleTodo(todo.id)}
              />
              {todo.text}
            </div>
          ))}
        </div>
      ))}
    </div>
  );

  function toggleTodo(id) {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  }
}

// 7. Virtual DOM Performance Tips
function PerformanceOptimizedList() {
  const [items, setItems] = useState([]);
  const [filter, setFilter] = useState('');

  // ✅ Memoize filtered items
  const filteredItems = useMemo(() => {
    return items.filter(item =>
      item.name.toLowerCase().includes(filter.toLowerCase())
    );
  }, [items, filter]);

  // ✅ Stable key generation
  const getItemKey = useCallback((item) => {
    // Use composite key if needed
    return `${item.id}-${item.version}`;
  }, []);

  return (
    <div>
      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="Filter items..."
      />

      <div>
        {filteredItems.map((item) => (
          <MemoizedItem
            key={getItemKey(item)} // ✅ Stable key function
            item={item}
          />
        ))}
      </div>
    </div>
  );
}

const MemoizedItem = memo(function Item({ item }) {
  return (
    <div>
      <h4>{item.name}</h4>
      <p>{item.description}</p>
    </div>
  );
});

// 8. Common Key Mistakes and Solutions
function KeyMistakesExample() {
  const [messages, setMessages] = useState([]);

  return (
    <div>
      {/* ❌ WRONG: Using random values */}
      {messages.map((msg) => (
        <div key={Math.random()}> {/* ❌ New key every render */}
          {msg.text}
        </div>
      ))}

      {/* ❌ WRONG: Using array index when order changes */}
      {messages.map((msg, index) => (
        <div key={index}> {/* ❌ Index changes when items move */}
          {msg.text}
        </div>
      ))}

      {/* ❌ WRONG: Non-unique keys */}
      {messages.map((msg) => (
        <div key={msg.type}> {/* ❌ Multiple messages of same type */}
          {msg.text}
        </div>
      ))}

      {/* ✅ CORRECT: Stable, unique identifiers */}
      {messages.map((msg) => (
        <div key={msg.id}> {/* ✅ Unique, stable ID */}
          {msg.text}
        </div>
      ))}
    </div>
  );
}
```

#### Q21: useRef vs useState, state vs props?

**Trả lời:**

```typescript
// 1. useRef vs useState - Fundamental Differences
import React, { useState, useRef, useEffect } from 'react';

function RefVsState() {
  // useState - triggers re-render when value changes
  const [count, setCount] = useState(0);

  // useRef - does NOT trigger re-render when value changes
  const countRef = useRef(0);
  const renderCount = useRef(0);

  // Track number of renders
  renderCount.current++;

  const incrementState = () => {
    setCount(prev => prev + 1); // ✅ Triggers re-render
    console.log('State updated, component will re-render');
  };

  const incrementRef = () => {
    countRef.current += 1; // ❌ No re-render triggered
    console.log('Ref updated, no re-render:', countRef.current);
  };

  console.log('Component rendered #', renderCount.current);

  return (
    <div>
      <h3>useState vs useRef</h3>
      <p>State count: {count}</p>
      <p>Ref count: {countRef.current}</p>
      <p>Render count: {renderCount.current}</p>

      <button onClick={incrementState}>Increment State (re-renders)</button>
      <button onClick={incrementRef}>Increment Ref (no re-render)</button>
    </div>
  );
}

// 2. useRef Use Cases
function RefUseCases() {
  // DOM references
  const inputRef = useRef(null);
  const divRef = useRef(null);

  // Previous values
  const [name, setName] = useState('');
  const prevNameRef = useRef('');

  // Mutable values that persist between renders
  const timerRef = useRef(null);
  const countRef = useRef(0);

  // Store previous value
  useEffect(() => {
    prevNameRef.current = name;
  });

  const focusInput = () => {
    inputRef.current?.focus();
  };

  const scrollToDiv = () => {
    divRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const startTimer = () => {
    if (timerRef.current) return; // Prevent multiple timers

    timerRef.current = setInterval(() => {
      countRef.current += 1;
      console.log('Timer count:', countRef.current);
    }, 1000);
  };

  const stopTimer = () => {
    if (timerRef.current) {
      clearInterval(timerRef.current);
      timerRef.current = null;
    }
  };

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      if (timerRef.current) {
        clearInterval(timerRef.current);
      }
    };
  }, []);

  return (
    <div>
      <h3>useRef Use Cases</h3>

      {/* DOM Reference */}
      <input
        ref={inputRef}
        value={name}
        onChange={(e) => setName(e.target.value)}
        placeholder="Type your name"
      />
      <button onClick={focusInput}>Focus Input</button>

      {/* Previous Value */}
      <p>Current name: {name}</p>
      <p>Previous name: {prevNameRef.current}</p>

      {/* Timer Control */}
      <button onClick={startTimer}>Start Timer</button>
      <button onClick={stopTimer}>Stop Timer</button>
      <p>Timer count (check console): {countRef.current}</p>

      {/* Scroll Reference */}
      <div style={{ height: '200px', overflow: 'auto' }}>
        <div style={{ height: '500px' }}>Scroll content...</div>
        <div ref={divRef} style={{ background: 'yellow' }}>
          Target div for scrolling
        </div>
      </div>
      <button onClick={scrollToDiv}>Scroll to Yellow Div</button>
    </div>
  );
}

// 3. State vs Props - Complete Comparison
// Props (Properties) - Data passed from parent to child
function ParentComponent() {
  const [userRole, setUserRole] = useState('user');
  const [theme, setTheme] = useState('light');

  return (
    <div>
      <h3>Parent Component (manages state)</h3>
      <button onClick={() => setUserRole(userRole === 'user' ? 'admin' : 'user')}>
        Toggle Role: {userRole}
      </button>
      <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
        Toggle Theme: {theme}
      </button>

      {/* Pass state as props to child */}
      <ChildComponent
        role={userRole}        // ✅ Props: read-only in child
        theme={theme}          // ✅ Props: read-only in child
        onRoleChange={setUserRole}  // ✅ Function to update parent state
      />
    </div>
  );
}

function ChildComponent({ role, theme, onRoleChange }) {
  // ✅ Child has its own state
  const [message, setMessage] = useState('');
  const [isExpanded, setIsExpanded] = useState(false);

  // ❌ Can't directly modify props
  // role = 'admin'; // This won't work!

  // ✅ Can call parent function to update parent state
  const requestAdminAccess = () => {
    onRoleChange('admin');
  };

  return (
    <div style={{
      background: theme === 'light' ? '#fff' : '#333',
      color: theme === 'light' ? '#000' : '#fff',
      padding: '20px',
      margin: '20px'
    }}>
      <h4>Child Component (receives props)</h4>
      <p>Role from props: {role}</p>
      <p>Theme from props: {theme}</p>

      {/* Child's own state */}
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Child's own message"
      />
      <p>Child's state: {message}</p>

      <button onClick={() => setIsExpanded(!isExpanded)}>
        {isExpanded ? 'Collapse' : 'Expand'} (Child State)
      </button>

      {isExpanded && (
        <div>
          <p>Expanded content controlled by child state</p>
          {role !== 'admin' && (
            <button onClick={requestAdminAccess}>
              Request Admin Access (Update Parent)
            </button>
          )}
        </div>
      )}
    </div>
  );
}

// 4. State Management Patterns
function StateManagementPatterns() {
  // Lifting state up example
  const [sharedData, setSharedData] = useState({
    cart: [],
    user: null,
    preferences: {}
  });

  // State that's local to this component
  const [localLoading, setLocalLoading] = useState(false);

  return (
    <div>
      <h3>State Management Patterns</h3>

      {/* Shared state passed as props */}
      <ShoppingCart
        cart={sharedData.cart}
        onUpdateCart={(newCart) => setSharedData(prev => ({ ...prev, cart: newCart }))}
      />

      <UserProfile
        user={sharedData.user}
        preferences={sharedData.preferences}
        onUpdateUser={(user) => setSharedData(prev => ({ ...prev, user }))}
      />

      {/* Local state not shared */}
      {localLoading && <div>Loading...</div>}
    </div>
  );
}

function ShoppingCart({ cart, onUpdateCart }) {
  // Local state for cart UI
  const [isMinimized, setIsMinimized] = useState(false);

  const addItem = (item) => {
    onUpdateCart([...cart, item]);
  };

  return (
    <div>
      <h4>Shopping Cart</h4>
      <button onClick={() => setIsMinimized(!isMinimized)}>
        {isMinimized ? 'Show' : 'Hide'} Cart
      </button>

      {!isMinimized && (
        <div>
          <p>Items: {cart.length}</p>
          <button onClick={() => addItem({ id: Date.now(), name: 'New Item' })}>
            Add Item
          </button>
        </div>
      )}
    </div>
  );
}

function UserProfile({ user, preferences, onUpdateUser }) {
  // Derived state from props
  const isLoggedIn = !!user;

  // Local form state
  const [formData, setFormData] = useState({
    name: user?.name || '',
    email: user?.email || ''
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    onUpdateUser({
      ...user,
      ...formData
    });
  };

  if (!isLoggedIn) {
    return <div>Please log in</div>;
  }

  return (
    <div>
      <h4>User Profile</h4>
      <form onSubmit={handleSubmit}>
        <input
          value={formData.name}
          onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
          placeholder="Name"
        />
        <input
          value={formData.email}
          onChange={(e) => setFormData(prev => ({ ...prev, email: e.target.value }))}
          placeholder="Email"
        />
        <button type="submit">Update Profile</button>
      </form>
    </div>
  );
}

// 5. When to use useState vs useRef
/*
Use useState when:
✅ Value changes should trigger re-renders
✅ Value is displayed in UI
✅ Value affects component appearance/behavior
✅ Need React to track changes for optimization

Use useRef when:
✅ Need to persist value between renders without re-rendering
✅ Storing DOM references
✅ Storing mutable values (timers, counters, flags)
✅ Storing previous values
✅ Caching expensive computations
✅ Preventing infinite loops in useEffect
*/

// 6. Anti-patterns and Best Practices
function AntiPatterns() {
  const [count, setCount] = useState(0);
  const badRef = useRef(0);

  // ❌ DON'T: Modify ref during render
  // badRef.current = count; // This can cause issues

  // ✅ DO: Modify ref in useEffect or event handlers
  useEffect(() => {
    badRef.current = count;
  });

  // ❌ DON'T: Use ref for values that should trigger re-renders
  const handleBadClick = () => {
    badRef.current += 1; // UI won't update
  };

  // ✅ DO: Use state for reactive values
  const handleGoodClick = () => {
    setCount(prev => prev + 1); // UI updates
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleGoodClick}>Good: Use State</button>
      <button onClick={handleBadClick}>Bad: Use Ref</button>
    </div>
  );
}
```

#### Q22: useMemo vs useCallback chi tiết?

**Trả lời:**

**Giải thích:**
- **useMemo**: Cache kết quả của một phép tính (memoize value)
- **useCallback**: Cache một function (memoize function)
- **Mục đích**: Tối ưu performance bằng cách tránh tính toán/tạo function không cần thiết

```typescript
// 1. useMemo vs useCallback - Sự khác biệt cơ bản
import React, { useState, useMemo, useCallback, memo, ReactNode } from 'react';

interface MemoVsCallbackProps {}

function MemoVsCallback(): JSX.Element {
  const [count, setCount] = useState<number>(0);
  const [items, setItems] = useState<string[]>(['apple', 'banana', 'cherry']);
  const [multiplier, setMultiplier] = useState<number>(2);

  // ✅✅✅ useMemo - CACHE KẾT QUẢ của một phép tính
  const expensiveValue = useMemo<number>(() => {
    console.log('🔢 Đang tính toán giá trị đắt...');
    // 💰 EXPENSIVE CALCULATION - chỉ chạy lại khi dependencies thay đổi
    return items.reduce((sum, item) => sum + item.length, 0) * multiplier;
  }, [items, multiplier]);
  // ⬆️ 🎯 CHỈ TÍNH LẠI khi items hoặc multiplier thay đổi
  // ⬆️ 🚀 SKIP CALCULATION nếu dependencies không đổi

  // ✅✅✅ useCallback - CACHE một FUNCTION
  const addItem = useCallback((): void => {
    console.log('🔧 Tạo function addItem...');
    setItems(prev => [...prev, `item-${Date.now()}`]);
  }, []); // 🔒 DEPENDENCIES EMPTY = function reference KHÔNG BAO GIỜ thay đổi
  // ⬆️ 🎯 SAME FUNCTION REFERENCE qua tất cả re-renders

  // ❌❌❌ CÁCH SAI - Tạo function mới mỗi lần render
  const badAddItem = (): void => {
    console.log('❌ Tạo function mới mỗi lần render');
    setItems(prev => [...prev, `item-${Date.now()}`]);
  };
  // ⬆️ 🚨 NEW FUNCTION REFERENCE mỗi re-render
  // ⬆️ 💸 Làm child components re-render không cần thiết nếu pass function này làm prop

  /*
  🧠 KHI NÀO DÙNG useMemo vs useCallback?

  📊 useMemo - Dùng khi:
  ✅ Có expensive calculation (sort, filter, reduce large arrays)
  ✅ Tạo object/array mới để pass xuống child components
  ✅ Derived state từ props/state
  ❌ KHÔNG dùng cho simple calculations (a + b, string concatenation)

  🎯 useCallback - Dùng khi:
  ✅ Pass function xuống memoized child components
  ✅ Function là dependency của useEffect/useMemo khác
  ✅ Function được tạo trong expensive component
  ❌ KHÔNG dùng nếu child component không được memoized
  */

  console.log('🔄 Component rendered');

  return (
    <div>
      <h3>useMemo vs useCallback</h3>
      <p>Count: {count}</p>
      <p>Expensive Value: {expensiveValue}</p>
      <p>Items: {items.length}</p>

      <button onClick={() => setCount(count + 1)}>
        Increment Count (doesn't recompute expensive value)
      </button>
      <button onClick={() => setMultiplier(multiplier + 1)}>
        Change Multiplier (recomputes expensive value)
      </button>

      {/* Child components that receive callbacks */}
      <MemoizedChild
        onAddGood={addItem}     // ✅ Stable function reference
        onAddBad={badAddItem}   // ❌ New function every render
      />
    </div>
  );
}

// Child component with React.memo
const MemoizedChild = memo(function MemoizedChild({ onAddGood, onAddBad }) {
  console.log('👶 Child component rendered');

  return (
    <div style={{ background: '#f0f0f0', padding: '10px', margin: '10px' }}>
      <h4>Child Component</h4>
      <button onClick={onAddGood}>
        Add Item (Good - useCallback)
      </button>
      <button onClick={onAddBad}>
        Add Item (Bad - new function)
      </button>
    </div>
  );
});

// 2. Performance Comparison Examples
function PerformanceComparison() {
  const [filter, setFilter] = useState('');
  const [sortBy, setSortBy] = useState('name');
  const [users, setUsers] = useState([
    { id: 1, name: 'John Doe', age: 30, department: 'Engineering' },
    { id: 2, name: 'Jane Smith', age: 25, department: 'Design' },
    { id: 3, name: 'Bob Johnson', age: 35, department: 'Engineering' },
    { id: 4, name: 'Alice Brown', age: 28, department: 'Marketing' }
  ]);

  // ✅ GOOD: Memoized expensive computation
  const filteredAndSortedUsers = useMemo(() => {
    console.log('🔍 Filtering and sorting users...');

    let filtered = users.filter(user =>
      user.name.toLowerCase().includes(filter.toLowerCase()) ||
      user.department.toLowerCase().includes(filter.toLowerCase())
    );

    return filtered.sort((a, b) => {
      if (sortBy === 'name') return a.name.localeCompare(b.name);
      if (sortBy === 'age') return a.age - b.age;
      return a.department.localeCompare(b.department);
    });
  }, [users, filter, sortBy]); // Only recomputes when dependencies change

  // ✅ GOOD: Memoized callback functions
  const handleUserUpdate = useCallback((userId, updates) => {
    console.log('👥 Updating user...');
    setUsers(prev => prev.map(user =>
      user.id === userId ? { ...user, ...updates } : user
    ));
  }, []); // Stable function reference

  const handleUserDelete = useCallback((userId) => {
    console.log('🗑️ Deleting user...');
    setUsers(prev => prev.filter(user => user.id !== userId));
  }, []); // Stable function reference

  // ❌ BAD: Would recompute every render
  // const badFilteredUsers = users.filter(user =>
  //   user.name.toLowerCase().includes(filter.toLowerCase())
  // ).sort((a, b) => a.name.localeCompare(b.name));

  return (
    <div>
      <h3>Performance Comparison</h3>

      <input
        value={filter}
        onChange={(e) => setFilter(e.target.value)}
        placeholder="Filter users..."
      />

      <select value={sortBy} onChange={(e) => setSortBy(e.target.value)}>
        <option value="name">Sort by Name</option>
        <option value="age">Sort by Age</option>
        <option value="department">Sort by Department</option>
      </select>

      <div>
        <h4>Filtered Users ({filteredAndSortedUsers.length}):</h4>
        {filteredAndSortedUsers.map(user => (
          <UserCard
            key={user.id}
            user={user}
            onUpdate={handleUserUpdate}  // ✅ Stable callback
            onDelete={handleUserDelete}  // ✅ Stable callback
          />
        ))}
      </div>
    </div>
  );
}

const UserCard = memo(function UserCard({ user, onUpdate, onDelete }) {
  console.log(`👤 UserCard rendered for ${user.name}`);

  const handleAgeIncrement = useCallback(() => {
    onUpdate(user.id, { age: user.age + 1 });
  }, [user.id, user.age, onUpdate]);

  return (
    <div style={{
      border: '1px solid #ccc',
      padding: '10px',
      margin: '5px',
      background: '#fafafa'
    }}>
      <h5>{user.name}</h5>
      <p>Age: {user.age} | Department: {user.department}</p>
      <button onClick={handleAgeIncrement}>+1 Age</button>
      <button onClick={() => onDelete(user.id)}>Delete</button>
    </div>
  );
});

// 3. When to use useMemo
function UseMemoExamples() {
  const [searchTerm, setSearchTerm] = useState('');
  const [data, setData] = useState([]);
  const [threshold, setThreshold] = useState(10);

  // ✅ Expensive computation - good for useMemo
  const processedData = useMemo(() => {
    console.log('Processing large dataset...');
    return data
      .filter(item => item.value > threshold)
      .map(item => ({
        ...item,
        processed: true,
        score: item.value * 2.5,
        category: item.value > 50 ? 'high' : 'medium'
      }))
      .sort((a, b) => b.score - a.score);
  }, [data, threshold]);

  // ✅ Derived state - good for useMemo
  const statistics = useMemo(() => {
    if (processedData.length === 0) return null;

    return {
      total: processedData.length,
      average: processedData.reduce((sum, item) => sum + item.score, 0) / processedData.length,
      highest: Math.max(...processedData.map(item => item.score)),
      lowest: Math.min(...processedData.map(item => item.score))
    };
  }, [processedData]);

  // ✅ Complex object creation - good for useMemo
  const chartConfig = useMemo(() => ({
    type: 'bar',
    data: processedData.slice(0, 10),
    options: {
      responsive: true,
      scales: {
        y: { beginAtZero: true }
      }
    }
  }), [processedData]);

  // ❌ DON'T use useMemo for simple computations
  // const simpleComputation = useMemo(() => searchTerm.length, [searchTerm]);
  // ✅ DO this instead:
  const simpleComputation = searchTerm.length;

  return (
    <div>
      <h3>useMemo Examples</h3>
      <input
        value={searchTerm}
        onChange={(e) => setSearchTerm(e.target.value)}
        placeholder="Search..."
      />
      <input
        type="number"
        value={threshold}
        onChange={(e) => setThreshold(Number(e.target.value))}
      />

      <p>Simple computation: {simpleComputation}</p>
      <p>Processed items: {processedData.length}</p>

      {statistics && (
        <div>
          <h4>Statistics:</h4>
          <p>Average: {statistics.average.toFixed(2)}</p>
          <p>Range: {statistics.lowest} - {statistics.highest}</p>
        </div>
      )}
    </div>
  );
}

// 4. When to use useCallback
function UseCallbackExamples() {
  const [todos, setTodos] = useState([]);
  const [filter, setFilter] = useState('all');

  // ✅ Callback passed to child components - good for useCallback
  const addTodo = useCallback((text) => {
    const newTodo = {
      id: Date.now(),
      text,
      completed: false,
      createdAt: new Date()
    };
    setTodos(prev => [...prev, newTodo]);
  }, []); // No dependencies, function never changes

  const toggleTodo = useCallback((id) => {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, completed: !todo.completed } : todo
    ));
  }, []); // No dependencies, function never changes

  const deleteTodo = useCallback((id) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  }, []); // No dependencies, function never changes

  // ✅ Callback with dependencies - good for useCallback
  const updateTodoText = useCallback((id, newText) => {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, text: newText } : todo
    ));
  }, []); // Function recreated only when dependencies change

  // ✅ Event handler passed to multiple children - good for useCallback
  const handleBulkAction = useCallback((action) => {
    switch (action) {
      case 'complete-all':
        setTodos(prev => prev.map(todo => ({ ...todo, completed: true })));
        break;
      case 'delete-completed':
        setTodos(prev => prev.filter(todo => !todo.completed));
        break;
      case 'clear-all':
        setTodos([]);
        break;
    }
  }, []); // Stable function reference

  const filteredTodos = useMemo(() => {
    switch (filter) {
      case 'active': return todos.filter(todo => !todo.completed);
      case 'completed': return todos.filter(todo => todo.completed);
      default: return todos;
    }
  }, [todos, filter]);

  return (
    <div>
      <h3>useCallback Examples</h3>

      <TodoInput onAdd={addTodo} />
      <FilterButtons filter={filter} onFilterChange={setFilter} />
      <BulkActions onBulkAction={handleBulkAction} />

      <div>
        {filteredTodos.map(todo => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
            onUpdate={updateTodoText}
          />
        ))}
      </div>
    </div>
  );
}

const TodoInput = memo(function TodoInput({ onAdd }) {
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (text.trim()) {
      onAdd(text.trim());
      setText('');
    }
  };

  console.log('📝 TodoInput rendered');

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add new todo..."
      />
      <button type="submit">Add</button>
    </form>
  );
});

const TodoItem = memo(function TodoItem({ todo, onToggle, onDelete, onUpdate }) {
  const [isEditing, setIsEditing] = useState(false);
  const [editText, setEditText] = useState(todo.text);

  console.log(`✅ TodoItem rendered for: ${todo.text}`);

  const handleSave = () => {
    onUpdate(todo.id, editText);
    setIsEditing(false);
  };

  return (
    <div style={{
      display: 'flex',
      alignItems: 'center',
      padding: '5px',
      background: todo.completed ? '#e8f5e8' : '#fff'
    }}>
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo.id)}
      />

      {isEditing ? (
        <input
          value={editText}
          onChange={(e) => setEditText(e.target.value)}
          onBlur={handleSave}
          onKeyPress={(e) => e.key === 'Enter' && handleSave()}
        />
      ) : (
        <span
          onClick={() => setIsEditing(true)}
          style={{
            textDecoration: todo.completed ? 'line-through' : 'none',
            cursor: 'pointer',
            flex: 1,
            padding: '5px'
          }}
        >
          {todo.text}
        </span>
      )}

      <button onClick={() => onDelete(todo.id)}>Delete</button>
    </div>
  );
});

// 5. Common Mistakes and Best Practices
function CommonMistakes() {
  const [count, setCount] = useState(0);
  const [name, setName] = useState('');

  // ❌ MISTAKE: Unnecessary useMemo for simple values
  const badMemo = useMemo(() => count * 2, [count]); // Don't do this!

  // ✅ CORRECT: Simple computation, no memo needed
  const goodComputation = count * 2; // Do this instead

  // ❌ MISTAKE: useMemo with changing dependencies
  const badMemoWithFunction = useMemo(() => {
    return () => console.log('Hello'); // New function every time
  }, []); // Dependencies are wrong!

  // ✅ CORRECT: useCallback for function memoization
  const goodCallback = useCallback(() => {
    console.log('Hello');
  }, []);

  // ❌ MISTAKE: useCallback without memo child
  const unnecessaryCallback = useCallback(() => {
    console.log('This callback is not needed');
  }, []);

  return (
    <div>
      <h3>Common Mistakes</h3>
      <p>Count: {count}</p>
      <p>Simple computation: {goodComputation}</p>

      <button onClick={() => setCount(count + 1)}>Increment</button>

      {/* This child doesn't use memo, so useCallback is unnecessary */}
      <RegularChild onClick={unnecessaryCallback} />

      {/* This child uses memo, so useCallback is beneficial */}
      <MemoizedChildForCallback onClick={goodCallback} />
    </div>
  );
}

const RegularChild = ({ onClick }) => {
  console.log('Regular child rendered');
  return <button onClick={onClick}>Regular Child</button>;
};

const MemoizedChildForCallback = memo(({ onClick }) => {
  console.log('Memoized child rendered');
  return <button onClick={onClick}>Memoized Child</button>;
});

// 6. Performance Guidelines
/*
useMemo Guidelines:
✅ DO use for expensive computations
✅ DO use for derived state from props/state
✅ DO use for complex object creation
❌ DON'T use for simple calculations
❌ DON'T use if dependencies change every render
❌ DON'T use for primitive values

useCallback Guidelines:
✅ DO use for callbacks passed to memoized child components
✅ DO use for event handlers in dependency arrays
✅ DO use for functions that create closures
❌ DON'T use if child components aren't memoized
❌ DON'T use for functions that don't depend on props/state
❌ DON'T use if the function changes every render anyway
*/
```

#### Q23: Parent re-renders thì child có re-render? Cách optimize?

**Trả lời:**

**🎯 React Re-render Rules:**

**📏 QUY LUẬT CỐT LÕI:**
```
🔄 Parent re-render → 🔄 ALL children re-render (by default)
```

**🚨 NHƯNG:** Child chỉ re-render DOM nếu Virtual DOM thay đổi thực sự

**📊 Re-render Decision Tree:**
```
Parent re-render
    ↓
Child props same?
    ↓ NO → Re-render
    ↓ YES → Check memo/optimization
        ↓ No memo → Re-render anyway
        ↓ Has memo → Skip re-render ✅
```

**🧠 GHI NHỚ:**
- **Default**: **P**arent **R**enders → **A**ll **C**hildren **R**ender (**PRACR**)
- **Optimized**: **M**emo **S**tops **U**nnecessary **R**enders (**MSUR**)

**🛠️ OPTIMIZATION STRATEGIES:**
1. **🎯 React.memo** - Skip re-render if props same
2. **🔒 useMemo** - Stable object/array props
3. **⚡ useCallback** - Stable function props
4. **✂️ Component splitting** - Isolate state changes

```typescript
// 1. Default Behavior - Child ALWAYS re-renders when parent re-renders
import React, { useState, memo, useCallback, useMemo } from 'react';

function ParentWithAlwaysRerender() {
  const [parentCount, setParentCount] = useState(0);
  const [otherState, setOtherState] = useState('');

  console.log('🔄 Parent rendered');

  return (
    <div>
      <h3>Parent Component</h3>
      <p>Parent count: {parentCount}</p>
      <p>Other state: {otherState}</p>

      <button onClick={() => setParentCount(prev => prev + 1)}>
        Increment Parent Count
      </button>
      <button onClick={() => setOtherState('changed')}>
        Change Other State
      </button>

      {/* ❌ Child ALWAYS re-renders when parent re-renders */}
      <RegularChild value="static value" />
      <RegularChild value={parentCount} />
    </div>
  );
}

function RegularChild({ value }) {
  console.log('👶 Regular Child rendered with value:', value);

  return (
    <div style={{ background: '#ffeeee', padding: '10px', margin: '5px' }}>
      <p>Child value: {value}</p>
    </div>
  );
}

// 2. Optimization với React.memo
function ParentWithMemoization() {
  const [parentCount, setParentCount] = useState(0);
  const [otherState, setOtherState] = useState('');

  console.log('🔄 Parent rendered');

  return (
    <div>
      <h3>Parent with Memoized Children</h3>
      <p>Parent count: {parentCount}</p>
      <p>Other state: {otherState}</p>

      <button onClick={() => setParentCount(prev => prev + 1)}>
        Increment Parent Count
      </button>
      <button onClick={() => setOtherState('changed')}>
        Change Other State
      </button>

      {/* ✅ Only re-renders when value actually changes */}
      <MemoizedChild value="static value" />
      <MemoizedChild value={parentCount} />
    </div>
  );
}

const MemoizedChild = memo(function MemoizedChild({ value }) {
  console.log('👶 Memoized Child rendered with value:', value);

  return (
    <div style={{ background: '#eeffee', padding: '10px', margin: '5px' }}>
      <p>Memoized Child value: {value}</p>
    </div>
  );
});

// 3. Problem với Object/Array props
function ParentWithObjectProps() {
  const [count, setCount] = useState(0);

  // ❌ BAD: New object every render
  const badUserData = {
    name: 'John',
    age: 30
  };

  // ❌ BAD: New array every render
  const badItems = ['item1', 'item2', 'item3'];

  // ❌ BAD: New function every render
  const badCallback = () => {
    console.log('Button clicked');
  };

  console.log('🔄 Parent with objects rendered');

  return (
    <div>
      <h3>Parent with Object Props (Problem)</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(prev => prev + 1)}>Increment</button>

      {/* ❌ Memo won't help - props are always "different" */}
      <MemoizedChildWithObjects
        user={badUserData}     // New object reference
        items={badItems}       // New array reference
        onClick={badCallback}  // New function reference
      />
    </div>
  );
}

const MemoizedChildWithObjects = memo(function MemoizedChildWithObjects({
  user,
  items,
  onClick
}) {
  console.log('👶 Child with objects rendered - memo didnt help!');

  return (
    <div style={{ background: '#ffeeaa', padding: '10px', margin: '5px' }}>
      <p>User: {user.name}, Age: {user.age}</p>
      <p>Items: {items.join(', ')}</p>
      <button onClick={onClick}>Click me</button>
    </div>
  );
});

// 4. Solution với useMemo và useCallback
function ParentWithOptimizedProps() {
  const [count, setCount] = useState(0);
  const [userName, setUserName] = useState('John');

  // ✅ GOOD: Stable object reference
  const userData = useMemo(() => ({
    name: userName,
    age: 30
  }), [userName]); // Only changes when userName changes

  // ✅ GOOD: Stable array reference
  const items = useMemo(() => ['item1', 'item2', 'item3'], []); // Never changes

  // ✅ GOOD: Stable function reference
  const handleClick = useCallback(() => {
    console.log('Button clicked');
  }, []); // Never changes

  console.log('🔄 Parent with optimized props rendered');

  return (
    <div>
      <h3>Parent with Optimized Props</h3>
      <p>Count: {count}</p>
      <button onClick={() => setCount(prev => prev + 1)}>
        Increment Count (child won't re-render)
      </button>
      <button onClick={() => setUserName(userName === 'John' ? 'Jane' : 'John')}>
        Change Name (child will re-render)
      </button>

      {/* ✅ Memo works properly now */}
      <MemoizedChildWithOptimizedProps
        user={userData}
        items={items}
        onClick={handleClick}
      />
    </div>
  );
}

const MemoizedChildWithOptimizedProps = memo(function MemoizedChildWithOptimizedProps({
  user,
  items,
  onClick
}) {
  console.log('👶 Optimized child rendered');

  return (
    <div style={{ background: '#aaffaa', padding: '10px', margin: '5px' }}>
      <p>User: {user.name}, Age: {user.age}</p>
      <p>Items: {items.join(', ')}</p>
      <button onClick={onClick}>Click me</button>
    </div>
  );
});

// 5. Advanced Optimization Patterns
function SmartParent() {
  const [globalCount, setGlobalCount] = useState(0);
  const [userFilter, setUserFilter] = useState('');
  const [users] = useState([
    { id: 1, name: 'John', department: 'Engineering' },
    { id: 2, name: 'Jane', department: 'Design' },
    { id: 3, name: 'Bob', department: 'Marketing' }
  ]);

  // ✅ Separate memoized computations
  const filteredUsers = useMemo(() => {
    console.log('🔍 Filtering users...');
    return users.filter(user =>
      user.name.toLowerCase().includes(userFilter.toLowerCase())
    );
  }, [users, userFilter]);

  const userStats = useMemo(() => {
    console.log('📊 Computing user stats...');
    return {
      total: users.length,
      engineering: users.filter(u => u.department === 'Engineering').length,
      design: users.filter(u => u.department === 'Design').length,
      marketing: users.filter(u => u.department === 'Marketing').length
    };
  }, [users]); // Independent of filter

  // ✅ Stable callbacks
  const handleUserSelect = useCallback((userId) => {
    console.log('User selected:', userId);
  }, []);

  console.log('🔄 Smart parent rendered');

  return (
    <div>
      <h3>Smart Parent with Optimizations</h3>

      <div>
        <p>Global count: {globalCount}</p>
        <button onClick={() => setGlobalCount(prev => prev + 1)}>
          Increment Global Count
        </button>
      </div>

      <div>
        <input
          value={userFilter}
          onChange={(e) => setUserFilter(e.target.value)}
          placeholder="Filter users..."
        />
      </div>

      {/* ✅ Independent components with different optimization strategies */}
      <UserList users={filteredUsers} onUserSelect={handleUserSelect} />
      <UserStats stats={userStats} />
      <GlobalCounter count={globalCount} />
    </div>
  );
}

// Component that depends on filtered data
const UserList = memo(function UserList({ users, onUserSelect }) {
  console.log('📋 UserList rendered with', users.length, 'users');

  return (
    <div style={{ background: '#e6f3ff', padding: '10px', margin: '5px' }}>
      <h4>User List ({users.length})</h4>
      {users.map(user => (
        <button
          key={user.id}
          onClick={() => onUserSelect(user.id)}
          style={{ margin: '2px', padding: '5px' }}
        >
          {user.name} - {user.department}
        </button>
      ))}
    </div>
  );
});

// Component that depends on stats (independent of filter)
const UserStats = memo(function UserStats({ stats }) {
  console.log('📊 UserStats rendered');

  return (
    <div style={{ background: '#fff3e6', padding: '10px', margin: '5px' }}>
      <h4>User Statistics</h4>
      <p>Total: {stats.total}</p>
      <p>Engineering: {stats.engineering}</p>
      <p>Design: {stats.design}</p>
      <p>Marketing: {stats.marketing}</p>
    </div>
  );
});

// Component that only depends on global state
const GlobalCounter = memo(function GlobalCounter({ count }) {
  console.log('🔢 GlobalCounter rendered');

  return (
    <div style={{ background: '#f0f0f0', padding: '10px', margin: '5px' }}>
      <h4>Global Counter: {count}</h4>
    </div>
  );
});

// 6. Custom memo with specific comparison
const ExpensiveChild = memo(function ExpensiveChild({ user, theme, data }) {
  console.log('💰 Expensive child rendered');

  // Simulate expensive computation
  const processedData = useMemo(() => {
    let result = 0;
    for (let i = 0; i < 100000; i++) {
      result += i;
    }
    return result + data.value;
  }, [data.value]);

  return (
    <div style={{
      background: theme === 'dark' ? '#333' : '#fff',
      color: theme === 'dark' ? '#fff' : '#000',
      padding: '10px',
      margin: '5px'
    }}>
      <h4>{user.name}</h4>
      <p>Processed: {processedData}</p>
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison function
  // Return true if props are equal (don't re-render)
  // Return false if props are different (do re-render)
  return (
    prevProps.user.id === nextProps.user.id &&
    prevProps.user.name === nextProps.user.name &&
    prevProps.theme === nextProps.theme &&
    prevProps.data.value === nextProps.data.value
  );
});

// 7. Summary of optimization strategies
/*
React Re-render Rules:
1. Parent re-renders → All children re-render (by default)
2. State change → Component re-renders
3. Props change → Component re-renders
4. Context change → All consumers re-render

Optimization Techniques:
✅ React.memo - Prevents re-render if props are the same
✅ useMemo - Memoizes expensive computations
✅ useCallback - Memoizes function references
✅ Split state - Separate fast-changing from slow-changing state
✅ Lift content up - Move static content to parent
✅ Custom comparison - memo with custom areEqual function

Performance Guidelines:
📝 Profile first, optimize second
📝 Don't optimize prematurely
📝 Measure the impact of optimizations
📝 Consider the cost of optimization vs benefit
📝 Sometimes re-rendering is fine and fast
*/
```

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

**Ưu điểm Functional Components:**
- Code ngắn gọn hơn
- Dễ test
- Performance tốt hơn
- Hooks cung cấp logic reuse tốt hơn

#### Q4: useState Hook hoạt động như thế nào?

**Trả lời:**
useState cho phép thêm state vào functional components.

```typescript
function Counter() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState({ name: '', email: '' });

  // Cập nhật đơn giản
  const increment = () => setCount(count + 1);

  // Cập nhật với function (tránh stale closure)
  const incrementCorrect = () => setCount(prevCount => prevCount + 1);

  // Cập nhật object state
  const updateUser = (field, value) => {
    setUser(prevUser => ({
      ...prevUser,
      [field]: value
    }));
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={increment}>Increment</button>
      <button onClick={incrementCorrect}>Increment Correct</button>

      <input
        value={user.name}
        onChange={(e) => updateUser('name', e.target.value)}
        placeholder="Name"
      />
    </div>
  );
}
```

---

## Câu Hỏi Trung Cấp (Mid-Level)

### 3. Advanced React Concepts

#### Q5: useEffect Hook và lifecycle methods tương ứng?

**Trả lời:**

```typescript
function ComponentLifecycle() {
  const [count, setCount] = useState(0);
  const [user, setUser] = useState(null);

  // componentDidMount
  useEffect(() => {
    console.log('Component mounted');
    fetchUser();
  }, []); // Empty dependency array

  // componentDidUpdate cho count
  useEffect(() => {
    console.log('Count updated:', count);
    document.title = `Count: ${count}`;
  }, [count]); // Dependency array với count

  // componentWillUnmount
  useEffect(() => {
    const timer = setInterval(() => {
      console.log('Timer tick');
    }, 1000);

    return () => {
      console.log('Cleanup timer');
      clearInterval(timer);
    };
  }, []);

  // Combination của multiple effects
  useEffect(() => {
    if (user) {
      const subscription = subscribeToUserUpdates(user.id);
      return () => subscription.unsubscribe();
    }
  }, [user]);

  const fetchUser = async () => {
    try {
      const userData = await api.getUser();
      setUser(userData);
    } catch (error) {
      console.error('Failed to fetch user:', error);
    }
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      {user && <p>User: {user.name}</p>}
    </div>
  );
}
```

#### Q6: Custom Hooks - Cách tạo và sử dụng?

**Trả lời:**

```typescript
// Custom Hook: useLocalStorage
function useLocalStorage(key, initialValue) {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error('Error reading localStorage:', error);
      return initialValue;
    }
  });

  const setValue = (value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error('Error setting localStorage:', error);
    }
  };

  return [storedValue, setValue];
}

// Custom Hook: useFetch
function useFetch(url) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const abortController = new AbortController();

    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url, {
          signal: abortController.signal
        });

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        setData(result);
        setError(null);
      } catch (err) {
        if (err.name !== 'AbortError') {
          setError(err.message);
        }
      } finally {
        setLoading(false);
      }
    };

    fetchData();

    return () => abortController.abort();
  }, [url]);

  return { data, loading, error };
}

// Sử dụng Custom Hooks
function UserProfile({ userId }) {
  const [preferences, setPreferences] = useLocalStorage('userPreferences', {});
  const { data: user, loading, error } = useFetch(`/api/users/${userId}`);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error}</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>Theme: {preferences.theme || 'light'}</p>
      <button
        onClick={() => setPreferences(prev => ({
          ...prev,
          theme: prev.theme === 'light' ? 'dark' : 'light'
        }))}
      >
        Toggle Theme
      </button>
    </div>
  );
}
```

#### Q7: Context API vs Redux - Khi nào nên sử dụng?

**Trả lời:**

```typescript
// Context API - Tốt cho state ít thay đổi
const ThemeContext = createContext();

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light');

  const value = {
    theme,
    toggleTheme: () => setTheme(prev => prev === 'light' ? 'dark' : 'light')
  };

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
}

function useTheme() {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
}

// Redux - Tốt cho state phức tạp, nhiều thay đổi
const userSlice = createSlice({
  name: 'user',
  initialState: {
    profile: null,
    loading: false,
    error: null
  },
  reducers: {
    fetchUserStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    fetchUserSuccess: (state, action) => {
      state.loading = false;
      state.profile = action.payload;
    },
    fetchUserFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
    }
  }
});

// Async thunk
const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId, { rejectWithValue }) => {
    try {
      const response = await api.getUser(userId);
      return response.data;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);
```

**Khi nào sử dụng:**
- **Context API**: Theme, user authentication, language settings
- **Redux**: Shopping cart, complex forms, real-time data updates

---

## Câu Hỏi Nâng Cao (Senior Level)

### 4. Performance & Optimization

#### Q8: React.memo, useMemo, useCallback - Khi nào và cách sử dụng?

**Trả lời:**

```typescript
// React.memo - Prevent unnecessary re-renders
const ExpensiveComponent = React.memo(({ data, onUpdate }) => {
  console.log('ExpensiveComponent rendered');

  return (
    <div>
      {data.map(item => (
        <div key={item.id} onClick={() => onUpdate(item.id)}>
          {item.name}
        </div>
      ))}
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison function (optional)
  return prevProps.data.length === nextProps.data.length &&
         prevProps.data.every((item, index) =>
           item.id === nextProps.data[index].id
         );
});

function ParentComponent() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([
    { id: 1, name: 'Item 1' },
    { id: 2, name: 'Item 2' }
  ]);

  // useMemo - Memoize expensive calculations
  const expensiveValue = useMemo(() => {
    console.log('Calculating expensive value...');
    return items.reduce((sum, item) => sum + item.id, 0) * 1000;
  }, [items]);

  // useCallback - Memoize functions
  const handleUpdate = useCallback((itemId) => {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === itemId
          ? { ...item, name: `Updated ${item.name}` }
          : item
      )
    );
  }, []); // No dependencies needed since we use functional update

  // Without useCallback, this function is recreated on every render
  const handleUpdateBad = (itemId) => {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === itemId
          ? { ...item, name: `Updated ${item.name}` }
          : item
      )
    );
  };

  return (
    <div>
      <p>Count: {count}</p>
      <p>Expensive Value: {expensiveValue}</p>
      <button onClick={() => setCount(c => c + 1)}>
        Increment Count
      </button>

      <ExpensiveComponent
        data={items}
        onUpdate={handleUpdate}
      />
    </div>
  );
}
```

#### Q9: Code Splitting và Lazy Loading trong React?

**Trả lời:**

```typescript
import { lazy, Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Dynamic imports với React.lazy
const Home = lazy(() => import('./pages/Home'));
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Profile = lazy(() =>
  import('./pages/Profile').then(module => ({
    default: module.Profile // Named export
  }))
);

// Component-level splitting
const HeavyChart = lazy(() =>
  import('./components/HeavyChart').then(module => {
    // Pre-load dependencies
    return Promise.all([
      module.default,
      import('./utils/chartHelpers')
    ]).then(([Component]) => ({ default: Component }));
  })
);

// Loading component
function LoadingSpinner() {
  return (
    <div className="loading-container">
      <div className="spinner">Loading...</div>
    </div>
  );
}

// Error Boundary cho lazy loading
class LazyLoadErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Lazy loading error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div>
          <h2>Something went wrong loading this component.</h2>
          <button onClick={() => window.location.reload()}>
            Reload Page
          </button>
        </div>
      );
    }

    return this.props.children;
  }
}

// Main App với code splitting
function App() {
  return (
    <Router>
      <LazyLoadErrorBoundary>
        <Suspense fallback={<LoadingSpinner />}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/profile" element={<Profile />} />
          </Routes>
        </Suspense>
      </LazyLoadErrorBoundary>
    </Router>
  );
}

// Advanced: Dynamic import với conditions
function DynamicComponentLoader({ type, data }) {
  const [Component, setComponent] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadComponent = async () => {
      try {
        let module;
        switch (type) {
          case 'chart':
            module = await import('./components/Chart');
            break;
          case 'table':
            module = await import('./components/Table');
            break;
          case 'graph':
            module = await import('./components/Graph');
            break;
          default:
            module = await import('./components/Default');
        }
        setComponent(() => module.default);
      } catch (error) {
        console.error('Failed to load component:', error);
      } finally {
        setLoading(false);
      }
    };

    loadComponent();
  }, [type]);

  if (loading) return <LoadingSpinner />;
  if (!Component) return <div>Failed to load component</div>;

  return <Component data={data} />;
}
```

### 5. Advanced Patterns

#### Q10: Higher-Order Components (HOC) vs Render Props vs Custom Hooks?

**Trả lời:**

```typescript
// 1. Higher-Order Component (HOC)
function withAuth(WrappedComponent) {
  return function WithAuthComponent(props) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
      const checkAuth = async () => {
        try {
          const userData = await authService.getCurrentUser();
          setUser(userData);
        } catch (error) {
          console.error('Auth check failed:', error);
        } finally {
          setLoading(false);
        }
      };

      checkAuth();
    }, []);

    if (loading) return <div>Checking authentication...</div>;
    if (!user) return <div>Please log in</div>;

    return <WrappedComponent {...props} user={user} />;
  };
}

// Sử dụng HOC
const ProtectedDashboard = withAuth(Dashboard);

// 2. Render Props Pattern
class AuthProvider extends React.Component {
  state = {
    user: null,
    loading: true,
    error: null
  };

  componentDidMount() {
    this.checkAuth();
  }

  checkAuth = async () => {
    try {
      const user = await authService.getCurrentUser();
      this.setState({ user, loading: false });
    } catch (error) {
      this.setState({ error: error.message, loading: false });
    }
  };

  render() {
    return this.props.children(this.state);
  }
}

// Sử dụng Render Props
function App() {
  return (
    <AuthProvider>
      {({ user, loading, error }) => {
        if (loading) return <div>Loading...</div>;
        if (error) return <div>Error: {error}</div>;
        if (!user) return <LoginForm />;

        return <Dashboard user={user} />;
      }}
    </AuthProvider>
  );
}

// 3. Custom Hook (Modern approach)
function useAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;

    const checkAuth = async () => {
      try {
        const userData = await authService.getCurrentUser();
        if (isMounted) {
          setUser(userData);
          setError(null);
        }
      } catch (err) {
        if (isMounted) {
          setError(err.message);
          setUser(null);
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    checkAuth();

    return () => {
      isMounted = false;
    };
  }, []);

  const login = async (credentials) => {
    setLoading(true);
    try {
      const userData = await authService.login(credentials);
      setUser(userData);
      setError(null);
      return userData;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  const logout = async () => {
    try {
      await authService.logout();
      setUser(null);
    } catch (err) {
      setError(err.message);
    }
  };

  return {
    user,
    loading,
    error,
    login,
    logout,
    isAuthenticated: !!user
  };
}

// Sử dụng Custom Hook
function ProtectedRoute({ children }) {
  const { user, loading } = useAuth();

  if (loading) return <div>Loading...</div>;
  if (!user) return <Navigate to="/login" />;

  return children;
}
```

---

## Performance Optimization

### Q11: Virtual DOM vs Real DOM - Performance implications?

**Trả lời:**

```typescript
// Vấn đề với Direct DOM manipulation
function updateListBadly(items) {
  const container = document.getElementById('list-container');

  // Xóa tất cả elements (expensive)
  container.innerHTML = '';

  // Tạo lại tất cả elements (expensive)
  items.forEach(item => {
    const div = document.createElement('div');
    div.textContent = item.name;
    div.onclick = () => handleClick(item.id);
    container.appendChild(div); // Reflow/repaint cho mỗi append
  });
}

// React Virtual DOM approach
function OptimizedList({ items, onItemClick }) {
  return (
    <div>
      {items.map(item => (
        <ListItem
          key={item.id}
          item={item}
          onClick={onItemClick}
        />
      ))}
    </div>
  );
}

// Tối ưu hóa với React.memo và key props
const ListItem = React.memo(({ item, onClick }) => {
  return (
    <div
      className="list-item"
      onClick={() => onClick(item.id)}
    >
      {item.name}
    </div>
  );
});

// Advanced: Virtualization cho large lists
import { FixedSizeList as List } from 'react-window';

function VirtualizedList({ items, onItemClick }) {
  const Row = ({ index, style }) => (
    <div style={style}>
      <ListItem
        item={items[index]}
        onClick={onItemClick}
      />
    </div>
  );

  return (
    <List
      height={600}
      itemCount={items.length}
      itemSize={50}
      width="100%"
    >
      {Row}
    </List>
  );
}
```

### Q12: Bundle Optimization và Tree Shaking?

**Trả lời:**

```typescript
// Bad: Import entire library
import _ from 'lodash'; // Imports entire lodash (~70KB)
import * as MUI from '@mui/material'; // Imports everything

// Good: Import only needed functions
import { debounce, throttle } from 'lodash';
import { Button, TextField } from '@mui/material';

// Better: Use babel plugins for automatic optimization
// babel-plugin-lodash
import { debounce } from 'lodash'; // Automatically optimized to lodash/debounce

// Webpack Bundle Analyzer để identify large bundles
// npm install --save-dev webpack-bundle-analyzer

// Dynamic imports cho conditional loading
async function loadChartLibrary() {
  if (window.innerWidth > 768) {
    // Load full-featured chart for desktop
    const { Chart } = await import('./AdvancedChart');
    return Chart;
  } else {
    // Load lightweight chart for mobile
    const { SimpleChart } = await import('./SimpleChart');
    return SimpleChart;
  }
}

// Tree shaking friendly module structure
// utils/index.js
export { debounce } from './debounce';
export { throttle } from './throttle';
export { formatDate } from './formatDate';

// utils/debounce.js
export function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Webpack config cho production optimization
module.exports = {
  optimization: {
    usedExports: true, // Enable tree shaking
    sideEffects: false, // No side effects in modules
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendors',
          chunks: 'all',
        },
        common: {
          name: 'common',
          minChunks: 2,
          chunks: 'all',
          enforce: true,
        },
      },
    },
  },
};
```

---

## Security Best Practices

### Q13: XSS Prevention trong React?

**Trả lời:**

```typescript
// React tự động escape JSX content, nhưng có exceptions:

// Safe: React automatically escapes
function SafeComponent({ userInput }) {
  return <div>{userInput}</div>; // Automatically escaped
}

// Dangerous: dangerouslySetInnerHTML
function DangerousComponent({ htmlContent }) {
  // NEVER do this with untrusted content
  return <div dangerouslySetInnerHTML={{ __html: htmlContent }} />;
}

// Safe approach: Sanitize HTML content
import DOMPurify from 'dompurify';

function SafeHTMLComponent({ htmlContent }) {
  const sanitizedHTML = DOMPurify.sanitize(htmlContent, {
    ALLOWED_TAGS: ['b', 'i', 'em', 'strong', 'p', 'br'],
    ALLOWED_ATTR: []
  });

  return <div dangerouslySetInnerHTML={{ __html: sanitizedHTML }} />;
}

// URL sanitization
function SafeLink({ href, children }) {
  const sanitizeURL = (url) => {
    try {
      const parsed = new URL(url);
      // Only allow http and https protocols
      if (!['http:', 'https:'].includes(parsed.protocol)) {
        return '#';
      }
      return url;
    } catch {
      return '#';
    }
  };

  return (
    <a
      href={sanitizeURL(href)}
      rel="noopener noreferrer"
      target="_blank"
    >
      {children}
    </a>
  );
}

// Input validation and sanitization
function SecureForm() {
  const [formData, setFormData] = useState({
    email: '',
    message: ''
  });
  const [errors, setErrors] = useState({});

  const validateInput = (field, value) => {
    const validators = {
      email: (val) => {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(val) ? null : 'Invalid email format';
      },
      message: (val) => {
        // Remove potentially dangerous characters
        const sanitized = val.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
        return sanitized.length > 500 ? 'Message too long' : null;
      }
    };

    return validators[field] ? validators[field](value) : null;
  };

  const handleInputChange = (field, value) => {
    // Validate on change
    const error = validateInput(field, value);

    setFormData(prev => ({ ...prev, [field]: value }));
    setErrors(prev => ({ ...prev, [field]: error }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Final validation
    const newErrors = {};
    Object.keys(formData).forEach(field => {
      const error = validateInput(field, formData[field]);
      if (error) newErrors[field] = error;
    });

    if (Object.keys(newErrors).length > 0) {
      setErrors(newErrors);
      return;
    }

    // Submit with additional server-side validation
    try {
      await api.submitForm(formData);
    } catch (error) {
      console.error('Form submission failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={formData.email}
        onChange={(e) => handleInputChange('email', e.target.value)}
        placeholder="Email"
      />
      {errors.email && <span className="error">{errors.email}</span>}

      <textarea
        value={formData.message}
        onChange={(e) => handleInputChange('message', e.target.value)}
        placeholder="Message"
        maxLength={500}
      />
      {errors.message && <span className="error">{errors.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
}
```

### Q14: CSRF Protection và Secure API Calls?

**Trả lời:**

```typescript
// API service với security headers
class SecureAPIService {
  constructor() {
    this.baseURL = process.env.REACT_APP_API_URL;
    this.csrfToken = null;
  }

  async getCSRFToken() {
    if (!this.csrfToken) {
      const response = await fetch(`${this.baseURL}/csrf-token`, {
        credentials: 'include' // Include cookies
      });
      const data = await response.json();
      this.csrfToken = data.token;
    }
    return this.csrfToken;
  }

  async makeSecureRequest(endpoint, options = {}) {
    const token = await this.getCSRFToken();

    const defaultOptions = {
      credentials: 'include', // Include cookies for session
      headers: {
        'Content-Type': 'application/json',
        'X-CSRF-Token': token,
        'X-Requested-With': 'XMLHttpRequest', // CSRF protection
        ...options.headers
      }
    };

    const response = await fetch(`${this.baseURL}${endpoint}`, {
      ...defaultOptions,
      ...options
    });

    if (response.status === 403) {
      // CSRF token might be expired, refresh and retry
      this.csrfToken = null;
      return this.makeSecureRequest(endpoint, options);
    }

    if (!response.ok) {
      throw new Error(`API Error: ${response.status}`);
    }

    return response.json();
  }

  async post(endpoint, data) {
    return this.makeSecureRequest(endpoint, {
      method: 'POST',
      body: JSON.stringify(data)
    });
  }

  async put(endpoint, data) {
    return this.makeSecureRequest(endpoint, {
      method: 'PUT',
      body: JSON.stringify(data)
    });
  }

  async delete(endpoint) {
    return this.makeSecureRequest(endpoint, {
      method: 'DELETE'
    });
  }
}

// Secure authentication hook
function useSecureAuth() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check authentication status on mount
    checkAuthStatus();

    // Set up token refresh interval
    const refreshInterval = setInterval(refreshToken, 15 * 60 * 1000); // 15 minutes

    return () => clearInterval(refreshInterval);
  }, []);

  const checkAuthStatus = async () => {
    try {
      const userData = await api.makeSecureRequest('/auth/me');
      setUser(userData);
    } catch (error) {
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  const refreshToken = async () => {
    try {
      await api.makeSecureRequest('/auth/refresh', { method: 'POST' });
    } catch (error) {
      // Refresh failed, redirect to login
      setUser(null);
      window.location.href = '/login';
    }
  };

  const login = async (credentials) => {
    try {
      const userData = await api.post('/auth/login', credentials);
      setUser(userData);
      return userData;
    } catch (error) {
      throw new Error('Login failed');
    }
  };

  const logout = async () => {
    try {
      await api.post('/auth/logout');
    } catch (error) {
      console.error('Logout error:', error);
    } finally {
      setUser(null);
      // Clear any sensitive data from localStorage
      localStorage.removeItem('userPreferences');
    }
  };

  return { user, loading, login, logout };
}

// Content Security Policy helper
function useCSP() {
  useEffect(() => {
    // Set CSP meta tag if not already set by server
    if (!document.querySelector('meta[http-equiv="Content-Security-Policy"]')) {
      const meta = document.createElement('meta');
      meta.httpEquiv = 'Content-Security-Policy';
      meta.content = `
        default-src 'self';
        script-src 'self' 'unsafe-inline' https://trusted-cdn.com;
        style-src 'self' 'unsafe-inline' https://fonts.googleapis.com;
        img-src 'self' data: https://trusted-images.com;
        connect-src 'self' https://api.yourapp.com;
        font-src 'self' https://fonts.gstatic.com;
      `.replace(/\s+/g, ' ').trim();

      document.head.appendChild(meta);
    }
  }, []);
}
```

### Q15: Secure Data Storage và Privacy?

**Trả lời:**

```typescript
// Secure storage utility
class SecureStorage {
  static encrypt(data, key) {
    // Simple encryption (use proper library in production)
    const encoded = btoa(JSON.stringify(data));
    return encoded;
  }

  static decrypt(encryptedData, key) {
    try {
      const decoded = atob(encryptedData);
      return JSON.parse(decoded);
    } catch (error) {
      console.error('Decryption failed:', error);
      return null;
    }
  }

  static setSecureItem(key, value, options = {}) {
    try {
      const data = {
        value,
        timestamp: Date.now(),
        expires: options.expires ? Date.now() + options.expires : null
      };

      const encrypted = this.encrypt(data, key);

      if (options.session) {
        sessionStorage.setItem(key, encrypted);
      } else {
        localStorage.setItem(key, encrypted);
      }
    } catch (error) {
      console.error('Failed to store data:', error);
    }
  }

  static getSecureItem(key, options = {}) {
    try {
      const storage = options.session ? sessionStorage : localStorage;
      const encrypted = storage.getItem(key);

      if (!encrypted) return null;

      const data = this.decrypt(encrypted, key);

      if (!data) return null;

      // Check expiration
      if (data.expires && Date.now() > data.expires) {
        storage.removeItem(key);
        return null;
      }

      return data.value;
    } catch (error) {
      console.error('Failed to retrieve data:', error);
      return null;
    }
  }

  static removeSecureItem(key, options = {}) {
    const storage = options.session ? sessionStorage : localStorage;
    storage.removeItem(key);
  }

  static clearExpiredItems() {
    const checkStorage = (storage) => {
      const keys = Object.keys(storage);
      keys.forEach(key => {
        try {
          const encrypted = storage.getItem(key);
          const data = this.decrypt(encrypted, key);

          if (data && data.expires && Date.now() > data.expires) {
            storage.removeItem(key);
          }
        } catch (error) {
          // Invalid data, remove it
          storage.removeItem(key);
        }
      });
    };

    checkStorage(localStorage);
    checkStorage(sessionStorage);
  }
}

// Privacy-compliant data handling
function usePrivacyCompliantData() {
  const [consent, setConsent] = useState(null);
  const [userData, setUserData] = useState(null);

  useEffect(() => {
    // Check existing consent
    const existingConsent = SecureStorage.getSecureItem('user-consent');
    setConsent(existingConsent);

    // Clear expired items periodically
    const cleanup = setInterval(() => {
      SecureStorage.clearExpiredItems();
    }, 60 * 60 * 1000); // Every hour

    return () => clearInterval(cleanup);
  }, []);

  const requestConsent = async (purposes) => {
    // Show consent dialog
    const userConsent = await showConsentDialog(purposes);

    if (userConsent.analytics) {
      // Only store analytics data if consented
      setConsent(userConsent);
      SecureStorage.setSecureItem('user-consent', userConsent, {
        expires: 365 * 24 * 60 * 60 * 1000 // 1 year
      });
    }

    return userConsent;
  };

  const storeUserData = (data, sensitive = false) => {
    if (!consent?.necessary) {
      console.warn('Cannot store data without consent');
      return;
    }

    const options = sensitive ? { session: true } : {};
    SecureStorage.setSecureItem('user-data', data, options);
    setUserData(data);
  };

  const anonymizeData = (data) => {
    // Remove PII
    const anonymized = { ...data };
    delete anonymized.email;
    delete anonymized.phone;
    delete anonymized.address;

    // Hash sensitive identifiers
    if (anonymized.userId) {
      anonymized.userId = btoa(anonymized.userId).slice(0, 8);
    }

    return anonymized;
  };

  const clearUserData = () => {
    SecureStorage.removeSecureItem('user-data');
    SecureStorage.removeSecureItem('user-data', { session: true });
    SecureStorage.removeSecureItem('user-consent');
    setUserData(null);
    setConsent(null);
  };

  return {
    consent,
    userData,
    requestConsent,
    storeUserData,
    anonymizeData,
    clearUserData
  };
}

// Secure form handling with PII protection
function SecureUserForm() {
  const { consent, storeUserData, anonymizeData } = usePrivacyCompliantData();
  const [formData, setFormData] = useState({
    email: '',
    phone: '',
    preferences: {}
  });

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validate consent for data processing
    if (!consent?.necessary) {
      alert('Please accept necessary cookies to proceed');
      return;
    }

    try {
      // Send full data to server (with encryption in transit)
      await api.post('/user/profile', formData);

      // Store only necessary data locally
      const localData = anonymizeData(formData);
      storeUserData(localData);

      // Store sensitive data in session only if needed
      if (consent.functionality) {
        storeUserData({ email: formData.email }, true);
      }

    } catch (error) {
      console.error('Form submission failed:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={formData.email}
        onChange={(e) => setFormData(prev => ({
          ...prev,
          email: e.target.value
        }))}
        placeholder="Email"
      />

      <input
        type="tel"
        value={formData.phone}
        onChange={(e) => setFormData(prev => ({
          ...prev,
          phone: e.target.value
        }))}
        placeholder="Phone"
      />

      <button type="submit">Submit</button>

      {!consent && (
        <div className="consent-notice">
          We need your consent to process this data.
          <button onClick={() => requestConsent(['necessary', 'functionality'])}>
            Manage Preferences
          </button>
        </div>
      )}
    </form>
  );
}
```

---

## Expert Level (Lead/Architect)

### 6. System Design & Architecture

#### Q16: Thiết kế kiến trúc Micro-frontend cho ứng dụng scale lớn?

**Trả lời:**

```typescript
// 1. Module Federation với Webpack 5
// Host Application (Shell)
const ModuleFederationPlugin = require('@module-federation/webpack');

module.exports = {
  mode: 'development',
  devServer: { port: 3000 },
  plugins: [
    new ModuleFederationPlugin({
      name: 'shell',
      remotes: {
        userModule: 'userModule@http://localhost:3001/remoteEntry.js',
        orderModule: 'orderModule@http://localhost:3002/remoteEntry.js',
        paymentModule: 'paymentModule@http://localhost:3003/remoteEntry.js',
      },
      shared: {
        react: { singleton: true, eager: true },
        'react-dom': { singleton: true, eager: true },
        '@reduxjs/toolkit': { singleton: true },
      },
    }),
  ],
};

// Shell App Component
function ShellApp() {
  const [currentModule, setCurrentModule] = useState('user');
  const [moduleError, setModuleError] = useState(null);

  // Dynamic module loading với error handling
  const loadModule = async (moduleName) => {
    try {
      setModuleError(null);

      const moduleMap = {
        user: () => import('userModule/UserApp'),
        order: () => import('orderModule/OrderApp'),
        payment: () => import('paymentModule/PaymentApp'),
      };

      const Module = await moduleMap[moduleName]();
      return Module.default;
    } catch (error) {
      console.error(`Failed to load module: ${moduleName}`, error);
      setModuleError(error.message);
      return () => <div>Module failed to load: {error.message}</div>;
    }
  };

  return (
    <ErrorBoundary>
      <div className="shell-app">
        <GlobalNavigation onModuleChange={setCurrentModule} />
        <Suspense fallback={<ModuleLoadingSpinner />}>
          <ModuleContainer
            moduleName={currentModule}
            loadModule={loadModule}
            error={moduleError}
          />
        </Suspense>
      </div>
    </ErrorBoundary>
  );
}

// 2. Event-driven communication giữa micro-frontends
class MicroFrontendEventBus {
  constructor() {
    this.events = new Map();
    this.middleware = [];
  }

  // Middleware cho logging, validation, etc.
  use(middleware) {
    this.middleware.push(middleware);
  }

  subscribe(eventName, callback, options = {}) {
    if (!this.events.has(eventName)) {
      this.events.set(eventName, new Set());
    }

    const wrappedCallback = (data) => {
      // Apply middleware
      let processedData = data;
      for (const middleware of this.middleware) {
        processedData = middleware(eventName, processedData, 'subscribe');
      }

      if (options.once) {
        this.events.get(eventName).delete(wrappedCallback);
      }

      callback(processedData);
    };

    this.events.get(eventName).add(wrappedCallback);

    return () => this.events.get(eventName)?.delete(wrappedCallback);
  }

  emit(eventName, data, options = {}) {
    // Apply middleware
    let processedData = data;
    for (const middleware of this.middleware) {
      processedData = middleware(eventName, processedData, 'emit');
    }

    const callbacks = this.events.get(eventName);
    if (callbacks) {
      if (options.async) {
        setTimeout(() => {
          callbacks.forEach(callback => callback(processedData));
        }, 0);
      } else {
        callbacks.forEach(callback => callback(processedData));
      }
    }
  }

  // Cross-domain messaging cho isolated micro-frontends
  emitCrossDomain(targetOrigin, eventName, data) {
    window.postMessage({
      type: 'MICRO_FRONTEND_EVENT',
      eventName,
      data,
      timestamp: Date.now(),
      source: window.location.origin
    }, targetOrigin);
  }
}

// Global event bus instance
window.MFEventBus = new MicroFrontendEventBus();

// Logging middleware
window.MFEventBus.use((eventName, data, type) => {
  console.log(`[MF EventBus] ${type}: ${eventName}`, data);
  return data;
});

// 3. Shared state management across micro-frontends
class SharedStateManager {
  constructor() {
    this.stores = new Map();
    this.subscribers = new Map();
  }

  createStore(storeId, initialState, reducer) {
    const store = {
      state: initialState,
      reducer,
      dispatch: (action) => {
        const newState = reducer(store.state, action);
        if (newState !== store.state) {
          store.state = newState;
          this.notifySubscribers(storeId, newState);

          // Persist critical state
          if (action.type.includes('PERSIST')) {
            localStorage.setItem(`mf_state_${storeId}`, JSON.stringify(newState));
          }
        }
      }
    };

    this.stores.set(storeId, store);
    return store;
  }

  subscribe(storeId, callback) {
    if (!this.subscribers.has(storeId)) {
      this.subscribers.set(storeId, new Set());
    }
    this.subscribers.get(storeId).add(callback);

    return () => this.subscribers.get(storeId)?.delete(callback);
  }

  getState(storeId) {
    return this.stores.get(storeId)?.state;
  }

  notifySubscribers(storeId, newState) {
    const callbacks = this.subscribers.get(storeId);
    if (callbacks) {
      callbacks.forEach(callback => callback(newState));
    }
  }

  // Cross-micro-frontend state sync
  syncState(storeId, targetOrigins) {
    const state = this.getState(storeId);
    targetOrigins.forEach(origin => {
      window.MFEventBus.emitCrossDomain(origin, 'STATE_SYNC', {
        storeId,
        state
      });
    });
  }
}

// Usage trong micro-frontend
function useSharedState(storeId) {
  const [state, setState] = useState(() =>
    window.SharedStateManager.getState(storeId)
  );

  useEffect(() => {
    const unsubscribe = window.SharedStateManager.subscribe(storeId, setState);
    return unsubscribe;
  }, [storeId]);

  const dispatch = useCallback((action) => {
    const store = window.SharedStateManager.stores.get(storeId);
    store?.dispatch(action);
  }, [storeId]);

  return [state, dispatch];
}
```

#### Q17: Implement advanced caching strategies cho production apps?

**Trả lời:**

```typescript
// 1. Multi-layer caching system
class AdvancedCacheManager {
  constructor() {
    this.memoryCache = new Map();
    this.browserCache = new Map();
    this.networkCache = new Map();
    this.cacheStats = {
      hits: 0,
      misses: 0,
      evictions: 0
    };

    // Cache configuration
    this.config = {
      memoryLimit: 50 * 1024 * 1024, // 50MB
      ttl: {
        short: 5 * 60 * 1000,     // 5 minutes
        medium: 30 * 60 * 1000,   // 30 minutes
        long: 24 * 60 * 60 * 1000  // 24 hours
      },
      maxEntries: 1000
    };

    this.setupPerformanceMonitoring();
    this.setupAutomaticCleanup();
  }

  async get(key, fetchFn, options = {}) {
    const startTime = performance.now();

    try {
      // 1. Try memory cache first (fastest)
      const memoryResult = this.getFromMemory(key);
      if (memoryResult) {
        this.recordCacheHit('memory', performance.now() - startTime);
        return memoryResult.data;
      }

      // 2. Try browser cache (IndexedDB/localStorage)
      const browserResult = await this.getFromBrowserCache(key);
      if (browserResult && !this.isExpired(browserResult)) {
        // Promote to memory cache
        this.setInMemory(key, browserResult.data, options);
        this.recordCacheHit('browser', performance.now() - startTime);
        return browserResult.data;
      }

      // 3. Try network cache (with stale-while-revalidate)
      const networkResult = await this.getFromNetworkCache(key);
      if (networkResult && options.staleWhileRevalidate) {
        // Serve stale data while fetching fresh
        this.revalidateInBackground(key, fetchFn, options);
        this.recordCacheHit('network-stale', performance.now() - startTime);
        return networkResult.data;
      }

      // 4. Fetch fresh data
      this.recordCacheMiss(performance.now() - startTime);
      const freshData = await this.fetchWithRetry(fetchFn, options);

      // Store in all cache layers
      await this.setMultiLayer(key, freshData, options);

      return freshData;

    } catch (error) {
      // Fallback to any available cached data
      const fallbackData = await this.getFallbackData(key);
      if (fallbackData) {
        console.warn('Using fallback cache data due to error:', error);
        return fallbackData;
      }
      throw error;
    }
  }

  setMultiLayer(key, data, options = {}) {
    const cacheEntry = {
      data,
      timestamp: Date.now(),
      ttl: options.ttl || this.config.ttl.medium,
      tags: options.tags || [],
      size: this.calculateSize(data)
    };

    // Memory cache
    this.setInMemory(key, cacheEntry, options);

    // Browser cache (async)
    this.setInBrowserCache(key, cacheEntry);

    // Network cache headers
    if (options.networkCache) {
      this.setNetworkCacheHeaders(options.networkCache);
    }
  }

  // LRU eviction with memory pressure awareness
  setInMemory(key, entry, options = {}) {
    if (this.shouldEvictMemory()) {
      this.evictLRU();
    }

    this.memoryCache.set(key, {
      ...entry,
      lastAccessed: Date.now(),
      accessCount: 0
    });
  }

  shouldEvictMemory() {
    const currentSize = this.calculateTotalMemorySize();
    const memoryPressure = this.getMemoryPressure();

    return (
      currentSize > this.config.memoryLimit ||
      this.memoryCache.size > this.config.maxEntries ||
      memoryPressure > 0.8
    );
  }

  evictLRU() {
    const entries = Array.from(this.memoryCache.entries())
      .sort((a, b) => {
        // Smart eviction: consider access frequency and recency
        const scoreA = a[1].accessCount / (Date.now() - a[1].lastAccessed);
        const scoreB = b[1].accessCount / (Date.now() - b[1].lastAccessed);
        return scoreA - scoreB;
      });

    const toEvict = Math.ceil(entries.length * 0.2); // Evict 20%
    for (let i = 0; i < toEvict; i++) {
      this.memoryCache.delete(entries[i][0]);
      this.cacheStats.evictions++;
    }
  }

  // Intelligent prefetching
  async prefetch(keys, fetchFns, options = {}) {
    const prefetchPromises = keys.map(async (key, index) => {
      try {
        // Only prefetch if not in cache and browser is idle
        if (!this.memoryCache.has(key) && this.isBrowserIdle()) {
          const data = await fetchFns[index]();
          await this.setMultiLayer(key, data, {
            ...options,
            ttl: this.config.ttl.long
          });
        }
      } catch (error) {
        console.warn(`Prefetch failed for ${key}:`, error);
      }
    });

    return Promise.allSettled(prefetchPromises);
  }

  // Cache invalidation với tags
  invalidateByTags(tags) {
    const toInvalidate = [];

    for (const [key, entry] of this.memoryCache.entries()) {
      if (entry.tags?.some(tag => tags.includes(tag))) {
        toInvalidate.push(key);
      }
    }

    toInvalidate.forEach(key => {
      this.memoryCache.delete(key);
      this.invalidateBrowserCache(key);
    });

    return toInvalidate.length;
  }

  // Performance monitoring
  setupPerformanceMonitoring() {
    setInterval(() => {
      const stats = this.getCacheStats();

      // Report metrics to analytics
      if (window.analytics) {
        window.analytics.track('Cache Performance', stats);
      }

      // Auto-tune cache based on performance
      this.autoTuneCache(stats);
    }, 60000); // Every minute
  }

  getCacheStats() {
    const hitRate = this.cacheStats.hits / (this.cacheStats.hits + this.cacheStats.misses);

    return {
      hitRate,
      memoryUsage: this.calculateTotalMemorySize(),
      entryCount: this.memoryCache.size,
      evictionRate: this.cacheStats.evictions / this.cacheStats.hits,
      averageAccessTime: this.averageAccessTime
    };
  }
}

// 2. Service Worker caching với advanced strategies
// sw.js
class ServiceWorkerCacheStrategy {
  constructor() {
    this.caches = {
      static: 'static-v1',
      dynamic: 'dynamic-v1',
      api: 'api-v1'
    };

    this.strategies = {
      staleWhileRevalidate: this.staleWhileRevalidate.bind(this),
      cacheFirst: this.cacheFirst.bind(this),
      networkFirst: this.networkFirst.bind(this),
      networkOnly: this.networkOnly.bind(this),
      cacheOnly: this.cacheOnly.bind(this)
    };
  }

  async handleRequest(event) {
    const { request } = event;
    const url = new URL(request.url);

    // Route-based caching strategy
    if (url.pathname.startsWith('/api/')) {
      return this.handleAPIRequest(request);
    } else if (url.pathname.match(/\.(js|css|png|jpg|jpeg|svg|woff2)$/)) {
      return this.strategies.cacheFirst(request, this.caches.static);
    } else {
      return this.strategies.staleWhileRevalidate(request, this.caches.dynamic);
    }
  }

  async handleAPIRequest(request) {
    const url = new URL(request.url);

    // Different strategies for different API endpoints
    if (url.pathname.includes('/user/profile')) {
      return this.strategies.staleWhileRevalidate(request, this.caches.api);
    } else if (url.pathname.includes('/static-data')) {
      return this.strategies.cacheFirst(request, this.caches.api);
    } else if (url.pathname.includes('/real-time')) {
      return this.strategies.networkFirst(request, this.caches.api);
    } else {
      return this.strategies.networkOnly(request);
    }
  }

  async staleWhileRevalidate(request, cacheName) {
    const cache = await caches.open(cacheName);
    const cachedResponse = await cache.match(request);

    const fetchPromise = fetch(request).then(async (response) => {
      if (response.ok) {
        // Clone before caching
        const responseClone = response.clone();
        await cache.put(request, responseClone);
      }
      return response;
    });

    // Return cached version immediately if available
    return cachedResponse || fetchPromise;
  }

  async cacheFirst(request, cacheName) {
    const cache = await caches.open(cacheName);
    const cachedResponse = await cache.match(request);

    if (cachedResponse) {
      return cachedResponse;
    }

    const response = await fetch(request);
    if (response.ok) {
      await cache.put(request, response.clone());
    }

    return response;
  }

  async networkFirst(request, cacheName) {
    try {
      const response = await fetch(request);

      if (response.ok) {
        const cache = await caches.open(cacheName);
        await cache.put(request, response.clone());
      }

      return response;
    } catch (error) {
      const cache = await caches.open(cacheName);
      const cachedResponse = await cache.match(request);

      if (cachedResponse) {
        return cachedResponse;
      }

      throw error;
    }
  }
}

// 3. React Query với advanced configuration
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      staleTime: 5 * 60 * 1000, // 5 minutes
      cacheTime: 30 * 60 * 1000, // 30 minutes
      refetchOnWindowFocus: false,
      refetchOnReconnect: true,
      retry: (failureCount, error) => {
        // Custom retry logic
        if (error.status === 404) return false;
        return failureCount < 3;
      },
      retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),
    },
    mutations: {
      retry: 1,
      onError: (error) => {
        // Global error handling
        console.error('Mutation error:', error);
      }
    }
  }
});

// Custom hook với intelligent caching
function useAdvancedQuery(key, fetcher, options = {}) {
  const [isOnline, setIsOnline] = useState(navigator.onLine);

  useEffect(() => {
    const handleOnline = () => setIsOnline(true);
    const handleOffline = () => setIsOnline(false);

    window.addEventListener('online', handleOnline);
    window.addEventListener('offline', handleOffline);

    return () => {
      window.removeEventListener('online', handleOnline);
      window.removeEventListener('offline', handleOffline);
    };
  }, []);

  return useQuery({
    queryKey: key,
    queryFn: fetcher,
    enabled: isOnline,
    ...options,
    staleTime: options.staleTime || (isOnline ? 5 * 60 * 1000 : Infinity),
    cacheTime: options.cacheTime || 30 * 60 * 1000,
  });
}
```

#### Q18: Design Pattern cho large-scale React applications?

**Trả lời:**

```typescript
// 1. Feature-Slice Design Architecture
// features/user/model/store.js
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';

export const fetchUser = createAsyncThunk(
  'user/fetchUser',
  async (userId, { rejectWithValue, getState, dispatch }) => {
    try {
      const response = await userAPI.getUser(userId);

      // Side effects - update related features
      dispatch(notificationsModel.actions.markAsRead({
        userId: response.id
      }));

      return response;
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const userSlice = createSlice({
  name: 'user',
  initialState: {
    entities: {},
    loading: false,
    error: null,
    currentUserId: null
  },
  reducers: {
    setCurrentUser: (state, action) => {
      state.currentUserId = action.payload;
    },
    updateUserProfile: (state, action) => {
      const { userId, updates } = action.payload;
      if (state.entities[userId]) {
        Object.assign(state.entities[userId], updates);
      }
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUser.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUser.fulfilled, (state, action) => {
        state.loading = false;
        state.entities[action.payload.id] = action.payload;
      })
      .addCase(fetchUser.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload;
      });
  }
});

export const userModel = {
  actions: userSlice.actions,
  reducer: userSlice.reducer,
  selectors: {
    selectUser: (state, userId) => state.user.entities[userId],
    selectCurrentUser: (state) =>
      state.user.entities[state.user.currentUserId],
    selectIsLoading: (state) => state.user.loading,
    selectError: (state) => state.user.error
  },
  thunks: { fetchUser }
};

// 2. Advanced Component Composition Patterns
// Compound Components với Context
const AccordionContext = createContext();

function useAccordion() {
  const context = useContext(AccordionContext);
  if (!context) {
    throw new Error('Accordion components must be used within Accordion');
  }
  return context;
}

function Accordion({ children, allowMultiple = false, defaultOpenItems = [] }) {
  const [openItems, setOpenItems] = useState(new Set(defaultOpenItems));

  const toggleItem = useCallback((itemId) => {
    setOpenItems(prev => {
      const newSet = new Set(prev);

      if (newSet.has(itemId)) {
        newSet.delete(itemId);
      } else {
        if (!allowMultiple) {
          newSet.clear();
        }
        newSet.add(itemId);
      }

      return newSet;
    });
  }, [allowMultiple]);

  const contextValue = useMemo(() => ({
    openItems,
    toggleItem,
    allowMultiple
  }), [openItems, toggleItem, allowMultiple]);

  return (
    <AccordionContext.Provider value={contextValue}>
      <div className="accordion">{children}</div>
    </AccordionContext.Provider>
  );
}

Accordion.Item = function AccordionItem({ id, children }) {
  const { openItems } = useAccordion();
  const isOpen = openItems.has(id);

  return (
    <div className={`accordion-item ${isOpen ? 'open' : ''}`}>
      {typeof children === 'function' ? children({ isOpen }) : children}
    </div>
  );
};

Accordion.Trigger = function AccordionTrigger({ itemId, children }) {
  const { toggleItem } = useAccordion();

  return (
    <button
      className="accordion-trigger"
      onClick={() => toggleItem(itemId)}
      aria-expanded={openItems.has(itemId)}
    >
      {children}
    </button>
  );
};

Accordion.Content = function AccordionContent({ itemId, children }) {
  const { openItems } = useAccordion();
  const isOpen = openItems.has(itemId);

  return (
    <div
      className="accordion-content"
      style={{ display: isOpen ? 'block' : 'none' }}
    >
      {children}
    </div>
  );
};

// Usage
function FAQSection() {
  return (
    <Accordion allowMultiple>
      <Accordion.Item id="item1">
        {({ isOpen }) => (
          <>
            <Accordion.Trigger itemId="item1">
              What is React? {isOpen ? '−' : '+'}
            </Accordion.Trigger>
            <Accordion.Content itemId="item1">
              React is a JavaScript library...
            </Accordion.Content>
          </>
        )}
      </Accordion.Item>
    </Accordion>
  );
}

// 3. Advanced State Management Pattern - Event Sourcing
class EventStore {
  constructor() {
    this.events = [];
    this.snapshots = new Map();
    this.projections = new Map();
    this.subscribers = new Set();
  }

  append(event) {
    const eventWithMeta = {
      ...event,
      id: generateUUID(),
      timestamp: Date.now(),
      version: this.events.length + 1
    };

    this.events.push(eventWithMeta);
    this.notifySubscribers(eventWithMeta);

    // Create snapshot every N events for performance
    if (this.events.length % 100 === 0) {
      this.createSnapshot();
    }

    return eventWithMeta;
  }

  replay(fromVersion = 0) {
    const eventsToReplay = this.events.slice(fromVersion);

    // Start from latest snapshot if available
    const latestSnapshot = this.getLatestSnapshot(fromVersion);
    let state = latestSnapshot?.state || this.getInitialState();

    return eventsToReplay.reduce((currentState, event) => {
      return this.applyEvent(currentState, event);
    }, state);
  }

  createProjection(name, reducer, fromVersion = 0) {
    const initialState = this.getInitialProjectionState(name);
    const state = this.events
      .slice(fromVersion)
      .reduce(reducer, initialState);

    this.projections.set(name, state);
    return state;
  }

  subscribe(callback) {
    this.subscribers.add(callback);
    return () => this.subscribers.delete(callback);
  }

  notifySubscribers(event) {
    this.subscribers.forEach(callback => callback(event));
  }
}

// Event-sourced User aggregate
class UserAggregate {
  constructor(eventStore) {
    this.eventStore = eventStore;
    this.state = {
      users: {},
      currentUserId: null
    };
  }

  // Commands (intent to change state)
  createUser(userData) {
    const event = {
      type: 'USER_CREATED',
      payload: {
        userId: generateUUID(),
        ...userData,
        createdAt: Date.now()
      }
    };

    this.eventStore.append(event);
    return event.payload.userId;
  }

  updateUserProfile(userId, updates) {
    if (!this.state.users[userId]) {
      throw new Error('User not found');
    }

    const event = {
      type: 'USER_PROFILE_UPDATED',
      payload: {
        userId,
        updates,
        updatedAt: Date.now()
      }
    };

    this.eventStore.append(event);
  }

  // Event handlers (how state changes)
  applyEvent(state, event) {
    switch (event.type) {
      case 'USER_CREATED':
        return {
          ...state,
          users: {
            ...state.users,
            [event.payload.userId]: event.payload
          }
        };

      case 'USER_PROFILE_UPDATED':
        return {
          ...state,
          users: {
            ...state.users,
            [event.payload.userId]: {
              ...state.users[event.payload.userId],
              ...event.payload.updates
            }
          }
        };

      default:
        return state;
    }
  }

  // Query current state
  getUser(userId) {
    return this.state.users[userId];
  }

  getAllUsers() {
    return Object.values(this.state.users);
  }
}

// React integration
function useEventSourcingState(aggregate) {
  const [state, setState] = useState(aggregate.state);

  useEffect(() => {
    const unsubscribe = aggregate.eventStore.subscribe((event) => {
      setState(prevState => aggregate.applyEvent(prevState, event));
    });

    return unsubscribe;
  }, [aggregate]);

  return state;
}

// 4. Advanced Error Boundary với Recovery Strategies
class AdvancedErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
      retryCount: 0,
      errorId: null
    };
  }

  static getDerivedStateFromError(error) {
    return {
      hasError: true,
      error,
      errorId: generateUUID()
    };
  }

  componentDidCatch(error, errorInfo) {
    this.setState({ errorInfo });

    // Advanced error reporting
    this.reportError(error, errorInfo);

    // Attempt automatic recovery for certain error types
    this.attemptRecovery(error);
  }

  reportError(error, errorInfo) {
    const errorReport = {
      message: error.message,
      stack: error.stack,
      componentStack: errorInfo.componentStack,
      timestamp: Date.now(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      userId: this.props.userId,
      sessionId: this.props.sessionId,
      buildVersion: process.env.REACT_APP_VERSION
    };

    // Send to error reporting service
    if (window.errorReporter) {
      window.errorReporter.captureException(error, {
        extra: errorReport,
        tags: {
          component: this.props.name || 'UnknownComponent',
          severity: this.getErrorSeverity(error)
        }
      });
    }

    // Store locally for offline scenarios
    this.storeErrorLocally(errorReport);
  }

  getErrorSeverity(error) {
    if (error.message.includes('ChunkLoadError')) return 'medium';
    if (error.name === 'NetworkError') return 'low';
    return 'high';
  }

  attemptRecovery(error) {
    const recoveryStrategies = {
      ChunkLoadError: () => this.handleChunkLoadError(),
      NetworkError: () => this.handleNetworkError(),
      ReferenceError: () => this.handleReferenceError()
    };

    const strategy = recoveryStrategies[error.name];
    if (strategy && this.state.retryCount < 3) {
      setTimeout(() => {
        strategy();
        this.setState(prevState => ({
          retryCount: prevState.retryCount + 1
        }));
      }, 1000 * Math.pow(2, this.state.retryCount)); // Exponential backoff
    }
  }

  handleChunkLoadError() {
    // Clear module cache and reload
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.getRegistrations().then(registrations => {
        registrations.forEach(registration => registration.unregister());
      });
    }
    window.location.reload();
  }

  handleNetworkError() {
    // Retry with cache-first strategy
    this.setState({ hasError: false, error: null });
  }

  handleReferenceError() {
    // Reset component state
    this.setState({ hasError: false, error: null });
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ? (
        this.props.fallback(this.state.error, () => this.setState({ hasError: false }))
      ) : (
        <ErrorFallbackComponent
          error={this.state.error}
          errorId={this.state.errorId}
          onRetry={() => this.setState({ hasError: false })}
          onReport={() => this.reportError(this.state.error, this.state.errorInfo)}
        />
      );
    }

    return this.props.children;
  }
}

// Usage
function App() {
  return (
    <AdvancedErrorBoundary
      name="App"
      fallback={(error, retry) => (
        <div>
          <h2>Something went wrong</h2>
          <details>
            <summary>Error details</summary>
            <pre>{error.message}</pre>
          </details>
          <button onClick={retry}>Retry</button>
        </div>
      )}
    >
      <Routes />
    </AdvancedErrorBoundary>
  );
}
```

### 7. Advanced Performance & Profiling

#### Q19: Memory leaks detection và optimization trong React apps?

**Trả lời:**

```typescript
// 1. Advanced Memory Leak Detection
class MemoryLeakDetector {
  constructor() {
    this.components = new Map();
    this.subscriptions = new Map();
    this.timers = new Map();
    this.observers = new Map();

    this.setupPerformanceObserver();
    this.setupMemoryMonitoring();
  }

  setupPerformanceObserver() {
    if ('PerformanceObserver' in window) {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (entry.entryType === 'measure') {
            this.analyzePerformanceEntry(entry);
          }
        }
      });

      observer.observe({ entryTypes: ['measure', 'navigation', 'resource'] });
    }
  }

  setupMemoryMonitoring() {
    if ('memory' in performance) {
      setInterval(() => {
        const memInfo = performance.memory;
        const memoryUsage = {
          used: memInfo.usedJSHeapSize,
          total: memInfo.totalJSHeapSize,
          limit: memInfo.jsHeapSizeLimit,
          timestamp: Date.now()
        };

        this.analyzeMemoryUsage(memoryUsage);
      }, 5000); // Check every 5 seconds
    }
  }

  analyzeMemoryUsage(memoryUsage) {
    const memoryGrowthRate = this.calculateGrowthRate(memoryUsage);

    if (memoryGrowthRate > 0.1) { // 10% growth per check
      console.warn('Potential memory leak detected', {
        growthRate: memoryGrowthRate,
        currentUsage: memoryUsage
      });

      // Trigger garbage collection if available
      if (window.gc) {
        window.gc();
      }

      // Report to monitoring service
      this.reportMemoryLeak(memoryUsage);
    }
  }

  // Component lifecycle tracking
  trackComponent(componentName, instanceId) {
    const tracking = {
      mountTime: Date.now(),
      renders: 0,
      subscriptions: new Set(),
      timers: new Set(),
      observers: new Set()
    };

    this.components.set(`${componentName}_${instanceId}`, tracking);
    return tracking;
  }

  trackSubscription(componentKey, subscription) {
    const tracking = this.components.get(componentKey);
    if (tracking) {
      tracking.subscriptions.add(subscription);
    }
  }

  trackTimer(componentKey, timerId) {
    const tracking = this.components.get(componentKey);
    if (tracking) {
      tracking.timers.add(timerId);
    }
  }

  untrackComponent(componentKey) {
    const tracking = this.components.get(componentKey);
    if (tracking) {
      // Check for potential leaks
      if (tracking.subscriptions.size > 0) {
        console.warn(`Component ${componentKey} unmounted with active subscriptions`,
          tracking.subscriptions);
      }

      if (tracking.timers.size > 0) {
        console.warn(`Component ${componentKey} unmounted with active timers`,
          tracking.timers);
      }

      this.components.delete(componentKey);
    }
  }
}

// Global instance
window.MemoryLeakDetector = new MemoryLeakDetector();

// 2. Custom Hook với automatic cleanup tracking
function useTrackedEffect(effect, deps, componentName) {
  const componentId = useRef(generateUUID());
  const trackingKey = `${componentName}_${componentId.current}`;

  useEffect(() => {
    // Track component mount
    window.MemoryLeakDetector.trackComponent(componentName, componentId.current);

    const cleanup = effect();

    return () => {
      if (cleanup) cleanup();
      // Track component unmount
      window.MemoryLeakDetector.untrackComponent(trackingKey);
    };
  }, deps);
}

function useTrackedSubscription(subscribe, componentName) {
  const componentId = useRef(generateUUID());
  const trackingKey = `${componentName}_${componentId.current}`;

  useEffect(() => {
    const subscription = subscribe();

    // Track subscription
    window.MemoryLeakDetector.trackSubscription(trackingKey, subscription);

    return () => {
      if (subscription && typeof subscription.unsubscribe === 'function') {
        subscription.unsubscribe();
      } else if (typeof subscription === 'function') {
        subscription();
      }
    };
  }, [subscribe, trackingKey]);
}

// 3. Advanced Performance Profiling
class ReactPerformanceProfiler {
  constructor() {
    this.profiles = new Map();
    this.renderTimes = new Map();
    this.componentMetrics = new Map();
  }

  startProfiling(sessionId) {
    if (React.Profiler) {
      this.profiles.set(sessionId, {
        startTime: Date.now(),
        interactions: [],
        renders: []
      });
    }
  }

  onRender(id, phase, actualDuration, baseDuration, startTime, commitTime, interactions) {
    const profile = this.profiles.get('current') || this.profiles.get('default');

    if (profile) {
      const renderData = {
        id,
        phase,
        actualDuration,
        baseDuration,
        startTime,
        commitTime,
        interactions: Array.from(interactions),
        timestamp: Date.now()
      };

      profile.renders.push(renderData);

      // Analyze for performance issues
      this.analyzeRenderPerformance(renderData);
    }
  }

  analyzeRenderPerformance(renderData) {
    const { id, actualDuration, baseDuration, phase } = renderData;

    // Detect slow renders
    if (actualDuration > 16.67) { // More than one frame at 60fps
      console.warn(`Slow render detected in ${id}`, {
        duration: actualDuration,
        phase,
        recommendation: this.getOptimizationRecommendation(renderData)
      });
    }

    // Detect unnecessary re-renders
    if (phase === 'update' && actualDuration > baseDuration * 2) {
      console.warn(`Inefficient update in ${id}`, {
        actualDuration,
        baseDuration,
        efficiency: baseDuration / actualDuration
      });
    }

    // Track component performance over time
    this.updateComponentMetrics(id, renderData);
  }

  getOptimizationRecommendation(renderData) {
    const recommendations = [];

    if (renderData.actualDuration > 50) {
      recommendations.push('Consider using React.memo() or useMemo()');
    }

    if (renderData.interactions.length > 5) {
      recommendations.push('Too many interactions, consider debouncing');
    }

    return recommendations;
  }

  generatePerformanceReport() {
    const report = {
      totalComponents: this.componentMetrics.size,
      slowComponents: Array.from(this.componentMetrics.entries())
        .filter(([_, metrics]) => metrics.averageDuration > 16.67)
        .map(([id, metrics]) => ({ id, ...metrics })),

      recommendations: this.generateRecommendations(),
      memoryUsage: performance.memory ? {
        used: performance.memory.usedJSHeapSize,
        total: performance.memory.totalJSHeapSize
      } : null
    };

    return report;
  }
}

// 4. Bundle size analysis và optimization
class BundleAnalyzer {
  constructor() {
    this.moduleMap = new Map();
    this.importCosts = new Map();
    this.unusedCode = new Set();
  }

  async analyzeBundleSize() {
    // Analyze loaded modules
    if (window.webpackChunkName) {
      const chunks = await this.getLoadedChunks();
      const analysis = await this.analyzeChunks(chunks);

      return {
        totalSize: analysis.totalSize,
        chunkSizes: analysis.chunkSizes,
        recommendations: this.generateSizeRecommendations(analysis)
      };
    }
  }

  trackImportCost(moduleName, size, loadTime) {
    this.importCosts.set(moduleName, {
      size,
      loadTime,
      timestamp: Date.now()
    });
  }

  detectUnusedCode() {
    // Use intersection observer to track which components are actually rendered
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const componentName = entry.target.dataset.component;
          if (componentName) {
            this.unusedCode.delete(componentName);
          }
        }
      });
    });

    // Track all components initially as unused
    document.querySelectorAll('[data-component]').forEach(element => {
      const componentName = element.dataset.component;
      this.unusedCode.add(componentName);
      observer.observe(element);
    });

    return observer;
  }

  generateSizeRecommendations(analysis) {
    const recommendations = [];

    // Large chunks
    const largeChunks = analysis.chunkSizes
      .filter(chunk => chunk.size > 250 * 1024) // 250KB
      .map(chunk => chunk.name);

    if (largeChunks.length > 0) {
      recommendations.push({
        type: 'code-splitting',
        message: `Consider splitting large chunks: ${largeChunks.join(', ')}`,
        impact: 'high'
      });
    }

    // Expensive imports
    const expensiveImports = Array.from(this.importCosts.entries())
      .filter(([_, cost]) => cost.loadTime > 100)
      .map(([name]) => name);

    if (expensiveImports.length > 0) {
      recommendations.push({
        type: 'lazy-loading',
        message: `Consider lazy loading: ${expensiveImports.join(', ')}`,
        impact: 'medium'
      });
    }

    return recommendations;
  }
}

// 5. Component usage with performance tracking
function withPerformanceTracking(WrappedComponent, componentName) {
  return React.forwardRef((props, ref) => {
    const renderCount = useRef(0);
    const mountTime = useRef(Date.now());
    const lastRenderTime = useRef(Date.now());

    useEffect(() => {
      renderCount.current++;

      const now = Date.now();
      const renderDuration = now - lastRenderTime.current;
      lastRenderTime.current = now;

      // Track performance metrics
      window.ReactPerformanceProfiler?.trackComponentRender(componentName, {
        renderCount: renderCount.current,
        renderDuration,
        totalLifetime: now - mountTime.current
      });

      return () => {
        // Track unmount
        window.ReactPerformanceProfiler?.trackComponentUnmount(componentName, {
          totalRenders: renderCount.current,
          totalLifetime: Date.now() - mountTime.current
        });
      };
    });

    return (
      <React.Profiler
        id={componentName}
        onRender={window.ReactPerformanceProfiler?.onRender}
      >
        <div data-component={componentName}>
          <WrappedComponent {...props} ref={ref} />
        </div>
      </React.Profiler>
    );
  });
}

// Usage
const OptimizedUserProfile = withPerformanceTracking(UserProfile, 'UserProfile');
```

### 8. Advanced Security & Penetration Testing

#### Q20: Implement comprehensive security measures cho frontend apps?

**Trả lời:**

```typescript
// 1. Advanced Security Headers Implementation
class SecurityHeadersManager {
  constructor() {
    this.policies = {
      csp: {
        'default-src': ["'self'"],
        'script-src': ["'self'", "'unsafe-inline'", 'https://trusted-scripts.com'],
        'style-src': ["'self'", "'unsafe-inline'", 'https://fonts.googleapis.com'],
        'img-src': ["'self'", 'data:', 'https://trusted-images.com'],
        'connect-src': ["'self'", 'https://api.yourapp.com', 'wss://ws.yourapp.com'],
        'font-src': ["'self'", 'https://fonts.gstatic.com'],
        'frame-ancestors': ["'none'"],
        'base-uri': ["'self'"],
        'form-action': ["'self'"]
      },
      permissions: {
        camera: [],
        microphone: [],
        geolocation: ['self'],
        notifications: ['self'],
        push: ['self'],
        midi: [],
        accelerometer: [],
        gyroscope: [],
        magnetometer: []
      }
    };
  }

  applySecurityHeaders() {
    // Content Security Policy
    const cspString = Object.entries(this.policies.csp)
      .map(([directive, sources]) => `${directive} ${sources.join(' ')}`)
      .join('; ');

    this.setMetaTag('Content-Security-Policy', cspString);

    // Permissions Policy
    const permissionsString = Object.entries(this.policies.permissions)
      .map(([feature, origins]) => `${feature}=(${origins.join(' ')})`)
      .join(', ');

    this.setMetaTag('Permissions-Policy', permissionsString);

    // Additional security headers
    this.setMetaTag('X-Content-Type-Options', 'nosniff');
    this.setMetaTag('X-Frame-Options', 'DENY');
    this.setMetaTag('X-XSS-Protection', '1; mode=block');
    this.setMetaTag('Referrer-Policy', 'strict-origin-when-cross-origin');
    this.setMetaTag('Strict-Transport-Security', 'max-age=31536000; includeSubDomains');
  }

  setMetaTag(name, content) {
    let meta = document.querySelector(`meta[http-equiv="${name}"]`);
    if (!meta) {
      meta = document.createElement('meta');
      meta.httpEquiv = name;
      document.head.appendChild(meta);
    }
    meta.content = content;
  }

  // Runtime CSP violation detection
  setupCSPViolationReporting() {
    document.addEventListener('securitypolicyviolation', (event) => {
      const violation = {
        blockedURI: event.blockedURI,
        violatedDirective: event.violatedDirective,
        originalPolicy: event.originalPolicy,
        sourceFile: event.sourceFile,
        lineNumber: event.lineNumber,
        timestamp: Date.now()
      };

      // Report violation to security monitoring
      this.reportSecurityViolation('csp', violation);

      // Auto-adjust policy for development
      if (process.env.NODE_ENV === 'development') {
        this.suggestPolicyUpdate(violation);
      }
    });
  }

  reportSecurityViolation(type, details) {
    if (window.securityMonitor) {
      window.securityMonitor.reportViolation(type, details);
    }

    // Store locally for analysis
    const violations = JSON.parse(localStorage.getItem('security_violations') || '[]');
    violations.push({ type, details, timestamp: Date.now() });
    localStorage.setItem('security_violations', JSON.stringify(violations.slice(-100))); // Keep last 100
  }
}

// 2. Advanced Input Validation và Sanitization
class AdvancedValidator {
  constructor() {
    this.rules = new Map();
    this.sanitizers = new Map();
    this.patterns = {
      email: /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/,
      phone: /^\+?[\d\s-()]{10,15}$/,
      url: /^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)$/,
      creditCard: /^\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}$/,
      ssn: /^\d{3}-\d{2}-\d{4}$/
    };
  }

  addRule(fieldName, validator) {
    this.rules.set(fieldName, validator);
  }

  addSanitizer(fieldName, sanitizer) {
    this.sanitizers.set(fieldName, sanitizer);
  }

  // Advanced validation with context awareness
  validate(data, context = {}) {
    const results = {
      isValid: true,
      errors: {},
      warnings: {},
      sanitized: {}
    };

    for (const [field, value] of Object.entries(data)) {
      // Sanitize first
      const sanitized = this.sanitizeField(field, value, context);
      results.sanitized[field] = sanitized;

      // Then validate
      const validation = this.validateField(field, sanitized, context);

      if (!validation.isValid) {
        results.isValid = false;
        results.errors[field] = validation.errors;
      }

      if (validation.warnings?.length > 0) {
        results.warnings[field] = validation.warnings;
      }
    }

    return results;
  }

  sanitizeField(fieldName, value, context) {
    if (typeof value !== 'string') return value;

    // Apply field-specific sanitization
    const sanitizer = this.sanitizers.get(fieldName);
    if (sanitizer) {
      value = sanitizer(value, context);
    }

    // Universal sanitization
    return this.applySafeSanitization(value);
  }

  applySafeSanitization(value) {
    return value
      // Remove null bytes
      .replace(/\0/g, '')
      // Remove or escape dangerous HTML
      .replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '')
      .replace(/<iframe\b[^<]*(?:(?!<\/iframe>)<[^<]*)*<\/iframe>/gi, '')
      // Normalize whitespace
      .replace(/\s+/g, ' ')
      .trim();
  }

  validateField(fieldName, value, context) {
    const result = {
      isValid: true,
      errors: [],
      warnings: []
    };

    // Check for common attack patterns
    this.checkForAttackPatterns(value, result);

    // Apply field-specific validation
    const rule = this.rules.get(fieldName);
    if (rule) {
      const ruleResult = rule(value, context);
      if (!ruleResult.isValid) {
        result.isValid = false;
        result.errors.push(...ruleResult.errors);
      }
    }

    // Pattern validation
    if (this.patterns[fieldName] && !this.patterns[fieldName].test(value)) {
      result.isValid = false;
      result.errors.push(`Invalid ${fieldName} format`);
    }

    return result;
  }

  checkForAttackPatterns(value, result) {
    const attackPatterns = [
      { pattern: /<script|javascript:|vbscript:|onload=|onerror=/i, type: 'XSS' },
      { pattern: /union.*select|select.*from|insert.*into|delete.*from/i, type: 'SQL Injection' },
      { pattern: /\.\.|\/etc\/|\/proc\/|\/var\/|\/tmp\//i, type: 'Path Traversal' },
      { pattern: /eval\s*\(|Function\s*\(|setTimeout\s*\(.*script/i, type: 'Code Injection' }
    ];

    for (const { pattern, type } of attackPatterns) {
      if (pattern.test(value)) {
        result.warnings.push(`Potential ${type} attack detected`);

        // Report to security monitoring
        window.SecurityHeadersManager?.reportSecurityViolation('input_attack', {
          type,
          value: value.substring(0, 100), // Truncate for privacy
          pattern: pattern.toString()
        });
      }
    }
  }
}

// 3. Runtime Security Monitoring
class SecurityMonitor {
  constructor() {
    this.threats = new Map();
    this.metrics = {
      requestCount: 0,
      suspiciousRequests: 0,
      blockedRequests: 0,
      xssAttempts: 0,
      csrfAttempts: 0
    };

    this.setupGlobalErrorHandler();
    this.setupNetworkMonitoring();
    this.setupDOMTamperingDetection();
  }

  setupGlobalErrorHandler() {
    window.addEventListener('error', (event) => {
      // Check for suspicious errors that might indicate attacks
      if (this.isSuspiciousError(event.error)) {
        this.reportThreat('suspicious_error', {
          message: event.error.message,
          stack: event.error.stack,
          filename: event.filename,
          lineno: event.lineno
        });
      }
    });

    window.addEventListener('unhandledrejection', (event) => {
      if (this.isSuspiciousPromiseRejection(event.reason)) {
        this.reportThreat('suspicious_rejection', {
          reason: event.reason.toString()
        });
      }
    });
  }

  setupNetworkMonitoring() {
    // Intercept fetch requests
    const originalFetch = window.fetch;
    window.fetch = async (...args) => {
      const [url, options] = args;

      this.metrics.requestCount++;

      // Analyze request for suspicious patterns
      if (this.isSuspiciousRequest(url, options)) {
        this.metrics.suspiciousRequests++;
        this.reportThreat('suspicious_request', { url, options });
      }

      try {
        const response = await originalFetch(...args);

        // Analyze response headers for security issues
        this.analyzeResponseSecurity(response);

        return response;
      } catch (error) {
        this.reportThreat('network_error', { error: error.message, url });
        throw error;
      }
    };
  }

  setupDOMTamperingDetection() {
    // Monitor for unauthorized DOM modifications
    const observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        if (mutation.type === 'childList') {
          mutation.addedNodes.forEach((node) => {
            if (node.nodeType === Node.ELEMENT_NODE) {
              this.checkForMaliciousElement(node);
            }
          });
        }
      });
    });

    observer.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['src', 'href', 'onclick', 'onload']
    });
  }

  isSuspiciousError(error) {
    const suspiciousPatterns = [
      /script error/i,
      /permission denied/i,
      /access denied/i,
      /unauthorized/i
    ];

    return suspiciousPatterns.some(pattern =>
      pattern.test(error.message || error.toString())
    );
  }

  isSuspiciousRequest(url, options = {}) {
    // Check for suspicious URL patterns
    const suspiciousUrlPatterns = [
      /\.\.|\/etc\/|\/proc\/|\/var\//,
      /<script|javascript:|data:/i,
      /\?(.*&){20,}/, // Too many parameters
    ];

    if (suspiciousUrlPatterns.some(pattern => pattern.test(url))) {
      return true;
    }

    // Check for suspicious headers
    const headers = options.headers || {};
    if (headers['User-Agent']?.includes('curl') ||
        headers['User-Agent']?.includes('wget')) {
      return true;
    }

    return false;
  }

  checkForMaliciousElement(element) {
    // Check for suspicious scripts
    if (element.tagName === 'SCRIPT') {
      const src = element.getAttribute('src');
      const content = element.textContent;

      if (src && !this.isAllowedScriptSource(src)) {
        this.reportThreat('unauthorized_script', { src });
        element.remove();
        this.metrics.blockedRequests++;
      }

      if (content && this.containsMaliciousCode(content)) {
        this.reportThreat('malicious_inline_script', { content });
        element.remove();
        this.metrics.blockedRequests++;
      }
    }

    // Check for suspicious iframes
    if (element.tagName === 'IFRAME') {
      const src = element.getAttribute('src');
      if (src && !this.isAllowedFrameSource(src)) {
        this.reportThreat('unauthorized_iframe', { src });
        element.remove();
        this.metrics.blockedRequests++;
      }
    }
  }

  reportThreat(type, details) {
    const threat = {
      type,
      details,
      timestamp: Date.now(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      sessionId: this.getSessionId()
    };

    this.threats.set(Date.now(), threat);

    // Send to security endpoint
    this.sendSecurityAlert(threat);

    // Log locally for analysis
    console.warn('[Security Monitor] Threat detected:', threat);
  }

  generateSecurityReport() {
    return {
      threats: Array.from(this.threats.values()),
      metrics: this.metrics,
      timestamp: Date.now(),
      recommendations: this.generateRecommendations()
    };
  }

  generateRecommendations() {
    const recommendations = [];

    if (this.metrics.xssAttempts > 0) {
      recommendations.push({
        type: 'XSS_PROTECTION',
        message: 'Implement stricter input validation and output encoding',
        priority: 'high'
      });
    }

    if (this.metrics.suspiciousRequests / this.metrics.requestCount > 0.1) {
      recommendations.push({
        type: 'RATE_LIMITING',
        message: 'Consider implementing rate limiting',
        priority: 'medium'
      });
    }

    return recommendations;
  }
}
```

#### Q21: Advanced debugging và production monitoring?

**Trả lời:**

```typescript
// 1. Advanced Error Tracking và Debugging
class AdvancedErrorTracker {
  constructor() {
    this.errorQueue = [];
    this.userSessions = new Map();
    this.performanceMetrics = new Map();
    this.breadcrumbs = [];
    this.maxBreadcrumbs = 50;

    this.setupErrorHandlers();
    this.setupPerformanceMonitoring();
    this.setupUserSessionTracking();
  }

  setupErrorHandlers() {
    // Global error handler
    window.addEventListener('error', (event) => {
      this.captureError({
        type: 'javascript',
        message: event.message,
        filename: event.filename,
        lineno: event.lineno,
        colno: event.colno,
        stack: event.error?.stack,
        timestamp: Date.now()
      });
    });

    // Unhandled promise rejections
    window.addEventListener('unhandledrejection', (event) => {
      this.captureError({
        type: 'unhandled_promise',
        message: event.reason?.message || event.reason,
        stack: event.reason?.stack,
        timestamp: Date.now()
      });
    });

    // Resource loading errors
    window.addEventListener('error', (event) => {
      if (event.target !== window) {
        this.captureError({
          type: 'resource',
          message: `Failed to load ${event.target.tagName}: ${event.target.src || event.target.href}`,
          element: event.target.outerHTML,
          timestamp: Date.now()
        });
      }
    }, true);
  }

  captureError(errorData) {
    const enhancedError = {
      ...errorData,
      id: this.generateErrorId(),
      url: window.location.href,
      userAgent: navigator.userAgent,
      viewport: {
        width: window.innerWidth,
        height: window.innerHeight
      },
      sessionId: this.getCurrentSessionId(),
      breadcrumbs: [...this.breadcrumbs],
      user: this.getCurrentUserContext(),
      environment: {
        timestamp: Date.now(),
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        language: navigator.language,
        online: navigator.onLine,
        memory: performance.memory ? {
          used: performance.memory.usedJSHeapSize,
          total: performance.memory.totalJSHeapSize,
          limit: performance.memory.jsHeapSizeLimit
        } : null
      }
    };

    // Add React component stack if available
    if (window.React && window.React.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED) {
      enhancedError.componentStack = this.getReactComponentStack();
    }

    this.errorQueue.push(enhancedError);
    this.processError(enhancedError);
    this.sendErrorToMonitoring(enhancedError);
  }

  addBreadcrumb(message, category = 'default', level = 'info', data = {}) {
    const breadcrumb = {
      message,
      category,
      level,
      data,
      timestamp: Date.now()
    };

    this.breadcrumbs.push(breadcrumb);

    if (this.breadcrumbs.length > this.maxBreadcrumbs) {
      this.breadcrumbs.shift();
    }
  }

  // Advanced source map support for production debugging
  async resolveSourceLocation(filename, lineno, colno) {
    try {
      if (!filename.includes('.min.') && !filename.includes('.prod.')) {
        return { filename, lineno, colno };
      }

      const sourceMapUrl = await this.getSourceMapUrl(filename);
      if (!sourceMapUrl) return { filename, lineno, colno };

      const sourceMap = await this.loadSourceMap(sourceMapUrl);
      const originalPosition = this.resolveOriginalPosition(sourceMap, lineno, colno);

      return {
        filename: originalPosition.source,
        lineno: originalPosition.line,
        colno: originalPosition.column,
        originalFilename: filename
      };
    } catch (error) {
      console.warn('Failed to resolve source location:', error);
      return { filename, lineno, colno };
    }
  }

  // React component stack extraction
  getReactComponentStack() {
    try {
      const fiber = this.findReactFiberNode(document.body);
      if (!fiber) return null;

      const stack = [];
      let current = fiber;

      while (current) {
        if (current.type && typeof current.type === 'function') {
          stack.push({
            name: current.type.name || current.type.displayName || 'Anonymous',
            props: this.sanitizeProps(current.memoizedProps),
            state: this.sanitizeState(current.memoizedState)
          });
        }
        current = current.return;
      }

      return stack;
    } catch (error) {
      return null;
    }
  }

  // Performance monitoring integration
  setupPerformanceMonitoring() {
    // Web Vitals tracking
    this.trackWebVitals();

    // Long task monitoring
    if ('PerformanceObserver' in window) {
      const observer = new PerformanceObserver((list) => {
        for (const entry of list.getEntries()) {
          if (entry.duration > 50) { // Tasks longer than 50ms
            this.addBreadcrumb(
              `Long task detected: ${entry.duration}ms`,
              'performance',
              'warning',
              {
                duration: entry.duration,
                startTime: entry.startTime,
                name: entry.name
              }
            );
          }
        }
      });

      observer.observe({ entryTypes: ['longtask'] });
    }

    // Resource timing
    this.monitorResourceTiming();
  }

  trackWebVitals() {
    // First Contentful Paint
    this.observePerformanceEntry('paint', (entry) => {
      if (entry.name === 'first-contentful-paint') {
        this.recordMetric('FCP', entry.startTime);
      }
    });

    // Largest Contentful Paint
    this.observePerformanceEntry('largest-contentful-paint', (entry) => {
      this.recordMetric('LCP', entry.startTime);
    });

    // First Input Delay
    this.observePerformanceEntry('first-input', (entry) => {
      this.recordMetric('FID', entry.processingStart - entry.startTime);
    });

    // Cumulative Layout Shift
    let clsValue = 0;
    this.observePerformanceEntry('layout-shift', (entry) => {
      if (!entry.hadRecentInput) {
        clsValue += entry.value;
        this.recordMetric('CLS', clsValue);
      }
    });
  }

  // Real-time monitoring dashboard
  createMonitoringDashboard() {
    if (process.env.NODE_ENV !== 'development') return;

    const dashboard = document.createElement('div');
    dashboard.style.cssText = `
      position: fixed;
      top: 10px;
      right: 10px;
      width: 300px;
      background: rgba(0, 0, 0, 0.9);
      color: white;
      padding: 10px;
      border-radius: 5px;
      font-family: monospace;
      font-size: 12px;
      z-index: 10000;
      max-height: 400px;
      overflow-y: auto;
    `;

    this.updateDashboard(dashboard);

    setInterval(() => {
      this.updateDashboard(dashboard);
    }, 1000);

    document.body.appendChild(dashboard);
  }

  updateDashboard(dashboard) {
    const metrics = this.getMetricsSummary();
    const recentErrors = this.errorQueue.slice(-5);

    dashboard.innerHTML = `
      <h4>🔍 Debug Monitor</h4>
      <div>Errors: ${this.errorQueue.length}</div>
      <div>Memory: ${this.formatBytes(performance.memory?.usedJSHeapSize || 0)}</div>
      <div>FCP: ${metrics.FCP?.toFixed(2) || 'N/A'}ms</div>
      <div>LCP: ${metrics.LCP?.toFixed(2) || 'N/A'}ms</div>

      <h5>Recent Errors:</h5>
      ${recentErrors.map(error => `
        <div style="margin: 5px 0; padding: 5px; background: rgba(255,0,0,0.2);">
          <div>${error.type}: ${error.message}</div>
          <div style="font-size: 10px; opacity: 0.7;">
            ${new Date(error.timestamp).toLocaleTimeString()}
          </div>
        </div>
      `).join('')}

      <h5>Recent Breadcrumbs:</h5>
      ${this.breadcrumbs.slice(-3).map(crumb => `
        <div style="margin: 2px 0; font-size: 10px;">
          [${crumb.category}] ${crumb.message}
        </div>
      `).join('')}
    `;
  }
}

// 2. Advanced React DevTools Integration
class ReactDevToolsIntegration {
  constructor() {
    this.componentProfiles = new Map();
    this.renderCounts = new Map();
    this.setupReactDevToolsHooks();
  }

  setupReactDevToolsHooks() {
    if (window.__REACT_DEVTOOLS_GLOBAL_HOOK__) {
      const hook = window.__REACT_DEVTOOLS_GLOBAL_HOOK__;

      // Intercept fiber commits
      hook.onCommitFiberRoot = (id, root, priorityLevel) => {
        this.analyzeCommit(root, priorityLevel);
      };

      // Track component updates
      hook.onCommitFiberUnmount = (id, fiber) => {
        this.trackComponentUnmount(fiber);
      };
    }
  }

  analyzeCommit(root, priorityLevel) {
    const commitTime = performance.now();

    this.traverseFiber(root.current, (fiber) => {
      if (fiber.actualDuration > 0) {
        const componentName = this.getComponentName(fiber);

        if (!this.componentProfiles.has(componentName)) {
          this.componentProfiles.set(componentName, {
            renderCount: 0,
            totalTime: 0,
            averageTime: 0,
            maxTime: 0,
            minTime: Infinity
          });
        }

        const profile = this.componentProfiles.get(componentName);
        profile.renderCount++;
        profile.totalTime += fiber.actualDuration;
        profile.averageTime = profile.totalTime / profile.renderCount;
        profile.maxTime = Math.max(profile.maxTime, fiber.actualDuration);
        profile.minTime = Math.min(profile.minTime, fiber.actualDuration);

        // Warn about slow components
        if (fiber.actualDuration > 16.67) { // More than one frame
          console.warn(`Slow render: ${componentName} took ${fiber.actualDuration.toFixed(2)}ms`);
        }
      }
    });
  }

  // Component dependency analysis
  analyzeComponentDependencies(component) {
    const dependencies = {
      props: new Set(),
      context: new Set(),
      hooks: new Set(),
      state: new Set()
    };

    // Analyze props
    if (component.memoizedProps) {
      Object.keys(component.memoizedProps).forEach(prop => {
        dependencies.props.add(prop);
      });
    }

    // Analyze hooks
    let hook = component.memoizedState;
    while (hook) {
      if (hook.queue) {
        dependencies.hooks.add(this.getHookType(hook));
      }
      hook = hook.next;
    }

    return dependencies;
  }

  generatePerformanceReport() {
    const report = {
      timestamp: Date.now(),
      components: Array.from(this.componentProfiles.entries()).map(([name, profile]) => ({
        name,
        ...profile,
        efficiency: profile.minTime / profile.maxTime // Closer to 1 is better
      })),
      recommendations: this.generateOptimizationRecommendations()
    };

    return report;
  }

  generateOptimizationRecommendations() {
    const recommendations = [];

    for (const [name, profile] of this.componentProfiles.entries()) {
      if (profile.averageTime > 10) {
        recommendations.push({
          component: name,
          issue: 'Slow average render time',
          suggestion: 'Consider using React.memo() or optimizing render logic',
          priority: profile.averageTime > 20 ? 'high' : 'medium'
        });
      }

      if (profile.renderCount > 100 && profile.efficiency < 0.5) {
        recommendations.push({
          component: name,
          issue: 'Inconsistent render performance',
          suggestion: 'Check for expensive operations or unnecessary re-renders',
          priority: 'medium'
        });
      }
    }

    return recommendations;
  }
}

// 3. Production monitoring integration
class ProductionMonitor {
  constructor() {
    this.config = {
      sampleRate: 0.1, // Sample 10% of sessions
      maxErrors: 50,
      batchSize: 10,
      flushInterval: 30000 // 30 seconds
    };

    this.initializeMonitoring();
  }

  initializeMonitoring() {
    // Only monitor in production
    if (process.env.NODE_ENV !== 'production') return;

    // Sample sessions
    if (Math.random() > this.config.sampleRate) return;

    this.errorTracker = new AdvancedErrorTracker();
    this.performanceMonitor = new ReactDevToolsIntegration();

    this.setupBatchedReporting();
    this.setupVisibilityTracking();
  }

  setupBatchedReporting() {
    setInterval(() => {
      this.flushPendingData();
    }, this.config.flushInterval);

    // Flush on page unload
    window.addEventListener('beforeunload', () => {
      this.flushPendingData(true);
    });
  }

  setupVisibilityTracking() {
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        this.flushPendingData();
      }
    });
  }

  flushPendingData(immediate = false) {
    const data = {
      errors: this.errorTracker.errorQueue.splice(0),
      performance: this.performanceMonitor.generatePerformanceReport(),
      session: {
        id: this.getSessionId(),
        duration: Date.now() - this.sessionStartTime,
        pageViews: this.pageViewCount,
        interactions: this.interactionCount
      }
    };

    if (data.errors.length > 0 || immediate) {
      this.sendToMonitoringService(data, immediate);
    }
  }

  sendToMonitoringService(data, immediate = false) {
    const url = '/api/monitoring/events';
    const payload = JSON.stringify(data);

    if (immediate && navigator.sendBeacon) {
      // Use sendBeacon for reliable delivery during page unload
      navigator.sendBeacon(url, payload);
    } else {
      // Use fetch with keepalive for regular sends
      fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: payload,
        keepalive: true
      }).catch(error => {
        console.warn('Failed to send monitoring data:', error);
        // Store locally for retry
        this.storeForRetry(data);
      });
    }
  }
}

// Global initialization
if (typeof window !== 'undefined') {
  window.AdvancedErrorTracker = new AdvancedErrorTracker();
  window.ReactDevTools = new ReactDevToolsIntegration();
  window.ProductionMonitor = new ProductionMonitor();

  // Create debug dashboard in development
  if (process.env.NODE_ENV === 'development') {
    window.AdvancedErrorTracker.createMonitoringDashboard();
  }
}
```

---

## Conclusion

Đây là bộ câu hỏi phỏng vấn toàn diện từ cơ bản đến Expert level, bao gồm:

### **Junior Level:**
1. **JavaScript Fundamentals**: Event Loop, Closures, Hoisting
2. **React Core Concepts**: Hooks, Components, State Management

### **Mid-Level:**
3. **Advanced React Concepts**: Custom Hooks, Context API vs Redux
4. **Performance Optimization**: Memoization, Code Splitting

### **Senior Level:**
5. **Advanced Patterns**: HOC, Render Props, Custom Hooks
6. **Security Best Practices**: XSS Prevention, CSRF Protection, Data Privacy

### **Expert/Lead Level:**
7. **System Design & Architecture**: Micro-frontends, Advanced Caching
8. **Advanced Performance & Profiling**: Memory Leak Detection, Bundle Analysis
9. **Enterprise Patterns**: Event Sourcing, Advanced Error Boundaries
10. **React Advanced Topics**: Concurrent Mode, Suspense, Server Components
11. **Clean Code & Best Practices**: SOLID principles, Code organization
12. **Performance Optimization**: Advanced React optimization techniques
13. **Testing Strategies**: Unit, Integration, E2E, Performance, A11y Testing
14. **Accessibility (A11y)**: ARIA patterns, Screen readers, Semantic HTML

## **Tóm Tắt Bộ Câu Hỏi Hoàn Chỉnh**

### 📊 **Thống Kê:**
- **Tổng cộng: 28 câu hỏi chuyên sâu**
- **6,900+ dòng code examples**
- **14 chủ đề chính từ cơ bản đến Expert**
- **Production-ready solutions với real-world scenarios**

### 🎯 **Phân Cấp Câu Hỏi:**

**Junior Level (4 câu):**
- Q1-Q4: JavaScript fundamentals, React basics, useState, useEffect

**Mid-Level (3 câu):**
- Q5-Q7: Advanced React concepts, Custom Hooks, Context vs Redux

**Senior Level (8 câu):**
- Q8-Q15: Performance optimization, Security best practices, HOC/Render Props

**Expert/Lead Level (13 câu):**
- Q16-Q28: System design, Advanced debugging, Clean code, Testing, A11y

### 🚀 **Điểm Nổi Bật:**

✅ **React 18 Features**: Concurrent Mode, Suspense, useTransition, useDeferredValue
✅ **Modern Patterns**: Server Components, Micro-frontends, Event Sourcing
✅ **Performance**: Memory leak detection, Bundle optimization, Virtualization
✅ **Security**: XSS prevention, CSRF protection, Runtime monitoring
✅ **Testing**: Unit, Integration, E2E, Performance, Visual regression
✅ **Accessibility**: ARIA patterns, Screen readers, Focus management
✅ **Clean Code**: SOLID principles, Feature-based architecture
✅ **Production Ready**: Error boundaries, Monitoring, Debugging tools

### 🔧 **Advanced Topics Covered:**

**System Architecture:**
- Module Federation với Webpack 5
- Event-driven communication
- Cross-domain state management
- Multi-layer caching strategies

**Performance Engineering:**
- Advanced memoization techniques
- Component splitting và lazy loading
- Memory management và cleanup
- Bundle size optimization

**Security Engineering:**
- Runtime security monitoring
- Input validation và sanitization
- Content Security Policy implementation
- Threat detection patterns

**Testing Engineering:**
- Comprehensive testing strategies
- Performance regression testing
- Accessibility compliance testing
- Visual regression với Storybook

Mỗi câu hỏi đều có ví dụ code production-ready và giải thích chi tiết về architectural decisions, performance implications, và best practices cho enterprise applications.

### 9. React Advanced Topics & Modern Features

#### Q22: React Concurrent Mode và Suspense - Cách hoạt động và ứng dụng?

**Trả lời:**

```typescript
// 1. React Concurrent Mode - Time Slicing và Interruptible Rendering
function App() {
  const [isPending, startTransition] = useTransition();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const deferredQuery = useDeferredValue(query);

  // High priority update - user input
  const handleInputChange = (e) => {
    const value = e.target.value;
    setQuery(value); // Immediate update

    // Low priority update - search results
    startTransition(() => {
      performSearch(value).then(setResults);
    });
  };

  return (
    <div>
      <input
        value={query}
        onChange={handleInputChange}
        placeholder="Search..."
      />

      {isPending && <div>Searching...</div>}

      <Suspense fallback={<SearchResultsSkeleton />}>
        <SearchResults query={deferredQuery} results={results} />
      </Suspense>
    </div>
  );
}

// 2. Advanced Suspense Patterns
const SearchResults = React.lazy(() =>
  import('./SearchResults').then(module => {
    // Simulate slow component
    return new Promise(resolve => {
      setTimeout(() => resolve(module), 1000);
    });
  })
);

// Suspense với Error Boundary
function SuspenseWrapper({ children, fallback }) {
  return (
    <ErrorBoundary
      fallback={<ErrorFallback />}
      onError={(error, errorInfo) => {
        console.error('Suspense error:', error);
        // Report to monitoring service
      }}
    >
      <Suspense fallback={fallback}>
        {children}
      </Suspense>
    </ErrorBoundary>
  );
}

// 3. Data Fetching với Suspense
function createSuspenseResource(promise) {
  let status = 'pending';
  let result;

  const suspender = promise.then(
    response => {
      status = 'success';
      result = response;
    },
    error => {
      status = 'error';
      result = error;
    }
  );

  return {
    read() {
      if (status === 'pending') {
        throw suspender; // Suspend component
      } else if (status === 'error') {
        throw result; // Trigger error boundary
      } else if (status === 'success') {
        return result;
      }
    }
  };
}

// Advanced data fetching hook với Suspense
function useSuspenseQuery(queryKey, queryFn, options = {}) {
  const [resource, setResource] = useState(() => {
    const cachedData = getCachedData(queryKey);
    if (cachedData && !isStale(cachedData, options.staleTime)) {
      return createSuspenseResource(Promise.resolve(cachedData));
    }
    return createSuspenseResource(queryFn());
  });

  useEffect(() => {
    const shouldRefetch = options.refetchOnMount ||
                         (options.refetchOnWindowFocus && document.hasFocus());

    if (shouldRefetch) {
      const newResource = createSuspenseResource(queryFn());
      setResource(newResource);
    }
  }, [queryKey]);

  return resource.read();
}

// Usage với Suspense
function UserProfile({ userId }) {
  const user = useSuspenseQuery(
    ['user', userId],
    () => fetchUser(userId),
    {
      staleTime: 5 * 60 * 1000,
      refetchOnWindowFocus: true
    }
  );

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
    </div>
  );
}

// 4. Concurrent Features với useTransition
function FilterableList({ items }) {
  const [filter, setFilter] = useState('');
  const [isPending, startTransition] = useTransition();
  const [filteredItems, setFilteredItems] = useState(items);

  const handleFilterChange = (value) => {
    setFilter(value); // High priority - immediate UI update

    // Low priority - expensive filtering operation
    startTransition(() => {
      const filtered = items.filter(item =>
        item.name.toLowerCase().includes(value.toLowerCase()) ||
        item.description.toLowerCase().includes(value.toLowerCase())
      );
      setFilteredItems(filtered);
    });
  };

  return (
    <div>
      <input
        value={filter}
        onChange={(e) => handleFilterChange(e.target.value)}
        placeholder="Filter items..."
      />

      <div style={{ opacity: isPending ? 0.7 : 1 }}>
        {filteredItems.map(item => (
          <ListItem key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}

// 5. Server Components Integration (Next.js 13+)
// app/dashboard/page.tsx - Server Component
async function DashboardPage() {
  // This runs on the server
  const user = await fetchUser();
  const stats = await fetchDashboardStats();

  return (
    <div>
      <h1>Dashboard</h1>
      <UserGreeting user={user} />

      <Suspense fallback={<StatsLoading />}>
        <DashboardStats stats={stats} />
      </Suspense>

      {/* Client Component */}
      <InteractiveChart />
    </div>
  );
}

// Client Component với 'use client' directive
'use client';
function InteractiveChart() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Client-side data fetching
    fetchChartData().then(setData);
  }, []);

  return (
    <div>
      <canvas ref={chartRef} />
      <button onClick={refreshData}>Refresh</button>
    </div>
  );
}
```

#### Q23: React 18 features và migration strategies?

**Trả lời:**

```typescript
// 1. Migration từ React 17 to React 18
// Before (React 17)
import ReactDOM from 'react-dom';
ReactDOM.render(<App />, document.getElementById('root'));

// After (React 18)
import { createRoot } from 'react-dom/client';
const root = createRoot(document.getElementById('root'));
root.render(<App />);

// 2. Automatic Batching
function BatchingExample() {
  const [count, setCount] = useState(0);
  const [flag, setFlag] = useState(false);

  // React 18: These updates are automatically batched
  const handleClick = () => {
    setCount(c => c + 1);
    setFlag(f => !f);
    // Only one re-render in React 18
  };

  // Even in async operations
  const handleAsyncClick = async () => {
    await fetch('/api/data');
    setCount(c => c + 1); // Batched
    setFlag(f => !f);     // Batched
  };

  // Opt-out of batching if needed
  const handleNoBatching = () => {
    flushSync(() => {
      setCount(c => c + 1);
    });
    // This will re-render immediately
    setFlag(f => !f);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <p>Flag: {flag.toString()}</p>
      <button onClick={handleClick}>Update State</button>
      <button onClick={handleAsyncClick}>Async Update</button>
      <button onClick={handleNoBatching}>No Batching</button>
    </div>
  );
}

// 3. Strict Mode Changes và Development Warnings
function StrictModeApp() {
  return (
    <StrictMode>
      <App />
    </StrictMode>
  );
}

// React 18 Strict Mode: Effects run twice in development
function EffectExample() {
  const [data, setData] = useState(null);

  useEffect(() => {
    let cancelled = false;

    const fetchData = async () => {
      try {
        const response = await fetch('/api/data');
        const result = await response.json();

        if (!cancelled) {
          setData(result);
        }
      } catch (error) {
        if (!cancelled) {
          console.error('Fetch error:', error);
        }
      }
    };

    fetchData();

    // Cleanup function - important for React 18 Strict Mode
    return () => {
      cancelled = true;
    };
  }, []);

  return <div>{data ? JSON.stringify(data) : 'Loading...'}</div>;
}

// 4. New Hooks trong React 18
function NewHooksExample() {
  // useId - for generating unique IDs
  const id = useId();
  const emailId = `${id}-email`;
  const passwordId = `${id}-password`;

  // useSyncExternalStore - for external state
  const isOnline = useSyncExternalStore(
    (callback) => {
      window.addEventListener('online', callback);
      window.addEventListener('offline', callback);
      return () => {
        window.removeEventListener('online', callback);
        window.removeEventListener('offline', callback);
      };
    },
    () => navigator.onLine,
    () => true // Server-side value
  );

  // useInsertionEffect - for CSS-in-JS libraries
  useInsertionEffect(() => {
    const style = document.createElement('style');
    style.textContent = `
      .dynamic-${id} {
        color: blue;
        font-weight: bold;
      }
    `;
    document.head.appendChild(style);

    return () => {
      document.head.removeChild(style);
    };
  }, [id]);

  return (
    <form>
      <div>
        <label htmlFor={emailId}>Email:</label>
        <input id={emailId} type="email" />
      </div>

      <div>
        <label htmlFor={passwordId}>Password:</label>
        <input id={passwordId} type="password" />
      </div>

      <div className={`dynamic-${id}`}>
        Status: {isOnline ? 'Online' : 'Offline'}
      </div>
    </form>
  );
}

// 5. Error Handling Improvements
class AdvancedErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }

  componentDidCatch(error, errorInfo) {
    // React 18: Better error reporting
    console.error('Error boundary caught:', {
      error,
      errorInfo,
      componentStack: errorInfo.componentStack,
      errorBoundary: this.constructor.name
    });

    // Report to error tracking service
    if (window.errorReporter) {
      window.errorReporter.captureException(error, {
        contexts: {
          react: {
            componentStack: errorInfo.componentStack
          }
        }
      });
    }
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback ? (
        this.props.fallback(this.state.error)
      ) : (
        <div>
          <h2>Something went wrong.</h2>
          <details style={{ whiteSpace: 'pre-wrap' }}>
            {this.state.error && this.state.error.toString()}
          </details>
        </div>
      );
    }

    return this.props.children;
  }
}

// 6. Migration Best Practices
function MigrationChecklist() {
  /*
  React 18 Migration Checklist:

  1. Update React and ReactDOM
     npm install react@18 react-dom@18

  2. Replace ReactDOM.render with createRoot
     - ReactDOM.render(<App />, container)
     + const root = createRoot(container); root.render(<App />)

  3. Update TypeScript types
     npm install @types/react@18 @types/react-dom@18

  4. Test with Strict Mode
     - Enable <StrictMode> in development
     - Fix any double-effect issues

  5. Review third-party dependencies
     - Check compatibility with React 18
     - Update libraries that use ReactDOM.render

  6. Test Suspense boundaries
     - Ensure error boundaries wrap Suspense
     - Test loading states thoroughly

  7. Performance testing
     - Measure before/after migration
     - Test concurrent features gradually
  */

  return null;
}

// 7. Advanced Concurrent Patterns
function AdvancedConcurrentApp() {
  const [tab, setTab] = useState('posts');
  const [isPending, startTransition] = useTransition();

  const handleTabChange = (newTab) => {
    startTransition(() => {
      setTab(newTab);
    });
  };

  return (
    <div>
      <TabBar
        activeTab={tab}
        onTabChange={handleTabChange}
        isPending={isPending}
      />

      <Suspense fallback={<TabContentSkeleton />}>
        <TabContent tab={tab} />
      </Suspense>
    </div>
  );
}

function TabContent({ tab }) {
  const data = useSuspenseQuery(['tab', tab], () => fetchTabData(tab));

  return <div>{renderTabContent(tab, data)}</div>;
}
```

### 10. Clean Code Principles & Best Practices

#### Q24: SOLID principles áp dụng trong React components?

**Trả lời:**

```typescript
// 1. Single Responsibility Principle (SRP)
// ❌ Bad: Component làm quá nhiều việc
function BadUserProfile({ userId }) {
  const [user, setUser] = useState(null);
  const [posts, setPosts] = useState([]);
  const [followers, setFollowers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetching user data
    fetch(`/api/users/${userId}`)
      .then(res => res.json())
      .then(setUser);

    // Fetching posts
    fetch(`/api/users/${userId}/posts`)
      .then(res => res.json())
      .then(setPosts);

    // Fetching followers
    fetch(`/api/users/${userId}/followers`)
      .then(res => res.json())
      .then(setFollowers);

    setLoading(false);
  }, [userId]);

  const handleFollow = () => {
    // Follow logic
  };

  const handleLike = (postId) => {
    // Like logic
  };

  return (
    <div>
      {/* Complex rendering logic */}
      <UserHeader user={user} onFollow={handleFollow} />
      <UserPosts posts={posts} onLike={handleLike} />
      <UserFollowers followers={followers} />
    </div>
  );
}

// ✅ Good: Tách thành các components có trách nhiệm đơn lẻ
function UserProfile({ userId }) {
  return (
    <div>
      <UserProfileHeader userId={userId} />
      <UserProfileContent userId={userId} />
    </div>
  );
}

function UserProfileHeader({ userId }) {
  const { data: user, loading } = useUser(userId);

  if (loading) return <UserHeaderSkeleton />;

  return (
    <div>
      <Avatar src={user.avatar} alt={user.name} />
      <h1>{user.name}</h1>
      <FollowButton userId={userId} />
    </div>
  );
}

function UserProfileContent({ userId }) {
  return (
    <div>
      <UserPosts userId={userId} />
      <UserFollowers userId={userId} />
    </div>
  );
}

// 2. Open/Closed Principle (OCP)
// ✅ Component mở cho extension, đóng cho modification
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  children: React.ReactNode;
  onClick?: () => void;
}

const buttonVariants = {
  primary: 'bg-blue-500 text-white hover:bg-blue-600',
  secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
  danger: 'bg-red-500 text-white hover:bg-red-600',
};

const buttonSizes = {
  small: 'px-2 py-1 text-sm',
  medium: 'px-4 py-2',
  large: 'px-6 py-3 text-lg',
};

function Button({
  variant = 'primary',
  size = 'medium',
  children,
  className = '',
  ...props
}: ButtonProps) {
  const baseClasses = 'rounded font-medium transition-colors';
  const variantClasses = buttonVariants[variant];
  const sizeClasses = buttonSizes[size];

  const classes = `${baseClasses} ${variantClasses} ${sizeClasses} ${className}`;

  return (
    <button className={classes} {...props}>
      {children}
    </button>
  );
}

// Extension through composition
function IconButton({ icon, ...props }: ButtonProps & { icon: React.ReactNode }) {
  return (
    <Button {...props}>
      <span className="mr-2">{icon}</span>
      {props.children}
    </Button>
  );
}

function LoadingButton({
  loading,
  loadingText = 'Loading...',
  ...props
}: ButtonProps & { loading: boolean; loadingText?: string }) {
  return (
    <Button {...props} disabled={loading || props.disabled}>
      {loading ? (
        <>
          <Spinner className="mr-2" />
          {loadingText}
        </>
      ) : (
        props.children
      )}
    </Button>
  );
}

// 3. Liskov Substitution Principle (LSP)
// ✅ Subcomponents có thể thay thế base component
interface InputProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
}

function TextInput({ value, onChange, ...props }: InputProps) {
  return (
    <input
      type="text"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      {...props}
    />
  );
}

function EmailInput({ value, onChange, ...props }: InputProps) {
  const handleChange = (newValue: string) => {
    // Additional email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (emailRegex.test(newValue) || newValue === '') {
      onChange(newValue);
    }
  };

  return (
    <input
      type="email"
      value={value}
      onChange={(e) => handleChange(e.target.value)}
      {...props}
    />
  );
}

function PasswordInput({ value, onChange, ...props }: InputProps) {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <div className="relative">
      <input
        type={showPassword ? 'text' : 'password'}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        {...props}
      />
      <button
        type="button"
        onClick={() => setShowPassword(!showPassword)}
        className="absolute right-2 top-1/2 transform -translate-y-1/2"
      >
        {showPassword ? <EyeOffIcon /> : <EyeIcon />}
      </button>
    </div>
  );
}

// Có thể sử dụng interchangeably
function Form() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');

  return (
    <form>
      <TextInput
        value={name}
        onChange={setName}
        placeholder="Full Name"
      />
      <EmailInput
        value={email}
        onChange={setEmail}
        placeholder="Email"
      />
      <PasswordInput
        value={password}
        onChange={setPassword}
        placeholder="Password"
      />
    </form>
  );
}

// 4. Interface Segregation Principle (ISP)
// ✅ Chia interfaces thành các phần nhỏ, specific
interface UserData {
  id: string;
  name: string;
  email: string;
  avatar: string;
}

interface UserActions {
  onFollow: () => void;
  onMessage: () => void;
  onBlock: () => void;
}

interface UserPreferences {
  theme: 'light' | 'dark';
  notifications: boolean;
  language: string;
}

// Components chỉ nhận props cần thiết
function UserAvatar({ user }: { user: Pick<UserData, 'name' | 'avatar'> }) {
  return (
    <img
      src={user.avatar}
      alt={user.name}
      className="w-10 h-10 rounded-full"
    />
  );
}

function UserActions({ actions }: { actions: UserActions }) {
  return (
    <div>
      <button onClick={actions.onFollow}>Follow</button>
      <button onClick={actions.onMessage}>Message</button>
      <button onClick={actions.onBlock}>Block</button>
    </div>
  );
}

function UserSettings({
  preferences,
  onUpdate
}: {
  preferences: UserPreferences;
  onUpdate: (prefs: Partial<UserPreferences>) => void;
}) {
  return (
    <div>
      <select
        value={preferences.theme}
        onChange={(e) => onUpdate({ theme: e.target.value as 'light' | 'dark' })}
      >
        <option value="light">Light</option>
        <option value="dark">Dark</option>
      </select>
    </div>
  );
}

// 5. Dependency Inversion Principle (DIP)
// ✅ Depend on abstractions, not concretions
interface DataService {
  fetchUser(id: string): Promise<UserData>;
  updateUser(id: string, data: Partial<UserData>): Promise<UserData>;
}

// Concrete implementations
class APIDataService implements DataService {
  async fetchUser(id: string): Promise<UserData> {
    const response = await fetch(`/api/users/${id}`);
    return response.json();
  }

  async updateUser(id: string, data: Partial<UserData>): Promise<UserData> {
    const response = await fetch(`/api/users/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data),
    });
    return response.json();
  }
}

class MockDataService implements DataService {
  private users: Map<string, UserData> = new Map();

  async fetchUser(id: string): Promise<UserData> {
    return this.users.get(id) || {
      id,
      name: 'Mock User',
      email: 'mock@example.com',
      avatar: '/mock-avatar.jpg'
    };
  }

  async updateUser(id: string, data: Partial<UserData>): Promise<UserData> {
    const existing = await this.fetchUser(id);
    const updated = { ...existing, ...data };
    this.users.set(id, updated);
    return updated;
  }
}

// Component depends on abstraction
function useUserService(service: DataService) {
  return {
    fetchUser: service.fetchUser.bind(service),
    updateUser: service.updateUser.bind(service),
  };
}

function UserProfile({ userId, dataService }: {
  userId: string;
  dataService: DataService;
}) {
  const [user, setUser] = useState<UserData | null>(null);
  const { fetchUser, updateUser } = useUserService(dataService);

  useEffect(() => {
    fetchUser(userId).then(setUser);
  }, [userId, fetchUser]);

  const handleUpdate = async (updates: Partial<UserData>) => {
    if (user) {
      const updated = await updateUser(user.id, updates);
      setUser(updated);
    }
  };

  if (!user) return <div>Loading...</div>;

  return (
    <div>
      <h1>{user.name}</h1>
      <p>{user.email}</p>
      <button onClick={() => handleUpdate({ name: 'Updated Name' })}>
        Update Name
      </button>
    </div>
  );
}

// Usage with dependency injection
function App() {
  const dataService = process.env.NODE_ENV === 'test'
    ? new MockDataService()
    : new APIDataService();

  return (
    <UserProfile userId="123" dataService={dataService} />
  );
}
```

#### Q25: Code organization và folder structure cho large React apps?

**Trả lời:**

```typescript
// 1. Feature-based Architecture
/*
src/
├── shared/                    # Shared utilities và components
│   ├── components/           # Reusable UI components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.test.tsx
│   │   │   ├── Button.stories.tsx
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── hooks/               # Custom hooks
│   │   ├── useLocalStorage.ts
│   │   ├── useDebounce.ts
│   │   └── index.ts
│   ├── utils/               # Utility functions
│   │   ├── format.ts
│   │   ├── validation.ts
│   │   └── index.ts
│   └── types/               # TypeScript types
│       ├── api.ts
│       ├── user.ts
│       └── index.ts
├── features/                 # Feature modules
│   ├── authentication/
│   │   ├── components/
│   │   │   ├── LoginForm/
│   │   │   ├── SignupForm/
│   │   │   └── index.ts
│   │   ├── hooks/
│   │   │   ├── useAuth.ts
│   │   │   └── index.ts
│   │   ├── services/
│   │   │   ├── authAPI.ts
│   │   │   └── index.ts
│   │   ├── store/
│   │   │   ├── authSlice.ts
│   │   │   └── index.ts
│   │   ├── types/
│   │   │   ├── auth.ts
│   │   │   └── index.ts
│   │   └── index.ts
│   ├── dashboard/
│   ├── user-management/
│   └── index.ts
├── pages/                   # Page components (routing)
│   ├── LoginPage/
│   ├── DashboardPage/
│   └── index.ts
├── store/                   # Global state management
│   ├── index.ts
│   ├── rootReducer.ts
│   └── middleware.ts
└── App.tsx
*/

// 2. Barrel Exports Pattern
// shared/components/index.ts
export { Button } from './Button';
export { Modal } from './Modal';
export { Input } from './Input';
export type { ButtonProps } from './Button';
export type { ModalProps } from './Modal';

// features/authentication/index.ts
export { LoginForm, SignupForm } from './components';
export { useAuth } from './hooks';
export { authAPI } from './services';
export { authSlice } from './store';
export type { AuthUser, LoginCredentials } from './types';

// 3. Clean Component Structure
// features/user-management/components/UserCard/UserCard.tsx
import React from 'react';
import { User } from '../../types';
import { useUserActions } from '../../hooks';
import { Avatar, Button } from '@/shared/components';
import styles from './UserCard.module.css';

interface UserCardProps {
  user: User;
  onEdit?: (user: User) => void;
  onDelete?: (userId: string) => void;
  className?: string;
}

export function UserCard({
  user,
  onEdit,
  onDelete,
  className = ''
}: UserCardProps) {
  const { deleteUser, isDeleting } = useUserActions();

  const handleEdit = () => {
    onEdit?.(user);
  };

  const handleDelete = async () => {
    if (window.confirm('Are you sure?')) {
      await deleteUser(user.id);
      onDelete?.(user.id);
    }
  };

  return (
    <div className={`${styles.userCard} ${className}`}>
      <div className={styles.header}>
        <Avatar src={user.avatar} alt={user.name} />
        <div className={styles.info}>
          <h3 className={styles.name}>{user.name}</h3>
          <p className={styles.email}>{user.email}</p>
        </div>
      </div>

      <div className={styles.actions}>
        <Button
          variant="secondary"
          size="small"
          onClick={handleEdit}
        >
          Edit
        </Button>
        <Button
          variant="danger"
          size="small"
          onClick={handleDelete}
          loading={isDeleting}
        >
          Delete
        </Button>
      </div>
    </div>
  );
}

// 4. Custom Hooks Organization
// features/user-management/hooks/useUserActions.ts
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { userAPI } from '../services';
import { User } from '../types';

export function useUserActions() {
  const queryClient = useQueryClient();

  const deleteUserMutation = useMutation({
    mutationFn: userAPI.deleteUser,
    onSuccess: (_, userId) => {
      // Optimistic update
      queryClient.setQueryData<User[]>(['users'], (old) =>
        old?.filter(user => user.id !== userId) ?? []
      );

      // Invalidate related queries
      queryClient.invalidateQueries({ queryKey: ['users'] });
      queryClient.invalidateQueries({ queryKey: ['user-stats'] });
    },
    onError: (error) => {
      console.error('Failed to delete user:', error);
      // Show error notification
    },
  });

  const updateUserMutation = useMutation({
    mutationFn: ({ id, data }: { id: string; data: Partial<User> }) =>
      userAPI.updateUser(id, data),
    onSuccess: (updatedUser) => {
      // Update cache
      queryClient.setQueryData<User>(['user', updatedUser.id], updatedUser);
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
  });

  return {
    deleteUser: deleteUserMutation.mutate,
    isDeleting: deleteUserMutation.isPending,
    updateUser: updateUserMutation.mutate,
    isUpdating: updateUserMutation.isPending,
  };
}

// 5. Service Layer Pattern
// features/user-management/services/userAPI.ts
import { apiClient } from '@/shared/services/apiClient';
import { User, CreateUserData, UpdateUserData } from '../types';

export const userAPI = {
  async getUsers(): Promise<User[]> {
    const response = await apiClient.get('/users');
    return response.data;
  },

  async getUser(id: string): Promise<User> {
    const response = await apiClient.get(`/users/${id}`);
    return response.data;
  },

  async createUser(data: CreateUserData): Promise<User> {
    const response = await apiClient.post('/users', data);
    return response.data;
  },

  async updateUser(id: string, data: UpdateUserData): Promise<User> {
    const response = await apiClient.put(`/users/${id}`, data);
    return response.data;
  },

  async deleteUser(id: string): Promise<void> {
    await apiClient.delete(`/users/${id}`);
  },

  async searchUsers(query: string): Promise<User[]> {
    const response = await apiClient.get('/users/search', {
      params: { q: query }
    });
    return response.data;
  },
};

// 6. State Management Organization
// features/user-management/store/userSlice.ts
import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { userAPI } from '../services';
import { User } from '../types';

interface UserState {
  users: User[];
  selectedUser: User | null;
  loading: boolean;
  error: string | null;
  filters: {
    search: string;
    role: string;
    status: string;
  };
}

const initialState: UserState = {
  users: [],
  selectedUser: null,
  loading: false,
  error: null,
  filters: {
    search: '',
    role: '',
    status: '',
  },
};

// Async thunks
export const fetchUsers = createAsyncThunk(
  'users/fetchUsers',
  async (_, { rejectWithValue }) => {
    try {
      return await userAPI.getUsers();
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

export const searchUsers = createAsyncThunk(
  'users/searchUsers',
  async (query: string, { rejectWithValue }) => {
    try {
      return await userAPI.searchUsers(query);
    } catch (error) {
      return rejectWithValue(error.message);
    }
  }
);

const userSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    setSelectedUser: (state, action) => {
      state.selectedUser = action.payload;
    },
    clearSelectedUser: (state) => {
      state.selectedUser = null;
    },
    updateFilters: (state, action) => {
      state.filters = { ...state.filters, ...action.payload };
    },
    clearError: (state) => {
      state.error = null;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.users = action.payload;
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      })
      .addCase(searchUsers.fulfilled, (state, action) => {
        state.users = action.payload;
      });
  },
});

export const {
  setSelectedUser,
  clearSelectedUser,
  updateFilters,
  clearError
} = userSlice.actions;

export default userSlice.reducer;

// Selectors
export const selectUsers = (state: RootState) => state.users.users;
export const selectSelectedUser = (state: RootState) => state.users.selectedUser;
export const selectUsersLoading = (state: RootState) => state.users.loading;
export const selectUsersError = (state: RootState) => state.users.error;
export const selectUserFilters = (state: RootState) => state.users.filters;

// 7. Type Definitions Organization
// features/user-management/types/user.ts
export interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  role: UserRole;
  status: UserStatus;
  createdAt: string;
  updatedAt: string;
}

export type UserRole = 'admin' | 'user' | 'moderator';
export type UserStatus = 'active' | 'inactive' | 'pending';

export interface CreateUserData {
  name: string;
  email: string;
  role: UserRole;
  password: string;
}

export interface UpdateUserData {
  name?: string;
  email?: string;
  role?: UserRole;
  status?: UserStatus;
}

export interface UserFilters {
  search?: string;
  role?: UserRole;
  status?: UserStatus;
  page?: number;
  limit?: number;
}

// features/user-management/types/index.ts
export type {
  User,
  UserRole,
  UserStatus,
  CreateUserData,
  UpdateUserData,
  UserFilters
} from './user';

// 8. Testing Organization
// features/user-management/components/UserCard/UserCard.test.tsx
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { UserCard } from './UserCard';
import { mockUser } from '../../__mocks__/userData';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: { queries: { retry: false } },
  });

  return ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={queryClient}>
      {children}
    </QueryClientProvider>
  );
};

describe('UserCard', () => {
  it('renders user information correctly', () => {
    render(<UserCard user={mockUser} />, { wrapper: createWrapper() });

    expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    expect(screen.getByText(mockUser.email)).toBeInTheDocument();
  });

  it('calls onEdit when edit button is clicked', () => {
    const onEdit = jest.fn();
    render(
      <UserCard user={mockUser} onEdit={onEdit} />,
      { wrapper: createWrapper() }
    );

    fireEvent.click(screen.getByText('Edit'));
    expect(onEdit).toHaveBeenCalledWith(mockUser);
  });

  it('shows confirmation dialog when delete is clicked', async () => {
    const onDelete = jest.fn();
    window.confirm = jest.fn(() => true);

    render(
      <UserCard user={mockUser} onDelete={onDelete} />,
      { wrapper: createWrapper() }
    );

    fireEvent.click(screen.getByText('Delete'));

    expect(window.confirm).toHaveBeenCalled();
  });
});
```

### 11. Advanced React Performance Optimization

#### Q26: Deep dive React performance optimization techniques?

**Trả lời:**

```typescript
// 1. Advanced Memoization Strategies
// ✅ Smart memoization với selective dependencies
function ExpensiveCalculation({ data, filters, config }) {
  // Memoize expensive calculations với selective dependencies
  const processedData = useMemo(() => {
    console.log('Processing data...'); // Should only log when data changes

    return data
      .filter(item => filters.includes(item.category))
      .map(item => ({
        ...item,
        score: calculateComplexScore(item, config.weights),
        trend: calculateTrend(item.history)
      }))
      .sort((a, b) => b.score - a.score);
  }, [data, filters]); // config intentionally excluded for performance

  // Separate memoization cho independent calculations
  const aggregatedStats = useMemo(() => {
    return {
      total: processedData.length,
      averageScore: processedData.reduce((sum, item) => sum + item.score, 0) / processedData.length,
      topPerformers: processedData.slice(0, 10)
    };
  }, [processedData]);

  // Memoize callbacks với stable references
  const handleItemClick = useCallback((itemId) => {
    // Use functional update to avoid dependencies
    setSelectedItems(prev =>
      prev.includes(itemId)
        ? prev.filter(id => id !== itemId)
        : [...prev, itemId]
    );
  }, []); // No dependencies needed

  return (
    <div>
      <StatsDisplay stats={aggregatedStats} />
      <ItemList
        items={processedData}
        onItemClick={handleItemClick}
      />
    </div>
  );
}

// 2. Component Splitting và Virtualization
// ✅ Split heavy components into lighter ones
function HeavyDashboard({ data }) {
  const [activeTab, setActiveTab] = useState('overview');

  return (
    <div>
      <TabNavigation activeTab={activeTab} onTabChange={setActiveTab} />

      {/* Only render active tab content */}
      <Suspense fallback={<TabSkeleton />}>
        {activeTab === 'overview' && <OverviewTab data={data} />}
        {activeTab === 'analytics' && <AnalyticsTab data={data} />}
        {activeTab === 'reports' && <ReportsTab data={data} />}
      </Suspense>
    </div>
  );
}

// Advanced virtualization với dynamic heights
function AdvancedVirtualList({ items, estimatedItemSize = 50 }) {
  const parentRef = useRef();
  const rowVirtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => estimatedItemSize,
    overscan: 5, // Render 5 extra items for smooth scrolling
  });

  return (
    <div
      ref={parentRef}
      style={{
        height: 400,
        overflow: 'auto',
      }}
    >
      <div
        style={{
          height: rowVirtualizer.getTotalSize(),
          width: '100%',
          position: 'relative',
        }}
      >
        {rowVirtualizer.getVirtualItems().map((virtualRow) => {
          const item = items[virtualRow.index];

          return (
            <div
              key={virtualRow.index}
              style={{
                position: 'absolute',
                top: 0,
                left: 0,
                width: '100%',
                height: virtualRow.size,
                transform: `translateY(${virtualRow.start}px)`,
              }}
            >
              <ComplexListItem
                item={item}
                onHeightChange={(height) => {
                  rowVirtualizer.measureElement(virtualRow.index, height);
                }}
              />
            </div>
          );
        })}
      </div>
    </div>
  );
}

// 3. State Management Optimization
// ✅ Optimized state updates với batching
function OptimizedStateManager() {
  const [state, setState] = useState({
    users: [],
    filters: { search: '', category: 'all' },
    pagination: { page: 1, limit: 20 },
    loading: false,
    error: null
  });

  // Batch multiple state updates
  const updateMultipleStates = useCallback((updates) => {
    setState(prevState => ({
      ...prevState,
      ...updates
    }));
  }, []);

  // Optimized search with debouncing
  const debouncedSearch = useMemo(
    () => debounce((searchTerm) => {
      updateMultipleStates({
        filters: { ...state.filters, search: searchTerm },
        pagination: { ...state.pagination, page: 1 },
        loading: true
      });
    }, 300),
    [state.filters, state.pagination, updateMultipleStates]
  );

  // Cleanup debounced function
  useEffect(() => {
    return () => {
      debouncedSearch.cancel();
    };
  }, [debouncedSearch]);

  return {
    state,
    updateMultipleStates,
    debouncedSearch
  };
}

// 4. Render Optimization Patterns
// ✅ Prevent unnecessary re-renders
const OptimizedParent = React.memo(function OptimizedParent({
  data,
  config,
  onAction
}) {
  // Split state to minimize re-renders
  const [uiState, setUiState] = useState({ expanded: false, selected: null });
  const [dataState, setDataState] = useState({ processed: null, loading: false });

  // Stable callback references
  const handleToggle = useCallback(() => {
    setUiState(prev => ({ ...prev, expanded: !prev.expanded }));
  }, []);

  const handleSelection = useCallback((id) => {
    setUiState(prev => ({ ...prev, selected: id }));
  }, []);

  // Memoize expensive operations
  const processedData = useMemo(() => {
    if (!data) return [];

    return data.map(item => ({
      ...item,
      calculated: expensiveCalculation(item, config)
    }));
  }, [data, config]);

  return (
    <div>
      {/* UI-only state doesn't affect data processing */}
      <Header
        expanded={uiState.expanded}
        onToggle={handleToggle}
      />

      {/* Data changes don't affect UI state */}
      <DataDisplay
        data={processedData}
        selected={uiState.selected}
        onSelect={handleSelection}
        onAction={onAction}
      />
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison for complex props
  return (
    prevProps.data.length === nextProps.data.length &&
    prevProps.config.version === nextProps.config.version &&
    prevProps.onAction === nextProps.onAction
  );
});

// 5. Bundle Size Optimization
// ✅ Code splitting với strategic loading
const LazyLoadedComponents = {
  // Critical components - load immediately
  Dashboard: React.lazy(() => import('./Dashboard')),

  // Secondary components - load on demand
  Reports: React.lazy(() =>
    import(/* webpackChunkName: "reports" */ './Reports')
  ),

  // Heavy components - load with preload strategy
  DataVisualization: React.lazy(() =>
    import(/* webpackChunkName: "viz", webpackPreload: true */ './DataVisualization')
  ),
};

// Smart preloading strategy
function usePreloader() {
  const [preloadedComponents, setPreloadedComponents] = useState(new Set());

  const preloadComponent = useCallback((componentName) => {
    if (preloadedComponents.has(componentName)) return;

    // Use requestIdleCallback for non-critical preloading
    requestIdleCallback(() => {
      LazyLoadedComponents[componentName];
      setPreloadedComponents(prev => new Set([...prev, componentName]));
    });
  }, [preloadedComponents]);

  // Preload on hover
  const preloadOnHover = useCallback((componentName) => ({
    onMouseEnter: () => preloadComponent(componentName),
    onFocus: () => preloadComponent(componentName),
  }), [preloadComponent]);

  return { preloadComponent, preloadOnHover };
}

// 6. Memory Management & Cleanup
// ✅ Advanced cleanup patterns
function useResourceCleanup() {
  const subscriptionsRef = useRef(new Set());
  const timeoutsRef = useRef(new Set());
  const intervalsRef = useRef(new Set());

  const addSubscription = useCallback((subscription) => {
    subscriptionsRef.current.add(subscription);
    return () => subscriptionsRef.current.delete(subscription);
  }, []);

  const addTimeout = useCallback((timeoutId) => {
    timeoutsRef.current.add(timeoutId);
    return () => {
      clearTimeout(timeoutId);
      timeoutsRef.current.delete(timeoutId);
    };
  }, []);

  const addInterval = useCallback((intervalId) => {
    intervalsRef.current.add(intervalId);
    return () => {
      clearInterval(intervalId);
      intervalsRef.current.delete(intervalId);
    };
  }, []);

  // Cleanup all resources
  useEffect(() => {
    return () => {
      // Cleanup subscriptions
      subscriptionsRef.current.forEach(subscription => {
        if (typeof subscription.unsubscribe === 'function') {
          subscription.unsubscribe();
        } else if (typeof subscription === 'function') {
          subscription();
        }
      });

      // Cleanup timeouts
      timeoutsRef.current.forEach(clearTimeout);

      // Cleanup intervals
      intervalsRef.current.forEach(clearInterval);

      // Clear all refs
      subscriptionsRef.current.clear();
      timeoutsRef.current.clear();
      intervalsRef.current.clear();
    };
  }, []);

  return { addSubscription, addTimeout, addInterval };
}

// 7. Performance Monitoring Integration
function usePerformanceMonitoring(componentName) {
  const renderCountRef = useRef(0);
  const mountTimeRef = useRef(Date.now());

  useEffect(() => {
    renderCountRef.current++;

    // Track render performance
    const renderTime = Date.now() - mountTimeRef.current;

    if (renderTime > 100) { // Slow render threshold
      console.warn(`Slow render detected in ${componentName}: ${renderTime}ms`);

      // Report to analytics
      if (window.analytics) {
        window.analytics.track('Slow Render', {
          component: componentName,
          renderTime,
          renderCount: renderCountRef.current
        });
      }
    }
  });

  // Track component lifecycle
  useEffect(() => {
    const mountTime = Date.now();

    return () => {
      const unmountTime = Date.now();
      const componentLifetime = unmountTime - mountTime;

      // Report component metrics
      if (window.analytics) {
        window.analytics.track('Component Unmount', {
          component: componentName,
          lifetime: componentLifetime,
          totalRenders: renderCountRef.current
        });
      }
    };
  }, [componentName]);
}

// 8. Network Optimization
function useOptimizedFetching() {
  const [cache, setCache] = useState(new Map());
  const abortControllersRef = useRef(new Map());

  const fetchWithOptimization = useCallback(async (url, options = {}) => {
    // Check cache first
    const cacheKey = `${url}${JSON.stringify(options)}`;
    const cached = cache.get(cacheKey);

    if (cached && Date.now() - cached.timestamp < 5 * 60 * 1000) { // 5 min cache
      return cached.data;
    }

    // Cancel previous request for same URL
    const existingController = abortControllersRef.current.get(url);
    if (existingController) {
      existingController.abort();
    }

    // Create new abort controller
    const controller = new AbortController();
    abortControllersRef.current.set(url, controller);

    try {
      const response = await fetch(url, {
        ...options,
        signal: controller.signal,
      });

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();

      // Update cache
      setCache(prev => new Map(prev.set(cacheKey, {
        data,
        timestamp: Date.now()
      })));

      return data;
    } finally {
      abortControllersRef.current.delete(url);
    }
  }, [cache]);

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      abortControllersRef.current.forEach(controller => controller.abort());
      abortControllersRef.current.clear();
    };
  }, []);

  return { fetchWithOptimization, clearCache: () => setCache(new Map()) };
}

// Usage example combining all optimizations
function HighPerformanceApp() {
  const { preloadOnHover } = usePreloader();
  const { addSubscription, addTimeout } = useResourceCleanup();
  const { fetchWithOptimization } = useOptimizedFetching();

  usePerformanceMonitoring('HighPerformanceApp');

  return (
    <div>
      <nav>
        <button {...preloadOnHover('Reports')}>
          Reports
        </button>
        <button {...preloadOnHover('DataVisualization')}>
          Analytics
        </button>
      </nav>

      <Suspense fallback={<LoadingSkeleton />}>
        <Routes>
          <Route path="/reports" element={<LazyLoadedComponents.Reports />} />
          <Route path="/analytics" element={<LazyLoadedComponents.DataVisualization />} />
        </Routes>
      </Suspense>
    </div>
  );
}
```

#### Q27: Testing strategies cho React applications?

**Trả lời:**

```typescript
// 1. Unit Testing với React Testing Library
// ✅ Component testing với best practices
import { render, screen, fireEvent, waitFor, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { BrowserRouter } from 'react-router-dom';
import { UserProfile } from './UserProfile';
import { mockUser, mockUserPosts } from '../__mocks__/userData';

// Test utilities
const createTestWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false },
    },
  });

  return function TestWrapper({ children }) {
    return (
      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          {children}
        </BrowserRouter>
      </QueryClientProvider>
    );
  };
};

// Mock API calls
jest.mock('../services/userAPI', () => ({
  userAPI: {
    getUser: jest.fn(),
    getUserPosts: jest.fn(),
    followUser: jest.fn(),
  },
}));

describe('UserProfile Component', () => {
  const user = userEvent.setup();
  let mockGetUser, mockGetUserPosts, mockFollowUser;

  beforeEach(() => {
    mockGetUser = require('../services/userAPI').userAPI.getUser;
    mockGetUserPosts = require('../services/userAPI').userAPI.getUserPosts;
    mockFollowUser = require('../services/userAPI').userAPI.followUser;

    // Reset mocks
    jest.clearAllMocks();
  });

  it('renders user information correctly', async () => {
    mockGetUser.mockResolvedValue(mockUser);
    mockGetUserPosts.mockResolvedValue(mockUserPosts);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    // Test loading state
    expect(screen.getByText('Loading...')).toBeInTheDocument();

    // Wait for data to load
    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // Test rendered content
    expect(screen.getByText(mockUser.email)).toBeInTheDocument();
    expect(screen.getByAltText(`${mockUser.name}'s avatar`)).toBeInTheDocument();
    expect(screen.getByText(`${mockUser.followersCount} followers`)).toBeInTheDocument();
  });

  it('handles follow/unfollow functionality', async () => {
    mockGetUser.mockResolvedValue({ ...mockUser, isFollowing: false });
    mockFollowUser.mockResolvedValue({ ...mockUser, isFollowing: true });

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    const followButton = screen.getByRole('button', { name: /follow/i });
    await user.click(followButton);

    expect(mockFollowUser).toHaveBeenCalledWith('123');

    await waitFor(() => {
      expect(screen.getByRole('button', { name: /unfollow/i })).toBeInTheDocument();
    });
  });

  it('displays error state when user fetch fails', async () => {
    const errorMessage = 'User not found';
    mockGetUser.mockRejectedValue(new Error(errorMessage));

    render(<UserProfile userId="invalid" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(/error loading user/i)).toBeInTheDocument();
      expect(screen.getByText(errorMessage)).toBeInTheDocument();
    });
  });

  it('filters posts when search term is entered', async () => {
    mockGetUser.mockResolvedValue(mockUser);
    mockGetUserPosts.mockResolvedValue(mockUserPosts);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // All posts should be visible initially
    expect(screen.getAllByTestId('post-item')).toHaveLength(mockUserPosts.length);

    // Search for specific post
    const searchInput = screen.getByPlaceholderText('Search posts...');
    await user.type(searchInput, 'react');

    // Only posts containing 'react' should be visible
    await waitFor(() => {
      const visiblePosts = screen.getAllByTestId('post-item');
      expect(visiblePosts.length).toBeLessThan(mockUserPosts.length);
    });
  });
});

// 2. Integration Testing
// ✅ Multi-component integration tests
describe('UserProfile Integration', () => {
  it('loads user profile and allows interaction with posts', async () => {
    const user = userEvent.setup();

    // Mock complete user flow
    mockGetUser.mockResolvedValue(mockUser);
    mockGetUserPosts.mockResolvedValue(mockUserPosts);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    // Wait for profile to load
    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // Test posts section
    const postsSection = screen.getByTestId('user-posts');
    expect(postsSection).toBeInTheDocument();

    // Test post interaction
    const firstPost = within(postsSection).getAllByTestId('post-item')[0];
    const likeButton = within(firstPost).getByRole('button', { name: /like/i });

    await user.click(likeButton);

    // Verify like action
    expect(within(firstPost).getByText(/liked/i)).toBeInTheDocument();
  });
});

// 3. Custom Hooks Testing
// ✅ Testing custom hooks in isolation
import { renderHook, act } from '@testing-library/react';
import { useUserActions } from '../hooks/useUserActions';

describe('useUserActions Hook', () => {
  const wrapper = createTestWrapper();

  it('provides user action functions', () => {
    const { result } = renderHook(() => useUserActions(), { wrapper });

    expect(result.current.followUser).toBeInstanceOf(Function);
    expect(result.current.unfollowUser).toBeInstanceOf(Function);
    expect(result.current.isFollowing).toBe(false);
    expect(result.current.isLoading).toBe(false);
  });

  it('handles follow user action', async () => {
    mockFollowUser.mockResolvedValue({ success: true });

    const { result } = renderHook(() => useUserActions(), { wrapper });

    await act(async () => {
      await result.current.followUser('123');
    });

    expect(mockFollowUser).toHaveBeenCalledWith('123');
    expect(result.current.isFollowing).toBe(true);
  });

  it('handles follow error gracefully', async () => {
    const errorMessage = 'Failed to follow user';
    mockFollowUser.mockRejectedValue(new Error(errorMessage));

    const { result } = renderHook(() => useUserActions(), { wrapper });

    await act(async () => {
      try {
        await result.current.followUser('123');
      } catch (error) {
        expect(error.message).toBe(errorMessage);
      }
    });

    expect(result.current.isFollowing).toBe(false);
    expect(result.current.error).toBe(errorMessage);
  });
});

// 4. E2E Testing với Cypress
// ✅ End-to-end user flows
// cypress/integration/user-profile.spec.js
describe('User Profile E2E', () => {
  beforeEach(() => {
    // Mock API responses
    cy.intercept('GET', '/api/users/123', { fixture: 'user.json' }).as('getUser');
    cy.intercept('GET', '/api/users/123/posts', { fixture: 'userPosts.json' }).as('getPosts');
    cy.intercept('POST', '/api/users/123/follow', { success: true }).as('followUser');

    cy.visit('/users/123');
  });

  it('displays user profile and allows following', () => {
    // Wait for data to load
    cy.wait(['@getUser', '@getPosts']);

    // Verify profile information
    cy.get('[data-testid="user-name"]').should('contain', 'John Doe');
    cy.get('[data-testid="user-email"]').should('contain', 'john@example.com');
    cy.get('[data-testid="followers-count"]').should('contain', '1,234 followers');

    // Test follow functionality
    cy.get('[data-testid="follow-button"]').click();
    cy.wait('@followUser');

    cy.get('[data-testid="follow-button"]')
      .should('contain', 'Unfollow')
      .and('have.class', 'following');

    // Verify follower count updated
    cy.get('[data-testid="followers-count"]').should('contain', '1,235 followers');
  });

  it('filters posts by search term', () => {
    cy.wait(['@getUser', '@getPosts']);

    // Count total posts
    cy.get('[data-testid="post-item"]').should('have.length.greaterThan', 0);
    cy.get('[data-testid="post-item"]').its('length').as('totalPosts');

    // Search for specific posts
    cy.get('[data-testid="search-posts"]').type('react');

    // Verify filtered results
    cy.get('[data-testid="post-item"]').should('have.length.lessThan', '@totalPosts');
    cy.get('[data-testid="post-item"]').each(($post) => {
      cy.wrap($post).should('contain.text', 'react');
    });
  });

  it('handles navigation between user sections', () => {
    cy.wait(['@getUser', '@getPosts']);

    // Test tab navigation
    cy.get('[data-testid="posts-tab"]').should('have.class', 'active');

    cy.get('[data-testid="followers-tab"]').click();
    cy.get('[data-testid="followers-tab"]').should('have.class', 'active');
    cy.get('[data-testid="followers-list"]').should('be.visible');

    cy.get('[data-testid="following-tab"]').click();
    cy.get('[data-testid="following-tab"]').should('have.class', 'active');
    cy.get('[data-testid="following-list"]').should('be.visible');
  });
});

// 5. Performance Testing
// ✅ Performance regression testing
describe('Performance Tests', () => {
  it('renders large user list efficiently', async () => {
    const largeUserList = Array.from({ length: 1000 }, (_, i) => ({
      id: i,
      name: `User ${i}`,
      email: `user${i}@example.com`,
    }));

    const startTime = performance.now();

    render(<UserList users={largeUserList} />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByTestId('user-list')).toBeInTheDocument();
    });

    const renderTime = performance.now() - startTime;

    // Assert render time is under threshold
    expect(renderTime).toBeLessThan(100); // 100ms threshold
  });

  it('handles rapid state updates without performance degradation', async () => {
    const user = userEvent.setup();

    render(<SearchableUserList />, { wrapper: createTestWrapper() });

    const searchInput = screen.getByPlaceholderText('Search users...');

    const startTime = performance.now();

    // Simulate rapid typing
    await user.type(searchInput, 'john doe test search');

    const typingTime = performance.now() - startTime;

    // Verify responsive typing
    expect(typingTime).toBeLessThan(500); // 500ms for full typing sequence

    // Verify final results
    await waitFor(() => {
      expect(screen.getByDisplayValue('john doe test search')).toBeInTheDocument();
    });
  });
});

// 6. Accessibility Testing
// ✅ A11y testing with jest-axe
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

describe('Accessibility Tests', () => {
  it('has no accessibility violations', async () => {
    mockGetUser.mockResolvedValue(mockUser);

    const { container } = render(
      <UserProfile userId="123" />,
      { wrapper: createTestWrapper() }
    );

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });

  it('supports keyboard navigation', async () => {
    mockGetUser.mockResolvedValue(mockUser);

    render(<UserProfile userId="123" />, { wrapper: createTestWrapper() });

    await waitFor(() => {
      expect(screen.getByText(mockUser.name)).toBeInTheDocument();
    });

    // Test tab navigation
    const followButton = screen.getByRole('button', { name: /follow/i });

    followButton.focus();
    expect(followButton).toHaveFocus();

    // Test Enter key activation
    fireEvent.keyDown(followButton, { key: 'Enter', code: 'Enter' });
    expect(mockFollowUser).toHaveBeenCalled();
  });
});

// 7. Visual Regression Testing
// ✅ Screenshot testing với Storybook
// UserProfile.stories.js
export default {
  title: 'Components/UserProfile',
  component: UserProfile,
  parameters: {
    docs: {
      description: {
        component: 'User profile component with follow functionality'
      }
    }
  }
};

export const Default = {
  args: {
    userId: '123'
  },
  parameters: {
    mockData: [
      {
        url: '/api/users/123',
        method: 'GET',
        status: 200,
        response: mockUser
      }
    ]
  }
};

export const LoadingState = {
  args: {
    userId: '123'
  },
  parameters: {
    mockData: [
      {
        url: '/api/users/123',
        method: 'GET',
        status: 200,
        response: mockUser,
        delay: 2000 // Simulate slow loading
      }
    ]
  }
};

export const ErrorState = {
  args: {
    userId: 'invalid'
  },
  parameters: {
    mockData: [
      {
        url: '/api/users/invalid',
        method: 'GET',
        status: 404,
        response: { error: 'User not found' }
      }
    ]
  }
};

// Chromatic configuration for visual testing
// .storybook/main.js
module.exports = {
  addons: ['@storybook/addon-essentials'],
  features: {
    buildStoriesJson: true
  }
};
```

#### Q28: Accessibility (A11y) best practices trong React?

**Trả lời:**

```typescript
// 1. Semantic HTML và ARIA Attributes
// ✅ Proper semantic structure
function AccessibleForm() {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: '',
    agreeToTerms: false
  });
  const [errors, setErrors] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validateForm = () => {
    const newErrors = {};

    if (!formData.email) {
      newErrors.email = 'Email is required';
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) {
      newErrors.email = 'Please enter a valid email address';
    }

    if (!formData.password) {
      newErrors.password = 'Password is required';
    } else if (formData.password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }

    if (formData.password !== formData.confirmPassword) {
      newErrors.confirmPassword = 'Passwords do not match';
    }

    if (!formData.agreeToTerms) {
      newErrors.agreeToTerms = 'You must agree to the terms';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!validateForm()) {
      // Focus first error field
      const firstErrorField = Object.keys(errors)[0];
      document.getElementById(firstErrorField)?.focus();
      return;
    }

    setIsSubmitting(true);
    try {
      await submitForm(formData);
    } catch (error) {
      setErrors({ submit: 'Submission failed. Please try again.' });
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} noValidate>
      {/* Form heading */}
      <h1 id="form-title">Create Account</h1>

      {/* Form description */}
      <p id="form-description">
        Fill out the form below to create your new account.
      </p>

      {/* Global form error */}
      {errors.submit && (
        <div
          role="alert"
          aria-live="polite"
          className="error-message global-error"
        >
          {errors.submit}
        </div>
      )}

      {/* Email field */}
      <div className="form-group">
        <label htmlFor="email" className="required">
          Email Address
        </label>
        <input
          id="email"
          type="email"
          value={formData.email}
          onChange={(e) => setFormData(prev => ({
            ...prev,
            email: e.target.value
          }))}
          aria-invalid={errors.email ? 'true' : 'false'}
          aria-describedby={errors.email ? 'email-error' : 'email-help'}
          aria-required="true"
          autoComplete="email"
        />
        <div id="email-help" className="help-text">
          We'll never share your email with anyone else.
        </div>
        {errors.email && (
          <div
            id="email-error"
            role="alert"
            className="error-message"
            aria-live="polite"
          >
            {errors.email}
          </div>
        )}
      </div>

      {/* Password field with strength indicator */}
      <div className="form-group">
        <label htmlFor="password" className="required">
          Password
        </label>
        <div className="password-container">
          <input
            id="password"
            type="password"
            value={formData.password}
            onChange={(e) => setFormData(prev => ({
              ...prev,
              password: e.target.value
            }))}
            aria-invalid={errors.password ? 'true' : 'false'}
            aria-describedby="password-requirements password-strength"
            aria-required="true"
            autoComplete="new-password"
          />
          <PasswordStrengthIndicator password={formData.password} />
        </div>

        <div id="password-requirements" className="help-text">
          Password must be at least 8 characters long.
        </div>

        {errors.password && (
          <div
            id="password-error"
            role="alert"
            className="error-message"
          >
            {errors.password}
          </div>
        )}
      </div>

      {/* Confirm password */}
      <div className="form-group">
        <label htmlFor="confirmPassword" className="required">
          Confirm Password
        </label>
        <input
          id="confirmPassword"
          type="password"
          value={formData.confirmPassword}
          onChange={(e) => setFormData(prev => ({
            ...prev,
            confirmPassword: e.target.value
          }))}
          aria-invalid={errors.confirmPassword ? 'true' : 'false'}
          aria-describedby={errors.confirmPassword ? 'confirm-password-error' : undefined}
          aria-required="true"
          autoComplete="new-password"
        />
        {errors.confirmPassword && (
          <div
            id="confirm-password-error"
            role="alert"
            className="error-message"
          >
            {errors.confirmPassword}
          </div>
        )}
      </div>

      {/* Checkbox with proper ARIA */}
      <div className="form-group">
        <label className="checkbox-label">
          <input
            id="agreeToTerms"
            type="checkbox"
            checked={formData.agreeToTerms}
            onChange={(e) => setFormData(prev => ({
              ...prev,
              agreeToTerms: e.target.checked
            }))}
            aria-invalid={errors.agreeToTerms ? 'true' : 'false'}
            aria-describedby={errors.agreeToTerms ? 'terms-error' : undefined}
            aria-required="true"
          />
          <span className="checkmark" aria-hidden="true"></span>
          I agree to the{' '}
          <a href="/terms" target="_blank" rel="noopener noreferrer">
            Terms of Service
            <span className="sr-only"> (opens in new tab)</span>
          </a>
        </label>
        {errors.agreeToTerms && (
          <div
            id="terms-error"
            role="alert"
            className="error-message"
          >
            {errors.agreeToTerms}
          </div>
        )}
      </div>

      {/* Submit button */}
      <button
        type="submit"
        disabled={isSubmitting}
        aria-describedby="submit-status"
      >
        {isSubmitting ? 'Creating Account...' : 'Create Account'}
      </button>

      {/* Screen reader status */}
      <div
        id="submit-status"
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      >
        {isSubmitting ? 'Form is being submitted' : ''}
      </div>
    </form>
  );
}

// 2. Advanced ARIA Patterns
// ✅ Accessible Modal Dialog
function AccessibleModal({
  isOpen,
  onClose,
  title,
  children,
  initialFocus
}) {
  const modalRef = useRef(null);
  const previousFocusRef = useRef(null);

  // Focus management
  useEffect(() => {
    if (isOpen) {
      // Store previously focused element
      previousFocusRef.current = document.activeElement;

      // Focus modal or initial focus element
      setTimeout(() => {
        if (initialFocus) {
          initialFocus.current?.focus();
        } else {
          modalRef.current?.focus();
        }
      }, 0);

      // Trap focus within modal
      const handleTabKey = (e) => {
        if (e.key !== 'Tab') return;

        const focusableElements = modalRef.current?.querySelectorAll(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );

        const firstElement = focusableElements?.[0];
        const lastElement = focusableElements?.[focusableElements.length - 1];

        if (e.shiftKey) {
          if (document.activeElement === firstElement) {
            e.preventDefault();
            lastElement?.focus();
          }
        } else {
          if (document.activeElement === lastElement) {
            e.preventDefault();
            firstElement?.focus();
          }
        }
      };

      document.addEventListener('keydown', handleTabKey);
      return () => document.removeEventListener('keydown', handleTabKey);
    } else {
      // Return focus to previously focused element
      previousFocusRef.current?.focus();
    }
  }, [isOpen, initialFocus]);

  // Escape key handler
  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };

    document.addEventListener('keydown', handleEscape);
    return () => document.removeEventListener('keydown', handleEscape);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  return (
    <>
      {/* Backdrop */}
      <div
        className="modal-backdrop"
        onClick={onClose}
        aria-hidden="true"
      />

      {/* Modal */}
      <div
        ref={modalRef}
        role="dialog"
        aria-modal="true"
        aria-labelledby="modal-title"
        aria-describedby="modal-description"
        className="modal"
        tabIndex={-1}
      >
        <div className="modal-content">
          {/* Header */}
          <div className="modal-header">
            <h2 id="modal-title">{title}</h2>
            <button
              onClick={onClose}
              aria-label="Close dialog"
              className="modal-close"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>

          {/* Body */}
          <div id="modal-description" className="modal-body">
            {children}
          </div>
        </div>
      </div>
    </>
  );
}

// 3. Accessible Data Tables
// ✅ Complex data table with sorting and filtering
function AccessibleDataTable({ data, columns, caption }) {
  const [sortConfig, setSortConfig] = useState({ key: null, direction: 'asc' });
  const [filter, setFilter] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const [announceSort, setAnnounceSort] = useState('');

  const filteredData = useMemo(() => {
    return data.filter(item =>
      Object.values(item).some(value =>
        value.toString().toLowerCase().includes(filter.toLowerCase())
      )
    );
  }, [data, filter]);

  const sortedData = useMemo(() => {
    if (!sortConfig.key) return filteredData;

    return [...filteredData].sort((a, b) => {
      const aVal = a[sortConfig.key];
      const bVal = b[sortConfig.key];

      if (aVal < bVal) return sortConfig.direction === 'asc' ? -1 : 1;
      if (aVal > bVal) return sortConfig.direction === 'asc' ? 1 : -1;
      return 0;
    });
  }, [filteredData, sortConfig]);

  const handleSort = (key) => {
    const direction =
      sortConfig.key === key && sortConfig.direction === 'asc'
        ? 'desc'
        : 'asc';

    setSortConfig({ key, direction });

    // Announce sort change to screen readers
    const column = columns.find(col => col.key === key);
    setAnnounceSort(
      `Table sorted by ${column.label} in ${direction}ending order`
    );
  };

  return (
    <div className="table-container">
      {/* Table controls */}
      <div className="table-controls">
        <label htmlFor="table-search">
          Search table:
        </label>
        <input
          id="table-search"
          type="search"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          aria-describedby="search-help"
        />
        <div id="search-help" className="help-text">
          Search across all table columns
        </div>
      </div>

      {/* Live region for announcements */}
      <div
        aria-live="polite"
        aria-atomic="true"
        className="sr-only"
      >
        {announceSort}
      </div>

      {/* Table */}
      <table
        role="table"
        aria-label={caption}
        aria-rowcount={sortedData.length + 1} // +1 for header
      >
        <caption>{caption}</caption>

        <thead>
          <tr role="row" aria-rowindex={1}>
            {columns.map((column, index) => (
              <th
                key={column.key}
                role="columnheader"
                aria-colindex={index + 1}
                aria-sort={
                  sortConfig.key === column.key
                    ? sortConfig.direction === 'asc' ? 'ascending' : 'descending'
                    : 'none'
                }
                tabIndex={0}
                onClick={() => handleSort(column.key)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    handleSort(column.key);
                  }
                }}
                className={`sortable ${sortConfig.key === column.key ? 'sorted' : ''}`}
              >
                {column.label}
                <span className="sort-indicator" aria-hidden="true">
                  {sortConfig.key === column.key
                    ? (sortConfig.direction === 'asc' ? ' ↑' : ' ↓')
                    : ' ↕'
                  }
                </span>
              </th>
            ))}
          </tr>
        </thead>

        <tbody>
          {sortedData.map((row, rowIndex) => (
            <tr
              key={row.id}
              role="row"
              aria-rowindex={rowIndex + 2}
            >
              {columns.map((column, colIndex) => (
                <td
                  key={column.key}
                  role="gridcell"
                  aria-colindex={colIndex + 1}
                >
                  {column.render ? column.render(row[column.key], row) : row[column.key]}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      {/* Table summary for screen readers */}
      <div className="sr-only">
        Showing {sortedData.length} of {data.length} rows
        {filter && ` filtered by "${filter}"`}
        {sortConfig.key && ` sorted by ${columns.find(c => c.key === sortConfig.key)?.label}`}
      </div>
    </div>
  );
}

// 4. Accessible Navigation
// ✅ Skip links and navigation landmarks
function AccessibleLayout({ children }) {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const menuButtonRef = useRef(null);

  return (
    <>
      {/* Skip links */}
      <div className="skip-links">
        <a href="#main-content" className="skip-link">
          Skip to main content
        </a>
        <a href="#main-navigation" className="skip-link">
          Skip to navigation
        </a>
        <a href="#footer" className="skip-link">
          Skip to footer
        </a>
      </div>

      {/* Header */}
      <header role="banner">
        <div className="header-content">
          <div className="logo">
            <a href="/" aria-label="Company name - Home">
              <img src="/logo.png" alt="Company Logo" />
            </a>
          </div>

          {/* Mobile menu button */}
          <button
            ref={menuButtonRef}
            className="menu-toggle"
            aria-expanded={isMenuOpen}
            aria-controls="main-navigation"
            aria-label="Toggle navigation menu"
            onClick={() => setIsMenuOpen(!isMenuOpen)}
          >
            <span className="hamburger" aria-hidden="true">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </button>

          {/* Navigation */}
          <nav
            id="main-navigation"
            role="navigation"
            aria-label="Main navigation"
            className={isMenuOpen ? 'open' : ''}
          >
            <ul className="nav-list">
              <li>
                <a href="/products" aria-current="page">
                  Products
                </a>
              </li>
              <li>
                <a href="/services">Services</a>
              </li>
              <li>
                <a href="/about">About</a>
              </li>
              <li>
                <a href="/contact">Contact</a>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      {/* Main content */}
      <main id="main-content" role="main">
        {children}
      </main>

      {/* Footer */}
      <footer id="footer" role="contentinfo">
        <div className="footer-content">
          <nav aria-label="Footer navigation">
            <ul>
              <li><a href="/privacy">Privacy Policy</a></li>
              <li><a href="/terms">Terms of Service</a></li>
              <li><a href="/accessibility">Accessibility</a></li>
            </ul>
          </nav>
          <p>&copy; 2024 Company Name. All rights reserved.</p>
        </div>
      </footer>
    </>
  );
}

// 5. Accessible Form Controls
// ✅ Custom accessible components
function AccessibleSelect({
  label,
  options,
  value,
  onChange,
  error,
  required = false,
  ...props
}) {
  const [isOpen, setIsOpen] = useState(false);
  const [focusedIndex, setFocusedIndex] = useState(-1);
  const selectRef = useRef(null);
  const optionsRef = useRef([]);

  const selectedOption = options.find(opt => opt.value === value);

  const handleKeyDown = (e) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
        } else {
          setFocusedIndex(prev =>
            prev < options.length - 1 ? prev + 1 : 0
          );
        }
        break;

      case 'ArrowUp':
        e.preventDefault();
        if (isOpen) {
          setFocusedIndex(prev =>
            prev > 0 ? prev - 1 : options.length - 1
          );
        }
        break;

      case 'Enter':
      case ' ':
        e.preventDefault();
        if (!isOpen) {
          setIsOpen(true);
        } else if (focusedIndex >= 0) {
          onChange(options[focusedIndex].value);
          setIsOpen(false);
        }
        break;

      case 'Escape':
        setIsOpen(false);
        selectRef.current?.focus();
        break;

      case 'Tab':
        setIsOpen(false);
        break;
    }
  };

  return (
    <div className="select-container">
      <label htmlFor={props.id} className={required ? 'required' : ''}>
        {label}
      </label>

      <div className="custom-select">
        <button
          ref={selectRef}
          id={props.id}
          type="button"
          className="select-trigger"
          aria-expanded={isOpen}
          aria-haspopup="listbox"
          aria-labelledby={`${props.id}-label`}
          aria-invalid={error ? 'true' : 'false'}
          aria-describedby={error ? `${props.id}-error` : undefined}
          onClick={() => setIsOpen(!isOpen)}
          onKeyDown={handleKeyDown}
        >
          {selectedOption ? selectedOption.label : 'Select an option'}
          <span className="select-arrow" aria-hidden="true">▼</span>
        </button>

        {isOpen && (
          <ul
            role="listbox"
            aria-labelledby={`${props.id}-label`}
            className="select-options"
          >
            {options.map((option, index) => (
              <li
                key={option.value}
                ref={el => optionsRef.current[index] = el}
                role="option"
                aria-selected={value === option.value}
                className={`select-option ${
                  index === focusedIndex ? 'focused' : ''
                } ${value === option.value ? 'selected' : ''}`}
                onClick={() => {
                  onChange(option.value);
                  setIsOpen(false);
                }}
                onMouseEnter={() => setFocusedIndex(index)}
              >
                {option.label}
              </li>
            ))}
          </ul>
        )}
      </div>

      {error && (
        <div
          id={`${props.id}-error`}
          role="alert"
          className="error-message"
        >
          {error}
        </div>
      )}
    </div>
  );
}

// 6. Screen Reader Utilities
// ✅ Screen reader only content and live regions
function useAnnouncements() {
  const [announcement, setAnnouncement] = useState('');

  const announce = useCallback((message, priority = 'polite') => {
    setAnnouncement(''); // Clear first to ensure announcement
    setTimeout(() => {
      setAnnouncement(message);
    }, 10);
  }, []);

  const LiveRegion = useMemo(() =>
    function LiveRegion({ priority = 'polite' }) {
      return (
        <div
          aria-live={priority}
          aria-atomic="true"
          className="sr-only"
        >
          {announcement}
        </div>
      );
    }, [announcement]
  );

  return { announce, LiveRegion };
}

// Usage example
function NotificationSystem() {
  const { announce, LiveRegion } = useAnnouncements();
  const [notifications, setNotifications] = useState([]);

  const addNotification = (message, type = 'info') => {
    const id = Date.now();
    const notification = { id, message, type };

    setNotifications(prev => [...prev, notification]);

    // Announce to screen readers
    announce(`${type} notification: ${message}`);

    // Auto-remove after 5 seconds
    setTimeout(() => {
      removeNotification(id);
    }, 5000);
  };

  const removeNotification = (id) => {
    setNotifications(prev => prev.filter(n => n.id !== id));
    announce('Notification dismissed');
  };

  return (
    <div>
      {/* Notifications container */}
      <div
        className="notifications"
        role="region"
        aria-label="Notifications"
        aria-live="polite"
      >
        {notifications.map(notification => (
          <div
            key={notification.id}
            className={`notification ${notification.type}`}
            role="alert"
          >
            <span>{notification.message}</span>
            <button
              onClick={() => removeNotification(notification.id)}
              aria-label={`Dismiss ${notification.type} notification`}
            >
              ×
            </button>
          </div>
        ))}
      </div>

      {/* Live region for announcements */}
      <LiveRegion priority="polite" />

      {/* Test buttons */}
      <div>
        <button onClick={() => addNotification('Success message', 'success')}>
          Show Success
        </button>
        <button onClick={() => addNotification('Error message', 'error')}>
          Show Error
        </button>
      </div>
    </div>
  );
}

// 7. CSS Classes for Screen Readers
/*
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.skip-link {
  position: absolute;
  top: -40px;
  left: 6px;
  background: #000;
  color: #fff;
  padding: 8px;
  text-decoration: none;
  z-index: 1000;
}

.skip-link:focus {
  top: 6px;
}
*/
```

---

## 💙 TypeScript Advanced Topics

**📌 [⬆️ Back to Top](#📚-câu-hỏi-frontend-interview---từ-cơ-bản-đến-senior) | [📋 Mục Lục](#📋-mục-lục-tổng-kết)**

### TS1: Utility Types trong TypeScript - Cách sử dụng và ứng dụng?

**Trả lời:**

Utility Types là những **BUILT-IN type helpers** mạnh mẽ trong TypeScript để transform existing types.

#### **🔥 Top Utility Types PHẢI BIẾT:**

**1. `Partial<T>` - Làm tất cả properties OPTIONAL:**
```typescript
interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

// ✅ Partial<User> = tất cả fields đều optional
type PartialUser = Partial<User>;
// = { id?: number; name?: string; email?: string; age?: number; }

// 🎯 USE CASE: Update functions
function updateUser(id: number, updates: Partial<User>): User {
  // Chỉ cần pass những fields muốn update
  return { ...existingUser, ...updates };
}

updateUser(1, { name: "New Name" }); // ✅ Chỉ update name
updateUser(1, { age: 25, email: "new@email.com" }); // ✅ Update nhiều fields
```

**2. `Required<T>` - Làm tất cả properties REQUIRED:**
```typescript
interface Config {
  host?: string;
  port?: number;
  ssl?: boolean;
}

// ✅ Required<Config> = tất cả fields đều required
type RequiredConfig = Required<Config>;
// = { host: string; port: number; ssl: boolean; }

// 🎯 USE CASE: Validation functions
function validateConfig(config: Required<Config>): boolean {
  // Guarantee tất cả fields đều có value
  return config.host.length > 0 && config.port > 0;
}
```

**3. `Pick<T, K>` - Chọn SPECIFIC properties:**
```typescript
interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  category: string;
  inStock: boolean;
}

// ✅ Pick chỉ những fields cần thiết
type ProductSummary = Pick<Product, 'id' | 'name' | 'price'>;
// = { id: number; name: string; price: number; }

// 🎯 USE CASE: API responses với limited data
function getProductSummaries(): ProductSummary[] {
  return products.map(p => ({ id: p.id, name: p.name, price: p.price }));
}
```

**4. `Omit<T, K>` - Loại bỏ SPECIFIC properties:**
```typescript
// ✅ Omit để remove fields không cần
type CreateProduct = Omit<Product, 'id' | 'inStock'>;
// = { name: string; price: number; description: string; category: string; }

// 🎯 USE CASE: Create functions (auto-generate id)
function createProduct(data: CreateProduct): Product {
  return {
    id: generateId(), // Auto-generate
    inStock: true,    // Default value
    ...data
  };
}
```

**5. `Record<K, T>` - Tạo object type với specific keys:**
```typescript
// ✅ Record cho mapping objects
type UserRoles = Record<string, string[]>;
// = { [key: string]: string[] }

type StatusColors = Record<'success' | 'error' | 'warning', string>;
// = { success: string; error: string; warning: string; }

const statusColors: StatusColors = {
  success: '#00ff00',
  error: '#ff0000',
  warning: '#ffaa00'
};

// 🎯 USE CASE: Configuration objects
type ApiEndpoints = Record<'users' | 'products' | 'orders', string>;
const endpoints: ApiEndpoints = {
  users: '/api/users',
  products: '/api/products',
  orders: '/api/orders'
};
```

#### **🚀 Advanced Utility Types:**

**6. `ReturnType<T>` - Lấy return type của function:**
```typescript
function getUserData(id: number) {
  return {
    id,
    name: 'John',
    email: 'john@example.com',
    lastLogin: new Date()
  };
}

// ✅ Tự động infer return type
type UserData = ReturnType<typeof getUserData>;
// = { id: number; name: string; email: string; lastLogin: Date; }

// 🎯 USE CASE: Type safety cho API responses
async function fetchUser(id: number): Promise<UserData> {
  const response = await api.get(`/users/${id}`);
  return response.data; // TypeScript sẽ check type match
}
```

**7. `Parameters<T>` - Lấy parameters type của function:**
```typescript
function createUser(name: string, email: string, age: number) {
  return { name, email, age };
}

// ✅ Extract parameter types
type CreateUserParams = Parameters<typeof createUser>;
// = [name: string, email: string, age: number]

// 🎯 USE CASE: Wrapper functions
function logAndCreateUser(...args: CreateUserParams) {
  console.log('Creating user with:', args);
  return createUser(...args);
}
```

#### **💡 PRACTICAL COMBINATIONS:**

```typescript
// 🔥 Combining multiple utilities
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

// Combine Pick + Partial cho flexible updates
type UpdateableUser = Partial<Pick<User, 'name' | 'email' | 'age'>>;

// Combine Omit + Required cho create operations
type CreateUserData = Required<Omit<User, 'id'>>;

// 🎯 REAL-WORLD EXAMPLE: Form handling
interface UserForm {
  name: string;
  email: string;
  password: string;
  confirmPassword: string;
}

// Remove confirmPassword khi submit
type UserSubmitData = Omit<UserForm, 'confirmPassword'>;

// Optional fields cho edit form
type UserEditForm = Partial<Pick<UserForm, 'name' | 'email'>> &
                   Required<Pick<UserForm, 'password'>>;
```

#### **🎯 KHI NÀO SỬ DỤNG UTILITY TYPES:**

```
✅ Partial<T>: Update operations, optional configurations
✅ Required<T>: Validation, ensuring complete data
✅ Pick<T, K>: API responses, component props subset
✅ Omit<T, K>: Create operations, removing sensitive data
✅ Record<K, T>: Configuration objects, mappings
✅ ReturnType<T>: Type inference, API response types
✅ Parameters<T>: Wrapper functions, middleware
```

**💡 GHI NHỚ:** Utility Types = **Type transformation tools** để reuse và modify existing types một cách type-safe! 🔥

---

### TS2: `as const` vs `enum` - Khi nào sử dụng cái nào?

**Trả lời:**

Đây là một **DESIGN CHOICE quan trọng** trong TypeScript. Cả hai đều tạo **CONSTANT VALUES** nhưng có trade-offs khác nhau.

#### **🔥 `as const` - Literal Type Assertion:**

**Cách hoạt động:**
```typescript
// ✅ as const tạo READONLY literal types
const STATUS = {
  PENDING: 'pending',
  APPROVED: 'approved',
  REJECTED: 'rejected'
} as const;

// TypeScript infer type:
// type STATUS = {
//   readonly PENDING: "pending";
//   readonly APPROVED: "approved";
//   readonly REJECTED: "rejected";
// }

// 🎯 Truy cập values
type StatusType = typeof STATUS[keyof typeof STATUS];
// = "pending" | "approved" | "rejected"
```

**💡 Advantages của `as const`:**
```typescript
// ✅ 1. ZERO JavaScript runtime overhead
const COLORS = ['red', 'green', 'blue'] as const;
// Compiled JS: const COLORS = ['red', 'green', 'blue'];

// ✅ 2. Perfect type inference
const CONFIG = {
  API_URL: 'https://api.example.com',
  TIMEOUT: 5000,
  RETRIES: 3
} as const;

type ConfigKey = keyof typeof CONFIG; // "API_URL" | "TIMEOUT" | "RETRIES"
type ConfigValue = typeof CONFIG[ConfigKey]; // string | number

// ✅ 3. Flexible với complex structures
const ROUTES = {
  home: '/',
  users: {
    list: '/users',
    detail: (id: number) => `/users/${id}`,
    create: '/users/new'
  },
  admin: '/admin'
} as const;

// TypeScript hiểu structure hoàn toàn!
```

#### **🔥 `enum` - Enumerated Types:**

**Numeric Enums:**
```typescript
// ✅ Auto-incrementing numbers
enum UserRole {
  GUEST,     // = 0
  USER,      // = 1
  ADMIN,     // = 2
  SUPER_ADMIN // = 3
}

// ✅ Custom values
enum HttpStatus {
  OK = 200,
  NOT_FOUND = 404,
  SERVER_ERROR = 500
}

console.log(UserRole.ADMIN); // 2
console.log(UserRole[2]);    // "ADMIN" (reverse mapping!)
```

**String Enums:**
```typescript
// ✅ String enums cho better debugging
enum Theme {
  LIGHT = 'light',
  DARK = 'dark',
  AUTO = 'auto'
}

// 🎯 Sử dụng trong code
function setTheme(theme: Theme) {
  document.body.className = theme; // "light", "dark", hoặc "auto"
}

setTheme(Theme.DARK); // ✅ Type safe
// setTheme('dark'); // ❌ Error nếu không cast
```

**💡 Advantages của `enum`:**
```typescript
// ✅ 1. Reverse mapping (chỉ numeric enums)
enum Status { PENDING, APPROVED, REJECTED }
console.log(Status[0]); // "PENDING"
console.log(Status.PENDING); // 0

// ✅ 2. Better IDE support và autocomplete
enum ApiEndpoints {
  USERS = '/api/users',
  PRODUCTS = '/api/products'
}
// IDE sẽ suggest ApiEndpoints.USERS

// ✅ 3. Clear intent - đây là ENUM type
function handleStatus(status: Status) {
  // Clear rằng parameter này là enum
}
```

#### **⚖️ SO SÁNH CHI TIẾT:**

| Feature | `as const` | `enum` |
|---------|------------|--------|
| **Runtime JS** | ✅ **No overhead** | ❌ **Generates JS object** |
| **Type Safety** | ✅ **Full type safety** | ✅ **Full type safety** |
| **Reverse Mapping** | ❌ **Manual** | ✅ **Auto (numeric)** |
| **Tree Shaking** | ✅ **Perfect** | ❌ **Difficult** |
| **Flexibility** | ✅ **Any structure** | ❌ **Simple key-value** |
| **Bundle Size** | ✅ **Smaller** | ❌ **Larger** |

#### **🎯 KHI NÀO SỬ DỤNG:**

**✅ Sử dụng `as const` khi:**
```typescript
// 1. Performance critical (zero runtime cost)
const EVENT_TYPES = ['click', 'hover', 'focus'] as const;

// 2. Complex nested structures
const API_CONFIG = {
  endpoints: {
    users: '/users',
    posts: '/posts'
  },
  timeout: 5000,
  retries: 3
} as const;

// 3. Bundle size matters
const THEME_COLORS = {
  primary: '#007bff',
  secondary: '#6c757d',
  success: '#28a745'
} as const;

// 4. Modern apps với good bundler
const ROUTES = ['/home', '/about', '/contact'] as const;
```

**✅ Sử dụng `enum` khi:**
```typescript
// 1. Need numeric values với meaning
enum Priority {
  LOW = 1,
  MEDIUM = 2,
  HIGH = 3,
  CRITICAL = 4
}

// So sánh numeric values
if (task.priority >= Priority.HIGH) {
  // Handle high priority
}

// 2. API integration với numeric codes
enum ApiResponseCode {
  SUCCESS = 200,
  NOT_FOUND = 404,
  SERVER_ERROR = 500
}

// 3. Bit flags operations
enum Permission {
  READ = 1,
  WRITE = 2,
  DELETE = 4,
  ADMIN = 8
}

const userPermissions = Permission.READ | Permission.WRITE; // Bitwise OR

// 4. Legacy codebase đã sử dụng enums
```

#### **🔥 BEST PRACTICES:**

```typescript
// 🎯 HYBRID APPROACH - Use both!

// as const cho simple constants
const APP_CONFIG = {
  NAME: 'MyApp',
  VERSION: '1.0.0'
} as const;

// enum cho business logic values
enum OrderStatus {
  PENDING = 'pending',
  PROCESSING = 'processing',
  SHIPPED = 'shipped',
  DELIVERED = 'delivered'
}

// ✅ Combine trong type definitions
type OrderUpdate = {
  status: OrderStatus;
  config: typeof APP_CONFIG;
};
```

**💡 GHI NHỚ:**
- **`as const`** = Zero cost, maximum flexibility 🚀
- **`enum`** = Runtime features, clear intent 📋

Choose based on **performance needs** và **use case complexity**! 🎯

---

### TS3: `type` vs `interface` - Sự khác biệt và best practices?

**Trả lời:**

Đây là **MỘT TRONG NHỮNG câu hỏi phổ biến nhất** về TypeScript. Cả hai đều define object shapes nhưng có những **KHÁC BIỆT QUAN TRỌNG**.

#### **🔥 SYNTAX & BASIC USAGE:**

**Interface:**
```typescript
// ✅ Interface - OOP style declaration
interface User {
  id: number;
  name: string;
  email: string;
}

// ✅ Extending interfaces
interface AdminUser extends User {
  permissions: string[];
  lastLogin: Date;
}
```

**Type:**
```typescript
// ✅ Type alias - functional style
type User = {
  id: number;
  name: string;
  email: string;
};

// ✅ Intersection types
type AdminUser = User & {
  permissions: string[];
  lastLogin: Date;
};
```

#### **⚖️ DETAILED COMPARISON:**

| Feature | `interface` | `type` |
|---------|-------------|--------|
| **Declaration Merging** | ✅ **CÓ** | ❌ **KHÔNG** |
| **Extending** | ✅ `extends` | ✅ `&` intersection |
| **Union Types** | ❌ **KHÔNG** | ✅ **CÓ** |
| **Computed Properties** | ❌ **Limited** | ✅ **Full support** |
| **Primitive Types** | ❌ **Object only** | ✅ **Any type** |
| **Performance** | ✅ **Faster** | ⚠️ **Slightly slower** |

#### **🔥 KEY DIFFERENCES:**

**1. Declaration Merging (Interface ONLY):**
```typescript
// ✅ Interface - CÓ THỂ merge multiple declarations
interface Window {
  title: string;
}

interface Window {
  version: string;
}

// TypeScript tự động merge thành:
// interface Window {
//   title: string;
//   version: string;
// }

// ❌ Type - KHÔNG THỂ redeclare
type Window = { title: string; };
// type Window = { version: string; }; // Error: Duplicate identifier
```

**2. Union Types (Type ONLY):**
```typescript
// ✅ Type - Có thể define union types
type Status = 'loading' | 'success' | 'error';
type StringOrNumber = string | number;
type ApiResponse = SuccessResponse | ErrorResponse;

// ❌ Interface - Không thể define unions trực tiếp
// interface Status = 'loading' | 'success' | 'error'; // Syntax error
```

**3. Computed Properties (Type BETTER):**
```typescript
// ✅ Type - Full support cho computed properties
type EventMap = {
  [K in 'click' | 'hover' | 'focus']: (event: Event) => void;
};

type DynamicObject<T> = {
  [K in keyof T]: T[K][];
};

// ⚠️ Interface - Limited support
interface EventMap {
  // Phải viết manual
  click: (event: Event) => void;
  hover: (event: Event) => void;
  focus: (event: Event) => void;
}
```

**4. Extending vs Intersection:**
```typescript
// ✅ Interface extending
interface Animal {
  name: string;
}

interface Dog extends Animal {
  breed: string;
}

// ✅ Type intersection
type Animal = {
  name: string;
};

type Dog = Animal & {
  breed: string;
};

// 🎯 Cả hai đều work tương tự cho simple cases
```

#### **🚀 ADVANCED USE CASES:**

**Interface cho OOP patterns:**
```typescript
// ✅ Interface - Perfect cho classes và inheritance
interface Drawable {
  draw(): void;
}

interface Resizable {
  resize(width: number, height: number): void;
}

// Multiple interface implementation
class Shape implements Drawable, Resizable {
  draw() { /* implementation */ }
  resize(width: number, height: number) { /* implementation */ }
}

// ✅ Declaration merging cho library augmentation
declare global {
  interface Array<T> {
    myCustomMethod(): T[];
  }
}
```

**Type cho functional programming:**
```typescript
// ✅ Type - Perfect cho utility types và transformations
type Partial<T> = {
  [P in keyof T]?: T[P];
};

type ApiEndpoint<T> = {
  url: string;
  method: 'GET' | 'POST' | 'PUT' | 'DELETE';
  body?: T;
  response: Promise<T>;
};

// Conditional types
type NonNullable<T> = T extends null | undefined ? never : T;

// Complex mappings
type EventHandlers<T> = {
  [K in keyof T as `on${Capitalize<string & K>}`]: (value: T[K]) => void;
};
```

#### **🎯 BEST PRACTICES - KHI NÀO DÙNG GÌ:**

**✅ Sử dụng `interface` khi:**
```typescript
// 1. Define object shapes cho classes
interface UserService {
  getUser(id: number): Promise<User>;
  updateUser(id: number, data: Partial<User>): Promise<User>;
}

class ApiUserService implements UserService {
  // Implementation
}

// 2. Public API definitions (libraries)
interface ComponentProps {
  children?: React.ReactNode;
  className?: string;
}

// 3. Có thể cần extend sau này
interface BaseConfig {
  apiUrl: string;
}

interface ProductionConfig extends BaseConfig {
  ssl: true;
}

// 4. Library augmentation
declare module 'react' {
  interface CSSProperties {
    '--custom-property'?: string;
  }
}
```

**✅ Sử dụng `type` khi:**
```typescript
// 1. Union types
type Theme = 'light' | 'dark' | 'auto';
type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE';

// 2. Complex type transformations
type EventMap<T> = {
  [K in keyof T]: (data: T[K]) => void;
};

// 3. Computed property names
type ApiRoutes = {
  [K in 'users' | 'posts' | 'comments' as `api/${K}`]: string;
};

// 4. Conditional logic
type NonEmptyArray<T> = [T, ...T[]];

// 5. Primitive type aliases
type ID = string | number;
type Timestamp = number;
```

#### **🔥 MODERN RECOMMENDATIONS:**

```typescript
// 🎯 HYBRID APPROACH - Use both strategically!

// ✅ interface cho object shapes
interface User {
  id: number;
  name: string;
  email: string;
}

// ✅ type cho unions và utilities
type UserStatus = 'active' | 'inactive' | 'banned';
type UserWithStatus = User & { status: UserStatus };

// ✅ interface cho component props
interface ButtonProps {
  children: React.ReactNode;
  onClick: () => void;
  variant?: 'primary' | 'secondary';
}

// ✅ type cho complex derived types
type ButtonEvents = {
  [K in keyof ButtonProps as K extends `on${string}` ? K : never]: ButtonProps[K];
};
```

**💡 GHI NHỚ:**
- **`interface`** = OOP style, extensible, declaration merging 🏗️
- **`type`** = Functional style, unions, computed properties 🎯

**Choose based on your use case, team style, và TypeScript version!** 🚀

---

### TS4: Browser có thể chạy TypeScript không? Tại sao?

**Trả lời:**

**❌ KHÔNG!** Browser **KHÔNG THỂ** chạy TypeScript trực tiếp. Đây là một **FUNDAMENTAL CONCEPT** cần hiểu rõ.

#### **🔥 TẠI SAO Browser KHÔNG chạy được TypeScript:**

**1. TypeScript IS NOT JavaScript:**
```typescript
// ❌ Code này browser KHÔNG hiểu
interface User {
  id: number;
  name: string;
}

function greetUser(user: User): string {
  return `Hello, ${user.name}!`;
}

// Browser sẽ throw: SyntaxError: Unexpected token ':'
```

**2. Browsers chỉ hiểu JavaScript (ES5/ES6+):**
```javascript
// ✅ Code này browser HIỂU được
function greetUser(user) {
  return `Hello, ${user.name}!`;
}
```

#### **🔄 QUY TRÌNH COMPILATION:**

```
📝 TypeScript (.ts)
        ↓
    🔧 TypeScript Compiler (tsc)
        ↓
📦 JavaScript (.js)
        ↓
    🌐 Browser Engine
        ↓
    🚀 Execution
```

#### **🛠️ CÁC CÁCH TRANSFORM TypeScript:**

**1. TypeScript Compiler (tsc):**
```bash
# Cài đặt TypeScript compiler
npm install -g typescript

# Compile single file
tsc app.ts

# Compile entire project
tsc --project tsconfig.json
```

**Example compilation:**
```typescript
// Input: app.ts
interface User {
  id: number;
  name: string;
}

const user: User = {
  id: 1,
  name: 'John'
};

function greetUser(user: User): string {
  return `Hello, ${user.name}!`;
}
```

```javascript
// Output: app.js (compiled)
"use strict";

const user = {
  id: 1,
  name: 'John'
};

function greetUser(user) {
  return `Hello, ${user.name}!`;
}
```

**2. Build Tools Integration:**

**Webpack với TypeScript:**
```javascript
// webpack.config.js
module.exports = {
  entry: './src/index.ts',
  module: {
    rules: [
      {
        test: /\.ts$/,
        use: 'ts-loader',
        exclude: /node_modules/
      }
    ]
  },
  resolve: {
    extensions: ['.ts', '.js']
  }
};
```

**Vite với TypeScript (Modern):**
```javascript
// vite.config.ts - ZERO CONFIG!
import { defineConfig } from 'vite';

export default defineConfig({
  // Vite tự động handle .ts files
});
```

**3. Real-time Development:**

**Babel-TypeScript:**
```json
// .babelrc
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-typescript"
  ]
}
```

**ts-node (Development only):**
```bash
# Chạy TypeScript trực tiếp (development)
npx ts-node src/app.ts

# Nhưng vẫn cần compile cho production!
```

#### **🚀 MODERN WORKFLOW:**

**Development:**
```typescript
// 📝 Write TypeScript
const users: User[] = await fetchUsers();

// 🔄 Hot reload với type checking
// Tools: Vite, Webpack Dev Server, ts-node
```

**Production Build:**
```bash
# 🔧 Build process
npm run build

# Output: Optimized JavaScript bundles
# dist/
#   ├── index.js (compiled + minified)
#   ├── vendor.js (dependencies)
#   └── style.css
```

#### **⚡ WHAT HAPPENS TO TypeScript FEATURES:**

**Type Annotations → REMOVED:**
```typescript
// TypeScript
function calculate(a: number, b: number): number {
  return a + b;
}

// Compiled JavaScript
function calculate(a, b) {
  return a + b;
}
```

**Interfaces → DISAPPEAR:**
```typescript
// TypeScript
interface Config {
  apiUrl: string;
  timeout: number;
}

// Compiled JavaScript
// (interfaces hoàn toàn biến mất!)
```

**Enums → BECOME Objects:**
```typescript
// TypeScript
enum Status {
  PENDING = 'pending',
  APPROVED = 'approved'
}

// Compiled JavaScript
var Status;
(function (Status) {
  Status["PENDING"] = "pending";
  Status["APPROVED"] = "approved";
})(Status || (Status = {}));
```

**Generics → ERASED:**
```typescript
// TypeScript
function identity<T>(arg: T): T {
  return arg;
}

// Compiled JavaScript
function identity(arg) {
  return arg;
}
```

#### **🔍 HOW TO VERIFY:**

**1. Browser DevTools:**
```javascript
// Open browser console và thử:
const user: User = { id: 1, name: 'John' };
// SyntaxError: Unexpected token ':'
```

**2. HTML Script Tag:**
```html
<!-- ❌ Điều này SẼ LỖI -->
<script src="app.ts"></script>

<!-- ✅ Điều này WORK -->
<script src="app.js"></script>
```

**3. Online TypeScript Playground:**
Visit [typescriptlang.org/play](https://typescriptlang.org/play) để see compilation process!

#### **💡 KEY TAKEAWAYS:**

```
🔹 TypeScript = DEVELOPMENT TIME tool
🔹 JavaScript = RUNTIME language
🔹 Compilation = MANDATORY step
🔹 Type safety = COMPILE TIME only
🔹 Browser = JavaScript ONLY environment
```

**🎯 INTERVIEW TIP:**
Always emphasize rằng TypeScript **MUST BE COMPILED** to JavaScript trước khi browser có thể run. Đây là **fundamental difference** giữa development và production environments!

**GHI NHỚ:** TypeScript in browser = **JavaScript with extra steps!** 🔄

---

### TS5: Type Narrowing trong TypeScript - Cách hoạt động?

**Trả lời:**

Type Narrowing là **CORE CONCEPT** trong TypeScript để **THU HẸP TYPE** từ union type thành specific type. Đây là **ADVANCED TECHNIQUE** giúp TypeScript hiểu chính xác type trong runtime.

#### **🔥 FUNDAMENTAL CONCEPT:**

**Type Narrowing = Từ WIDE TYPE → NARROW TYPE**

```typescript
// 🌐 WIDE TYPE (Union)
type StringOrNumber = string | number;

function processValue(value: StringOrNumber) {
  // 🔍 NARROWING: Thu hẹp type để TypeScript hiểu rõ
  if (typeof value === "string") {
    // ✅ TypeScript biết: value is STRING
    return value.toUpperCase(); // ✅ String methods available
  } else {
    // ✅ TypeScript biết: value is NUMBER
    return value.toFixed(2); // ✅ Number methods available
  }
}
```

#### **🛠️ CÁC PHƯƠNG PHÁP TYPE NARROWING:**

**1. typeof Guards:**
```typescript
function handleInput(input: string | number | boolean) {
  if (typeof input === "string") {
    console.log(`String: ${input.length} characters`); // ✅ string methods
  } else if (typeof input === "number") {
    console.log(`Number: ${input.toFixed(2)}`); // ✅ number methods
  } else {
    console.log(`Boolean: ${input ? "true" : "false"}`); // ✅ boolean context
  }
}

// 📝 GHI NHỚ: typeof returns "string" | "number" | "boolean" | "object" | "undefined" | "function"
```

**2. instanceof Guards:**
```typescript
class Dog {
  bark() { return "Woof!"; }
}

class Cat {
  meow() { return "Meow!"; }
}

function makeSound(animal: Dog | Cat) {
  if (animal instanceof Dog) {
    return animal.bark(); // ✅ TypeScript knows it's Dog
  } else {
    return animal.meow(); // ✅ TypeScript knows it's Cat
  }
}

// 📝 GHI NHỚ: instanceof kiểm tra prototype chain
```

**3. in Operator (Property Check):**
```typescript
interface Bird {
  fly(): void;
  feathers: number;
}

interface Fish {
  swim(): void;
  scales: number;
}

function move(animal: Bird | Fish) {
  if ("fly" in animal) {
    animal.fly(); // ✅ TypeScript knows it's Bird
    console.log(`Bird has ${animal.feathers} feathers`);
  } else {
    animal.swim(); // ✅ TypeScript knows it's Fish
    console.log(`Fish has ${animal.scales} scales`);
  }
}

// 📝 GHI NHỚ: "property" in object kiểm tra property existence
```

**4. Literal Type Guards:**
```typescript
type Status = "loading" | "success" | "error";

function handleStatus(status: Status) {
  if (status === "loading") {
    return "Đang tải..."; // ✅ Exact literal type
  } else if (status === "success") {
    return "Thành công!"; // ✅ Exact literal type
  } else {
    return "Có lỗi xảy ra!"; // ✅ TypeScript knows it's "error"
  }
}
```

**5. Custom Type Guards (Advanced):**
```typescript
// 🎯 CUSTOM TYPE PREDICATE FUNCTIONS
interface User {
  id: number;
  name: string;
  email: string;
}

interface Admin {
  id: number;
  name: string;
  permissions: string[];
}

// 🔧 Custom Type Guard Function
function isAdmin(user: User | Admin): user is Admin {
  return 'permissions' in user; // Return type: user is Admin
}

function handleUser(user: User | Admin) {
  if (isAdmin(user)) {
    // ✅ TypeScript knows user is Admin
    console.log(`Admin ${user.name} has ${user.permissions.length} permissions`);
  } else {
    // ✅ TypeScript knows user is User
    console.log(`User ${user.name} email: ${user.email}`);
  }
}

// 📝 GHI NHỚ: "x is Type" syntax là Type Predicate
```

#### **⚡ ADVANCED NARROWING PATTERNS:**

**1. Discriminated Unions:**
```typescript
// 🏷️ TAGGED UNION với common property
interface LoadingState {
  status: "loading"; // 🏷️ Discriminator property
}

interface SuccessState {
  status: "success"; // 🏷️ Discriminator property
  data: any[];
}

interface ErrorState {
  status: "error"; // 🏷️ Discriminator property
  message: string;
}

type AppState = LoadingState | SuccessState | ErrorState;

function renderState(state: AppState) {
  // 🎯 PERFECT NARROWING bằng discriminator
  switch (state.status) {
    case "loading":
      return <div>Loading...</div>; // ✅ TypeScript knows LoadingState
    case "success":
      return <div>{state.data.length} items</div>; // ✅ data property available
    case "error":
      return <div>Error: {state.message}</div>; // ✅ message property available
  }
}

// 📝 GHI NHỚ: Discriminated Union = Union + Common Property với literal types
```

**2. Exhaustiveness Checking:**
```typescript
type Theme = "light" | "dark" | "auto";

function getThemeColor(theme: Theme): string {
  switch (theme) {
    case "light":
      return "#ffffff";
    case "dark":
      return "#000000";
    case "auto":
      return "#f0f0f0";
    default:
      // 🚨 EXHAUSTIVENESS CHECK
      const exhaustiveCheck: never = theme;
      throw new Error(`Unhandled theme: ${exhaustiveCheck}`);
  }
}

// 📝 GHI NHỚ: never type giúp catch missing cases khi thêm new literal types
```

**3. Nullish Narrowing:**
```typescript
function processName(name: string | null | undefined) {
  // ❌ UNSAFE - might be null/undefined
  // return name.toUpperCase();

  // ✅ SAFE - narrowing first
  if (name != null) { // Removes both null AND undefined
    return name.toUpperCase(); // ✅ TypeScript knows name is string
  }
  return "Unknown";
}

// Alternative với Optional Chaining
function processNameSafe(name: string | null | undefined) {
  return name?.toUpperCase() ?? "Unknown";
}

// 📝 GHI NHỚ: name != null removes both null AND undefined
// 📝 GHI NHỞ: name !== null chỉ removes null, NOT undefined
```

#### **🎯 PRACTICAL EXAMPLES:**

**Real-world API Response Handling:**
```typescript
interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}

function handleApiResponse<T>(response: ApiResponse<T>) {
  if (response.success && response.data) {
    // ✅ TypeScript knows data exists và success = true
    return response.data; // ✅ Type T available
  } else if (!response.success && response.error) {
    // ✅ TypeScript knows error exists và success = false
    throw new Error(response.error); // ✅ string methods available
  } else {
    throw new Error("Invalid API response format");
  }
}

// 📝 GHI NHỞ: Multiple conditions for comprehensive narrowing
```

**React Props Narrowing:**
```typescript
interface ButtonProps {
  variant: "primary" | "secondary";
  size: "small" | "medium" | "large";
  disabled?: boolean;
  onClick?: () => void;
}

function Button({ variant, size, disabled, onClick }: ButtonProps) {
  // 🎯 NARROWING cho conditional rendering
  if (disabled) {
    return (
      <button className={`btn-${variant} btn-${size} btn-disabled`}>
        {/* ✅ TypeScript knows disabled is true */}
        Disabled Button
      </button>
    );
  }

  return (
    <button
      className={`btn-${variant} btn-${size}`}
      onClick={onClick} // ✅ Safe to use
    >
      Active Button
    </button>
  );
}
```

#### **💡 INTERVIEW INSIGHTS:**

**🔹 KHI NÀO SỬ DỤNG:**
- Union types cần specific handling
- API responses với multiple states
- Event handling với different event types
- Form validation với conditional logic

**🔹 COMMON MISTAKES:**
```typescript
// ❌ SAI: Không narrow type
function badExample(value: string | number) {
  return value.toUpperCase(); // 💥 Error: toUpperCase not exist on number
}

// ✅ ĐÚNG: Narrow type first
function goodExample(value: string | number) {
  if (typeof value === "string") {
    return value.toUpperCase(); // ✅ Works
  }
  return value.toString().toUpperCase();
}
```

**🔹 PERFORMANCE IMPACT:**
- Type narrowing = **COMPILE TIME** only
- **NO RUNTIME OVERHEAD**
- Improves **DEVELOPMENT EXPERIENCE** và **TYPE SAFETY**

#### **🚀 TYPE NARROWING WORKFLOW:**

```
🌐 Wide Union Type
        ↓
🔍 Runtime Check (typeof, instanceof, in, custom guard)
        ↓
🎯 Narrowed Specific Type
        ↓
✅ Safe Property/Method Access
```

**📝 GOLDEN RULES:**
1. **Always narrow BEFORE access** union type properties
2. **Use type guards** cho complex narrowing logic
3. **Discriminated unions** cho state management
4. **Custom type predicates** cho reusable logic
5. **Exhaustiveness checking** với never type

**GHI NHỞ:** Type Narrowing = **TypeScript's way of making UNSAFE code SAFE!** 🛡️

---

### TS6: `unknown` vs `any` - Sự khác biệt và khi nào sử dụng?

**Trả lời:**

Đây là **CRUCIAL DISTINCTION** trong TypeScript! `unknown` và `any` đều represent "anything", nhưng **SAFETY LEVEL** hoàn toàn khác nhau.

#### **🔥 FUNDAMENTAL DIFFERENCE:**

| Aspect | **`any`** | **`unknown`** |
|--------|-----------|---------------|
| **Type Safety** | ❌ **UNSAFE** | ✅ **SAFE** |
| **Type Checking** | **DISABLED** | **ENABLED** |
| **Direct Access** | ✅ **Allowed** | ❌ **Forbidden** |
| **Need Type Guards** | ❌ **No** | ✅ **Required** |
| **Best Practice** | 🚫 **Avoid** | ✅ **Preferred** |

#### **🛠️ `any` - THE ESCAPE HATCH:**

```typescript
let value: any = 42;

// ❌ DANGEROUS: No type checking whatsoever!
value.foo.bar.baz; // 💥 Runtime error, TypeScript won't catch
value(); // 💥 Runtime error if not a function
value[0][1][2]; // 💥 Runtime error if not nested array
value.toUpperCase(); // 💥 Runtime error if not string

// 😱 TYPESCRIPT GIVES UP: No intellisense, no safety!
```

**ANY = "Trust me, I know what I'm doing" (but usually you don't!) 🚫**

#### **🛡️ `unknown` - THE SAFE ALTERNATIVE:**

```typescript
let value: unknown = 42;

// ✅ SAFE: TypeScript forces type checking!
// value.foo; // ❌ Compile error: Object is of type 'unknown'
// value(); // ❌ Compile error: Cannot invoke unknown type
// value.toUpperCase(); // ❌ Compile error: Property doesn't exist

// ✅ MUST USE TYPE GUARDS first:
if (typeof value === "string") {
  console.log(value.toUpperCase()); // ✅ Now it's safe!
}

if (typeof value === "number") {
  console.log(value.toFixed(2)); // ✅ Number methods available
}
```

**UNKNOWN = "I don't know what this is, let me check first!" ✅**

#### **📊 DETAILED COMPARISON:**

**1. Assignment TO them:**
```typescript
// ✅ BOTH accept anything
let anyValue: any = "hello";
let unknownValue: unknown = "hello";

anyValue = 42; // ✅ OK
unknownValue = 42; // ✅ OK

anyValue = { name: "John" }; // ✅ OK
unknownValue = { name: "John" }; // ✅ OK

anyValue = [1, 2, 3]; // ✅ OK
unknownValue = [1, 2, 3]; // ✅ OK
```

**2. Assignment FROM them:**
```typescript
let anyValue: any = "hello";
let unknownValue: unknown = "hello";

// ❌ ANY: Can assign to ANYTHING (dangerous!)
let str1: string = anyValue; // ✅ No error (but dangerous!)
let num1: number = anyValue; // ✅ No error (but dangerous!)
let bool1: boolean = anyValue; // ✅ No error (but dangerous!)

// ✅ UNKNOWN: Cannot assign without type checking
// let str2: string = unknownValue; // ❌ Error: Type 'unknown' not assignable
// let num2: number = unknownValue; // ❌ Error

// ✅ MUST narrow type first
if (typeof unknownValue === "string") {
  let str2: string = unknownValue; // ✅ Now it's safe!
}
```

**3. Property Access:**
```typescript
let anyValue: any = { name: "John", age: 30 };
let unknownValue: unknown = { name: "John", age: 30 };

// ❌ ANY: Direct access (unsafe)
console.log(anyValue.name); // ✅ No error (but risky)
console.log(anyValue.nonexistent); // ✅ No error (returns undefined)

// ✅ UNKNOWN: Must check first
// console.log(unknownValue.name); // ❌ Error

// ✅ Safe way with type guards
if (unknownValue && typeof unknownValue === "object" && "name" in unknownValue) {
  console.log((unknownValue as { name: string }).name); // ✅ Safe
}
```

#### **🎯 PRACTICAL USE CASES:**

**1. API Responses (Best Practice with `unknown`):**
```typescript
// ❌ BAD: Using any
async function fetchUserBad(): Promise<any> {
  const response = await fetch('/api/user');
  const data = await response.json(); // Returns any
  return data; // ❌ No type safety
}

// ✅ GOOD: Using unknown
async function fetchUserGood(): Promise<unknown> {
  const response = await fetch('/api/user');
  const data = await response.json(); // Returns any, but we convert to unknown
  return data; // ✅ Forces type checking at usage
}

// Usage
async function handleUser() {
  const userData = await fetchUserGood();

  // ✅ Must validate first
  if (isUser(userData)) {
    console.log(`User: ${userData.name}`); // ✅ Type-safe
  }
}

// 🔧 Type guard function
interface User {
  id: number;
  name: string;
  email: string;
}

function isUser(obj: unknown): obj is User {
  return (
    obj !== null &&
    typeof obj === "object" &&
    typeof (obj as User).id === "number" &&
    typeof (obj as User).name === "string" &&
    typeof (obj as User).email === "string"
  );
}
```

**2. Error Handling:**
```typescript
// ❌ BAD: Using any
function handleErrorBad(error: any) {
  console.log(error.message); // 💥 Might crash if error has no message
  throw error; // ❌ No type safety
}

// ✅ GOOD: Using unknown
function handleErrorGood(error: unknown) {
  // ✅ Safe error handling
  if (error instanceof Error) {
    console.log(error.message); // ✅ TypeScript knows it's Error
    console.log(error.stack);
  } else if (typeof error === "string") {
    console.log(error); // ✅ TypeScript knows it's string
  } else {
    console.log("Unknown error occurred"); // ✅ Fallback
  }
}

// Better: Custom error type guard
function isErrorWithMessage(error: unknown): error is { message: string } {
  return (
    typeof error === "object" &&
    error !== null &&
    "message" in error &&
    typeof (error as { message: unknown }).message === "string"
  );
}

function safeErrorHandler(error: unknown) {
  if (isErrorWithMessage(error)) {
    console.log(error.message); // ✅ Safe access
  } else {
    console.log("Error without message");
  }
}
```

**3. JSON Parsing:**
```typescript
// ❌ BAD: JSON.parse returns any
function parseJsonBad(jsonString: string) {
  const data = JSON.parse(jsonString); // any type
  return data.user.name; // 💥 Might crash
}

// ✅ GOOD: Treat as unknown and validate
function parseJsonGood(jsonString: string) {
  const data: unknown = JSON.parse(jsonString);

  // ✅ Validate structure first
  if (isValidUserData(data)) {
    return data.user.name; // ✅ Type-safe
  }

  throw new Error("Invalid JSON structure");
}

function isValidUserData(data: unknown): data is { user: { name: string } } {
  return (
    data !== null &&
    typeof data === "object" &&
    "user" in data &&
    typeof (data as any).user === "object" &&
    typeof (data as any).user.name === "string"
  );
}
```

**4. Library Migration:**
```typescript
// 🔄 MIGRATION STRATEGY: any → unknown
// Step 1: Change return type from any to unknown
function oldLibraryCall(): unknown { // Was: any
  return legacyLibrary.getData();
}

// Step 2: Add type guards where needed
function useLibraryData() {
  const data = oldLibraryCall();

  // Must add validation now
  if (isExpectedFormat(data)) {
    processData(data); // ✅ Type-safe
  }
}
```

#### **⚡ ADVANCED PATTERNS:**

**1. Generic Functions with unknown:**
```typescript
// ✅ SAFE generic function
function safeCast<T>(value: unknown, validator: (val: unknown) => val is T): T | null {
  return validator(value) ? value : null;
}

// Usage
const userData = safeCast(apiResponse, isUser);
if (userData) {
  console.log(userData.name); // ✅ Typed as User
}
```

**2. Unknown in Union Types:**
```typescript
type SafeApiResponse =
  | { success: true; data: unknown } // ✅ Unknown forces validation
  | { success: false; error: string };

function handleResponse(response: SafeApiResponse) {
  if (response.success) {
    // Must validate response.data before use
    if (isUser(response.data)) {
      console.log(response.data.name); // ✅ Safe
    }
  } else {
    console.log(response.error); // ✅ Already typed as string
  }
}
```

#### **🚨 MIGRATION GUIDE: `any` → `unknown`:**

```typescript
// 🔄 STEP-BY-STEP MIGRATION

// Before (unsafe):
function processData(data: any) {
  return data.items.map((item: any) => item.name.toUpperCase());
}

// After (safe):
function processDataSafe(data: unknown) {
  // Add validation
  if (isDataWithItems(data)) {
    return data.items
      .filter(isItemWithName) // Filter valid items
      .map(item => item.name.toUpperCase()); // ✅ Safe
  }
  throw new Error("Invalid data format");
}

// Type guards needed:
function isDataWithItems(data: unknown): data is { items: unknown[] } {
  return (
    data !== null &&
    typeof data === "object" &&
    "items" in data &&
    Array.isArray((data as any).items)
  );
}

function isItemWithName(item: unknown): item is { name: string } {
  return (
    item !== null &&
    typeof item === "object" &&
    "name" in item &&
    typeof (item as any).name === "string"
  );
}
```

#### **💡 INTERVIEW INSIGHTS:**

**🔹 KHI NÀO SỬ DỤNG `any`:**
- 😤 **NEVER** in new code! (nếu có thể)
- 🔄 **Legacy code migration** (temporary)
- 📦 **Third-party libraries** without types (use `@types` if available)
- ⚡ **Rapid prototyping** (but refactor later!)

**🔹 KHI NÀO SỬ DỤNG `unknown`:**
- ✅ **API responses** chưa biết structure
- ✅ **Error handling** generic errors
- ✅ **JSON parsing** external data
- ✅ **User input** validation
- ✅ **Library functions** returning uncertain types

**🔹 PERFORMANCE:**
- Both `any` và `unknown` = **NO RUNTIME COST**
- Difference = **COMPILE TIME** type checking only
- `unknown` = **Better developer experience** + **Fewer runtime errors**

#### **🎯 DECISION FRAMEWORK:**

```
❓ Do you know the exact type?
   ├─ Yes → Use specific type
   └─ No ↓

❓ Can you validate the type?
   ├─ Yes → Use unknown + type guards
   └─ No ↓

❓ Is this legacy/migration code?
   ├─ Yes → Use any (temporarily)
   └─ No → Refactor to use unknown
```

**📝 GOLDEN RULES:**
1. **Default to `unknown`** when uncertain about types
2. **Avoid `any`** unless absolutely necessary
3. **Always validate `unknown`** before usage
4. **Create type guards** for common validation patterns
5. **Migrate `any` to `unknown`** in existing code

**GHI NHỚ:**
- `any` = **"I don't care about types"** 🚫
- `unknown` = **"I care about types, let me check first"** ✅

**INTERVIEW TIP:** Always emphasize rằng `unknown` is **TYPE-SAFE** alternative to `any`, và showcase your knowledge của proper type validation patterns! 🎯

---

### TS7: Decorator trong TypeScript - Khái niệm và ứng dụng?

**Trả lời:**

Decorators là **EXPERIMENTAL FEATURE** trong TypeScript cho phép **MODIFY BEHAVIOR** của classes, methods, properties, và parameters thông qua **METADATA và RUNTIME MANIPULATION**.

#### **🔥 FUNDAMENTAL CONCEPT:**

**Decorator = Function that MODIFIES another function/class**

```typescript
// 🏷️ BASIC DECORATOR SYNTAX
@decoratorFunction
class MyClass {
  @propertyDecorator
  property: string;

  @methodDecorator
  method() {}
}

// Equivalent to:
MyClass = decoratorFunction(MyClass);
```

#### **⚙️ ENABLING DECORATORS:**

**tsconfig.json:**
```json
{
  "compilerOptions": {
    "experimentalDecorators": true,    // ✅ Enable legacy decorators
    "emitDecoratorMetadata": true      // ✅ Emit metadata (cho reflection)
  }
}

// 📝 GHI NHỚ: Decorators vẫn là EXPERIMENTAL feature!
```

#### **🛠️ TYPES OF DECORATORS:**

**1. Class Decorators:**
```typescript
// 🎯 CLASS DECORATOR FUNCTION
function Component(config: { selector: string; template: string }) {
  return function<T extends { new(...args: any[]): {} }>(constructor: T) {
    return class extends constructor {
      selector = config.selector;
      template = config.template;

      // ✅ Add new functionality to class
      render() {
        console.log(`Rendering ${this.selector}: ${this.template}`);
      }
    };
  };
}

// 🏷️ USAGE
@Component({
  selector: 'app-user',
  template: '<div>User Component</div>'
})
class UserComponent {
  name = 'John';
}

// Test
const user = new UserComponent() as any;
user.render(); // "Rendering app-user: <div>User Component</div>"

// 📝 GHI NHỚ: Class decorator receives constructor function
```

**2. Method Decorators:**
```typescript
// 🎯 METHOD DECORATOR for performance tracking
function benchmark(target: any, propertyName: string, descriptor: PropertyDescriptor) {
  const method = descriptor.value;

  descriptor.value = function (...args: any[]) {
    console.time(`${propertyName} execution time`);
    const result = method.apply(this, args);
    console.timeEnd(`${propertyName} execution time`);
    return result;
  };
}

class DataProcessor {
  @benchmark
  processLargeDataset(data: any[]) {
    // Simulate heavy computation
    return data.map(item => item * 2);
  }
}

// Usage
const processor = new DataProcessor();
processor.processLargeDataset([1, 2, 3]); // ⏱️ Logs execution time

// 📝 GHI NHỚ: Method decorator receives target, propertyName, descriptor
```

**3. Property Decorators:**
```typescript
// 🎯 PROPERTY DECORATOR for validation
function required(target: any, propertyName: string) {
  // Store metadata về required fields
  const requiredFields = Reflect.getMetadata('required', target) || [];
  requiredFields.push(propertyName);
  Reflect.defineMetadata('required', requiredFields, target);
}

function validate(target: any) {
  const requiredFields: string[] = Reflect.getMetadata('required', target) || [];

  for (const field of requiredFields) {
    if (!target[field]) {
      throw new Error(`Field ${field} is required`);
    }
  }
}

class User {
  @required
  name: string;

  @required
  email: string;

  age?: number;

  constructor(name: string, email: string, age?: number) {
    this.name = name;
    this.email = email;
    this.age = age;

    validate(this); // ✅ Validate required fields
  }
}

// Usage
const user1 = new User("John", "john@email.com"); // ✅ OK
// const user2 = new User("", "john@email.com"); // ❌ Error: Field name is required

// 📝 GHI NHỞ: Property decorator receives target và propertyName
```

**4. Parameter Decorators:**
```typescript
// 🎯 PARAMETER DECORATOR for dependency injection
function inject(token: string) {
  return function (target: any, propertyName: string | symbol, parameterIndex: number) {
    // Store injection metadata
    const existingTokens = Reflect.getMetadata('inject', target) || [];
    existingTokens[parameterIndex] = token;
    Reflect.defineMetadata('inject', existingTokens, target);
  };
}

// Simple DI Container
class Container {
  private services = new Map<string, any>();

  register(token: string, service: any) {
    this.services.set(token, service);
  }

  resolve<T>(constructor: new (...args: any[]) => T): T {
    const tokens: string[] = Reflect.getMetadata('inject', constructor) || [];
    const dependencies = tokens.map(token => this.services.get(token));
    return new constructor(...dependencies);
  }
}

// Services
class Logger {
  log(message: string) {
    console.log(`[LOG]: ${message}`);
  }
}

class Database {
  query(sql: string) {
    console.log(`Executing: ${sql}`);
  }
}

// Service with dependencies
class UserService {
  constructor(
    @inject('logger') private logger: Logger,
    @inject('database') private database: Database
  ) {}

  getUser(id: number) {
    this.logger.log(`Getting user ${id}`);
    this.database.query(`SELECT * FROM users WHERE id = ${id}`);
  }
}

// Usage
const container = new Container();
container.register('logger', new Logger());
container.register('database', new Database());

const userService = container.resolve(UserService);
userService.getUser(1);

// 📝 GHI NHỚ: Parameter decorator receives target, propertyName, parameterIndex
```

#### **⚡ ADVANCED PATTERNS:**

**1. Decorator Factory Pattern:**
```typescript
// 🎯 DECORATOR FACTORY - Function that returns decorator
function cache(ttl: number = 5000) {
  const cacheStore = new Map<string, { data: any; timestamp: number }>();

  return function (target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;

    descriptor.value = function (...args: any[]) {
      const key = `${propertyName}_${JSON.stringify(args)}`;
      const cached = cacheStore.get(key);

      // ✅ Return cached result if valid
      if (cached && (Date.now() - cached.timestamp) < ttl) {
        console.log(`Cache hit for ${propertyName}`);
        return cached.data;
      }

      // ✅ Execute và cache result
      const result = originalMethod.apply(this, args);
      cacheStore.set(key, { data: result, timestamp: Date.now() });
      console.log(`Cache miss for ${propertyName}`);
      return result;
    };
  };
}

class ApiService {
  @cache(3000) // Cache for 3 seconds
  fetchUser(id: number) {
    console.log(`Fetching user ${id} from API...`);
    return { id, name: `User ${id}` };
  }
}

// Test caching
const api = new ApiService();
api.fetchUser(1); // Cache miss
api.fetchUser(1); // Cache hit (within 3s)
```

**2. Multiple Decorators (Composition):**
```typescript
// 🎯 MULTIPLE DECORATORS - Applied bottom to top
function log(target: any, propertyName: string, descriptor: PropertyDescriptor) {
  const method = descriptor.value;
  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyName} with args:`, args);
    return method.apply(this, args);
  };
}

function retry(attempts: number = 3) {
  return function (target: any, propertyName: string, descriptor: PropertyDescriptor) {
    const method = descriptor.value;

    descriptor.value = async function (...args: any[]) {
      for (let i = 0; i < attempts; i++) {
        try {
          return await method.apply(this, args);
        } catch (error) {
          console.log(`Attempt ${i + 1} failed:`, error);
          if (i === attempts - 1) throw error;
        }
      }
    };
  };
}

class NetworkService {
  @log           // ✅ Applied second (outer)
  @retry(3)      // ✅ Applied first (inner)
  async fetchData(url: string) {
    // Simulate random failure
    if (Math.random() > 0.7) {
      throw new Error('Network error');
    }
    return `Data from ${url}`;
  }
}

// 📝 GHI NHỚ: Decorators execute BOTTOM to TOP (như function composition)
```

#### **🎯 REAL-WORLD EXAMPLES:**

**1. Angular-style Component Decorator:**
```typescript
interface ComponentConfig {
  selector: string;
  template: string;
  styles?: string[];
}

// 🎯 COMPONENT FRAMEWORK với decorators
function Component(config: ComponentConfig) {
  return function <T extends { new(...args: any[]): {} }>(constructor: T) {
    // Add metadata to class
    Reflect.defineMetadata('component', config, constructor);

    return class extends constructor {
      // ✅ Add framework functionality
      private _selector = config.selector;
      private _template = config.template;

      render(container: HTMLElement) {
        container.innerHTML = this._template;
        console.log(`Component ${this._selector} rendered`);
      }
    };
  };
}

@Component({
  selector: 'user-profile',
  template: '<div class="user">{{name}}</div>',
  styles: ['div.user { color: blue; }']
})
class UserProfileComponent {
  name: string = 'John Doe';
}
```

**2. Express-style Route Decorators:**
```typescript
// 🎯 EXPRESS ROUTING với decorators
const routes: Array<{
  method: string;
  path: string;
  handler: string;
  target: any;
}> = [];

function Get(path: string) {
  return function (target: any, propertyName: string) {
    routes.push({
      method: 'GET',
      path,
      handler: propertyName,
      target: target.constructor
    });
  };
}

function Post(path: string) {
  return function (target: any, propertyName: string) {
    routes.push({
      method: 'POST',
      path,
      handler: propertyName,
      target: target.constructor
    });
  };
}

class UserController {
  @Get('/users')
  getUsers() {
    return [{ id: 1, name: 'John' }];
  }

  @Post('/users')
  createUser() {
    return { id: 2, name: 'Jane' };
  }

  @Get('/users/:id')
  getUser() {
    return { id: 1, name: 'John' };
  }
}

// Framework integration
function createRouter() {
  console.log('Registered routes:');
  routes.forEach(route => {
    console.log(`${route.method} ${route.path} -> ${route.target.name}.${route.handler}`);
  });
}

createRouter();
// Output:
// GET /users -> UserController.getUsers
// POST /users -> UserController.createUser
// GET /users/:id -> UserController.getUser
```

**3. Validation Decorators:**
```typescript
// 🎯 VALIDATION DECORATORS
function IsEmail(target: any, propertyName: string) {
  addValidator(target, propertyName, (value: string) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(value) || `${propertyName} must be a valid email`;
  });
}

function MinLength(length: number) {
  return function (target: any, propertyName: string) {
    addValidator(target, propertyName, (value: string) => {
      return value.length >= length || `${propertyName} must be at least ${length} characters`;
    });
  };
}

function addValidator(target: any, propertyName: string, validator: (value: any) => boolean | string) {
  const validators = Reflect.getMetadata('validators', target) || {};
  validators[propertyName] = validators[propertyName] || [];
  validators[propertyName].push(validator);
  Reflect.defineMetadata('validators', validators, target);
}

function validate(obj: any): string[] {
  const validators = Reflect.getMetadata('validators', obj) || {};
  const errors: string[] = [];

  for (const [property, validatorList] of Object.entries(validators)) {
    const value = obj[property];
    for (const validator of validatorList as Function[]) {
      const result = validator(value);
      if (result !== true) {
        errors.push(result);
      }
    }
  }

  return errors;
}

class RegisterDto {
  @IsEmail
  email: string;

  @MinLength(8)
  password: string;

  constructor(email: string, password: string) {
    this.email = email;
    this.password = password;
  }
}

// Usage
const dto1 = new RegisterDto("test@email.com", "password123");
console.log(validate(dto1)); // []

const dto2 = new RegisterDto("invalid-email", "123");
console.log(validate(dto2)); // ["email must be a valid email", "password must be at least 8 characters"]
```

#### **💡 INTERVIEW INSIGHTS:**

**🔹 DECORATOR EXECUTION ORDER:**
```typescript
@first
@second
@third
class MyClass {}

// Execution: third() → second() → first()
// Like: first(second(third(MyClass)))
```

**🔹 PERFORMANCE CONSIDERATIONS:**
- Decorators run at **CLASS DEFINITION TIME**, not instantiation
- **NO RUNTIME OVERHEAD** for simple decorators
- **METADATA STORAGE** can increase memory usage
- **METHOD WRAPPING** có thể affect performance

**🔹 BROWSER SUPPORT:**
- Cần **POLYFILL** cho `reflect-metadata`
- **BABEL/TSC** transforms decorators to regular JavaScript
- Modern frameworks handle này automatically

**🔹 ALTERNATIVES TO DECORATORS:**
```typescript
// Instead of decorators, you can use:

// 1. Higher-Order Functions
const withLogging = (fn: Function) => (...args: any[]) => {
  console.log('Calling function');
  return fn(...args);
};

// 2. Class Mixins
function LoggingMixin<T extends Constructor>(Base: T) {
  return class extends Base {
    log(message: string) {
      console.log(message);
    }
  };
}

// 3. Composition Pattern
class Logger {
  static wrap(method: Function) {
    return (...args: any[]) => {
      console.log('Method called');
      return method(...args);
    };
  }
}
```

#### **🚀 BEST PRACTICES:**

**📝 DO's:**
- ✅ Use for **CROSS-CUTTING CONCERNS** (logging, caching, validation)
- ✅ Keep decorators **SIMPLE và FOCUSED**
- ✅ **DOCUMENT** decorator behavior clearly
- ✅ Consider **COMPOSITION** over complex inheritance

**📝 DON'Ts:**
- ❌ Don't use for **BUSINESS LOGIC**
- ❌ Avoid **DEEPLY NESTED** decorator logic
- ❌ Don't **OVERUSE** decorators (readability impact)
- ❌ Avoid **SIDE EFFECTS** in decorator factories

**GHI NHỚ:** Decorators = **METADATA + BEHAVIOR MODIFICATION** at compile/definition time! Perfect for **FRAMEWORK DEVELOPMENT** và **ASPECT-ORIENTED PROGRAMMING**! 🎯

---

### TS8: Generics trong TypeScript - Concept và Examples?

**Trả lời:**

Generics là **POWERFUL FEATURE** cho phép tạo **REUSABLE COMPONENTS** với **FLEXIBLE TYPES**. Thay vì hardcode specific types, generics cho phép **PARAMETERIZE TYPES**!

#### **🔥 FUNDAMENTAL CONCEPT:**

**Generics = PLACEHOLDER for TYPES**

```typescript
// ❌ WITHOUT GENERICS: Type-specific functions
function getStringArray(): string[] {
  return [];
}

function getNumberArray(): number[] {
  return [];
}

function getBooleanArray(): boolean[] {
  return [];
}

// ✅ WITH GENERICS: One function, any type!
function getArray<T>(): T[] {
  return [];
}

// Usage - TypeScript infers the type
const strings = getArray<string>(); // string[]
const numbers = getArray<number>(); // number[]
const booleans = getArray<boolean>(); // boolean[]

// 📝 GHI NHỚ: T = Type Parameter (có thể đặt tên gì cũng được: K, V, U, etc.)
```

#### **🛠️ BASIC GENERIC SYNTAX:**

**1. Function Generics:**
```typescript
// 🎯 GENERIC FUNCTION với type parameter T
function identity<T>(arg: T): T {
  return arg; // Input type = Output type
}

// ✅ USAGE - Explicit type
const result1 = identity<string>("hello"); // result1: string
const result2 = identity<number>(42); // result2: number

// ✅ USAGE - Type inference (TypeScript tự đoán)
const result3 = identity("hello"); // result3: string (inferred)
const result4 = identity(42); // result4: number (inferred)

// 📝 GHI NHỚ: Type inference makes generics MORE CONVENIENT!
```

**2. Generic Arrays:**
```typescript
// 🎯 WORKING WITH GENERIC ARRAYS
function getFirstElement<T>(array: T[]): T | undefined {
  return array.length > 0 ? array[0] : undefined;
}

// Usage
const firstString = getFirstElement(["a", "b", "c"]); // string | undefined
const firstNumber = getFirstElement([1, 2, 3]); // number | undefined
const firstUser = getFirstElement([
  { id: 1, name: "John" },
  { id: 2, name: "Jane" }
]); // { id: number; name: string; } | undefined

// 🎯 GENERIC ARRAY OPERATIONS
function reverseArray<T>(array: T[]): T[] {
  return array.slice().reverse(); // ✅ Preserve original array
}

const reversedStrings = reverseArray(["a", "b", "c"]); // string[]
const reversedNumbers = reverseArray([1, 2, 3]); // number[]
```

#### **🏗️ GENERIC CLASSES:**

```typescript
// 🎯 GENERIC CLASS for data storage
class Container<T> {
  private items: T[] = [];

  add(item: T): void {
    this.items.push(item);
  }

  get(index: number): T | undefined {
    return this.items[index];
  }

  getAll(): T[] {
    return [...this.items]; // ✅ Return copy
  }

  size(): number {
    return this.items.length;
  }

  // ✅ Generic method within generic class
  filter(predicate: (item: T) => boolean): T[] {
    return this.items.filter(predicate);
  }
}

// Usage
const stringContainer = new Container<string>();
stringContainer.add("hello");
stringContainer.add("world");
console.log(stringContainer.getAll()); // ["hello", "world"]

const numberContainer = new Container<number>();
numberContainer.add(1);
numberContainer.add(2);
const evenNumbers = numberContainer.filter(n => n % 2 === 0); // number[]

// 📝 GHI NHỚ: Generic classes create TYPE-SAFE containers!
```

#### **🔗 GENERIC INTERFACES:**

```typescript
// 🎯 GENERIC INTERFACE định nghĩa contract
interface Repository<T> {
  save(entity: T): T;
  findById(id: string): T | null;
  findAll(): T[];
  delete(id: string): boolean;
}

// ✅ IMPLEMENTATION cho specific type
interface User {
  id: string;
  name: string;
  email: string;
}

class UserRepository implements Repository<User> {
  private users: User[] = [];

  save(user: User): User {
    const existingIndex = this.users.findIndex(u => u.id === user.id);
    if (existingIndex >= 0) {
      this.users[existingIndex] = user; // Update
    } else {
      this.users.push(user); // Create
    }
    return user;
  }

  findById(id: string): User | null {
    return this.users.find(u => u.id === id) || null;
  }

  findAll(): User[] {
    return [...this.users];
  }

  delete(id: string): boolean {
    const index = this.users.findIndex(u => u.id === id);
    if (index >= 0) {
      this.users.splice(index, 1);
      return true;
    }
    return false;
  }
}

// Usage
const userRepo = new UserRepository();
const user = userRepo.save({ id: "1", name: "John", email: "john@email.com" });
```

#### **⚡ ADVANCED GENERIC PATTERNS:**

**1. Multiple Type Parameters:**
```typescript
// 🎯 MULTIPLE GENERICS for key-value pairs
class KeyValueStore<K, V> {
  private items = new Map<K, V>();

  set(key: K, value: V): void {
    this.items.set(key, value);
  }

  get(key: K): V | undefined {
    return this.items.get(key);
  }

  has(key: K): boolean {
    return this.items.has(key);
  }

  entries(): [K, V][] {
    return Array.from(this.items.entries());
  }
}

// Usage
const stringToNumberStore = new KeyValueStore<string, number>();
stringToNumberStore.set("age", 25);
stringToNumberStore.set("height", 175);

const userToPermissionStore = new KeyValueStore<User, string[]>();
userToPermissionStore.set(user, ["read", "write"]);

// 📝 GHI NHỚ: Use multiple type parameters for RELATED but DIFFERENT types!
```

**2. Generic Constraints:**
```typescript
// 🎯 CONSTRAINTS limit generic types
interface Lengthwise {
  length: number;
}

// ✅ T must have length property
function logLength<T extends Lengthwise>(arg: T): T {
  console.log(`Length: ${arg.length}`);
  return arg;
}

// Usage
logLength("hello"); // ✅ string has length
logLength([1, 2, 3]); // ✅ array has length
logLength({ length: 10, value: "test" }); // ✅ object with length

// logLength(123); // ❌ Error: number doesn't have length

// 🎯 CONSTRAINT with keyof
function getProperty<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key]; // ✅ Type-safe property access
}

// Usage
const person = { name: "John", age: 30, email: "john@email.com" };
const name = getProperty(person, "name"); // string
const age = getProperty(person, "age"); // number
// const invalid = getProperty(person, "salary"); // ❌ Error: salary doesn't exist

// 📝 GHI NHỚ: Constraints ensure generics meet MINIMUM REQUIREMENTS!
```

**3. Conditional Types:**
```typescript
// 🎯 CONDITIONAL TYPES với generics
type ApiResponse<T> = T extends string
  ? { message: T }
  : T extends number
    ? { count: T }
    : { data: T };

// Usage
type StringResponse = ApiResponse<string>; // { message: string }
type NumberResponse = ApiResponse<number>; // { count: number }
type UserResponse = ApiResponse<User>; // { data: User }

// 🎯 UTILITY TYPE với conditional generics
type NonNullable<T> = T extends null | undefined ? never : T;

type SafeString = NonNullable<string | null>; // string
type SafeNumber = NonNullable<number | undefined>; // number
```

#### **🎯 REAL-WORLD EXAMPLES:**

**1. Generic API Client:**
```typescript
// 🎯 TYPE-SAFE API CLIENT
interface ApiResponse<T> {
  data: T;
  status: number;
  message: string;
}

class ApiClient {
  private baseUrl: string;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  // ✅ Generic GET method
  async get<T>(endpoint: string): Promise<ApiResponse<T>> {
    const response = await fetch(`${this.baseUrl}${endpoint}`);
    const data = await response.json();

    return {
      data: data as T, // Type assertion (in real app, add validation)
      status: response.status,
      message: response.statusText
    };
  }

  // ✅ Generic POST method
  async post<TRequest, TResponse>(
    endpoint: string,
    body: TRequest
  ): Promise<ApiResponse<TResponse>> {
    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body)
    });

    const data = await response.json();
    return {
      data: data as TResponse,
      status: response.status,
      message: response.statusText
    };
  }
}

// Usage
const apiClient = new ApiClient('https://api.example.com');

// ✅ Type-safe API calls
interface User {
  id: number;
  name: string;
  email: string;
}

interface CreateUserRequest {
  name: string;
  email: string;
}

// GET request
const usersResponse = await apiClient.get<User[]>('/users');
const users: User[] = usersResponse.data; // ✅ Typed as User[]

// POST request
const newUserResponse = await apiClient.post<CreateUserRequest, User>(
  '/users',
  { name: 'John', email: 'john@email.com' }
);
const newUser: User = newUserResponse.data; // ✅ Typed as User
```

**2. Generic Event Emitter:**
```typescript
// 🎯 TYPE-SAFE EVENT EMITTER
type EventMap = Record<string, any>;

class TypedEventEmitter<T extends EventMap> {
  private listeners: {
    [K in keyof T]?: Array<(data: T[K]) => void>;
  } = {};

  // ✅ Type-safe event registration
  on<K extends keyof T>(event: K, listener: (data: T[K]) => void): void {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    this.listeners[event]!.push(listener);
  }

  // ✅ Type-safe event emission
  emit<K extends keyof T>(event: K, data: T[K]): void {
    const eventListeners = this.listeners[event];
    if (eventListeners) {
      eventListeners.forEach(listener => listener(data));
    }
  }

  // ✅ Remove listener
  off<K extends keyof T>(event: K, listener: (data: T[K]) => void): void {
    const eventListeners = this.listeners[event];
    if (eventListeners) {
      const index = eventListeners.indexOf(listener);
      if (index >= 0) {
        eventListeners.splice(index, 1);
      }
    }
  }
}

// Define event types
interface UserEvents {
  'user:created': { id: number; name: string };
  'user:updated': { id: number; changes: Partial<User> };
  'user:deleted': { id: number };
}

// Usage
const userEventEmitter = new TypedEventEmitter<UserEvents>();

// ✅ Type-safe listeners
userEventEmitter.on('user:created', (data) => {
  console.log(`User created: ${data.name} (${data.id})`); // ✅ data is typed
});

userEventEmitter.on('user:updated', (data) => {
  console.log(`User ${data.id} updated:`, data.changes); // ✅ data is typed
});

// ✅ Type-safe emission
userEventEmitter.emit('user:created', { id: 1, name: 'John' }); // ✅ Correct type
// userEventEmitter.emit('user:created', { name: 'John' }); // ❌ Error: missing id

// 📝 GHI NHỚ: Generic EventEmitter provides COMPILE-TIME safety for events!
```

**3. Generic State Management:**
```typescript
// 🎯 SIMPLE GENERIC STATE STORE
class Store<T> {
  private state: T;
  private listeners: Array<(state: T) => void> = [];

  constructor(initialState: T) {
    this.state = initialState;
  }

  // ✅ Get current state
  getState(): T {
    return this.state;
  }

  // ✅ Update state với type safety
  setState(updater: (currentState: T) => T): void {
    this.state = updater(this.state);
    this.notifyListeners();
  }

  // ✅ Subscribe to state changes
  subscribe(listener: (state: T) => void): () => void {
    this.listeners.push(listener);

    // Return unsubscribe function
    return () => {
      const index = this.listeners.indexOf(listener);
      if (index >= 0) {
        this.listeners.splice(index, 1);
      }
    };
  }

  private notifyListeners(): void {
    this.listeners.forEach(listener => listener(this.state));
  }
}

// Define app state type
interface AppState {
  user: User | null;
  theme: 'light' | 'dark';
  notifications: string[];
}

// Usage
const appStore = new Store<AppState>({
  user: null,
  theme: 'light',
  notifications: []
});

// ✅ Type-safe state updates
appStore.setState(state => ({
  ...state,
  user: { id: 1, name: 'John', email: 'john@email.com' }
}));

appStore.setState(state => ({
  ...state,
  theme: 'dark' // ✅ TypeScript ensures valid theme values
}));

// ✅ Type-safe subscriptions
const unsubscribe = appStore.subscribe(state => {
  console.log('Current user:', state.user?.name); // ✅ Optional chaining
  console.log('Theme:', state.theme); // ✅ Typed as 'light' | 'dark'
});

// Cleanup
unsubscribe();
```

#### **💡 INTERVIEW INSIGHTS:**

**🔹 WHY USE GENERICS:**
- ✅ **TYPE SAFETY** without sacrificing flexibility
- ✅ **CODE REUSE** across different types
- ✅ **BETTER IntelliSense** và autocomplete
- ✅ **COMPILE-TIME ERROR DETECTION**
- ✅ **SELF-DOCUMENTING CODE**

**🔹 GENERIC NAMING CONVENTIONS:**
```typescript
// Common conventions:
T = Type (most common)
K = Key
V = Value
U = Second type
E = Element
R = Return type
P = Props (React context)

// Examples:
Map<K, V>        // Key-Value mapping
Array<T>         // Array of Type T
Promise<T>       // Promise resolving to Type T
Record<K, V>     // Record with Key K and Value V
```

**🔹 PERFORMANCE:**
- Generics = **COMPILE TIME** feature only
- **NO RUNTIME OVERHEAD** - types are erased
- **Better OPTIMIZATION** due to type information

**🔹 COMMON MISTAKES:**
```typescript
// ❌ OVER-CONSTRAINING
function processItem<T extends object>(item: T): T {
  // What if T could be primitive?
}

// ✅ BETTER
function processItem<T>(item: T): T {
  // More flexible
}

// ❌ UNNECESSARY GENERICS
function addNumbers<T extends number>(a: T, b: T): T {
  return (a + b) as T; // Type assertion needed - red flag!
}

// ✅ BETTER
function addNumbers(a: number, b: number): number {
  return a + b; // Simple và clear
}
```

#### **🚀 BEST PRACTICES:**

**📝 DO's:**
- ✅ Use **MEANINGFUL NAMES** cho type parameters
- ✅ Add **CONSTRAINTS** when needed
- ✅ **LEVERAGE TYPE INFERENCE** when possible
- ✅ Use generics for **REUSABLE COMPONENTS**

**📝 DON'Ts:**
- ❌ Don't **OVER-ENGINEER** với unnecessary generics
- ❌ Avoid **TOO MANY** type parameters (max 3-4)
- ❌ Don't use generics just for **TYPE ASSERTION**
- ❌ Avoid **COMPLEX CONDITIONAL TYPES** without good reason

**GHI NHỞ:** Generics = **FLEXIBLE TYPES** that maintain **TYPE SAFETY**! Perfect for building **REUSABLE và TYPE-SAFE** libraries và frameworks! 🎯

---

### TS9: Static Typing, `typeof`, `keyof` - Advanced Type Operations?

**Trả lời:**

Đây là **ADVANCED TYPE OPERATIONS** trong TypeScript giúp bạn tạo **DYNAMIC TYPES** và **TYPE-SAFE CODE** từ existing types và values. Đây là **NEXT LEVEL** type manipulation!

#### **🔥 FUNDAMENTAL CONCEPTS:**

**Static Typing + Runtime Reflection = POWERFUL TYPE SYSTEM**

```typescript
// 🎯 STATIC TYPING: Types known at compile time
const user = {
  id: 1,
  name: "John",
  email: "john@email.com",
  age: 30
};

// ✅ TypeScript KNOWS the exact shape
type UserType = typeof user;
// Equivalent to: { id: number; name: string; email: string; age: number; }

type UserKeys = keyof typeof user;
// Equivalent to: "id" | "name" | "email" | "age"

// 📝 GHI NHỚ: typeof = value to type, keyof = type to union of keys
```

#### **🛠️ `typeof` OPERATOR:**

**1. Basic typeof Usage:**
```typescript
// 🎯 EXTRACT TYPE from values
const config = {
  apiUrl: "https://api.example.com",
  timeout: 5000,
  retries: 3,
  enableLogging: true
} as const; // ✅ as const for literal types

// ✅ Extract type from value
type Config = typeof config;
// Result: {
//   readonly apiUrl: "https://api.example.com";
//   readonly timeout: 5000;
//   readonly retries: 3;
//   readonly enableLogging: true;
// }

// 🎯 FUNCTION TYPE extraction
function calculateTotal(price: number, tax: number): number {
  return price + (price * tax);
}

type CalculateFunction = typeof calculateTotal;
// Result: (price: number, tax: number) => number

// ✅ Use extracted function type
const myCalculator: CalculateFunction = (p, t) => p * (1 + t);
```

**2. Advanced typeof Patterns:**
```typescript
// 🎯 COMPLEX OBJECT TYPES
const apiEndpoints = {
  users: {
    list: "/api/users",
    create: "/api/users",
    update: (id: number) => `/api/users/${id}`,
    delete: (id: number) => `/api/users/${id}`
  },
  posts: {
    list: "/api/posts",
    byUser: (userId: number) => `/api/posts?user=${userId}`
  }
} as const;

type ApiEndpoints = typeof apiEndpoints;
// Result: {
//   readonly users: {
//     readonly list: "/api/users";
//     readonly create: "/api/users";
//     readonly update: (id: number) => string;
//     readonly delete: (id: number) => string;
//   };
//   readonly posts: {
//     readonly list: "/api/posts";
//     readonly byUser: (userId: number) => string;
//   };
// }

// ✅ Extract specific nested types
type UserEndpoints = typeof apiEndpoints.users;
type UpdateFunction = typeof apiEndpoints.users.update;

// 📝 GHI NHỚ: typeof preserves function signatures và nested structures
```

#### **🔑 `keyof` OPERATOR:**

**1. Basic keyof Usage:**
```typescript
// 🎯 EXTRACT KEYS as union type
interface User {
  id: number;
  name: string;
  email: string;
  createdAt: Date;
}

type UserKeys = keyof User;
// Result: "id" | "name" | "email" | "createdAt"

// ✅ Type-safe property access
function getUserProperty<K extends keyof User>(user: User, key: K): User[K] {
  return user[key]; // ✅ TypeScript knows exact return type
}

const user: User = {
  id: 1,
  name: "John",
  email: "john@email.com",
  createdAt: new Date()
};

const userName = getUserProperty(user, "name"); // string
const userId = getUserProperty(user, "id"); // number
const userDate = getUserProperty(user, "createdAt"); // Date
// const invalid = getUserProperty(user, "invalid"); // ❌ Error

// 📝 GHI NHỚ: keyof creates LITERAL UNION TYPES from object keys
```

**2. Advanced keyof Patterns:**
```typescript
// 🎯 CONDITIONAL KEYOF
type StringKeys<T> = {
  [K in keyof T]: T[K] extends string ? K : never;
}[keyof T];

type NumberKeys<T> = {
  [K in keyof T]: T[K] extends number ? K : never;
}[keyof T];

interface MixedData {
  id: number;
  name: string;
  age: number;
  email: string;
  isActive: boolean;
}

type StringProperties = StringKeys<MixedData>; // "name" | "email"
type NumberProperties = NumberKeys<MixedData>; // "id" | "age"

// ✅ Type-safe getters with filtering
function getStringProperty<T, K extends StringKeys<T>>(
  obj: T,
  key: K
): T[K] {
  return obj[key];
}

const data: MixedData = {
  id: 1,
  name: "John",
  age: 30,
  email: "john@email.com",
  isActive: true
};

const name = getStringProperty(data, "name"); // ✅ string
const email = getStringProperty(data, "email"); // ✅ string
// const age = getStringProperty(data, "age"); // ❌ Error: age is number
```

#### **⚡ ADVANCED COMBINATIONS:**

**1. Dynamic Object Creation:**
```typescript
// 🎯 TYPE-SAFE OBJECT BUILDERS
const formSchema = {
  username: { type: "string", required: true, minLength: 3 },
  email: { type: "email", required: true },
  age: { type: "number", required: false, min: 0, max: 120 },
  password: { type: "password", required: true, minLength: 8 }
} as const;

type FormSchema = typeof formSchema;
type FormFields = keyof FormSchema;

// ✅ Extract form data type from schema
type FormData = {
  [K in FormFields]: FormSchema[K]["required"] extends true
    ? string
    : string | undefined;
};

// Result: {
//   username: string;
//   email: string;
//   age: string | undefined;
//   password: string;
// }

// ✅ Type-safe form validation
function validateField<K extends FormFields>(
  field: K,
  value: string
): { valid: boolean; error?: string } {
  const fieldSchema = formSchema[field];

  if (fieldSchema.required && !value) {
    return { valid: false, error: `${field} is required` };
  }

  if ("minLength" in fieldSchema && value.length < fieldSchema.minLength) {
    return { valid: false, error: `${field} must be at least ${fieldSchema.minLength} characters` };
  }

  return { valid: true };
}

// Usage
const usernameValidation = validateField("username", "jo");
// { valid: false, error: "username must be at least 3 characters" }
```

**2. API Response Mapping:**
```typescript
// 🎯 TYPE-SAFE API RESPONSE HANDLING
const apiRoutes = {
  "/users": { method: "GET", response: [] as User[] },
  "/users/:id": { method: "GET", response: {} as User },
  "/posts": { method: "GET", response: [] as Post[] },
  "/auth/login": { method: "POST", response: {} as { token: string; user: User } }
} as const;

type ApiRoutes = typeof apiRoutes;
type ApiPaths = keyof ApiRoutes;

// ✅ Extract response types from routes
type ApiResponseMap = {
  [K in ApiPaths]: ApiRoutes[K]["response"];
};

// Result: {
//   "/users": User[];
//   "/users/:id": User;
//   "/posts": Post[];
//   "/auth/login": { token: string; user: User };
// }

// ✅ Type-safe API client
async function apiCall<P extends ApiPaths>(
  path: P
): Promise<ApiResponseMap[P]> {
  const route = apiRoutes[path];

  // Simulate API call
  const response = await fetch(path as string);
  const data = await response.json();

  return data as ApiResponseMap[P]; // ✅ Correctly typed return
}

// Usage với perfect type inference
const users = await apiCall("/users"); // User[]
const user = await apiCall("/users/:id"); // User
const loginResult = await apiCall("/auth/login"); // { token: string; user: User }
```

**3. State Management Type Safety:**
```typescript
// 🎯 REDUX-STYLE TYPE-SAFE ACTIONS
const actionCreators = {
  setUser: (user: User) => ({ type: "SET_USER" as const, payload: user }),
  setLoading: (loading: boolean) => ({ type: "SET_LOADING" as const, payload: loading }),
  addPost: (post: Post) => ({ type: "ADD_POST" as const, payload: post }),
  removePost: (id: number) => ({ type: "REMOVE_POST" as const, payload: id })
};

type ActionCreators = typeof actionCreators;
type ActionCreatorKeys = keyof ActionCreators;

// ✅ Extract all possible action types
type Actions = ReturnType<ActionCreators[ActionCreatorKeys]>;
// Result: Union of all action types

// ✅ Type-safe reducer
function appReducer(state: AppState, action: Actions): AppState {
  switch (action.type) {
    case "SET_USER":
      return { ...state, user: action.payload }; // ✅ payload is User
    case "SET_LOADING":
      return { ...state, loading: action.payload }; // ✅ payload is boolean
    case "ADD_POST":
      return { ...state, posts: [...state.posts, action.payload] }; // ✅ payload is Post
    case "REMOVE_POST":
      return {
        ...state,
        posts: state.posts.filter(p => p.id !== action.payload) // ✅ payload is number
      };
    default:
      return state;
  }
}

// ✅ Type-safe action dispatcher
function createDispatcher<K extends ActionCreatorKeys>(
  reducerDispatch: (action: Actions) => void
) {
  return {
    [K in ActionCreatorKeys]: (...args: Parameters<ActionCreators[K]>) => {
      const action = actionCreators[K](...args);
      reducerDispatch(action);
    }
  } as {
    [K in ActionCreatorKeys]: ActionCreators[K]
  };
}
```

#### **🎯 REAL-WORLD PATTERNS:**

**1. Configuration Management:**
```typescript
// 🎯 ENVIRONMENT-AWARE CONFIG
const baseConfig = {
  app: {
    name: "MyApp",
    version: "1.0.0"
  },
  api: {
    baseUrl: "https://api.example.com",
    timeout: 5000
  },
  features: {
    darkMode: true,
    analytics: true,
    notifications: false
  }
} as const;

type BaseConfig = typeof baseConfig;
type ConfigPaths = keyof BaseConfig;
type FeatureFlags = keyof BaseConfig["features"];

// ✅ Type-safe config updater
function updateConfig<
  TPath extends ConfigPaths,
  TKey extends keyof BaseConfig[TPath]
>(
  path: TPath,
  key: TKey,
  value: BaseConfig[TPath][TKey]
): void {
  (baseConfig[path] as any)[key] = value; // Type-safe update
}

// Usage
updateConfig("features", "darkMode", false); // ✅ boolean expected
updateConfig("api", "timeout", 3000); // ✅ number expected
// updateConfig("features", "darkMode", "invalid"); // ❌ Error: string not assignable to boolean

// ✅ Feature flag checker
function isFeatureEnabled<T extends FeatureFlags>(feature: T): boolean {
  return baseConfig.features[feature];
}

if (isFeatureEnabled("analytics")) {
  // Analytics code
}
```

**2. Database Query Builder:**
```typescript
// 🎯 TYPE-SAFE QUERY BUILDER
const tableSchemas = {
  users: {
    id: "number",
    name: "string",
    email: "string",
    createdAt: "date"
  },
  posts: {
    id: "number",
    title: "string",
    content: "string",
    authorId: "number",
    publishedAt: "date"
  }
} as const;

type TableSchemas = typeof tableSchemas;
type TableNames = keyof TableSchemas;

// ✅ Type-safe column selector
function select<
  TTable extends TableNames,
  TColumns extends (keyof TableSchemas[TTable])[]
>(
  table: TTable,
  columns: TColumns
): Pick<TableSchemas[TTable], TColumns[number]> {
  // Query building logic here
  return {} as Pick<TableSchemas[TTable], TColumns[number]>;
}

// Usage với perfect type inference
const userQuery = select("users", ["id", "name", "email"]);
// Type: Pick<{ id: "number"; name: "string"; email: "string"; createdAt: "date" }, "id" | "name" | "email">

const postQuery = select("posts", ["title", "publishedAt"]);
// Type: Pick<{ id: "number"; title: "string"; content: "string"; authorId: "number"; publishedAt: "date" }, "title" | "publishedAt">

// ✅ Type-safe where clause builder
function where<
  TTable extends TableNames,
  TColumn extends keyof TableSchemas[TTable]
>(
  table: TTable,
  column: TColumn,
  value: TableSchemas[TTable][TColumn]
): void {
  // WHERE clause logic
}

// Usage
where("users", "id", 1); // ✅ number expected
where("users", "name", "John"); // ✅ string expected
// where("users", "id", "invalid"); // ❌ Error: string not assignable to number
```

#### **💡 INTERVIEW INSIGHTS:**

**🔹 STATIC TYPING BENEFITS:**
- ✅ **COMPILE-TIME** error detection
- ✅ **INTELLISENSE** và autocomplete
- ✅ **REFACTORING SAFETY** - renaming variables/properties
- ✅ **SELF-DOCUMENTING** code
- ✅ **PERFORMANCE** - no runtime type checking needed

**🔹 TYPEOF vs KEYOF:**

| Operator | **Input** | **Output** | **Use Case** |
|----------|-----------|------------|-------------|
| `typeof` | **Value** | **Type** | Extract type from runtime value |
| `keyof` | **Type** | **Union of Keys** | Get property names as literal types |

**🔹 COMMON PATTERNS:**
```typescript
// Pattern 1: typeof + keyof combination
const obj = { a: 1, b: "hello" };
type ObjKeys = keyof typeof obj; // "a" | "b"

// Pattern 2: Generic type-safe property access
function getProp<T, K extends keyof T>(obj: T, key: K): T[K] {
  return obj[key];
}

// Pattern 3: Conditional type với keyof
type StringKeys<T> = {
  [K in keyof T]: T[K] extends string ? K : never;
}[keyof T];
```

**🔹 PERFORMANCE:**
- **NO RUNTIME OVERHEAD** - all operations compile-time only
- **Better OPTIMIZATION** - TypeScript compiler can optimize better
- **TREE SHAKING** - unused properties can be eliminated

#### **🚀 ADVANCED USE CASES:**

**1. Type-Safe Event System:**
```typescript
// 🎯 EVENT SYSTEM với static typing
const eventMap = {
  "user:login": (data: { userId: number; timestamp: Date }) => {},
  "user:logout": (data: { userId: number }) => {},
  "post:created": (data: { postId: number; authorId: number }) => {},
  "post:deleted": (data: { postId: number }) => {}
} as const;

type EventMap = typeof eventMap;
type EventNames = keyof EventMap;

class TypedEventEmitter {
  private listeners: {
    [K in EventNames]?: Array<Parameters<EventMap[K]>[0]>
  } = {};

  on<K extends EventNames>(
    event: K,
    callback: EventMap[K]
  ): void {
    if (!this.listeners[event]) {
      this.listeners[event] = [];
    }
    (this.listeners[event] as any[]).push(callback);
  }

  emit<K extends EventNames>(
    event: K,
    data: Parameters<EventMap[K]>[0]
  ): void {
    const callbacks = this.listeners[event];
    if (callbacks) {
      callbacks.forEach(callback => callback(data));
    }
  }
}

// Usage với full type safety
const emitter = new TypedEventEmitter();

emitter.on("user:login", (data) => {
  console.log(`User ${data.userId} logged in at ${data.timestamp}`);
  // ✅ data is correctly typed as { userId: number; timestamp: Date }
});

emitter.emit("user:login", { userId: 123, timestamp: new Date() }); // ✅ Correct
// emitter.emit("user:login", { userId: "123" }); // ❌ Error: string not assignable to number
```

**2. Form Builder với Type Safety:**
```typescript
// 🎯 FORM BUILDER system
const formFields = {
  textInput: { type: "text", validation: (v: string) => v.length > 0 },
  emailInput: { type: "email", validation: (v: string) => /\S+@\S+\.\S+/.test(v) },
  numberInput: { type: "number", validation: (v: number) => !isNaN(v) },
  selectInput: {
    type: "select",
    options: ["option1", "option2", "option3"] as const,
    validation: (v: string) => v.length > 0
  }
} as const;

type FormFields = typeof formFields;
type FieldNames = keyof FormFields;

// ✅ Dynamic form type generation
type FormSchema<T extends Record<string, FieldNames>> = {
  [K in keyof T]: T[K] extends FieldNames
    ? FormFields[T[K]] extends { type: "number" }
      ? number
      : FormFields[T[K]] extends { type: "select", options: readonly any[] }
        ? FormFields[T[K]]["options"][number]
        : string
    : never;
};

// Usage
const myFormConfig = {
  username: "textInput",
  email: "emailInput",
  age: "numberInput",
  country: "selectInput"
} as const;

type MyFormData = FormSchema<typeof myFormConfig>;
// Result: {
//   username: string;
//   email: string;
//   age: number;
//   country: "option1" | "option2" | "option3";
// }

// ✅ Type-safe form validator
function validateForm<T extends Record<string, FieldNames>>(
  config: T,
  data: FormSchema<T>
): { valid: boolean; errors: Partial<Record<keyof T, string>> } {
  const errors: Partial<Record<keyof T, string>> = {};

  for (const [fieldName, fieldType] of Object.entries(config)) {
    const field = formFields[fieldType as FieldNames];
    const value = data[fieldName as keyof T];

    if (!field.validation(value as any)) {
      errors[fieldName as keyof T] = `Invalid ${fieldName}`;
    }
  }

  return {
    valid: Object.keys(errors).length === 0,
    errors
  };
}
```

#### **🎯 DECISION FRAMEWORK:**

```
❓ Need to extract type from existing value?
   └─ Use `typeof`

❓ Need to get keys of a type as union?
   └─ Use `keyof`

❓ Need both operations combined?
   └─ Use `keyof typeof value`

❓ Need conditional type based on properties?
   └─ Use mapped types với `keyof`

❓ Need type-safe property access?
   └─ Use generics với `keyof` constraint
```

**📝 GOLDEN RULES:**
1. **typeof** = convert runtime VALUES to compile-time TYPES
2. **keyof** = extract KEYS from types as literal unions
3. **Combine them** for maximum type safety
4. **Use generics** với keyof constraints for reusable type-safe functions
5. **as const** để preserve literal types when using typeof

**GHI NHỚ:**
- `typeof value` = **VALUE → TYPE**
- `keyof Type` = **TYPE → KEY UNION**
- `keyof typeof value` = **VALUE → KEY UNION**

**INTERVIEW TIP:** Demonstrate knowledge của advanced type operations và how they enable **RUNTIME-SAFE** code với **COMPILE-TIME** guarantees! 🎯

---

### TS10: OOP trong TypeScript - Abstract Class, Implement, Extend?

**Trả lời:**

TypeScript mang **FULL OBJECT-ORIENTED PROGRAMMING** vào JavaScript với **STRONG TYPING**! Đây là **CORE CONCEPTS** mà mọi Senior Developer cần nắm vững.

#### **🔥 FUNDAMENTAL OOP CONCEPTS:**

**OOP in TypeScript = Classes + Inheritance + Polymorphism + Encapsulation + Abstraction**

```typescript
// 🎯 BASIC CLASS STRUCTURE
class Animal {
  // ✅ ENCAPSULATION: Private, Protected, Public
  private id: number;           // ❌ Chỉ class này access được
  protected name: string;       // ✅ Class này + subclasses
  public species: string;       // ✅ Mọi nơi đều access được

  constructor(id: number, name: string, species: string) {
    this.id = id;
    this.name = name;
    this.species = species;
  }

  // ✅ PUBLIC METHOD
  public makeSound(): string {
    return "Some generic animal sound";
  }

  // ✅ PROTECTED METHOD (for subclasses)
  protected getName(): string {
    return this.name;
  }

  // ✅ PRIVATE METHOD (internal only)
  private generateId(): number {
    return Math.random() * 1000;
  }
}

// 📝 GHI NHỚ:
// private = chỉ class hiện tại
// protected = class hiện tại + subclasses
// public = mọi nơi (default)
```

#### **🏗️ INHERITANCE với EXTENDS:**

```typescript
// 🎯 EXTENDS: Class inheritance
class Dog extends Animal {
  private breed: string;

  constructor(id: number, name: string, breed: string) {
    super(id, name, "Canine"); // ✅ Call parent constructor
    this.breed = breed;
  }

  // ✅ OVERRIDE parent method
  public makeSound(): string {
    return "Woof! Woof!";
  }

  // ✅ ACCESS protected member từ parent
  public introduce(): string {
    return `I'm ${this.getName()}, a ${this.breed} dog`; // ✅ getName() is protected
  }

  // ✅ NEW method specific to Dog
  public fetch(item: string): string {
    return `${this.getName()} is fetching ${item}`;
  }

  // ✅ GETTER/SETTER pattern
  get breedInfo(): string {
    return this.breed;
  }

  set breedInfo(newBreed: string) {
    if (newBreed.length > 0) {
      this.breed = newBreed;
    }
  }
}

// Usage
const myDog = new Dog(1, "Buddy", "Golden Retriever");
console.log(myDog.makeSound()); // "Woof! Woof!" (overridden)
console.log(myDog.introduce()); // "I'm Buddy, a Golden Retriever dog"
console.log(myDog.species); // "Canine" (public property)
// console.log(myDog.name); // ❌ Error: protected property
// console.log(myDog.id); // ❌ Error: private property

// 📝 GHI NHỚ: extends creates IS-A relationship (Dog IS AN Animal)
```

#### **📋 INTERFACES với IMPLEMENTS:**

```typescript
// 🎯 INTERFACES: Define contracts
interface Flyable {
  maxAltitude: number;
  fly(): string;
  land(): string;
}

interface Swimmable {
  maxDepth: number;
  swim(): string;
  dive(depth: number): string;
}

// ✅ SINGLE INTERFACE implementation
class Bird extends Animal implements Flyable {
  maxAltitude: number;

  constructor(id: number, name: string, maxAltitude: number) {
    super(id, name, "Avian");
    this.maxAltitude = maxAltitude;
  }

  // ✅ MUST implement interface methods
  fly(): string {
    return `${this.getName()} is flying up to ${this.maxAltitude}m`;
  }

  land(): string {
    return `${this.getName()} is landing safely`;
  }

  // ✅ Override parent method
  makeSound(): string {
    return "Tweet! Tweet!";
  }
}

// ✅ MULTIPLE INTERFACES implementation
class Duck extends Animal implements Flyable, Swimmable {
  maxAltitude: number;
  maxDepth: number;

  constructor(id: number, name: string) {
    super(id, name, "Waterfowl");
    this.maxAltitude = 100; // Ducks don't fly very high
    this.maxDepth = 5; // Shallow diving
  }

  // ✅ Implement Flyable
  fly(): string {
    return `${this.getName()} is flying low over water`;
  }

  land(): string {
    return `${this.getName()} is landing on water`;
  }

  // ✅ Implement Swimmable
  swim(): string {
    return `${this.getName()} is swimming gracefully`;
  }

  dive(depth: number): string {
    if (depth > this.maxDepth) {
      return `${this.getName()} can't dive that deep!`;
    }
    return `${this.getName()} is diving to ${depth}m`;
  }

  makeSound(): string {
    return "Quack! Quack!";
  }
}

// Usage
const eagle = new Bird(2, "Eagle", 3000);
console.log(eagle.fly()); // "Eagle is flying up to 3000m"

const duck = new Duck(3, "Donald");
console.log(duck.fly()); // "Donald is flying low over water"
console.log(duck.swim()); // "Donald is swimming gracefully"
console.log(duck.dive(3)); // "Donald is diving to 3m"

// 📝 GHI NHỚ: implements creates CAN-DO relationship (Duck CAN FLY and CAN SWIM)
```

#### **🏛️ ABSTRACT CLASSES:**

```typescript
// 🎯 ABSTRACT CLASS: Cannot be instantiated directly
abstract class Vehicle {
  protected brand: string;
  protected model: string;
  protected year: number;

  constructor(brand: string, model: string, year: number) {
    this.brand = brand;
    this.model = model;
    this.year = year;
  }

  // ✅ CONCRETE METHOD (có implementation)
  getInfo(): string {
    return `${this.year} ${this.brand} ${this.model}`;
  }

  // ✅ ABSTRACT METHOD (must be implemented by subclasses)
  abstract start(): string;
  abstract stop(): string;
  abstract getMaxSpeed(): number;

  // ✅ CONCRETE METHOD sử dụng abstract method
  race(): string {
    const startMsg = this.start();
    const maxSpeed = this.getMaxSpeed();
    return `${startMsg} - Racing at max speed: ${maxSpeed} km/h`;
  }
}

// ✅ CONCRETE implementation của abstract class
class Car extends Vehicle {
  private engineType: string;

  constructor(brand: string, model: string, year: number, engineType: string) {
    super(brand, model, year);
    this.engineType = engineType;
  }

  // ✅ MUST implement abstract methods
  start(): string {
    return `${this.getInfo()} engine started with ${this.engineType}`;
  }

  stop(): string {
    return `${this.getInfo()} engine stopped`;
  }

  getMaxSpeed(): number {
    return this.engineType === "electric" ? 200 : 180;
  }

  // ✅ Additional car-specific methods
  openTrunk(): string {
    return `${this.getInfo()} trunk opened`;
  }
}

class Motorcycle extends Vehicle {
  private hasWindshield: boolean;

  constructor(brand: string, model: string, year: number, hasWindshield: boolean) {
    super(brand, model, year);
    this.hasWindshield = hasWindshield;
  }

  start(): string {
    return `${this.getInfo()} motorcycle engine roared to life`;
  }

  stop(): string {
    return `${this.getInfo()} motorcycle engine turned off`;
  }

  getMaxSpeed(): number {
    return this.hasWindshield ? 250 : 200; // Windshield allows higher speed
  }

  wheelie(): string {
    return `${this.getInfo()} doing a wheelie!`;
  }
}

// Usage
// const vehicle = new Vehicle("Generic", "Model", 2024); // ❌ Error: Cannot instantiate abstract class

const car = new Car("Tesla", "Model 3", 2024, "electric");
console.log(car.start()); // "2024 Tesla Model 3 engine started with electric"
console.log(car.race()); // "2024 Tesla Model 3 engine started with electric - Racing at max speed: 200 km/h"

const bike = new Motorcycle("Yamaha", "R1", 2024, true);
console.log(bike.start()); // "2024 Yamaha R1 motorcycle engine roared to life"
console.log(bike.wheelie()); // "2024 Yamaha R1 doing a wheelie!"

// 📝 GHI NHỚ: Abstract class = PARTIAL implementation + ENFORCED contract
```

#### **⚡ ADVANCED OOP PATTERNS:**

**1. Method Overloading:**
```typescript
// 🎯 METHOD OVERLOADING với different signatures
class Calculator {
  // ✅ OVERLOAD SIGNATURES
  add(a: number, b: number): number;
  add(a: string, b: string): string;
  add(a: number[], b: number[]): number[];

  // ✅ IMPLEMENTATION signature
  add(a: any, b: any): any {
    if (typeof a === "number" && typeof b === "number") {
      return a + b;
    }

    if (typeof a === "string" && typeof b === "string") {
      return a + b;
    }

    if (Array.isArray(a) && Array.isArray(b)) {
      return [...a, ...b];
    }

    throw new Error("Unsupported types for add operation");
  }
}

const calc = new Calculator();
console.log(calc.add(1, 2)); // 3 (number)
console.log(calc.add("Hello", " World")); // "Hello World" (string)
console.log(calc.add([1, 2], [3, 4])); // [1, 2, 3, 4] (array)
```

**2. Static Members:**
```typescript
// 🎯 STATIC MEMBERS: Belong to class, not instance
class MathUtils {
  // ✅ STATIC PROPERTY
  static readonly PI = 3.14159;
  private static instanceCount = 0;

  // ✅ INSTANCE PROPERTY
  private id: number;

  constructor() {
    MathUtils.instanceCount++;
    this.id = MathUtils.instanceCount;
  }

  // ✅ STATIC METHOD
  static circleArea(radius: number): number {
    return MathUtils.PI * radius * radius;
  }

  static getInstanceCount(): number {
    return MathUtils.instanceCount;
  }

  // ✅ INSTANCE METHOD
  getId(): number {
    return this.id;
  }
}

// Usage
console.log(MathUtils.PI); // 3.14159 (no instance needed)
console.log(MathUtils.circleArea(5)); // 78.53975 (static method)

const math1 = new MathUtils();
const math2 = new MathUtils();
console.log(MathUtils.getInstanceCount()); // 2
console.log(math1.getId()); // 1
console.log(math2.getId()); // 2

// 📝 GHI NHỚ: static = class-level, instance = object-level
```

**3. Abstract + Interface Combined:**
```typescript
// 🎯 COMBINING Abstract Class + Interface
interface Saveable {
  save(): Promise<boolean>;
  load(): Promise<boolean>;
}

interface Validatable {
  validate(): boolean;
  getErrors(): string[];
}

// ✅ ABSTRACT BASE với common functionality
abstract class Entity implements Saveable, Validatable {
  protected id: string;
  protected createdAt: Date;
  protected updatedAt: Date;

  constructor(id?: string) {
    this.id = id || this.generateId();
    this.createdAt = new Date();
    this.updatedAt = new Date();
  }

  // ✅ CONCRETE implementation
  private generateId(): string {
    return Math.random().toString(36).substr(2, 9);
  }

  // ✅ CONCRETE method
  protected touch(): void {
    this.updatedAt = new Date();
  }

  // ✅ ABSTRACT methods (must implement)
  abstract validate(): boolean;
  abstract getErrors(): string[];

  // ✅ DEFAULT implementation (có thể override)
  async save(): Promise<boolean> {
    if (!this.validate()) {
      console.log("Validation failed:", this.getErrors());
      return false;
    }

    this.touch();

    // Simulate API call
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(`${this.constructor.name} saved with ID: ${this.id}`);
        resolve(true);
      }, 100);
    });
  }

  async load(): Promise<boolean> {
    // Simulate loading from database
    return new Promise(resolve => {
      setTimeout(() => {
        console.log(`${this.constructor.name} loaded with ID: ${this.id}`);
        resolve(true);
      }, 100);
    });
  }
}

// ✅ CONCRETE implementation
class User extends Entity {
  private name: string;
  private email: string;
  private age: number;

  constructor(name: string, email: string, age: number, id?: string) {
    super(id);
    this.name = name;
    this.email = email;
    this.age = age;
  }

  // ✅ IMPLEMENT abstract methods
  validate(): boolean {
    return this.getErrors().length === 0;
  }

  getErrors(): string[] {
    const errors: string[] = [];

    if (!this.name || this.name.trim().length === 0) {
      errors.push("Name is required");
    }

    if (!this.email || !this.email.includes("@")) {
      errors.push("Valid email is required");
    }

    if (this.age < 0 || this.age > 150) {
      errors.push("Age must be between 0 and 150");
    }

    return errors;
  }

  // ✅ User-specific methods
  getProfile(): string {
    return `${this.name} (${this.email}) - Age: ${this.age}`;
  }

  // ✅ OVERRIDE save để add extra logic
  async save(): Promise<boolean> {
    console.log(`Saving user: ${this.getProfile()}`);
    return super.save(); // Call parent implementation
  }
}

// Usage
const user = new User("John Doe", "john@email.com", 30);

if (user.validate()) {
  await user.save(); // "Saving user: John Doe (john@email.com) - Age: 30"
} else {
  console.log("User validation failed:", user.getErrors());
}

const invalidUser = new User("", "invalid-email", -5);
console.log(invalidUser.getErrors());
// ["Name is required", "Valid email is required", "Age must be between 0 and 150"]
```

#### **🎯 REAL-WORLD EXAMPLE: Game Engine:**

```typescript
// 🎯 COMPLEX OOP SYSTEM: Game Engine
interface Drawable {
  draw(context: CanvasRenderingContext2D): void;
}

interface Updatable {
  update(deltaTime: number): void;
}

interface Collidable {
  getBounds(): Rectangle;
  onCollision(other: Collidable): void;
}

// ✅ UTILITY CLASSES
class Vector2 {
  constructor(public x: number = 0, public y: number = 0) {}

  add(other: Vector2): Vector2 {
    return new Vector2(this.x + other.x, this.y + other.y);
  }

  multiply(scalar: number): Vector2 {
    return new Vector2(this.x * scalar, this.y * scalar);
  }
}

class Rectangle {
  constructor(
    public x: number,
    public y: number,
    public width: number,
    public height: number
  ) {}

  intersects(other: Rectangle): boolean {
    return !(
      this.x + this.width < other.x ||
      other.x + other.width < this.x ||
      this.y + this.height < other.y ||
      other.y + other.height < this.y
    );
  }
}

// ✅ ABSTRACT BASE CLASS
abstract class GameObject implements Drawable, Updatable {
  protected position: Vector2;
  protected velocity: Vector2;
  protected size: Vector2;
  protected health: number;

  constructor(x: number, y: number, width: number, height: number) {
    this.position = new Vector2(x, y);
    this.velocity = new Vector2(0, 0);
    this.size = new Vector2(width, height);
    this.health = 100;
  }

  // ✅ CONCRETE methods
  update(deltaTime: number): void {
    // Update position based on velocity
    this.position = this.position.add(this.velocity.multiply(deltaTime));

    // Boundary checking
    this.checkBounds();

    // Call subclass-specific update
    this.onUpdate(deltaTime);
  }

  protected checkBounds(): void {
    // Simple boundary checking (screen edges)
    if (this.position.x < 0) this.position.x = 0;
    if (this.position.y < 0) this.position.y = 0;
  }

  takeDamage(amount: number): void {
    this.health -= amount;
    if (this.health <= 0) {
      this.onDestroy();
    }
  }

  // ✅ ABSTRACT methods (must implement)
  abstract draw(context: CanvasRenderingContext2D): void;
  abstract onUpdate(deltaTime: number): void;
  abstract onDestroy(): void;
}

// ✅ CONCRETE IMPLEMENTATIONS
class Player extends GameObject implements Collidable {
  private score: number = 0;
  private isInvulnerable: boolean = false;

  constructor(x: number, y: number) {
    super(x, y, 32, 32); // Player is 32x32 pixels
  }

  // ✅ Implement abstract methods
  draw(context: CanvasRenderingContext2D): void {
    context.fillStyle = this.isInvulnerable ? 'rgba(0, 255, 0, 0.5)' : 'green';
    context.fillRect(this.position.x, this.position.y, this.size.x, this.size.y);

    // Draw health bar
    context.fillStyle = 'red';
    context.fillRect(this.position.x, this.position.y - 10, this.size.x, 4);
    context.fillStyle = 'green';
    context.fillRect(this.position.x, this.position.y - 10, (this.size.x * this.health) / 100, 4);
  }

  onUpdate(deltaTime: number): void {
    // Handle input, special abilities, etc.
    this.handleInput();
  }

  onDestroy(): void {
    console.log(`Player destroyed! Final score: ${this.score}`);
  }

  // ✅ Implement Collidable
  getBounds(): Rectangle {
    return new Rectangle(this.position.x, this.position.y, this.size.x, this.size.y);
  }

  onCollision(other: Collidable): void {
    if (other instanceof Enemy && !this.isInvulnerable) {
      this.takeDamage(10);
      this.becomeInvulnerable(1000); // 1 second invulnerability
    } else if (other instanceof PowerUp) {
      this.score += (other as PowerUp).getValue();
    }
  }

  // ✅ Player-specific methods
  private handleInput(): void {
    // Keyboard input handling would go here
    // For demo, just show the concept
  }

  private becomeInvulnerable(duration: number): void {
    this.isInvulnerable = true;
    setTimeout(() => {
      this.isInvulnerable = false;
    }, duration);
  }

  moveUp(): void { this.velocity.y = -100; }
  moveDown(): void { this.velocity.y = 100; }
  moveLeft(): void { this.velocity.x = -100; }
  moveRight(): void { this.velocity.x = 100; }
  stop(): void { this.velocity = new Vector2(0, 0); }
}

class Enemy extends GameObject implements Collidable {
  private attackDamage: number;

  constructor(x: number, y: number, attackDamage: number = 20) {
    super(x, y, 24, 24); // Enemy is 24x24 pixels
    this.attackDamage = attackDamage;
    this.velocity = new Vector2(-50, 0); // Move left by default
  }

  draw(context: CanvasRenderingContext2D): void {
    context.fillStyle = 'red';
    context.fillRect(this.position.x, this.position.y, this.size.x, this.size.y);
  }

  onUpdate(deltaTime: number): void {
    // AI behavior - simple back and forth movement
    if (this.position.x <= 0 || this.position.x >= 800 - this.size.x) {
      this.velocity.x *= -1; // Reverse direction
    }
  }

  onDestroy(): void {
    console.log("Enemy destroyed!");
  }

  getBounds(): Rectangle {
    return new Rectangle(this.position.x, this.position.y, this.size.x, this.size.y);
  }

  onCollision(other: Collidable): void {
    if (other instanceof Player) {
      // Enemy collision logic handled by Player
    }
  }

  getAttackDamage(): number {
    return this.attackDamage;
  }
}

class PowerUp extends GameObject implements Collidable {
  private value: number;
  private rotationSpeed: number = 2;
  private rotation: number = 0;

  constructor(x: number, y: number, value: number = 50) {
    super(x, y, 16, 16); // PowerUp is 16x16 pixels
    this.value = value;
  }

  draw(context: CanvasRenderingContext2D): void {
    context.save();
    context.translate(
      this.position.x + this.size.x / 2,
      this.position.y + this.size.y / 2
    );
    context.rotate(this.rotation);
    context.fillStyle = 'gold';
    context.fillRect(-this.size.x / 2, -this.size.y / 2, this.size.x, this.size.y);
    context.restore();
  }

  onUpdate(deltaTime: number): void {
    this.rotation += this.rotationSpeed * deltaTime;
  }

  onDestroy(): void {
    console.log(`PowerUp collected! Value: ${this.value}`);
  }

  getBounds(): Rectangle {
    return new Rectangle(this.position.x, this.position.y, this.size.x, this.size.y);
  }

  onCollision(other: Collidable): void {
    if (other instanceof Player) {
      this.onDestroy(); // PowerUp gets consumed
    }
  }

  getValue(): number {
    return this.value;
  }
}

// ✅ GAME MANAGER
class Game {
  private gameObjects: GameObject[] = [];
  private collidableObjects: Collidable[] = [];
  private canvas: HTMLCanvasElement;
  private context: CanvasRenderingContext2D;
  private lastTime: number = 0;

  constructor(canvasId: string) {
    this.canvas = document.getElementById(canvasId) as HTMLCanvasElement;
    this.context = this.canvas.getContext('2d')!;

    this.initializeGame();
  }

  private initializeGame(): void {
    // Create game objects
    const player = new Player(100, 100);
    const enemy1 = new Enemy(300, 150);
    const enemy2 = new Enemy(500, 200);
    const powerUp = new PowerUp(400, 100);

    this.gameObjects.push(player, enemy1, enemy2, powerUp);
    this.collidableObjects.push(player, enemy1, enemy2, powerUp);
  }

  private gameLoop = (currentTime: number): void => {
    const deltaTime = (currentTime - this.lastTime) / 1000; // Convert to seconds
    this.lastTime = currentTime;

    // Update all objects
    this.gameObjects.forEach(obj => obj.update(deltaTime));

    // Check collisions
    this.checkCollisions();

    // Render everything
    this.render();

    // Continue the loop
    requestAnimationFrame(this.gameLoop);
  }

  private checkCollisions(): void {
    for (let i = 0; i < this.collidableObjects.length; i++) {
      for (let j = i + 1; j < this.collidableObjects.length; j++) {
        const obj1 = this.collidableObjects[i];
        const obj2 = this.collidableObjects[j];

        if (obj1.getBounds().intersects(obj2.getBounds())) {
          obj1.onCollision(obj2);
          obj2.onCollision(obj1);
        }
      }
    }
  }

  private render(): void {
    // Clear canvas
    this.context.clearRect(0, 0, this.canvas.width, this.canvas.height);

    // Draw all objects
    this.gameObjects.forEach(obj => obj.draw(this.context));
  }

  start(): void {
    requestAnimationFrame(this.gameLoop);
  }
}

// Usage
// const game = new Game('gameCanvas');
// game.start();
```

#### **💡 INTERVIEW INSIGHTS:**

**🔹 ABSTRACT CLASS vs INTERFACE:**

| Aspect | **Abstract Class** | **Interface** |
|--------|-------------------|---------------|
| **Implementation** | ✅ **Can have** concrete methods | ❌ **Only** method signatures |
| **Constructor** | ✅ **Can have** constructor | ❌ **Cannot** have constructor |
| **Properties** | ✅ **Can have** instance properties | ✅ **Only** property declarations |
| **Inheritance** | ❌ **Single** inheritance only | ✅ **Multiple** implementation |
| **Access Modifiers** | ✅ **public, private, protected** | ❌ **All public** |
| **When to Use** | **Shared code** + **enforced contract** | **Pure contract** definition |

**🔹 PERFORMANCE CONSIDERATIONS:**
- **Inheritance** = slight runtime overhead cho method calls
- **Interfaces** = **NO runtime cost** (compile-time only)
- **Abstract classes** = normal class performance
- **Static members** = faster access (no instance needed)

**🔹 COMMON MISTAKES:**
```typescript
// ❌ SAI: Deep inheritance hierarchies
class A {}
class B extends A {}
class C extends B {}
class D extends C {} // Too deep!

// ✅ ĐÚNG: Favor composition over inheritance
interface Feature1 {}
interface Feature2 {}
class MyClass implements Feature1, Feature2 {} // Flexible!

// ❌ SAI: Using abstract class như interface
abstract class BadBase {
  abstract method1(): void;
  abstract method2(): void;
  // No shared code!
}

// ✅ ĐÚNG: Use interface for pure contracts
interface GoodContract {
  method1(): void;
  method2(): void;
}
```

#### **🚀 BEST PRACTICES:**

**📝 DO's:**
- ✅ **Favor composition** over inheritance
- ✅ Use **interfaces** cho contracts
- ✅ Use **abstract classes** cho shared behavior
- ✅ Keep inheritance **SHALLOW** (max 3-4 levels)
- ✅ Use **access modifiers** appropriately

**📝 DON'Ts:**
- ❌ Don't create **GOD CLASSES** (too many responsibilities)
- ❌ Avoid **DEEP inheritance** chains
- ❌ Don't **OVERUSE** abstract classes
- ❌ Don't make everything **PUBLIC**

**GHI NHỚ:**
- **extends** = IS-A relationship (inheritance)
- **implements** = CAN-DO relationship (contract)
- **abstract** = PARTIAL implementation + ENFORCED contract

**INTERVIEW TIP:** Always emphasize **SOLID principles** và how TypeScript's OOP features help implement clean, maintainable code architecture! 🎯

---

## 🎨 CSS & HTML Advanced Topics

**📌 [⬆️ Back to Top](#📚-câu-hỏi-frontend-interview---từ-cơ-bản-đến-senior) | [📋 Mục Lục](#📋-mục-lục-tổng-kết)**

### CSS1: `em` (parent) vs `rem` (root) vs `px` - Khi nào sử dụng cái nào?

**Trả lời:**

Đây là **FUNDAMENTAL QUESTION** về CSS units. Mỗi unit có **USE CASES riêng biệt** và ảnh hưởng khác nhau đến responsive design.

#### **🔥 SO SÁNH CHI TIẾT:**

| Unit | **Relative to** | **Use Case** | **Responsive** | **Accessibility** |
|------|----------------|--------------|----------------|-------------------|
| **`px`** | ❌ **Fixed** | ✅ **Borders, shadows** | ❌ **Không** | ❌ **Không scale** |
| **`em`** | 🔄 **Parent element** | ✅ **Component spacing** | ✅ **Cascading** | ⚠️ **Compounding** |
| **`rem`** | 🏠 **Root element** | ✅ **Typography, layout** | ✅ **Predictable** | ✅ **User preferences** |

#### **🎯 `px` - Absolute Units:**

```css
/* ✅ Tốt cho: Fixed elements */
.border {
  border: 1px solid #ccc; /* Border luôn 1px */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1); /* Shadow cố định */
}

.icon {
  width: 16px; /* Icon size cố định */
  height: 16px;
}

/* ❌ Tránh cho: Typography và spacing */
.bad-text {
  font-size: 16px; /* Không respect user font preferences */
  margin: 20px; /* Không scale với root font */
}
```

**💡 Khi dùng `px`:**
- Borders, box-shadows
- Small icons (16px, 24px, 32px)
- Fixed layouts (khi cần exact pixels)
- Media query breakpoints

#### **🔄 `em` - Relative to Parent:**

```css
/* ✅ Component scaling dựa trên parent */
.card {
  font-size: 18px; /* Parent font size */
}

.card-title {
  font-size: 1.2em; /* = 18px * 1.2 = 21.6px */
  margin-bottom: 0.5em; /* = 10.8px, scale theo title */
}

.card-content {
  font-size: 0.9em; /* = 18px * 0.9 = 16.2px */
  line-height: 1.4em; /* Scale theo content font */
}

/* 🎯 Button component tự scale */
.button {
  padding: 0.5em 1em; /* Scale theo parent font */
  font-size: 1em; /* Inherit parent size */
  border-radius: 0.25em; /* Proportional radius */
}

/* Sử dụng: */
.small-button { font-size: 14px; } /* Button sẽ nhỏ hơn */
.large-button { font-size: 20px; } /* Button sẽ lớn hơn */
```

**⚠️ Em Compounding Problem:**
```css
/* ❌ Compounding issue */
.parent { font-size: 1.2em; } /* 1.2 * 16px = 19.2px */
.child { font-size: 1.2em; }  /* 1.2 * 19.2px = 23.04px */
.grandchild { font-size: 1.2em; } /* 1.2 * 23.04px = 27.65px */

/* ✅ Better approach */
.parent { font-size: 1.2rem; } /* Always 1.2 * root */
.child { font-size: 1.2rem; }  /* Always 1.2 * root */
```

#### **🏠 `rem` - Relative to Root:**

```css
/* ✅ Typography system */
:root {
  font-size: 16px; /* Base font size */
}

.h1 { font-size: 2.5rem; }    /* 40px */
.h2 { font-size: 2rem; }      /* 32px */
.h3 { font-size: 1.5rem; }    /* 24px */
.body { font-size: 1rem; }    /* 16px */
.small { font-size: 0.875rem; } /* 14px */

/* ✅ Spacing system */
.margin-xs { margin: 0.5rem; }  /* 8px */
.margin-sm { margin: 1rem; }    /* 16px */
.margin-md { margin: 1.5rem; }  /* 24px */
.margin-lg { margin: 2rem; }    /* 32px */

/* ✅ Responsive layout */
.container {
  max-width: 75rem; /* 1200px */
  padding: 2rem; /* 32px */
}

.grid-gap {
  gap: 1.5rem; /* 24px - consistent spacing */
}
```

#### **🚀 MODERN BEST PRACTICES:**

**1. Typography Scale với `rem`:**
```css
/* Design system approach */
:root {
  --font-size-xs: 0.75rem;   /* 12px */
  --font-size-sm: 0.875rem;  /* 14px */
  --font-size-base: 1rem;    /* 16px */
  --font-size-lg: 1.125rem;  /* 18px */
  --font-size-xl: 1.25rem;   /* 20px */
  --font-size-2xl: 1.5rem;   /* 24px */
  --font-size-3xl: 2rem;     /* 32px */
}

.text-sm { font-size: var(--font-size-sm); }
.text-base { font-size: var(--font-size-base); }
.text-lg { font-size: var(--font-size-lg); }
```

**2. Component Approach với `em`:**
```css
/* Self-contained component */
.badge {
  font-size: 0.875rem; /* Set base size with rem */
  padding: 0.25em 0.5em; /* Use em for internal spacing */
  border-radius: 0.375em; /* Proportional border radius */
  border: 1px solid currentColor; /* 1px border */
}

/* Variants scale automatically */
.badge--large { font-size: 1rem; }
.badge--small { font-size: 0.75rem; }
```

**3. Responsive Typography:**
```css
/* Fluid typography */
:root {
  font-size: clamp(14px, 2.5vw, 18px); /* Responsive root */
}

/* All rem units scale automatically! */
.title { font-size: 2rem; } /* Scales with viewport */
.body { font-size: 1rem; }  /* Scales with viewport */
```

#### **🎯 DECISION FRAMEWORK:**

```
📐 px: Fixed elements (borders, icons, breakpoints)
📏 em: Component internal spacing, scale with parent
📱 rem: Typography, layout spacing, predictable scaling
```

**✅ Recommended approach:**
```css
/* Layout & Typography: rem */
.container { max-width: 75rem; padding: 2rem; }
.heading { font-size: 2rem; margin-bottom: 1rem; }

/* Component internals: em */
.button { padding: 0.5em 1em; border-radius: 0.25em; }

/* Fixed elements: px */
.border { border: 1px solid #ccc; }
.icon { width: 20px; height: 20px; }
```

**💡 GHI NHỚ:**
- **`rem`** = **R**oot-based, **R**esponsive, **R**eliable 🏠
- **`em`** = **E**lement-relative, **E**scalable components 📦
- **`px`** = **P**ixel-**p**erfect, **P**redictable sizing 📐

**Choose based on context: Layout (rem), Components (em), Fixed (px)!** 🎯

---

### CSS2: CSS Solutions - Module CSS, Styled Components, Inline Styles?

**Trả lời:**

Đây là câu hỏi về **CSS ARCHITECTURE** trong modern React apps. Mỗi approach có **trade-offs khác nhau** về maintainability, performance, và developer experience.

#### **🔥 SO SÁNH TỔNG QUAN:**

| Solution | **Scope** | **Performance** | **Bundle Size** | **TypeScript** | **Flexibility** |
|----------|-----------|-----------------|-----------------|----------------|-----------------|
| **CSS Modules** | ✅ **Scoped** | ✅ **Excellent** | ✅ **Small** | ⚠️ **Limited** | ⚠️ **Static** |
| **Styled Components** | ✅ **Scoped** | ⚠️ **Runtime** | ❌ **Large** | ✅ **Full** | ✅ **Dynamic** |
| **Inline Styles** | ✅ **Scoped** | ⚠️ **Inline** | ✅ **None** | ✅ **Native** | ❌ **Limited** |

#### **📦 CSS Modules - Build-time Scoping:**

```typescript
// Button.module.css
.button {
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
}

.primary {
  background-color: #3b82f6;
  color: white;
}

.secondary {
  background-color: #e5e7eb;
  color: #374151;
}

.size-sm { font-size: 0.875rem; }
.size-lg { font-size: 1.125rem; }
```

```typescript
// Button.tsx
import React from 'react';
import styles from './Button.module.css';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'lg';
  children: React.ReactNode;
}

const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'sm',
  children
}) => {
  // ✅ Type-safe class name composition
  const buttonClasses = [
    styles.button,
    styles[variant],
    styles[`size-${size}`]
  ].join(' ');

  return (
    <button className={buttonClasses}>
      {children}
    </button>
  );
};

// Generated output: button_abc123 primary_def456 size-sm_ghi789
```

**💡 CSS Modules Advantages:**
```typescript
// ✅ 1. Build-time optimization
// CSS được extract thành separate files, cached efficiently

// ✅ 2. Scoped styles - no conflicts
.button {} // Becomes .button_abc123
.card .button {} // Becomes .card_def456 .button_ghi789

// ✅ 3. Small bundle size
// Only used styles included in final CSS

// ✅ 4. Works with any CSS preprocessor
// .module.scss, .module.less supported
```

#### **💅 Styled Components - Runtime CSS-in-JS:**

```typescript
import styled, { css } from 'styled-components';

// ✅ Base styled component với TypeScript
const Button = styled.button<{
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'lg';
  fullWidth?: boolean;
}>`
  /* Base styles */
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;

  /* Conditional styles với props */
  ${({ variant }) => variant === 'primary' && css`
    background-color: #3b82f6;
    color: white;

    &:hover {
      background-color: #2563eb;
    }
  `}

  ${({ variant }) => variant === 'secondary' && css`
    background-color: #e5e7eb;
    color: #374151;

    &:hover {
      background-color: #d1d5db;
    }
  `}

  ${({ size }) => size === 'sm' && css`
    font-size: 0.875rem;
    padding: 0.375rem 0.75rem;
  `}

  ${({ size }) => size === 'lg' && css`
    font-size: 1.125rem;
    padding: 0.75rem 1.5rem;
  `}

  ${({ fullWidth }) => fullWidth && css`
    width: 100%;
  `}
`;

// ✅ Theme integration
const theme = {
  colors: {
    primary: '#3b82f6',
    secondary: '#e5e7eb',
  },
  spacing: {
    sm: '0.5rem',
    md: '1rem',
  }
};

const ThemedButton = styled.button`
  background-color: ${props => props.theme.colors.primary};
  padding: ${props => props.theme.spacing.md};
`;

// ✅ Dynamic styles based on props
const ProgressBar = styled.div<{ progress: number }>`
  width: 100%;
  height: 8px;
  background-color: #e5e7eb;
  border-radius: 4px;

  &::after {
    content: '';
    display: block;
    height: 100%;
    width: ${props => props.progress}%;
    background-color: #3b82f6;
    border-radius: 4px;
    transition: width 0.3s ease;
  }
`;

// Usage
<ProgressBar progress={75} /> // 75% filled
```

#### **📝 Inline Styles - JavaScript Objects:**

```typescript
import React, { CSSProperties } from 'react';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'lg';
  disabled?: boolean;
  children: React.ReactNode;
}

const Button: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'sm',
  disabled = false,
  children
}) => {
  // ✅ Dynamic styles với TypeScript support
  const getButtonStyles = (): CSSProperties => {
    const baseStyles: CSSProperties = {
      padding: size === 'sm' ? '0.375rem 0.75rem' : '0.75rem 1.5rem',
      fontSize: size === 'sm' ? '0.875rem' : '1.125rem',
      fontWeight: 500,
      borderRadius: '0.375rem',
      border: 'none',
      cursor: disabled ? 'not-allowed' : 'pointer',
      transition: 'all 0.2s ease',
      opacity: disabled ? 0.6 : 1,
    };

    const variantStyles: CSSProperties = variant === 'primary'
      ? {
          backgroundColor: '#3b82f6',
          color: 'white',
        }
      : {
          backgroundColor: '#e5e7eb',
          color: '#374151',
        };

    return { ...baseStyles, ...variantStyles };
  };

  // ✅ Hover styles với event handlers
  const [isHovered, setIsHovered] = React.useState(false);

  const hoverStyles: CSSProperties = isHovered ? {
    backgroundColor: variant === 'primary' ? '#2563eb' : '#d1d5db',
    transform: 'translateY(-1px)',
    boxShadow: '0 4px 8px rgba(0, 0, 0, 0.12)',
  } : {};

  return (
    <button
      style={{ ...getButtonStyles(), ...hoverStyles }}
      onMouseEnter={() => setIsHovered(true)}
      onMouseLeave={() => setIsHovered(false)}
      disabled={disabled}
    >
      {children}
    </button>
  );
};

// ✅ CSS-in-JS với computed styles
const DynamicCard: React.FC<{
  bgColor: string;
  borderRadius: number;
}> = ({ bgColor, borderRadius, children }) => {
  const cardStyles: CSSProperties = {
    backgroundColor: bgColor,
    borderRadius: `${borderRadius}px`,
    padding: '1rem',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    margin: '1rem 0',
  };

  return <div style={cardStyles}>{children}</div>;
};
```

#### **⚖️ WHEN TO USE WHAT:**

**✅ CSS Modules - Best for:**
```typescript
// ✅ Static styling với good performance
// ✅ Large applications với design system
// ✅ SSR apps (Next.js default support)
// ✅ Team muốn familiar CSS syntax

const HomePage: React.FC = () => (
  <div className={styles.container}>
    <header className={styles.header}>
      <h1 className={styles.title}>Welcome</h1>
    </header>
  </div>
);
```

**✅ Styled Components - Best for:**
```typescript
// ✅ Component libraries (Chakra UI, Material-UI style)
// ✅ Heavy theming requirements
// ✅ Dynamic styling based on props
// ✅ Complex animations và interactions

const ThemeProvider = () => (
  <ThemeProvider theme={customTheme}>
    <DynamicButton animate={true} theme="dark" />
  </ThemeProvider>
);
```

**✅ Inline Styles - Best for:**
```typescript
// ✅ Dynamic styles từ API/user input
// ✅ One-off styling
// ✅ Simple components
// ✅ No build step required

const CustomWidget: React.FC<{ config: WidgetConfig }> = ({ config }) => (
  <div style={{
    backgroundColor: config.bgColor, // Dynamic từ user
    width: `${config.width}px`,     // Dynamic size
    height: `${config.height}px`,
  }}>
    {config.content}
  </div>
);
```

#### **🚀 MODERN HYBRID APPROACH:**

```typescript
// ✅ Combine best of all worlds
import styles from './Card.module.css'; // Static styles
import styled from 'styled-components';   // Dynamic components

// Base styling với CSS Modules
const Card: React.FC<{
  variant?: 'elevated' | 'outlined';
  padding?: number; // Dynamic padding
}> = ({ variant = 'elevated', padding = 16, children }) => {

  // Dynamic styles inline
  const dynamicStyles: CSSProperties = {
    padding: `${padding}px`,
  };

  return (
    <div
      className={`${styles.card} ${styles[variant]}`}
      style={dynamicStyles}
    >
      {children}
    </div>
  );
};

// Styled component cho complex interactions
const AnimatedCard = styled(Card)`
  transition: transform 0.2s ease;

  &:hover {
    transform: translateY(-4px);
  }
`;
```

**💡 GHI NHỚ:**
- **CSS Modules** = **Static**, **Fast**, **Familiar** 📦
- **Styled Components** = **Dynamic**, **Powerful**, **Runtime** 💅
- **Inline Styles** = **Simple**, **Direct**, **Limited** 📝

**Choose based on project needs: Performance (Modules), Flexibility (Styled), Simplicity (Inline)!** 🎯

---

### CSS3: CSS Specificity - Cách tính và best practices?

**Trả lời:**

CSS Specificity là **ALGORITHM** để determine style nào sẽ được apply khi có **CONFLICT**. Hiểu rõ specificity là **KEY** để viết maintainable CSS.

#### **🔥 SPECIFICITY CALCULATION:**

| Selector Type | **Value** | **Example** | **Specificity** |
|---------------|-----------|-------------|-----------------|
| **Inline styles** | **1000** | `style="color: red"` | **(1,0,0,0)** |
| **IDs** | **100** | `#header` | **(0,1,0,0)** |
| **Classes, attributes, pseudo-classes** | **10** | `.button`, `[type]`, `:hover` | **(0,0,1,0)** |
| **Elements, pseudo-elements** | **1** | `div`, `::before` | **(0,0,0,1)** |

#### **📊 SPECIFICITY EXAMPLES:**

```css
/* Specificity: (0,0,0,1) = 1 */
div {
  color: black;
}

/* Specificity: (0,0,1,0) = 10 */
.button {
  color: blue;
}

/* Specificity: (0,1,0,0) = 100 */
#header {
  color: red;
}

/* Specificity: (0,1,1,1) = 111 */
#header .nav a {
  color: green;
}

/* Specificity: (0,0,2,1) = 21 */
.nav.primary a {
  color: purple;
}

/* Specificity: (0,0,1,2) = 12 */
.button:hover span {
  color: orange;
}
```

#### **🎯 COMPLEX SPECIFICITY CALCULATIONS:**

```css
/* (0,0,0,1) - Chỉ element */
p { color: black; }

/* (0,0,1,1) - Class + element */
p.intro { color: blue; }

/* (0,0,2,1) - 2 classes + element */
p.intro.highlight { color: red; }

/* (0,1,0,1) - ID + element */
#content p { color: green; }

/* (0,1,1,2) - ID + class + 2 elements */
#sidebar .widget h3 { color: purple; }

/* (0,0,3,0) - 3 classes (HIGHEST trong non-ID) */
.nav.primary.active { color: yellow; }

/* (0,2,0,0) - 2 IDs (RẤT KHUYÊN KHÔNG) */
#header #nav { color: orange; }
```

#### **⚠️ COMMON SPECIFICITY MISTAKES:**

```css
/* ❌ BAD: Over-specific selectors */
.header .nav .menu .item .link {
  color: blue; /* Specificity: (0,0,5,0) = 50 */
}

/* ✅ GOOD: Simple, maintainable */
.nav-link {
  color: blue; /* Specificity: (0,0,1,0) = 10 */
}

/* ❌ BAD: Overusing IDs */
#header #nav #menu {
  display: flex; /* Specificity: (0,3,0,0) = 300 */
}

/* ✅ GOOD: Use classes instead */
.header-nav {
  display: flex; /* Specificity: (0,0,1,0) = 10 */
}

/* ❌ BAD: Fighting specificity với !important */
.button {
  background: blue !important; /* Nuclear option */
}

/* ✅ GOOD: Use more specific selector */
.form .button {
  background: blue; /* Specificity: (0,0,2,0) = 20 */
}
```

#### **🚀 MODERN BEST PRACTICES:**

**1. BEM Methodology cho consistent specificity:**
```css
/* All selectors have same specificity: (0,0,1,0) = 10 */
.card { /* Block */ }
.card__header { /* Element */ }
.card__title { /* Element */ }
.card--featured { /* Modifier */ }
.card__header--large { /* Element + Modifier */ }

/* Easy to override */
.homepage .card--featured {
  /* Specificity: (0,0,2,0) = 20 */
}
```

**2. CSS Custom Properties cho dynamic values:**
```css
/* Low specificity base styles */
.button {
  background: var(--button-bg, #007bff);
  color: var(--button-color, white);
}

/* Override with custom properties (same specificity) */
.button.secondary {
  --button-bg: #6c757d;
  --button-color: white;
}

.dark-theme {
  --button-bg: #0d6efd;
}
```

**3. Utility-first approach (Tailwind style):**
```css
/* Utilities có same specificity */
.text-blue { color: blue; }      /* (0,0,1,0) = 10 */
.text-red { color: red; }        /* (0,0,1,0) = 10 */
.text-green { color: green; }    /* (0,0,1,0) = 10 */

/* Source order determines winner khi specificity bằng nhau */
```

#### **🛠️ DEBUGGING SPECIFICITY:**

**Browser DevTools:**
```css
/* Chrome DevTools shows specificity */
.element {
  color: blue; /* (0,0,1,0) */
}

#container .element {
  color: red; /* (0,1,1,0) - WINS */
}
```

**Specificity Calculator Tools:**
- [Specificity Calculator](https://specificity.keegan.st/)
- [CSS Specificity Graph](https://jonassebastianohlsson.com/specificity-graph/)

#### **⚖️ SPECIFICITY STRATEGIES:**

**✅ Strategy 1: Keep Specificity Low**
```css
/* Low and consistent specificity */
.nav-item { } /* 10 */
.nav-item.active { } /* 20 */
.nav-item:hover { } /* 20 */
```

**✅ Strategy 2: Logical Hierarchy**
```css
/* Natural progression */
.button { } /* 10 - base */
.button.primary { } /* 20 - variant */
.form .button.primary { } /* 30 - context */
```

**✅ Strategy 3: Namespace Pattern**
```css
/* Consistent namespacing */
.layout-header { } /* 10 */
.layout-sidebar { } /* 10 */
.component-card { } /* 10 */
.utility-hidden { } /* 10 */
```

#### **🔧 SPECIFICITY OVERRIDE TECHNIQUES:**

**1. Increase Specificity Safely:**
```css
/* Instead of !important */
.button.button {
  background: blue; /* Specificity: (0,0,2,0) = 20 */
}

/* Or duplicate class */
.primary.primary {
  color: white; /* Specificity: (0,0,2,0) = 20 */
}
```

**2. CSS Layers (Modern Solution):**
```css
@layer base, components, utilities;

@layer base {
  button { background: gray; } /* Low priority */
}

@layer components {
  .btn { background: blue; } /* Medium priority */
}

@layer utilities {
  .bg-red { background: red !important; } /* High priority */
}
```

**3. `:where()` for Zero Specificity:**
```css
/* Specificity: (0,0,0,0) = 0 */
:where(.button) {
  padding: 0.5rem;
}

/* Easy to override */
.custom-button {
  padding: 1rem; /* Specificity: (0,0,1,0) = 10 - WINS */
}
```

#### **💡 INTERVIEW TIPS:**

**Specificity Calculation Quiz:**
```css
/* What wins? */
.nav .item.active { color: blue; }    /* (0,0,3,0) = 30 */
#sidebar .item { color: red; }        /* (0,1,1,0) = 110 - WINS */
.item:hover:focus { color: green; }   /* (0,0,3,0) = 30 */
div.nav .item { color: purple; }      /* (0,0,2,1) = 21 */
```

**💡 GHI NHỚ:**
- **Inline** = 1000 (tránh!)
- **ID** = 100 (dùng ít)
- **Class** = 10 (dùng nhiều)
- **Element** = 1 (base styles)

**Specificity Strategy: Start low, increase gradually, avoid !important!** 🎯

---

### CSS4: Position: absolute vs relative vs static vs fixed?

**Trả lời:**

CSS Position là **LAYOUT MECHANISM** fundamentally khác nhau. Hiểu rõ position là **CRITICAL** cho layout design và element positioning.

#### **🔥 POSITION TYPES OVERVIEW:**

| Position | **Document Flow** | **Positioning Context** | **Common Use** |
|----------|-------------------|-------------------------|----------------|
| **`static`** | ✅ **In flow** | ❌ **Cannot position** | **Default behavior** |
| **`relative`** | ✅ **In flow** | 🎯 **Self-relative** | **Positioning context** |
| **`absolute`** | ❌ **Out of flow** | 📍 **Nearest positioned parent** | **Overlays, tooltips** |
| **`fixed`** | ❌ **Out of flow** | 🖥️ **Viewport** | **Headers, modals** |
| **`sticky`** | 🔄 **Conditional** | 📜 **Scroll container** | **Sticky headers** |

#### **📍 `static` - Default Positioning:**

```css
.element {
  position: static; /* Default value */
  /* top, right, bottom, left có NO EFFECT */
  top: 50px; /* ❌ Ignored */
  z-index: 10; /* ❌ Ignored */
}
```

```html
<!-- Normal document flow -->
<div class="container">
  <div class="box1">Box 1</div> <!-- Follows document flow -->
  <div class="box2">Box 2</div> <!-- Below box1 -->
  <div class="box3">Box 3</div> <!-- Below box2 -->
</div>
```

#### **🎯 `relative` - Self-Relative Positioning:**

```css
.relative-box {
  position: relative;
  top: 20px;    /* Move down 20px from original position */
  left: 30px;   /* Move right 30px from original position */
  z-index: 1;   /* ✅ z-index works */
}

/* 🎯 Common use: Positioning context cho absolute children */
.card {
  position: relative; /* Tạo positioning context */
}

.card__badge {
  position: absolute;
  top: 10px;    /* 10px from card's top */
  right: 10px;  /* 10px from card's right */
}
```

**Key Points về `relative`:**
- Element vẫn **chiếm space** trong document flow
- Other elements **KHÔNG move** để fill space
- Creates **positioning context** cho absolute children

#### **📍 `absolute` - Positioned Parent Relative:**

```css
.parent {
  position: relative; /* ✅ Positioning context */
  width: 300px;
  height: 200px;
}

.absolute-child {
  position: absolute;
  top: 0;      /* 0px from parent's top */
  right: 0;    /* 0px from parent's right */
  width: 50px;
  height: 50px;
  /* Element removed from document flow */
}

/* 🎯 Real-world examples */
.tooltip {
  position: absolute;
  top: 100%;   /* Below the parent */
  left: 50%;   /* Centered horizontally */
  transform: translateX(-50%); /* Perfect center */
  z-index: 1000;
}

.modal-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;   /* Fill entire positioned parent */
  background: rgba(0,0,0,0.5);
}
```

**Positioning Context Hierarchy:**
```html
<div class="grandparent">
  <div class="parent" style="position: relative;">
    <div class="child" style="position: absolute; top: 0;">
      <!-- Positioned relative to .parent (nearest positioned ancestor) -->
    </div>
  </div>
</div>

<div class="no-positioned-parent">
  <div class="child" style="position: absolute; top: 0;">
    <!-- Positioned relative to <body> (initial containing block) -->
  </div>
</div>
```

#### **🖥️ `fixed` - Viewport Relative:**

```css
/* Sticky header */
.header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;    /* Full width */
  height: 60px;
  background: white;
  z-index: 100; /* Above other content */
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

/* Modal backdrop */
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;  /* Full viewport width */
  height: 100vh; /* Full viewport height */
  background: rgba(0,0,0,0.8);
  z-index: 1000;
}

/* Floating action button */
.fab {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 56px;
  height: 56px;
  border-radius: 50%;
  z-index: 50;
}

/* Mobile-first approach */
.mobile-menu {
  position: fixed;
  top: 0;
  left: -100%; /* Hidden off-screen */
  width: 80%;
  height: 100vh;
  transition: left 0.3s ease;
}

.mobile-menu.open {
  left: 0; /* Slide in */
}
```

#### **📜 `sticky` - Scroll-Conditional:**

```css
/* Sticky table header */
.table-header {
  position: sticky;
  top: 0; /* Stick when reaching top of viewport */
  background: white;
  z-index: 10;
}

/* Sticky sidebar */
.sidebar {
  position: sticky;
  top: 80px; /* Stick 80px from top (below fixed header) */
  height: calc(100vh - 80px);
  overflow-y: auto;
}

/* Sticky section headers */
.section-title {
  position: sticky;
  top: 60px; /* Below main header */
  background: #f8f9fa;
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}
```

#### **🎯 PRACTICAL USE CASES:**

**1. Card với Badge Overlay:**
```html
<div class="product-card"> <!-- position: relative -->
  <img src="product.jpg" alt="Product">
  <div class="sale-badge"> <!-- position: absolute -->
    50% OFF
  </div>
  <div class="card-content">
    <h3>Product Name</h3>
  </div>
</div>
```

```css
.product-card {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
}

.sale-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background: #e74c3c;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.875rem;
  font-weight: bold;
}
```

**2. Responsive Modal System:**
```css
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0,0,0,0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  position: relative; /* For close button positioning */
  background: white;
  border-radius: 8px;
  padding: 2rem;
  max-width: 500px;
  max-height: 80vh;
  overflow-y: auto;
}

.modal-close {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}
```

#### **⚠️ COMMON POSITION PITFALLS:**

```css
/* ❌ BAD: z-index without position */
.element {
  z-index: 999; /* NO EFFECT on static elements */
}

/* ✅ GOOD: Position + z-index */
.element {
  position: relative; /* or absolute/fixed */
  z-index: 999;
}

/* ❌ BAD: Absolute without positioned parent */
.child {
  position: absolute;
  top: 20px; /* Relative to <body>, not intended parent */
}

/* ✅ GOOD: Clear positioning context */
.parent {
  position: relative; /* Positioning context */
}
.child {
  position: absolute;
  top: 20px; /* Relative to .parent */
}

/* ❌ BAD: Fixed elements breaking mobile scroll */
.mobile-header {
  position: fixed;
  height: 60px; /* But body doesn't account for this */
}

/* ✅ GOOD: Account for fixed element space */
body {
  padding-top: 60px; /* Space for fixed header */
}
```

#### **📱 RESPONSIVE CONSIDERATIONS:**

```css
/* Mobile-first positioning */
.sidebar {
  /* Mobile: Full-width overlay */
  position: fixed;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100vh;
  transform: translateX(0);
  transition: transform 0.3s ease;
}

.sidebar.open {
  transform: translateX(100%);
}

/* Desktop: Sticky sidebar */
@media (min-width: 768px) {
  .sidebar {
    position: sticky;
    top: 80px;
    left: auto;
    width: 250px;
    height: calc(100vh - 80px);
    transform: none;
  }
}
```

**💡 GHI NHỚ:**
- **`static`** = Default, no positioning
- **`relative`** = Self-offset, creates context
- **`absolute`** = Parent-relative, out of flow
- **`fixed`** = Viewport-relative, always visible
- **`sticky`** = Scroll-conditional, responsive

**Position Strategy: Context (relative) → Overlay (absolute) → Always visible (fixed) → Scroll-aware (sticky)!** 🎯

---

### CSS5: CSS Variables vs SCSS vs BEM Methodology?

**Trả lời:**

Đây là câu hỏi về **CSS ARCHITECTURE** và **METHODOLOGY**. Ba approaches này solve khác nhau problems trong CSS organization và maintainability.

#### **🔥 OVERVIEW COMPARISON:**

| Aspect | **CSS Variables** | **SCSS** | **BEM** |
|--------|-------------------|----------|---------|
| **Type** | **Runtime values** | **Build-time preprocessing** | **Naming convention** |
| **Browser Support** | ✅ **Modern browsers** | ✅ **All (compiled)** | ✅ **All browsers** |
| **Dynamic** | ✅ **Runtime changeable** | ❌ **Build-time only** | ❌ **Static classes** |
| **Learning Curve** | ✅ **Easy** | ⚠️ **Medium** | ✅ **Easy** |

#### **🎨 CSS Variables (Custom Properties):**

```css
/* ✅ Root level variables */
:root {
  /* Design tokens */
  --primary-color: #3b82f6;
  --secondary-color: #64748b;
  --success-color: #10b981;
  --error-color: #ef4444;

  /* Typography */
  --font-family-sans: 'Inter', sans-serif;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --line-height-base: 1.5;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 3rem;

  /* Breakpoints (for consistent usage) */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
}

/* ✅ Component-scoped variables */
.card {
  --card-bg: white;
  --card-border: #e5e7eb;
  --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  --card-radius: 0.5rem;

  background: var(--card-bg);
  border: 1px solid var(--card-border);
  box-shadow: var(--card-shadow);
  border-radius: var(--card-radius);
  padding: var(--spacing-lg);
}

/* ✅ Dynamic theming */
.dark-theme {
  --primary-color: #60a5fa;
  --card-bg: #1f2937;
  --card-border: #374151;
}

.light-theme {
  --primary-color: #3b82f6;
  --card-bg: white;
  --card-border: #e5e7eb;
}

/* ✅ Responsive variables */
@media (min-width: 768px) {
  :root {
    --font-size-base: 1.125rem;
    --spacing-lg: 2rem;
  }
}

/* ✅ JavaScript integration */
.progress-bar {
  --progress: 0%; /* Controlled by JS */
  width: 100%;
  height: 8px;
  background: #e5e7eb;
}

.progress-bar::after {
  content: '';
  display: block;
  width: var(--progress);
  height: 100%;
  background: var(--primary-color);
  transition: width 0.3s ease;
}
```

```typescript
// ✅ Dynamic control với JavaScript
const progressBar = document.querySelector('.progress-bar') as HTMLElement;
const updateProgress = (percentage: number) => {
  progressBar.style.setProperty('--progress', `${percentage}%`);
};

// Theme switching
const setTheme = (theme: 'light' | 'dark') => {
  document.body.className = `${theme}-theme`;
};
```

#### **📦 SCSS (Sass) - CSS Preprocessor:**

```scss
// ✅ Variables (compile-time)
$primary-color: #3b82f6;
$secondary-color: #64748b;
$font-family-sans: 'Inter', sans-serif;
$spacing-unit: 0.25rem;

// ✅ Maps for organized data
$colors: (
  primary: #3b82f6,
  secondary: #64748b,
  success: #10b981,
  error: #ef4444
);

$spacing: (
  xs: $spacing-unit,
  sm: $spacing-unit * 2,
  md: $spacing-unit * 4,
  lg: $spacing-unit * 6,
  xl: $spacing-unit * 12
);

$breakpoints: (
  sm: 640px,
  md: 768px,
  lg: 1024px,
  xl: 1280px
);

// ✅ Functions
@function color($name) {
  @return map-get($colors, $name);
}

@function spacing($size) {
  @return map-get($spacing, $size);
}

// ✅ Mixins for reusable patterns
@mixin button-variant($bg-color, $text-color: white) {
  background-color: $bg-color;
  color: $text-color;
  border: none;
  padding: spacing(sm) spacing(md);
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    background-color: darken($bg-color, 10%);
    transform: translateY(-1px);
  }

  &:active {
    transform: translateY(0);
  }
}

@mixin respond-to($breakpoint) {
  $bp: map-get($breakpoints, $breakpoint);
  @media (min-width: $bp) {
    @content;
  }
}

// ✅ Usage
.button {
  @include button-variant(color(primary));

  &--secondary {
    @include button-variant(color(secondary));
  }

  &--success {
    @include button-variant(color(success));
  }
}

// ✅ Responsive mixins
.container {
  width: 100%;
  padding: 0 spacing(md);

  @include respond-to(md) {
    max-width: 768px;
    margin: 0 auto;
  }

  @include respond-to(lg) {
    max-width: 1024px;
  }
}

// ✅ Nested selectors
.card {
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  padding: spacing(lg);

  &__header {
    margin-bottom: spacing(md);
    padding-bottom: spacing(sm);
    border-bottom: 1px solid #e5e7eb;
  }

  &__title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1f2937;
    margin: 0;
  }

  &__content {
    color: #6b7280;
    line-height: 1.6;
  }

  &--featured {
    border: 2px solid color(primary);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  }
}
```

#### **📚 BEM Methodology (Block Element Modifier):**

```css
/* ✅ Block - Standalone component */
.menu {
  display: flex;
  background: white;
  border-radius: 0.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

/* ✅ Element - Part of block */
.menu__item {
  padding: 0.75rem 1rem;
  text-decoration: none;
  color: #374151;
  transition: background-color 0.2s ease;
}

.menu__link {
  display: block;
  font-weight: 500;
}

.menu__icon {
  margin-right: 0.5rem;
  width: 1rem;
  height: 1rem;
}

/* ✅ Modifier - Variation of block/element */
.menu--vertical {
  flex-direction: column;
}

.menu--dark {
  background: #1f2937;
}

.menu__item--active {
  background: #f3f4f6;
  color: #1f2937;
}

.menu__item--disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.menu__link--external::after {
  content: ' ↗';
  font-size: 0.875rem;
}

/* ✅ Complex BEM example */
.product-card {
  background: white;
  border-radius: 0.5rem;
  overflow: hidden;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.product-card__image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.product-card__content {
  padding: 1rem;
}

.product-card__title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.product-card__price {
  font-size: 1.25rem;
  font-weight: bold;
  color: #059669;
}

.product-card__badge {
  position: absolute;
  top: 0.5rem;
  left: 0.5rem;
  background: #ef4444;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.75rem;
  font-weight: bold;
}

/* Modifiers */
.product-card--featured {
  border: 2px solid #3b82f6;
}

.product-card--on-sale .product-card__price {
  color: #ef4444;
}

.product-card__badge--new {
  background: #10b981;
}

.product-card__badge--sale {
  background: #f59e0b;
}
```

#### **🚀 MODERN HYBRID APPROACH:**

```scss
// ✅ SCSS + CSS Variables + BEM
:root {
  // CSS Variables cho runtime control
  --primary-hue: 220;
  --primary-saturation: 90%;
  --primary-lightness: 50%;
}

// SCSS variables cho build-time logic
$primary-base: hsl(var(--primary-hue), var(--primary-saturation), var(--primary-lightness));

// BEM + SCSS mixins
@mixin block($name) {
  .#{$name} {
    @content;
  }
}

@mixin element($parent, $name) {
  .#{$parent}__#{$name} {
    @content;
  }
}

@mixin modifier($parent, $name) {
  .#{$parent}--#{$name} {
    @content;
  }
}

// Usage
@include block('button') {
  // CSS Variables cho theming
  --button-bg: #{$primary-base};
  --button-color: white;

  background: var(--button-bg);
  color: var(--button-color);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    --button-bg: #{darken($primary-base, 10%)};
  }
}

@include element('button', 'icon') {
  margin-right: 0.5rem;
}

@include modifier('button', 'large') {
  padding: 0.75rem 1.5rem;
  font-size: 1.125rem;
}
```

#### **⚖️ WHEN TO USE WHAT:**

**✅ CSS Variables - Best for:**
```css
/* Runtime theming */
.theme-switcher {
  --primary: #3b82f6; /* User can change */
}

/* Component customization */
.progress-bar {
  --progress: 75%; /* Dynamic from JS */
}

/* Responsive values */
@media (min-width: 768px) {
  :root { --spacing: 2rem; }
}
```

**✅ SCSS - Best for:**
```scss
/* Complex calculations */
$golden-ratio: 1.618;
$base-size: 1rem;
$scale: $base-size * $golden-ratio;

/* Advanced mixins */
@mixin triangle($size, $color, $direction) {
  // Complex CSS generation
}

/* Build-time optimizations */
@if $environment == 'production' {
  // Production-specific styles
}
```

**✅ BEM - Best for:**
```css
/* Large teams */
.navigation__item--active { }

/* Component libraries */
.ui-button__icon--loading { }

/* Clear naming patterns */
.product-card__price--discounted { }
```

#### **💡 DECISION MATRIX:**

```
🎨 CSS Variables: Runtime values, theming, JS integration
📦 SCSS: Build tools, complex logic, team workflows
📚 BEM: Naming consistency, large teams, maintainability

💥 HYBRID: Use all three together for maximum power!
```

**GHI NHỚ:** CSS Variables = **Runtime**, SCSS = **Build-time**, BEM = **Organization**! 🎯

---

### CSS6: `div` vs `span` - Semantic differences và use cases?

**Trả lời:**

Đây là **FUNDAMENTAL HTML** question về **SEMANTIC ELEMENTS**. `div` và `span` có **different display behaviors** và **semantic meanings**.

#### **🔥 CORE DIFFERENCES:**

| Aspect | **`<div>`** | **`<span>`** |
|--------|-------------|--------------|
| **Display** | **Block-level** | **Inline** |
| **Content Model** | **Flow content** | **Phrasing content** |
| **Default Width** | **100% parent** | **Content width** |
| **Line Breaks** | ✅ **Creates breaks** | ❌ **No breaks** |
| **Nesting** | ✅ **Can contain block + inline** | ⚠️ **Inline only** |
| **Semantic Meaning** | ❌ **None (generic)** | ❌ **None (generic)** |

#### **📦 `<div>` - Block-level Container:**

```html
<!-- ✅ Layout containers -->
<div class="header">
  <div class="logo">
    <img src="logo.png" alt="Logo">
  </div>
  <div class="navigation">
    <nav>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About</a></li>
      </ul>
    </nav>
  </div>
</div>

<!-- ✅ Content sections -->
<div class="main-content">
  <div class="article">
    <h1>Article Title</h1>
    <p>Article content...</p>
  </div>
  <div class="sidebar">
    <div class="widget">
      <h3>Widget Title</h3>
      <ul>
        <li>Widget item 1</li>
        <li>Widget item 2</li>
      </ul>
    </div>
  </div>
</div>

<!-- ✅ Component wrappers -->
<div class="card">
  <div class="card-header">
    <h2>Card Title</h2>
  </div>
  <div class="card-body">
    <p>Card content goes here...</p>
  </div>
  <div class="card-footer">
    <button>Action</button>
  </div>
</div>
```

**CSS behavior của `div`:**
```css
div {
  /* Default browser styles */
  display: block;      /* Full-width, new line */
  margin: 0;          /* No default margin */
  padding: 0;         /* No default padding */
}

/* ✅ Common div usage patterns */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 1rem;
}

.flex-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
```

#### **📝 `<span>` - Inline Container:**

```html
<!-- ✅ Text styling -->
<p>
  This is a paragraph with
  <span class="highlight">highlighted text</span>
  and <span class="bold">bold text</span>.
</p>

<!-- ✅ Small UI elements -->
<button class="btn">
  <span class="btn-icon">📧</span>
  <span class="btn-text">Send Email</span>
</button>

<!-- ✅ Data formatting -->
<div class="price">
  <span class="currency">$</span>
  <span class="amount">99</span>
  <span class="cents">.99</span>
</div>

<!-- ✅ Status indicators -->
<p class="user-status">
  <span class="username">John Doe</span>
  <span class="status online">● Online</span>
</p>

<!-- ✅ Form labels with styling -->
<label for="email">
  Email Address
  <span class="required">*</span>
</label>

<!-- ✅ Badge/tag systems -->
<div class="tags">
  <span class="tag tag--primary">React</span>
  <span class="tag tag--secondary">TypeScript</span>
  <span class="tag tag--success">CSS</span>
</div>
```

**CSS behavior của `span`:**
```css
span {
  /* Default browser styles */
  display: inline;     /* Inline flow, no line breaks */
}

/* ✅ Common span styling patterns */
.highlight {
  background-color: #fef3c7;
  padding: 0.125rem 0.25rem;
  border-radius: 0.25rem;
}

.badge {
  display: inline-block; /* Allows padding/margin */
  background: #3b82f6;
  color: white;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  font-size: 0.875rem;
  font-weight: 500;
}

.required {
  color: #ef4444;
  font-weight: bold;
}

/* ✅ Icon + text patterns */
.btn-icon {
  margin-right: 0.5rem;
}

.status.online {
  color: #10b981;
}

.status.offline {
  color: #6b7280;
}
```

#### **🎯 PRACTICAL USAGE EXAMPLES:**

**1. Card Component Structure:**
```html
<div class="product-card">           <!-- Block container -->
  <div class="card-image">           <!-- Block for layout -->
    <img src="product.jpg" alt="Product">
    <span class="sale-badge">SALE</span>  <!-- Inline badge -->
  </div>
  <div class="card-content">         <!-- Block for content -->
    <h3>Product Name</h3>
    <p class="description">
      Product description with
      <span class="highlight">special features</span>
    </p>
    <div class="price-section">      <!-- Block for price layout -->
      <span class="price-original">$99.99</span>  <!-- Inline price -->
      <span class="price-sale">$79.99</span>      <!-- Inline price -->
    </div>
  </div>
</div>
```

**2. Navigation with Status:**
```html
<div class="navigation">             <!-- Block container -->
  <div class="nav-item">             <!-- Block item -->
    <a href="/messages">Messages</a>
    <span class="notification-count">3</span>  <!-- Inline count -->
  </div>
  <div class="nav-item">
    <a href="/profile">Profile</a>
    <span class="status-indicator online">●</span>  <!-- Inline status -->
  </div>
</div>
```

**3. Form with Validation:**
```html
<div class="form-group">             <!-- Block container -->
  <label for="password">
    Password
    <span class="required">*</span>   <!-- Inline indicator -->
  </label>
  <input type="password" id="password">
  <div class="validation-message">   <!-- Block for message -->
    <span class="error-icon">⚠️</span>  <!-- Inline icon -->
    <span class="error-text">Password too short</span>  <!-- Inline text -->
  </div>
</div>
```

#### **⚠️ COMMON MISTAKES:**

```html
<!-- ❌ BAD: Span containing block elements -->
<span>
  <div>This breaks HTML semantics</div>
  <p>Block elements inside inline element</p>
</span>

<!-- ✅ GOOD: Div containing spans -->
<div>
  <span>Inline element 1</span>
  <span>Inline element 2</span>
</div>

<!-- ❌ BAD: Using div for inline styling -->
<p>
  This text has <div class="highlight">highlighted section</div> in it.
</p>
<!-- Creates unwanted line breaks -->

<!-- ✅ GOOD: Using span for inline styling -->
<p>
  This text has <span class="highlight">highlighted section</span> in it.
</p>

<!-- ❌ BAD: Unnecessary nesting -->
<div>
  <div>
    <div>
      <span>Over-nested content</span>
    </div>
  </div>
</div>

<!-- ✅ GOOD: Minimal necessary structure -->
<div class="content">
  <span>Simple content</span>
</div>
```

#### **🚀 MODERN ALTERNATIVES:**

**Instead of generic `div`/`span`, use semantic HTML5:**

```html
<!-- ❌ Generic divs -->
<div class="header">
  <div class="navigation">
    <div class="nav-item">Home</div>
  </div>
</div>
<div class="main">
  <div class="article">
    <div class="article-header">Title</div>
    <div class="article-content">Content</div>
  </div>
  <div class="sidebar">Sidebar</div>
</div>

<!-- ✅ Semantic HTML5 -->
<header>
  <nav>
    <a href="/">Home</a>
  </nav>
</header>
<main>
  <article>
    <header>
      <h1>Title</h1>
    </header>
    <section>Content</section>
  </article>
  <aside>Sidebar</aside>
</main>

<!-- ✅ When semantic elements don't fit, use div/span -->
<div class="card">              <!-- No semantic meaning needed -->
  <div class="card-actions">    <!-- Pure layout container -->
    <button>Action</button>
  </div>
</div>
```

#### **📱 RESPONSIVE CONSIDERATIONS:**

```css
/* ✅ Responsive div layouts */
.container {
  display: block;
}

@media (min-width: 768px) {
  .container {
    display: flex;
    gap: 1rem;
  }
}

/* ✅ Responsive span behavior */
.tag {
  display: inline-block;
  margin: 0.25rem;
}

@media (max-width: 640px) {
  .tag {
    display: block;      /* Stack on mobile */
    margin: 0.25rem 0;
  }
}

/* ✅ Hiding spans responsively */
.desktop-only {
  display: inline;
}

@media (max-width: 768px) {
  .desktop-only {
    display: none;
  }
}
```

#### **💡 DECISION FRAMEWORK:**

```
📦 Use <div> when:
- Creating layout containers
- Grouping block-level content
- Building components/widgets
- Need full-width elements

📝 Use <span> when:
- Styling part of text
- Creating inline UI elements
- Adding markers/indicators
- Need inline flow behavior

🎯 Use semantic HTML when:
- Content has inherent meaning
- Accessibility is important
- SEO matters
- Standard patterns exist
```

**GHI NHỚ:**
- **`div`** = **Block** container, layout structure 📦
- **`span`** = **Inline** wrapper, text styling 📝
- **Semantic HTML** = Meaningful content structure 🎯

**Choose based on display needs: Block layout (div) vs Inline styling (span)!** 💡

---

### CSS7: Margin vs Padding và Box Model concepts?

**Trả lời:**

CSS Box Model là **FUNDAMENTAL CONCEPT** của web layout. Hiểu rõ **margin vs padding** và **box-sizing** là **CRITICAL** cho precise layout control.

#### **🔥 BOX MODEL ANATOMY:**

```
┌─────────────────────────────────────┐
│              MARGIN                 │ ← Outside spacing
│  ┌─────────────────────────────────┐ │
│  │            BORDER               │ │ ← Element border
│  │  ┌─────────────────────────────┐ │ │
│  │  │          PADDING            │ │ │ ← Inside spacing
│  │  │  ┌─────────────────────────┐ │ │ │
│  │  │  │       CONTENT           │ │ │ │ ← Actual content
│  │  │  │                         │ │ │ │
│  │  │  └─────────────────────────┘ │ │ │
│  │  └─────────────────────────────┘ │ │
│  └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

#### **📊 MARGIN vs PADDING COMPARISON:**

| Aspect | **Margin** | **Padding** |
|--------|------------|-------------|
| **Position** | **Outside border** | **Inside border** |
| **Background** | ❌ **Transparent** | ✅ **Inherits element background** |
| **Clickable Area** | ❌ **Not clickable** | ✅ **Part of clickable area** |
| **Collapsing** | ✅ **Margin collapse** | ❌ **No collapse** |
| **Negative Values** | ✅ **Allowed** | ❌ **Not allowed** |
| **Use Case** | **Spacing between elements** | **Space inside element** |

#### **🎯 PRACTICAL EXAMPLES:**

**1. Button Design - Padding cho internal spacing:**
```css
.button {
  /* ✅ PADDING - Space inside button */
  padding: 12px 24px;          /* Vertical: 12px, Horizontal: 24px */
  padding-top: 12px;           /* Individual sides */
  padding-right: 24px;
  padding-bottom: 12px;
  padding-left: 24px;

  /* ✅ MARGIN - Space between buttons */
  margin: 0 8px;               /* Horizontal spacing between buttons */
  margin-bottom: 16px;         /* Space below button */

  background: #3b82f6;
  border: 2px solid #1d4ed8;
  border-radius: 6px;
  color: white;
  cursor: pointer;
}

/* Visual comparison */
.button-no-padding {
  padding: 0;                  /* Text touches border */
  margin: 0 8px;
}

.button-no-margin {
  padding: 12px 24px;
  margin: 0;                   /* Buttons touch each other */
}
```

**2. Card Layout - Combined margin + padding:**
```css
.card {
  /* ✅ MARGIN - Space between cards */
  margin: 20px;                /* Space around entire card */
  margin-bottom: 24px;         /* Extra space below each card */

  /* ✅ PADDING - Internal content spacing */
  padding: 24px;               /* Space inside card */

  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.card-header {
  /* ✅ PADDING - Content spacing */
  padding-bottom: 16px;        /* Space below header */

  /* ✅ MARGIN - Space between elements */
  margin-bottom: 16px;         /* Space after header */

  border-bottom: 1px solid #e5e7eb;
}

.card-content {
  /* ✅ No additional margin - uses card padding */
  padding: 0;

  /* ✅ MARGIN for content spacing */
  margin-bottom: 16px;
}

.card-actions {
  /* ✅ MARGIN to push to bottom */
  margin-top: auto;            /* Push to bottom in flex container */

  /* ✅ PADDING for button spacing */
  padding-top: 16px;

  border-top: 1px solid #e5e7eb;
}
```

#### **⚡ BOX-SIZING BEHAVIOR:**

**1. `content-box` (Default):**
```css
.content-box {
  box-sizing: content-box;     /* Default browser behavior */
  width: 300px;
  padding: 20px;
  border: 5px solid #3b82f6;
  margin: 10px;
}

/*
Total width calculation:
- Content: 300px (width)
- Padding: 20px × 2 = 40px
- Border: 5px × 2 = 10px
- TOTAL WIDTH: 300 + 40 + 10 = 350px
- TOTAL HEIGHT: content + padding + border
- Margin không tính vào total size
*/
```

**2. `border-box` (Modern approach):**
```css
/* ✅ Modern CSS Reset */
*, *::before, *::after {
  box-sizing: border-box;      /* Include padding + border in width */
}

.border-box {
  box-sizing: border-box;
  width: 300px;                /* Total width including padding + border */
  padding: 20px;
  border: 5px solid #3b82f6;
  margin: 10px;
}

/*
Total width calculation:
- TOTAL WIDTH: 300px (includes content + padding + border)
- Content width: 300 - 40 (padding) - 10 (border) = 250px
- Much easier to work with!
*/
```

#### **🚀 RESPONSIVE BOX MODEL:**

```css
/* ✅ Mobile-first padding/margin */
.container {
  padding: 16px;               /* Small screens */
  margin: 0 auto;
  max-width: 1200px;
}

@media (min-width: 768px) {
  .container {
    padding: 24px;             /* Medium screens */
  }
}

@media (min-width: 1024px) {
  .container {
    padding: 32px;             /* Large screens */
  }
}

/* ✅ Responsive card spacing */
.card-grid {
  display: grid;
  gap: 16px;                   /* Modern way - replaces margin */
  padding: 16px;
}

@media (min-width: 768px) {
  .card-grid {
    gap: 24px;
    padding: 24px;
  }

  .card {
    padding: 32px;             /* Larger internal spacing */
  }
}
```

#### **⚠️ COMMON MARGIN/PADDING MISTAKES:**

```css
/* ❌ BAD: Margin collapse issues */
.section {
  margin-top: 20px;
  margin-bottom: 20px;
}

.section + .section {
  /* Margins collapse - only 20px gap, not 40px! */
}

/* ✅ GOOD: Use padding or gap */
.sections-container {
  display: flex;
  flex-direction: column;
  gap: 20px;                   /* Consistent spacing */
}

/* ❌ BAD: Mixing margin directions */
.element {
  margin: 10px 0 15px 0;       /* Inconsistent vertical margins */
}

/* ✅ GOOD: Consistent spacing system */
.element {
  margin-bottom: 16px;         /* Consistent bottom margin */
}

/* ❌ BAD: Padding on wrong element */
.button-wrapper {
  padding: 20px;               /* Padding outside button */
}

.button {
  background: blue;            /* Background doesn't extend to padding */
}

/* ✅ GOOD: Padding on styled element */
.button {
  padding: 20px;               /* Padding extends background */
  background: blue;
}
```

#### **🎯 MARGIN COLLAPSE DEEP DIVE:**

```css
/* Margin collapse scenarios */

/* 1. Adjacent siblings */
.box1 {
  margin-bottom: 20px;
}

.box2 {
  margin-top: 30px;           /* Result: 30px gap (larger wins) */
}

/* 2. Parent and first/last child */
.parent {
  margin-top: 10px;
}

.first-child {
  margin-top: 20px;           /* Result: 20px from parent top */
}

/* ✅ Prevent margin collapse */
.parent {
  padding-top: 1px;           /* or border-top, or overflow: hidden */
}

/* or use modern layout */
.flex-parent {
  display: flex;
  flex-direction: column;
  gap: 20px;                  /* No margin collapse */
}
```

#### **🔧 ADVANCED BOX MODEL TECHNIQUES:**

**1. Negative Margins for Overlap:**
```css
.overlap-card {
  margin-top: -50px;          /* Overlap with element above */
  position: relative;
  z-index: 2;
}

.pullout-quote {
  margin-left: -40px;         /* Extend beyond container */
  margin-right: -40px;
  padding: 0 40px;            /* Maintain content alignment */
  background: #f8fafc;
}
```

**2. Auto Margins for Centering:**
```css
.centered-block {
  width: 300px;
  margin: 0 auto;             /* Center horizontally */
}

.flex-item {
  margin-left: auto;          /* Push to right in flex container */
}

.last-item {
  margin-top: auto;           /* Push to bottom in flex column */
}
```

**3. Logical Properties (Modern):**
```css
.modern-spacing {
  /* Instead of margin-left/right */
  margin-inline: 16px;        /* Horizontal (respects writing direction) */

  /* Instead of margin-top/bottom */
  margin-block: 24px;         /* Vertical */

  /* Instead of padding-left/right */
  padding-inline: 20px;

  /* Instead of padding-top/bottom */
  padding-block: 16px;
}
```

#### **📱 MOBILE-FIRST BOX MODEL:**

```css
/* ✅ Mobile-first approach */
.content {
  /* Mobile: tight spacing */
  padding: 16px;
  margin: 8px;
}

/* Tablet */
@media (min-width: 768px) {
  .content {
    padding: 24px;
    margin: 16px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .content {
    padding: 32px;
    margin: 24px;
  }
}

/* ✅ Container queries (modern) */
.card {
  container-type: inline-size;
  padding: 16px;
}

@container (min-width: 300px) {
  .card {
    padding: 24px;
  }
}
```

#### **💡 BOX MODEL DEBUGGING:**

```css
/* ✅ Debug box model visually */
* {
  outline: 1px solid red;     /* Shows all element boundaries */
}

/* More specific debugging */
.debug-margins {
  outline: 2px solid blue;    /* Element boundary */
}

.debug-margins::before {
  content: '';
  position: absolute;
  top: -10px;
  left: -10px;
  right: -10px;
  bottom: -10px;
  border: 1px dashed red;     /* Shows margin area */
  pointer-events: none;
}
```

**💡 GHI NHỚ:**
- **Margin** = **Outside** spacing, transparent, collapses 📏
- **Padding** = **Inside** spacing, inherits background, clickable 📦
- **border-box** = Width includes padding + border 🎯
- **Gap** = Modern spacing, no collapse 🚀

**Box Model Strategy: Use `border-box`, prefer `gap`, consistent spacing system!** 🎯

---

### CSS8: Build Theme System - CSS Variables và Design Tokens?

**Trả lời:**

Building a **SCALABLE THEME SYSTEM** là essential cho modern applications. **CSS Variables + Design Tokens** tạo ra **CONSISTENT**, **MAINTAINABLE** và **ACCESSIBLE** design system.

#### **🔥 DESIGN TOKENS HIERARCHY:**

```
🎨 DESIGN TOKENS STRUCTURE:

Global Tokens     ←  Brand Colors, Typography Scale
   ↓
Semantic Tokens   ←  Primary, Secondary, Success, Error
   ↓
Component Tokens  ←  Button, Card, Input specific values
   ↓
CSS Variables     ←  Runtime implementation
```

#### **🎯 COMPREHENSIVE THEME FOUNDATION:**

```css
/* ✅ ROOT DESIGN TOKENS */
:root {
  /* 🎨 COLOR PALETTE - Global tokens */
  --color-blue-50: #eff6ff;
  --color-blue-100: #dbeafe;
  --color-blue-200: #bfdbfe;
  --color-blue-300: #93c5fd;
  --color-blue-400: #60a5fa;
  --color-blue-500: #3b82f6;   /* Base blue */
  --color-blue-600: #2563eb;
  --color-blue-700: #1d4ed8;
  --color-blue-800: #1e40af;
  --color-blue-900: #1e3a8a;

  --color-gray-50: #f9fafb;
  --color-gray-100: #f3f4f6;
  --color-gray-200: #e5e7eb;
  --color-gray-300: #d1d5db;
  --color-gray-400: #9ca3af;
  --color-gray-500: #6b7280;
  --color-gray-600: #4b5563;
  --color-gray-700: #374151;
  --color-gray-800: #1f2937;
  --color-gray-900: #111827;

  /* 🎯 SEMANTIC TOKENS - Meaning-based */
  --color-primary: var(--color-blue-500);
  --color-primary-hover: var(--color-blue-600);
  --color-primary-active: var(--color-blue-700);
  --color-primary-disabled: var(--color-blue-300);

  --color-secondary: var(--color-gray-500);
  --color-secondary-hover: var(--color-gray-600);

  --color-success: #10b981;
  --color-success-hover: #059669;
  --color-warning: #f59e0b;
  --color-warning-hover: #d97706;
  --color-error: #ef4444;
  --color-error-hover: #dc2626;

  /* 📝 TEXT COLORS */
  --text-primary: var(--color-gray-900);
  --text-secondary: var(--color-gray-600);
  --text-muted: var(--color-gray-400);
  --text-inverse: white;
  --text-link: var(--color-primary);
  --text-link-hover: var(--color-primary-hover);

  /* 🏗️ SURFACE COLORS */
  --surface-primary: white;
  --surface-secondary: var(--color-gray-50);
  --surface-tertiary: var(--color-gray-100);
  --surface-overlay: rgba(0, 0, 0, 0.8);
  --surface-elevated: white;

  /* 🔲 BORDER COLORS */
  --border-primary: var(--color-gray-200);
  --border-secondary: var(--color-gray-300);
  --border-focus: var(--color-primary);
  --border-error: var(--color-error);

  /* 📏 SPACING SYSTEM */
  --spacing-xs: 0.25rem;      /* 4px */
  --spacing-sm: 0.5rem;       /* 8px */
  --spacing-md: 1rem;         /* 16px */
  --spacing-lg: 1.5rem;       /* 24px */
  --spacing-xl: 2rem;         /* 32px */
  --spacing-2xl: 3rem;        /* 48px */
  --spacing-3xl: 4rem;        /* 64px */

  /* 📱 BREAKPOINTS */
  --breakpoint-sm: 640px;
  --breakpoint-md: 768px;
  --breakpoint-lg: 1024px;
  --breakpoint-xl: 1280px;

  /* 🔤 TYPOGRAPHY SCALE */
  --font-family-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-family-mono: 'Fira Code', 'Courier New', monospace;

  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */

  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;

  --line-height-tight: 1.25;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.75;

  /* 🎭 SHADOWS */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
  --shadow-xl: 0 20px 25px rgba(0, 0, 0, 0.15);

  /* 🎨 BORDER RADIUS */
  --radius-none: 0;
  --radius-sm: 0.25rem;       /* 4px */
  --radius-md: 0.5rem;        /* 8px */
  --radius-lg: 0.75rem;       /* 12px */
  --radius-xl: 1rem;          /* 16px */
  --radius-full: 9999px;      /* Fully rounded */

  /* ⏱️ TRANSITIONS */
  --transition-fast: 150ms ease;
  --transition-normal: 250ms ease;
  --transition-slow: 350ms ease;

  /* 🎛️ Z-INDEX SCALE */
  --z-dropdown: 1000;
  --z-sticky: 1020;
  --z-fixed: 1030;
  --z-modal-backdrop: 1040;
  --z-modal: 1050;
  --z-popover: 1060;
  --z-tooltip: 1070;
  --z-toast: 1080;
}
```

#### **🌙 DARK THEME IMPLEMENTATION:**

```css
/* ✅ DARK THEME OVERRIDE */
[data-theme="dark"] {
  /* 🎯 Semantic color overrides */
  --color-primary: var(--color-blue-400);
  --color-primary-hover: var(--color-blue-300);
  --color-primary-active: var(--color-blue-500);

  /* 📝 Text colors */
  --text-primary: var(--color-gray-100);
  --text-secondary: var(--color-gray-300);
  --text-muted: var(--color-gray-500);

  /* 🏗️ Surface colors */
  --surface-primary: var(--color-gray-900);
  --surface-secondary: var(--color-gray-800);
  --surface-tertiary: var(--color-gray-700);
  --surface-elevated: var(--color-gray-800);

  /* 🔲 Border colors */
  --border-primary: var(--color-gray-700);
  --border-secondary: var(--color-gray-600);

  /* 🎭 Shadows for dark theme */
  --shadow-sm: 0 1px 2px rgba(0, 0, 0, 0.3);
  --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.4);
  --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);
}

/* ✅ System preference detection */
@media (prefers-color-scheme: dark) {
  :root {
    /* Apply dark theme if no explicit theme set */
  }
}
```

#### **🎨 COMPONENT TOKENS:**

```css
/* ✅ BUTTON COMPONENT TOKENS */
.button {
  /* 🎯 Component-specific design tokens */
  --button-height: 2.5rem;
  --button-padding-x: var(--spacing-lg);
  --button-padding-y: var(--spacing-sm);
  --button-font-size: var(--font-size-sm);
  --button-font-weight: var(--font-weight-medium);
  --button-border-radius: var(--radius-md);
  --button-transition: var(--transition-fast);

  /* Primary variant */
  --button-bg: var(--color-primary);
  --button-bg-hover: var(--color-primary-hover);
  --button-bg-active: var(--color-primary-active);
  --button-bg-disabled: var(--color-primary-disabled);
  --button-text: var(--text-inverse);
  --button-border: var(--button-bg);

  /* Implementation */
  height: var(--button-height);
  padding: var(--button-padding-y) var(--button-padding-x);
  font-size: var(--button-font-size);
  font-weight: var(--button-font-weight);
  border-radius: var(--button-border-radius);
  transition: var(--button-transition);

  background: var(--button-bg);
  color: var(--button-text);
  border: 1px solid var(--button-border);
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-family: inherit;
}

.button:hover:not(:disabled) {
  background: var(--button-bg-hover);
  transform: translateY(-1px);
  box-shadow: var(--shadow-md);
}

.button:active {
  background: var(--button-bg-active);
  transform: translateY(0);
}

.button:disabled {
  background: var(--button-bg-disabled);
  cursor: not-allowed;
  opacity: 0.6;
}

/* ✅ Button variants using token overrides */
.button--secondary {
  --button-bg: transparent;
  --button-bg-hover: var(--surface-secondary);
  --button-bg-active: var(--surface-tertiary);
  --button-text: var(--text-primary);
  --button-border: var(--border-primary);
}

.button--danger {
  --button-bg: var(--color-error);
  --button-bg-hover: var(--color-error-hover);
  --button-bg-active: var(--color-error);
}

.button--large {
  --button-height: 3rem;
  --button-padding-x: var(--spacing-xl);
  --button-font-size: var(--font-size-base);
}

.button--small {
  --button-height: 2rem;
  --button-padding-x: var(--spacing-md);
  --button-font-size: var(--font-size-xs);
}
```

#### **🏗️ CARD COMPONENT SYSTEM:**

```css
/* ✅ CARD COMPONENT TOKENS */
.card {
  /* 🎯 Card-specific tokens */
  --card-bg: var(--surface-elevated);
  --card-border: var(--border-primary);
  --card-border-radius: var(--radius-lg);
  --card-padding: var(--spacing-lg);
  --card-shadow: var(--shadow-sm);
  --card-shadow-hover: var(--shadow-md);

  /* Implementation */
  background: var(--card-bg);
  border: 1px solid var(--card-border);
  border-radius: var(--card-border-radius);
  padding: var(--card-padding);
  box-shadow: var(--card-shadow);
  transition: var(--transition-normal);
}

.card:hover {
  box-shadow: var(--card-shadow-hover);
  transform: translateY(-2px);
}

.card__header {
  --card-header-border: var(--border-primary);

  padding-bottom: var(--spacing-md);
  margin-bottom: var(--spacing-md);
  border-bottom: 1px solid var(--card-header-border);
}

.card__title {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--text-primary);
  margin: 0 0 var(--spacing-xs) 0;
}

.card__subtitle {
  font-size: var(--font-size-sm);
  color: var(--text-secondary);
  margin: 0;
}
```

#### **🚀 TYPESCRIPT THEME INTEGRATION:**

```typescript
// ✅ Design tokens as TypeScript constants
export const tokens = {
  colors: {
    primary: 'var(--color-primary)',
    primaryHover: 'var(--color-primary-hover)',
    secondary: 'var(--color-secondary)',
    success: 'var(--color-success)',
    error: 'var(--color-error)',
    warning: 'var(--color-warning)',
  },
  spacing: {
    xs: 'var(--spacing-xs)',
    sm: 'var(--spacing-sm)',
    md: 'var(--spacing-md)',
    lg: 'var(--spacing-lg)',
    xl: 'var(--spacing-xl)',
  },
  typography: {
    fontSizes: {
      xs: 'var(--font-size-xs)',
      sm: 'var(--font-size-sm)',
      base: 'var(--font-size-base)',
      lg: 'var(--font-size-lg)',
      xl: 'var(--font-size-xl)',
    },
    fontWeights: {
      normal: 'var(--font-weight-normal)',
      medium: 'var(--font-weight-medium)',
      semibold: 'var(--font-weight-semibold)',
      bold: 'var(--font-weight-bold)',
    },
  },
  radius: {
    sm: 'var(--radius-sm)',
    md: 'var(--radius-md)',
    lg: 'var(--radius-lg)',
    full: 'var(--radius-full)',
  },
  shadows: {
    sm: 'var(--shadow-sm)',
    md: 'var(--shadow-md)',
    lg: 'var(--shadow-lg)',
  },
} as const;

// ✅ Theme context for React
interface ThemeContextType {
  theme: 'light' | 'dark' | 'auto';
  setTheme: (theme: 'light' | 'dark' | 'auto') => void;
  toggleTheme: () => void;
}

export const ThemeContext = createContext<ThemeContextType | null>(null);

// ✅ Theme provider component
export const ThemeProvider: React.FC<{ children: React.ReactNode }> = ({
  children
}) => {
  const [theme, setTheme] = useState<'light' | 'dark' | 'auto'>('auto');

  useEffect(() => {
    // 🎯 Apply theme to document
    const root = document.documentElement;

    if (theme === 'auto') {
      // Detect system preference
      const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      root.setAttribute('data-theme', prefersDark ? 'dark' : 'light');
    } else {
      root.setAttribute('data-theme', theme);
    }

    // 💾 Persist to localStorage
    localStorage.setItem('theme-preference', theme);
  }, [theme]);

  const toggleTheme = useCallback(() => {
    setTheme(prev => prev === 'light' ? 'dark' : 'light');
  }, []);

  const value = useMemo(() => ({
    theme,
    setTheme,
    toggleTheme,
  }), [theme, toggleTheme]);

  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  );
};

// ✅ Theme hook
export const useTheme = (): ThemeContextType => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error('useTheme must be used within ThemeProvider');
  }
  return context;
};
```

#### **🎭 COMPONENT VARIANTS WITH TOKENS:**

```css
/* ✅ INPUT COMPONENT SYSTEM */
.input {
  /* 🎯 Input-specific tokens */
  --input-height: 2.5rem;
  --input-padding: var(--spacing-sm) var(--spacing-md);
  --input-font-size: var(--font-size-sm);
  --input-border-radius: var(--radius-md);
  --input-border: var(--border-primary);
  --input-border-focus: var(--border-focus);
  --input-bg: var(--surface-primary);
  --input-text: var(--text-primary);
  --input-placeholder: var(--text-muted);

  /* States */
  --input-border-error: var(--border-error);
  --input-bg-disabled: var(--surface-tertiary);

  /* Implementation */
  height: var(--input-height);
  padding: var(--input-padding);
  font-size: var(--input-font-size);
  border-radius: var(--input-border-radius);
  border: 1px solid var(--input-border);
  background: var(--input-bg);
  color: var(--input-text);
  transition: var(--transition-fast);
  font-family: inherit;
  width: 100%;
}

.input::placeholder {
  color: var(--input-placeholder);
}

.input:focus {
  outline: none;
  border-color: var(--input-border-focus);
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.input:disabled {
  background: var(--input-bg-disabled);
  cursor: not-allowed;
  opacity: 0.6;
}

.input--error {
  --input-border: var(--input-border-error);
  --input-border-focus: var(--input-border-error);
}

.input--large {
  --input-height: 3rem;
  --input-font-size: var(--font-size-base);
}
```

#### **📱 RESPONSIVE THEME TOKENS:**

```css
/* ✅ Responsive design tokens */
:root {
  /* Mobile-first spacing */
  --container-padding: var(--spacing-md);
  --section-spacing: var(--spacing-xl);
  --card-padding: var(--spacing-md);
}

@media (min-width: 768px) {
  :root {
    --container-padding: var(--spacing-lg);
    --section-spacing: var(--spacing-2xl);
    --card-padding: var(--spacing-lg);
  }
}

@media (min-width: 1024px) {
  :root {
    --container-padding: var(--spacing-xl);
    --section-spacing: var(--spacing-3xl);
    --card-padding: var(--spacing-xl);
  }
}

/* ✅ Component responsive behavior */
.container {
  padding: var(--container-padding);
  max-width: var(--breakpoint-xl);
  margin: 0 auto;
}

.section {
  margin-bottom: var(--section-spacing);
}

.card {
  padding: var(--card-padding);
}
```

#### **💡 THEME DEBUGGING TOOLS:**

```css
/* ✅ Development theme debugging */
.debug-theme {
  position: fixed;
  top: var(--spacing-md);
  right: var(--spacing-md);
  background: var(--surface-elevated);
  border: 1px solid var(--border-primary);
  border-radius: var(--radius-md);
  padding: var(--spacing-md);
  font-size: var(--font-size-xs);
  font-family: var(--font-family-mono);
  z-index: var(--z-tooltip);
  box-shadow: var(--shadow-lg);
}

.debug-theme::before {
  content: 'Theme: ' attr(data-theme);
  display: block;
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--spacing-xs);
}
```

**💡 GHI NHỚ:**
- **Global Tokens** = Brand foundation 🎨
- **Semantic Tokens** = Meaning-based colors 🎯
- **Component Tokens** = Component-specific values 🧩
- **CSS Variables** = Runtime implementation ⚡

**Theme Strategy: Global foundation → Semantic meaning → Component specifics → Runtime flexibility!** 🚀

---

### CSS9: CSS Reset vs Normalize - Tại sao cần và cách sử dụng?

**Trả lời:**

CSS Reset và Normalize là **FOUNDATION STRATEGIES** để handle **BROWSER INCONSISTENCIES**. Hiểu rõ differences và khi nào sử dụng là **CRUCIAL** cho consistent cross-browser design.

#### **🔥 BROWSER DEFAULT STYLES PROBLEM:**

```css
/* 🚨 Browser defaults vary across browsers */

/* Chrome default for <h1> */
h1 {
  display: block;
  font-size: 2em;
  margin: 0.67em 0;
  font-weight: bold;
}

/* Firefox default for <h1> */
h1 {
  display: block;
  font-size: 2em;
  margin-top: 0.67em;
  margin-bottom: 0.67em;
  font-weight: bold;
}

/* Safari default cho <p> */
p {
  display: block;
  margin: 1em 0;
}

/* IE default cho <p> */
p {
  margin: 1em 0;
  padding: 0;
}
```

#### **📊 CSS RESET vs NORMALIZE COMPARISON:**

| Aspect | **CSS Reset** | **Normalize.css** |
|--------|---------------|-------------------|
| **Philosophy** | **Remove ALL default styles** | **Preserve useful defaults** |
| **Approach** | **Nuclear option** | **Surgical fixes** |
| **File Size** | **Smaller (~2KB)** | **Larger (~8KB)** |
| **Styling Start** | **From scratch** | **Enhanced defaults** |
| **Use Case** | **Custom design systems** | **Standard web content** |
| **Maintenance** | **Less frequent updates** | **Active development** |

#### **🗑️ CSS RESET APPROACH:**

```css
/* ✅ MODERN CSS RESET (Minimal) */

/* Reset margins and padding */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Remove default list styles */
ol, ul {
  list-style: none;
}

/* Reset table styles */
table {
  border-collapse: collapse;
  border-spacing: 0;
}

/* Reset form elements */
button, input, select, textarea {
  font: inherit;
  background: none;
  border: none;
  outline: none;
}

/* Reset links */
a {
  text-decoration: none;
  color: inherit;
}

/* Reset headings */
h1, h2, h3, h4, h5, h6 {
  font-size: inherit;
  font-weight: inherit;
}

/* ✅ COMPREHENSIVE CSS RESET (Eric Meyer style) */
html, body, div, span, applet, object, iframe,
h1, h2, h3, h4, h5, h6, p, blockquote, pre,
a, abbr, acronym, address, big, cite, code,
del, dfn, em, img, ins, kbd, q, s, samp,
small, strike, strong, sub, sup, tt, var,
b, u, i, center,
dl, dt, dd, ol, ul, li,
fieldset, form, label, legend,
table, caption, tbody, tfoot, thead, tr, th, td,
article, aside, canvas, details, embed,
figure, figcaption, footer, header, hgroup,
menu, nav, output, ruby, section, summary,
time, mark, audio, video {
  margin: 0;
  padding: 0;
  border: 0;
  font-size: 100%;
  font: inherit;
  vertical-align: baseline;
}

/* HTML5 display-role reset for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, menu, nav, section {
  display: block;
}

body {
  line-height: 1;
}

ol, ul {
  list-style: none;
}

blockquote, q {
  quotes: none;
}

blockquote:before, blockquote:after,
q:before, q:after {
  content: '';
  content: none;
}

table {
  border-collapse: collapse;
  border-spacing: 0;
}
```

#### **🔧 NORMALIZE.CSS APPROACH:**

```css
/* ✅ NORMALIZE.CSS EXCERPTS */

/**
 * 1. Correct the line height in all browsers.
 * 2. Prevent adjustments of font size after orientation changes in iOS.
 */
html {
  line-height: 1.15; /* 1 */
  -webkit-text-size-adjust: 100%; /* 2 */
}

/**
 * Remove the margin in all browsers.
 */
body {
  margin: 0;
}

/**
 * Render the `main` element consistently in IE.
 */
main {
  display: block;
}

/**
 * Correct the font size and margin on `h1` elements within `section` and
 * `article` contexts in Chrome, Firefox, and Safari.
 */
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}

/**
 * Add the correct box sizing in Firefox.
 * Show the overflow in Edge and IE.
 */
hr {
  box-sizing: content-box; /* 1 */
  height: 0; /* 1 */
  overflow: visible; /* 2 */
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */
pre {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}

/**
 * Remove the gray background on active links in IE 10.
 */
a {
  background-color: transparent;
}

/**
 * 1. Remove the bottom border in Chrome 57-
 * 2. Add the correct text decoration in Chrome, Edge, IE, Opera, and Safari.
 */
abbr[title] {
  border-bottom: none; /* 1 */
  text-decoration: underline; /* 2 */
  text-decoration: underline dotted; /* 2 */
}

/**
 * Add the correct font weight in Chrome, Edge, and Safari.
 */
b, strong {
  font-weight: bolder;
}

/**
 * 1. Correct the inheritance and scaling of font size in all browsers.
 * 2. Correct the odd `em` font sizing in all browsers.
 */
code, kbd, samp {
  font-family: monospace, monospace; /* 1 */
  font-size: 1em; /* 2 */
}
```

#### **🚀 MODERN HYBRID APPROACH:**

```css
/* ✅ MODERN CSS FOUNDATION (Best of both worlds) */

/* Box sizing reset */
*,
*::before,
*::after {
  box-sizing: border-box;
}

/* Remove default margins */
* {
  margin: 0;
}

/* HTML & Body foundation */
html {
  /* Improve text rendering */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  /* Better mobile experience */
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;

  /* Consistent line height */
  line-height: 1.5;

  /* Enable font features */
  font-variant-ligatures: common-ligatures;
}

body {
  /* Remove default margin */
  margin: 0;

  /* Better font rendering */
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto,
               'Helvetica Neue', Arial, sans-serif;

  /* Improve text rendering */
  text-rendering: optimizeSpeed;

  /* Better mobile scrolling */
  -webkit-overflow-scrolling: touch;
}

/* Media elements */
img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
  height: auto;
}

/* Form elements */
input, button, textarea, select {
  font: inherit;
  color: inherit;
}

/* Remove button default styles */
button {
  background: none;
  border: none;
  cursor: pointer;
}

/* Better focus styles */
:focus {
  outline: 2px solid #4A90E2;
  outline-offset: 2px;
}

/* Skip focus for mouse users */
:focus:not(:focus-visible) {
  outline: none;
}

/* List styles */
ul, ol {
  padding-left: 0;
  list-style: none;
}

/* Table styles */
table {
  border-collapse: collapse;
  border-spacing: 0;
}

/* Remove text decoration */
a {
  text-decoration: none;
  color: inherit;
}

/* Better typography */
h1, h2, h3, h4, h5, h6 {
  font-weight: 600;
  line-height: 1.25;
  margin-bottom: 0.5em;
}

p {
  line-height: 1.6;
  margin-bottom: 1em;
}

/* Address styling for older browsers */
article, aside, details, figcaption, figure,
footer, header, hgroup, main, menu, nav,
section, summary {
  display: block;
}

/* Hidden attribute */
[hidden] {
  display: none !important;
}
```

#### **🛠️ FRAMEWORK-SPECIFIC RESETS:**

**1. Tailwind CSS Reset:**
```css
/* ✅ Tailwind's Preflight (based on normalize.css) */
*, ::before, ::after {
  box-sizing: border-box;
  border-width: 0;
  border-style: solid;
  border-color: theme('borderColor.DEFAULT', currentColor);
}

::before, ::after {
  --tw-content: '';
}

html {
  line-height: 1.5;
  -webkit-text-size-adjust: 100%;
  -moz-tab-size: 4;
  tab-size: 4;
  font-family: theme('fontFamily.sans', ui-sans-serif, system-ui);
}

body {
  margin: 0;
  line-height: inherit;
}

hr {
  height: 0;
  color: inherit;
  border-top-width: 1px;
}

abbr:where([title]) {
  text-decoration: underline dotted;
}

h1, h2, h3, h4, h5, h6 {
  font-size: inherit;
  font-weight: inherit;
}

a {
  color: inherit;
  text-decoration: inherit;
}

button, input, optgroup, select, textarea {
  font-family: inherit;
  font-size: 100%;
  font-weight: inherit;
  line-height: inherit;
  color: inherit;
  margin: 0;
  padding: 0;
}
```

**2. Bootstrap Reboot:**
```css
/* ✅ Bootstrap's Reboot (normalize.css + additions) */
*,
*::before,
*::after {
  box-sizing: border-box;
}

html {
  font-family: sans-serif;
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

article, aside, figcaption, figure, footer, header, hgroup, main, nav, section {
  display: block;
}

body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
  font-size: 1rem;
  font-weight: 400;
  line-height: 1.5;
  color: #212529;
  text-align: left;
  background-color: #fff;
}

[tabindex="-1"]:focus:not(:focus-visible) {
  outline: 0 !important;
}

hr {
  box-sizing: content-box;
  height: 0;
  overflow: visible;
}
```

#### **⚖️ DECISION FRAMEWORK:**

**✅ Use CSS Reset when:**
```css
/* Custom design system */
.design-system {
  /* Start from zero, build everything custom */
}

/* Unique UI patterns */
.creative-layout {
  /* Need complete control over styling */
}

/* Component library */
.ui-library {
  /* Consistent base across different projects */
}
```

**✅ Use Normalize.css when:**
```css
/* Content-heavy websites */
.blog-content {
  /* Want semantic HTML to look decent by default */
}

/* Rapid prototyping */
.prototype {
  /* Want basic styling without much custom CSS */
}

/* Legacy browser support */
.enterprise-app {
  /* Need documented fixes for browser quirks */
}
```

**✅ Use Modern Hybrid when:**
```css
/* Modern web applications */
.modern-app {
  /* Want minimal reset + modern best practices */
}

/* Progressive web apps */
.pwa {
  /* Need mobile-optimized foundation */
}

/* Design systems */
.design-tokens {
  /* Want controlled foundation for token system */
}
```

#### **🔧 IMPLEMENTATION STRATEGIES:**

**1. NPM Package Integration:**
```bash
# Install normalize.css
npm install normalize.css

# Install modern-normalize
npm install modern-normalize

# Install sanitize.css (alternative)
npm install sanitize.css
```

```typescript
// ✅ Import in your main CSS/JS file
import 'normalize.css';
// or
import 'modern-normalize';

// ✅ Or in CSS
@import 'normalize.css';
@import url('https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css');
```

**2. Custom Reset with CSS Custom Properties:**
```css
/* ✅ Configurable reset using CSS variables */
:root {
  --reset-font-family: -apple-system, BlinkMacSystemFont, sans-serif;
  --reset-line-height: 1.5;
  --reset-focus-color: #4A90E2;
  --reset-focus-offset: 2px;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: var(--reset-font-family);
  line-height: var(--reset-line-height);
}

:focus-visible {
  outline: 2px solid var(--reset-focus-color);
  outline-offset: var(--reset-focus-offset);
}
```

#### **📱 MOBILE-SPECIFIC CONSIDERATIONS:**

```css
/* ✅ Mobile-optimized reset additions */
html {
  /* Prevent zoom on orientation change */
  -webkit-text-size-adjust: 100%;
  -ms-text-size-adjust: 100%;

  /* Better mobile scrolling */
  -webkit-overflow-scrolling: touch;

  /* Disable pull-to-refresh */
  overscroll-behavior-y: contain;
}

body {
  /* Disable rubber band scrolling */
  overscroll-behavior: contain;

  /* Better mobile font rendering */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

/* Touch-friendly tap targets */
button, input, select, textarea, a {
  /* Minimum 44px touch target */
  min-height: 44px;

  /* Remove tap highlights */
  -webkit-tap-highlight-color: transparent;
}

/* Disable user select on UI elements */
button, .ui-element {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
```

#### **🧪 TESTING CROSS-BROWSER CONSISTENCY:**

```css
/* ✅ Visual test for reset effectiveness */
.reset-test {
  /* All these should look identical across browsers */
  margin: 20px;
  padding: 20px;
  border: 1px solid #ccc;
}

.reset-test h1 { font-size: 2em; }
.reset-test h2 { font-size: 1.5em; }
.reset-test p { margin: 1em 0; }
.reset-test ul { margin: 1em 0; padding-left: 2em; }
.reset-test button { padding: 0.5em 1em; }
```

**💡 GHI NHỚ:**
- **CSS Reset** = **Nuclear** approach, start from zero 💥
- **Normalize** = **Surgical** fixes, preserve useful defaults 🔧
- **Modern Hybrid** = **Best of both**, optimized for modern web 🚀
- **Always test** across target browsers 🧪

**Reset Strategy: Choose based on project needs → Apply early → Test consistently → Document decisions!** 🎯

---

### CSS10: Pseudo-classes và Pseudo-elements trong CSS?

**Trả lời:**

**Pseudo-classes** và **Pseudo-elements** là **POWERFUL CSS SELECTORS** để target elements based on **STATE** hoặc **STRUCTURE**. Hiểu rõ differences và use cases là **ESSENTIAL** cho advanced CSS.

#### **🔥 PSEUDO-CLASSES vs PSEUDO-ELEMENTS:**

| Aspect | **Pseudo-classes (`:`)** | **Pseudo-elements (`::`)** |
|--------|-------------------------|---------------------------|
| **Syntax** | **Single colon `:hover`** | **Double colon `::before`** |
| **Purpose** | **Target element STATES** | **Target element PARTS** |
| **Examples** | `:hover`, `:focus`, `:nth-child` | `::before`, `::after`, `::first-line` |
| **DOM Impact** | **No DOM manipulation** | **Creates virtual elements** |
| **Styling** | **Styles existing elements** | **Styles generated content** |

#### **🎯 COMMON PSEUDO-CLASSES:**

**1. User Action Pseudo-classes:**
```css
/* ✅ HOVER STATES */
.button {
  background: #3b82f6;
  color: white;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 0.375rem;
  cursor: pointer;
  transition: all 0.2s ease;
}

.button:hover {
  background: #2563eb;
  transform: translateY(-1px);
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.button:active {
  background: #1d4ed8;
  transform: translateY(0);
}

.button:focus {
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3);
}

/* ✅ FOCUS MANAGEMENT */
.input {
  border: 1px solid #d1d5db;
  padding: 0.5rem;
  border-radius: 0.375rem;
  transition: border-color 0.2s ease;
}

.input:focus {
  border-color: #3b82f6;
  outline: none;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.input:focus-visible {
  /* Only show focus for keyboard users */
  border-color: #3b82f6;
}

.input:focus:not(:focus-visible) {
  /* Hide focus for mouse users */
  box-shadow: none;
}

/* ✅ VISITED LINKS */
.link {
  color: #3b82f6;
  text-decoration: none;
}

.link:visited {
  color: #7c3aed;  /* Purple for visited links */
}

.link:hover {
  text-decoration: underline;
}
```

**2. Structural Pseudo-classes:**
```css
/* ✅ NTH-CHILD PATTERNS */
.grid-item:nth-child(odd) {
  background: #f9fafb;    /* Zebra striping */
}

.grid-item:nth-child(even) {
  background: white;
}

.grid-item:nth-child(3n) {
  /* Every 3rd item */
  border-right: 3px solid #3b82f6;
}

.grid-item:nth-child(3n+1) {
  /* 1st, 4th, 7th, etc. */
  margin-left: 0;
}

/* ✅ FIRST/LAST CHILD */
.card:first-child {
  margin-top: 0;
  border-radius: 0.5rem 0.5rem 0 0;
}

.card:last-child {
  margin-bottom: 0;
  border-radius: 0 0 0.5rem 0.5rem;
}

.card:only-child {
  border-radius: 0.5rem;
  margin: 0;
}

/* ✅ FIRST/LAST OF TYPE */
.article h2:first-of-type {
  margin-top: 0;
  font-size: 2rem;
}

.article p:last-of-type {
  margin-bottom: 0;
}

/* ✅ EMPTY/NOT SELECTORS */
.message:empty {
  display: none;
}

.message:not(:empty) {
  padding: 1rem;
  border: 1px solid #e5e7eb;
}

.input:not(:disabled):hover {
  border-color: #9ca3af;
}

.button:not(.primary):not(.secondary) {
  background: #6b7280;
}
```

**3. Form Pseudo-classes:**
```css
/* ✅ FORM VALIDATION STATES */
.form-field {
  margin-bottom: 1rem;
}

.input:valid {
  border-color: #10b981;
}

.input:invalid:not(:focus):not(:placeholder-shown) {
  border-color: #ef4444;
}

.input:required:invalid {
  background-image: url('data:image/svg+xml;utf8,<svg>...</svg>');
  background-position: right 0.5rem center;
  background-repeat: no-repeat;
}

/* ✅ CHECKBOX/RADIO STYLING */
.checkbox:checked + .label {
  font-weight: 600;
  color: #3b82f6;
}

.checkbox:checked + .label::before {
  background: #3b82f6;
  content: '✓';
  color: white;
}

.radio:checked + .label {
  background: #eff6ff;
  border-color: #3b82f6;
}

/* ✅ DISABLED STATES */
.input:disabled {
  background: #f3f4f6;
  color: #9ca3af;
  cursor: not-allowed;
}

.button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  transform: none !important;
}
```

#### **🎨 PSEUDO-ELEMENTS:**

**1. `::before` và `::after`:**
```css
/* ✅ DECORATIVE ELEMENTS */
.quote {
  position: relative;
  padding: 1rem 2rem;
  font-style: italic;
  background: #f8fafc;
  border-left: 4px solid #3b82f6;
}

.quote::before {
  content: '"';
  position: absolute;
  top: -0.5rem;
  left: 0.5rem;
  font-size: 3rem;
  color: #3b82f6;
  font-weight: bold;
  line-height: 1;
}

.quote::after {
  content: '"';
  position: absolute;
  bottom: -1rem;
  right: 0.5rem;
  font-size: 3rem;
  color: #3b82f6;
  font-weight: bold;
  line-height: 1;
}

/* ✅ ICON ADDITIONS */
.external-link::after {
  content: ' ↗';
  font-size: 0.875rem;
  color: #6b7280;
}

.download-link::before {
  content: '⬇ ';
  color: #10b981;
}

.email-link::before {
  content: '✉ ';
  color: #3b82f6;
}

/* ✅ TOOLTIPS */
.tooltip {
  position: relative;
  cursor: help;
  border-bottom: 1px dotted #6b7280;
}

.tooltip::after {
  content: attr(data-tooltip);
  position: absolute;
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  background: #1f2937;
  color: white;
  padding: 0.5rem;
  border-radius: 0.25rem;
  font-size: 0.875rem;
  white-space: nowrap;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.2s ease;
  z-index: 1000;
}

.tooltip:hover::after {
  opacity: 1;
}

/* ✅ LOADING SPINNER */
.loading::after {
  content: '';
  width: 20px;
  height: 20px;
  border: 2px solid #e5e7eb;
  border-top: 2px solid #3b82f6;
  border-radius: 50%;
  animation: spin 1s linear infinite;
  display: inline-block;
  margin-left: 0.5rem;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
```

**2. Typography Pseudo-elements:**
```css
/* ✅ FIRST LINE/LETTER STYLING */
.article p::first-line {
  font-weight: 600;
  color: #374151;
  font-size: 1.1em;
}

.chapter::first-letter {
  float: left;
  font-size: 4rem;
  font-weight: bold;
  line-height: 1;
  margin: 0 0.5rem 0 0;
  color: #3b82f6;
  font-family: Georgia, serif;
}

/* ✅ SELECTION STYLING */
::selection {
  background: #3b82f6;
  color: white;
}

::-moz-selection {
  background: #3b82f6;
  color: white;
}

/* ✅ PLACEHOLDER STYLING */
.input::placeholder {
  color: #9ca3af;
  opacity: 1;
  font-style: italic;
}

.input::-webkit-input-placeholder {
  color: #9ca3af;
  opacity: 1;
}

.input::-moz-placeholder {
  color: #9ca3af;
  opacity: 1;
}
```

#### **🚀 ADVANCED PSEUDO-CLASS COMBINATIONS:**

```css
/* ✅ COMPLEX SELECTORS */

/* Target specific patterns */
.nav-item:nth-child(3n+1):not(:last-child) {
  /* 1st, 4th, 7th items (but not if they're the last) */
  margin-right: auto;
}

/* Form validation combinations */
.input:required:invalid:not(:focus):not(:placeholder-shown) {
  /* Required field that's invalid, not focused, and has content */
  border-color: #ef4444;
  background-color: #fef2f2;
}

.input:valid:not(:placeholder-shown) {
  /* Valid field with content */
  border-color: #10b981;
}

/* Hover states with conditions */
.card:hover:not(.disabled):not(.loading) {
  /* Only hover if not disabled or loading */
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

/* State combinations */
.button:focus:hover:not(:active) {
  /* Focused and hovered but not being clicked */
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.3),
              0 4px 8px rgba(0, 0, 0, 0.1);
}
```

#### **🎯 PRACTICAL EXAMPLES:**

**1. Card Component với Pseudo-classes:**
```css
.card {
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0.5rem;
  padding: 1.5rem;
  transition: all 0.2s ease;
  cursor: pointer;
}

.card:hover {
  border-color: #3b82f6;
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.card:active {
  transform: translateY(0);
}

.card:focus-within {
  /* Style card if any child element is focused */
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.card:target {
  /* Style card when it's the target of a URL fragment */
  border-color: #f59e0b;
  background: #fffbeb;
}
```

**2. Form với Advanced Pseudo-classes:**
```css
.form-group {
  margin-bottom: 1rem;
}

.form-input {
  width: 100%;
  padding: 0.75rem;
  border: 1px solid #d1d5db;
  border-radius: 0.375rem;
  transition: all 0.2s ease;
}

.form-input:focus {
  outline: none;
  border-color: #3b82f6;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

.form-input:user-invalid {
  /* Only show error after user interaction */
  border-color: #ef4444;
  background-color: #fef2f2;
}

.form-input:user-valid {
  /* Show success after user interaction */
  border-color: #10b981;
  background-color: #f0fdf4;
}

.form-input:placeholder-shown {
  /* Style when placeholder is visible */
  font-style: italic;
}

.form-input:in-range {
  /* For number inputs within valid range */
  border-color: #10b981;
}

.form-input:out-of-range {
  /* For number inputs outside valid range */
  border-color: #ef4444;
}
```

**3. Navigation với Pseudo-elements:**
```css
.nav-link {
  position: relative;
  padding: 0.5rem 1rem;
  color: #6b7280;
  text-decoration: none;
  transition: color 0.2s ease;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: #3b82f6;
  transition: width 0.3s ease;
}

.nav-link:hover {
  color: #3b82f6;
}

.nav-link:hover::after {
  width: 100%;
}

.nav-link.active {
  color: #3b82f6;
}

.nav-link.active::after {
  width: 100%;
}

/* Badge with counter */
.nav-item {
  position: relative;
}

.nav-item[data-count]::after {
  content: attr(data-count);
  position: absolute;
  top: -0.5rem;
  right: -0.5rem;
  background: #ef4444;
  color: white;
  border-radius: 50%;
  width: 1.25rem;
  height: 1.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: bold;
}
```

#### **📱 RESPONSIVE PSEUDO-CLASSES:**

```css
/* ✅ Media query pseudo-classes */
@media (hover: hover) {
  /* Only apply hover on devices that support it */
  .button:hover {
    background: #2563eb;
  }
}

@media (hover: none) {
  /* Mobile devices without hover */
  .button:active {
    background: #2563eb;
  }
}

/* ✅ Container queries with pseudo-classes */
.card-container {
  container-type: inline-size;
}

@container (min-width: 300px) {
  .card:nth-child(even) {
    background: #f8fafc;
  }
}
```

**💡 GHI NHỚ:**
- **Pseudo-classes (`:`)** = Element **STATES** 🎭
- **Pseudo-elements (`::`)** = Element **PARTS** 🧩
- **`:not()`** = Exclusion logic ❌
- **`::before/::after`** = Generated content ✨

**Pseudo Strategy: Use pseudo-classes for states → Use pseudo-elements for decoration → Combine for complex patterns!** 🎯

---

### CSS11: `display: none` vs `visibility: hidden` - Performance Impact?

**Trả lời:**

`display: none` và `visibility: hidden` đều **HIDE ELEMENTS** nhưng có **FUNDAMENTAL DIFFERENCES** về **DOM flow**, **performance**, và **browser rendering**. Hiểu rõ differences là **CRUCIAL** cho optimization.

#### **🔥 CORE DIFFERENCES:**

| Aspect | **`display: none`** | **`visibility: hidden`** |
|--------|---------------------|--------------------------|
| **DOM Flow** | ❌ **Removed from flow** | ✅ **Remains in flow** |
| **Space Occupation** | ❌ **No space taken** | ✅ **Space preserved** |
| **Child Elements** | **All children hidden** | **Children can override** |
| **Event Handling** | ❌ **No events triggered** | ❌ **No events triggered** |
| **Accessibility** | **Screen readers ignore** | **Screen readers ignore** |
| **Performance** | **🔥 Triggers Reflow** | **⚡ Only Repaint** |

#### **📊 PERFORMANCE COMPARISON:**

```css
/* 🔥 DISPLAY: NONE - Heavy Performance Impact */
.element-display-none {
  display: none;  /* Element completely removed from render tree */
}

/* PERFORMANCE IMPACT:
 * 1. REFLOW: Layout recalculation required
 * 2. REPAINT: Visual update needed
 * 3. COMPOSITE: Layer updates if needed
 * 4. JavaScript: offsetHeight, offsetWidth return 0
 */

/* ⚡ VISIBILITY: HIDDEN - Light Performance Impact */
.element-visibility-hidden {
  visibility: hidden;  /* Element invisible but space maintained */
}

/* PERFORMANCE IMPACT:
 * 1. REPAINT: Only visual update (no layout change)
 * 2. Layout: Preserved (no reflow needed)
 * 3. JavaScript: offsetHeight, offsetWidth return actual values
 */
```

#### **🎯 PRACTICAL PERFORMANCE EXAMPLES:**

**1. Animation Performance Comparison:**
```css
/* ❌ BAD: Frequent display toggles cause layout thrashing */
.modal-bad {
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: all 0.3s ease;
}

.modal-bad.show {
  display: block;  /* Triggers REFLOW on every show/hide */
}

/* ⚡ BETTER: Visibility preserves layout */
.modal-better {
  visibility: hidden;
  opacity: 0;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.modal-better.show {
  visibility: visible;
  opacity: 1;      /* Only REPAINT, no REFLOW */
}

/* ✅ BEST: Transform-based approach (GPU accelerated) */
.modal-best {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0);
  opacity: 0;
  transition: transform 0.3s ease, opacity 0.3s ease;
  pointer-events: none;
}

.modal-best.show {
  transform: translate(-50%, -50%) scale(1);
  opacity: 1;
  pointer-events: auto;  /* Only COMPOSITE layer update */
}
```

**2. List Item Performance:**
```css
/* 🔥 PERFORMANCE BOTTLENECK: display: none on large lists */
.list-item {
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
  transition: all 0.2s ease;
}

/* ❌ BAD: Each toggle causes layout recalculation */
.list-item.hidden-bad {
  display: none;  /* Entire list layout recalculated */
}

/* ⚡ BETTER: Visibility preserves list layout */
.list-item.hidden-better {
  visibility: hidden;  /* List layout preserved */
}

/* ✅ BEST: Virtual scrolling approach */
.list-item.hidden-best {
  height: 0;
  overflow: hidden;
  padding: 0;
  margin: 0;
  border: none;
  transition: height 0.2s ease, padding 0.2s ease;
}

.list-item.visible-best {
  height: auto;
  padding: 1rem;
  border-bottom: 1px solid #e5e7eb;
}
```

#### **⚡ BROWSER RENDERING PIPELINE:**

```css
/* UNDERSTANDING THE RENDERING PIPELINE */

/* 1. REFLOW (Layout) - Most Expensive */
.trigger-reflow {
  display: none;          /* ✓ Triggers */
  width: 100px;          /* ✓ Triggers */
  height: 100px;         /* ✓ Triggers */
  padding: 10px;         /* ✓ Triggers */
  margin: 10px;          /* ✓ Triggers */
  border: 1px solid;     /* ✓ Triggers */
  font-size: 14px;       /* ✓ Triggers */
  position: absolute;    /* ✓ Triggers (sometimes) */
}

/* 2. REPAINT - Moderate Cost */
.trigger-repaint {
  visibility: hidden;    /* ✓ Triggers */
  color: red;           /* ✓ Triggers */
  background: blue;     /* ✓ Triggers */
  box-shadow: 0 0 5px;  /* ✓ Triggers */
  border-color: green;  /* ✓ Triggers */
  outline: 2px solid;   /* ✓ Triggers */
}

/* 3. COMPOSITE - Least Expensive (GPU) */
.trigger-composite {
  transform: scale(0);   /* ✓ GPU accelerated */
  opacity: 0;           /* ✓ GPU accelerated */
  filter: blur(5px);    /* ✓ GPU accelerated */
  will-change: transform; /* ✓ Force GPU layer */
}
```

#### **🚀 MODERN PERFORMANCE TECHNIQUES:**

**1. CSS Containment for Performance:**
```css
/* ✅ CSS Containment - Isolate layout calculations */
.container {
  contain: layout style paint;  /* Isolate expensive operations */
}

.container .item {
  /* Changes here won't affect parent layout */
  display: none;  /* Reflow contained within .container */
}

/* ✅ Container queries for responsive hiding */
.responsive-container {
  container-type: inline-size;
}

@container (max-width: 300px) {
  .optional-content {
    display: none;  /* Contextual hiding based on container size */
  }
}
```

**2. Performance-Optimized Toggle Patterns:**
```typescript
// ✅ PERFORMANCE-AWARE TOGGLE IMPLEMENTATION
interface ElementToggleOptions {
  method: 'display' | 'visibility' | 'transform' | 'clip-path';
  duration?: number;
  easing?: string;
}

class PerformantToggle {
  private element: HTMLElement;
  private isVisible: boolean = true;

  constructor(element: HTMLElement) {
    this.element = element;
    this.setupGPULayer();
  }

  private setupGPULayer(): void {
    // Force GPU layer for better performance
    this.element.style.willChange = 'transform, opacity';
    this.element.style.backfaceVisibility = 'hidden';
  }

  // ⚡ FAST: GPU-accelerated approach
  toggleWithTransform(show: boolean): void {
    if (show) {
      this.element.style.transform = 'scale(1)';
      this.element.style.opacity = '1';
      this.element.style.pointerEvents = 'auto';
    } else {
      this.element.style.transform = 'scale(0)';
      this.element.style.opacity = '0';
      this.element.style.pointerEvents = 'none';
    }
    this.isVisible = show;
  }

  // 🔥 SLOW: Layout-affecting approach
  toggleWithDisplay(show: boolean): void {
    this.element.style.display = show ? 'block' : 'none';
    this.isVisible = show;
    // This will trigger reflow and affect performance
  }

  // ⚡ MEDIUM: Repaint-only approach
  toggleWithVisibility(show: boolean): void {
    this.element.style.visibility = show ? 'visible' : 'hidden';
    this.element.style.opacity = show ? '1' : '0';
    this.isVisible = show;
  }

  // ✅ BEST: Clip-path approach (modern browsers)
  toggleWithClipPath(show: boolean): void {
    if (show) {
      this.element.style.clipPath = 'inset(0)';
      this.element.style.opacity = '1';
    } else {
      this.element.style.clipPath = 'inset(100%)';
      this.element.style.opacity = '0';
    }
    this.isVisible = show;
  }

  // 📊 Performance measurement
  measureTogglePerformance(method: keyof PerformantToggle, iterations: number = 100): number {
    const start = performance.now();

    for (let i = 0; i < iterations; i++) {
      (this[method] as Function)(i % 2 === 0);
    }

    const end = performance.now();
    return end - start;
  }
}

// ✅ Usage example
const element = document.querySelector('.toggle-element') as HTMLElement;
const toggle = new PerformantToggle(element);

// Measure different approaches
const displayTime = toggle.measureTogglePerformance('toggleWithDisplay');
const visibilityTime = toggle.measureTogglePerformance('toggleWithVisibility');
const transformTime = toggle.measureTogglePerformance('toggleWithTransform');

console.log('Performance Results:');
console.log(`Display toggle: ${displayTime}ms`);
console.log(`Visibility toggle: ${visibilityTime}ms`);
console.log(`Transform toggle: ${transformTime}ms`);
```

#### **🎯 USE CASE RECOMMENDATIONS:**

**✅ Use `display: none` when:**
```css
/* 1. Complete removal needed */
.modal {
  display: none;  /* Modal completely removed when closed */
}

.modal.open {
  display: flex;
}

/* 2. Responsive design (one-time layout change) */
@media (max-width: 768px) {
  .desktop-only {
    display: none;  /* Permanent hide on mobile */
  }
}

/* 3. Content that affects layout significantly */
.sidebar {
  display: none;  /* Sidebar collapse affects main content width */
}

.sidebar.open {
  display: block;
}
```

**✅ Use `visibility: hidden` when:**
```css
/* 1. Maintain layout spacing */
.placeholder {
  visibility: hidden;  /* Keep space for content loading */
}

.placeholder.loaded {
  visibility: visible;
}

/* 2. Animation sequences */
.fade-sequence .item {
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.fade-sequence .item.show {
  visibility: visible;
  opacity: 1;
}

/* 3. Print styles */
@media print {
  .no-print {
    visibility: hidden;  /* Hide but maintain layout */
  }
}
```

**✅ Use modern alternatives when:**
```css
/* 1. Frequent toggling (animations) */
.performance-critical {
  transform: scale(1);
  opacity: 1;
  transition: transform 0.2s ease, opacity 0.2s ease;
}

.performance-critical.hidden {
  transform: scale(0);
  opacity: 0;
  pointer-events: none;
}

/* 2. GPU acceleration needed */
.gpu-optimized {
  will-change: transform, opacity;
  transform: translateZ(0);  /* Force GPU layer */
}

/* 3. Complex clip animations */
.clip-reveal {
  clip-path: inset(0 0 0 0);
  transition: clip-path 0.5s ease;
}

.clip-reveal.hidden {
  clip-path: inset(0 0 100% 0);
}
```

#### **📱 MOBILE PERFORMANCE CONSIDERATIONS:**

```css
/* ✅ Mobile-optimized hiding strategies */

/* 1. Reduce layout calculations on mobile */
@media (max-width: 768px) {
  .mobile-performance {
    /* Prefer transform over display for mobile */
    transform: scale(1);
    transition: transform 0.2s ease;
  }

  .mobile-performance.hidden {
    transform: scale(0);
    pointer-events: none;
  }
}

/* 2. Intersection Observer approach */
.lazy-content {
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.3s ease, transform 0.3s ease;
}

.lazy-content.visible {
  opacity: 1;
  transform: translateY(0);
}

/* 3. Content priority for mobile */
.mobile-secondary {
  /* Use visibility for less important content */
  visibility: visible;
  opacity: 1;
  transition: opacity 0.2s ease, visibility 0.2s ease;
}

@media (max-width: 480px) {
  .mobile-secondary {
    visibility: hidden;
    opacity: 0;
  }
}
```

#### **🧪 PERFORMANCE TESTING:**

```typescript
// ✅ Performance testing utility
class HideShowPerformanceTester {
  private container: HTMLElement;
  private items: HTMLElement[] = [];

  constructor(containerSelector: string, itemCount: number = 1000) {
    this.container = document.querySelector(containerSelector)!;
    this.createTestItems(itemCount);
  }

  private createTestItems(count: number): void {
    for (let i = 0; i < count; i++) {
      const item = document.createElement('div');
      item.className = 'test-item';
      item.textContent = `Item ${i}`;
      item.style.cssText = `
        padding: 10px;
        margin: 2px;
        background: #f0f0f0;
        border: 1px solid #ddd;
      `;
      this.container.appendChild(item);
      this.items.push(item);
    }
  }

  // Test display: none performance
  testDisplayNone(iterations: number = 10): number {
    const start = performance.now();

    for (let i = 0; i < iterations; i++) {
      this.items.forEach((item, index) => {
        item.style.display = index % 2 === i % 2 ? 'none' : 'block';
      });
    }

    return performance.now() - start;
  }

  // Test visibility: hidden performance
  testVisibilityHidden(iterations: number = 10): number {
    const start = performance.now();

    for (let i = 0; i < iterations; i++) {
      this.items.forEach((item, index) => {
        item.style.visibility = index % 2 === i % 2 ? 'hidden' : 'visible';
      });
    }

    return performance.now() - start;
  }

  // Test transform performance
  testTransform(iterations: number = 10): number {
    const start = performance.now();

    for (let i = 0; i < iterations; i++) {
      this.items.forEach((item, index) => {
        item.style.transform = index % 2 === i % 2 ? 'scale(0)' : 'scale(1)';
      });
    }

    return performance.now() - start;
  }

  // Run comprehensive test
  runPerformanceTest(): void {
    console.log('🧪 Running Hide/Show Performance Tests...\n');

    const displayTime = this.testDisplayNone();
    const visibilityTime = this.testVisibilityHidden();
    const transformTime = this.testTransform();

    console.log(`📊 Results for ${this.items.length} items:`);
    console.log(`Display none: ${displayTime.toFixed(2)}ms`);
    console.log(`Visibility hidden: ${visibilityTime.toFixed(2)}ms`);
    console.log(`Transform scale: ${transformTime.toFixed(2)}ms`);

    const fastest = Math.min(displayTime, visibilityTime, transformTime);
    console.log(`\n⚡ Fastest method: ${fastest === displayTime ? 'display: none' :
                                         fastest === visibilityTime ? 'visibility: hidden' :
                                         'transform: scale'}`);
  }
}

// Usage
const tester = new HideShowPerformanceTester('#test-container', 1000);
tester.runPerformanceTest();
```

**💡 GHI NHỚ:**
- **`display: none`** = **Removes from flow**, triggers **REFLOW** 🔥
- **`visibility: hidden`** = **Preserves space**, only **REPAINT** ⚡
- **Transform/Opacity** = **GPU accelerated**, only **COMPOSITE** ✨
- **Choose based on** = Layout impact vs Performance needs 🎯

**Performance Strategy: GPU layers (transform) > Visibility (repaint) > Display (reflow)!** 🚀

---

### CSS12: Flexbox vs CSS Grid - Khi nào sử dụng cái nào?

**Trả lời:**

**Flexbox** và **CSS Grid** là hai **POWERFUL LAYOUT SYSTEMS** với **different strengths**. Hiểu rõ **when to use what** là **CRITICAL** cho optimal layout design và performance.

#### **🔥 FUNDAMENTAL DIFFERENCES:**

| Aspect | **Flexbox** | **CSS Grid** |
|--------|-------------|--------------|
| **Dimension** | **1D Layout** (row OR column) | **2D Layout** (rows AND columns) |
| **Content** | **Content-driven** | **Container-driven** |
| **Alignment** | **Excellent for centering** | **Excellent for positioning** |
| **Use Case** | **Components, UI elements** | **Page layouts, complex grids** |
| **Browser Support** | **Excellent (IE10+)** | **Good (IE11+ with prefixes)** |
| **Learning Curve** | **Easier to learn** | **More complex but powerful** |

#### **📊 FLEXBOX - 1D LAYOUT MASTER:**

```css
/* ✅ FLEXBOX FUNDAMENTALS */
.flex-container {
  display: flex;

  /* Main axis control */
  flex-direction: row;        /* row | column | row-reverse | column-reverse */
  justify-content: center;    /* start | end | center | space-between | space-around | space-evenly */

  /* Cross axis control */
  align-items: center;        /* start | end | center | stretch | baseline */

  /* Multi-line control */
  flex-wrap: wrap;           /* nowrap | wrap | wrap-reverse */
  align-content: center;     /* start | end | center | stretch | space-between | space-around */

  /* Shorthand */
  flex-flow: row wrap;       /* flex-direction + flex-wrap */
  gap: 1rem;                 /* Modern spacing */
}

.flex-item {
  /* Growth and shrink */
  flex-grow: 1;              /* How much to grow */
  flex-shrink: 1;            /* How much to shrink */
  flex-basis: auto;          /* Initial size */

  /* Shorthand */
  flex: 1 1 auto;            /* grow shrink basis */

  /* Individual alignment */
  align-self: center;        /* Override container align-items */
}
```

**Flexbox Perfect Use Cases:**
```css
/* ✅ 1. NAVIGATION BARS */
.navbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

.navbar__logo {
  flex-shrink: 0;           /* Don't shrink logo */
}

.navbar__menu {
  display: flex;
  gap: 2rem;
  list-style: none;
}

.navbar__actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

/* ✅ 2. BUTTON GROUPS */
.button-group {
  display: flex;
  gap: 0.5rem;
  align-items: center;
}

.button-group .button {
  flex: 1;                  /* Equal width buttons */
  min-width: 0;            /* Allow shrinking */
}

.button-group .button.primary {
  flex: 2;                  /* Primary button twice as wide */
}

/* ✅ 3. MEDIA OBJECTS */
.media-object {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}

.media-object__image {
  flex-shrink: 0;           /* Image doesn't shrink */
  width: 64px;
  height: 64px;
}

.media-object__content {
  flex: 1;                  /* Content takes remaining space */
  min-width: 0;            /* Allow text overflow */
}

/* ✅ 4. FORM LAYOUTS */
.form-row {
  display: flex;
  gap: 1rem;
  align-items: flex-start;
}

.form-row .field {
  flex: 1;                  /* Equal width fields */
}

.form-row .field.small {
  flex: 0 0 100px;         /* Fixed width field */
}

.form-row .field.large {
  flex: 2;                  /* Double width field */
}

/* ✅ 5. CENTERING (Flexbox specialty) */
.perfect-center {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;        /* Full viewport height */
}

.card-center {
  width: 400px;
  padding: 2rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
```

#### **🏗️ CSS GRID - 2D LAYOUT POWERHOUSE:**

```css
/* ✅ CSS GRID FUNDAMENTALS */
.grid-container {
  display: grid;

  /* Define columns */
  grid-template-columns: 1fr 2fr 1fr;           /* Fractional units */
  grid-template-columns: 200px auto 100px;     /* Mixed units */
  grid-template-columns: repeat(3, 1fr);       /* Repeat pattern */
  grid-template-columns: minmax(200px, 1fr) repeat(2, 200px);

  /* Define rows */
  grid-template-rows: 100px auto 50px;
  grid-template-rows: repeat(3, minmax(100px, auto));

  /* Named grid lines */
  grid-template-columns: [sidebar-start] 250px [sidebar-end main-start] 1fr [main-end];

  /* Grid areas */
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";

  /* Gaps */
  gap: 1rem;                    /* row-gap + column-gap */
  row-gap: 1rem;
  column-gap: 2rem;

  /* Alignment */
  justify-items: center;        /* Align items horizontally */
  align-items: center;          /* Align items vertically */
  justify-content: center;      /* Align grid horizontally */
  align-content: center;        /* Align grid vertically */
}

.grid-item {
  /* Positioning */
  grid-column: 1 / 3;          /* Span from line 1 to 3 */
  grid-row: 2 / 4;             /* Span from line 2 to 4 */

  /* Shorthand */
  grid-area: 2 / 1 / 4 / 3;    /* row-start / col-start / row-end / col-end */

  /* Named areas */
  grid-area: header;

  /* Individual alignment */
  justify-self: stretch;        /* Override container justify-items */
  align-self: start;           /* Override container align-items */
}
```

**CSS Grid Perfect Use Cases:**
```css
/* ✅ 1. PAGE LAYOUTS */
.page-layout {
  display: grid;
  grid-template-areas:
    "header header header"
    "sidebar main aside"
    "footer footer footer";
  grid-template-columns: 250px 1fr 200px;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
  gap: 1rem;
}

.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.main { grid-area: main; }
.aside { grid-area: aside; }
.footer { grid-area: footer; }

/* ✅ 2. CARD GRIDS */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  padding: 2rem;
}

/* Auto-responsive without media queries! */
.card-grid .card {
  background: white;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

/* ✅ 3. COMPLEX LAYOUTS */
.dashboard {
  display: grid;
  grid-template-areas:
    "header header header header"
    "sidebar stats stats actions"
    "sidebar chart chart chart"
    "sidebar recent recent recent";
  grid-template-columns: 200px 1fr 1fr 200px;
  grid-template-rows: 60px 100px 300px 1fr;
  gap: 1rem;
  height: 100vh;
}

.dashboard-header { grid-area: header; }
.dashboard-sidebar { grid-area: sidebar; }
.dashboard-stats { grid-area: stats; }
.dashboard-actions { grid-area: actions; }
.dashboard-chart { grid-area: chart; }
.dashboard-recent { grid-area: recent; }

/* ✅ 4. MASONRY-LIKE LAYOUTS */
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-auto-rows: 20px;        /* Small row height */
  gap: 1rem;
}

.masonry-item {
  grid-row-end: span var(--span);  /* Dynamic spanning */
}

/* ✅ 5. FORM GRIDS */
.form-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);  /* 12-column system */
  gap: 1rem;
}

.form-grid .field-full {
  grid-column: 1 / -1;         /* Full width */
}

.form-grid .field-half {
  grid-column: span 6;         /* Half width */
}

.form-grid .field-third {
  grid-column: span 4;         /* Third width */
}

.form-grid .field-quarter {
  grid-column: span 3;         /* Quarter width */
}
```

#### **🚀 MODERN RESPONSIVE PATTERNS:**

**1. Flexbox for Component Layout:**
```css
/* ✅ Responsive navigation with Flexbox */
.responsive-nav {
  display: flex;
  flex-direction: column;      /* Mobile: stack vertically */
  gap: 1rem;
}

.responsive-nav__brand {
  flex-shrink: 0;
}

.responsive-nav__menu {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

@media (min-width: 768px) {
  .responsive-nav {
    flex-direction: row;       /* Desktop: horizontal */
    justify-content: space-between;
    align-items: center;
  }

  .responsive-nav__menu {
    flex-direction: row;
    gap: 2rem;
  }
}

/* ✅ Flexible button groups */
.action-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  justify-content: flex-end;
}

.action-bar .button {
  flex: 0 1 auto;             /* Don't grow, can shrink */
  min-width: fit-content;
}

@media (max-width: 480px) {
  .action-bar {
    justify-content: stretch;
  }

  .action-bar .button {
    flex: 1;                   /* Equal width on mobile */
  }
}
```

**2. Grid for Layout Structure:**
```css
/* ✅ Responsive grid layout */
.responsive-layout {
  display: grid;
  grid-template-areas:
    "header"
    "main"
    "sidebar"
    "footer";
  grid-template-rows: auto 1fr auto auto;
  min-height: 100vh;
  gap: 1rem;
}

@media (min-width: 768px) {
  .responsive-layout {
    grid-template-areas:
      "header header"
      "sidebar main"
      "footer footer";
    grid-template-columns: 250px 1fr;
    grid-template-rows: auto 1fr auto;
  }
}

@media (min-width: 1024px) {
  .responsive-layout {
    grid-template-areas:
      "header header header"
      "sidebar main aside"
      "footer footer footer";
    grid-template-columns: 200px 1fr 200px;
  }
}

/* ✅ Auto-responsive content grid */
.content-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(300px, 100%), 1fr));
  gap: 2rem;
}
```

#### **⚖️ DECISION FRAMEWORK:**

**Choose Flexbox for:**
```css
/* 1D layouts, content-driven sizing */
.choose-flexbox {
  /* ✅ Navigation bars */
  /* ✅ Button groups */
  /* ✅ Media objects */
  /* ✅ Form controls */
  /* ✅ Centering content */
  /* ✅ Distributing space */
  /* ✅ Component-level layout */
}
```

**Choose Grid for:**
```css
/* 2D layouts, container-driven sizing */
.choose-grid {
  /* ✅ Page layouts */
  /* ✅ Card grids */
  /* ✅ Complex alignments */
  /* ✅ Overlapping content */
  /* ✅ Template-based designs */
  /* ✅ Responsive without media queries */
  /* ✅ Application-level layout */
}
```

#### **🎯 HYBRID APPROACH (Best Practice):**

```css
/* ✅ COMBINING FLEXBOX + GRID */

/* Grid for overall page structure */
.app-layout {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  grid-template-columns: 250px 1fr;
  grid-template-rows: auto 1fr auto;
  min-height: 100vh;
}

/* Flexbox for header components */
.header {
  grid-area: header;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem 2rem;
}

.header__nav {
  display: flex;
  gap: 2rem;
  align-items: center;
}

/* Grid for main content area */
.main-content {
  grid-area: main;
  display: grid;
  grid-template-rows: auto 1fr;
  gap: 2rem;
  padding: 2rem;
}

/* Flexbox for content sections */
.content-section {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.content-actions {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

/* Grid for card layouts within sections */
.section-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
}

/* Flexbox for individual card content */
.card {
  display: flex;
  flex-direction: column;
  padding: 1.5rem;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card__header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.card__content {
  flex: 1;                    /* Grow to fill space */
}

.card__actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid #e5e7eb;
}
```

#### **📱 MOBILE-FIRST RESPONSIVE STRATEGY:**

```css
/* ✅ Mobile-first with progressive enhancement */

/* Mobile: Simple flexbox stack */
.responsive-component {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

/* Tablet: Introduce grid for more complex layout */
@media (min-width: 768px) {
  .responsive-component {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }
}

/* Desktop: More sophisticated grid */
@media (min-width: 1024px) {
  .responsive-component {
    grid-template-columns: 300px 1fr 200px;
    gap: 3rem;
  }
}

/* ✅ Container queries for true component responsiveness */
.container-responsive {
  container-type: inline-size;
}

@container (min-width: 400px) {
  .flexible-card {
    display: grid;
    grid-template-columns: auto 1fr;
    gap: 1rem;
  }
}

@container (min-width: 600px) {
  .flexible-card {
    grid-template-columns: auto 1fr auto;
  }
}
```

**💡 GHI NHỚ:**
- **Flexbox** = **1D**, **content-driven**, **perfect for components** 📏
- **Grid** = **2D**, **container-driven**, **perfect for layouts** 🏗️
- **Combine both** = Grid for structure, Flexbox for components 🔗
- **Modern approach** = Container queries + Intrinsic sizing 🚀

**Layout Strategy: Grid for structure → Flexbox for components → Container queries for true responsiveness!** 🎯

---

### CSS13: CSS Frameworks - Tailwind vs MUI vs Ant Design?

**Trả lời:**

**CSS Frameworks** solve different problems: **Utility-first** (Tailwind), **Component-based** (MUI), và **Enterprise-ready** (Ant Design). Chọn đúng framework là **CRITICAL** cho project success và developer productivity.

#### **🔥 FRAMEWORK COMPARISON OVERVIEW:**

| Aspect | **Tailwind CSS** | **Material-UI (MUI)** | **Ant Design** |
|--------|------------------|----------------------|----------------|
| **Philosophy** | **Utility-first** | **Design system** | **Enterprise components** |
| **Approach** | **Low-level utilities** | **Pre-built components** | **Complete UI library** |
| **Bundle Size** | **Small (purged)** | **Large (~300KB)** | **Very large (~500KB)** |
| **Customization** | **Highly flexible** | **Theme-based** | **Less flexible** |
| **Learning Curve** | **Steep initially** | **Medium** | **Easy** |
| **Design Opinion** | **No opinion** | **Material Design** | **Ant Design Language** |

#### **🎨 TAILWIND CSS - Utility-First Approach:**

```typescript
// ✅ TAILWIND FUNDAMENTALS
interface TailwindProps {
  className?: string;
}

// Basic utility classes
const TailwindCard: React.FC<TailwindProps> = ({ className }) => {
  return (
    <div className={`
      bg-white          /* Background color */
      rounded-lg        /* Border radius */
      shadow-md         /* Box shadow */
      p-6              /* Padding */
      border           /* Border */
      border-gray-200  /* Border color */
      hover:shadow-lg  /* Hover state */
      transition-shadow /* Smooth transition */
      duration-200     /* Animation duration */
      ${className}     /* Additional classes */
    `}>
      <h3 className="text-xl font-semibold text-gray-900 mb-2">
        Card Title
      </h3>
      <p className="text-gray-600 leading-relaxed">
        Card content with proper spacing and typography.
      </p>
      <button className="
        mt-4 px-4 py-2
        bg-blue-500 hover:bg-blue-600
        text-white font-medium
        rounded transition-colors
        focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2
      ">
        Action Button
      </button>
    </div>
  );
};

// ✅ RESPONSIVE DESIGN WITH TAILWIND
const ResponsiveTailwind: React.FC = () => {
  return (
    <div className="
      grid gap-6
      grid-cols-1          /* Mobile: 1 column */
      md:grid-cols-2       /* Tablet: 2 columns */
      lg:grid-cols-3       /* Desktop: 3 columns */
      xl:grid-cols-4       /* Large: 4 columns */
      p-4 md:p-6 lg:p-8   /* Responsive padding */
    ">
      {[1, 2, 3, 4].map((item) => (
        <TailwindCard key={item} />
      ))}
    </div>
  );
};

// ✅ CUSTOM COMPONENT WITH VARIANTS
interface ButtonProps {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
  onClick?: () => void;
}

const TailwindButton: React.FC<ButtonProps> = ({
  variant = 'primary',
  size = 'md',
  children,
  ...props
}) => {
  const baseClasses = "font-medium rounded transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2";

  const variantClasses = {
    primary: "bg-blue-500 hover:bg-blue-600 text-white focus:ring-blue-500",
    secondary: "bg-gray-200 hover:bg-gray-300 text-gray-900 focus:ring-gray-500",
    danger: "bg-red-500 hover:bg-red-600 text-white focus:ring-red-500"
  };

  const sizeClasses = {
    sm: "px-3 py-1.5 text-sm",
    md: "px-4 py-2 text-base",
    lg: "px-6 py-3 text-lg"
  };

  return (
    <button
      className={`${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]}`}
      {...props}
    >
      {children}
    </button>
  );
};

// ✅ TAILWIND CONFIG CUSTOMIZATION
// tailwind.config.js
export const tailwindConfig = {
  content: ['./src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#eff6ff',
          500: '#3b82f6',
          900: '#1e3a8a',
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      }
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
};
```

#### **🎭 MATERIAL-UI (MUI) - Component System:**

```typescript
import {
  ThemeProvider,
  createTheme,
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  Grid,
  styled
} from '@mui/material';

// ✅ MUI THEME CUSTOMIZATION
const muiTheme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
      light: '#42a5f5',
      dark: '#1565c0',
    },
    secondary: {
      main: '#dc004e',
    },
    background: {
      default: '#f5f5f5',
    },
  },
  typography: {
    h4: {
      fontWeight: 600,
    },
    body1: {
      fontSize: '1rem',
      lineHeight: 1.6,
    },
  },
  components: {
    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: '0 4px 6px rgba(0, 0, 0, 0.1)',
        },
      },
    },
    MuiButton: {
      styleOverrides: {
        root: {
          textTransform: 'none',
          borderRadius: 8,
        },
      },
    },
  },
});

// ✅ MUI COMPONENT USAGE
const MUICard: React.FC = () => {
  return (
    <Card elevation={2}>
      <CardContent>
        <Typography variant="h5" component="h2" gutterBottom>
          Material-UI Card
        </Typography>
        <Typography variant="body2" color="text.secondary" paragraph>
          This card uses Material Design principles with consistent spacing,
          typography, and elevation.
        </Typography>
        <Box sx={{ mt: 2, display: 'flex', gap: 1 }}>
          <Button variant="contained" color="primary">
            Primary Action
          </Button>
          <Button variant="outlined" color="secondary">
            Secondary
          </Button>
        </Box>
      </CardContent>
    </Card>
  );
};

// ✅ STYLED COMPONENTS WITH MUI
const StyledCard = styled(Card)(({ theme }) => ({
  borderRadius: theme.spacing(2),
  padding: theme.spacing(3),
  background: `linear-gradient(45deg, ${theme.palette.primary.main} 30%, ${theme.palette.primary.light} 90%)`,
  color: theme.palette.primary.contrastText,
  '&:hover': {
    transform: 'translateY(-4px)',
    transition: 'transform 0.2s ease-in-out',
  },
}));

// ✅ RESPONSIVE GRID WITH MUI
const MUIResponsiveGrid: React.FC = () => {
  return (
    <ThemeProvider theme={muiTheme}>
      <Box sx={{ flexGrow: 1, p: 3 }}>
        <Grid container spacing={3}>
          {[1, 2, 3, 4, 5, 6].map((item) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={item}>
              <MUICard />
            </Grid>
          ))}
        </Grid>
      </Box>
    </ThemeProvider>
  );
};

// ✅ CUSTOM MUI COMPONENT
interface CustomButtonProps {
  variant?: 'gradient' | 'glassmorphism';
  children: React.ReactNode;
}

const CustomMUIButton = styled(Button)<CustomButtonProps>(({ theme, variant }) => ({
  ...(variant === 'gradient' && {
    background: `linear-gradient(45deg, ${theme.palette.primary.main} 30%, ${theme.palette.secondary.main} 90%)`,
    color: 'white',
    '&:hover': {
      background: `linear-gradient(45deg, ${theme.palette.primary.dark} 30%, ${theme.palette.secondary.dark} 90%)`,
    },
  }),
  ...(variant === 'glassmorphism' && {
    background: 'rgba(255, 255, 255, 0.1)',
    backdropFilter: 'blur(10px)',
    border: '1px solid rgba(255, 255, 255, 0.2)',
    color: theme.palette.text.primary,
  }),
}));
```

#### **🏢 ANT DESIGN - Enterprise UI Library:**

```typescript
import {
  Card,
  Button,
  Row,
  Col,
  Typography,
  Space,
  ConfigProvider,
  theme as antTheme,
  Table,
  Form,
  Input,
  DatePicker,
  Select,
} from 'antd';
import type { ColumnsType } from 'antd/es/table';

const { Title, Paragraph } = Typography;

// ✅ ANT DESIGN THEME CUSTOMIZATION
const antDesignTheme = {
  algorithm: antTheme.darkAlgorithm, // or antTheme.defaultAlgorithm
  token: {
    colorPrimary: '#1677ff',
    colorInfo: '#1677ff',
    colorSuccess: '#52c41a',
    colorWarning: '#faad14',
    colorError: '#ff4d4f',
    fontSize: 14,
    borderRadius: 8,
  },
  components: {
    Card: {
      borderRadius: 12,
      headerBg: '#fafafa',
    },
    Button: {
      borderRadius: 8,
    },
  },
};

// ✅ ANT DESIGN COMPONENT USAGE
const AntCard: React.FC = () => {
  return (
    <Card
      title="Ant Design Card"
      extra={<Button type="link">More</Button>}
      actions={[
        <Button key="action1" type="primary">
          Primary
        </Button>,
        <Button key="action2">Secondary</Button>,
      ]}
    >
      <Paragraph>
        Ant Design provides enterprise-ready components with consistent
        design language and comprehensive functionality.
      </Paragraph>
      <Space>
        <Button type="primary" size="large">
          Large Primary
        </Button>
        <Button type="dashed" size="middle">
          Middle Dashed
        </Button>
        <Button type="text" size="small">
          Small Text
        </Button>
      </Space>
    </Card>
  );
};

// ✅ COMPLEX ANT DESIGN TABLE
interface DataType {
  key: string;
  name: string;
  age: number;
  address: string;
  status: 'active' | 'inactive';
}

const AntTable: React.FC = () => {
  const columns: ColumnsType<DataType> = [
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
      filterDropdown: ({ setSelectedKeys, selectedKeys, confirm, clearFilters }) => (
        <div style={{ padding: 8 }}>
          <Input
            placeholder="Search name"
            value={selectedKeys[0]}
            onChange={e => setSelectedKeys(e.target.value ? [e.target.value] : [])}
            onPressEnter={() => confirm()}
            style={{ width: 188, marginBottom: 8, display: 'block' }}
          />
        </div>
      ),
    },
    {
      title: 'Age',
      dataIndex: 'age',
      key: 'age',
      sorter: (a, b) => a.age - b.age,
    },
    {
      title: 'Address',
      dataIndex: 'address',
      key: 'address',
    },
    {
      title: 'Status',
      dataIndex: 'status',
      key: 'status',
      render: (status: string) => (
        <Button
          type={status === 'active' ? 'primary' : 'default'}
          size="small"
        >
          {status}
        </Button>
      ),
    },
  ];

  const data: DataType[] = [
    {
      key: '1',
      name: 'John Brown',
      age: 32,
      address: 'New York No. 1 Lake Park',
      status: 'active',
    },
    // ... more data
  ];

  return (
    <Table
      columns={columns}
      dataSource={data}
      pagination={{
        pageSize: 10,
        showSizeChanger: true,
        showQuickJumper: true,
      }}
      scroll={{ x: 800 }}
    />
  );
};

// ✅ ANT DESIGN FORM
const AntForm: React.FC = () => {
  const [form] = Form.useForm();

  const onFinish = (values: any) => {
    console.log('Form values:', values);
  };

  return (
    <ConfigProvider theme={antDesignTheme}>
      <Card title="Enterprise Form">
        <Form
          form={form}
          layout="vertical"
          onFinish={onFinish}
          autoComplete="off"
        >
          <Row gutter={16}>
            <Col span={12}>
              <Form.Item
                label="Full Name"
                name="fullName"
                rules={[{ required: true, message: 'Please input your name!' }]}
              >
                <Input placeholder="Enter your full name" />
              </Form.Item>
            </Col>
            <Col span={12}>
              <Form.Item
                label="Email"
                name="email"
                rules={[
                  { required: true, message: 'Please input your email!' },
                  { type: 'email', message: 'Please enter a valid email!' }
                ]}
              >
                <Input placeholder="Enter your email" />
              </Form.Item>
            </Col>
          </Row>

          <Row gutter={16}>
            <Col span={8}>
              <Form.Item
                label="Department"
                name="department"
                rules={[{ required: true, message: 'Please select department!' }]}
              >
                <Select placeholder="Select department">
                  <Select.Option value="engineering">Engineering</Select.Option>
                  <Select.Option value="marketing">Marketing</Select.Option>
                  <Select.Option value="sales">Sales</Select.Option>
                </Select>
              </Form.Item>
            </Col>
            <Col span={8}>
              <Form.Item
                label="Start Date"
                name="startDate"
                rules={[{ required: true, message: 'Please select start date!' }]}
              >
                <DatePicker style={{ width: '100%' }} />
              </Form.Item>
            </Col>
            <Col span={8}>
              <Form.Item label=" ">
                <Button type="primary" htmlType="submit" block>
                  Submit Form
                </Button>
              </Form.Item>
            </Col>
          </Row>
        </Form>
      </Card>
    </ConfigProvider>
  );
};
```

#### **⚖️ DECISION FRAMEWORK:**

**✅ Choose Tailwind CSS when:**
```typescript
// 1. Custom design system
interface CustomDesignProps {
  /* ✅ Unique brand identity needed */
  /* ✅ Full design control required */
  /* ✅ Small bundle size critical */
  /* ✅ Team comfortable with utility classes */
  /* ✅ Long-term maintainability important */
}

// 2. Performance-critical applications
const PerformanceCriticalApp: React.FC = () => {
  return (
    <div className="min-h-screen bg-gray-50">
      {/* Optimized bundle size with tree shaking */}
      <header className="bg-white shadow-sm border-b border-gray-200">
        <nav className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          {/* Custom components with utilities */}
        </nav>
      </header>
    </div>
  );
};
```

**✅ Choose Material-UI when:**
```typescript
// 1. Material Design adoption
interface MaterialAppProps {
  /* ✅ Google's design system fits brand */
  /* ✅ Rich component ecosystem needed */
  /* ✅ Accessibility out-of-the-box */
  /* ✅ Strong TypeScript support required */
  /* ✅ Theming flexibility important */
}

// 2. React-focused applications
const MaterialApp: React.FC = () => {
  return (
    <ThemeProvider theme={muiTheme}>
      <CssBaseline />
      <Container>
        {/* Rich component ecosystem */}
        <AppBar position="static">
          <Toolbar>
            <Typography variant="h6">Material App</Typography>
          </Toolbar>
        </AppBar>
      </Container>
    </ThemeProvider>
  );
};
```

**✅ Choose Ant Design when:**
```typescript
// 1. Enterprise applications
interface EnterpriseAppProps {
  /* ✅ Admin dashboards and tools */
  /* ✅ Data-heavy applications */
  /* ✅ Complex forms and tables */
  /* ✅ Fast development timeline */
  /* ✅ Consistent enterprise UX */
}

// 2. B2B applications
const EnterpriseApp: React.FC = () => {
  return (
    <ConfigProvider theme={antDesignTheme}>
      <Layout>
        <Layout.Sider>
          {/* Rich navigation components */}
        </Layout.Sider>
        <Layout.Content>
          {/* Complex data components */}
          <Table dataSource={data} columns={columns} />
        </Layout.Content>
      </Layout>
    </ConfigProvider>
  );
};
```

#### **🚀 MODERN HYBRID APPROACHES:**

**1. Tailwind + Headless UI:**
```typescript
import { Dialog, Transition } from '@headlessui/react';

const ModernModal: React.FC<{ isOpen: boolean; onClose: () => void }> = ({
  isOpen,
  onClose
}) => {
  return (
    <Transition appear show={isOpen} as={React.Fragment}>
      <Dialog as="div" className="relative z-10" onClose={onClose}>
        <Transition.Child
          as={React.Fragment}
          enter="ease-out duration-300"
          enterFrom="opacity-0"
          enterTo="opacity-100"
          leave="ease-in duration-200"
          leaveFrom="opacity-100"
          leaveTo="opacity-0"
        >
          <div className="fixed inset-0 bg-black bg-opacity-25" />
        </Transition.Child>

        <div className="fixed inset-0 overflow-y-auto">
          <div className="flex min-h-full items-center justify-center p-4">
            <Transition.Child
              as={React.Fragment}
              enter="ease-out duration-300"
              enterFrom="opacity-0 scale-95"
              enterTo="opacity-100 scale-100"
              leave="ease-in duration-200"
              leaveFrom="opacity-100 scale-100"
              leaveTo="opacity-0 scale-95"
            >
              <Dialog.Panel className="w-full max-w-md transform overflow-hidden rounded-2xl bg-white p-6 text-left align-middle shadow-xl transition-all">
                <Dialog.Title className="text-lg font-medium leading-6 text-gray-900">
                  Modern Modal
                </Dialog.Title>
                <div className="mt-2">
                  <p className="text-sm text-gray-500">
                    Combining Tailwind utilities with Headless UI logic.
                  </p>
                </div>
              </Dialog.Panel>
            </Transition.Child>
          </div>
        </div>
      </Dialog>
    </Transition>
  );
};
```

**2. CSS-in-JS + Design Tokens:**
```typescript
import styled from 'styled-components';

// Design tokens approach
const tokens = {
  colors: {
    primary: '#3b82f6',
    secondary: '#64748b',
    success: '#10b981',
    error: '#ef4444',
  },
  spacing: {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '1.5rem',
    xl: '3rem',
  },
  breakpoints: {
    sm: '640px',
    md: '768px',
    lg: '1024px',
    xl: '1280px',
  },
};

const ModernCard = styled.div`
  background: white;
  border-radius: 0.75rem;
  padding: ${tokens.spacing.lg};
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  border: 1px solid #e5e7eb;

  transition: all 0.2s ease;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
  }

  @media (min-width: ${tokens.breakpoints.md}) {
    padding: ${tokens.spacing.xl};
  }
`;
```

#### **📊 PERFORMANCE & BUNDLE SIZE:**

```typescript
// ✅ Bundle size optimization strategies

// 1. Tailwind CSS with PurgeCSS
const tailwindBundleSize = {
  development: '3.2MB', // Full utility set
  production: '8-50KB', // Only used utilities
  treeshaking: 'Excellent',
  customization: 'Unlimited',
};

// 2. Material-UI with tree shaking
import { Button } from '@mui/material/Button'; // ❌ Imports entire module
import Button from '@mui/material/Button';     // ✅ Tree-shakeable import

const muiBundleSize = {
  minimal: '80KB', // Button only
  typical: '300KB', // Common components
  full: '1MB+', // All components
  treeshaking: 'Good with proper imports',
  customization: 'Theme-based',
};

// 3. Ant Design with babel plugin
const antBundleSize = {
  minimal: '150KB', // Button only
  typical: '500KB', // Common components
  full: '2MB+', // All components
  treeshaking: 'Requires babel plugin',
  customization: 'Limited theme options',
};
```

**💡 GHI NHỚ:**
- **Tailwind** = **Utility-first**, **small bundles**, **full control** 🎨
- **MUI** = **Component-rich**, **Material Design**, **React-focused** 🎭
- **Ant Design** = **Enterprise-ready**, **complete toolkit**, **fast development** 🏢
- **Choose based on** = Project type, team skills, design requirements 🎯

**Framework Strategy: Start with requirements → Consider team expertise → Evaluate long-term maintenance → Choose accordingly!** 🚀

---

### CSS14: HTML5 Semantic Elements - Modern Web Standards?

**Trả lời:**

**HTML5 Semantic Elements** provide **MEANINGFUL STRUCTURE** và **ACCESSIBILITY** cho modern web applications. Using semantic HTML là **FOUNDATION** cho SEO, accessibility, và maintainable code.

#### **🔥 SEMANTIC ELEMENTS OVERVIEW:**

| Element | **Purpose** | **When to Use** | **SEO Impact** |
|---------|-------------|-----------------|----------------|
| **`<header>`** | **Page/section header** | **Top of page/section** | **High** - Contains main headings |
| **`<nav>`** | **Navigation links** | **Main/secondary navigation** | **High** - Defines site structure |
| **`<main>`** | **Primary content** | **Once per page** | **Critical** - Main content identifier |
| **`<article>`** | **Independent content** | **Blog posts, news articles** | **High** - Standalone content |
| **`<section>`** | **Content sections** | **Thematic grouping** | **Medium** - Content organization |
| **`<aside>`** | **Supplementary content** | **Sidebars, related content** | **Low** - Supporting information |
| **`<footer>`** | **Page/section footer** | **Bottom of page/section** | **Medium** - Contact/copyright info |

#### **🏗️ SEMANTIC HTML STRUCTURE:**

```html
<!-- ✅ PROPER SEMANTIC STRUCTURE -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Modern Semantic Website</title>

  <!-- SEO and Social Meta -->
  <meta name="description" content="Learn about HTML5 semantic elements for better accessibility and SEO">
  <meta property="og:title" content="HTML5 Semantic Elements Guide">
  <meta property="og:description" content="Comprehensive guide to modern HTML5 semantic elements">
  <meta property="og:type" content="article">
  <meta name="twitter:card" content="summary">

  <!-- Structured Data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "HTML5 Semantic Elements Guide",
    "author": {
      "@type": "Person",
      "name": "Frontend Developer"
    },
    "datePublished": "2024-01-15"
  }
  </script>
</head>
<body>
  <!-- ✅ PAGE HEADER -->
  <header role="banner" class="site-header">
    <div class="container">
      <!-- Logo/Brand -->
      <div class="brand">
        <a href="/" aria-label="Home">
          <img src="/logo.svg" alt="Company Logo" width="120" height="40">
        </a>
      </div>

      <!-- Primary Navigation -->
      <nav role="navigation" aria-label="Main navigation">
        <ul class="nav-menu">
          <li><a href="/" aria-current="page">Home</a></li>
          <li><a href="/about">About</a></li>
          <li><a href="/services">Services</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>

      <!-- Mobile Menu Toggle -->
      <button
        class="mobile-menu-toggle"
        aria-expanded="false"
        aria-controls="mobile-menu"
        aria-label="Toggle mobile menu"
      >
        <span class="hamburger"></span>
      </button>
    </div>
  </header>

  <!-- ✅ MAIN CONTENT AREA -->
  <main role="main" class="main-content">
    <!-- Hero Section -->
    <section class="hero" aria-labelledby="hero-title">
      <div class="container">
        <h1 id="hero-title">HTML5 Semantic Elements</h1>
        <p class="hero-subtitle">
          Building accessible and SEO-friendly web applications
        </p>
        <a href="#content" class="cta-button">
          Learn More
          <span class="sr-only">(about HTML5 semantic elements)</span>
        </a>
      </div>
    </section>

    <!-- Article Content -->
    <article id="content" class="article" role="article">
      <header class="article-header">
        <h1>Understanding HTML5 Semantic Elements</h1>
        <div class="article-meta">
          <time datetime="2024-01-15T10:00:00Z" pubdate>
            January 15, 2024
          </time>
          <address class="author">
            By <a rel="author" href="/author/john-doe">John Doe</a>
          </address>
          <span class="reading-time">5 min read</span>
        </div>
      </header>

      <!-- Article Sections -->
      <section aria-labelledby="intro-heading">
        <h2 id="intro-heading">Introduction</h2>
        <p>
          HTML5 introduced semantic elements that provide meaning
          to the structure of web content...
        </p>
      </section>

      <section aria-labelledby="benefits-heading">
        <h2 id="benefits-heading">Benefits of Semantic HTML</h2>
        <ul>
          <li><strong>Accessibility:</strong> Screen readers understand content structure</li>
          <li><strong>SEO:</strong> Search engines better understand content hierarchy</li>
          <li><strong>Maintainability:</strong> Code is self-documenting</li>
        </ul>
      </section>

      <!-- Code Example Section -->
      <section aria-labelledby="examples-heading">
        <h2 id="examples-heading">Practical Examples</h2>
        <pre><code>
&lt;article&gt;
  &lt;header&gt;
    &lt;h1&gt;Article Title&lt;/h1&gt;
  &lt;/header&gt;
  &lt;p&gt;Article content...&lt;/p&gt;
&lt;/article&gt;
        </code></pre>
      </section>
    </article>

    <!-- Related Content -->
    <aside class="sidebar" role="complementary" aria-labelledby="sidebar-title">
      <h2 id="sidebar-title">Related Topics</h2>

      <!-- Related Articles -->
      <section aria-labelledby="related-heading">
        <h3 id="related-heading">You Might Also Like</h3>
        <nav aria-label="Related articles">
          <ul>
            <li>
              <article class="related-article">
                <h4>
                  <a href="/css-accessibility">CSS for Accessibility</a>
                </h4>
                <p>Learn how to write accessible CSS...</p>
              </article>
            </li>
            <li>
              <article class="related-article">
                <h4>
                  <a href="/aria-attributes">ARIA Attributes Guide</a>
                </h4>
                <p>Understanding ARIA for better accessibility...</p>
              </article>
            </li>
          </ul>
        </nav>
      </section>

      <!-- Newsletter Signup -->
      <section aria-labelledby="newsletter-heading">
        <h3 id="newsletter-heading">Stay Updated</h3>
        <form class="newsletter-form" novalidate>
          <label for="email-input">Email Address</label>
          <input
            type="email"
            id="email-input"
            name="email"
            required
            aria-describedby="email-error"
            placeholder="Enter your email"
          >
          <div id="email-error" class="error-message" aria-live="polite"></div>
          <button type="submit">Subscribe</button>
        </form>
      </section>
    </aside>
  </main>

  <!-- ✅ SITE FOOTER -->
  <footer role="contentinfo" class="site-footer">
    <div class="container">
      <!-- Footer Navigation -->
      <nav aria-label="Footer navigation">
        <div class="footer-section">
          <h3>Company</h3>
          <ul>
            <li><a href="/about">About Us</a></li>
            <li><a href="/careers">Careers</a></li>
            <li><a href="/press">Press</a></li>
          </ul>
        </div>

        <div class="footer-section">
          <h3>Support</h3>
          <ul>
            <li><a href="/help">Help Center</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/privacy">Privacy Policy</a></li>
          </ul>
        </div>
      </nav>

      <!-- Contact Information -->
      <address class="contact-info">
        <h3>Contact Information</h3>
        <p>
          <strong>Email:</strong>
          <a href="mailto:info@example.com">info@example.com</a>
        </p>
        <p>
          <strong>Phone:</strong>
          <a href="tel:+1234567890">+1 (234) 567-890</a>
        </p>
      </address>

      <!-- Copyright -->
      <div class="copyright">
        <p>&copy; 2024 Company Name. All rights reserved.</p>
        <small>
          Built with HTML5 semantic elements for better accessibility.
        </small>
      </div>
    </div>
  </footer>
</body>
</html>
```

#### **🎯 SEMANTIC ELEMENT DETAILS:**

**1. `<header>` Element:**
```html
<!-- ✅ PAGE HEADER -->
<header class="site-header">
  <h1>Site Title</h1>
  <nav>...</nav>
</header>

<!-- ✅ ARTICLE HEADER -->
<article>
  <header class="article-header">
    <h1>Article Title</h1>
    <time datetime="2024-01-15">January 15, 2024</time>
    <address>By Author Name</address>
  </header>
  <p>Article content...</p>
</article>

<!-- ✅ SECTION HEADER -->
<section>
  <header>
    <h2>Section Title</h2>
    <p class="section-intro">Section introduction...</p>
  </header>
  <div class="section-content">...</div>
</section>
```

**2. `<nav>` Element:**
```html
<!-- ✅ PRIMARY NAVIGATION -->
<nav role="navigation" aria-label="Main navigation">
  <ul>
    <li><a href="/" aria-current="page">Home</a></li>
    <li><a href="/about">About</a></li>
    <li><a href="/services">Services</a></li>
  </ul>
</nav>

<!-- ✅ BREADCRUMB NAVIGATION -->
<nav aria-label="Breadcrumb">
  <ol class="breadcrumb">
    <li><a href="/">Home</a></li>
    <li><a href="/category">Category</a></li>
    <li aria-current="page">Current Page</li>
  </ol>
</nav>

<!-- ✅ PAGINATION NAVIGATION -->
<nav aria-label="Pagination">
  <ul class="pagination">
    <li>
      <a href="/page/1" rel="prev" aria-label="Previous page">
        ← Previous
      </a>
    </li>
    <li><a href="/page/2" aria-current="page">2</a></li>
    <li><a href="/page/3">3</a></li>
    <li>
      <a href="/page/3" rel="next" aria-label="Next page">
        Next →
      </a>
    </li>
  </ul>
</nav>

<!-- ✅ TABLE OF CONTENTS -->
<nav aria-labelledby="toc-heading">
  <h2 id="toc-heading">Table of Contents</h2>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#methodology">Methodology</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#conclusion">Conclusion</a></li>
  </ol>
</nav>
```

**3. `<main>` Element:**
```html
<!-- ✅ MAIN CONTENT WRAPPER -->
<main role="main" class="main-content">
  <!-- Skip link target -->
  <a id="main-content" tabindex="-1"></a>

  <!-- Primary content -->
  <h1>Page Title</h1>
  <p>Main page content...</p>

  <!-- Content sections -->
  <section>...</section>
  <article>...</article>
</main>

<!-- ❌ MULTIPLE MAIN ELEMENTS (Invalid) -->
<main>First main content</main>
<main>Second main content</main> <!-- Invalid! -->

<!-- ✅ CONDITIONAL MAIN WITH SPA -->
<div id="app">
  <header>...</header>
  <main v-if="currentRoute === 'home'">
    Home content
  </main>
  <main v-if="currentRoute === 'about'">
    About content
  </main>
  <footer>...</footer>
</div>
```

**4. `<article>` Element:**
```html
<!-- ✅ BLOG POST -->
<article class="blog-post" itemscope itemtype="https://schema.org/BlogPosting">
  <header>
    <h1 itemprop="headline">How to Write Semantic HTML</h1>
    <time itemprop="datePublished" datetime="2024-01-15">
      January 15, 2024
    </time>
    <address itemprop="author" itemscope itemtype="https://schema.org/Person">
      By <span itemprop="name">John Doe</span>
    </address>
  </header>

  <div itemprop="articleBody">
    <p>Article content goes here...</p>
  </div>

  <footer>
    <p>Tags: <a href="/tag/html">HTML</a>, <a href="/tag/accessibility">Accessibility</a></p>
  </footer>
</article>

<!-- ✅ NEWS ARTICLE -->
<article class="news-article" itemscope itemtype="https://schema.org/NewsArticle">
  <header>
    <h2 itemprop="headline">Breaking News Title</h2>
    <time itemprop="datePublished" datetime="2024-01-15T14:30:00Z">
      Today at 2:30 PM
    </time>
  </header>
  <p itemprop="articleBody">News content...</p>
</article>

<!-- ✅ PRODUCT REVIEW -->
<article class="product-review" itemscope itemtype="https://schema.org/Review">
  <header>
    <h3 itemprop="name">Great Product!</h3>
    <div itemprop="reviewRating" itemscope itemtype="https://schema.org/Rating">
      <span itemprop="ratingValue">5</span> out of
      <span itemprop="bestRating">5</span> stars
    </div>
  </header>
  <div itemprop="reviewBody">
    <p>This product exceeded my expectations...</p>
  </div>
  <footer>
    <address itemprop="author">By Reviewer Name</address>
  </footer>
</article>
```

**5. `<section>` Element:**
```html
<!-- ✅ THEMATIC CONTENT SECTIONS -->
<section aria-labelledby="features-heading">
  <h2 id="features-heading">Key Features</h2>
  <div class="features-grid">
    <div class="feature">
      <h3>Fast Performance</h3>
      <p>Optimized for speed...</p>
    </div>
    <div class="feature">
      <h3>Secure</h3>
      <p>Built with security in mind...</p>
    </div>
  </div>
</section>

<!-- ✅ CONTENT CHAPTERS -->
<section aria-labelledby="chapter1">
  <h2 id="chapter1">Chapter 1: Introduction</h2>
  <p>Chapter content...</p>
</section>

<section aria-labelledby="chapter2">
  <h2 id="chapter2">Chapter 2: Getting Started</h2>
  <p>Chapter content...</p>
</section>

<!-- ✅ FORM SECTIONS -->
<form>
  <section aria-labelledby="personal-info">
    <h2 id="personal-info">Personal Information</h2>
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
  </section>

  <section aria-labelledby="contact-info">
    <h2 id="contact-info">Contact Information</h2>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
  </section>
</form>
```

#### **🚀 MODERN SEMANTIC PATTERNS:**

**1. Component-Based Semantic Structure:**
```typescript
// ✅ React Semantic Components
interface SemanticCardProps {
  title: string;
  content: string;
  author?: string;
  publishDate?: string;
  isArticle?: boolean;
}

const SemanticCard: React.FC<SemanticCardProps> = ({
  title,
  content,
  author,
  publishDate,
  isArticle = false
}) => {
  const CardElement = isArticle ? 'article' : 'div';

  return (
    <CardElement
      className="semantic-card"
      {...(isArticle && {
        itemScope: true,
        itemType: 'https://schema.org/Article'
      })}
    >
      <header className="card-header">
        <h3 {...(isArticle && { itemProp: 'headline' })}>
          {title}
        </h3>
        {publishDate && (
          <time
            dateTime={publishDate}
            {...(isArticle && { itemProp: 'datePublished' })}
          >
            {new Date(publishDate).toLocaleDateString()}
          </time>
        )}
        {author && (
          <address {...(isArticle && { itemProp: 'author' })}>
            By {author}
          </address>
        )}
      </header>

      <div
        className="card-content"
        {...(isArticle && { itemProp: 'articleBody' })}
      >
        {content}
      </div>
    </CardElement>
  );
};

// ✅ Semantic Navigation Component
interface NavItem {
  label: string;
  href: string;
  isCurrent?: boolean;
}

const SemanticNav: React.FC<{
  items: NavItem[];
  ariaLabel: string;
}> = ({ items, ariaLabel }) => {
  return (
    <nav role="navigation" aria-label={ariaLabel}>
      <ul className="nav-list">
        {items.map((item, index) => (
          <li key={index}>
            <a
              href={item.href}
              {...(item.isCurrent && { 'aria-current': 'page' })}
              className={item.isCurrent ? 'current' : ''}
            >
              {item.label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  );
};
```

**2. SEO-Optimized Semantic Structure:**
```html
<!-- ✅ RICH SEMANTIC MARKUP -->
<article
  itemscope
  itemtype="https://schema.org/BlogPosting"
  class="blog-post"
>
  <header class="post-header">
    <h1 itemprop="headline">
      Complete Guide to HTML5 Semantic Elements
    </h1>

    <div class="post-meta">
      <time
        itemprop="datePublished"
        datetime="2024-01-15T10:00:00+00:00"
        class="published-date"
      >
        January 15, 2024
      </time>

      <time
        itemprop="dateModified"
        datetime="2024-01-16T14:30:00+00:00"
        class="modified-date"
      >
        Updated: January 16, 2024
      </time>

      <address
        itemprop="author"
        itemscope
        itemtype="https://schema.org/Person"
        class="author"
      >
        <span itemprop="name">John Doe</span>
        <meta itemprop="email" content="john@example.com">
        <meta itemprop="url" content="https://johndoe.com">
      </address>

      <div
        itemprop="publisher"
        itemscope
        itemtype="https://schema.org/Organization"
        style="display: none;"
      >
        <span itemprop="name">Tech Blog</span>
        <div itemprop="logo" itemscope itemtype="https://schema.org/ImageObject">
          <meta itemprop="url" content="https://example.com/logo.png">
        </div>
      </div>
    </div>
  </header>

  <div itemprop="articleBody" class="post-content">
    <section aria-labelledby="introduction">
      <h2 id="introduction">Introduction</h2>
      <p>Semantic HTML provides structure and meaning...</p>
    </section>

    <section aria-labelledby="benefits">
      <h2 id="benefits">Benefits</h2>
      <ul>
        <li>Improved accessibility</li>
        <li>Better SEO performance</li>
        <li>Enhanced code maintainability</li>
      </ul>
    </section>
  </div>

  <footer class="post-footer">
    <div itemprop="keywords" class="tags">
      <span class="tag">HTML5</span>
      <span class="tag">Semantic Elements</span>
      <span class="tag">Accessibility</span>
      <span class="tag">SEO</span>
    </div>

    <div class="sharing">
      <h3>Share this article</h3>
      <a href="#" aria-label="Share on Twitter">Twitter</a>
      <a href="#" aria-label="Share on Facebook">Facebook</a>
    </div>
  </footer>
</article>
```

**💡 GHI NHỚ:**
- **`<header>`** = **Page/section header** 📄
- **`<nav>`** = **Navigation links** 🧭
- **`<main>`** = **Primary content** (once per page) 🎯
- **`<article>`** = **Independent content** 📰
- **`<section>`** = **Thematic grouping** 📚
- **`<aside>`** = **Supplementary content** 📋
- **`<footer>`** = **Page/section footer** 📜

**Semantic Strategy: Meaningful structure → Better accessibility → Improved SEO → Maintainable code!** 🚀

---

### CSS15: Script `defer` vs `async` - Performance Optimization?

**Trả lời:**

`defer` và `async` attributes control **SCRIPT LOADING BEHAVIOR** và **EXECUTION TIMING**. Understanding these attributes là **CRITICAL** cho **page performance** và **proper script execution order**.

#### **🔥 SCRIPT LOADING BEHAVIOR:**

| Attribute | **Download** | **Execution** | **DOM Blocking** | **Order** |
|-----------|--------------|---------------|------------------|-----------|
| **None** | **Blocks parsing** | **Immediate** | ✅ **Blocks** | **Sequential** |
| **`async`** | **Parallel** | **When ready** | ❌ **Non-blocking** | **Random** |
| **`defer`** | **Parallel** | **After DOM** | ❌ **Non-blocking** | **Sequential** |

#### **📊 VISUAL EXECUTION TIMELINE:**

```
🔄 NORMAL SCRIPT (blocking):
HTML Parsing: ████████░░░░░░░░░░░░░░░░░░░░
Script Download:     ████░░░░░░░░░░░░░░░░░░░░
Script Execution:        ██░░░░░░░░░░░░░░░░░░
HTML Parsing:              ████████░░░░░░░░░░
                           ↑ Parsing resumes

⚡ ASYNC SCRIPT (non-blocking):
HTML Parsing: ████████████████████████████
Script Download:     ████░░░░░░░░░░░░░░░░░░░░
Script Execution:        ██░░░░░░░░░░░░░░░░░░
                           ↑ Executes when ready

⏳ DEFER SCRIPT (ordered):
HTML Parsing: ████████████████████████████
Script Download:     ████░░░░░░░░░░░░░░░░░░░░
Script Execution:                         ██
                                           ↑ After DOM ready
```

#### **🎯 PRACTICAL IMPLEMENTATIONS:**

**1. Normal Script Loading (Blocking):**
```html
<!-- ❌ BLOCKING: Stops HTML parsing -->
<html>
<head>
  <title>Page Title</title>
  <!-- This blocks HTML parsing until loaded and executed -->
  <script src="large-library.js"></script>
</head>
<body>
  <h1>Page Content</h1>
  <!-- Content appears after script execution -->
</body>
</html>
```

**2. Async Script Loading:**
```html
<!-- ⚡ ASYNC: Downloads in parallel, executes when ready -->
<html>
<head>
  <title>Page Title</title>
  <!-- ✅ Good for independent scripts -->
  <script async src="analytics.js"></script>
  <script async src="ad-tracker.js"></script>
  <script async src="social-widgets.js"></script>
</head>
<body>
  <h1>Page Content</h1>
  <!-- Content appears immediately, scripts execute when ready -->

  <!-- ⚠️ WARNING: Order not guaranteed -->
  <script async src="library.js"></script>
  <script async src="app.js"></script> <!-- May execute before library.js! -->
</body>
</html>
```

**3. Defer Script Loading:**
```html
<!-- ⏳ DEFER: Downloads in parallel, executes after DOM -->
<html>
<head>
  <title>Page Title</title>
  <!-- ✅ Good for DOM-dependent scripts -->
  <script defer src="library.js"></script>
  <script defer src="app.js"></script> <!-- Executes after library.js -->
  <script defer src="init.js"></script> <!-- Executes last -->
</head>
<body>
  <h1>Page Content</h1>
  <!-- Content appears immediately, scripts execute in order after DOM ready -->
</body>
</html>
```

#### **🚀 TYPESCRIPT EXAMPLES:**

**1. Performance-Optimized Loading:**
```typescript
// ✅ Script loading utility
class ScriptLoader {
  private static loadedScripts = new Set<string>();

  // Load script with async
  static async loadAsync(src: string): Promise<void> {
    if (this.loadedScripts.has(src)) {
      return Promise.resolve();
    }

    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.src = src;
      script.async = true;

      script.onload = () => {
        this.loadedScripts.add(src);
        resolve();
      };

      script.onerror = () => {
        reject(new Error(`Failed to load script: ${src}`));
      };

      document.head.appendChild(script);
    });
  }

  // Load script with defer-like behavior
  static async loadDeferred(src: string): Promise<void> {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      await new Promise(resolve => {
        document.addEventListener('DOMContentLoaded', resolve, { once: true });
      });
    }

    return this.loadAsync(src);
  }

  // Load multiple scripts in order
  static async loadSequential(scripts: string[]): Promise<void> {
    for (const script of scripts) {
      await this.loadAsync(script);
    }
  }

  // Load multiple scripts in parallel
  static async loadParallel(scripts: string[]): Promise<void[]> {
    return Promise.all(scripts.map(script => this.loadAsync(script)));
  }
}

// ✅ Usage examples
const setupApplication = async () => {
  try {
    // Load critical dependencies first
    await ScriptLoader.loadSequential([
      '/js/polyfills.js',
      '/js/core-library.js',
      '/js/app-init.js'
    ]);

    // Load non-critical scripts in parallel
    await ScriptLoader.loadParallel([
      '/js/analytics.js',
      '/js/social-widgets.js',
      '/js/ads.js'
    ]);

    console.log('All scripts loaded successfully');
  } catch (error) {
    console.error('Script loading failed:', error);
  }
};

// Wait for DOM then load application
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', setupApplication);
} else {
  setupApplication();
}
```

**2. Modern Module Loading:**
```html
<!-- ✅ MODERN ES MODULES -->
<script type="module">
  // Modern browsers: ES modules with automatic defer behavior
  import { initApp } from './js/app.js';
  import { analytics } from './js/analytics.js';

  // Modules are automatically deferred
  document.addEventListener('DOMContentLoaded', () => {
    initApp();
    analytics.track('page_view');
  });
</script>

<!-- ✅ FALLBACK FOR OLDER BROWSERS -->
<script nomodule defer src="/js/app-legacy.js"></script>

<!-- ✅ DYNAMIC IMPORTS FOR CODE SPLITTING -->
<script type="module">
  // Load components on demand
  const loadComponent = async (componentName) => {
    const { default: Component } = await import(`./components/${componentName}.js`);
    return Component;
  };

  // Load when needed
  document.querySelector('#load-chart').addEventListener('click', async () => {
    const ChartComponent = await loadComponent('chart');
    const chart = new ChartComponent('#chart-container');
    chart.render();
  });
</script>
```

#### **⚖️ USE CASE RECOMMENDATIONS:**

**✅ Use `async` for:**
```html
<!-- 1. Analytics and tracking -->
<script async src="https://www.google-analytics.com/analytics.js"></script>
<script async src="https://connect.facebook.net/en_US/fbevents.js"></script>

<!-- 2. Advertisement scripts -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>

<!-- 3. Social media widgets -->
<script async src="https://platform.twitter.com/widgets.js"></script>
<script async src="https://apis.google.com/js/platform.js"></script>

<!-- 4. Independent utilities (order doesn't matter) -->
<script async src="/js/error-reporter.js"></script>
<script async src="/js/performance-monitor.js"></script>

<!-- 5. Third-party embeds -->
<script async src="https://embeds.example.com/widget.js"></script>
```

**✅ Use `defer` for:**
```html
<!-- 1. Application dependencies (order matters) -->
<script defer src="/js/polyfills.js"></script>
<script defer src="/js/vendor.js"></script>
<script defer src="/js/app.js"></script>

<!-- 2. DOM-dependent scripts -->
<script defer src="/js/form-handlers.js"></script>
<script defer src="/js/interactive-elements.js"></script>

<!-- 3. Application initialization -->
<script defer src="/js/app-init.js"></script>
<script defer src="/js/page-specific.js"></script>

<!-- 4. UI component libraries -->
<script defer src="/js/ui-components.js"></script>
<script defer src="/js/component-init.js"></script>
```

**✅ Use normal loading for:**
```html
<!-- 1. Critical polyfills needed immediately -->
<script src="/js/critical-polyfills.js"></script>

<!-- 2. Document.write dependencies (legacy) -->
<script src="/js/legacy-document-write.js"></script>

<!-- 3. Inline configuration needed by other scripts -->
<script>
  window.CONFIG = {
    apiUrl: 'https://api.example.com',
    version: '1.2.3'
  };
</script>
<script defer src="/js/app.js"></script>
```

#### **🧪 PERFORMANCE TESTING:**

```typescript
// ✅ Performance measurement utility
class ScriptPerformanceMonitor {
  private static measurements = new Map<string, PerformanceMeasure>();

  // Measure script loading performance
  static measureScriptLoad(scriptSrc: string): void {
    const startMark = `script-start-${scriptSrc}`;
    const endMark = `script-end-${scriptSrc}`;
    const measureName = `script-load-${scriptSrc}`;

    performance.mark(startMark);

    const script = document.createElement('script');
    script.src = scriptSrc;

    script.onload = () => {
      performance.mark(endMark);
      const measure = performance.measure(measureName, startMark, endMark);
      this.measurements.set(scriptSrc, measure);

      console.log(`Script ${scriptSrc} loaded in ${measure.duration.toFixed(2)}ms`);
    };

    document.head.appendChild(script);
  }

  // Compare async vs defer performance
  static async compareLoadingStrategies(): Promise<void> {
    const testScripts = [
      '/js/test-1.js',
      '/js/test-2.js',
      '/js/test-3.js'
    ];

    // Test async loading
    const asyncStart = performance.now();
    await Promise.all(testScripts.map(src => this.loadAsync(src)));
    const asyncTime = performance.now() - asyncStart;

    // Test defer-like loading (sequential)
    const deferStart = performance.now();
    for (const script of testScripts) {
      await this.loadAsync(script);
    }
    const deferTime = performance.now() - deferStart;

    console.log('Loading Strategy Comparison:');
    console.log(`Async (parallel): ${asyncTime.toFixed(2)}ms`);
    console.log(`Defer (sequential): ${deferTime.toFixed(2)}ms`);
  }

  private static loadAsync(src: string): Promise<void> {
    return new Promise((resolve) => {
      const script = document.createElement('script');
      script.src = src;
      script.async = true;
      script.onload = () => resolve();
      document.head.appendChild(script);
    });
  }

  // Monitor Core Web Vitals impact
  static monitorWebVitals(): void {
    // First Contentful Paint
    new PerformanceObserver((list) => {
      const entries = list.getEntries();
      entries.forEach((entry) => {
        if (entry.name === 'first-contentful-paint') {
          console.log(`FCP: ${entry.startTime.toFixed(2)}ms`);
        }
      });
    }).observe({ entryTypes: ['paint'] });

    // Largest Contentful Paint
    new PerformanceObserver((list) => {
      const entries = list.getEntries();
      const lastEntry = entries[entries.length - 1];
      console.log(`LCP: ${lastEntry.startTime.toFixed(2)}ms`);
    }).observe({ entryTypes: ['largest-contentful-paint'] });

    // Cumulative Layout Shift
    let clsValue = 0;
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
          clsValue += entry.value;
        }
      }
      console.log(`CLS: ${clsValue.toFixed(4)}`);
    }).observe({ entryTypes: ['layout-shift'] });
  }
}

// Usage
ScriptPerformanceMonitor.monitorWebVitals();
ScriptPerformanceMonitor.compareLoadingStrategies();
```

#### **📱 MOBILE OPTIMIZATION:**

```html
<!-- ✅ MOBILE-OPTIMIZED SCRIPT LOADING -->
<html>
<head>
  <!-- Critical inline styles -->
  <style>
    /* Critical CSS inlined for fast rendering */
    .hero { background: #007bff; color: white; padding: 2rem; }
    .content { max-width: 800px; margin: 0 auto; }
  </style>

  <!-- Preload critical resources -->
  <link rel="preload" href="/js/critical.js" as="script">
  <link rel="preload" href="/fonts/main.woff2" as="font" type="font/woff2" crossorigin>

  <!-- DNS prefetch for external resources -->
  <link rel="dns-prefetch" href="//www.google-analytics.com">
  <link rel="dns-prefetch" href="//fonts.googleapis.com">

  <!-- Critical scripts (minimal) -->
  <script>
    // Inline critical JavaScript
    window.performance && performance.mark('script-start');
  </script>
</head>
<body>
  <!-- Page content -->
  <header class="hero">
    <h1>Fast Loading Page</h1>
  </header>

  <main class="content">
    <p>Content loads immediately while scripts load in background.</p>
  </main>

  <!-- Non-critical scripts -->
  <script defer src="/js/app.js"></script>
  <script defer src="/js/components.js"></script>

  <!-- Third-party scripts -->
  <script async src="https://www.google-analytics.com/analytics.js"></script>

  <!-- Load additional resources after initial paint -->
  <script>
    // Load non-critical CSS
    const loadCSS = (href) => {
      const link = document.createElement('link');
      link.rel = 'stylesheet';
      link.href = href;
      document.head.appendChild(link);
    };

    // Load after FCP
    addEventListener('load', () => {
      loadCSS('/css/non-critical.css');

      // Load additional scripts on interaction
      let loaded = false;
      const loadInteractiveScripts = () => {
        if (loaded) return;
        loaded = true;

        const script = document.createElement('script');
        script.src = '/js/interactive.js';
        script.async = true;
        document.head.appendChild(script);
      };

      // Load on first user interaction
      ['mousedown', 'touchstart', 'keydown'].forEach(event => {
        document.addEventListener(event, loadInteractiveScripts, { once: true });
      });
    });
  </script>
</body>
</html>
```

**💡 GHI NHỚ:**
- **`async`** = **Download parallel**, **execute when ready**, **no order** ⚡
- **`defer`** = **Download parallel**, **execute after DOM**, **ordered** ⏳
- **Normal** = **Blocks parsing**, **immediate execution**, **ordered** 🔄
- **Choose based on** = Script dependencies và performance needs 🎯

**Script Strategy: Critical (normal) → Dependencies (defer) → Independent (async) → Lazy load (on interaction)!** 🚀

---

## 💼 Câu Hỏi Kinh Nghiệm & Thực Tế

**📌 [⬆️ Back to Top](#📚-câu-hỏi-frontend-interview---từ-cơ-bản-đến-senior) | [📋 Mục Lục](#📋-mục-lục-tổng-kết)**

*Phần này tập trung vào kinh nghiệm thực tế, cách xử lý vấn đề trong production và soft skills*

### EXP1: Mô tả dự án frontend phức tạp nhất bạn từng làm?

**Trả lời mẫu:**

**🎯 STRUCTURE câu trả lời theo STAR Method:**

**📋 STAR Method:**
- **🏢 S**ituation - Bối cảnh dự án
- **📋 T**ask - Nhiệm vụ cần hoàn thành
- **⚡ A**ction - Hành động thực hiện
- **📊 R**esult - Kết quả đạt được

**🧠 GHI NHỚ:** **S**how **T**echnical **A**bility **R**ealistically

**💡 TIPS KHI TRẢ LỜI:**
1. **🔢 QUANTIFY everything** (users, performance, timeline)
2. **🛠️ MENTION specific technologies** và lý do chọn
3. **🚧 HIGHLIGHT challenges** và cách overcome
4. **📈 SHOW business impact** không chỉ technical
5. **📚 SHARE lessons learned** cho future projects

```typescript
// Ví dụ mô tả dự án e-commerce platform
interface ProjectDescription {
  name: string;
  scope: string;
  timeline: string;
  teamSize: number;
  technologies: string[];
  challenges: Challenge[];
  results: string[];
}

interface Challenge {
  problem: string;
  solution: string;
  impact: string;
}

const complexProject: ProjectDescription = {
  name: "Multi-vendor E-commerce Platform",
  scope: "Full-stack e-commerce với real-time chat, payment integration, inventory management",
  timeline: "8 tháng",
  teamSize: 6,
  technologies: [
    "React 18", "TypeScript", "Next.js", "Redux Toolkit",
    "React Query", "Socket.io", "Stripe API", "AWS S3"
  ],
  challenges: [
    {
      problem: "Performance issues với large product lists (10,000+ items)",
      solution: "Implement virtual scrolling và server-side pagination với caching",
      impact: "Giảm load time từ 8s xuống 1.2s"
    },
    {
      problem: "Real-time inventory updates across multiple vendors",
      solution: "WebSocket integration với optimistic updates và conflict resolution",
      impact: "99.9% data consistency và instant updates"
    },
    {
      problem: "Complex state management với nested forms và wizards",
      solution: "Custom hooks với useReducer và context pattern",
      impact: "Giảm bugs từ 15% xuống 3%"
    }
  ],
  results: [
    "Successfully launched với 50,000+ daily active users",
    "Page load speed cải thiện 70%",
    "Bug rate giảm 80% so với version cũ",
    "Mobile conversion rate tăng 45%"
  ]
};

// Cách present project trong interview
function presentProject(): void {
  console.log(`
    📌 Project: ${complexProject.name}

    🎯 Scope: ${complexProject.scope}
    ⏱️ Timeline: ${complexProject.timeline}
    👥 Team: ${complexProject.teamSize} developers

    🛠️ Tech Stack:
    ${complexProject.technologies.map(tech => `- ${tech}`).join('\n')}

    🚧 Key Challenges & Solutions:
    ${complexProject.challenges.map(challenge => `
    Problem: ${challenge.problem}
    Solution: ${challenge.solution}
    Impact: ${challenge.impact}
    `).join('\n')}

    📊 Results:
    ${complexProject.results.map(result => `- ${result}`).join('\n')}
  `);
}
```

### EXP2: Xử lý performance issue trong production như thế nào?

**Trả lời mẫu:**

**Quy trình xử lý performance issues:**

```typescript
interface PerformanceIssue {
  type: 'loading' | 'runtime' | 'memory' | 'network';
  symptoms: string[];
  investigationSteps: string[];
  solution: string;
  prevention: string[];
}

class PerformanceTroubleshooter {
  // Bước 1: Identify và measure the problem
  identifyIssue(): PerformanceIssue[] {
    return [
      {
        type: 'loading',
        symptoms: [
          "First Contentful Paint > 3s",
          "Time to Interactive > 5s",
          "Large bundle size (>1MB)"
        ],
        investigationSteps: [
          "Sử dụng Lighthouse audit",
          "Analyze webpack bundle với webpack-bundle-analyzer",
          "Check Core Web Vitals trong Chrome DevTools"
        ],
        solution: `
          - Code splitting: React.lazy() và dynamic imports
          - Tree shaking để remove unused code
          - Image optimization với next/image hoặc WebP format
          - Preload critical resources
        `,
        prevention: [
          "Set up performance budgets trong CI/CD",
          "Regular bundle size monitoring",
          "Performance testing trong staging"
        ]
      }
    ];
  }

  // Bước 2: Real-world example - Slow loading issue
  async optimizeLoadingPerformance(): Promise<void> {
    // Before: All components loaded at once
    // import AllComponents from './AllComponents';

    // After: Code splitting và lazy loading
    const HomePage = React.lazy(() => import('./pages/HomePage'));
    const ProductPage = React.lazy(() => import('./pages/ProductPage'));
    const CheckoutPage = React.lazy(() => import('./pages/CheckoutPage'));

    // Preload critical data
    const criticalData = await this.preloadCriticalData();

    // Bundle splitting strategy
    const optimization = {
      splitChunks: {
        chunks: 'all',
        cacheGroups: {
          vendor: {
            test: /[\\/]node_modules[\\/]/,
            name: 'vendors',
            chunks: 'all',
          },
          common: {
            name: 'common',
            minChunks: 2,
            chunks: 'all',
          }
        }
      }
    };
  }

  // Bước 3: Runtime performance optimization
  optimizeRuntimePerformance(): void {
    // Memory leak detection và fix
    const memoryLeakSolutions = {
      eventListeners: "Remove event listeners trong cleanup",
      timers: "Clear intervals/timeouts trong useEffect cleanup",
      subscriptions: "Unsubscribe observables và websockets",
      domReferences: "Clear DOM references trong refs"
    };

    // Performance monitoring trong production
    const monitoring = {
      tools: ["New Relic", "Sentry Performance", "LogRocket"],
      metrics: ["LCP", "FID", "CLS", "TTFB"],
      alerts: "Set up alerts cho performance regressions"
    };
  }
}

// Real-world performance fix example
const performanceFix: PerformanceIssue = {
  type: 'runtime',
  symptoms: [
    "Trang product list lag khi scroll",
    "Memory usage tăng liên tục",
    "Browser freeze khi filter products"
  ],
  investigationSteps: [
    "Profile với React DevTools Profiler",
    "Memory tab trong Chrome DevTools",
    "Performance tab để analyze main thread blocking"
  ],
  solution: `
    1. Implement React.memo cho ProductCard components
    2. Virtualization cho large lists với react-window
    3. Debounce search input để giảm API calls
    4. Optimize re-renders với useMemo cho expensive calculations
    5. Replace inefficient lodash operations
  `,
  prevention: [
    "Performance testing với Jest và @testing-library/react",
    "Bundle size limits trong CI pipeline",
    "Regular performance audits",
    "User experience monitoring với RUM tools"
  ]
};
```

### EXP3: Debugging và troubleshooting trong môi trường thực tế?

**Trả lời mẫu:**

```typescript
interface DebuggingStrategy {
  environment: 'development' | 'staging' | 'production';
  tools: string[];
  approach: string[];
  escalation: string[];
}

class ProductionDebugging {
  // Debugging approach based on environment
  getDebuggingStrategy(env: string): DebuggingStrategy {
    const strategies: Record<string, DebuggingStrategy> = {
      production: {
        environment: 'production',
        tools: [
          "Sentry for error tracking",
          "LogRocket for session replay",
          "New Relic for performance monitoring",
          "CloudWatch logs for server-side issues"
        ],
        approach: [
          "Reproduce issue trong staging environment",
          "Check error logs và user sessions",
          "Analyze performance metrics",
          "Use feature flags để isolate problems"
        ],
        escalation: [
          "Hotfix deployment process",
          "Rollback strategy",
          "Communication với stakeholders",
          "Post-mortem analysis"
        ]
      }
    };

    return strategies[env];
  }

  // Real debugging scenario
  debugCriticalIssue(): void {
    const scenario = {
      issue: "Users không thể complete checkout process",
      impact: "Revenue loss, customer complaints",

      investigationProcess: [
        "1. Check Sentry for JavaScript errors",
        "2. Review payment gateway logs",
        "3. Analyze user sessions với LogRocket",
        "4. Test payment flow trong staging",
        "5. Check recent deployments for correlation"
      ],

      rootCause: "Payment validation regex broke sau dependency update",

      solution: [
        "Immediate: Hotfix regex pattern",
        "Short-term: Add comprehensive payment flow tests",
        "Long-term: Implement payment flow monitoring"
      ],

      prevention: [
        "End-to-end testing cho critical user flows",
        "Dependency update testing protocol",
        "Payment flow health checks",
        "Staged deployment với canary releases"
      ]
    };
  }

  // Advanced debugging techniques
  advancedDebuggingTechniques(): void {
    // Source map debugging trong production
    const sourceMapDebugging = {
      setup: "Configure source maps cho production builds",
      privacy: "Upload source maps to error tracking service only",
      debugging: "Map error stack traces back to original code"
    };

    // Feature flag debugging
    const featureFlagDebugging = {
      isolation: "Use feature flags để isolate problematic features",
      gradualRollout: "Gradually enable features để identify issues",
      instantRollback: "Quick disable features nếu có problems"
    };

    // Performance debugging
    const performanceDebugging = {
      realUserMonitoring: "Track actual user performance metrics",
      syntheticTesting: "Automated performance tests",
      performanceBudgets: "Alert khi performance degrades"
    };
  }
}
```

### EXP4: Làm việc với team và code review process?

**Trả lời mẫu:**

```typescript
interface TeamCollaboration {
  codeReviewProcess: CodeReviewProcess;
  communicationTools: string[];
  bestPractices: string[];
  conflictResolution: string[];
}

interface CodeReviewProcess {
  workflow: string[];
  checklist: string[];
  tools: string[];
  standards: CodingStandards;
}

interface CodingStandards {
  formatting: string;
  naming: string[];
  testing: string[];
  documentation: string[];
}

class TeamWorkflow {
  codeReviewProcess: CodeReviewProcess = {
    workflow: [
      "1. Create feature branch từ main/develop",
      "2. Implement feature với unit tests",
      "3. Self-review code trước khi create PR",
      "4. Create Pull Request với clear description",
      "5. Assign reviewers (ít nhất 2 người)",
      "6. Address review comments",
      "7. Get approval và merge"
    ],

    checklist: [
      "✅ Code follows established patterns",
      "✅ Tests cover new functionality",
      "✅ No console.logs hoặc debugging code",
      "✅ TypeScript types are properly defined",
      "✅ Performance implications considered",
      "✅ Accessibility requirements met",
      "✅ Error handling implemented",
      "✅ Documentation updated"
    ],

    tools: [
      "GitHub/GitLab for PR reviews",
      "ESLint + Prettier for code formatting",
      "Husky for pre-commit hooks",
      "SonarQube for code quality",
      "Jest for testing coverage"
    ],

    standards: {
      formatting: "Prettier với team config",
      naming: [
        "Components: PascalCase",
        "Functions: camelCase",
        "Constants: UPPER_SNAKE_CASE",
        "Files: kebab-case for components"
      ],
      testing: [
        "Unit tests cho all functions",
        "Integration tests cho components",
        "E2E tests cho critical flows",
        "Minimum 80% code coverage"
      ],
      documentation: [
        "JSDoc cho complex functions",
        "README cho each module",
        "API documentation với OpenAPI",
        "Component stories trong Storybook"
      ]
    }
  };

  // Effective code review practices
  conductCodeReview(): void {
    const reviewGuidelines = {
      positive: [
        "Recognize good code và improvements",
        "Suggest alternatives thay vì chỉ criticism",
        "Ask questions để understand reasoning",
        "Provide specific examples"
      ],

      constructive: [
        "Focus on code, not person",
        "Explain 'why' behind suggestions",
        "Offer to pair program for complex issues",
        "Link to documentation hoặc examples"
      ],

      efficient: [
        "Review small PRs (< 400 lines)",
        "Use async review cho non-urgent changes",
        "Schedule sync discussion cho major changes",
        "Use draft PRs để get early feedback"
      ]
    };
  }

  // Handling team conflicts
  resolveTeamConflicts(): void {
    const conflictScenarios = {
      technicalDisagreements: {
        approach: [
          "Research pros/cons của each approach",
          "Create small POCs để compare",
          "Involve senior developer/architect",
          "Document decision reasoning"
        ]
      },

      codeStyleDisputes: {
        approach: [
          "Refer to established team guidelines",
          "Update guidelines if needed",
          "Use automated tooling to enforce",
          "Focus on consistency over personal preference"
        ]
      },

      priorityConflicts: {
        approach: [
          "Discuss với Product Manager/Tech Lead",
          "Consider business impact vs technical debt",
          "Negotiate timeline adjustments",
          "Document tradeoffs made"
        ]
      }
    };
  }
}
```

### EXP5: Migration và upgrade project strategies?

**Trả lời mẫu:**

```typescript
interface MigrationStrategy {
  type: 'framework' | 'library' | 'tooling' | 'architecture';
  approach: 'bigBang' | 'incremental' | 'parallel';
  phases: MigrationPhase[];
  riskMitigation: string[];
}

interface MigrationPhase {
  name: string;
  duration: string;
  deliverables: string[];
  successCriteria: string[];
}

class ProjectMigration {
  // Real-world migration example: React 16 to React 18
  reactMigrationStrategy: MigrationStrategy = {
    type: 'framework',
    approach: 'incremental',
    phases: [
      {
        name: "Phase 1: Assessment & Planning",
        duration: "2 weeks",
        deliverables: [
          "Compatibility audit của dependencies",
          "Breaking changes analysis",
          "Migration timeline",
          "Testing strategy"
        ],
        successCriteria: [
          "All dependencies compatibility confirmed",
          "Risk assessment completed",
          "Team alignment on approach"
        ]
      },
      {
        name: "Phase 2: Core Dependencies Update",
        duration: "3 weeks",
        deliverables: [
          "React 18 installation",
          "Critical dependencies update",
          "Build system adjustments",
          "Basic functionality testing"
        ],
        successCriteria: [
          "Application builds successfully",
          "No runtime errors in development",
          "Core features working"
        ]
      },
      {
        name: "Phase 3: Feature-by-Feature Migration",
        duration: "6 weeks",
        deliverables: [
          "Migrate to new React 18 features",
          "Update state management patterns",
          "Performance optimizations",
          "Comprehensive testing"
        ],
        successCriteria: [
          "All features migrated successfully",
          "Performance metrics maintained/improved",
          "Full test coverage"
        ]
      }
    ],
    riskMitigation: [
      "Feature flags cho gradual rollout",
      "Comprehensive rollback plan",
      "Parallel environment testing",
      "User acceptance testing"
    ]
  };

  // Legacy system modernization approach
  modernizeLegacySystem(): void {
    const modernizationStrategy = {
      currentState: {
        tech: "jQuery, vanilla JS, server-side rendering",
        issues: [
          "Poor maintainability",
          "Slow development cycles",
          "Limited mobile responsiveness",
          "SEO và performance issues"
        ]
      },

      targetState: {
        tech: "React 18, TypeScript, Next.js, modern CSS",
        benefits: [
          "Component-based architecture",
          "Better developer experience",
          "Improved performance",
          "Mobile-first responsive design"
        ]
      },

      migrationApproach: {
        strategy: "Strangler Fig Pattern",
        steps: [
          "1. Set up new React app alongside legacy",
          "2. Migrate page by page",
          "3. Share common components/assets",
          "4. Gradually replace legacy routes",
          "5. Retire legacy system"
        ]
      }
    };
  }

  // Database migration coordination
  coordinateWithBackend(): void {
    const backendCoordination = {
      challenges: [
        "API contract changes",
        "Data format modifications",
        "Authentication updates",
        "Performance impacts"
      ],

      solutions: [
        "API versioning strategy",
        "Backward compatibility period",
        "Joint testing environments",
        "Incremental data migration"
      ],

      communication: [
        "Daily standups với backend team",
        "Shared documentation",
        "Integration testing schedule",
        "Rollback coordination plan"
      ]
    };
  }
}
```

### EXP6: Xử lý legacy code và technical debt?

**Trả lời mẫu:**

```typescript
interface TechnicalDebt {
  type: 'code' | 'architecture' | 'tooling' | 'documentation';
  priority: 'high' | 'medium' | 'low';
  impact: string;
  effort: string;
  strategy: string;
}

class TechnicalDebtManagement {
  // Assess và categorize technical debt
  assessTechnicalDebt(): TechnicalDebt[] {
    return [
      {
        type: 'code',
        priority: 'high',
        impact: "Blocking new feature development, causing bugs",
        effort: "3 sprints",
        strategy: "Refactor critical paths first, add comprehensive tests"
      },
      {
        type: 'tooling',
        priority: 'medium',
        impact: "Slower development cycles, developer frustration",
        effort: "1 sprint",
        strategy: "Upgrade build tools, improve CI/CD pipeline"
      }
    ];
  }

  // Legacy code refactoring strategy
  refactorLegacyCode(): void {
    const refactoringApproach = {
      // Phase 1: Understand và document
      understanding: [
        "Code archaeology - trace through complex functions",
        "Document current behavior với tests",
        "Identify code smells và anti-patterns",
        "Map dependencies và side effects"
      ],

      // Phase 2: Safe refactoring
      safeRefactoring: [
        "Write characterization tests cho existing behavior",
        "Extract methods để break down complex functions",
        "Introduce TypeScript types gradually",
        "Remove dead code carefully"
      ],

      // Phase 3: Architectural improvements
      architecture: [
        "Separate concerns (UI, business logic, data)",
        "Introduce proper abstraction layers",
        "Implement design patterns appropriately",
        "Improve error handling và logging"
      ]
    };

    // Example: Refactoring a complex legacy component
    this.refactorComplexComponent();
  }

  refactorComplexComponent(): void {
    // Before: 500-line component với mixed concerns
    const legacyIssues = {
      problems: [
        "Mixing UI rendering với business logic",
        "No TypeScript types",
        "Inline styles và hardcoded values",
        "No error boundaries",
        "Difficult to test"
      ],

      refactoringSteps: [
        "1. Add PropTypes/TypeScript interfaces",
        "2. Extract business logic to custom hooks",
        "3. Break down into smaller components",
        "4. Move styles to CSS modules",
        "5. Add proper error handling",
        "6. Write comprehensive tests"
      ]
    };

    // After: Clean, testable, maintainable code
    const improvedArchitecture = {
      structure: [
        "Container component cho state management",
        "Presentational components cho UI",
        "Custom hooks cho business logic",
        "Separate files cho constants và types",
        "Comprehensive test coverage"
      ]
    };
  }

  // Managing technical debt backlog
  manageTechnicalDebtBacklog(): void {
    const debtManagement = {
      prioritization: [
        "Business impact assessment",
        "Development velocity impact",
        "Risk assessment (security, performance)",
        "Effort estimation"
      ],

      communication: [
        "Regular tech debt reviews với stakeholders",
        "Include debt work trong sprint planning",
        "Document ROI của debt reduction",
        "Celebrate debt reduction wins"
      ],

      prevention: [
        "Code review standards",
        "Definition of Done includes quality criteria",
        "Regular architecture reviews",
        "Automated code quality checks"
      ]
    };
  }
}
```

### EXP7: Production deployment và monitoring experience?

**Trả lời mẫu:**

```typescript
interface DeploymentStrategy {
  type: 'blueGreen' | 'canary' | 'rollingUpdate' | 'feature';
  tools: string[];
  pipeline: DeploymentPipeline;
  monitoring: MonitoringSetup;
}

interface DeploymentPipeline {
  stages: string[];
  gates: string[];
  rollback: string[];
}

interface MonitoringSetup {
  metrics: string[];
  alerts: AlertConfig[];
  tools: string[];
}

interface AlertConfig {
  metric: string;
  threshold: string;
  action: string;
}

class ProductionOperations {
  deploymentStrategy: DeploymentStrategy = {
    type: 'canary',
    tools: [
      "GitHub Actions for CI/CD",
      "Docker for containerization",
      "AWS ECS/Kubernetes for orchestration",
      "CloudFront for CDN",
      "Route 53 for DNS management"
    ],

    pipeline: {
      stages: [
        "1. Code commit triggers build",
        "2. Run automated tests (unit, integration, e2e)",
        "3. Build và push Docker image",
        "4. Deploy to staging environment",
        "5. Run smoke tests",
        "6. Deploy to production (canary)",
        "7. Monitor metrics for 30 minutes",
        "8. Full production rollout if healthy"
      ],

      gates: [
        "All tests must pass (100%)",
        "Code coverage > 80%",
        "Security scan passes",
        "Performance benchmarks met",
        "Manual approval for production"
      ],

      rollback: [
        "Automated rollback on critical errors",
        "Database migration rollback strategy",
        "DNS cutover for immediate traffic switch",
        "Communication plan for incidents"
      ]
    },

    monitoring: {
      metrics: [
        "Error rate (< 0.1%)",
        "Response time (< 200ms p95)",
        "CPU usage (< 70%)",
        "Memory usage (< 80%)",
        "Business metrics (conversion rate)"
      ],

      alerts: [
        {
          metric: "Error rate",
          threshold: "> 1% for 5 minutes",
          action: "Auto-rollback and page on-call engineer"
        },
        {
          metric: "Response time",
          threshold: "> 500ms p95 for 10 minutes",
          action: "Alert development team"
        }
      ],

      tools: [
        "New Relic for application monitoring",
        "CloudWatch for infrastructure metrics",
        "PagerDuty for incident management",
        "Grafana for custom dashboards"
      ]
    }
  };

  // Real deployment incident handling
  handleDeploymentIncident(): void {
    const incidentResponse = {
      detection: [
        "Automated alerting detected error spike",
        "Customer support reported issues",
        "Monitoring dashboard showed anomalies"
      ],

      response: [
        "1. Immediate assessment - check recent deployments",
        "2. Identify scope - which features affected",
        "3. Rollback decision within 10 minutes",
        "4. Execute rollback procedure",
        "5. Verify system recovery",
        "6. Internal communication",
        "7. Customer communication if needed"
      ],

      postMortem: [
        "Root cause analysis within 24 hours",
        "Action items để prevent recurrence",
        "Process improvements",
        "Share learnings với team"
      ]
    };
  }

  // Advanced deployment techniques
  advancedDeploymentTechniques(): void {
    const techniques = {
      featureFlags: {
        purpose: "Decouple deployment từ feature release",
        implementation: "LaunchDarkly hoặc custom solution",
        benefits: [
          "Safe production testing",
          "Gradual user rollout",
          "Instant feature disable",
          "A/B testing capabilities"
        ]
      },

      canaryDeployment: {
        process: [
          "Deploy to 5% of servers first",
          "Monitor error rates và performance",
          "Gradually increase traffic if healthy",
          "Full rollout after validation"
        ],
        monitoring: [
          "Error rate comparison",
          "Performance metrics",
          "User experience metrics",
          "Business KPIs"
        ]
      },

      blueGreenDeployment: {
        setup: [
          "Maintain two identical environments",
          "Deploy to inactive environment",
          "Switch traffic instantly",
          "Keep old environment for quick rollback"
        ],
        advantages: [
          "Zero downtime deployment",
          "Instant rollback capability",
          "Full testing in production environment"
        ]
      }
    };
  }
}
```

### EXP8: Những thách thức lớn nhất khi scale application?

**Trả lời mẫu:**

```typescript
interface ScalingChallenge {
  category: 'performance' | 'architecture' | 'team' | 'data';
  challenge: string;
  impact: string;
  solution: string;
  metrics: string[];
}

class ApplicationScaling {
  scalingChallenges: ScalingChallenge[] = [
    {
      category: 'performance',
      challenge: "Frontend performance degradation với large datasets",
      impact: "User experience drop, higher bounce rate, customer complaints",
      solution: `
        - Implement virtual scrolling cho large lists
        - Data pagination và infinite scroll
        - Aggressive caching strategy
        - Code splitting và lazy loading
        - CDN optimization cho static assets
      `,
      metrics: [
        "Page load time: 8s → 2s",
        "Time to Interactive: 12s → 3s",
        "Bounce rate: 45% → 15%"
      ]
    },

    {
      category: 'architecture',
      challenge: "Monolithic frontend becomes unmaintainable",
      impact: "Slow development, frequent conflicts, difficult deployments",
      solution: `
        - Micro-frontend architecture
        - Module federation với Webpack 5
        - Independent team ownership
        - Shared component library
        - API contract standardization
      `,
      metrics: [
        "Deploy frequency: weekly → daily",
        "Lead time: 2 weeks → 3 days",
        "Team productivity: 40% increase"
      ]
    }
  ];

  // Real-world scaling scenario
  scaleEcommerceApplication(): void {
    const scenario = {
      initialState: {
        users: "10,000 daily active users",
        architecture: "Single React SPA",
        performance: "Acceptable với small catalog",
        team: "3 frontend developers"
      },

      growthChallenges: {
        traffic: "100,000+ daily active users",
        catalog: "50,000+ products với complex filtering",
        features: "Multi-language, multi-currency, personalization",
        team: "15+ developers across 4 teams"
      },

      scalingSolutions: {
        performance: [
          "Product catalog virtualization",
          "Search results pagination",
          "Image lazy loading và optimization",
          "Service worker caching",
          "GraphQL query optimization"
        ],

        architecture: [
          "Micro-frontend split by domain",
          "Shared design system",
          "API gateway pattern",
          "Event-driven communication",
          "Independent deployment pipelines"
        ],

        team: [
          "Domain-driven team structure",
          "Clear API contracts",
          "Automated testing suites",
          "Documentation standards",
          "Code ownership models"
        ]
      }
    };
  }

  // Performance scaling strategies
  performanceScalingStrategies(): void {
    const strategies = {
      clientSide: [
        "Bundle splitting và lazy loading",
        "Aggressive caching với service workers",
        "Image optimization và WebP format",
        "Critical CSS inlining",
        "Prefetching critical resources"
      ],

      serverSide: [
        "CDN deployment globally",
        "Server-side rendering optimization",
        "API response compression",
        "Database query optimization",
        "Caching layers (Redis, Memcached)"
      ],

      monitoring: [
        "Real User Monitoring (RUM)",
        "Synthetic performance testing",
        "Core Web Vitals tracking",
        "Business metrics correlation",
        "A/B testing for optimizations"
      ]
    };
  }

  // Team scaling challenges
  teamScalingChallenges(): void {
    const challenges = {
      communication: {
        problem: "Information silos giữa teams",
        solution: [
          "Regular cross-team sync meetings",
          "Shared documentation hub",
          "Architecture decision records",
          "Demo sessions cho knowledge sharing"
        ]
      },

      codeConsistency: {
        problem: "Different coding standards across teams",
        solution: [
          "Shared ESLint/Prettier configuration",
          "Component library with guidelines",
          "Code review cross-team participation",
          "Automated quality gates"
        ]
      },

      deployment: {
        problem: "Deployment conflicts và dependencies",
        solution: [
          "Independent deployment pipelines",
          "Feature flags cho safe releases",
          "Automated dependency checking",
          "Rollback automation"
        ]
      }
    };
  }
}
```

### EXP9: Trend và technologies mới bạn quan tâm?

**Trả lời mẫu:**

```typescript
interface TechnologyTrend {
  name: string;
  category: 'framework' | 'tooling' | 'methodology' | 'standard';
  maturity: 'experimental' | 'emerging' | 'established';
  impact: 'high' | 'medium' | 'low';
  adoptionPlan: string;
  learningResources: string[];
}

class TechnologyTrends {
  currentTrends: TechnologyTrend[] = [
    {
      name: "React Server Components",
      category: 'framework',
      maturity: 'emerging',
      impact: 'high',
      adoptionPlan: `
        - Experiment trong pet projects
        - Evaluate với Next.js 13+ App Router
        - Consider cho new projects với heavy server logic
        - Gradual adoption strategy
      `,
      learningResources: [
        "React docs về Server Components",
        "Next.js App Router documentation",
        "Dan Abramov's blog posts",
        "Hands-on practice projects"
      ]
    },

    {
      name: "WebAssembly (WASM)",
      category: 'standard',
      maturity: 'established',
      impact: 'high',
      adoptionPlan: `
        - Learn Rust/C++ for WASM compilation
        - Identify performance-critical modules
        - Prototype computation-heavy features
        - Evaluate bundle size tradeoffs
      `,
      learningResources: [
        "MDN WebAssembly documentation",
        "Rust và WebPack integration",
        "Performance benchmarking tools",
        "WASM community projects"
      ]
    }
  ];

  // Why these trends matter
  explainTrendRelevance(): void {
    const trendAnalysis = {
      serverComponents: {
        benefits: [
          "Better SEO và initial page load",
          "Reduced client bundle size",
          "Improved developer experience",
          "Better data fetching patterns"
        ],
        concerns: [
          "Learning curve for mental model shift",
          "Tooling ecosystem still maturing",
          "Complexity trong debugging",
          "Limited browser compatibility for some features"
        ],
        useCase: "Perfect cho content-heavy applications như blogs, e-commerce"
      },

      webAssembly: {
        benefits: [
          "Near-native performance for CPU-intensive tasks",
          "Language flexibility (Rust, C++, Go)",
          "Better security model",
          "Complementary to JavaScript"
        ],
        concerns: [
          "Additional complexity trong build process",
          "Limited DOM access",
          "Bundle size considerations",
          "Debugging challenges"
        ],
        useCase: "Image processing, games, scientific computing, cryptography"
      }
    };
  }

  // Learning và adoption strategy
  technologyAdoptionStrategy(): void {
    const strategy = {
      evaluation: [
        "Research community adoption và stability",
        "Evaluate learning curve vs benefits",
        "Consider team skillset và capacity",
        "Assess project requirements fit"
      ],

      experimentation: [
        "Start với personal projects",
        "Create proofs of concept",
        "Compare performance benchmarks",
        "Document lessons learned"
      ],

      gradualAdoption: [
        "Introduce trong low-risk features",
        "Train team members gradually",
        "Monitor production impact carefully",
        "Build internal expertise"
      ],

      stayingCurrent: [
        "Follow key developers trên Twitter",
        "Subscribe to relevant newsletters",
        "Attend conferences và meetups",
        "Participate trong open source projects"
      ]
    };
  }

  // Industry trends observation
  industryTrendsAnalysis(): void {
    const trends = {
      2024Predictions: [
        "AI-assisted development tools maturation",
        "Edge computing adoption for frontend",
        "Progressive Web Apps renaissance",
        "TypeScript continued dominance",
        "Performance-first development culture"
      ],

      emergingPatterns: [
        "Resumable frameworks (Qwik)",
        "Islands architecture (Astro)",
        "Edge-first SSR",
        "Build-time optimizations",
        "Developer experience focus"
      ],

      learningPriorities: [
        "Core web fundamentals remain critical",
        "Performance optimization skills",
        "Accessibility expertise",
        "Security best practices",
        "Cross-platform development"
      ]
    };
  }
}
```

---

## 🎯 Tổng Kết Summary

### 📝 **Key Concepts Cheat Sheet - Những kiến thức PHẢI NHỚ**

#### **🟢 JavaScript Core Essentials:**
```
🔑 Primitive vs Reference: Stack vs Heap, Copy VALUE vs Copy ADDRESS
🔑 var/let/const: Function vs Block scope, Hoisting vs TDZ
🔑 Event Loop: Call Stack → Web API → Callback Queue → Microtask Queue
🔑 Closure: Inner function + Outer variables = PRIVATE data
🔑 this binding: Arrow = Lexical, Regular = Dynamic context
🔑 Async: Callbacks → Promises → Async/Await (từ Hell đến Heaven)
🔑 Falsy: false, 0, "", null, undefined, NaN (nhớ: "FO"NUN")
🔑 == vs ===: Loose equality vs Strict equality (type coercion!)
```

#### **⚡ React Core Essentials:**
```
🔑 Virtual DOM: Lightweight copy, Diffing algorithm, Reconciliation
🔑 Keys in Lists: NEVER use index, use stable unique IDs
🔑 useState: Functional updates, Lazy initial state, Immutable updates
🔑 useEffect: Dependencies array, Cleanup function, Lifecycle coverage
🔑 useMemo vs useCallback: Cache VALUE vs Cache FUNCTION
🔑 React.memo: Shallow comparison, Prevent unnecessary re-renders
🔑 Parent re-render → Child re-render (unless optimized with memo)
```

#### **🚀 Performance Optimization:**
```
🔑 Code Splitting: React.lazy() + Suspense + dynamic imports
🔑 Memoization: React.memo, useMemo, useCallback (đúng chỗ, đúng lúc)
🔑 Bundle Optimization: Tree shaking, Dead code elimination
🔑 Virtualization: Chỉ render items visible (react-window/react-virtualized)
🔑 Memory Leaks: Event listeners, Timers, Subscriptions cleanup
🔑 Web Vitals: LCP, FID, CLS - measure what users feel
```

#### **🛡️ Security Must-Know:**
```
🔑 XSS Prevention: Sanitize inputs, Content Security Policy
🔑 CSRF Protection: CSRF tokens, SameSite cookies
🔑 Input Validation: Client + Server side validation
🔑 Secure Headers: HTTPS, HSTS, X-Frame-Options
🔑 Authentication: JWT properly, Secure storage practices
```

#### **🏗️ Architecture Patterns:**
```
🔑 SOLID Principles: SRP, OCP, LSP, ISP, DIP
🔑 Component Patterns: HOC, Render Props, Compound Components
🔑 State Management: Context API vs Redux vs Zustand
🔑 Code Organization: Feature-based folder structure
🔑 Micro-frontends: Module Federation, Independent deployments
```

#### **🧪 Testing Strategy:**
```
🔑 Testing Pyramid: Unit → Integration → E2E
🔑 React Testing: @testing-library/react, userEvent
🔑 Mocking: jest.mock(), MSW for API mocking
🔑 Accessibility Testing: jest-axe, screen readers
🔑 Performance Testing: Lighthouse, Web Vitals
```

#### **💙 TypeScript Essentials:**
```
🔑 Utility Types: Partial<T>, Pick<T,K>, Omit<T,K>, Record<K,T>
🔑 as const vs enum: Zero cost vs Runtime features
🔑 type vs interface: Functional vs OOP style, Union vs Declaration merging
🔑 Type Narrowing: Guards, discriminated unions, conditional types
🔑 unknown vs any: Type-safe vs Escape hatch
🔑 Browser Support: TypeScript MUST BE COMPILED to JavaScript
🔑 Advanced Types: Generics, typeof keyof, conditional types
```

---

### 💡 **Quick Mental Models - Cách tư duy nhanh**

#### **🎯 JavaScript Mental Models:**
```
📚 "Primitive = Copy the VALUE 📄→📄"
📚 "Reference = Copy the ADDRESS 📮→📮"
📚 "Event Loop = Restaurant with 1 Chef, Many Orders"
📚 "Closure = Function with Memory Bag 🎒"
📚 "this = Who called me? 👤"
```

#### **⚛️ React Mental Models:**
```
📚 "Virtual DOM = Blueprint, Real DOM = House 🏠"
📚 "useState = State Box with Setter 📦"
📚 "useEffect = Side Effect Manager 🎭"
📚 "Props = Mail sent 📬, State = Private diary 📓"
📚 "Re-render = Redraw the UI Canvas 🎨"
```

#### **⚡ Performance Mental Models:**
```
📚 "Bundle = Suitcase, Tree Shaking = Remove unused clothes 👕"
📚 "Code Splitting = Send postcards, not whole photo album 📮"
📚 "Memoization = Cache expensive calculations 💰"
📚 "Virtualization = Show only visible photos in gallery 📸"
```

#### **💙 TypeScript Mental Models:**
```
📚 "TypeScript = JavaScript with Type Bodyguard 🛡️"
📚 "Utility Types = Swiss Army Knife for types 🔧"
📚 "as const = Lock the value box 🔒"
📚 "enum = Named number/string catalog 📋"
📚 "type vs interface = Function vs Class style 🎭"
📚 "Generics = Template for multiple types 📄"
```

---

### ⚠️ **Common Interview Mistakes - Tránh những lỗi này!**

#### **❌ JavaScript Mistakes:**
```
🚫 Confusing var hoisting với let/const TDZ
🚫 Không hiểu this context trong arrow functions
🚫 Mixing up == với === (type coercion trap!)
🚫 Forgetting event loop order: Microtasks trước Macrotasks
🚫 Mutating objects/arrays trực tiếp (not immutable)
🚫 Không cleanup event listeners → Memory leaks
```

#### **❌ React Mistakes:**
```
🚫 Using array index as key in dynamic lists
🚫 Calling hooks inside loops/conditions
🚫 Forgetting dependency array trong useEffect
🚫 Overusing useMemo/useCallback (premature optimization)
🚫 Mutating state directly: state.push() ❌, setState([...state, newItem]) ✅
🚫 Not understanding when components re-render
```

#### **❌ Performance Mistakes:**
```
🚫 Bundle toàn bộ libraries khi chỉ cần 1 function
🚫 Not lazy loading routes/components
🚫 Unnecessary re-renders do object/function props
🚫 Loading all data at once thay vì pagination
🚫 Không optimize images (WebP, lazy loading)
🚫 Blocking main thread với heavy computations
```

---

### 🔥 **Last-Minute Quick Review - 5 phút trước phỏng vấn**

#### **⚡ 30-Second JavaScript Rapid Fire:**
```
🔹 Event Loop: Call Stack → Web API → Callback → Microtask
🔹 Closure: Function + Lexical Environment
🔹 this: Arrow=lexical, Regular=caller
🔹 Async: Callback Hell → Promise Chain → Async/Await
🔹 Hoisting: var=undefined, let/const=TDZ
```

#### **⚡ 30-Second React Rapid Fire:**
```
🔹 Virtual DOM: Diffing + Reconciliation
🔹 useState: Functional updates, immutable
🔹 useEffect: Dependencies + Cleanup
🔹 Keys: Stable unique IDs, NEVER index
🔹 Memoization: React.memo, useMemo, useCallback
```

#### **⚡ 30-Second Performance Rapid Fire:**
```
🔹 Code Splitting: React.lazy + Suspense
🔹 Bundle: Webpack/Vite, Tree shaking
🔹 Memory: Cleanup listeners/timers/subscriptions
🔹 Rendering: Virtualization for large lists
🔹 Network: Caching, compression, CDN
```

#### **💡 Golden Interview Rules:**
```
✨ EXPLAIN your THINKING PROCESS
✨ ASK CLARIFYING questions
✨ CODE first, then OPTIMIZE
✨ ADMIT when you DON'T KNOW something
✨ CONNECT technical concepts to BUSINESS VALUE
```

---

### 🎯 **Interview Success Formula**

**Cách chuẩn bị cho các câu hỏi kinh nghiệm:**

1. **Chuẩn bị STAR format**: Situation, Task, Action, Result
2. **Quantify achievements**: Sử dụng số liệu cụ thể
3. **Highlight problem-solving**: Tập trung vào cách giải quyết vấn đề
4. **Show growth mindset**: Demonstrative learning từ failures
5. **Technical depth**: Sẵn sàng deep dive vào technical details

**🎯 Tips cho phỏng vấn:**

**📋 PREPARATION CHECKLIST:**
- ✅ **2-3 dự án chi tiết** với metrics cụ thể
- ✅ **Practice explaining** complex concepts simply
- ✅ **Specific examples** của challenges và solutions
- ✅ **Show passion** for continuous learning
- ✅ **Demonstrate collaboration** và leadership skills

**🧠 MINDSET FRAMEWORK:**
```
📖 LEARN → 🛠️ APPLY → 📊 MEASURE → 🔄 IMPROVE
```

**🏆 SUCCESS FORMULA:**
```
💡 Technical Knowledge + 💬 Communication Skills + 🤝 Team Collaboration = HIRED!
```

**⚡ FINAL REMINDERS:**
- **🎯 BE SPECIFIC** - "Improved performance by 70%" thay vì "improved performance"
- **🛠️ SHOW PROCESS** - How you approach problems
- **📈 BUSINESS IMPACT** - Always connect technical work to business value
- **🔄 GROWTH MINDSET** - What you learned from failures
- **❓ ASK QUESTIONS** - Show curiosity about their challenges

---

# 🎉 **GOOD LUCK WITH YOUR INTERVIEW!**

**Remember:** *"The best developers are not those who never make mistakes, but those who learn from every mistake and share that knowledge to help others grow."*

**🚀 You've got this!** 💪

---

## 🔗 **Quick Links Cheat Sheet**

**📚 Sections:**
- [📋 Mục Lục](#📋-mục-lục-tổng-kết)
- [🟢 JavaScript Core](#1-javascript-core-fundamentals)
- [🟢 React Fundamentals](#2-react-fundamentals)
- [🟡 Câu Hỏi Trung Cấp](#q4-usestate-hook-hoạt-động-như-thế-nào)
- [🔴 Câu Hỏi Nâng Cao](#q16-thiết-kế-kiến-trúc-micro-frontend-cho-ứng-dụng-scale-lớn)
- [🚀 React Advanced](#q24-react-concurrent-mode-và-suspense---cách-hoạt-động-và-ứng-dụng)
- [💙 TypeScript Advanced](#💙-typescript-advanced-topics)
- [💼 Experience Questions](#💼-câu-hỏi-kinh-nghiệm--thực-tế)
- [🎯 Tổng Kết Summary](#🎯-tổng-kết-summary)

**🔥 Popular Questions:**
- [Event Loop](#q5-event-loop-hoạt-động-như-thế-nào-giải-thích-đơn-giản)
- [Closure](#q6-closure-và-data-privacy-trong-javascript)
- [Virtual DOM](#q20-virtual-dom-và-key-trong-lists)
- [useMemo vs useCallback](#q22-usememo-vs-usecallback-chi-tiết)
- [React Concurrent Mode](#q24-react-concurrent-mode-và-suspense---cách-hoạt-động-và-ứng-dụng)
- [Performance Optimization](#q28-deep-dive-react-performance-optimization-techniques)
- [Utility Types](#ts1-utility-types-trong-typescript---cách-sử-dụng-và-ứng-dụng)
- [type vs interface](#ts3-type-vs-interface---sự-khác-biệt-và-best-practices)

**⚡ Quick Reference:**
- [📝 Key Concepts Cheat Sheet](#📝-key-concepts-cheat-sheet---những-kiến-thức-phải-nhớ)
- [💡 Mental Models](#💡-quick-mental-models---cách-tư-duy-nhanh)
- [⚠️ Common Mistakes](#⚠️-common-interview-mistakes---tránh-những-lỗi-này)
- [🔥 Last-Minute Review](#🔥-last-minute-quick-review---5-phút-trước-phỏng-vấn)

**📌 [⬆️ Back to Top](#📚-câu-hỏi-frontend-interview---từ-cơ-bản-đến-senior)**

---

*Created with ❤️ for Frontend Developers*
