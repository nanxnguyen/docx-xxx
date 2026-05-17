# 📱 Topic 49: Mobile-First Development, Responsive Design, Touch Events & Device Quirks

## 1. ⭐ Senior/Staff Summary

`Mobile-first` nghĩa là thiết kế và implement từ ràng buộc nhỏ nhất trước: màn hình hẹp, network chậm, CPU yếu, touch input, viewport thay đổi, browser quirks và accessibility. Sau đó mới enhance dần cho tablet/desktop.

Các key cần nắm:

- 🎨 **Responsive design:** fluid layout, CSS Grid/Flexbox, media queries, container queries, safe max-width.
- 👁️ **Viewport:** meta viewport đúng, `viewport-fit=cover`, safe-area insets cho notch.
- 👆 **Touch UX:** touch target tối thiểu, pointer/touch events, gesture, scroll, hit area, hover fallback.
- ⚡ **Mobile performance:** image optimization, lazy loading, code splitting, reduce JS, avoid long tasks.
- 🍎 **iOS Safari quirks:** `100vh`, dynamic address bar, input zoom, safe-area, fixed/sticky edge cases.
- 🤖 **Android Chrome quirks:** keyboard resize, back button, viewport changes, device fragmentation.
- 🧪 **Testing:** real device testing, remote debugging, network throttling, automated visual/e2e tests.
- ♿ **Accessibility:** zoom không bị tắt, target đủ lớn, reduced motion, keyboard/screen reader không bị bỏ quên.

> 🔥 Senior point: mobile-first không chỉ là `@media (min-width)`. Nó là cách thiết kế product dưới constraint thật: slow network, touch ergonomics, browser quirks, viewport động, memory thấp và Core Web Vitals trên thiết bị thật.

## 2. 🧠 Key Mental Model or Key Points

- **Start small, enhance upward:** CSS base cho mobile, breakpoint chỉ thêm layout khi màn hình đủ rộng.
- **Content first:** Layout phải phục vụ nội dung và action chính, không ép desktop UI xuống mobile.
- **Viewport không cố định:** Mobile browser có address bar, keyboard, notch, orientation, zoom.
- **Touch khác mouse:** Không có hover ổn định, tap target cần lớn, gesture có xung đột với scroll.
- **Performance budget nhỏ hơn desktop:** Mobile CPU/network yếu hơn, JS parse/execute có thể là bottleneck lớn.
- **Device quirks là production reality:** Emulator không thay thế real iOS/Android devices.
- **Responsive ≠ adaptive only by width:** Cần nghĩ thêm input type, pointer precision, motion preference, orientation, container size.

## 3. 📚 Main Concepts

### 3.1. 🎨 Mobile-First CSS

Mobile-first CSS đặt style mặc định cho mobile, sau đó dùng `min-width` để enhance.

```css
.product-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
  padding: 16px;
}

@media (min-width: 768px) {
  .product-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    padding: 24px;
  }
}

@media (min-width: 1024px) {
  .product-grid {
    grid-template-columns: repeat(3, 1fr);
    max-width: 1200px;
    margin-inline: auto;
  }
}
```

✅ Lợi ích:

- CSS cascade tự nhiên hơn.
- Mobile không phải tải nhiều override desktop.
- Bắt buộc team nghĩ về flow nhỏ trước.
- Dễ giữ UI usable khi breakpoint chưa match.

⚠️ Không nên dùng breakpoint theo device cụ thể quá nhiều. Ưu tiên breakpoint theo layout/content: “khi card đủ rộng thì lên 2 cột”, không phải “iPad thì 2 cột”.

### 3.2. 👁️ Viewport Meta và Safe Area

Viewport meta gần như bắt buộc cho responsive mobile:

```html
<meta
  name="viewport"
  content="width=device-width, initial-scale=1, viewport-fit=cover"
/>
```

Giải thích:

- `width=device-width`: dùng width thật của device, không dùng layout viewport mặc định cũ.
- `initial-scale=1`: không zoom tự động khi load.
- `viewport-fit=cover`: cho phép layout đi vào vùng notch/safe area trên iOS.

