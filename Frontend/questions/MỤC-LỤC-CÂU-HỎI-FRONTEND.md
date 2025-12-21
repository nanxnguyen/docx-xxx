# 📚 MỤC LỤC CÂU HỎI FRONTEND - INTERVIEW QUESTIONS

> **Tổng hợp 30+ câu hỏi phỏng vấn Frontend từ cơ bản đến nâng cao** *(Được đồng bộ từ SUMMARY file)*  
> Cập nhật: November 27, 2025

---

## 📖 **Table of Contents**

- [I. JavaScript Core (Q01-Q22)](#i-javascript-core-q01-q22)
- [II. Async & Data Fetching (Q23-Q26)](#ii-async--data-fetching-q23-q26)
- [III. Advanced JavaScript (Q27-Q34)](#iii-advanced-javascript-q27-q34)
- [IV. React & Frameworks (Q35-Q36)](#iv-react--frameworks-q35-q36)
- [V. Build Tools & Modules (Q37-Q38)](#v-build-tools--modules-q37-q38)
- [VI. Browser APIs & Security (Q39-Q40)](#vi-browser-apis--security-q39-q40)
- [VII. UI Libraries & Performance (Q42-Q48)](#vii-ui-libraries--performance-q42-q48)
- [VIII. Senior-Level Topics (Q49-Q61)](#viii-senior-level-topics-q49-q61)

---

## **I. JavaScript Core** (Q01-Q22)

### **🔤 Data Types & Comparison**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q01** | [JavaScript Fundamentals Overview - Tổng Quan Nền Tảng](Q01-javascript-fundamentals-overview-tổng-quan-nền-tảng.md) | ⭐ | JavaScript core concepts, execution context, memory management |
| **Q02** | [Data Types & Memory Management - Tổng Hợp Toàn Diện](Q02-data-types-memory-management-tổng-hợp-toàn-diện.md) | ⭐⭐ | Primitive vs Reference, Stack vs Heap, GC |
| **Q03** | [ES5 vs ES6+ Features - So Sánh Chi Tiết & Cách Hoạt Động](Q03-es5-vs-es6+-features-so-sánh-chi-tiết-&-cách-hoạt-động.md) | ⭐⭐ | let/const, arrow functions, classes, modules, destructuring |
| **Q04** | [Hoisting & Temporal Dead Zone](Q04-hoisting-&-temporal-dead-zone.md) | ⭐⭐⭐ | var/let/const hoisting, TDZ, execution context |
| **Q05** | [Set/Map, WeakSet/WeakMap, WeakRef & FinalizationRegistry](Q05-setmap,-weaksetweakmap,-weakref-&-finalizationregistry.md) | ⭐⭐⭐ | Collections, Weak references, Garbage collection |
| **Q06** | [Event Loop - Cơ Chế Hoạt Động JavaScript (Technical Deep Dive)](Q06-event-loop-cơ-chế-hoạt-động-javascript.md) | ⭐⭐⭐⭐⭐ | Call stack, Task queue, Microtask queue |
| **Q07** | [Event Loop - Giải Thích Theo Cách Nói Chuyện Đời Thường](Q07-event-loop-giải-thích-theo-cách-nói-chuyện-đời-thường.md) | ⭐⭐ | Analogy, real-world examples |
| **Q08** | [Closure & Data Privacy](Q08-closure-&-data-privacy.md) | ⭐⭐⭐ | Lexical scope, private variables, module pattern |
| **Q22** | [Compare Data Types](Q22-compare-data-types-objects,-strings,-big-numbers-&-decimals.md) | ⭐⭐⭐ | Objects, Strings, Big Numbers, Decimals |

### **🚀 ES5 vs ES6+ Features**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q09** | [Arrow vs Regular Functions & this Binding](Q09-arrow-vs-regular-functions-&-this-binding.md) | ⭐⭐⭐ | this binding, call/apply/bind |
| **Q10** | [IIFE (Immediately Invoked Function Expression) & Functional Programming](Q10-iife-&-functional-programming.md) | ⭐⭐⭐ | IIFE pattern, scope isolation |
| **Q11** | [DOM Events - Event Flow, Delegation & Event Properties](Q11-dom-events-event-flow,-delegation-&-event-properties.md) | ⭐⭐⭐ | Bubbling, Capturing, Event delegation |

### **⚡ Event Loop & Async**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q12** | [DOM API & Query Methods](Q12-dom-api-&-query-methods.md) | ⭐⭐ | querySelector, getElementById, traversal |
| **Q13** | [Async/Await vs Promises vs Callbacks & Promise.all/any/race](Q13-asyncawait-vs-promises-vs-callbacks.md) | ⭐⭐⭐⭐ | Sequential execution, Promise.all/any/race |
| **Q19** | [Loop Performance & Async Loops](Q19-loop-performance-&-async-loops.md) | ⭐⭐⭐ | for vs forEach, async iterations |
| **Q21** | [Advanced Deferring Execution Techniques](Q21-advanced-deferring-execution-techniques-kỹ-thuật-trì-hoãn-thực-thi-nâng-cao.md) | ⭐⭐⭐⭐ | setTimeout, requestAnimationFrame, queueMicrotask |
| **Q38** | [Cancellation, Concurrency & Retry](Q38-cancellation,-concurrency-&-retry.md) | ⭐⭐⭐⭐ | AbortController, p-limit, retry strategies |

### **🔒 Closures & Functions**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q14** | [Axios Interceptors - Phân Tích Chi Tiết & Tối Ưu Hóa](Q14-axios-interceptors.md) | ⭐⭐⭐ | Request/Response interceptors, auth tokens |
| **Q15** | [Advanced Deferring Execution Techniques](Q15-advanced-deferring-execution-techniques.md) | ⭐⭐⭐⭐ | setTimeout, requestAnimationFrame, queueMicrotask |
| **Q16** | [Compare Data Types - Objects, Strings, Big Numbers & Decimals](Q16-compare-data-types.md) | ⭐⭐⭐ | Objects, Strings, Big Numbers, Decimals |

### **🌐 DOM & Browser Events**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q17** | [React Query (TanStack Query) - Data Fetching, Caching & State Management](Q17-react-query.md) | ⭐⭐⭐⭐ | Caching, stale-while-revalidate, mutations |
| **Q18** | [Browser Rendering (Paint, Repaint, Reflow)](Q18-browser-rendering.md) | ⭐⭐⭐⭐ | Paint, Repaint, Reflow optimization |

---

## **II. Async & Data Fetching** (Q23-Q26)

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q20** | [Handle Caching - HTTP Caching & Browser Cache Strategies](Q20-handle-caching.md) | ⭐⭐⭐⭐ | Cache-Control, ETag, Service Worker |
| **Q23** | [React Query (TanStack Query)](Q23-react-query-(tanstack-query)-data-fetching,-caching-&-state-management.md) | ⭐⭐⭐⭐ | Caching, stale-while-revalidate, mutations |
| **Q24** | [Browser Rendering](Q24-browser-rendering-(paint,-repaint,-reflow).md) | ⭐⭐⭐⭐ | Paint, Repaint, Reflow optimization |
| **Q25** | [Loop Performance & Async Loops](Q25-loop-performance-&-async-loops.md) | ⭐⭐⭐ | for vs forEach, async iterations |
| **Q20** | [Handle Caching - HTTP Caching & Browser Cache Strategies](Q20-handle-caching.md) | ⭐⭐⭐⭐ | Cache-Control, ETag, Service Worker |
| **Q41** | [Date & Time Handling - Xử Lý Múi Giờ Đúng Cách](Q41-date-time-handling.md) | ⭐⭐⭐ | Timezone handling, Date objects, libraries |
| **Q42** | [Client-Side Rendering (CSR) vs Server-Side Rendering (SSR)](Q42-csr-vs-ssr.md) | ⭐⭐⭐⭐ | Rendering strategies, performance comparison |
| **Q43** | [Authentication Flow An Toàn](Q43-authentication-flow.md) | ⭐⭐⭐⭐⭐ | Access Token, Refresh Token, Cookie Security |
| **Q44** | [Microfrontend & Monorepo](Q44-microfrontend-monorepo.md) | ⭐⭐⭐⭐⭐ | Module Federation, Multi-Framework, Communication |

---

## **III. Advanced JavaScript** (Q27-Q34)

### **🔧 Advanced Concepts**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q27** | [JavaScript Proxy](Q27-javascript-proxy.md) | ⭐⭐⭐⭐ | Proxy handlers, traps, validation |
| **Q28** | [JavaScript Classes](Q28-javascript-classes.md) | ⭐⭐⭐ | Class syntax, inheritance, static methods |
| **Q30** | [Generator Functions](Q30-generator-functions-&-async-generators.md) | ⭐⭐⭐⭐ | yield, async generators, iterators |
| **Q31** | [Memory Management](Q31-memory-management-&-garbage-collection.md) | ⭐⭐⭐⭐⭐ | Garbage collection, memory leaks (10 cases) |
| **Q47** | [Git Workflow & Team Collaboration](Q47-git-workflow.md) | ⭐⭐⭐ | Branching Strategy, Merge vs Rebase, Conflict Resolution |
| **Q53** | [CI/CD Pipeline - GitHub Actions, Deployment Automation](Q53-cicd-pipeline.md) | ⭐⭐⭐⭐⭐ | GitHub Actions, Build Optimization, Deployment |
| **Q54** | [Code Quality & Standards](Q54-code-quality.md) | ⭐⭐⭐⭐ | ESLint, Prettier, Code Review |
| **Q55** | [GraphQL vs REST - API Design, Apollo Client](Q55-graphql-vs-rest.md) | ⭐⭐⭐⭐ | API Design, Apollo Client, Queries/Mutations |
| **Q56** | [Web Accessibility (a11y)](Q56-web-accessibility.md) | ⭐⭐⭐⭐ | WCAG 2.1, ARIA, Screen Readers |
| **Q57** | [State Management Comparison](Q57-state-management.md) | ⭐⭐⭐⭐ | Redux vs Zustand vs Jotai |
| **Q58** | [Networking & Browser Internals](Q58-networking-browser.md) | ⭐⭐⭐⭐ | Mạng & Nội Tế Trình Duyệt |
| **Q59** | [CSS Architecture & Modern Styling Approaches](Q59-css-architecture.md) | ⭐⭐⭐⭐ | BEM, CSS Modules, Styled Components, Tailwind |
| **Q60** | [JavaScript Design Patterns for Frontend](Q60-js-design-patterns.md) | ⭐⭐⭐⭐⭐ | Singleton, Observer, Factory, Module, Dependency Injection |

---

## **IV. React & Frameworks** (Q35-Q36)

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q35** | [React Hooks & Advanced Patterns](Q35-react-hooks.md) | ⭐⭐⭐⭐⭐ | useState, useEffect, useMemo, custom hooks |
| **Q36** | [Next.js - React Framework](Q36-nextjs.md) | ⭐⭐⭐⭐ | SSR, SSG, ISR, App Router, Server Components |

---

## **V. Build Tools & Modules** (Q37-Q38)

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q37** | [CommonJS vs ES Modules](Q37-commonjs-vs-es-modules-(esm)-&-bundling-deep-dive.md) | ⭐⭐⭐⭐ | require vs import, tree shaking, bundling |

---

## **VI. Browser APIs & Security** (Q39-Q40)

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q39** | [Bảo mật Security trên Web Application](Q39-bảo-mật-security-trên-web-application.md) | ⭐⭐⭐⭐⭐ | XSS, CSRF, CORS, CSP, Authentication |
| **Q40** | [Browser Storage](Q40-browser-storage-localstorage,-sessionstorage,-cookie-&-indexeddb.md) | ⭐⭐⭐ | localStorage, sessionStorage, cookies, IndexedDB |

---

## **VII. UI Libraries & Performance** (Q42-Q48)

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q42** | [AG Grid - Enterprise Data Grid](Q42-ag-grid-enterprise-data-grid-performance,-real-time-updates,-best-practices.md) | ⭐⭐⭐⭐⭐ | Performance, real-time updates, getRowId, applyTransactionAsync |

---

## **VIII. Senior-Level Topics** (Q49-Q57)

> **🎯 Các chủ đề nâng cao cho Senior Frontend Developer**

### **🏗️ System Design & Architecture**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q49** | [System Design - Thiết kế Hệ thống Frontend Architecture](Q49-system-design-thiết-kế-hệ-thống-frontend-architecture.md) | ⭐⭐⭐⭐⭐ | Micro-frontends, Monorepo, BFF Pattern, State Architecture, Error Boundaries, Feature Flags |
| **Q50** | [Testing Strategy - Unit, Integration, E2E Testing](Q50-testing-strategy-unit,-integration,-e2e-testing.md) | ⭐⭐⭐⭐⭐ | Test Pyramid, Jest/Vitest, React Testing Library, Playwright/Cypress, Visual Regression |
| **Q51** | [Performance Monitoring & APM](Q51-performance-monitoring-&-apm-application-performance-monitoring.md) | ⭐⭐⭐⭐⭐ | Core Web Vitals, Sentry, DataDog, Performance Budgets, Source Maps |

### **🔧 Advanced TypeScript & DevOps**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q52** | [TypeScript Advanced Patterns](Q52-typescript-advanced-patterns-generics,-utility-types,-advanced-patterns.md) | ⭐⭐⭐⭐⭐ | Generic Constraints, Utility Types, Mapped Types, Type Guards, Branded Types |
| **Q53** | [CI/CD Pipeline - GitHub Actions, Deployment Automation](Q53-cicd-pipeline-github-actions,-deployment-automation.md) | ⭐⭐⭐⭐⭐ | GitHub Actions, Build Optimization, Blue-Green/Canary Deployment, Docker |
| **Q54** | [Code Quality & Standards](Q54-code-quality-&-standards-eslint,-prettier,-code-review.md) | ⭐⭐⭐⭐ | ESLint Advanced Config, Prettier, Husky, Commitlint, SonarQube, Bundle Analysis |

### **🌐 API & Accessibility**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q55** | [GraphQL vs REST - API Design, Apollo Client](Q55-graphql-vs-rest-api-design,-apollo-client.md) | ⭐⭐⭐⭐ | GraphQL Queries/Mutations, Apollo Cache, Pagination, Optimistic Updates |
| **Q56** | [Web Accessibility (a11y) - WCAG 2.1, ARIA, Screen Readers](Q56-web-accessibility-(a11y)-wcag-2.1,-aria,-screen-readers.md) | ⭐⭐⭐⭐ | WCAG Compliance, ARIA Attributes, Keyboard Navigation, Color Contrast, axe-core |
| **Q57** | [State Management Comparison - Redux vs Zustand vs Jotai](Q57-state-management-comparison-redux-vs-zustand-vs-jotai.md) | ⭐⭐⭐⭐ | Redux Toolkit, Zustand, Jotai Atoms, Performance Comparison, Migration Strategies |

### **🆕 NEW: CSS Architecture & Design Patterns (Q59-Q61)**

| # | Câu hỏi | Độ khó | Nội dung chính |
|---|---------|--------|----------------|
| **Q59** | [CSS Architecture & Modern Styling Approaches](Q59-css-architecture-&-modern-styling-approaches.md) | ⭐⭐⭐⭐ | BEM, CSS Modules, Styled Components, Tailwind CSS, Critical CSS Extraction |
| **Q60** | [JavaScript Design Patterns for Frontend](Q60-javascript-design-patterns-for-frontend.md) | ⭐⭐⭐⭐⭐ | Singleton, Observer, Pub/Sub, Factory, Module, Dependency Injection |
| **Q61** | [React Design Patterns - Advanced Architecture](Q61-react-design-patterns-advanced-architecture.md) | ⭐⭐⭐⭐⭐ | Compound Components, Render Props, HOC, Container/Presentational, Controlled vs Uncontrolled |

---

## 📊 **Statistics**

```
┌─────────────────────┬────────┬────────────┐
│ Category            │ Count  │ Percentage │
├─────────────────────┼────────┼────────────┤
│ JavaScript Core     │ 20     │ 64%        │
│ Async & Fetching    │ 5      │ 16%        │
│ Advanced JS/Tools   │ 6      │ 19%        │
├─────────────────────┼────────┼────────────┤
│ TOTAL               │ 31     │ 100%       │
└─────────────────────┴────────┴────────────┘
```

### **Độ khó phân bố:**

- ⭐ **Basic (1-2 ⭐):** 28% - Foundational concepts
- ⭐⭐⭐ **Intermediate (3 ⭐):** 37% - Common interview questions
- ⭐⭐⭐⭐ **Advanced (4 ⭐):** 23% - Senior-level topics
- ⭐⭐⭐⭐⭐ **Expert (5 ⭐):** 12% - Deep technical knowledge

---

## 🎯 **Learning Path Recommendations**

### **🌱 Beginner (0-1 năm kinh nghiệm)**
```
START HERE:
1. Q01-Q08: Data types & comparison
2. Q09-Q10: ES6+ features
3. Q17-Q18: DOM basics
4. Q19: Async fundamentals
5. Q35: React hooks basics
6. Q59: CSS Architecture (BEM, CSS Modules basics)
```

### **🚀 Intermediate (1-3 năm)**
```
1. Q12-Q13: Event loop deep dive
2. Q14-Q16: Closures & functions
3. Q20, Q23: Data fetching & caching
4. Q24: Browser rendering
5. Q31: Memory management
6. Q36: Next.js framework
7. Q60: JavaScript Design Patterns (Observer, Factory, Module)
```

### **🔥 Advanced (3+ năm) - Senior Level**
```
1. Q27: Proxy patterns
2. Q30: Generators
3. Q37: Module systems
4. Q38: Cancellation & concurrency
5. Q42: AG Grid performance
6. Q49-Q57: Senior Topics (System Design, Testing, CI/CD, TypeScript Advanced, GraphQL, a11y, State Management)
7. Q59-Q61: Advanced CSS + Design Patterns (Tailwind, CSS-in-JS, React Patterns, Dependency Injection)
```

---

## 📝 **How to Use This Guide**

### **1️⃣ Preparation (Chuẩn bị phỏng vấn)**
```markdown
- Đọc 5-10 câu/ngày theo learning path
- Practice coding examples trong mỗi câu
- Note lại concepts khó, review lại sau 1 tuần
```

### **2️⃣ Interview (Trong buổi phỏng vấn)**
```markdown
- Trả lời theo cấu trúc: Definition → Example → Use case
- Mention performance implications
- Bonus: So sánh với alternatives
```

### **3️⃣ On-the-job (Trong công việc)**
```markdown
- Áp dụng best practices từ Q26, Q31, Q35, Q42
- Reference Q20, Q23 khi implement data fetching
- Use Q37, Q39 cho build optimization
```

---

## 🔍 **Quick Reference**

### **Top 15 Most Important Questions:**

**🔥 Foundation (Must-know):**
1. **Q12** - Event Loop (Must-know cho mọi level)
2. **Q19** - Async/Await (90% projects dùng)
3. **Q31** - Memory Management (Production issues)
4. **Q35** - React Hooks (React ecosystem)
5. **Q15** - this Binding (Common bug source)

**⚡ Advanced (Mid-Senior):**
6. **Q23** - React Query (Modern data fetching)
7. **Q26** - Caching Strategies (Performance)
8. **Q24** - Browser Rendering (Optimization)
9. **Q36** - Next.js (Modern framework)
10. **Q42** - AG Grid (Enterprise apps)

**🎯 Senior-Level (Leadership):**
11. **Q49** - System Design (Micro-frontends, Architecture)
12. **Q50** - Testing Strategy (Test Pyramid, E2E)
13. **Q52** - TypeScript Advanced (Type System mastery)
14. **Q53** - CI/CD Pipeline (DevOps integration)
15. **Q55** - GraphQL vs REST (API design decisions)

### **Common Interview Combos:**

```
📍 Junior Interview (0-2 years):
   Q01 → Q03 → Q04 → Q19 → Q35 (basic)

📍 Mid-level Interview (2-4 years):
   Q12 → Q14 → Q15 → Q23 → Q31 → Q35 (advanced)

📍 Senior Interview (4+ years):
   Q12 → Q31 → Q49 → Q50 → Q52 → Q53
   
📍 Tech Lead Interview:
   Q49 (System Design) → Q50 (Testing) → Q53 (CI/CD) → Q56 (Accessibility) → Q57 (State Management)

📍 Performance-focused:
   Q24 → Q25 → Q26 → Q31 → Q42 → Q51

📍 Architecture-focused:
   Q36 (Next.js) → Q37 (Modules) → Q49 (System Design) → Q52 (TypeScript) → Q55 (API Design)
```

---

## 💡 **Tips for Success**

### **✅ DO:**
- Hiểu concept sâu, không chỉ thuộc lòng
- Practice coding examples hands-on
- Giải thích bằng analogy/real-world examples
- Mention trade-offs và when to use

### **❌ DON'T:**
- Đọc qua loa không thực hành
- Bỏ qua phần "Why" và "When to use"
- Học thuộc code mà không hiểu flow
- Ignore performance implications

---

## 📚 **Additional Resources**

- **MDN Web Docs:** https://developer.mozilla.org/
- **JavaScript.info:** https://javascript.info/
- **React Docs:** https://react.dev/
- **Next.js Docs:** https://nextjs.org/docs
- **AG Grid Docs:** https://www.ag-grid.com/

---

## 🎓 **Contribution**

Nếu phát hiện lỗi hoặc muốn bổ sung nội dung:
1. Fork repository
2. Create feature branch
3. Submit pull request với mô tả chi tiết

---

## 📅 **Version History**

- **v1.0** (Nov 2025) - Initial release với 48 câu hỏi
- **v1.1** - Thêm AG Grid, React Query, Memory Management
- **v1.2** - Merge Q22+Q23, Q31+Q32, optimize Q42
- **v2.0** (Nov 23, 2025) - ✨ **MAJOR UPDATE:** Thêm nhiều Senior-level topics:
  - Q41: Date & Time Handling
  - Q42: CSR vs SSR
  - Q43: Authentication Flow
  - Q44: Microfrontend & Monorepo
  - Q47: Git Workflow
  - Q53: CI/CD Pipeline & Deployment
  - Q54: Code Quality & Standards
  - Q55: GraphQL vs REST
  - Q56: Web Accessibility (a11y)
  - Q57: State Management Comparison
  - Q58: Networking & Browser Internals
  - Q59: CSS Architecture
  - Q60: JavaScript Design Patterns
  - **Total: 30+ câu hỏi theo thứ tự từ summary file**

---

**Happy Learning! 🚀**

> "The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie
>
> 
PROMPT FULL – “Senior Technical Answer Generator”
Câu hỏi: # 🗂️ Bảo Mật Security trên Web Application Frontend  (**"Web security = 7 layers: HTTPS, XSS, CSRF, Auth, Storage, API, Headers)
"Từ bây giờ, hãy trả lời mọi câu hỏi phỏng vấn Frontend ở cấp Senior/Technical Lead.
Mỗi câu trả lời phải bao gồm đầy đủ các phần sau bằng tiếng việt:

Tóm tắt 1–2 câu (để trả lời nhanh trong phỏng vấn).

Giải thích chi tiết ở cấp Senior/Staff, bao gồm kiến trúc, cơ chế, cách hoạt động.

Ví dụ code thực tế (React/JS/TS hoặc tùy ngữ cảnh).

Best Practices theo ngành.

Các pitfalls/lỗi phổ biến mà dev hay gặp

So sánh với các kỹ thuật/công nghệ khác nếu phù hợp.

Scenario thực tế trong dự án lớn để chứng minh hiểu biết.

Cách tối ưu hóa / nâng cấp giải pháp nếu được hỏi tiếp.

Phiên bản trả lời 1 phút cho phỏng vấn (đủ ý và sắc nét)