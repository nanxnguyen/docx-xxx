# Topic19: Browser Observer APIs - Intersection, Resize, Mutation Observer

## ⭐ Mục tiêu phỏng vấn Senior/Staff

> **Observer APIs giúp theo dõi thay đổi của browser/DOM một cách bất đồng bộ, hiệu quả hơn polling hoặc event listener thủ công.**

Senior/staff frontend cần nắm:

- 👁️ `IntersectionObserver`: element có vào viewport/container không.
- 📐 `ResizeObserver`: element có đổi kích thước không.
- 🧬 `MutationObserver`: DOM có bị thêm/xóa/sửa node/attribute không.
- ⚡ Vì sao observer tốt hơn `scroll`, `resize`, polling thủ công.
- 🧹 Cleanup đúng để tránh memory leak.
- 🧠 Performance pitfalls: layout thrashing, infinite loop, over-observing.
- 🧩 Cách dùng trong React/component architecture.

---

## 1. 🧠 Observer APIs Là Gì?

Observer APIs là nhóm Web APIs cho phép browser thông báo khi một điều kiện thay đổi:

```txt
DOM visibility changes    -> IntersectionObserver
Element size changes      -> ResizeObserver
DOM tree changes          -> MutationObserver
```

Thay vì tự làm:

```ts
window.addEventListener("scroll", () => {
  element.getBoundingClientRect();
});
```

Ta dùng:

```ts
const observer = new IntersectionObserver((entries) => {
  // browser báo khi element giao với viewport/container
});
```

### 🔥 Highlight

> **Observer API chuyển việc theo dõi thay đổi từ app code sang browser engine, giúp giảm polling, giảm layout thrashing và dễ batch callback hơn.**

---

## 2. 🧩 So Sánh Nhanh 3 Observer

| API | Theo dõi gì? | Use case chính | Thay thế cho |
|---|---|---|---|
| 👁️ `IntersectionObserver` | Element vào/ra viewport hoặc container | Lazy image, infinite scroll, analytics viewability | `scroll` + `getBoundingClientRect()` |
| 📐 `ResizeObserver` | Kích thước element thay đổi | Responsive chart, virtual layout, component resize | `window.resize`, polling size |
| 🧬 `MutationObserver` | DOM node/attribute/text thay đổi | Third-party integration, auto-init, detect DOM injection | Mutation Events cũ, polling DOM |

### Mental model

```txt
observe(target)
  -> browser theo dõi target
  -> batch changes
  -> gọi callback(entries)
  -> app xử lý
  -> disconnect/unobserve khi không cần
```

---

## 3. 👁️ IntersectionObserver

`IntersectionObserver` theo dõi một element có giao với viewport hoặc container không.

```ts
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        console.log("Element visible");
      }
    }
  },
  {
    root: null,
    rootMargin: "200px",
    threshold: 0.1,
  }
);

observer.observe(element);
```

### Options quan trọng

| Option | Ý nghĩa |
|---|---|
| `root` | Container dùng để tính visibility. `null` nghĩa là viewport |
| `rootMargin` | Nới rộng/thu hẹp vùng observe, giống CSS margin |
| `threshold` | Tỉ lệ visible để trigger callback, từ `0` đến `1` |

Ví dụ:

```ts
{
  root: null,
  rootMargin: "300px 0px",
  threshold: 0
}
```

Nghĩa là callback chạy khi element còn cách viewport 300px, phù hợp để preload sớm.

### Entry quan trọng

```ts
entry.target;              // element đang observe
entry.isIntersecting;      // có đang giao không
entry.intersectionRatio;   // tỉ lệ giao nhau 0..1
entry.boundingClientRect;  // rect của target
entry.rootBounds;          // rect của root
```

---

## 4. 🖼️ Use Case: Lazy Load Image

```tsx
import { useEffect, useRef, useState } from "react";

type LazyImageProps = {
  src: string;
  alt: string;
};

export function LazyImage({ src, alt }: LazyImageProps) {
  const imgRef = useRef<HTMLImageElement | null>(null);
  const [shouldLoad, setShouldLoad] = useState(false);

  useEffect(() => {
    const img = imgRef.current;
    if (!img || shouldLoad) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setShouldLoad(true);
          observer.unobserve(entry.target);
        }
      },
      { rootMargin: "300px 0px" }
    );

    observer.observe(img);

    return () => observer.disconnect();
  }, [shouldLoad]);

  return (
    <img
      ref={imgRef}
      src={shouldLoad ? src : undefined}
      alt={alt}
      loading="lazy"
      width={800}
      height={450}
    />
  );
}
```