Safe area:

```css
.app-shell {
  min-height: 100dvh;
  padding-top: max(16px, env(safe-area-inset-top));
  padding-right: max(16px, env(safe-area-inset-right));
  padding-bottom: max(16px, env(safe-area-inset-bottom));
  padding-left: max(16px, env(safe-area-inset-left));
}
```

> ♿ Không tắt zoom bằng `user-scalable=no` hoặc `maximum-scale=1` nếu không có lý do cực kỳ rõ. Đây là accessibility issue.

### 3.3. 📐 Breakpoints, Container Queries và Fluid Sizing

Breakpoint tham khảo:

| Range | Ý nghĩa thực tế | Lưu ý |
|---|---|---|
| `320-479px` | điện thoại nhỏ | ưu tiên single column |
| `480-767px` | điện thoại lớn | tăng spacing/card density vừa phải |
| `768-1023px` | tablet | cân nhắc 2 columns/sidebar nhẹ |
| `1024px+` | desktop/laptop | layout nhiều cột, hover enhancement |
| `1440px+` | wide desktop | giới hạn max-width để dễ đọc |

Fluid sizing giúp tránh quá nhiều breakpoint:

```css
.page {
  width: min(100% - 32px, 1120px);
  margin-inline: auto;
}

.title {
  font-size: clamp(1.5rem, 4vw, 3rem);
}
```

Container queries hữu ích khi component nằm trong nhiều layout khác nhau:

```css
.card-list {
  container-type: inline-size;
}

@container (min-width: 520px) {
  .product-card {
    display: grid;
    grid-template-columns: 160px 1fr;
  }
}
```

### 3.4. 🧱 Mobile Layout Patterns

Các pattern phổ biến:

- **Single column first:** mobile đọc từ trên xuống, action chính rõ.
- **Bottom navigation:** hợp app có 3-5 tab chính.
- **Drawer/sidebar:** mobile drawer, desktop fixed sidebar.
- **Sticky CTA:** checkout/book/submit action luôn dễ bấm.
- **Progressive disclosure:** ẩn detail phụ sau accordion/sheet thay vì nhồi vào màn hình nhỏ.

Ví dụ shell:

```tsx
export function AppShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="app-shell">
      <aside className="sidebar">...</aside>
      <main className="content">{children}</main>
      <nav className="bottom-nav">...</nav>
    </div>
  );
}
```

```css
.app-shell {
  min-height: 100dvh;
  display: grid;
  grid-template-rows: 1fr auto;
}

.sidebar {
  display: none;
}

.bottom-nav {
  position: sticky;
  bottom: 0;
}

@media (min-width: 1024px) {
  .app-shell {
    grid-template-columns: 280px 1fr;
    grid-template-rows: 1fr;
  }

  .sidebar {
    display: block;
  }

  .bottom-nav {
    display: none;
  }
}
```

### 3.5. 👆 Touch Events, Pointer Events và Gestures

Modern recommendation: ưu tiên `Pointer Events` vì gom mouse, touch, pen vào cùng model.

| API | Dùng khi | Ghi chú |
|---|---|---|
| `click` | button/link bình thường | Browser xử lý activation/accessibility tốt |
| `pointerdown/move/up` | drag/swipe/custom gesture | Hỗ trợ mouse/touch/pen |
| `touchstart/move/end` | legacy hoặc cần touch-specific | Cẩn thận passive listeners |
| `wheel` | trackpad/mouse wheel | Không đại diện touch scroll |

Touch target:

- ✅ Nên tối thiểu khoảng `44x44px`.
- ✅ Có spacing giữa các target để tránh bấm nhầm.
- ✅ Đừng chỉ dựa vào hover để lộ action.
- ✅ Dùng real button/link để giữ accessibility.

```css
.icon-button {
  min-width: 44px;
  min-height: 44px;
  display: inline-grid;
  place-items: center;
  touch-action: manipulation;
}
```

Gesture cần tránh xung đột với scroll:

```css
.carousel {
  touch-action: pan-y;
}
```

