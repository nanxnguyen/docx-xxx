# 🔥 Frontend Real-World Problems & Deep Dive Questions

> **📖 Bộ câu hỏi Senior/Staff Engineer - 180 vấn đề thực tế Production**
> **🎯 System Design · Security · Performance · Architecture · Leadership**
> **✅ Checklist tracking - Đánh dấu câu đã học/trả lời được**


---

## 🗂️ **MỤC LỤC THEO CHỦ ĐỀ**

<details open>
<summary><strong>🚨 PART 1: CRITICAL PRODUCTION ISSUES (35 câu)</strong></summary>

### **A. Emergency Response & Incident Management** ⚠️
> *Production down, security breach, data loss - immediate action required*

- [ ] [Q0: Production Incident Response](#q0-production-incident) 🔴
  - *App crash 100% users, $10K/min loss*
- [ ] [Q1: Memory Leak at Scale](#q-1-memory-leak-at-scale) 🔴
  - *10K users, memory 2GB→8GB trong 2h*
- [ ] [Q2: Cascading Failures](#q-2-cascading-failures) 🔴
  - *API timeout → retry storm → complete system down*
- [ ] [Q3: Race Condition in Production](#q-3-race-condition-production) 🔴
  - *Concurrent updates → data corruption*
- [ ] [Q4: Zombie Process](#q-4-zombie-process) 🔴
  - *Background tasks không terminate → memory leak*

### **B. Security Critical Issues** 🔐
> *Zero-day exploits, data breaches, attack prevention*

- [ ] [Q5: Zero-Day XSS Attack](#q-5-zero-day-xss) 🔴
  - *Emergency patch trong 2 giờ, đang bị exploit*
- [ ] [Q6: Token Theft Attack](#q-6-token-theft-attack) 🔴
  - *JWT stolen, unauthorized access*
- [ ] [Q7: CSRF in Banking App](#q-7-csrf-banking-app) 🔴
  - *Fake money transfer, multi-layer defense*
- [ ] [Q8: Clickjacking Attack](#q-8-clickjacking-attack) 🔴
  - *Invisible iframe overlay stealing credentials*
- [ ] [Q9: Prototype Pollution](#q-9-prototype-pollution) 🔴
  - *Object.prototype modified → code execution*
- [ ] [Q10: CORS Misconfiguration](#q-10-cors-misconfiguration) 🔴
  - *Access-Control-Allow-Origin: * exposing APIs*
- [ ] [Q11: Dependency Vulnerability](#q-11-dependency-vulnerability) 🔴
  - *npm package critical CVE, hotfix strategy*
- [ ] [Q12: Man-in-the-Middle Attack](#q-12-mitm-attack) 🔴
  - *HTTP downgrade, SSL stripping*
- [ ] [Q13: SQL Injection via Frontend](#q-13-sql-injection-frontend) 🔴
  - *GraphQL/REST injection vectors*
- [ ] [Q14: Session Hijacking](#q-14-session-hijacking) 🔴
  - *Session tokens intercepted, account takeover*

### **C. Performance at Scale** ⚡
> *Millions users, high load, optimization critical*

- [ ] [Q15: 1M Daily Users - Scale Bottleneck](#q-15-scale-bottleneck) 🔴
  - *App fine 10K users, crash 100K+*
- [ ] [Q16: CDN Strategy](#q-16-cdn-strategy) 🟡
  - *Global users, latency 500ms+, edge computing*
- [ ] [Q17: Database Query N+1](#q-17-database-n-plus-one) 🔴
  - *Frontend trigger 1000 DB queries*
- [ ] [Q18: Real-time at Scale](#q-18-realtime-at-scale) 🔴
  - *100K concurrent WebSocket connections*
- [ ] [Q19: Bundle Optimization](#q-19-bundle-optimization) 🟡
  - *Initial load 10s+, 5MB+ bundle*
- [ ] [Q20: Memory Pressure](#q-20-memory-pressure) 🔴
  - *Mobile browser crash sau 5 phút*

### **D. System Design & Architecture** 🏗️
> *Large-scale system design, distributed systems*

- [ ] [Q21: Microfrontend Migration](#q-21-microfrontend-migration) 🟡
  - *Monolith → Microfrontends, 5 teams*
- [ ] [Q22: State Management at Scale](#q-22-state-management-scale) 🟡
  - *Redux 50MB+ store, slow re-renders*
- [ ] [Q23: Distributed Frontend](#q-23-distributed-frontend) 🟡
  - *Multi-region (US, EU, APAC), state sync*
- [ ] [Q24: Offline-First Architecture](#q-24-offline-first-architecture) 🟡
  - *Sync conflicts, CRDTs, event sourcing*
- [ ] [Q25: Micro-Interactions Performance](#q-25-micro-interactions-performance) 🟡
  - *60fps animations với 10K data points*

### **E. Advanced Debugging & Monitoring** 🔍
> *Production debugging, observability, incident analysis*

- [ ] [Q26: Heisenbug](#q-26-heisenbug) 🔴
  - *Bug chỉ xảy ra production, không reproduce*
- [ ] [Q27: Memory Leak in Production](#q-27-memory-leak-production) 🔴
  - *Live profiling millions users*
- [ ] [Q28: Performance Regression](#q-28-performance-regression) 🔴
  - *Deploy mới chậm hơn 30%*
- [ ] [Q29: Distributed Tracing](#q-29-distributed-tracing) 🟡
  - *Track request qua 5 microfrontends + 10 services*
- [ ] [Q30: Error Budget & SLO](#q-30-error-budget) 🟡
  - *Define SLO/SLI cho frontend*

### **F. Business-Critical Scenarios** 💰
> *High-stakes features, revenue impact, compliance*

- [ ] [Q31: Flash Sale](#q-31-flash-sale) 🔴
  - *100K users đồng thời, 100 items, prevent stampede*
- [ ] [Q32: Payment Gateway Timeout](#q-32-payment-gateway-timeout) 🔴
  - *Uncertain payment status, idempotency*
- [ ] [Q33: Trading Platform](#q-33-trading-platform) 🔴
  - *Real-time stock prices, eventual consistency*
- [ ] [Q34: Regulatory Compliance](#q-34-regulatory-compliance) 🔴
  - *GDPR/SOC2, audit logs*
- [ ] [Q35: Multi-Tenant SaaS](#q-35-multi-tenant-saas) 🔴
  - *1000 tenants, data isolation*

**📊 Part 1 Progress: [ ] 0/35 completed**

</details>

---

<details>
<summary><strong>💻 PART 2: CORE TECHNICAL ISSUES (40 câu)</strong></summary>

### **G. Memory & Performance** 🧠
> *Memory leaks, performance bottlenecks, optimization*

- [ ] [Q36: Memory Leak Debugging](#q1-memory-leak-debugging) 🟡
  - *Heap snapshot analysis, detached nodes*
- [ ] [Q37: Performance Bottleneck](#q2-performance-bottleneck) 🟡
  - *CPU vs I/O bound, profiling tools*
- [ ] [Q38: Infinite Re-render](#q3-infinite-re-render) 🟡
  - *React component render loop, browser freeze*
- [ ] [Q39: Large List Rendering](#q4-large-list-rendering) 🟡
  - *10K+ items, virtualization*
- [ ] [Q40: Bundle Size](#q5-bundle-size) 🟡
  - *5MB+ bundle, code splitting*

### **H. Reference & Mutation** 🔄
> *Immutability, deep/shallow copy, state updates*

- [ ] [Q41: Unexpected Mutation](#q6-unexpected-mutation) 🟢
  - *Object/array modified unexpectedly*
- [ ] [Q42: Shallow vs Deep Copy](#q7-shallow-vs-deep-copy) 🟢
  - *When to use, trade-offs*
- [ ] [Q43: React State Update](#q8-react-state-update) 🟡
  - *setState but UI no update*
- [ ] [Q44: Redux Immutability](#q9-redux-immutability) 🟡
  - *Why immutable, consequences*
- [ ] [Q45: Object Freeze](#q10-object-freeze) 🟢
  - *Shallow vs deep freeze*

### **I. Async & Promise** ⏱️
> *Async patterns, race conditions, error handling*

- [ ] [Q46: Promise Hell](#q11-promise-hell) 🟢
  - *Callback hell → Promises/async-await*
- [ ] [Q47: Race Condition](#q12-race-condition) 🟡
  - *Multiple requests, cancel previous*
- [ ] [Q48: Request Cancellation](#q13-request-cancellation) 🟡
  - *AbortController, cleanup*
- [ ] [Q49: Retry Logic](#q14-retry-logic) 🟡
  - *Exponential backoff, jitter*
- [ ] [Q50: Concurrent Requests](#q15-concurrent-requests) 🟡
  - *100 APIs, limit 5 concurrent*
- [ ] [Q51: Promise.all vs allSettled](#q16-promise-all-vs-allsettled) 🟢
  - *Error handling differences*
- [ ] [Q52: Async Error Handling](#q17-async-error-handling) 🟡
  - *Global error handler, typed errors*

### **J. Closure & Scope** 🔒
> *Closures, memory leaks, private variables*

- [ ] [Q53: Loop Closure Bug](#q18-loop-closure-bug) 🟢
  - *for loop + setTimeout, wrong values*
- [ ] [Q54: Memory Leak from Closure](#q19-memory-leak-from-closure) 🟡
  - *Closure giữ reference*
- [ ] [Q55: Private Variables](#q20-private-variables) 🟢
  - *Closure vs WeakMap vs Symbols*
- [ ] [Q56: Module Pattern](#q21-module-pattern) 🟢
  - *Singleton với closure*
- [ ] [Q57: Event Listener Leak](#q22-event-listener-leak) 🟡
  - *addEventListener cleanup*

### **K. Event Loop & Timing** ⏰
> *Microtask, macrotask, requestAnimationFrame*

- [ ] [Q58: setTimeout 0](#q23-settimeout-0) 🟢
  - *Why not run immediately*
- [ ] [Q59: Microtask vs Macrotask](#q24-microtask-vs-macrotask) 🟢
  - *Promise vs setTimeout order*
- [ ] [Q60: requestAnimationFrame](#q25-requestanimationframe) �
  - *RAF vs setTimeout for animations*
- [ ] [Q61: Debounce vs Throttle](#q26-debounce-vs-throttle) 🟢
  - *Implementation, use cases*
- [ ] [Q62: Long Task Blocking](#q27-long-task-blocking) 🟡
  - *Break into chunks, Web Workers*
- [ ] [Q63: Event Loop Starvation](#q28-event-loop-starvation) 🟡
  - *Microtasks block macrotasks*

### **L. this Binding** 👉
> *Context loss, arrow functions, bind/call/apply*

- [ ] [Q64: Lost this Context](#q29-lost-this-context) 🟢
  - *Callback lose this, solutions*
- [ ] [Q65: Arrow Function this](#q30-arrow-function-this) 🟢
  - *Lexical binding, memory implications*
- [ ] [Q66: Event Handler this](#q31-event-handler-this) 🟢
  - *addEventListener this undefined*
- [ ] [Q67: call vs apply vs bind](#q32-call-apply-bind) 🟢
  - *Differences, use cases*
- [ ] [Q68: Constructor this](#q33-constructor-this) 🟢
  - *Forgot new keyword*

### **M. Type Coercion & Comparison** 🔢
> *Falsy values, == vs ===, NaN, type conversion*

- [ ] [Q69: Falsy Value Bugs](#q34-falsy-value-bugs) 🟢
  - *0, '', false, null treated same*
- [ ] [Q70: == vs ===](#q35-loose-vs-strict-equality) 🟢
  - *When == safe vs dangerous*
- [ ] [Q71: NaN Comparison](#q36-nan-comparison) 🟢
  - *NaN === NaN → false*
- [ ] [Q72: Array Comparison](#q37-array-comparison) 🟢
  - *[1,2] === [1,2] → false*
- [ ] [Q73: Object Key Coercion](#q38-object-key-coercion) 🟢
  - *Keys always string*
- [ ] [Q74: Implicit Conversion](#q39-implicit-conversion) 🟢
  - *"5" - 2 = 3 but "5" + 2 = "52"*
  
**📊 Part 2 Progress: [ ] 0/40 completed**

</details>

---

<details>
<summary><strong>🎨 PART 3: UI/UX & BROWSER (30 câu)</strong></summary>

### **N. DOM & Events** 🌐
> *Event delegation, propagation, memory leaks*

- [ ] [Q75: Event Delegation](#q40-event-delegation) 🟢
  - *1000 buttons → event delegation*
- [ ] [Q76: Event Propagation](#q41-event-propagation) 🟢
  - *stopPropagation vs preventDefault*
- [ ] [Q77: Memory Leak from DOM](#q42-memory-leak-from-dom) 🟡
  - *Detached nodes, references*
- [ ] [Q78: Reflow/Repaint](#q43-reflow-repaint) 🟡
  - *Layout thrashing, batching*
- [ ] [Q79: Virtual DOM](#q44-virtual-dom) 🟢
  - *Reconciliation, when slower*

### **O. React-Specific** ⚛️
> *Hooks, reconciliation, performance optimization*

- [ ] [Q80: useEffect Dependencies](#q45-useeffect-dependencies) 🟡
  - *Infinite loop, missing deps*
- [ ] [Q81: Stale Closure](#q46-stale-closure) 🟡
  - *useState in callback → old value*
- [ ] [Q82: Key Prop](#q47-key-prop) 🟢
  - *List without key, index as key*
- [ ] [Q83: Context Performance](#q48-context-performance) 🟡
  - *All consumers re-render*
- [ ] [Q84: Prop Drilling](#q49-prop-drilling) 🟢
  - *Props qua 5+ levels*
- [ ] [Q85: React Reconciliation](#q50-react-reconciliation) 🟡
  - *Fiber algorithm, optimization*
- [ ] [Q86: useMemo vs useCallback](#q51-usememo-vs-usecallback) 🟡
  - *When to use, premature optimization*
- [ ] [Q87: Custom Hooks](#q52-custom-hooks) 🟢
  - *Reusable logic, best practices*

### **P. UX & Interaction Design** 🎯
> *Empty states, loading, forms, navigation*

- [ ] [Q88: Empty State Design](#q146-empty-state) 🟢
  - *First-time vs returning users*
- [ ] [Q89: Form UX & Validation](#q147-form-ux) 🟢
  - *Real-time vs on-submit validation*
- [ ] [Q90: Progressive Image Loading](#q148-progressive-image) 🟢
  - *LQIP, BlurHash, lazy loading*
- [ ] [Q91: Font Rendering](#q149-font-rendering) 🟢
  - *Cross-platform consistency*
- [ ] [Q92: Navigation UX](#q150-navigation-ux) 🟢
  - *Breadcrumbs, mobile menu*
- [ ] [Q93: Data Visualization Performance](#q151-data-viz) 🟡
  - *10K+ data points, Canvas vs SVG*
- [ ] [Q94: File Upload UX](#q152-file-upload) 🟢
  - *Chunked upload, progress tracking*
- [ ] [Q95: Search Performance](#q153-search) 🟡
  - *1M+ records, debounce, fuzzy search*
- [ ] [Q96: Notification System](#q154-notifications) 🟢
  - *Toast vs banner, queue management*
- [ ] [Q97: Offline-First](#q155-offline-first) 🟡
  - *Service Worker, conflict resolution*

### **Q. Accessibility & i18n** ♿
> *WCAG compliance, internationalization*

- [ ] [Q98: Global i18n](#q157-global-i18n) 🟡
  - *20+ languages, RTL support*
- [ ] [Q99: A11y Compliance](#q137-accessibility) 🟢
  - *WCAG 2.1 AA, screen readers*
- [ ] [Q100: Form A11y](#q138-form-a11y) 🟢
  - *Labels, ARIA live regions*
- [ ] [Q101: Mobile A11y](#q139-mobile-a11y) 🟢
  - *Touch targets, gestures*
- [ ] [Q102: Performance vs A11y](#q140-perf-vs-a11y) 🟡
  - *Balance lazy loading với screen readers*

**📊 Part 3 Progress: [ ] 0/30 completed**

</details>

---

<details>
<summary><strong>🔧 PART 4: BUILD & DEPLOYMENT (25 câu)</strong></summary>

### **R. Build & Bundle** 📦
> *Webpack, Vite, tree shaking, code splitting*

- [ ] [Q103: Tree Shaking](#q53-tree-shaking) 🟡
  - *Why not working, ESM requirement*
- [ ] [Q104: Code Splitting](#q54-code-splitting) 🟡
  - *Route-based vs component-based*
- [ ] [Q105: Webpack vs Vite](#q55-webpack-vs-vite) 🟢
  - *HMR, dev server speed*
- [ ] [Q106: Source Maps](#q56-source-maps) 🟢
  - *Production trade-offs*
- [ ] [Q107: Polyfill Strategy](#q57-polyfill-strategy) 🟡
  - *Differential serving, bundle size*

### **S. Deployment & DevOps** 🚀
> *CI/CD, zero-downtime, monitoring*

- [ ] [Q108: Zero-Downtime Deployment](#q131-zero-downtime) 🟡
  - *Blue-green, canary releases*
- [ ] [Q109: CI/CD Pipeline](#q132-ci-cd-pipeline) 🟡
  - *Linting, tests, security scanning*
- [ ] [Q110: Feature Flags](#q133-feature-flags) 🟡
  - *Gradual rollout, kill switches*
- [ ] [Q111: Asset Optimization](#q134-asset-optimization) 🟡
  - *Images, fonts, compression*
- [ ] [Q112: Monorepo Strategy](#q135-monorepo-strategy) 🟡
  - *Nx vs Turborepo, caching*
- [ ] [Q113: Performance Budget](#q169-performance-budget) 🟡
  - *CI/CD enforcement, Lighthouse CI*
- [ ] [Q114: Build Pipeline Optimization](#q179-build-optimization) 🟡
  - *30min → 5min, parallel jobs*
- [ ] [Q115: Monorepo at Scale](#q180-monorepo-scale) 🟡
  - *1000+ packages management*

### **T. Infrastructure & CDN** 🌍
> *CDN, global deployment, resiliency*

- [ ] [Q116: Multi-Tenant White-Label](#q156-multi-tenant) 🟡
  - *Dynamic theming per tenant*
- [ ] [Q117: CDN Failover](#q166-cdn-failover) 🔴
  - *Multi-CDN strategy*
- [ ] [Q118: Global Deployment](#q177-global-deployment) 🟡
  - *Multi-region, data residency*
- [ ] [Q119: Resiliency](#q178-resiliency) 🟡
  - *Circuit breaker, graceful degradation*
- [ ] [Q120: Cost Optimization](#q176-cost-optimization) 🟡
  - *CDN bandwidth, infrastructure costs*

### **U. Monitoring & Observability** 📊
> *Logging, metrics, distributed tracing*

- [ ] [Q121: Frontend Observability](#q121-frontend-observability) 🟡
  - *RUM, logs, traces*
- [ ] [Q122: Custom Metrics](#q122-custom-metrics) 🟢
  - *User journey funnels, business metrics*
- [ ] [Q123: Correlation Analysis](#q123-correlation-causation) 🟡
  - *Metric spike root cause*
- [ ] [Q124: Core Web Vitals](#q124-core-web-vitals) 🟡
  - *LCP, FID, CLS optimization*
- [ ] [Q125: Error Tracking](#q125-error-tracking) 🟡
  - *Sentry, error boundaries, PII scrubbing*

**📊 Part 4 Progress: [ ] 0/25 completed**

</details>

---

<details>
<summary><strong>🏛️ PART 5: ARCHITECTURE & PATTERNS (25 câu)</strong></summary>

### **V. State Management** 🗄️
> *Redux, Zustand, Context, normalization*

- [ ] [Q126: Redux Boilerplate](#q64-redux-boilerplate) 🟢
  - *Redux Toolkit, createSlice*
- [ ] [Q127: Global vs Local State](#q65-global-vs-local-state) 🟢
  - *When to lift state up*
- [ ] [Q128: Derived State](#q66-derived-state) 🟢
  - *useMemo vs selector functions*
- [ ] [Q129: State Normalization](#q67-state-normalization) 🟡
  - *Flatten nested data*
- [ ] [Q130: Zustand vs Redux](#q68-zustand-vs-redux) 🟢
  - *Bundle size, DevTools, use cases*

### **W. Design Patterns** 🎨
> *React patterns, design system, component architecture*

- [ ] [Q131: Compound Components](#q126-compound-components) 🟢
  - *Context for implicit state sharing*
- [ ] [Q132: State Machines](#q127-state-machines) 🟡
  - *XState, finite state machine*
- [ ] [Q133: Render Props vs Hooks](#q128-render-props-vs-hooks) 🟢
  - *When to use each*
- [ ] [Q134: React Server Components](#q129-react-server-components) 🟡
  - *RSC architecture, benefits*
- [ ] [Q135: Concurrent React](#q130-concurrent-react) 🟡
  - *useTransition, useDeferredValue*
- [ ] [Q136: Component Architecture](#q106-component-architecture) 🟢
  - *Atomic design vs feature-based*
- [ ] [Q137: Design Patterns](#q108-design-patterns) 🟢
  - *HOC, Render Props, Factory*

### **X. API & Network** 🌐
> *REST, GraphQL, caching, error handling*

- [ ] [Q138: CORS Error](#q58-cors-error) 🟢
  - *Same-origin policy, preflight*
- [ ] [Q139: Token Refresh](#q59-token-refresh) 🟡
  - *401 handling, queue requests*
- [ ] [Q140: Request Interceptor](#q60-request-interceptor) 🟢
  - *Axios interceptors, add token*
- [ ] [Q141: Optimistic Update](#q61-optimistic-update) 🟡
  - *Update UI first, rollback on error*
- [ ] [Q142: Caching Strategy](#q62-caching-strategy) 🟡
  - *HTTP cache, React Query, SWR*
- [ ] [Q143: GraphQL vs REST](#q63-graphql-vs-rest) 🟢
  - *Over/under fetching*
- [ ] [Q144: Rate Limit Handling](#q162-rate-limit) 🟡
  - *429 response, exponential backoff*
- [ ] [Q145: API Versioning](#q163-api-versioning) 🟡
  - *v1 & v2 support simultaneously*

### **Y. Advanced Architecture** 🏗️
> *Microfrontends, SSR, system design*

- [ ] [Q146: SSR vs SSG vs CSR](#q142-ssr-vs-ssg) 🟡
  - *Rendering strategy decision*
- [ ] [Q147: GraphQL vs REST Decision](#q141-graphql-vs-rest-decision) 🟢
  - *Architecture choice factors*
- [ ] [Q148: TypeScript Adoption](#q144-typescript-adoption) 🟡
  - *Migration strategy, strictness*
- [ ] [Q149: Microfrontends Trade-offs](#q145-microfrontends-tradeoffs) 🟡
  - *When NOT to use*

**📊 Part 5 Progress: [ ] 0/25 completed**

</details>

---

<details>
<summary><strong>🔬 PART 6: TESTING & QUALITY (15 câu)</strong></summary>

### **Z. Testing Strategies** 🧪
> *Unit, integration, E2E, coverage*

- [ ] [Q150: Async Testing](#q74-async-testing) 🟢
  - *waitFor, findBy queries*
- [ ] [Q151: Mock API Calls](#q75-mock-api-calls) 🟢
  - *MSW, Jest mocks*
- [ ] [Q152: Test React Hooks](#q76-test-react-hooks) 🟢
  - *renderHook, act warnings*
- [ ] [Q153: E2E vs Unit Tests](#q77-e2e-vs-unit-tests) 🟢
  - *Testing pyramid, trade-offs*
- [ ] [Q154: Test Coverage](#q78-test-coverage) 🟢
  - *100% coverage meaning*

### **AA. Code Quality** ✨
> *Review, refactoring, technical debt*

- [ ] [Q155: Code Review Process](#q172-code-review) 🟢
  - *Checklist, constructive feedback*
- [ ] [Q156: Technical Debt](#q171-technical-debt) 🟡
  - *Balance features vs refactoring*
- [ ] [Q157: Legacy Migration](#q164-legacy-migration) 🟡
  - *jQuery → React, strangler pattern*
- [ ] [Q158: Incident Post-Mortem](#q170-post-mortem) 🟡
  - *Blameless culture, 5 Whys*
- [ ] [Q159: Architecture Decisions](#q175-adr) 🟢
  - *ADR template, documentation*

### **AB. TypeScript** 📘
> *Types, interfaces, generics, utility types*

- [ ] [Q160: Type vs Interface](#q79-type-vs-interface) 🟢
  - *Declaration merging, use cases*
- [ ] [Q161: Generic Constraints](#q80-generic-constraints) 🟢
  - *extends keyword, conditional types*
- [ ] [Q162: Type Guards](#q81-type-guards) 🟢
  - *typeof, instanceof, custom predicates*
- [ ] [Q163: Utility Types](#q82-utility-types) 🟢
  - *Pick, Omit, Partial, Record*
- [ ] [Q164: any vs unknown](#q83-any-vs-unknown) 🟢
  - *Type-safe unknown*

**📊 Part 6 Progress: [ ] 0/15 completed**

</details>

---

<details>
<summary><strong>🎓 PART 7: LEADERSHIP & PROCESS (10 câu)</strong></summary>

### **AC. Team & Communication** 👥
> *Mentoring, stakeholder management, onboarding*

- [ ] [Q165: Onboarding Developers](#q173-onboarding) 🟢
  - *Fast & effective onboarding*
- [ ] [Q166: Stakeholder Communication](#q174-stakeholder-communication) 🟢
  - *Explain technical to non-technical*
- [ ] [Q167: Team Disagreement](#q-team-disagreement) 🔵
  - *Resolve architecture conflicts*
- [ ] [Q168: Mentoring Junior](#q-mentoring) 🔵
  - *Effective mentorship strategies*

### **AD. Business & Operations** 💼
> *Analytics, payments, compliance, third-party*

- [ ] [Q169: Analytics & Tracking](#q158-analytics) 🟢
  - *User behavior, GDPR compliance*
- [ ] [Q170: Payment Integration](#q160-payment-integration) 🟡
  - *PCI DSS, tokenization, 3D Secure*
- [ ] [Q171: OAuth Multi-Provider](#q161-oauth) 🟡
  - *Social login, account linking*
- [ ] [Q172: Third-Party Scripts](#q159-third-party-scripts) 🟢
  - *Async loading, performance impact*

### **AE. Crisis & Recovery** 🚨
> *Security incidents, data breaches, database recovery*

- [ ] [Q173: Security Incident](#q167-security-incident) 🔴
  - *Website hacked, immediate response*
- [ ] [Q174: Data Leak](#q168-data-leak) 🔴
  - *User data exposed, 72-hour rule*
- [ ] [Q175: Database Corruption](#q165-database-corruption) 🔴
  - *Recovery strategy, RCA*

**📊 Part 7 Progress: [ ] 0/10 completed**

</details>

---

## 📈 **OVERALL PROGRESS TRACKER**

```
┌─────────────────────────────────────────────────────────────┐
│                   COMPLETION DASHBOARD                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🚨 Part 1: Critical Production     [ ] 0/35  (0%)   🔴    │
│  💻 Part 2: Core Technical          [ ] 0/40  (0%)   🟡    │
│  🎨 Part 3: UI/UX & Browser         [ ] 0/30  (0%)   🟢    │
│  🔧 Part 4: Build & Deployment      [ ] 0/25  (0%)   🟡    │
│  🏛️ Part 5: Architecture            [ ] 0/25  (0%)   🟡    │
│  🔬 Part 6: Testing & Quality       [ ] 0/15  (0%)   🟢    │
│  🎓 Part 7: Leadership              [ ] 0/10  (0%)   🔵    │
│                                                              │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │
│  📊 TOTAL PROGRESS:                 [ ] 0/180 (0%)          │
│  ⏱️  Estimated Time Remaining:      90 hours                │
│  🎯 Target Completion:              [Set your date]         │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🎯 **LEARNING PATH RECOMMENDATIONS**

### **🥇 Foundation Track (Start Here)**
> *Essential concepts mọi Senior engineer cần biết*

**Week 1-2: Core Fundamentals**
- Part 2G: Memory & Performance (Q36-Q40)
- Part 2H: Reference & Mutation (Q41-Q45)
- Part 2M: Type Coercion (Q69-Q74)
- Part 3N: DOM & Events (Q75-Q79)

**Week 3-4: Async & React**
- Part 2I: Async & Promise (Q46-Q52)
- Part 2K: Event Loop (Q58-Q63)
- Part 3O: React-Specific (Q80-Q87)
- Part 5V: State Management (Q126-Q130)

### **🥈 Intermediate Track**
> *Architecture, performance, patterns*

**Week 5-6: Architecture & Design**
- Part 5W: Design Patterns (Q131-Q137)
- Part 5X: API & Network (Q138-Q145)
- Part 4R: Build & Bundle (Q103-Q107)
- Part 3P: UX Design (Q88-Q97)

**Week 7-8: Testing & Quality**
- Part 6Z: Testing Strategies (Q150-Q154)
- Part 6AA: Code Quality (Q155-Q159)
- Part 6AB: TypeScript (Q160-Q164)

### **🥇 Advanced Track**
> *Production-ready, scale, leadership*

**Week 9-10: Performance at Scale**
- Part 1C: Performance at Scale (Q15-Q20)
- Part 1D: System Design (Q21-Q25)
- Part 4S: Deployment (Q108-Q115)
- Part 4T: Infrastructure (Q116-Q120)

**Week 11-12: Critical Issues**
- Part 1A: Emergency Response (Q0-Q4)
- Part 1B: Security Critical (Q5-Q14)
- Part 1E: Advanced Debugging (Q26-Q30)
- Part 1F: Business-Critical (Q31-Q35)

### **👨‍💼 Leadership Track**
> *Team, process, communication*

**Week 13-14: People & Process**
- Part 7AC: Team & Communication (Q165-Q168)
- Part 7AD: Business Operations (Q169-Q172)
- Part 7AE: Crisis Management (Q173-Q175)
- Part 4U: Monitoring (Q121-Q125)

---

## 📝 **HOW TO USE THIS GUIDE**

### **Step 1: Self-Assessment**
```markdown
- [ ] Đọc qua toàn bộ questions trong 1 part
- [ ] Mark ✅ những câu bạn TỰ TIN trả lời được (70%+)
- [ ] Mark ⚠️ những câu bạn hiểu concept nhưng chưa vững (30-70%)
- [ ] Mark ❌ những câu hoàn toàn không biết (<30%)
```

### **Step 2: Learning Cycle**
```markdown
1️⃣ Chọn 1 topic (5-7 questions)
2️⃣ Research & understand concepts
3️⃣ Write down answers (Context → Solution → Trade-offs)
4️⃣ Practice coding examples
5️⃣ Mark completed ✅
6️⃣ Review after 3 days, 1 week, 1 month
```

### **Step 3: Interview Prep**
```markdown
📅 4 weeks before interview:
   - Complete Foundation Track
   - Focus on weak areas

📅 2 weeks before:
   - Complete Intermediate Track
   - Mock interviews

📅 1 week before:
   - Review Advanced Track critical questions
   - Rehearse top 50 most common

📅 Night before:
   - Skim Part 1 (Critical Issues)
   - Review your weak topics
```

---

## 🎁 **BONUS RESOURCES**

### **Recommended Tools**
- 🔍 Debugging: Chrome DevTools, React DevTools
- 📊 Monitoring: Sentry, Datadog, LogRocket
- ⚡ Performance: Lighthouse, Web Vitals, Bundle Analyzer
- 🧪 Testing: Jest, React Testing Library, Playwright
- 📦 Build: Vite, Webpack, Nx, Turborepo

### **Reading Materials**
- 📘 [React Docs Beta](https://react.dev)
- 📙 [Web.dev Performance](https://web.dev/performance)
- 📗 [MDN Web Docs](https://developer.mozilla.org)
- 📕 [JavaScript Info](https://javascript.info)

---

**🎯 Ready to start? Pick a track and begin! Good luck! 🚀**

### **🚨 CRITICAL SYSTEM ISSUES**
- [Q0: Production Incident Response - App crash toàn bộ users, xử lý thế nào?](#q0-production-incident)
- [Q-1: Memory Leak at Scale - 10,000 concurrent users, memory overflow, debug?](#q-1-memory-leak-at-scale)
- [Q-2: Cascading Failures - Một service down → domino effect, prevent?](#q-2-cascading-failures)
- [Q-3: Race Condition in Production - Data corruption từ concurrent updates, fix?](#q-3-race-condition-production)
- [Q-4: Zombie Process - Background tasks không die, memory tăng dần, giải quyết?](#q-4-zombie-process)

### **🔐 SECURITY CRITICAL ISSUES**
- [Q-5: Zero-Day XSS - Phát hiện XSS vulnerability trong production, emergency patch?](#q-5-zero-day-xss)
- [Q-6: Token Theft Attack - JWT tokens bị steal, revoke toàn bộ sessions?](#q-6-token-theft-attack)
- [Q-7: CSRF in Banking App - Chuyển tiền giả mạo, prevent với multiple layers?](#q-7-csrf-banking-app)
- [Q-8: Clickjacking Attack - Iframe overlay để steal credentials, defense?](#q-8-clickjacking-attack)
- [Q-9: Prototype Pollution - Object.prototype bị modify, exploit & prevent?](#q-9-prototype-pollution)
- [Q-10: CORS Misconfiguration - Expose sensitive APIs, secure properly?](#q-10-cors-misconfiguration)
- [Q-11: Dependency Vulnerability - npm package có CVE critical, hotfix strategy?](#q-11-dependency-vulnerability)
- [Q-12: Man-in-the-Middle - HTTP downgrade attack, HSTS & certificate pinning?](#q-12-mitm-attack)
- [Q-13: SQL Injection via Frontend - GraphQL/REST injection, sanitization layers?](#q-13-sql-injection-frontend)
- [Q-14: Session Hijacking - Session tokens intercepted, rotating tokens & fingerprinting?](#q-14-session-hijacking)

### **⚡ PERFORMANCE AT SCALE**
- [Q-15: 1M Daily Users - App chậm khi scale, bottleneck identification?](#q-15-scale-bottleneck)
- [Q-16: CDN Strategy - Global users, latency cao, CDN + edge computing?](#q-16-cdn-strategy)
- [Q-17: Database Query N+1 - Frontend trigger N+1, detect & optimize?](#q-17-database-n-plus-one)
- [Q-18: Real-time at Scale - 100K concurrent WebSocket, architecture?](#q-18-realtime-at-scale)
- [Q-19: Bundle Optimization - Initial load 10s+, aggressive optimization?](#q-19-bundle-optimization)
- [Q-20: Memory Pressure - Browser crash trên mobile, memory profiling?](#q-20-memory-pressure)

### **🏗️ SYSTEM DESIGN & ARCHITECTURE**
- [Q-21: Microfrontend Migration - Monolith → microfrontend, strategy & pitfalls?](#q-21-microfrontend-migration)
- [Q-22: State Management at Scale - Redux too slow, alternatives (Zustand, Jotai, Recoil)?](#q-22-state-management-scale)
- [Q-23: Distributed Frontend - Multi-region deployment, state sync?](#q-23-distributed-frontend)
- [Q-24: Offline-First Architecture - Sync conflicts, CRDTs, event sourcing?](#q-24-offline-first-architecture)
- [Q-25: Micro-Interactions Performance - 60fps animations với heavy data?](#q-25-micro-interactions-performance)

### **🔥 ADVANCED DEBUGGING & MONITORING**
- [Q-26: Heisenbug - Bug chỉ xảy ra production, không reproduce local?](#q-26-heisenbug)
- [Q-27: Memory Leak in Production - Profiling production với millions users?](#q-27-memory-leak-production)
- [Q-28: Performance Regression - Deploy mới chậm hơn 30%, root cause?](#q-28-performance-regression)
- [Q-29: Distributed Tracing - Track request qua microfrontends + microservices?](#q-29-distributed-tracing)
- [Q-30: Error Budget - SLO/SLI cho frontend, alerting strategy?](#q-30-error-budget)

### **💰 BUSINESS-CRITICAL SCENARIOS**
- [Q-31: Flash Sale - 100K users cùng lúc, prevent stampede?](#q-31-flash-sale)
- [Q-32: Payment Gateway Timeout - Uncertain payment status, idempotency?](#q-32-payment-gateway-timeout)
- [Q-33: Trading Platform - Real-time stock prices, eventual consistency?](#q-33-trading-platform)
- [Q-34: Regulatory Compliance - GDPR/SOC2, audit logs & data residency?](#q-34-regulatory-compliance)
- [Q-35: Multi-Tenant SaaS - Tenant isolation, data leakage prevention?](#q-35-multi-tenant-saas)

---

## **🚨 CRITICAL SYSTEM ISSUES**

### **Q0: Production Incident Response**
App crash ảnh hưởng 100% users, revenue loss $10K/minute:
1. Incident response protocol (detection → mitigation → resolution)?
2. Rollback strategy vs hotfix forward?
3. Communication plan (stakeholders, users, team)?
4. Post-mortem process (blameless culture)?
5. Prevent similar incidents (circuit breakers, canary deployment)?
6. SLA/SLO violations handling?
7. Data integrity verification sau incident?
8. Recovery time objective (RTO) vs recovery point objective (RPO)?

### **Q-1: Memory Leak at Scale**
10,000 concurrent users, server memory tăng từ 2GB → 8GB trong 2 giờ:
1. Live debugging production (không down service)?
2. Heap dump analysis với millions objects?
3. Identify leaking components (React components, event listeners, timers)?
4. Progressive rollout của fix (phased deployment)?
5. Monitoring & alerting để catch early?
6. Load testing để reproduce?
7. Memory limit enforcement (Node.js --max-old-space-size)?
8. Trade-offs giữa performance và memory safety?

### **Q-2: Cascading Failures**
API Gateway timeout → Frontend retries → Database overload → Complete system down:
1. Circuit breaker pattern implementation?
2. Bulkhead isolation giữa services?
3. Graceful degradation strategy?
4. Timeout tuning (connect, read, total)?
5. Rate limiting & throttling?
6. Backpressure handling?
7. Chaos engineering để test resilience?
8. Observability để detect cascade early?

### **Q-3: Race Condition in Production**
Multiple users update cùng document → Data corruption, lost updates:
1. Optimistic locking vs pessimistic locking?
2. CRDTs (Conflict-free Replicated Data Types)?
3. Operational Transformation (như Google Docs)?
4. Version vectors & conflict resolution?
5. Atomic operations & transactions?
6. Idempotency keys?
7. Eventual consistency handling?
8. User experience during conflicts?

### **Q-4: Zombie Process**
Background sync tasks tăng dần, memory leak, browser tab crash:
1. Task lifecycle management?
2. AbortController cho cleanup?
3. Web Workers lifecycle?
4. Service Worker update strategy?
5. Visibility API để pause tasks?
6. RequestIdleCallback để yield?
7. Memory monitoring & auto-cleanup?
8. Graceful task termination?

---

## **🔐 SECURITY CRITICAL ISSUES**

### **Q-5: Zero-Day XSS**
Security researcher report XSS vulnerability, đang bị exploit:
1. Emergency response (patch trong 2 giờ)?
2. Content Security Policy (CSP) để mitigate ngay?
3. Input sanitization strategy (DOMPurify)?
4. Output encoding (React auto-escaping)?
5. WAF rules để block attack patterns?
6. Vulnerability disclosure process?
7. Security headers (X-XSS-Protection, X-Frame-Options)?
8. Post-incident audit (tìm similar vulnerabilities)?

### **Q-6: Token Theft Attack**
Attacker steal JWT tokens, access unauthorized accounts:
1. Immediate token revocation strategy?
2. Token rotation & refresh flow?
3. Fingerprinting để detect stolen tokens?
4. Rate limiting trên sensitive endpoints?
5. Anomaly detection (IP, device, behavior)?
6. HttpOnly + Secure + SameSite cookies?
7. Short-lived tokens vs long-lived?
8. User notification & forced re-authentication?

### **Q-7: CSRF in Banking App**
Attacker trick user vào transfer tiền giả mạo:
1. CSRF tokens implementation?
2. Double submit cookie pattern?
3. SameSite cookie attribute?
4. Custom headers (X-Requested-With)?
5. Origin & Referer validation?
6. Re-authentication cho sensitive actions?
7. Transaction signing với OTP?
8. Defense in depth strategy?

### **Q-8: Clickjacking Attack**
Invisible iframe overlay để steal clicks/credentials:
1. X-Frame-Options header?
2. Content-Security-Policy frame-ancestors?
3. Frame-busting JavaScript?
4. Transparent overlay detection?
5. Click delay & user confirmation?
6. Visual security indicators?
7. Testing clickjacking vulnerabilities?
8. User education?

### **Q-9: Prototype Pollution**
Attacker modify Object.prototype → Code execution:
1. Input validation để prevent __proto__?
2. Object.create(null) for dictionaries?
3. Map instead of plain objects?
4. Freeze prototypes?
5. JSON.parse vulnerabilities?
6. Recursive merge functions?
7. Lodash merge vs deepmerge security?
8. Detection & monitoring?

### **Q-10: CORS Misconfiguration**
Access-Control-Allow-Origin: * expose sensitive APIs:
1. Whitelist specific origins?
2. Dynamic origin validation?
3. Credentials handling với CORS?
4. Preflight request optimization?
5. Vary: Origin header?
6. CORS vs JSONP security?
7. Subdomain security?
8. API Gateway CORS policies?

### **Q-11: Dependency Vulnerability**
React/Next.js dependency có critical CVE, 100K+ downloads/week:
1. Vulnerability scanning (npm audit, Snyk)?
2. Patch vs upgrade decision?
3. Vendor security advisories?
4. Lock file security?
5. Private registry với scanning?
6. SBOM (Software Bill of Materials)?
7. Zero-trust dependencies?
8. Emergency patching process?

### **Q-12: Man-in-the-Middle Attack**
HTTP downgrade, SSL stripping attacks:
1. HSTS (HTTP Strict Transport Security)?
2. HSTS preload list?
3. Certificate pinning?
4. Certificate Transparency?
5. Mixed content blocking?
6. Upgrade-Insecure-Requests?
7. Subresource Integrity (SRI)?
8. TLS 1.3 enforcement?

### **Q-13: SQL Injection via Frontend**
GraphQL query injection, REST API injection:
1. Parameterized queries enforcement?
2. Input validation layers?
3. Query complexity limiting?
4. Depth limiting (GraphQL)?
5. Whitelist allowed fields?
6. ORM security?
7. Prepared statements?
8. Backend validation (never trust frontend)?

### **Q-14: Session Hijacking**
Session tokens intercepted, account takeover:
1. Session fixation prevention?
2. Session rotation sau login?
3. IP binding & device fingerprinting?
4. Concurrent session limiting?
5. Session timeout strategy?
6. Remember-me token security?
7. Session invalidation on logout?
8. Activity monitoring?

---

## **⚡ PERFORMANCE AT SCALE**

### **Q-15: 1M Daily Users - Scale Bottleneck**
App fine với 10K users, crash với 100K+:
1. Load testing strategy (K6, Artillery, Gatling)?
2. Identify bottlenecks (CPU, memory, network, I/O)?
3. Horizontal scaling vs vertical scaling?
4. Caching layers (browser, CDN, application, database)?
5. Database connection pooling?
6. Async processing (queues, workers)?
7. Auto-scaling policies?
8. Capacity planning?

### **Q-16: CDN Strategy**
Users ở Asia truy cập US servers, latency 500ms+:
1. Multi-CDN strategy (Cloudflare, Akamai, Fastly)?
2. Edge computing (Cloudflare Workers, Lambda@Edge)?
3. Geographic routing?
4. Cache invalidation strategy?
5. Dynamic content caching?
6. Image optimization (WebP, AVIF, responsive)?
7. HTTP/2, HTTP/3 (QUIC)?
8. Cost optimization?

### **Q-17: Database Query N+1**
Frontend component trigger 1000 database queries:
1. GraphQL DataLoader pattern?
2. Batch requests?
3. Query planning?
4. Prefetching strategy?
5. Pagination vs infinite scroll?
6. Cursor-based vs offset-based pagination?
7. Database indexing?
8. Read replicas?

### **Q-18: Real-time at Scale**
100K concurrent WebSocket connections:
1. WebSocket server architecture (Socket.IO, uWebSockets)?
2. Message broker (Redis Pub/Sub, Kafka)?
3. Connection pooling & load balancing?
4. Sticky sessions?
5. Horizontal scaling WebSocket servers?
6. Backpressure handling?
7. Reconnection strategy (exponential backoff)?
8. Fallback to polling?

### **Q-19: Bundle Optimization**
Initial load 10MB+, Time to Interactive 15s:
1. Code splitting strategy (route-based, component-based)?
2. Tree shaking optimization?
3. Dynamic imports?
4. Preloading critical resources?
5. Compression (Brotli, Gzip)?
6. Minification & obfuscation?
7. Asset optimization (images, fonts)?
8. Bundle analysis (webpack-bundle-analyzer)?

### **Q-20: Memory Pressure**
Mobile browsers crash sau 5 phút usage:
1. Memory profiling trên mobile?
2. Garbage collection tuning?
3. Object pooling?
4. Virtual scrolling?
5. Image lazy loading & unloading?
6. Detached DOM nodes cleanup?
7. Service Worker memory limits?
8. Progressive Web App optimization?

---

## **🏗️ SYSTEM DESIGN & ARCHITECTURE**

### **Q-21: Microfrontend Migration**
Monolith React app → Microfrontends (5 teams):
1. Decomposition strategy (domain-driven)?
2. Module Federation vs iframe vs Web Components?
3. Shared dependencies management?
4. Routing strategy (shell routing vs distributed)?
5. State sharing (cross-microfrontend)?
6. Build & deployment pipeline?
7. Version compatibility?
8. Performance implications?

### **Q-22: State Management at Scale**
Redux store 50MB+, re-renders slow toàn app:
1. State normalization?
2. Selector optimization (Reselect, re-reselect)?
3. Code splitting reducers?
4. Zustand vs Jotai vs Recoil comparison?
5. React Query for server state?
6. Local state vs global state?
7. State persistence strategy?
8. DevTools performance?

### **Q-23: Distributed Frontend**
Multi-region deployment (US, EU, APAC):
1. State synchronization giữa regions?
2. Eventual consistency handling?
3. Conflict resolution?
4. Data residency & compliance?
5. Latency compensation?
6. Failover strategy?
7. Split-brain prevention?
8. Monitoring & observability?

### **Q-24: Offline-First Architecture**
PWA cần work 100% offline, sync khi online:
1. Service Worker caching strategy?
2. IndexedDB for complex data?
3. Background sync?
4. Conflict resolution (last-write-wins, CRDTs)?
5. Delta sync vs full sync?
6. Network detection?
7. Queue failed requests?
8. User feedback during sync?

### **Q-25: Micro-Interactions Performance**
60fps animations với 10K data points real-time:
1. RequestAnimationFrame optimization?
2. Web Workers for computation?
3. OffscreenCanvas?
4. GPU acceleration (will-change, transform)?
5. Throttle/debounce updates?
6. Virtualization cho data?
7. WASM for heavy computation?
8. Profiling animation performance?

---

## **🔥 ADVANCED DEBUGGING & MONITORING**

### **Q-26: Heisenbug**
Bug chỉ xảy ra production, 1% users, không reproduce được:
1. Distributed tracing (Datadog, New Relic)?
2. Session replay (LogRocket, FullStory)?
3. Feature flags để test in production?
4. Canary deployment?
5. Error context capture?
6. Environment differences analysis?
7. User cohort analysis?
8. Hypothesis-driven debugging?

### **Q-27: Memory Leak in Production**
Production server memory tăng dần, không thể restart:
1. Online heap dump collection?
2. Sampling profiler (low overhead)?
3. Memory timeline analysis?
4. Retained objects identification?
5. Gradual rollout của fix?
6. Blue-green deployment?
7. Canary analysis?
8. Automated rollback triggers?

### **Q-28: Performance Regression**
New deployment chậm hơn 30%, không rõ cause:
1. Synthetic monitoring (Lighthouse CI)?
2. Real User Monitoring (RUM)?
3. Performance budgets?
4. Regression testing?
5. Trace comparison (before/after)?
6. CPU profiling?
7. Network waterfall analysis?
8. Database query analysis?

### **Q-29: Distributed Tracing**
Request đi qua 5 microfrontends + 10 microservices:
1. OpenTelemetry implementation?
2. Trace context propagation?
3. Span creation strategy?
4. Sampling strategy (head-based, tail-based)?
5. Correlation IDs?
6. Service dependency graph?
7. Critical path analysis?
8. Trace visualization (Jaeger, Zipkin)?

### **Q-30: Error Budget**
Define SLO/SLI cho frontend application:
1. SLI metrics (availability, latency, error rate)?
2. SLO targets (99.9%, 99.95%)?
3. Error budget calculation?
4. Burn rate alerting?
5. Trade-offs (features vs reliability)?
6. Multi-window alerting?
7. User-centric SLIs?
8. Compliance với business requirements?

---

## **💰 BUSINESS-CRITICAL SCENARIOS**

### **Q-31: Flash Sale**
100K users click "Buy" cùng 1 lúc, only 100 items available:
1. Rate limiting strategy?
2. Queue system (virtual waiting room)?
3. Inventory locking?
4. Optimistic vs pessimistic locking?
5. Cache stampede prevention?
6. Database hotspot handling?
7. Fairness algorithm?
8. User experience during high load?

### **Q-32: Payment Gateway Timeout**
Payment API timeout, uncertain nếu payment succeeded:
1. Idempotency keys?
2. Retry logic (safe vs unsafe)?
3. Webhook for async confirmation?
4. Reconciliation process?
5. User communication strategy?
6. Refund automation?
7. Audit trail?
8. PCI compliance?

### **Q-33: Trading Platform**
Real-time stock prices, thousands updates/second:
1. WebSocket optimization?
2. Throttling updates (client-side)?
3. Conflation (merge updates)?
4. Priority queuing?
5. Delta updates vs snapshots?
6. Eventual consistency?
7. Stale data detection?
8. Circuit breaker for market data?

### **Q-34: Regulatory Compliance**
GDPR, SOC2, HIPAA compliance requirements:
1. Data retention policies?
2. Right to deletion implementation?
3. Audit logging (immutable)?
4. Data encryption (at rest, in transit)?
5. Access controls (RBAC, ABAC)?
6. Consent management?
7. Data residency?
8. Compliance monitoring?

### **Q-35: Multi-Tenant SaaS**
1000 tenants sharing infrastructure, prevent data leakage:
1. Tenant isolation strategy?
2. Database sharding vs schema separation?
3. Row-level security?
4. API key management?
5. Rate limiting per tenant?
6. Resource quotas?
7. Cross-tenant attack prevention?
8. Tenant-specific customization?

---

## **Phần 1: Memory & Performance Issues**
- [Q1: Memory Leak Debugging - Bạn phát hiện và fix memory leak như thế nào?](#q1-memory-leak-debugging)
- [Q2: Performance Bottleneck - App chậm, làm sao tìm và tối ưu?](#q2-performance-bottleneck)
- [Q3: Infinite Re-render - React component render liên tục, debug thế nào?](#q3-infinite-re-render)
- [Q4: Large List Rendering - Render 10,000+ items, làm sao tối ưu?](#q4-large-list-rendering)
- [Q5: Bundle Size - App bundle quá lớn, làm sao giảm?](#q5-bundle-size)

### **Phần 2: Reference & Mutation Issues**
- [Q6: Unexpected Mutation - Object/Array bị thay đổi không mong muốn, tại sao?](#q6-unexpected-mutation)
- [Q7: Shallow vs Deep Copy - Khi nào cần shallow/deep copy? Trade-offs?](#q7-shallow-vs-deep-copy)
- [Q8: React State Update - setState nhưng UI không update, tại sao?](#q8-react-state-update)
- [Q9: Redux Immutability - Tại sao Redux yêu cầu immutability? Vi phạm sẽ ra sao?](#q9-redux-immutability)
- [Q10: Object Freeze - Object.freeze() hoạt động thế nào? Khi nào dùng?](#q10-object-freeze)

### **Phần 3: Async & Promise Issues**
- [Q11: Promise Hell - Nhiều async operations, làm sao tránh callback hell?](#q11-promise-hell)
- [Q12: Race Condition - User click nhanh → nhiều requests, xử lý thế nào?](#q12-race-condition)
- [Q13: Request Cancellation - Hủy request khi user navigate away, làm sao?](#q13-request-cancellation)
- [Q14: Retry Logic - API fail → retry với exponential backoff, implement thế nào?](#q14-retry-logic)
- [Q15: Concurrent Requests - Gọi 100 APIs cùng lúc nhưng limit 5 concurrent, làm sao?](#q15-concurrent-requests)
- [Q16: Promise.all vs Promise.allSettled - Khi nào dùng cái nào?](#q16-promise-all-vs-allsettled)
- [Q17: Async Error Handling - Catch errors từ multiple async operations thế nào?](#q17-async-error-handling)

### **Phần 4: Closure & Scope Issues**
- [Q18: Loop Closure Bug - for loop với setTimeout, in sai giá trị, tại sao?](#q18-loop-closure-bug)
- [Q19: Memory Leak from Closure - Closure giữ reference → memory leak, giải quyết?](#q19-memory-leak-from-closure)
- [Q20: Private Variables - Implement private properties không dùng class, làm sao?](#q20-private-variables)
- [Q21: Module Pattern - Tạo singleton pattern với closure, implement thế nào?](#q21-module-pattern)
- [Q22: Event Listener Leak - addEventListener không cleanup → leak, debug?](#q22-event-listener-leak)

### **Phần 5: Event Loop & Timing Issues**
- [Q23: setTimeout 0 - setTimeout(fn, 0) hoạt động thế nào? Tại sao không chạy ngay?](#q23-settimeout-0)
- [Q24: Microtask vs Macrotask - Promise vs setTimeout, thứ tự thực thi ra sao?](#q24-microtask-vs-macrotask)
- [Q25: requestAnimationFrame - RAF khác setTimeout thế nào? Khi nào dùng?](#q25-requestanimationframe)
- [Q26: Debounce vs Throttle - Implement debounce/throttle? Use cases?](#q26-debounce-vs-throttle)
- [Q27: Long Task Blocking - Task chạy lâu block UI, giải quyết thế nào?](#q27-long-task-blocking)
- [Q28: Event Loop Starvation - Microtasks nhiều → block macrotasks, xử lý?](#q28-event-loop-starvation)

### **Phần 6: this Binding Issues**
- [Q29: Lost this Context - Method pass vào callback → lose this, fix sao?](#q29-lost-this-context)
- [Q30: Arrow Function this - Arrow function trong class method, ảnh hưởng gì?](#q30-arrow-function-this)
- [Q31: Event Handler this - addEventListener(this.handleClick) → this undefined, tại sao?](#q31-event-handler-this)
- [Q32: call vs apply vs bind - Khi nào dùng cái nào? Performance khác nhau?](#q32-call-apply-bind)
- [Q33: Constructor this - Quên new khi gọi constructor, this trỏ đâu?](#q33-constructor-this)

### **Phần 7: Type Coercion & Comparison Issues**
- [Q34: Falsy Value Bugs - 0, '', false, null bị treat như nhau, xử lý thế nào?](#q34-falsy-value-bugs)
- [Q35: == vs === - Khi nào dùng == an toàn? Khi nào nguy hiểm?](#q35-loose-vs-strict-equality)
- [Q36: NaN Comparison - NaN === NaN → false, check NaN thế nào?](#q36-nan-comparison)
- [Q37: Array Comparison - [1,2] === [1,2] → false, so sánh array đúng cách?](#q37-array-comparison)
- [Q38: Object Key Coercion - Object key luôn là string, ảnh hưởng gì?](#q38-object-key-coercion)
- [Q39: Implicit Type Conversion - "5" - 2 = 3 nhưng "5" + 2 = "52", tại sao?](#q39-implicit-conversion)

### **Phần 8: DOM & Event Issues**
- [Q40: Event Delegation - 1000 buttons → 1000 listeners vs event delegation, so sánh?](#q40-event-delegation)
- [Q41: Event Propagation - stopPropagation vs preventDefault, khác nhau thế nào?](#q41-event-propagation)
- [Q42: Memory Leak from DOM - Remove element nhưng vẫn giữ reference, ảnh hưởng?](#q42-memory-leak-from-dom)
- [Q43: Reflow/Repaint - Làm sao tránh layout thrashing khi update DOM nhiều lần?](#q43-reflow-repaint)
- [Q44: Virtual DOM - Virtual DOM giải quyết vấn đề gì? Khi nào không cần?](#q44-virtual-dom)

### **Phần 9: React-Specific Issues**
- [Q45: useEffect Dependencies - Dependency array sai → infinite loop, debug?](#q45-useeffect-dependencies)
- [Q46: Stale Closure - useState trong callback → giá trị cũ, tại sao?](#q46-stale-closure)
- [Q47: Key Prop - List không có key hoặc key sai, ảnh hưởng gì?](#q47-key-prop)
- [Q48: Context Performance - Context re-render toàn bộ consumers, tối ưu thế nào?](#q48-context-performance)
- [Q49: Prop Drilling - Pass props qua 5+ levels, giải pháp?](#q49-prop-drilling)
- [Q50: React Reconciliation - React quyết định re-render thế nào? Tối ưu?](#q50-react-reconciliation)
- [Q51: useMemo vs useCallback - Khi nào dùng? Khi nào không nên dùng?](#q51-usememo-vs-usecallback)
- [Q52: Custom Hooks - Tạo custom hook để reuse logic, best practices?](#q52-custom-hooks)

### **Phần 10: Build & Bundle Issues**
- [Q53: Tree Shaking - Tree shaking không work, tại sao? Fix thế nào?](#q53-tree-shaking)
- [Q54: Code Splitting - Khi nào nên code split? Strategy?](#q54-code-splitting)
- [Q55: Webpack vs Vite - Khác nhau về build process? Khi nào dùng cái nào?](#q55-webpack-vs-vite)
- [Q56: Source Maps - Production có nên dùng source maps? Trade-offs?](#q56-source-maps)
- [Q57: Polyfill Strategy - Browser cũ cần polyfill gì? Làm sao tối ưu bundle?](#q57-polyfill-strategy)

### **Phần 11: Network & API Issues**
- [Q58: CORS Error - API call bị CORS, xử lý thế nào?](#q58-cors-error)
- [Q59: 401 Token Expired - Token hết hạn giữa chừng, refresh token thế nào?](#q59-token-refresh)
- [Q60: Request Interceptor - Axios interceptor để add token, implement ra sao?](#q60-request-interceptor)
- [Q61: Optimistic Update - Update UI trước khi API success, rollback khi fail?](#q61-optimistic-update)
- [Q62: Caching Strategy - Cache API responses, invalidation strategy?](#q62-caching-strategy)
- [Q63: GraphQL vs REST - Khi nào dùng GraphQL? Over-fetching/under-fetching?](#q63-graphql-vs-rest)

### **Phần 12: State Management Issues**
- [Q64: Redux Boilerplate - Redux nhiều boilerplate, giảm thế nào?](#q64-redux-boilerplate)
- [Q65: Global vs Local State - State nên để đâu? Khi nào hoist up?](#q65-global-vs-local-state)
- [Q66: Derived State - Compute từ state khác, nên dùng useMemo hay state?](#q66-derived-state)
- [Q67: State Normalization - Nested data trong Redux, normalize thế nào?](#q67-state-normalization)
- [Q68: Zustand vs Redux - So sánh performance, DX, use cases?](#q68-zustand-vs-redux)

### **Phần 13: Security Issues**
- [Q69: XSS Attack - Prevent XSS khi render user input thế nào?](#q69-xss-attack)
- [Q70: CSRF Attack - CSRF là gì? Prevent thế nào?](#q70-csrf-attack)
- [Q71: Secure Token Storage - Lưu JWT ở đâu an toàn? localStorage vs cookie?](#q71-secure-token-storage)
- [Q72: Input Sanitization - Sanitize user input, làm sao đúng cách?](#q72-input-sanitization)
- [Q73: Content Security Policy - CSP là gì? Config thế nào?](#q73-content-security-policy)

### **Phần 14: Testing Issues**
- [Q74: Async Testing - Test async code với Jest, best practices?](#q74-async-testing)
- [Q75: Mock API Calls - Mock axios/fetch trong tests thế nào?](#q75-mock-api-calls)
- [Q76: Test React Hooks - Test custom hooks, strategy?](#q76-test-react-hooks)
- [Q77: E2E vs Unit Tests - Khi nào dùng E2E? Khi nào unit test đủ?](#q77-e2e-vs-unit-tests)
- [Q78: Test Coverage - 100% coverage có nghĩa code quality tốt?](#q78-test-coverage)

### **Phần 15: TypeScript Issues**
- [Q79: Type vs Interface - Khi nào dùng type, khi nào interface?](#q79-type-vs-interface)
- [Q80: Generic Constraints - Tạo generic với constraints, use cases?](#q80-generic-constraints)
- [Q81: Type Guards - Implement type guards để narrow types?](#q81-type-guards)
- [Q82: Utility Types - Pick, Omit, Partial... khi nào dùng?](#q82-utility-types)
- [Q83: any vs unknown - Khác nhau thế nào? Khi nào dùng unknown?](#q83-any-vs-unknown)

### **Phần 16: SSR & Next.js Issues**
- [Q84: getServerSideProps vs getStaticProps - Khi nào dùng cái nào?](#q84-ssr-vs-ssg)
- [Q85: Hydration Mismatch - Server HTML khác client HTML, tại sao?](#q85-hydration-mismatch)
- [Q86: API Routes - Next.js API routes vs separate backend, trade-offs?](#q86-api-routes)
- [Q87: ISR (Incremental Static Regeneration) - ISR hoạt động thế nào? Use cases?](#q87-isr)
- [Q88: SSR Performance - SSR app chậm, tối ưu thế nào?](#q88-ssr-performance)

### **Phần 17: Microfrontend Issues**
- [Q89: Module Federation - Setup module federation với Webpack, challenges?](#q89-module-federation)
- [Q90: Shared Dependencies - Share React giữa các microfrontends, conflicts?](#q90-shared-dependencies)
- [Q91: Communication - Microfrontends communicate thế nào? Event bus?](#q91-microfrontend-communication)
- [Q92: Deployment - Deploy microfrontends independently, strategy?](#q92-microfrontend-deployment)
- [Q93: Styling Conflicts - CSS conflicts giữa microfrontends, giải quyết?](#q93-styling-conflicts)

### **Phần 18: Advanced Debugging**
- [Q94: Chrome DevTools - Dùng DevTools để debug performance, memory?](#q94-devtools-profiling)
- [Q95: Network Waterfall - Analyze network waterfall, tối ưu thế nào?](#q95-network-waterfall)
- [Q96: Lighthouse Audit - Lighthouse score thấp, improve thế nào?](#q96-lighthouse-audit)
- [Q97: Error Tracking - Setup Sentry/error tracking, best practices?](#q97-error-tracking)
- [Q98: Production Debugging - Debug issues chỉ xảy ra production, strategy?](#q98-production-debugging)

### **Phần 19: Real-World Scenarios**
- [Q99: Infinite Scroll - Implement infinite scroll with performance, làm sao?](#q99-infinite-scroll)
- [Q100: File Upload - Upload large files với progress, pause/resume?](#q100-file-upload)
- [Q101: Real-time Collaboration - Implement như Google Docs, architecture?](#q101-realtime-collaboration)
- [Q102: Offline Mode - PWA offline mode với sync khi online lại?](#q102-offline-mode)
- [Q103: Localization - i18n cho multi-language app, best practices?](#q103-localization)
- [Q104: AB Testing - Implement A/B testing frontend, strategy?](#q104-ab-testing)
- [Q105: Analytics - Track user behavior, privacy considerations?](#q105-analytics)

### **Phần 20: Architecture & Design Patterns**
- [Q106: Component Architecture - Atomic design vs feature-based, trade-offs?](#q106-component-architecture)
- [Q107: Folder Structure - Organize large codebase thế nào? Monorepo?](#q107-folder-structure)
- [Q108: Design Patterns - Factory, Observer, Singleton... trong React?](#q108-design-patterns)
- [Q109: Domain-Driven Design - DDD trong frontend, có nên apply?](#q109-ddd-frontend)
- [Q110: Micro vs Macro Components - Component granularity, strategy?](#q110-component-granularity)

---

## **Phần 1: Memory & Performance Issues**

### **Q1: Memory Leak Debugging**
Bạn phát hiện app React của mình có memory leak sau khi user navigate qua lại nhiều pages. Chrome DevTools Heap Snapshot cho thấy memory tăng dần. Làm thế nào để:
1. Xác định chính xác đâu là source of leak?
2. Common causes của memory leak trong React apps?
3. Tools và techniques để debug memory leaks?
4. Prevent memory leaks trong useEffect, event listeners, timers?
5. Detached DOM nodes là gì và làm sao detect?

### **Q2: Performance Bottleneck**
App của bạn chậm, user complain. Làm thế nào để:
1. Profile và identify performance bottlenecks?
2. Distinguish giữa CPU-bound vs I/O-bound issues?
3. Measure First Contentful Paint, Time to Interactive?
4. Optimize rendering performance trong React?
5. Trade-offs giữa code readability và performance?

### **Q3: Infinite Re-render**
React component của bạn render liên tục, browser freeze. Làm sao để:
1. Debug và tìm root cause?
2. Common patterns gây infinite re-render?
3. Fix useEffect dependencies issues?
4. Prevent object/array recreation trong render?
5. Dùng useMemo/useCallback đúng cách?

### **Q4: Large List Rendering**
Bạn cần render 10,000+ items trong list. Làm thế nào để:
1. Implement virtualization (react-window, react-virtualized)?
2. Optimize key prop strategy?
3. Handle dynamic item heights?
4. Implement infinite scroll với windowing?
5. Trade-offs của virtualization?

### **Q5: Bundle Size**
Production bundle của bạn quá lớn (5MB+), initial load chậm. Giải pháp:
1. Analyze bundle với webpack-bundle-analyzer?
2. Implement code splitting effectively?
3. Lazy load components và routes?
4. Tree shake unused code?
5. Optimize third-party dependencies?

---

## **Phần 2: Reference & Mutation Issues**

### **Q6: Unexpected Mutation**
Object/array của bạn bị thay đổi không mong muốn ở nơi khác trong code:
1. Làm sao trace back mutation source?
2. Object.freeze() vs immutability libraries?
3. Prevent mutations trong function parameters?
4. Deep freeze nested objects?
5. Performance impact của immutability?

### **Q7: Shallow vs Deep Copy**
Khi nào bạn cần shallow copy vs deep copy?
1. Implement deep copy safely (tránh circular references)?
2. Performance comparison: spread vs Object.assign vs structuredClone?
3. Handle Date, RegExp, Function trong deep copy?
4. Khi nào JSON.parse(JSON.stringify()) không đủ?
5. Immer vs native immutability?

### **Q8: React State Update**
setState nhưng UI không update:
1. Common causes (same reference, async updates)?
2. Fix state updates với nested objects?
3. Batch updates trong React 18?
4. Force re-render khi cần?
5. Debug state updates với React DevTools?

### **Q9: Redux Immutability**
Tại sao Redux require immutable state updates?
1. Consequences khi mutate Redux state trực tiếp?
2. Redux Toolkit RTK Query giải quyết thế nào?
3. Immer trong Redux Toolkit?
4. Shallow equality checks trong mapStateToProps?
5. Normalize state để avoid deep nesting?

### **Q10: Object Freeze**
Object.freeze() hoạt động thế nào?
1. Shallow freeze vs deep freeze?
2. Performance impact?
3. Khi nào nên dùng Object.freeze()?
4. Object.seal() vs Object.freeze() vs Object.preventExtensions()?
5. TypeScript readonly vs Object.freeze()?

---

## **Phần 3: Async & Promise Issues**

### **Q11: Promise Hell**
Nhiều async operations phụ thuộc lẫn nhau:
1. Refactor callback hell sang Promises/async-await?
2. Handle errors trong promise chains?
3. Khi nào dùng Promise.all vs sequential awaits?
4. Cancel promise chain khi user navigates away?
5. Timeout handling cho async operations?

### **Q12: Race Condition**
User click button nhanh → multiple API requests:
1. Prevent duplicate requests (debounce, flag)?
2. Cancel previous request khi có new request?
3. AbortController usage?
4. Handle out-of-order responses?
5. Optimistic updates với rollback?

### **Q13: Request Cancellation**
User navigate away trước khi request complete:
1. Implement request cancellation với AbortController?
2. Cleanup trong useEffect?
3. Cancel all pending requests khi unmount?
4. Handle cancelled requests errors?
5. Cancel requests trong Redux Toolkit?

### **Q14: Retry Logic**
API call fail → retry với exponential backoff:
1. Implement retry với increasing delays?
2. Max retry attempts?
3. Different strategies cho different error types?
4. Jitter để avoid thundering herd?
5. User feedback during retries?

### **Q15: Concurrent Requests**
Cần call 100 APIs nhưng limit 5 concurrent requests:
1. Implement concurrency control?
2. Queue system cho requests?
3. Promise pool pattern?
4. Handle partial failures?
5. Progress tracking?

### **Q16: Promise.all vs Promise.allSettled**
Khi nào dùng Promise.all vs Promise.allSettled vs Promise.race?
1. Difference về error handling?
2. Use cases cho từng loại?
3. Performance implications?
4. Implement custom Promise combinator?
5. Handle mixed success/failure results?

### **Q17: Async Error Handling**
Catch errors từ multiple async operations:
1. try-catch trong async functions?
2. Error boundaries cho async errors?
3. Global error handler?
4. Typed errors với TypeScript?
5. User-friendly error messages?

---

## **Phần 4: Closure & Scope Issues**

### **Q18: Loop Closure Bug**
for loop với setTimeout in sai values:
1. Tại sao in ra cùng value?
2. Fix với IIFE?
3. Fix với let vs var?
4. Fix với forEach?
5. Understanding lexical scope?

### **Q19: Memory Leak from Closure**
Closure giữ reference → memory không được free:
1. Identify closure memory leaks?
2. WeakMap/WeakSet để avoid leaks?
3. Break circular references?
4. Profiling closures trong DevTools?
5. Best practices để avoid closure leaks?

### **Q20: Private Variables**
Implement private properties không dùng class:
1. Closure-based private variables?
2. WeakMap for private state?
3. Symbols for pseudo-private?
4. Performance của different approaches?
5. TypeScript private vs runtime private?

### **Q21: Module Pattern**
Tạo singleton pattern với closure:
1. Module pattern implementation?
2. Revealing module pattern?
3. Namespace collision prevention?
4. Initialization timing?
5. ES modules vs closure modules?

### **Q22: Event Listener Leak**
addEventListener không cleanup → memory leak:
1. Identify event listener leaks?
2. removeEventListener best practices?
3. useEffect cleanup function?
4. Passive listeners for performance?
5. Event delegation để reduce listeners?

---

## **Phần 5: Event Loop & Timing Issues**

### **Q23: setTimeout 0**
setTimeout(fn, 0) hoạt động thế nào?
1. Tại sao không chạy immediately?
2. Use cases cho setTimeout 0?
3. Defer execution để unblock UI?
4. Difference với queueMicrotask()?
5. Event loop mechanics?

### **Q24: Microtask vs Macrotask**
Promise vs setTimeout execution order:
1. Microtask queue vs macrotask queue?
2. Priority của different task types?
3. Predict execution order của mixed tasks?
4. requestAnimationFrame timing?
5. Process.nextTick trong Node.js?

### **Q25: requestAnimationFrame**
RAF khác setTimeout thế nào?
1. RAF cho smooth animations?
2. 60fps target?
3. Cancel RAF khi component unmounts?
4. RAF vs CSS animations?
5. Performance monitoring với RAF?

### **Q26: Debounce vs Throttle**
Implement debounce/throttle functions:
1. Difference giữa debounce và throttle?
2. Leading vs trailing execution?
3. Use cases (search, scroll, resize)?
4. Cancel debounced/throttled functions?
5. React hooks cho debounce/throttle?

### **Q27: Long Task Blocking**
Long-running task block UI:
1. Break into smaller chunks?
2. Web Workers cho heavy computation?
3. requestIdleCallback usage?
4. Time slicing techniques?
5. Measure long tasks trong Performance API?

### **Q28: Event Loop Starvation**
Too many microtasks block macrotasks:
1. Identify event loop starvation?
2. Balance microtasks và macrotasks?
3. Yield to main thread?
4. Scheduler API (React)?
5. Performance implications?

---

## **Phần 6: this Binding Issues**

### **Q29: Lost this Context**
Method passed vào callback lose this:
1. Bind this trong constructor?
2. Arrow functions preserve this?
3. .bind() vs arrow function performance?
4. Class properties with arrow functions?
5. Explicit this parameter trong TypeScript?

### **Q30: Arrow Function this**
Arrow functions trong class methods:
1. Lexical this binding?
2. Memory implications (new function mỗi instance)?
3. Khi nào nên dùng arrow vs regular?
4. Inheritance issues với arrow functions?
5. Testing arrow function methods?

### **Q31: Event Handler this**
addEventListener(this.handleClick) → this undefined:
1. Tại sao lose this context?
2. Solutions: bind, arrow, proxy?
3. React event handlers best practices?
4. removeEventListener với bound functions?
5. Performance của different binding methods?

### **Q32: call vs apply vs bind**
Khi nào dùng call, apply, bind?
1. Differences và use cases?
2. Performance comparison?
3. Partial application với bind?
4. apply với arguments array?
5. Modern alternatives (spread operator)?

### **Q33: Constructor this**
Quên `new` khi call constructor:
1. this trỏ vào đâu?
2. Strict mode differences?
3. Detect và handle missing new?
4. Class vs constructor function?
5. Factory pattern alternative?

---

## **Phần 7: Type Coercion & Comparison Issues**

### **Q34: Falsy Value Bugs**
0, '', false, null, undefined treated như nhau:
1. Distinguish giữa falsy values?
2. ?? operator vs || operator?
3. Explicit checks (=== null) vs implicit?
4. Form validation với falsy values?
5. Default values handling?

### **Q35: Loose vs Strict Equality**
Khi nào == safe vs dangerous?
1. Type coercion rules?
2. Common gotchas với ==?
3. null == undefined use case?
4. ESLint rules cho equality?
5. Performance == vs ===?

### **Q36: NaN Comparison**
NaN === NaN → false, làm sao check NaN?
1. Number.isNaN() vs isNaN()?
2. Object.is(NaN, NaN)?
3. NaN propagation trong calculations?
4. Avoid NaN trong code?
5. TypeScript types để prevent NaN?

### **Q37: Array Comparison**
[1,2] === [1,2] → false, compare arrays đúng:
1. Shallow comparison strategies?
2. Deep comparison libraries?
3. JSON.stringify limitations?
4. Reference equality vs value equality?
5. Immutability để simplify comparison?

### **Q38: Object Key Coercion**
Object keys luôn coerced sang string:
1. Numeric keys behavior?
2. Symbol keys?
3. Map vs Object for non-string keys?
4. WeakMap key requirements?
5. Performance implications?

### **Q39: Implicit Conversion**
"5" - 2 = 3 nhưng "5" + 2 = "52":
1. Operator precedence và coercion rules?
2. Unary + để convert string→number?
3. Template literals vs concatenation?
4. Avoid implicit conversions?
5. TypeScript strict checks?

---

## **Phần 8: DOM & Event Issues**

### **Q40: Event Delegation**
1000 buttons → event delegation strategy:
1. Implement event delegation?
2. e.target vs e.currentTarget?
3. Closest() method usage?
4. Memory benefits?
5. Trade-offs (event specificity)?

### **Q41: Event Propagation**
stopPropagation vs preventDefault:
1. Bubbling vs capturing phases?
2. When to stop propagation?
3. preventDefault for default actions?
4. stopImmediatePropagation?
5. React synthetic events?

### **Q42: Memory Leak from DOM**
Remove DOM element nhưng JS giữ reference:
1. Detached nodes detection?
2. Clear references trước remove?
3. MutationObserver to track removals?
4. WeakMap for DOM associations?
5. Framework cleanup (React, Vue)?

### **Q43: Reflow/Repaint**
Multiple DOM updates → layout thrashing:
1. Batch DOM reads/writes?
2. requestAnimationFrame for updates?
3. DocumentFragment for multiple appends?
4. CSS containment?
5. Virtual scrolling to reduce DOM size?

### **Q44: Virtual DOM**
Virtual DOM solve vấn đề gì?
1. Reconciliation algorithm?
2. Diffing strategy?
3. Khi nào Virtual DOM slower than direct DOM?
4. Keys trong lists?
5. Svelte/SolidJS approaches (no Virtual DOM)?

---

## **Phần 9: React-Specific Issues**

### **Q45: useEffect Dependencies**
Dependency array sai → infinite loop:
1. Identify missing dependencies?
2. ESLint exhaustive-deps rule?
3. Fix với useCallback/useMemo?
4. Khi nào ignore lint warnings?
5. useEffect vs useLayoutEffect?

### **Q46: Stale Closure**
useState trong callback → old value:
1. Tại sao closure capture old state?
2. Functional updates: setState(prev => ...)?
3. useRef to store latest value?
4. useEvent (React 18+)?
5. Understanding closure scope?

### **Q47: Key Prop**
List không có key hoặc key = index:
1. Consequences (wrong updates, lost state)?
2. Stable unique keys?
3. Index as key khi nào OK?
4. Key changes → remount component?
5. Debugging key issues?

### **Q48: Context Performance**
Context update → tất cả consumers re-render:
1. Split contexts để reduce re-renders?
2. useMemo trong Provider value?
3. Context selectors (use-context-selector)?
4. Jotai/Zustand alternatives?
5. When Context is overkill?

### **Q49: Prop Drilling**
Props pass qua 5+ levels:
1. Context to avoid drilling?
2. Component composition?
3. Render props?
4. State management libraries?
5. Trade-offs của different solutions?

### **Q50: React Reconciliation**
React decide re-render thế nào?
1. Reconciliation algorithm (Fiber)?
2. Pure components và memo?
3. shouldComponentUpdate?
4. React.memo comparison function?
5. Profiler to identify re-renders?

### **Q51: useMemo vs useCallback**
Khi nào dùng useMemo/useCallback?
1. Premature optimization?
2. Reference equality cho dependencies?
3. Expensive computations?
4. Profiling to verify benefit?
5. Cost của hooks themselves?

### **Q52: Custom Hooks**
Tạo reusable logic với custom hooks:
1. Rules of hooks?
2. Naming convention (use*)?
3. Return values (array vs object)?
4. Testing custom hooks?
5. Share state vs share logic?

---

## **Phần 10: Build & Bundle Issues**

### **Q53: Tree Shaking**
Tree shaking không remove unused code:
1. ES modules requirement?
2. Side effects trong package.json?
3. CommonJS vs ESM?
4. Verify tree shaking worked?
5. Lodash-es vs lodash?

### **Q54: Code Splitting**
Strategy cho code splitting:
1. Route-based splitting?
2. Component-based splitting?
3. Dynamic imports?
4. Suspense và lazy()?
5. Preload/prefetch hints?

### **Q55: Webpack vs Vite**
Build process differences:
1. Dev server speed?
2. HMR implementation?
3. Production build?
4. Plugin ecosystems?
5. Migration from Webpack→Vite?

### **Q56: Source Maps**
Production source maps trade-offs:
1. Security risks?
2. Debug production issues?
3. Source map types (inline, external)?
4. Sentry source map upload?
5. Disable in production?

### **Q57: Polyfill Strategy**
Browser support cũ cần polyfills:
1. Differential serving (modern vs legacy)?
2. Polyfill.io vs bundled polyfills?
3. Core-js configuration?
4. Browserslist target?
5. Bundle size impact?

---

## **Phần 11: Network & API Issues**

### **Q58: CORS Error**
API call bị block bởi CORS policy:
1. CORS là gì? Same-origin policy?
2. Backend config: Access-Control-Allow-Origin?
3. Preflight requests (OPTIONS)?
4. Credentials (cookies) trong CORS?
5. Proxy trong development?

### **Q59: Token Refresh**
Access token expire → refresh seamlessly:
1. Detect 401 errors?
2. Queue requests during refresh?
3. Axios interceptors?
4. Refresh token rotation?
5. Handle refresh failure (logout)?

### **Q60: Request Interceptor**
Add auth token vào all requests:
1. Axios request interceptors?
2. Fetch wrapper?
3. Update token dynamically?
4. Error interceptor?
5. TypeScript typing?

### **Q61: Optimistic Update**
Update UI trước API response:
1. Immediate feedback?
2. Rollback on error?
3. Conflict resolution?
4. React Query optimistic updates?
5. User experience considerations?

### **Q62: Caching Strategy**
Cache API responses effectively:
1. Browser cache (Cache-Control)?
2. Service Worker cache?
3. Application-level cache (React Query)?
4. Cache invalidation?
5. Stale-while-revalidate?

### **Q63: GraphQL vs REST**
Khi nào chọn GraphQL vs REST?
1. Over-fetching/under-fetching?
2. Query complexity?
3. Caching strategies?
4. Learning curve?
5. Real-world trade-offs?

---

## **Phần 12: State Management Issues**

### **Q64: Redux Boilerplate**
Giảm Redux boilerplate:
1. Redux Toolkit benefits?
2. createSlice vs manual reducers?
3. RTK Query vs Redux + API middleware?
4. Immer trong Redux Toolkit?
5. Migration strategy?

### **Q65: Global vs Local State**
State nên global hay local?
1. Lift state up vs keep local?
2. Server state vs client state?
3. React Query for server state?
4. Form state (local vs global)?
5. Over-engineering state management?

### **Q66: Derived State**
Compute từ existing state:
1. useMemo trong component?
2. Selector functions (Reselect)?
3. Avoid storing derived state?
4. Performance considerations?
5. Recomputation triggers?

### **Q67: State Normalization**
Flatten nested Redux state:
1. Normalizr library?
2. Entities vs UI state?
3. Selectors to denormalize?
4. Update efficiency?
5. Relationships handling?

### **Q68: Zustand vs Redux**
Compare state management solutions:
1. Bundle size?
2. DevTools support?
3. Middleware ecosystem?
4. Learning curve?
5. Use cases for each?

---

## **Phần 13: Security Issues**

### **Q69: XSS Attack**
Prevent cross-site scripting:
1. Sanitize user input?
2. DOMPurify library?
3. React auto-escaping?
4. dangerouslySetInnerHTML risks?
5. Content Security Policy?

### **Q70: CSRF Attack**
Cross-site request forgery prevention:
1. CSRF tokens?
2. SameSite cookies?
3. Double submit cookies?
4. Custom headers?
5. Backend validation?

### **Q71: Secure Token Storage**
JWT storage location:
1. localStorage vs sessionStorage vs cookies?
2. HttpOnly cookies?
3. Secure flag?
4. XSS vs CSRF trade-offs?
5. Token expiration handling?

### **Q72: Input Sanitization**
Validate và sanitize user input:
1. Client-side vs server-side validation?
2. Whitelist vs blacklist?
3. Libraries (validator.js, DOMPurify)?
4. SQL injection prevention?
5. File upload validation?

### **Q73: Content Security Policy**
CSP configuration:
1. CSP headers?
2. Nonce for inline scripts?
3. Report-only mode?
4. Third-party scripts?
5. Strict CSP?

---

## **Phần 14: Testing Issues**

### **Q74: Async Testing**
Test async code properly:
1. waitFor, findBy queries?
2. Act warnings?
3. Flush promises?
4. Test timeouts?
5. Mock timers?

### **Q75: Mock API Calls**
Mock fetch/axios:
1. Jest mock functions?
2. MSW (Mock Service Worker)?
3. Nock library?
4. Test different responses?
5. Verify request payloads?

### **Q76: Test React Hooks**
Test custom hooks:
1. @testing-library/react-hooks?
2. renderHook helper?
3. Act warning fixes?
4. Test async hooks?
5. Mock dependencies?

### **Q77: E2E vs Unit Tests**
Testing strategy:
1. Testing pyramid?
2. E2E tools (Playwright, Cypress)?
3. Coverage goals?
4. CI/CD integration?
5. Test maintenance cost?

### **Q78: Test Coverage**
100% coverage meaning:
1. Line vs branch coverage?
2. Meaningful tests vs coverage gaming?
3. Integration tests value?
4. Diminishing returns?
5. Coverage tools (Istanbul)?

---

## **Phần 15: TypeScript Issues**

### **Q79: Type vs Interface**
type vs interface choice:
1. Declaration merging?
2. Union types?
3. Performance differences?
4. Extensibility?
5. Team conventions?

### **Q80: Generic Constraints**
Constrain generic types:
1. extends keyword?
2. Multiple constraints?
3. Conditional types?
4. Infer keyword?
5. Practical examples?

### **Q81: Type Guards**
Narrow types safely:
1. typeof guards?
2. instanceof guards?
3. Custom type predicates?
4. Discriminated unions?
5. Assertion functions?

### **Q82: Utility Types**
Built-in utility types:
1. Pick, Omit, Partial, Required?
2. Record, Readonly?
3. ReturnType, Parameters?
4. Custom utility types?
5. Mapped types?

### **Q83: any vs unknown**
Type-safe unknown:
1. unknown forces checks?
2. Migration from any?
3. Type assertions?
4. never type?
5. Strictness trade-offs?

---

## **Phần 16: SSR & Next.js Issues**

### **Q84: SSR vs SSG**
getServerSideProps vs getStaticProps:
1. When to use which?
2. Incremental Static Regeneration?
3. Performance implications?
4. SEO considerations?
5. Hybrid approaches?

### **Q85: Hydration Mismatch**
Server HTML ≠ client HTML:
1. Causes (random IDs, Date.now())?
2. Suppress warnings?
3. Client-only components?
4. useEffect to defer rendering?
5. Debug mismatches?

### **Q86: API Routes**
Next.js API routes vs separate backend:
1. When to use API routes?
2. Serverless limitations?
3. Authentication trong API routes?
4. Database connections?
5. TypeScript sharing?

### **Q87: ISR**
Incremental Static Regeneration:
1. Revalidate strategies?
2. On-demand revalidation?
3. Fallback modes?
4. CDN caching?
5. Cache invalidation?

### **Q88: SSR Performance**
Optimize SSR apps:
1. Reduce TTFB?
2. Stream rendering?
3. Caching strategies?
4. Edge rendering?
5. Monitor SSR metrics?

---

## **Phần 17: Microfrontend Issues**

### **Q89: Module Federation**
Webpack Module Federation setup:
1. Shared dependencies config?
2. Version mismatches?
3. Runtime vs build time sharing?
4. Singleton enforcement?
5. Debugging federation issues?

### **Q90: Shared Dependencies**
Share React giữa microfrontends:
1. Version compatibility?
2. Singleton React instance?
3. Peer dependencies?
4. Bundle duplication?
5. Dynamic loading?

### **Q91: Microfrontend Communication**
Communication patterns:
1. Custom events?
2. Shared state (Redux)?
3. Props drilling?
4. Query params?
5. Loose coupling?

### **Q92: Microfrontend Deployment**
Independent deployment:
1. Versioning strategy?
2. Rollback plan?
3. Canary releases?
4. Feature flags?
5. Monitoring per microfrontend?

### **Q93: Styling Conflicts**
CSS isolation:
1. CSS Modules?
2. CSS-in-JS?
3. Shadow DOM?
4. BEM naming?
5. Runtime styles vs build?

---

## **Phần 18: Advanced Debugging**

### **Q94: DevTools Profiling**
Chrome DevTools advanced usage:
1. Performance tab analysis?
2. Memory heap snapshots?
3. Network throttling?
4. Coverage tab?
5. Layers panel?

### **Q95: Network Waterfall**
Optimize resource loading:
1. Waterfall chart reading?
2. Blocking resources?
3. Preload/prefetch?
4. Resource hints?
5. Critical path optimization?

### **Q96: Lighthouse Audit**
Improve Lighthouse scores:
1. Performance metrics (LCP, FID, CLS)?
2. Accessibility issues?
3. Best practices?
4. SEO optimization?
5. PWA checklist?

### **Q97: Error Tracking**
Production error monitoring:
1. Sentry setup?
2. Error boundaries?
3. Source maps upload?
4. User context?
5. Alert configurations?

### **Q98: Production Debugging**
Debug production-only issues:
1. Source maps usage?
2. Logging strategies?
3. Feature flags for testing?
4. Session replay tools?
5. Reproduce locally?

---

## **Phần 19: Real-World Scenarios**

### **Q99: Infinite Scroll**
Implement performant infinite scroll:
1. Intersection Observer?
2. Virtualization?
3. Fetch next page trigger?
4. Loading states?
5. End of list handling?

### **Q100: File Upload**
Large file upload with features:
1. Chunk upload?
2. Progress tracking?
3. Pause/resume?
4. Retry failed chunks?
5. Drag-and-drop?

### **Q101: Real-time Collaboration**
Google Docs-like collaboration:
1. WebSocket vs polling?
2. Operational Transformation?
3. CRDTs?
4. Conflict resolution?
5. Presence indicators?

### **Q102: Offline Mode**
PWA offline functionality:
1. Service Worker caching?
2. IndexedDB for data?
3. Background sync?
4. Conflict resolution?
5. Online/offline detection?

### **Q103: Localization**
Multi-language support:
1. i18next setup?
2. Language detection?
3. Dynamic imports for translations?
4. RTL support?
5. Date/number formatting?

### **Q104: AB Testing**
Frontend A/B testing:
1. Feature flags?
2. User bucketing?
3. Analytics integration?
4. Performance impact?
5. Statistical significance?

### **Q105: Analytics**
User behavior tracking:
1. Events vs page views?
2. Custom dimensions?
3. GDPR compliance?
4. Performance impact?
5. Google Analytics vs alternatives?

---

## **Phần 20: Architecture & Design Patterns**

### **Q106: Component Architecture**
Organize components:
1. Atomic design?
2. Feature-based structure?
3. Presentational vs container?
4. Compound components?
5. Composition patterns?

### **Q107: Folder Structure**
Large codebase organization:
1. Feature folders?
2. Monorepo vs multi-repo?
3. Shared code location?
4. Import path aliases?
5. Scalability considerations?

### **Q108: Design Patterns**
Patterns trong React:
1. Higher-Order Components?
2. Render Props?
3. Factory pattern?
4. Observer/PubSub?
5. Singleton (với caveats)?

### **Q109: DDD Frontend**
Domain-Driven Design:
1. Frontend domains?
2. Bounded contexts?
3. Value objects?
4. Repository pattern?
5. Overkill or valuable?

### **Q110: Component Granularity**
Component size strategy:
1. Single responsibility?
2. Reusability vs specificity?
3. Performance (memo boundaries)?
4. Testing ease?
5. Refactoring indicators?

---

**📌 Lưu ý:**
- Đây là bộ câu hỏi tập trung vào **kinh nghiệm thực tế** và **deep understanding**
- Mỗi câu hỏi đi sâu vào vấn đề cụ thể, yêu cầu hiểu rõ core concepts
- Câu trả lời nên bao gồm: **tại sao**, **khi nào**, **trade-offs**, **best practices**
- Phù hợp cho: **Senior/Lead Frontend Engineers**, **Technical Interviews**, **Self-learning**

---

## **🚀 ADVANCED SYSTEM SCENARIOS**

### **Q111: Distributed Rate Limiting**
Multi-server deployment, prevent abuse với rate limiting:
1. Centralized vs distributed rate limiting?
2. Token bucket vs leaky bucket algorithm?
3. Redis-based rate limiting?
4. Sliding window log?
5. User identification (IP, token, fingerprint)?
6. Graceful degradation khi rate limiter down?
7. Rate limit headers (X-RateLimit-*)?
8. DDoS protection layers?

### **Q112: Global State Synchronization**
Multiple browser tabs/windows cần sync state:
1. BroadcastChannel API?
2. SharedWorker for state?
3. LocalStorage events?
4. Service Worker as proxy?
5. Conflict resolution giữa tabs?
6. Leader election (một tab làm master)?
7. State reconciliation?
8. Performance impact?

### **Q113: Progressive Enhancement**
Support từ IE11 → latest Chrome:
1. Feature detection strategy?
2. Polyfill loading strategy?
3. Differential serving (modern vs legacy bundles)?
4. Core functionality vs enhancements?
5. Graceful degradation examples?
6. Testing matrix?
7. Bundle size trade-offs?
8. Maintenance cost?

### **Q114: Serverless Frontend**
JAMstack với edge functions:
1. Static site generation vs SSR?
2. Edge compute (Cloudflare Workers, Deno Deploy)?
3. API routes tại edge?
4. Cold start optimization?
5. State management without server?
6. Database access from edge?
7. Cost optimization?
8. Vendor lock-in mitigation?

### **Q115: Web Assembly Integration**
Heavy computation bottleneck, migrate sang WASM:
1. Rust/C++ vs AssemblyScript?
2. JS ↔ WASM communication overhead?
3. Memory management (linear memory)?
4. Threading (SharedArrayBuffer)?
5. Bundle size impact?
6. Browser compatibility?
7. Debugging WASM?
8. When NOT to use WASM?

---

## **🛡️ ADVANCED SECURITY SCENARIOS**

### **Q116: Supply Chain Attack**
npm package compromised, inject malicious code:
1. Dependency integrity verification?
2. Subresource Integrity (SRI)?
3. Lock file security?
4. Private registry?
5. Automated vulnerability scanning?
6. Code review for dependencies?
7. Minimal dependencies principle?
8. Incident response plan?

### **Q117: OAuth/OIDC Implementation**
Secure authentication flow (Google, GitHub, Auth0):
1. Authorization Code Flow with PKCE?
2. State parameter (CSRF protection)?
3. Nonce for replay attack prevention?
4. Token validation (signature, expiry, audience)?
5. Refresh token rotation?
6. Single Sign-On (SSO) across subdomains?
7. Single Logout (SLO)?
8. Session management?

### **Q118: API Security**
Expose public APIs, prevent abuse:
1. API key management?
2. OAuth 2.0 vs API keys?
3. Rate limiting per API key?
4. Scope-based permissions?
5. Request signing (HMAC)?
6. IP whitelisting?
7. API versioning strategy?
8. Monitoring & alerting?

### **Q119: Content Security Policy (CSP)**
Strict CSP without breaking functionality:
1. CSP directives (script-src, style-src, etc.)?
2. Nonce-based CSP?
3. Hash-based CSP?
4. Report-only mode testing?
5. Third-party scripts handling?
6. Inline event handlers migration?
7. CSP violation reporting?
8. Gradual rollout?

### **Q120: Secure File Upload**
File upload vulnerable to attacks:
1. File type validation (MIME vs extension)?
2. File size limits?
3. Malware scanning?
4. Separate storage domain?
5. Signed URLs for access?
6. Image processing (remove EXIF)?
7. Prevent path traversal?
8. Content-Disposition header?

---

## **📊 OBSERVABILITY & MONITORING**

### **Q121: Frontend Observability Stack**
Build comprehensive monitoring cho production:
1. Metrics (RED/USE method)?
2. Logs aggregation (structured logging)?
3. Traces (distributed tracing)?
4. Real User Monitoring (RUM)?
5. Synthetic monitoring?
6. Alerts & on-call rotation?
7. Dashboards for different audiences?
8. Cost optimization?

### **Q122: Custom Metrics**
Track business-specific metrics:
1. Custom events tracking?
2. User journey funnels?
3. Feature adoption metrics?
4. Error categorization?
5. Performance budgets enforcement?
6. A/B test metrics?
7. Cardinality explosion prevention?
8. Privacy compliance (GDPR)?

### **Q123: Correlation & Causation**
Metric spike, find root cause:
1. Correlation analysis (multiple metrics)?
2. Change tracking (deployments, config)?
3. Hypothesis testing?
4. Flame graphs analysis?
5. User cohort analysis?
6. External factors (marketing campaigns)?
7. Seasonality detection?
8. Automated anomaly detection?

### **Q124: Performance Monitoring**
Core Web Vitals optimization:
1. LCP (Largest Contentful Paint) optimization?
2. FID (First Input Delay) optimization?
3. CLS (Cumulative Layout Shift) fixes?
4. INP (Interaction to Next Paint)?
5. TTFB (Time to First Byte)?
6. Real user percentiles (p50, p95, p99)?
7. Lab data vs field data?
8. Performance regression detection?

### **Q125: Error Tracking Strategy**
Comprehensive error handling:
1. Error boundaries placement?
2. Global error handlers?
3. Unhandled promise rejection?
4. Source maps for production?
5. Error grouping & deduplication?
6. User context capture?
7. PII scrubbing?
8. Error sampling strategy?

---

## **🎯 ADVANCED REACT PATTERNS**

### **Q126: Compound Components**
Complex component with sub-components:
1. Context for implicit state sharing?
2. Flexible composition?
3. Prop drilling elimination?
4. Type safety với TypeScript?
5. Render props alternative?
6. Real-world examples (Tabs, Accordion)?
7. Performance considerations?
8. Testing strategy?

### **Q127: State Machines**
Complex UI state (loading, error, success, ...):
1. XState integration?
2. Finite state machine benefits?
3. State transitions visualization?
4. Side effects handling?
5. Testing state machines?
6. Reducer pattern vs state machine?
7. TypeScript state typing?
8. When overkill?

### **Q128: Render Props vs Hooks**
When to use each pattern:
1. Render props use cases?
2. Custom hooks benefits?
3. Performance comparison?
4. Composition patterns?
5. TypeScript ergonomics?
6. Testing differences?
7. Migration path?
8. Combining both patterns?

### **Q129: React Server Components**
RSC architecture & benefits:
1. Server vs Client components?
2. Data fetching in RSC?
3. Bundle size reduction?
4. Streaming SSR?
5. Hydration strategy?
6. Limitations & trade-offs?
7. Next.js App Router?
8. Migration from traditional SSR?

### **Q130: Concurrent React**
Leverage React 18 concurrency:
1. useTransition for non-urgent updates?
2. useDeferredValue for derived state?
3. Suspense for data fetching?
4. startTransition vs setTimeout?
5. Concurrent rendering benefits?
6. Race condition prevention?
7. User experience improvements?
8. Backward compatibility?

---

## **🔧 BUILD & DEPLOYMENT**

### **Q131: Zero-Downtime Deployment**
Deploy không downtime cho users:
1. Blue-green deployment?
2. Canary releases?
3. Rolling updates?
4. Feature flags?
5. Database migrations?
6. Cache invalidation?
7. Rollback strategy?
8. Health checks?

### **Q132: CI/CD Pipeline**
Comprehensive pipeline cho frontend:
1. Linting & formatting?
2. Type checking (TypeScript)?
3. Unit tests (Jest)?
4. Integration tests?
5. E2E tests (Playwright)?
6. Visual regression (Percy, Chromatic)?
7. Performance budgets?
8. Security scanning?

### **Q133: Feature Flags**
Decouple deployment from release:
1. Feature flag system (LaunchDarkly, Unleash)?
2. Kill switches?
3. Gradual rollout (percentage-based)?
4. User targeting (segments)?
5. A/B testing integration?
6. Flag lifecycle management?
7. Technical debt từ flags?
8. Testing với flags?

### **Q134: Asset Optimization**
Comprehensive asset strategy:
1. Image optimization (responsive, lazy, WebP/AVIF)?
2. Font optimization (subset, swap, preload)?
3. Video optimization (adaptive bitrate)?
4. Icon strategy (sprite, inline SVG, icon fonts)?
5. Critical CSS extraction?
6. Unused CSS removal (PurgeCSS)?
7. Compression (Brotli, Gzip)?
8. CDN cache headers?

### **Q135: Monorepo Strategy**
Manage multiple apps trong một repo:
1. Nx vs Turborepo vs Lerna?
2. Workspace organization?
3. Shared library versioning?
4. Build caching?
5. Dependency management?
6. CI/CD optimization (affected commands)?
7. Code ownership (CODEOWNERS)?
8. Scaling challenges?

---

## **🌐 INTERNATIONALIZATION & ACCESSIBILITY**

### **Q136: i18n at Scale**
Support 20+ languages:
1. Translation management (Crowdin, Phrase)?
2. Locale detection & switching?
3. Number/date/currency formatting?
4. Pluralization rules?
5. RTL (right-to-left) support?
6. Dynamic imports for translations?
7. Missing translation handling?
8. Translation testing?

### **Q137: Accessibility (a11y)**
WCAG 2.1 AA compliance:
1. Keyboard navigation?
2. Screen reader support (ARIA)?
3. Color contrast?
4. Focus management?
5. Semantic HTML?
6. Skip links?
7. Live regions for dynamic content?
8. Automated testing (axe-core, pa11y)?

### **Q138: Form Accessibility**
Complex forms accessible:
1. Label association?
2. Error messaging (ARIA live)?
3. Validation timing?
4. Required fields indication?
5. Fieldset & legend?
6. Autocomplete attributes?
7. Touch target sizing?
8. Testing với screen readers?

### **Q139: Mobile Accessibility**
Touch & gesture accessibility:
1. Touch target sizes (44x44px)?
2. Gesture alternatives?
3. Orientation support?
4. Zoom support?
5. Motion sensitivity (prefers-reduced-motion)?
6. Voice control?
7. One-handed usage?
8. Testing on actual devices?

### **Q140: Performance vs Accessibility**
Balance performance và a11y:
1. Lazy loading vs screen readers?
2. Virtual scrolling vs keyboard navigation?
3. Skeleton screens vs screen reader announcements?
4. Image optimization vs alt text?
5. Animations vs vestibular disorders?
6. Infinite scroll vs pagination?
7. Loading states accessibility?
8. Testing strategy?

---

## **💡 ARCHITECTURAL DECISIONS**

### **Q141: GraphQL vs REST**
Choose API architecture:
1. Over-fetching/under-fetching?
2. Schema evolution?
3. Caching strategies?
4. Real-time subscriptions?
5. File uploads?
6. Error handling?
7. Tooling ecosystem?
8. Team expertise?

### **Q142: SSR vs SSG vs CSR**
Rendering strategy decision:
1. SEO requirements?
2. Data freshness needs?
3. Personalization?
4. Time to First Byte (TTFB)?
5. Server costs?
6. Complexity?
7. Hybrid approaches?
8. ISR (Incremental Static Regeneration)?

### **Q143: SQL vs NoSQL**
Database choice for frontend:
1. Data structure (relational vs document)?
2. Query patterns?
3. Scalability needs?
4. Consistency requirements?
5. Developer experience?
6. Ecosystem maturity?
7. Cost?
8. Hybrid approaches (Postgres JSONB)?

### **Q144: TypeScript Adoption**
Migrate JS codebase sang TS:
1. Migration strategy (gradual vs big bang)?
2. strictNullChecks configuration?
3. any vs unknown?
4. Type definition files (.d.ts)?
5. Third-party library types?
6. Build process changes?
7. Team training?
8. ROI measurement?

### **Q145: Micro-Frontends Tradeoffs**
Decision to adopt microfrontends:
1. Team autonomy vs coordination?
2. Deployment independence vs integration testing?
3. Technology diversity vs consistency?
4. Shared dependencies vs bundle size?
5. Runtime integration vs build-time?
6. Organizational alignment?
7. When NOT to use microfrontends?
8. Migration path?

---

**🎓 Tổng Kết:**

Bộ câu hỏi này bao gồm **145 câu hỏi** chia thành:

**🚨 Critical Issues (35 câu)**
- Production incidents & emergency response
- Security vulnerabilities & attacks
- Performance bottlenecks at scale
- System failures & debugging

**💼 Business-Critical (20 câu)**
- High-stakes scenarios (flash sales, payments, trading)
- Compliance & regulatory
- Multi-tenant architecture
- SLA/SLO management

**🏗️ Architecture & Design (30 câu)**
- Microfrontends & distributed systems
- State management at scale
- Rendering strategies
- Technology choices

**🔧 Engineering Excellence (30 câu)**
- Observability & monitoring
- CI/CD & deployment
- Testing strategies
- Build optimization

**🌐 User Experience (30 câu)**
- Accessibility (WCAG compliance)
- Internationalization
- Performance optimization
- Progressive enhancement

**Yêu cầu kỹ năng:**
- ✅ System design & architecture
- ✅ Security-first mindset
- ✅ Performance engineering
- ✅ Incident response
- ✅ Business acumen
- ✅ Trade-off analysis
- ✅ Team leadership
- ✅ Production operations

**Target level:** Senior/Staff/Principal Engineers, Tech Leads, Engineering Managers

---

## **🎯 ADDITIONAL SENIOR-LEVEL SCENARIOS**

### **Q146: Empty State & Loading State Design**
User experience với empty/loading states:
1. Design empty state cho first-time users vs returning users?
2. Skeleton screens vs spinners vs progress bars?
3. Stale data display during refresh?
4. Error state vs empty state distinction?
5. Actionable empty states (CTA, suggestions)?
6. Loading state cho slow networks?
7. Perceived performance tricks?
8. A11y cho loading states?

### **Q147: Form UX & Validation**
Complex form với validation tốt:
1. Real-time validation vs on-submit?
2. Field-level vs form-level errors?
3. Inline validation timing (onBlur, onChange)?
4. Multi-step form state persistence?
5. Autosave vs manual save?
6. Dirty state tracking & unsaved changes warning?
7. Accessibility (ARIA live regions, focus management)?
8. Form recovery sau crash/refresh?

### **Q148: Progressive Image Loading**
Optimize image loading experience:
1. LQIP (Low Quality Image Placeholder)?
2. BlurHash vs ThumbHash?
3. Lazy loading strategies (Intersection Observer)?
4. Responsive images (srcset, picture)?
5. WebP/AVIF fallbacks?
6. Loading priority (above-fold vs below)?
7. Skeleton screens cho images?
8. Network-aware loading (Save-Data header)?

### **Q149: Cross-Browser Font Rendering**
Font consistency across platforms:
1. Font loading strategies (FOUT, FOIT, FOFT)?
2. font-display: swap vs optional vs block?
3. Variable fonts benefits?
4. Font subsetting?
5. System font stack fallbacks?
6. macOS vs Windows vs Linux rendering differences?
7. Web font optimization (woff2, preload)?
8. Icon fonts vs SVG icons?

### **Q150: Navigation UX Issues**
User không hiểu cách navigate:
1. Breadcrumbs implementation?
2. Sticky navigation vs scroll-away?
3. Mobile menu patterns (hamburger, tab bar)?
4. Deep linking preservation?
5. Back button behavior trong SPA?
6. Skip navigation links (A11y)?
7. Search integration trong navigation?
8. Multi-level navigation (mega menu)?

### **Q151: Data Visualization Performance**
10,000+ data points rendering:
1. Canvas vs SVG performance?
2. WebGL cho large datasets?
3. Data decimation strategies?
4. Viewport-based rendering?
5. Real-time chart updates throttling?
6. Responsive charts (mobile vs desktop)?
7. Chart accessibility (ARIA, keyboard nav)?
8. Export functionality (PNG, CSV)?

### **Q152: File Upload UX**
Large file upload với good UX:
1. Drag-and-drop implementation?
2. Chunked upload (resume capability)?
3. Progress tracking (bytes, percentage, ETA)?
4. Multiple file selection?
5. File type/size validation (client + server)?
6. Preview before upload?
7. Cancel/pause/resume upload?
8. Background upload (Service Worker)?

### **Q153: Search Performance**
Search 1M+ records efficiently:
1. Client-side vs server-side search?
2. Debounce input (optimal timing)?
3. Search-as-you-type implementation?
4. Fuzzy search algorithms?
5. Search result highlighting?
6. Autocomplete suggestions?
7. Recent searches persistence?
8. Search analytics tracking?

### **Q154: Notification System**
Comprehensive notification strategy:
1. Toast vs banner vs modal?
2. Notification persistence (session vs permanent)?
3. Action buttons trong notifications?
4. Undo functionality?
5. Notification queue (max concurrent)?
6. Auto-dismiss timing?
7. Notification center (history)?
8. Push notifications (Web Push API)?

### **Q155: Offline-First Strategy**
PWA với offline capabilities:
1. Service Worker caching strategies?
2. Background sync implementation?
3. IndexedDB for offline data?
4. Conflict resolution (online vs offline changes)?
5. Offline indicator UI?
6. Queue failed requests?
7. Sync progress feedback?
8. Testing offline scenarios?

### **Q156: Multi-Tenant White-Label**
SaaS với custom branding per tenant:
1. Dynamic theme loading?
2. CSS variables vs runtime styling?
3. Asset management per tenant?
4. Domain-based tenant detection?
5. Build-time vs runtime theming?
6. Branding cache strategies?
7. Theme preview functionality?
8. Tenant isolation enforcement?

### **Q157: Global Application (i18n)**
Support 20+ languages & regions:
1. Translation file management?
2. RTL (right-to-left) support?
3. Pluralization handling?
4. Date/time/number formatting?
5. Currency formatting?
6. Locale detection (browser, IP, user preference)?
7. Translation loading strategy (bundle vs lazy)?
8. Missing translation fallbacks?

### **Q158: Analytics & User Behavior**
Track user behavior ethically:
1. Event tracking strategy (page views, clicks, custom)?
2. User journey funnels?
3. Heatmaps & session replay?
4. GDPR/CCPA compliance (consent management)?
5. PII scrubbing?
6. Analytics sampling (reduce overhead)?
7. Custom dimensions & metrics?
8. A/B test integration?

### **Q159: Third-Party Script Management**
External scripts không làm chậm app:
1. Async vs defer script loading?
2. Script loading priority?
3. Lazy load third-party widgets?
4. Iframe sandboxing?
5. CSP (Content Security Policy) headers?
6. Performance impact measurement?
7. Fallback khi script blocked?
8. GDPR consent before loading scripts?

### **Q160: Payment Integration**
Secure payment flow:
1. PCI DSS compliance?
2. Tokenization (không lưu card data)?
3. 3D Secure authentication?
4. Payment retry logic?
5. Webhook handling (async confirmation)?
6. Idempotency keys?
7. Refund workflow?
8. Multi-currency support?

### **Q161: OAuth Multi-Provider**
Social login với nhiều providers:
1. OAuth 2.0 flow (authorization code + PKCE)?
2. State parameter (CSRF protection)?
3. Account linking (merge social accounts)?
4. Fallback khi provider down?
5. Token storage security?
6. Refresh token handling?
7. Revoking access?
8. Provider-specific quirks (Google, Facebook, GitHub)?

### **Q162: Rate Limit Handling**
API trả 429 Too Many Requests:
1. Exponential backoff implementation?
2. Retry-After header parsing?
3. Queue requests locally?
4. User feedback during rate limit?
5. Circuit breaker pattern?
6. Request batching?
7. Cache để reduce API calls?
8. Rate limit per user vs global?

### **Q163: API Versioning Strategy**
Support API v1 & v2 simultaneously:
1. Versioning scheme (URL, header, query param)?
2. Backward compatibility layer?
3. Deprecation warnings?
4. Feature detection vs version detection?
5. Migration path for users?
6. Dual-write pattern?
7. Testing multiple versions?
8. Phased rollout strategy?

### **Q164: Legacy Migration (jQuery → React)**
Incremental migration strategy:
1. Strangler pattern implementation?
2. Dual framework setup (React + jQuery)?
3. Shared state management?
4. Component boundary definition?
5. Event communication giữa jQuery ↔ React?
6. Testing hybrid setup?
7. Performance during migration?
8. Team training & onboarding?

### **Q165: Database Corruption Recovery**
Data integrity issues trong production:
1. Backup & restore strategy?
2. Point-in-time recovery?
3. Data validation scripts?
4. Rollback transactions?
5. User communication plan?
6. RCA (Root Cause Analysis)?
7. Preventing future corruption?
8. Monitoring data integrity?

### **Q166: CDN Failover**
CDN provider down, maintain service:
1. Multi-CDN strategy?
2. Automatic failover DNS?
3. Origin server fallback?
4. Health check monitoring?
5. Cache consistency across CDNs?
6. Geographic routing?
7. Cost optimization?
8. Testing failover scenarios?

### **Q167: Security Incident Response**
Website bị hack, immediate actions:
1. Incident detection (monitoring, alerts)?
2. Immediate mitigation (take offline, block IPs)?
3. Forensics & log analysis?
4. User notification requirements?
5. Patch deployment?
6. Password reset enforcement?
7. Security audit post-incident?
8. Legal & compliance obligations?

### **Q168: Data Leak Prevention**
User data accidentally exposed:
1. Immediate response (revoke access, notify)?
2. Scope assessment (how many users)?
3. Regulatory reporting (GDPR 72-hour rule)?
4. Credit monitoring services?
5. Root cause fixing?
6. Security training for team?
7. Third-party security audit?
8. PR & communication strategy?

### **Q169: Performance Budget Enforcement**
Maintain performance standards:
1. Define budgets (bundle size, LCP, CLS)?
2. CI/CD integration (fail build on violation)?
3. Lighthouse CI setup?
4. Real user monitoring (RUM) thresholds?
5. Budget trade-off decisions?
6. Alert stakeholders on regression?
7. Performance dashboard?
8. Regular audit cadence?

### **Q170: Incident Post-Mortem**
After production incident:
1. Blameless culture enforcement?
2. Timeline reconstruction?
3. Root cause identification (5 Whys)?
4. Action items tracking?
5. Documentation sharing?
6. Follow-up verification?
7. Learning distribution?
8. Recurring incident pattern detection?

### **Q171: Technical Debt Management**
Balance features vs refactoring:
1. Debt inventory & prioritization?
2. Cost/benefit analysis?
3. Time allocation (20% refactoring)?
4. Convincing stakeholders?
5. Incremental refactoring strategy?
6. Measuring debt reduction?
7. Preventing new debt?
8. Boy Scout Rule enforcement?

### **Q172: Team Code Review**
Effective code review process:
1. Review checklist (functionality, tests, perf, security)?
2. Automated checks (linting, formatting)?
3. Review turnaround time SLA?
4. Constructive feedback culture?
5. Knowledge sharing opportunities?
6. Handling disagreements?
7. Senior vs junior review approach?
8. Review tools & workflows?

### **Q173: Onboarding New Developers**
Fast & effective onboarding:
1. Documentation quality (README, ADRs)?
2. Dev environment setup automation?
3. Mentorship pairing?
4. Starter tasks selection?
5. Team rituals introduction?
6. Codebase tour & architecture overview?
7. Feedback loops (1-week, 1-month)?
8. Success metrics?

### **Q174: Stakeholder Communication**
Explain technical decisions to non-technical:
1. Business value translation?
2. Visual aids (diagrams, demos)?
3. Risk/benefit framing?
4. Time/cost estimates?
5. Avoiding jargon?
6. Addressing concerns?
7. Setting realistic expectations?
8. Follow-up documentation?

### **Q175: Architecture Decision Records (ADR)**
Document important decisions:
1. ADR template structure?
2. Context, decision, consequences?
3. Storage & discoverability?
4. Review & approval process?
5. Reversing decisions?
6. Linking to code?
7. Team buy-in?
8. Maintenance & updates?

### **Q176: Frontend Cost Optimization**
Reduce infrastructure costs:
1. CDN bandwidth optimization?
2. Image compression savings?
3. API call reduction?
4. Bundle size reduction ROI?
5. Caching strategy impact?
6. Serverless cost analysis?
7. Monitoring costs themselves?
8. Cost vs performance trade-offs?

### **Q177: Global Multi-Region Deployment**
Serve users globally với low latency:
1. Region selection strategy?
2. Edge locations (Cloudflare, AWS)?
3. Database replication?
4. Data residency compliance?
5. Routing logic (latency-based, geo)?
6. Failover between regions?
7. Deployment coordination?
8. Cost optimization?

### **Q178: Resiliency & Fault Tolerance**
App hoạt động khi dependencies fail:
1. Circuit breaker pattern?
2. Graceful degradation?
3. Fallback data/UI?
4. Retry with backoff?
5. Timeout configuration?
6. Health checks?
7. Chaos engineering tests?
8. SLA guarantees?

### **Q179: Build Pipeline Optimization**
CI/CD build từ 30 phút → 5 phút:
1. Parallel job execution?
2. Build caching (Nx, Turborepo)?
3. Incremental builds?
4. Docker layer caching?
5. Test parallelization?
6. Artifact reuse?
7. Resource allocation?
8. Pipeline monitoring?

### **Q180: Monorepo Strategy**
Manage large codebase hiệu quả:
1. Nx vs Turborepo vs Lerna?
2. Workspace organization?
3. Dependency graph analysis?
4. Affected command (chỉ build changed)?
5. Shared library versioning?
6. Code ownership (CODEOWNERS)?
7. CI/CD optimization?
8. Scaling challenges (1000+ packages)?

---

**🎯 Tổng Kết Bổ Sung:**

**35 câu hỏi mới** tập trung vào:

**🎨 UX/UI Excellence (10 câu)**
- Empty/loading states, form validation, progressive loading
- Navigation patterns, font rendering
- Notification systems, search UX

**💼 Business Operations (8 câu)**
- Payment integration, OAuth, rate limiting
- Multi-tenant, i18n, analytics
- Cost optimization, global deployment

**🔧 Engineering Process (12 câu)**
- Legacy migration, incident response
- Technical debt, code review, onboarding
- ADRs, stakeholder communication

**⚡ Infrastructure (5 câu)**
- CDN failover, resiliency, build optimization
- Monorepo strategy, multi-region deployment

**Tổng cộng file hiện có: 180 câu hỏi**
- Từ Q0 đến Q180
- Cover đầy đủ: Technical + System + Business + Leadership
- Phù hợp: Senior/Staff/Principal level interviews