### Senior notes

- Native `loading="lazy"` đủ tốt cho nhiều case đơn giản.
- IntersectionObserver hữu ích khi cần custom preload, animation trigger, analytics hoặc infinite scroll.
- Luôn set `width/height` hoặc aspect ratio để tránh CLS.

---

## 5. ♾️ Use Case: Infinite Scroll

Pattern phổ biến là đặt một `sentinel` ở cuối list.

```tsx
function InfiniteList({ loadMore, hasMore, isLoading }) {
  const sentinelRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    const sentinel = sentinelRef.current;
    if (!sentinel || !hasMore) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting && !isLoading) {
          loadMore();
        }
      },
      { rootMargin: "400px 0px" }
    );

    observer.observe(sentinel);

    return () => observer.disconnect();
  }, [loadMore, hasMore, isLoading]);

  return <div ref={sentinelRef} />;
}
```

### ⚠️ Pitfalls

- Cần guard `isLoading` để tránh gọi API nhiều lần.
- Cần `hasMore` để ngừng observe khi hết data.
- Nên xử lý error/retry.
- Với list rất lớn, kết hợp virtualization.

### 🔥 Highlight

> **Infinite scroll production không chỉ là observer. Cần loading guard, pagination state, error handling, hasMore và virtualization nếu list lớn.**

---

## 6. 📊 Use Case: Viewability Analytics

Ví dụ: chỉ track impression khi item hiển thị ít nhất 50%.

```ts
const observer = new IntersectionObserver(
  (entries) => {
    for (const entry of entries) {
      if (entry.isIntersecting && entry.intersectionRatio >= 0.5) {
        trackImpression(entry.target.id);
        observer.unobserve(entry.target);
      }
    }
  },
  { threshold: [0.5] }
);
```

Analytics tốt cần:

- Không track trùng.
- Có threshold rõ.
- Có thể yêu cầu visible trong một khoảng thời gian, ví dụ 1 giây.
- Không gửi event quá nhiều, nên batch.

---

## 7. 📐 ResizeObserver

`ResizeObserver` theo dõi kích thước của element.

```ts
const observer = new ResizeObserver((entries) => {
  for (const entry of entries) {
    const { width, height } = entry.contentRect;
    console.log(width, height);
  }
});

observer.observe(element);
```

Nó tốt hơn `window.resize` vì:

- `window.resize` chỉ biết viewport đổi.
- Element có thể đổi size do parent, content, sidebar, CSS grid, font, data.
- Component responsive nên quan sát chính container của nó.

### Entry quan trọng

```ts
entry.target;
entry.contentRect;
entry.contentBoxSize;
entry.borderBoxSize;
entry.devicePixelContentBoxSize;
```

| Field | Ý nghĩa |
|---|---|
| `contentRect` | Kích thước content box, dễ dùng nhất |
| `contentBoxSize` | Content box size hiện đại hơn |
| `borderBoxSize` | Tính cả border |
| `devicePixelContentBoxSize` | Pixel vật lý, hữu ích cho canvas high-DPI |

---

## 8. 📈 Use Case: Responsive Chart

```tsx
function ResponsiveChart() {
  const containerRef = useRef<HTMLDivElement | null>(null);
  const [size, setSize] = useState({ width: 0, height: 0 });

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    const observer = new ResizeObserver(([entry]) => {
      const { width, height } = entry.contentRect;

      setSize({
        width: Math.round(width),
        height: Math.round(height),
      });
    });

    observer.observe(container);

    return () => observer.disconnect();
  }, []);

  return (
    <div ref={containerRef} style={{ width: "100%", height: 320 }}>
      {size.width > 0 && <Chart width={size.width} height={size.height} />}
    </div>
  );
}
```

### ⚠️ ResizeObserver loop

Sai pattern:

```ts
new ResizeObserver(([entry]) => {
  entry.target.style.width = `${entry.contentRect.width + 1}px`;
});
```

Callback resize lại đổi size chính element đang observe, có thể tạo loop.

Tốt hơn:

- Không mutate size của chính target trong callback.
- Nếu cần update layout, dùng state có guard.
- Có thể schedule bằng `requestAnimationFrame`.

```ts
let frame = 0;

const observer = new ResizeObserver(([entry]) => {
  cancelAnimationFrame(frame);

  frame = requestAnimationFrame(() => {
    updateLayout(entry.contentRect);
  });
});
```

### 🔥 Highlight

> **ResizeObserver phù hợp cho component-level responsiveness. Nhưng callback không nên gây resize loop trên chính element đang observe.**

---

## 9. 🧬 MutationObserver

`MutationObserver` theo dõi thay đổi trong DOM tree.

```ts
const observer = new MutationObserver((mutations) => {
  for (const mutation of mutations) {
    console.log(mutation.type);
  }
});

observer.observe(element, {
  childList: true,
  attributes: true,
  subtree: true,
});
```

### Options quan trọng

| Option | Ý nghĩa |
|---|---|
| `childList` | Theo dõi node con được thêm/xóa |
| `attributes` | Theo dõi attribute thay đổi |
| `characterData` | Theo dõi text node thay đổi |
| `subtree` | Theo dõi cả cây con |
| `attributeFilter` | Chỉ observe một số attribute |
| `attributeOldValue` | Lưu giá trị attribute cũ |

### Mutation record

```ts
mutation.type;           // "childList" | "attributes" | "characterData"
mutation.target;
mutation.addedNodes;
mutation.removedNodes;
mutation.attributeName;
mutation.oldValue;
```

---

## 10. 🧩 Use Case: Third-Party Integration

Khi tích hợp CMS, widget, extension hoặc script ngoài, DOM có thể bị thêm sau khi app render.

```ts
const observer = new MutationObserver((mutations) => {
  for (const mutation of mutations) {
    for (const node of mutation.addedNodes) {
      if (!(node instanceof HTMLElement)) continue;

      const widget = node.matches("[data-widget]")
        ? node
        : node.querySelector("[data-widget]");

      if (widget) {
        initializeWidget(widget);
      }
    }
  }
});

observer.observe(document.body, {
  childList: true,
  subtree: true,
});
```

### ⚠️ Pitfalls

- Observe `document.body` + `subtree: true` có thể rất tốn nếu DOM thay đổi nhiều.
- Cần filter sớm để callback nhẹ.
- Nếu callback tự sửa DOM, có thể trigger observer lại.
- Phải `disconnect()` khi không còn cần.

### 🔥 Highlight

> **MutationObserver là công cụ mạnh nhưng dễ bị lạm dụng. Chỉ observe phạm vi nhỏ nhất và filter mutation càng sớm càng tốt.**

---

## 11. 🧹 Cleanup: `unobserve` Vs `disconnect`

```ts
observer.observe(elementA);
observer.observe(elementB);

observer.unobserve(elementA); // ngừng observe một element
observer.disconnect();        // ngừng toàn bộ observer
```

| Method | Khi dùng |
|---|---|
| `unobserve(target)` | Bỏ theo dõi một element cụ thể |
| `disconnect()` | Cleanup toàn bộ observer |
| `takeRecords()` | Lấy records đang pending trước khi callback chạy |

Trong React, cleanup thường đặt trong `useEffect`:

```ts
useEffect(() => {
  const observer = new IntersectionObserver(callback);

  if (ref.current) {
    observer.observe(ref.current);
  }

  return () => observer.disconnect();
}, []);
```

### 🔥 Highlight

> **Quên cleanup observer là lỗi production phổ biến, đặc biệt trong SPA khi component mount/unmount nhiều lần.**

---

## 12. ⚡ Performance Model

Observer APIs thường tốt hơn event listeners thủ công vì browser có thể:

- Batch nhiều thay đổi thành một callback.
- Tối ưu thời điểm callback.
- Tránh app phải đọc layout liên tục.
- Giảm polling.
- Giảm số lần chạy code khi scroll/resize.

Nhưng không có nghĩa callback được phép nặng.

Callback nên:

- Làm ít việc.
- Không đọc/ghi layout lặp lại.
- Debounce/throttle nếu cần.
- Batch analytics/network calls.
- Cleanup đúng.
- Observe ít target nhất có thể.

### Layout thrashing

Pattern xấu:

```ts
for (const item of items) {
  const rect = item.getBoundingClientRect(); // read layout
  item.style.height = `${rect.width}px`;     // write layout
}
```

Nên tách read và write:

```ts
const sizes = items.map((item) => item.getBoundingClientRect());

items.forEach((item, index) => {
  item.style.height = `${sizes[index].width}px`;
});
```

---

## 13. 🧠 One Observer Cho Nhiều Elements

Thường nên dùng một observer để observe nhiều targets cùng options.

```ts
const observer = new IntersectionObserver((entries) => {
  for (const entry of entries) {
    if (entry.isIntersecting) {
      reveal(entry.target);
      observer.unobserve(entry.target);
    }
  }
});

document.querySelectorAll("[data-reveal]").forEach((element) => {
  observer.observe(element);
});
```

Không nên tạo quá nhiều observer giống nhau:

```ts
// Không tối ưu nếu có 500 items
items.forEach((item) => {
  const observer = new IntersectionObserver(callback);
  observer.observe(item);
});
```

### Senior note

> **Tối ưu tốt là reuse observer theo cùng option set, không tạo observer mới cho từng element nếu không cần.**

---

## 14. ⚛️ React Hook Patterns

### `useIntersectionObserver`

```tsx
function useIntersectionObserver(
  ref: React.RefObject<Element>,
  options?: IntersectionObserverInit
) {
  const [entry, setEntry] = useState<IntersectionObserverEntry | null>(null);

  useEffect(() => {
    const target = ref.current;
    if (!target) return;

    const observer = new IntersectionObserver(([nextEntry]) => {
      setEntry(nextEntry);
    }, options);

    observer.observe(target);

    return () => observer.disconnect();
  }, [ref, options?.root, options?.rootMargin, options?.threshold]);

  return entry;
}
```

### ⚠️ Lưu ý với options object

Nếu truyền object inline:

```tsx
useIntersectionObserver(ref, { threshold: 0.5 });
```

Object mới được tạo mỗi render, effect có thể chạy lại. Nên memoize nếu cần:

```tsx
const options = useMemo(() => ({ threshold: 0.5 }), []);
const entry = useIntersectionObserver(ref, options);
```

### Callback stale closure

Nếu observer callback dùng state/function thay đổi liên tục, cần cẩn thận stale closure hoặc effect recreate quá nhiều.

Pattern tốt:

- Dùng `useCallback` cho callback ổn định.
- Dùng ref để giữ latest callback nếu cần.
- Cleanup observer khi dependency đổi.

---

## 15. 🔄 Observer Vs Event Listener

| Nhu cầu | Nên dùng |
|---|---|
| Biết element có visible không | `IntersectionObserver` |
| Biết element đổi size không | `ResizeObserver` |
| Biết DOM node/attribute đổi không | `MutationObserver` |
| Cần bắt click/input/keyboard | Event listener |
| Cần scroll position chính xác từng frame | Scroll listener + throttle/rAF |
| Cần animation theo scroll liên tục | CSS Scroll-driven animation hoặc rAF |

### 🔥 Highlight

> **Observer không thay thế mọi event listener. Nó thay thế tốt các case theo dõi visibility, size và DOM mutation.**

---

## 16. 🛡️ Production Checklist

- ✅ Cleanup bằng `disconnect()` khi component unmount.
- ✅ Dùng `unobserve()` khi target đã xử lý xong.
- ✅ Reuse một observer cho nhiều elements nếu options giống nhau.
- ✅ Callback nhẹ, tránh logic nặng.
- ✅ Tránh đọc/ghi layout xen kẽ gây layout thrashing.
- ✅ Với `ResizeObserver`, tránh mutate size của chính target liên tục.
- ✅ Với `MutationObserver`, observe phạm vi nhỏ nhất.
- ✅ Filter mutation sớm bằng `attributeFilter`, selector hoặc node type.
- ✅ Guard infinite scroll bằng `isLoading` và `hasMore`.
- ✅ Track analytics không trùng, có threshold/time rule.
- ✅ Test trên Safari/mobile nếu dùng API mới hoặc edge case layout.

---

## 17. ⚠️ Lỗi Thường Gặp Khi Phỏng Vấn

### 1. Nói observer luôn chạy off-main-thread

Không chính xác. Browser tối ưu việc theo dõi và batch callback, nhưng callback JavaScript vẫn chạy trên main thread.