`touch-action: pan-y` nói với browser: vertical scroll vẫn thuộc browser, component chỉ xử lý horizontal gesture.

### 3.6. ⚡ Mobile Performance Optimization

Mobile performance thường nghẽn ở:

- JS bundle lớn: parse/compile/execute chậm.
- Image quá nặng.
- Font blocking.
- Main-thread long tasks.
- Layout/repaint lớn.
- Third-party scripts.

Image:

```html
<img
  src="/products/shoe-640.webp"
  srcset="/products/shoe-320.webp 320w, /products/shoe-640.webp 640w, /products/shoe-960.webp 960w"
  sizes="(min-width: 768px) 33vw, 100vw"
  width="640"
  height="480"
  loading="lazy"
  decoding="async"
  alt="Giày chạy bộ màu đen"
/>
```

Code splitting:

```tsx
const ProductReviews = React.lazy(() => import("./ProductReviews"));

function ProductPage() {
  return (
    <React.Suspense fallback={<ReviewsSkeleton />}>
      <ProductReviews />
    </React.Suspense>
  );
}
```

Performance budget gợi ý:

- Critical JS càng nhỏ càng tốt.
- Defer non-critical scripts.
- Lazy load below-the-fold images/components.
- Preload hero image/font quan trọng có kiểm soát.
- Đo LCP/INP/CLS trên device thật hoặc lab profile mobile.

### 3.7. 🍎 iOS Safari Quirks

Các vấn đề thường gặp:

**`100vh` không khớp viewport thật**

iOS Safari có dynamic address bar. Dùng viewport units mới khi có thể:

```css
.full-screen {
  min-height: 100dvh;
}

@supports not (height: 100dvh) {
  .full-screen {
    min-height: 100vh;
  }
}
```

**Input zoom**

iOS có thể zoom khi input font-size nhỏ. Giữ font-size input ít nhất `16px`.

```css
input,
select,
textarea {
  font-size: 16px;
}
```

**Safe area / notch**

Dùng `env(safe-area-inset-*)` cho fixed header/footer/bottom nav.

**Fixed/sticky + keyboard**

Khi keyboard mở, viewport thay đổi. Tránh giả định fixed footer luôn nằm đúng; test form trên real iPhone.

### 3.8. 🤖 Android Chrome Quirks

Các vấn đề thường gặp:

- Keyboard làm viewport resize khác nhau theo browser/device.
- Back button cần hành vi rõ với modal/drawer.
- Device fragmentation: RAM/CPU/GPU/browser version rất đa dạng.
- Một số WebView cũ thiếu feature hoặc có bug khác Chrome mới.
- Address bar show/hide làm viewport height thay đổi.

Back button với modal:

```ts
function openModalWithHistory() {
  window.history.pushState({ modal: true }, "");
  openModal();
}

window.addEventListener("popstate", () => {
  if (isModalOpen()) {
    closeModal();
  }
});
```

> ⚠️ Đừng phá browser back navigation. Với SPA, back button nên đóng modal/drawer trước, sau đó mới rời route nếu phù hợp.

### 3.9. 🧪 Testing: Device, Emulator, Automation

Emulator tốt để iterate nhanh, nhưng không đủ cho production mobile.

Test matrix tối thiểu:

- iOS Safari real device.
- Android Chrome real device.
- Small phone width khoảng 320-360px.
- Low/mid-range Android nếu target user phổ biến.
- Slow 3G/4G throttling.
- Portrait và landscape.
- Keyboard open/close.
- Notch/safe area.
- Reduced motion / larger text.

Remote debugging:

- Android: Chrome `chrome://inspect`.
- iOS: Safari Develop menu với device thật.
- Performance: record trace trên device thật, không chỉ desktop throttling.

Automated testing:

- Playwright/Cypress viewport tests.
- Visual regression ở vài viewport chính.
- Lighthouse/WebPageTest mobile profile.
- BrowserStack/Sauce Labs khi cần device coverage rộng.

## 4. 🧪 Practical TypeScript/JavaScript Examples

### 4.1. ✅ Hook phát hiện coarse pointer

```tsx
function useIsTouchLikePointer() {
  const [isTouchLike, setIsTouchLike] = React.useState(false);

  React.useEffect(() => {
    const media = window.matchMedia("(pointer: coarse)");

    function update() {
      setIsTouchLike(media.matches);
    }

    update();
    media.addEventListener("change", update);

    return () => media.removeEventListener("change", update);
  }, []);

  return isTouchLike;
}
```

> 💡 Dùng để điều chỉnh UI density hoặc interaction hint, không dùng để phân biệt tuyệt đối “mobile vs desktop”.

### 4.2. ✅ Swipe gesture bằng Pointer Events

```tsx
function useSwipe(onSwipeLeft: () => void, onSwipeRight: () => void) {
  const startX = React.useRef<number | null>(null);

  const onPointerDown = React.useCallback((event: React.PointerEvent) => {
    startX.current = event.clientX;
  }, []);

  const onPointerUp = React.useCallback(
    (event: React.PointerEvent) => {
      if (startX.current === null) return;

      const deltaX = event.clientX - startX.current;
      startX.current = null;

      if (Math.abs(deltaX) < 48) return;
      if (deltaX < 0) onSwipeLeft();
      else onSwipeRight();
    },
    [onSwipeLeft, onSwipeRight],
  );

  return { onPointerDown, onPointerUp };
}
```

Usage:

```tsx
function ProductCarousel() {
  const swipeHandlers = useSwipe(showNext, showPrevious);

  return (
    <div className="carousel" {...swipeHandlers}>
      ...
    </div>
  );
}
```

```css
.carousel {
  touch-action: pan-y;
}
```

### 4.3. ✅ Safe-area bottom navigation

```css
.bottom-nav {
  position: sticky;
  bottom: 0;
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  padding-bottom: max(8px, env(safe-area-inset-bottom));
  min-height: calc(56px + env(safe-area-inset-bottom));
  background: Canvas;
  border-top: 1px solid color-mix(in srgb, CanvasText 12%, transparent);
}

.bottom-nav button {
  min-height: 44px;
  touch-action: manipulation;
}
```

### 4.4. ✅ Responsive e-commerce product grid

```css
.product-page {
  width: min(100% - 32px, 1180px);
  margin-inline: auto;
  padding-block: 16px 80px;
}

.product-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 16px;
}

@media (min-width: 640px) {
  .product-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}

@media (min-width: 1024px) {
  .product-grid {
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;
  }
}
```

### 4.5. ✅ React image component có kích thước ổn định

```tsx
type ResponsiveImageProps = {
  alt: string;
  src: string;
  srcSet: string;
  sizes: string;
  width: number;
  height: number;
};

function ResponsiveImage(props: ResponsiveImageProps) {
  return (
    <img
      {...props}
      loading="lazy"
      decoding="async"
      style={{
        width: "100%",
        height: "auto",
        aspectRatio: `${props.width} / ${props.height}`,
      }}
    />
  );
}
```

## 5. 🏭 Production Notes / React Implications

- ⚛️ **Hydration:** Đừng render khác nhau giữa server/client chỉ vì đọc `window.innerWidth`. Dùng CSS responsive trước, JS sau mount khi thật sự cần.
- 📦 **Bundle:** Mobile-first cần giảm JS, không chỉ CSS. Route splitting, defer third-party, tránh ship desktop-only code sớm.
- 🖼️ **Images:** Set `width/height` hoặc `aspect-ratio` để tránh CLS. Dùng responsive images và modern formats.
- 👆 **Touch:** Button/link thật tốt hơn div clickable. Giữ hit target đủ lớn và focus state rõ.
- ♿ **Accessibility:** Không disable zoom, hỗ trợ reduced motion, screen reader, keyboard, text scaling.
- 🧪 **Testing:** Test iOS Safari thật cho `100vh`, keyboard, safe area. Test Android thật cho back button, keyboard, low-end performance.
- 🔐 **Security:** Mobile WebView/in-app browsers có behavior khác; auth redirect, cookie, storage và deep link cần test riêng.
- 🚀 **Performance:** Đo LCP/INP/CLS trên mobile profile. INP thường bị ảnh hưởng bởi long JS tasks và heavy event handlers.
- 🧱 **Maintainability:** Tạo design tokens cho spacing/breakpoints/touch target thay vì hardcode rải rác.
- 🧯 **Fallback:** Feature mới như container queries/dynamic viewport units cần fallback hoặc support matrix rõ.