### 2. Quên cleanup

SPA unmount/mount nhiều lần có thể giữ reference cũ, gây memory leak hoặc callback chạy sai.

### 3. Dùng MutationObserver cho state trong React

Nếu DOM do React quản lý, thường nên đọc từ state/props thay vì observe DOM ngược lại.

### 4. Dùng ResizeObserver thay CSS container queries cho mọi thứ

Nếu chỉ cần đổi style theo container size, CSS container queries thường đơn giản hơn.

### 5. Dùng IntersectionObserver cho animation từng pixel

IntersectionObserver không dành cho animation theo scroll từng frame. Dùng CSS/rAF phù hợp hơn.

### 6. Observe phạm vi quá rộng

`document.body` + `subtree: true` trong MutationObserver có thể rất đắt.

---

## 18. 🧾 Câu Trả Lời Phỏng Vấn 2 Phút

> **Observer APIs là nhóm Web APIs giúp theo dõi thay đổi của DOM/browser hiệu quả hơn polling hoặc event listeners thủ công. Ba API chính là IntersectionObserver để biết element vào/ra viewport hoặc container, ResizeObserver để biết element đổi kích thước, và MutationObserver để biết DOM tree, attribute hoặc text node thay đổi.**
>
> **IntersectionObserver thường dùng cho lazy loading, infinite scroll và viewability analytics, thay cho scroll listener cộng `getBoundingClientRect`. ResizeObserver dùng cho responsive component như chart/grid vì element có thể đổi size mà window không resize. MutationObserver dùng khi cần tích hợp third-party DOM hoặc theo dõi DOM mutation, nhưng phải giới hạn scope vì có thể rất tốn.**
>
> **Ở production, điểm quan trọng là cleanup bằng `disconnect`, reuse observer khi options giống nhau, callback phải nhẹ, tránh layout thrashing và tránh mutation/resize loop. Observer giúp browser batch và tối ưu việc theo dõi, nhưng callback JS vẫn chạy trên main thread nên không được xử lý nặng trong đó.**

---

## 19. 🎯 Câu Trả Lời Staff-Level

> **Ở staff level, tôi xem Observer APIs như primitive để xây dựng UI reactive với browser state mà không tạo polling hoặc event storm. Tôi chọn IntersectionObserver cho visibility, ResizeObserver cho component-level layout, MutationObserver cho DOM integration ngoài vòng kiểm soát của framework.**
>
> **Tôi không dùng observer như default solution cho mọi thứ. Nếu React state đã là source of truth thì không observe DOM để suy luận ngược. Nếu chỉ cần style theo container size thì ưu tiên CSS container queries. Nếu cần scroll animation liên tục thì dùng CSS/rAF thay vì IntersectionObserver.**
>
> **Khi thiết kế shared hook/component, tôi quan tâm đến lifecycle và scale: một observer có thể observe nhiều targets, cleanup rõ ràng, callback không gây layout thrashing, analytics được dedupe/batch, infinite scroll có loading guard và virtualization. Đó là khác biệt giữa demo chạy được và implementation production-ready.**

---

## 20. 🧠 Ghi Nhớ Nhanh

| Icon | Ý chính |
|---|---|
| 👁️ | IntersectionObserver theo dõi visibility |
| 📐 | ResizeObserver theo dõi element size |
| 🧬 | MutationObserver theo dõi DOM changes |
| 🧹 | Luôn cleanup bằng `disconnect()` |
| ♾️ | Infinite scroll cần `isLoading` + `hasMore` |
| ⚡ | Callback vẫn chạy trên main thread, phải nhẹ |
| 🧩 | Reuse observer cho nhiều elements nếu options giống |
| ⚠️ | Mutation/resize callback có thể tạo loop |
| 🎯 | Observer tốt cho visibility/size/mutation, không thay mọi event |

---

## 21. ✅ Kết Luận

> **Observer APIs giúp frontend theo dõi visibility, size và DOM mutation hiệu quả hơn cách thủ công, nhưng senior/staff cần hiểu lifecycle, cleanup, batching, performance và giới hạn của từng API.**

Câu nhớ nhanh:

> **Intersection = thấy chưa, Resize = to nhỏ chưa, Mutation = DOM đổi chưa. Dùng đúng API, scope nhỏ, callback nhẹ, cleanup kỹ.**