## 6. ⚠️ Common Pitfalls

- ❌ Build desktop trước rồi cố thu nhỏ xuống mobile.
- ❌ Dùng breakpoint theo device name thay vì theo content/layout.
- ❌ Tắt zoom bằng `user-scalable=no`.
- ❌ Touch target quá nhỏ, icon button chỉ 24px nhưng hit area không đủ.
- ❌ Dựa vào hover để hiện action quan trọng trên mobile.
- ❌ Dùng `100vh` cũ cho full-screen mobile mà không test iOS Safari.
- ❌ Không xử lý safe-area cho bottom nav/fixed CTA.
- ❌ Load ảnh desktop lớn cho mobile.
- ❌ Ship bundle desktop-heavy cho mobile.
- ❌ Gesture custom chặn scroll tự nhiên.
- ❌ Không cleanup event listeners trong React hooks.
- ❌ Chỉ test bằng Chrome DevTools emulator, không test device thật.
- ❌ Quên keyboard open/close trong form và checkout flow.
- ❌ Không đo LCP/INP/CLS trên mobile.

## 7. ✅ Decision Guide or Checklist + câu trả lời ngắn

### Chọn kỹ thuật nào?

| Nhu cầu | Chọn | Trả lời ngắn |
|---|---|---|
| Layout responsive cơ bản | Mobile-first CSS + `min-width` queries | Base mobile, enhance dần cho màn hình rộng. |
| Component phụ thuộc width của container | Container queries | Tốt hơn breakpoint global khi component tái sử dụng nhiều nơi. |
| Full-screen mobile | `100dvh` + fallback | Tránh bug dynamic address bar của mobile browser. |
| Notch/bottom home indicator | `env(safe-area-inset-*)` | Cần cho fixed header/footer/bottom nav. |
| Button/icon touch | `min-width/min-height: 44px` | Giảm bấm nhầm, tốt cho accessibility. |
| Custom swipe/drag | Pointer Events + `touch-action` | Hỗ trợ mouse/touch/pen và tránh chặn scroll sai. |
| Product/list dài | Pagination hoặc virtualization | Giảm DOM, memory và render cost. |
| Ảnh responsive | `srcset`, `sizes`, WebP/AVIF, dimensions | Giảm LCP/CLS và bandwidth. |
| Code lớn theo route | Dynamic import / route splitting | Mobile không tải JS chưa cần. |
| Mobile browser bug | Feature detection + real device test | Đừng chỉ UA sniff nếu có thể tránh. |

### Checklist trước khi merge mobile UI

| Câu hỏi | Trả lời ngắn |
|---|---|
| Base CSS đã mobile-first chưa? | Nên có mobile layout trước, desktop chỉ là enhancement. |
| Meta viewport đúng chưa? | Cần `width=device-width, initial-scale=1`; không disable zoom. |
| Touch targets đủ lớn chưa? | Nên tối thiểu khoảng `44x44px`, có spacing chống bấm nhầm. |
| Có phụ thuộc hover không? | Action quan trọng phải dùng được bằng tap/focus. |
| Full-screen có dùng `100dvh` hoặc fallback chưa? | Cần để tránh `100vh` sai trên mobile Safari/Chrome. |
| Fixed bottom/header có safe-area chưa? | Cần `env(safe-area-inset-*)` cho notch/home indicator. |
| Ảnh có responsive + dimensions chưa? | Cần `srcset/sizes` và `width/height` hoặc `aspect-ratio`. |
| JS mobile có quá nặng không? | Kiểm tra bundle, code split và defer third-party. |
| Gesture có chặn scroll không? | Dùng `touch-action` và test scroll thật. |
| Form đã test keyboard chưa? | Test focus, viewport resize, sticky CTA và submit trên device. |
| Đã test real iOS/Android chưa? | Cần ít nhất một iPhone Safari và một Android Chrome thật. |
| LCP/INP/CLS mobile ổn chưa? | Đo bằng Lighthouse/WebPageTest/field data nếu có. |

## 8. 🗣️ Short Interview Answer

Theo em, mobile-first không chỉ là viết media query từ nhỏ lên lớn. Nó là cách build UI từ constraint thật của mobile: màn hình nhỏ, touch input, network chậm, CPU yếu, browser viewport thay đổi và nhiều quirks trên iOS/Android. Em thường viết CSS base cho mobile trước, dùng `min-width` hoặc container queries để enhance, giữ touch target đủ lớn và không phụ thuộc hover cho action quan trọng.

Về performance, em ưu tiên giảm JS và ảnh cho mobile: responsive images, lazy loading, route-level code splitting, defer third-party và đo LCP/INP/CLS trên mobile profile. Với device quirks, em chú ý `100vh` trên iOS, safe-area cho notch, input zoom, keyboard resize và Android back button. Em không chỉ tin emulator; flow quan trọng như login, checkout, form và sticky CTA phải test trên thiết bị thật.

## 9. 🧾 Ghi nhớ nhanh

- Mobile-first = base mobile, enhance desktop.
- Breakpoint nên theo content/layout, không theo tên device.
- Không disable zoom; đây là accessibility issue.
- Touch target nên khoảng `44x44px`.
- Hover không đáng tin trên touch devices.
- Dùng `100dvh` cho full-screen mobile khi support cho phép.
- Safe area cần cho notch/home indicator.
- Ảnh và JS thường là bottleneck lớn nhất trên mobile.
- Dùng Pointer Events cho gesture hiện đại.
- `touch-action` giúp tránh gesture chặn scroll sai.
- iOS Safari và Android Chrome phải test thật.
- Đo LCP/INP/CLS trên mobile, không đo mỗi desktop.

## 10. 📖 Giải thích các thuật ngữ trong topic

- `Mobile-first`: Cách thiết kế/implement từ mobile constraint trước, rồi mở rộng cho màn hình lớn.
- `Responsive design`: UI thích ứng với kích thước viewport/container khác nhau.
- `Breakpoint`: Ngưỡng width/container size nơi layout thay đổi.
- `Media query`: CSS rule áp dụng theo điều kiện như width, orientation, pointer.
- `Container query`: CSS rule áp dụng theo kích thước container của component.
- `Viewport`: Vùng hiển thị trang web trong browser.
- `Dynamic viewport`: Viewport thay đổi khi address bar/keyboard show-hide trên mobile.
- `100vh`: 100% viewport height kiểu cũ, có thể sai trên mobile browser.
- `100dvh`: Dynamic viewport height, phản ánh viewport hiện tại tốt hơn.
- `Safe area`: Vùng tránh notch, rounded corners, home indicator.
- `Touch target`: Vùng có thể chạm để kích hoạt control.
- `Pointer Events`: Event model thống nhất cho mouse, touch và pen.
- `Touch Events`: Event model touch-specific cũ hơn.
- `Gesture`: Tương tác như swipe, pinch, long press, drag.
- `touch-action`: CSS khai báo gesture nào browser được xử lý mặc định.
- `Lazy loading`: Trì hoãn tải tài nguyên đến khi gần cần dùng.
- `Code splitting`: Chia bundle để chỉ tải phần code cần thiết.
- `LCP`: Largest Contentful Paint, đo tốc độ nội dung chính hiển thị.
- `INP`: Interaction to Next Paint, đo độ phản hồi sau tương tác.
- `CLS`: Cumulative Layout Shift, đo layout shift ngoài ý muốn.
- `PWA`: Progressive Web App, web app có thể cài đặt/offline/tích hợp native-like.
- `Remote debugging`: Debug web trên device thật từ desktop DevTools.
