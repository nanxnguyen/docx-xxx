# 👁️ Q46: Observer APIs - Intersection, Resize, Mutation Observer

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">👁️ Q46: Observer APIs - Intersection, Resize, Mutation Observer</span></summary>


**❓ Câu Hỏi:**

Observer APIs là gì? Khi nào và tại sao nên dùng chúng thay vì event listeners truyền thống?


**✅ Đáp Án Chi Tiết:**

**🎯 Tổng Quan Observer APIs:**

Observer APIs là nhóm Web APIs hiện đại cho phép **theo dõi (observe) các thay đổi** trong DOM một cách **bất đồng bộ và hiệu quả** mà không cần polling hay event listeners liên tục.

**3 Observer APIs Quan Trọng:**

```
┌──────────────────────────────────────────────────────────────┐
│                    OBSERVER APIs                              │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1️⃣ INTERSECTION OBSERVER (Quan sát giao điểm)              │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Theo dõi element vào/ra khỏi viewport                 │ │
│  │ • Use cases: Lazy loading, Infinite scroll, Analytics   │ │
│  │ • Thay thế: scroll event + getBoundingClientRect()      │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  2️⃣ RESIZE OBSERVER (Quan sát thay đổi kích thước)          │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Theo dõi thay đổi kích thước của element              │ │
│  │ • Use cases: Responsive components, Charts, Layouts     │ │
│  │ • Thay thế: window.resize event + polling               │ │
│  └─────────────────────────────────────────────────────────┘ │
│                                                               │
│  3️⃣ MUTATION OBSERVER (Quan sát thay đổi DOM)               │
│  ┌─────────────────────────────────────────────────────────┐ │
│  │ • Theo dõi thay đổi DOM tree (add/remove/modify)        │ │
│  │ • Use cases: Auto-init, Debug, Third-party integration  │ │
│  │ • Thay thế: Mutation Events (deprecated)                │ │
│  └─────────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

**🔍 1. INTERSECTION OBSERVER API (Quan Sát Giao Điểm)**

**Khái niệm:**
- API theo dõi khi một element **xuất hiện, biến mất hoặc giao nhau** với viewport (hoặc một element cha)
- Sử dụng cho: Lazy loading images, Infinite scroll, Visibility tracking, Analytics

**Hoạt động:**
1. Tạo observer với callback function
2. Đăng ký các elements cần theo dõi
3. Callback được gọi **bất đồng bộ** khi element vào/ra khỏi vùng quan sát
4. Browser engine tự tối ưu, không cần poll/scroll listener liên tục

**Ưu điểm:**
- ✅ **Hiệu năng cao**: Không block main thread, browser tối ưu internally
- ✅ **API đơn giản**: Dễ sử dụng hơn scroll event + getBoundingClientRect()
- ✅ **Linh hoạt**: Hỗ trợ threshold (ngưỡng %), rootMargin (trigger sớm/muộn)
- ✅ **Giảm layout thrashing**: Không gây reflow/repaint như getBoundingClientRect()

**Nhược điểm:**
- ⚠️ Callback bất đồng bộ → không đảm bảo timing chính xác đến pixel
- ⚠️ Cần polyfill cho browsers rất cũ (IE11-)
- ⚠️ Không phù hợp cho logic cần đồng bộ chính xác

**Code Example (TypeScript + React):**

```typescript
import { useEffect, useRef, useState } from 'react';

// ============================================
// A. LAZY LOADING IMAGES (Tải Ảnh Lười)
// ============================================

// Giải thích: Chỉ tải ảnh khi user scroll đến gần → tiết kiệm bandwidth, tăng tốc độ load trang

function LazyImage({ src, alt }: { src: string; alt: string }) {
  const imgRef = useRef<HTMLImageElement>(null);
  const [imageSrc, setImageSrc] = useState<string>(''); // Ảnh thật chưa load
  const [isLoaded, setIsLoaded] = useState(false);
  
  useEffect(() => {
    // Tạo Intersection Observer
    const observer = new IntersectionObserver(
      (entries) => {
        // entries: Danh sách các elements đang được observe
        entries.forEach((entry) => {
          // entry.isIntersecting: true = element xuất hiện trong viewport
          if (entry.isIntersecting && !isLoaded) {
            console.log('✅ Image vào viewport, bắt đầu load:', src);
            
            // Load ảnh thật
            setImageSrc(src);
            setIsLoaded(true);
            
            // Ngừng observe sau khi load (không cần theo dõi nữa)
            observer.unobserve(entry.target);
          }
        });
      },
      {
        root: null, // null = observe trong viewport (màn hình)
        
        // rootMargin: Mở rộng vùng observe
        // '50px' = trigger khi element còn cách viewport 50px
        // → Preload ảnh trước khi user nhìn thấy (UX mượt hơn)
        rootMargin: '50px',
        
        // threshold: Ngưỡng % element hiển thị để trigger callback
        // 0.1 = trigger khi 10% element visible
        threshold: 0.1
      }
    );
    
    // Bắt đầu observe image element
    if (imgRef.current) {
      observer.observe(imgRef.current);
    }
    
    // Cleanup: Disconnect observer khi component unmount
    return () => {
      observer.disconnect();
    };
  }, [src, isLoaded]);
  
  return (
    <div className="lazy-image-container">
      {!imageSrc ? (
        // Placeholder khi chưa load (skeleton)
        <div className="skeleton-loader" style={{ width: '100%', height: 300, background: '#e0e0e0' }}>
          <span>Đang tải...</span>
        </div>
      ) : (
        <img 
          ref={imgRef}
          src={imageSrc} 
          alt={alt}
          onLoad={() => console.log('✅ Image đã load xong')}
        />
      )}
    </div>
  );
}

// Sử dụng:
function Gallery() {
  const images = [
    'https://example.com/image1.jpg',
    'https://example.com/image2.jpg',
    // ... 100+ images
  ];
  
  return (
    <div className="gallery">
      {images.map((src, i) => (
        <LazyImage key={i} src={src} alt={`Image ${i + 1}`} />
      ))}
    </div>
  );
}
// Kết quả: Chỉ load 5-10 ảnh đầu tiên (trong viewport) thay vì 100+ ảnh cùng lúc
// → Trang load nhanh hơn 10x!

// ============================================
// B. INFINITE SCROLL (Cuộn Vô Hạn)
// ============================================

// Giải thích: Tự động load thêm data khi user scroll đến cuối danh sách

interface Order {
  id: string;
  symbol: string;
  price: number;
}

function InfiniteOrderList() {
  const [orders, setOrders] = useState<Order[]>([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [isLoading, setIsLoading] = useState(false);
  
  // Ref cho sentinel element (phần tử "canh gác" ở cuối list)
  const sentinelRef = useRef<HTMLDivElement>(null);
  
  // Load more data
  const loadMoreOrders = async () => {
    if (isLoading || !hasMore) return;
    
    setIsLoading(true);
    console.log(`📥 Đang load page ${page}...`);
    
    try {
      const res = await fetch(`/api/orders?page=${page}&limit=20`);
      const newOrders = await res.json();
      
      if (newOrders.length === 0) {
        setHasMore(false); // Hết data
        console.log('✅ Đã load hết orders');
      } else {
        setOrders(prev => [...prev, ...newOrders]);
        setPage(prev => prev + 1);
        console.log(`✅ Load thành công ${newOrders.length} orders`);
      }
    } catch (error) {
      console.error('❌ Lỗi load orders:', error);
    } finally {
      setIsLoading(false);
    }
  };
  
  useEffect(() => {
    // Tạo observer cho sentinel element
    const observer = new IntersectionObserver(
      (entries) => {
        const sentinel = entries[0];
        
        // Khi sentinel xuất hiện trong viewport → load more
        if (sentinel.isIntersecting && hasMore && !isLoading) {
          console.log('🔄 Sentinel vào viewport → Load more...');
          loadMoreOrders();
        }
      },
      {
        root: null,
        rootMargin: '100px', // Trigger sớm 100px (load trước khi user scroll đến cuối)
        threshold: 0
      }
    );
    
    if (sentinelRef.current) {
      observer.observe(sentinelRef.current);
    }
    
    return () => observer.disconnect();
  }, [hasMore, isLoading, page]);
  
  // Load initial data
  useEffect(() => {
    loadMoreOrders();
  }, []);
  
  return (
    <div className="order-list">
      <h2>📋 Orders (Infinite Scroll)</h2>
      
      {orders.map((order) => (
        <div key={order.id} className="order-item">
          <span>{order.symbol}</span>
          <span>${order.price}</span>
        </div>
      ))}
      
      {/* Sentinel element: Phần tử "canh gác" ở cuối list */}
      <div ref={sentinelRef} style={{ height: 20 }}>
        {isLoading && <span>⏳ Đang tải thêm...</span>}
        {!hasMore && <span>✅ Đã hiển thị tất cả</span>}
      </div>
    </div>
  );
}
// Cách hoạt động:
// 1. User scroll xuống
// 2. Sentinel element vào viewport
// 3. Observer trigger → loadMoreOrders()
// 4. Fetch data mới, append vào list
// 5. Lặp lại cho đến khi hết data

// ============================================
// C. VISIBILITY TRACKING (Theo Dõi Hiển Thị)
// ============================================

// Giải thích: Track % element hiển thị → gửi analytics
// VD: Biết được section nào user đọc nhiều nhất

function VisibilityTracker({ children, id }: { children: React.ReactNode; id: string }) {
  const elementRef = useRef<HTMLDivElement>(null);
  const [visibilityPercentage, setVisibilityPercentage] = useState(0);
  
  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          // intersectionRatio: Tỷ lệ % element hiển thị (0.0 - 1.0)
          const percentage = Math.round(entry.intersectionRatio * 100);
          setVisibilityPercentage(percentage);
          
          console.log(`👁️ Section "${id}" hiển thị: ${percentage}%`);
          
          // Gửi analytics khi >50% visible
          if (percentage > 50) {
            // analytics.track('section_viewed', { id, percentage });
          }
        });
      },
      {
        root: null,
        threshold: [0, 0.25, 0.5, 0.75, 1.0] // Track ở nhiều mức: 0%, 25%, 50%, 75%, 100%
      }
    );
    
    if (elementRef.current) {
      observer.observe(elementRef.current);
    }
    
    return () => observer.disconnect();
  }, [id]);
  
  return (
    <div ref={elementRef} className="tracked-section">
      <div className="visibility-indicator">
        Hiển thị: {visibilityPercentage}%
      </div>
      {children}
    </div>
  );
}

// Sử dụng:
function Article() {
  return (
    <article>
      <VisibilityTracker id="section-1">
        <h2>Phần 1: Giới thiệu</h2>
        <p>Nội dung...</p>
      </VisibilityTracker>
      
      <VisibilityTracker id="section-2">
        <h2>Phần 2: Phát triển</h2>
        <p>Nội dung...</p>
      </VisibilityTracker>
    </article>
  );
}
```

**Best Practices (Thực Hành Tốt):**

1. **✅ Dùng `rootMargin` để preload sớm**
   ```typescript
   rootMargin: '50px' // Load trước khi vào viewport 50px → UX mượt
   ```

2. **✅ Unobserve sau khi xử lý xong**
   ```typescript
   if (entry.isIntersecting) {
     // Xử lý...
     observer.unobserve(entry.target); // Ngừng observe → tiết kiệm tài nguyên
   }
   ```

3. **✅ Dùng multiple thresholds cho tracking chi tiết**
   ```typescript
   threshold: [0, 0.25, 0.5, 0.75, 1] // Track ở 5 mức độ
   ```

4. **✅ Kết hợp với native lazy loading**
   ```html
   <img src="image.jpg" loading="lazy" /> <!-- Browser native lazy load -->
   ```

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Dùng scroll event + getBoundingClientRect() (chậm, gây layout thrashing)
window.addEventListener('scroll', () => {
  images.forEach((img) => {
    const rect = img.getBoundingClientRect(); // ❌ Trigger reflow mỗi scroll
    if (rect.top < window.innerHeight) {
      // Load image...
    }
  });
});

// ✅ SỬA: Dùng IntersectionObserver (tối ưu, không block main thread)
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      // Load image...
    }
  });
});
images.forEach((img) => observer.observe(img));

// ❌ LỖI 2: Quên disconnect observer → memory leak
useEffect(() => {
  const observer = new IntersectionObserver(callback);
  observer.observe(element);
  // ❌ Thiếu cleanup
}, []);

// ✅ SỬA: Luôn cleanup
useEffect(() => {
  const observer = new IntersectionObserver(callback);
  observer.observe(element);
  
  return () => {
    observer.disconnect(); // ✅ Cleanup khi unmount
  };
}, []);
```

---

**🔍 2. RESIZE OBSERVER API (Quan Sát Thay Đổi Kích Thước)**
- Hoạt động: Đăng ký callback được gọi bất đồng bộ khi target element vào/ra khỏi vùng quan sát; engine tối ưu không cần poll/scroll listener liên tục.
- Ưu điểm: Hiệu năng cao (không block main thread), API đơn giản, hỗ trợ threshold linh hoạt; giảm layout thrashing so với getBoundingClientRect() trong scroll.
- Nhược điểm: Callback bất đồng bộ nên không đảm bảo timing chính xác pixel; cần polyfill cho trình duyệt rất cũ; không phù hợp cho logic cần sync chính xác.

Chú thích: Dùng `rootMargin` để trigger sớm/muộn (ví dụ: lazy load trước khi vào viewport); `threshold` xác định % giao nhau để fire callback.

**Code Example:**

```ts
// Lazy load images khi vào viewport
const images = document.querySelectorAll('img[data-src]');

const imageObserver = new IntersectionObserver(
  (entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const img = entry.target as HTMLImageElement;
        // Load ảnh thật
        img.src = img.dataset.src!;
        img.removeAttribute('data-src');
        // Ngừng observe sau khi load
        observer.unobserve(img);
      }
    });
  },
  {
    root: null, // viewport
    rootMargin: '50px', // trigger 50px trước khi vào viewport
    threshold: 0.1, // 10% visible là trigger
  }
);

images.forEach((img) => imageObserver.observe(img));

// Infinite scroll example
const sentinel = document.querySelector('#load-more-trigger');
const loadMoreObserver = new IntersectionObserver((entries) => {
  if (entries[0].isIntersecting) {
    loadMoreContent(); // fetch thêm data
  }
});
if (sentinel) loadMoreObserver.observe(sentinel);

// Cleanup
// loadMoreObserver.disconnect();
```

**Best Practices:**

- Dùng `rootMargin` để preload sớm cho UX mượt
- Unobserve sau khi xử lý xong (tránh callback thừa)
- Dùng `threshold: [0, 0.25, 0.5, 0.75, 1]` nếu cần theo dõi nhiều mức độ
- Kết hợp với `loading="lazy"` native cho ảnh

**Mistakes:**

```ts
// ❌ Dùng scroll listener + getBoundingClientRect → chậm, layout thrashing
window.addEventListener('scroll', () => {
  images.forEach((img) => {
    const rect = img.getBoundingClientRect();
    if (rect.top < window.innerHeight) {
      // load image
    }
  });
});

// ✅ Dùng IntersectionObserver
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      // load image
    }
  });
});
```

---

**🔍 2. RESIZE OBSERVER API (Quan Sát Thay Đổi Kích Thước)**

**Khái niệm:**
- API theo dõi **thay đổi kích thước của element** (width, height)
- Sử dụng cho: Responsive components, Charts auto-resize, Dynamic layouts

**Hoạt động:**
1. Callback được gọi khi **content box hoặc border box** của element thay đổi
2. Chạy **trước paint** để tránh visual flash
3. Hỗ trợ nhiều box model: `content-box`, `border-box`, `device-pixel-content-box`

**Ưu điểm:**
- ✅ **Hiệu năng tốt hơn** window.resize + polling
- ✅ **Phát hiện resize từ bất kỳ nguồn**: CSS, JavaScript, user action
- ✅ **Per-element tracking**: Theo dõi từng element riêng lẻ (không phải toàn viewport)
- ✅ **Không cần media queries**: Component tự responsive

**Nhược điểm:**
- ⚠️ Callback có thể fire liên tục khi animate
- ⚠️ Cần debounce cho logic nặng
- ⚠️ Có thể gây **infinite loop** nếu callback thay đổi size của chính element đang observe

**Code Example (TypeScript + React):**

```typescript
import { useEffect, useRef, useState } from 'react';

// ============================================
// A. RESPONSIVE COMPONENT (Component Tự Responsive)
// ============================================

// Giải thích: Component tự điều chỉnh layout khi kích thước thay đổi
// Không cần media queries → component portable, reusable

function ResponsiveCard() {
  const cardRef = useRef<HTMLDivElement>(null);
  const [layout, setLayout] = useState<'horizontal' | 'vertical'>('horizontal');
  const [dimensions, setDimensions] = useState({ width: 0, height: 0 });
  
  useEffect(() => {
    // Tạo Resize Observer
    const resizeObserver = new ResizeObserver((entries) => {
      // entries: Danh sách các elements đang observe
      for (const entry of entries) {
        // contentRect: Kích thước content box của element
        const { width, height } = entry.contentRect;
        
        console.log(`📏 Card resize: ${width}x${height}`);
        setDimensions({ width, height });
        
        // Tự động chuyển layout dựa vào width
        if (width < 500) {
          setLayout('vertical');   // Mobile: stack vertically
          console.log('→ Chuyển sang vertical layout');
        } else {
          setLayout('horizontal'); // Desktop: side by side
          console.log('→ Chuyển sang horizontal layout');
        }
      }
    });
    
    // Observe card element
    if (cardRef.current) {
      resizeObserver.observe(cardRef.current);
    }
    
    // Cleanup khi unmount
    return () => {
      resizeObserver.disconnect();
    };
  }, []);
  
  return (
    <div 
      ref={cardRef}
      className={`card ${layout}`}
      style={{
        display: 'flex',
        flexDirection: layout === 'vertical' ? 'column' : 'row',
        gap: '1rem',
        padding: '1rem',
        border: '1px solid #ccc'
      }}
    >
      <div className="card-image">
        <img src="/image.jpg" alt="Card" style={{ width: '100%' }} />
      </div>
      <div className="card-content">
        <h3>Tiêu đề</h3>
        <p>Nội dung...</p>
        <p className="dimensions">
          📐 Kích thước: {dimensions.width.toFixed(0)}px × {dimensions.height.toFixed(0)}px
        </p>
      </div>
    </div>
  );
}
// Kết quả: Component tự adapt layout khi container resize
// → Không cần CSS media queries → Portable, reusable

// ============================================
// B. CHART AUTO-RESIZE (Biểu Đồ Tự Scale)
// ============================================

// Giải thích: Chart tự động scale khi container resize
// VD: User mở/đóng sidebar → chart tự fit container mới

function TradingChart() {
  const containerRef = useRef<HTMLDivElement>(null);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const chartInstance = useRef<any>(null); // Chart.js instance
  
  useEffect(() => {
    // Khởi tạo chart
    if (canvasRef.current) {
      const ctx = canvasRef.current.getContext('2d');
      // chartInstance.current = new Chart(ctx, { ... });
    }
    
    // Observe container (KHÔNG observe canvas trực tiếp)
    // Tại sao? Nếu observe canvas → canvas resize → observer fire → canvas resize lại → loop!
    const resizeObserver = new ResizeObserver((entries) => {
      const { width, height } = entries[0].contentRect;
      
      console.log(`📊 Chart container resize: ${width}x${height}`);
      
      // Resize chart để fit container
      if (chartInstance.current && canvasRef.current) {
        canvasRef.current.width = width;
        canvasRef.current.height = height;
        
        // Update chart dimensions
        chartInstance.current.resize(width, height);
        console.log('✅ Chart đã resize');
      }
    });
    
    // Observe parent container (KHÔNG phải canvas)
    if (containerRef.current) {
      resizeObserver.observe(containerRef.current);
    }
    
    return () => {
      resizeObserver.disconnect();
      // chartInstance.current?.destroy();
    };
  }, []);
  
  return (
    <div 
      ref={containerRef}
      className="chart-container"
      style={{ width: '100%', height: '400px', position: 'relative' }}
    >
      <canvas ref={canvasRef} />
    </div>
  );
}

// ============================================
// C. TEXTAREA AUTO-HEIGHT (Textarea Tự Điều Chỉnh Chiều Cao)
// ============================================

// Giải thích: Textarea tự tăng/giảm height khi user type
// Không cần fixed height → UX tốt hơn

function AutoExpandTextarea() {
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [height, setHeight] = useState(60); // Min height
  
  useEffect(() => {
    const resizeObserver = new ResizeObserver((entries) => {
      const { height } = entries[0].contentRect;
      
      // Chỉ log khi height thay đổi đáng kể (tránh spam)
      if (Math.abs(height - entries[0].target.clientHeight) > 5) {
        console.log(`✏️ Textarea height: ${height}px`);
        setHeight(height);
      }
    });
    
    if (textareaRef.current) {
      // Observe textarea itself
      resizeObserver.observe(textareaRef.current);
    }
    
    return () => resizeObserver.disconnect();
  }, []);
  
  return (
    <div>
      <textarea 
        ref={textareaRef}
        placeholder="Type something..."
        style={{
          width: '100%',
          minHeight: '60px',
          resize: 'vertical', // Cho phép user resize manually
          padding: '0.5rem'
        }}
      />
      <p className="info">Current height: {height}px</p>
    </div>
  );
}
```

**Best Practices (Thực Hành Tốt):**

1. **✅ Debounce logic nặng với requestAnimationFrame**
   ```typescript
   const resizeObserver = new ResizeObserver((entries) => {
     requestAnimationFrame(() => {
       // Logic nặng (recalculate layout, re-render chart, etc.)
     });
   });
   ```

2. **✅ Observe parent container, KHÔNG phải element sẽ resize**
   ```typescript
   // ❌ SAI: Observe canvas trực tiếp
   resizeObserver.observe(canvas);
   
   // ✅ ĐÚNG: Observe parent container
   resizeObserver.observe(canvas.parentElement);
   ```

3. **✅ Disconnect khi component unmount**
   ```typescript
   useEffect(() => {
     const observer = new ResizeObserver(callback);
     observer.observe(element);
     
     return () => observer.disconnect(); // ✅ Cleanup
   }, []);
   ```

4. **✅ Dùng cho responsive components (thay thế media queries)**
   - Media queries: Dựa vào viewport size
   - ResizeObserver: Dựa vào component size → Reusable hơn

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Infinite Loop - Resize chính element đang observe
const box = document.querySelector('.box') as HTMLElement;

const badObserver = new ResizeObserver(() => {
  // ❌ Thay đổi size của chính element đang observe
  box.style.width = (box.offsetWidth + 10) + 'px';
  // → Observer fire → tăng width → observer fire lại → loop vô hạn!
});
badObserver.observe(box);

// ✅ SỬA: Dùng flag để ngăn loop hoặc observe parent
let isResizing = false;

const goodObserver = new ResizeObserver(() => {
  if (!isResizing) {
    isResizing = true;
    
    // Logic resize
    requestAnimationFrame(() => {
      box.style.width = (box.offsetWidth + 10) + 'px';
      isResizing = false; // Reset flag
    });
  }
});
goodObserver.observe(box);

// ❌ LỖI 2: Không debounce logic nặng → Chậm
const heavyObserver = new ResizeObserver((entries) => {
  // ❌ Logic nặng chạy mỗi lần resize (có thể fire rất nhiều lần)
  entries.forEach((entry) => {
    recalculateComplexLayout(); // Expensive operation
    rerenderChart(); // Expensive operation
  });
});

// ✅ SỬA: Debounce với requestAnimationFrame
const optimizedObserver = new ResizeObserver((entries) => {
  requestAnimationFrame(() => {
    // Logic nặng chỉ chạy 1 lần per frame
    entries.forEach((entry) => {
      recalculateComplexLayout();
      rerenderChart();
    });
  });
});

// ❌ LỖI 3: Quên disconnect → Memory leak
function MyComponent() {
  useEffect(() => {
    const observer = new ResizeObserver(callback);
    observer.observe(element);
    // ❌ Thiếu cleanup → observer vẫn chạy sau unmount
  }, []);
}

// ✅ SỬA: Luôn cleanup
function MyComponent() {
  useEffect(() => {
    const observer = new ResizeObserver(callback);
    observer.observe(element);
    
    return () => observer.disconnect(); // ✅ Cleanup
  }, []);
}
```

---

**🔍 3. MUTATION OBSERVER API (Quan Sát Thay Đổi DOM)**

**Khái niệm:**
- API theo dõi **thay đổi DOM tree**: thêm/xóa nodes, thay đổi attributes, thay đổi text content
- Thay thế cho **Mutation Events** (deprecated - đã lỗi thời)
- Sử dụng cho: Auto-init new elements, Debug DOM changes, Polyfill custom elements, Third-party integration

**Hoạt động:**
1. Callback được gọi **bất đồng bộ (microtask)** khi có mutation khớp config
2. Browser **gom nhóm mutations** để giảm số lần gọi callback (batch processing)
3. Hỗ trợ filter theo loại mutation: `childList`, `attributes`, `characterData`

**Ưu điểm:**
- ✅ **Hiệu năng tốt hơn** Mutation Events (deprecated)
- ✅ **Linh hoạt**: Filter chính xác loại mutation cần quan tâm
- ✅ **Observe subtree**: Theo dõi toàn bộ cây con (descendants)
- ✅ **Track old values**: Lưu giá trị cũ của attributes/text

**Nhược điểm:**
- ⚠️ Callback bất đồng bộ → không real-time
- ⚠️ Performance issue nếu observe toàn `document.body` với `subtree: true`
- ⚠️ Logic phức tạp khi xử lý nhiều mutations cùng lúc

**Code Example (TypeScript + React):**

```typescript
import { useEffect, useRef } from 'react';

// ============================================
// A. THEME SWITCHER TRACKING (Theo Dõi Đổi Theme)
// ============================================

// Giải thích: Theo dõi attribute data-theme thay đổi
// → Update components khi user switch theme

function ThemeAwareComponent() {
  useEffect(() => {
    const root = document.documentElement; // <html> element
    
    // Tạo Mutation Observer
    const themeObserver = new MutationObserver((mutations) => {
      // mutations: Danh sách các thay đổi DOM
      mutations.forEach((mutation) => {
        // Chỉ quan tâm khi attribute thay đổi
        if (mutation.type === 'attributes' && mutation.attributeName === 'data-theme') {
          const newTheme = root.getAttribute('data-theme');
          const oldTheme = mutation.oldValue;
          
          console.log(`🎨 Theme changed: ${oldTheme} → ${newTheme}`);
          
          // Update chart colors, reload styles, etc.
          updateComponentTheme(newTheme);
        }
      });
    });
    
    // Observe <html> element
    themeObserver.observe(root, {
      attributes: true,              // Theo dõi attributes thay đổi
      attributeFilter: ['data-theme'], // Chỉ quan tâm data-theme (ignore các attributes khác)
      attributeOldValue: true        // Lưu giá trị cũ (để so sánh)
    });
    
    return () => themeObserver.disconnect();
  }, []);
  
  return <div>Theme-aware content...</div>;
}

function updateComponentTheme(theme: string | null) {
  // Update chart colors
  // Reload CSS variables
  // Re-render components with new theme
}

// ============================================
// B. AUTO-INIT NEW ELEMENTS (Tự Động Khởi Tạo Elements Mới)
// ============================================

// Giải thích: Tự động init tooltips, modals cho elements mới được thêm vào DOM
// Use case: SPA with dynamic content, third-party libraries add elements

function AutoInitializer() {
  useEffect(() => {
    const container = document.querySelector('#dynamic-content') as HTMLElement;
    
    const nodeObserver = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        // Chỉ quan tâm nodes được thêm vào
        mutation.addedNodes.forEach((node) => {
          // Kiểm tra node type (chỉ xử lý element nodes)
          if (node.nodeType === Node.ELEMENT_NODE) {
            const element = node as HTMLElement;
            
            // Auto-init tooltips
            if (element.matches('[data-tooltip]')) {
              console.log('✨ Init tooltip cho:', element);
              initTooltip(element);
            }
            
            // Auto-init modals
            if (element.matches('[data-modal]')) {
              console.log('✨ Init modal cho:', element);
              initModal(element);
            }
            
            // Auto-init date pickers
            if (element.matches('.date-picker')) {
              console.log('✨ Init date picker cho:', element);
              initDatePicker(element);
            }
          }
        });
      });
    });
    
    nodeObserver.observe(container, {
      childList: true, // Theo dõi thêm/xóa node con
      subtree: true    // Theo dõi cả các node con sâu hơn (descendants)
    });
    
    return () => nodeObserver.disconnect();
  }, []);
  
  return <div id="dynamic-content">Content will be added here...</div>;
}

function initTooltip(element: HTMLElement) {
  // Init tooltip library...
}

function initModal(element: HTMLElement) {
  // Init modal library...
}

function initDatePicker(element: HTMLElement) {
  // Init date picker library...
}

// ============================================
// C. DEBUG DOM CHANGES (Debug Thay Đổi DOM)
// ============================================

// Giải thích: Track tất cả thay đổi DOM để debug
// Use case: Phát hiện third-party library nào đang modify DOM

function DOMDebugger() {
  useEffect(() => {
    const debugObserver = new MutationObserver((mutations) => {
      console.group(`🔍 ${mutations.length} DOM mutations detected`);
      
      mutations.forEach((mutation, index) => {
        console.log(`\n[${index + 1}] Type: ${mutation.type}`);
        
        if (mutation.type === 'childList') {
          // Nodes được thêm
          if (mutation.addedNodes.length > 0) {
            console.log('  ➕ Added nodes:', Array.from(mutation.addedNodes));
          }
          
          // Nodes bị xóa
          if (mutation.removedNodes.length > 0) {
            console.log('  ➖ Removed nodes:', Array.from(mutation.removedNodes));
          }
        }
        
        if (mutation.type === 'attributes') {
          console.log('  🏷️ Attribute changed:', mutation.attributeName);
          console.log('     Old value:', mutation.oldValue);
          console.log('     New value:', (mutation.target as Element).getAttribute(mutation.attributeName!));
        }
        
        if (mutation.type === 'characterData') {
          console.log('  📝 Text changed');
          console.log('     Old:', mutation.oldValue);
          console.log('     New:', mutation.target.textContent);
        }
      });
      
      console.groupEnd();
    });
    
    // Observe toàn bộ document (CHỈ cho debug, KHÔNG dùng production)
    debugObserver.observe(document.body, {
      childList: true,         // Track add/remove nodes
      attributes: true,        // Track attribute changes
      characterData: true,     // Track text changes
      subtree: true,           // Track all descendants
      attributeOldValue: true, // Lưu giá trị cũ
      characterDataOldValue: true
    });
    
    return () => debugObserver.disconnect();
  }, []);
  
  return <div>DOM Debugger active...</div>;
}
```

**Best Practices (Thực Hành Tốt):**

1. **✅ Filter chính xác loại mutation**
   ```typescript
   observer.observe(element, {
     attributes: true,
     attributeFilter: ['data-state', 'aria-expanded'], // Chỉ 2 attributes này
     // KHÔNG: attributes: true (quan sát TẤT CẢ attributes)
   });
   ```

2. **✅ Dùng `attributeFilter` để giảm noise**
   ```typescript
   // ❌ Quan sát tất cả attributes → callback fire rất nhiều
   { attributes: true }
   
   // ✅ Chỉ quan sát 1 attribute cụ thể
   { attributes: true, attributeFilter: ['data-theme'] }
   ```

3. **✅ Disconnect khi không cần**
   ```typescript
   useEffect(() => {
     const observer = new MutationObserver(callback);
     observer.observe(element, config);
     
     return () => observer.disconnect(); // ✅ Cleanup
   }, []);
   ```

4. **✅ Debounce/batch xử lý mutations**
   ```typescript
   let mutationQueue: MutationRecord[] = [];
   let timeoutId: number;
   
   const observer = new MutationObserver((mutations) => {
     mutationQueue.push(...mutations);
     
     clearTimeout(timeoutId);
     timeoutId = setTimeout(() => {
       // Xử lý tất cả mutations cùng lúc
       processMutations(mutationQueue);
       mutationQueue = [];
     }, 100);
   });
   ```

**Common Mistakes (Lỗi Thường Gặp):**

```typescript
// ❌ LỖI 1: Observe toàn document với subtree → Rất chậm
const badObserver = new MutationObserver((mutations) => {
  // ❌ Logic nặng chạy mỗi khi DOM thay đổi (rất nhiều lần)
  mutations.forEach((mutation) => {
    expensiveOperation();
  });
});

badObserver.observe(document.body, {
  childList: true,
  subtree: true,  // ❌ Quan sát TẤT CẢ descendants
  attributes: true // ❌ Quan sát TẤT CẢ attributes
});
// → Callback fire hàng trăm lần/giây → App chậm

// ✅ SỬA: Scope nhỏ + Filter chính xác
const goodObserver = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    targetedOperation();
  });
});

const specificContainer = document.querySelector('#app-content');
goodObserver.observe(specificContainer, {
  childList: true,
  subtree: false, // ✅ Chỉ direct children
  attributeFilter: ['data-state'] // ✅ Chỉ 1 attribute
});

// ❌ LỖI 2: Quên disconnect → Memory leak
function Component() {
  useEffect(() => {
    const observer = new MutationObserver(callback);
    observer.observe(document.body, config);
    // ❌ Thiếu cleanup
  }, []);
}

// ✅ SỬA: Luôn disconnect
function Component() {
  useEffect(() => {
    const observer = new MutationObserver(callback);
    observer.observe(document.body, config);
    
    return () => observer.disconnect(); // ✅ Cleanup
  }, []);
}

// ❌ LỖI 3: Logic đồng bộ nặng trong callback
const syncObserver = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    // ❌ Sync operations block main thread
    for (let i = 0; i < 10000; i++) {
      doHeavyCalculation();
    }
  });
});

// ✅ SỬA: Batch + async processing
const asyncObserver = new MutationObserver((mutations) => {
  // Gom mutations
  const addedElements = mutations
    .flatMap(m => Array.from(m.addedNodes))
    .filter(n => n.nodeType === Node.ELEMENT_NODE);
  
  // Xử lý async
  queueMicrotask(() => {
    processElementsBatch(addedElements);
  });
});
```

---

**📊 So Sánh 3 Observer APIs:**

```
┌─────────────────────┬──────────────────────┬─────────────────────┬─────────────────────┐
│ Tiêu Chí            │ Intersection         │ Resize              │ Mutation            │
├─────────────────────┼──────────────────────┼─────────────────────┼─────────────────────┤
│ Theo dõi            │ Giao điểm viewport   │ Kích thước element  │ Thay đổi DOM        │
│ Use Cases           │ Lazy load, Infinite  │ Responsive, Charts  │ Auto-init, Debug    │
│                     │ scroll, Analytics    │ Layouts             │ Polyfills           │
│ Performance         │ ⭐⭐⭐⭐⭐            │ ⭐⭐⭐⭐⭐           │ ⭐⭐⭐⭐ (cẩn thận)  │
│ Complexity          │ Dễ                   │ Trung bình          │ Khó (nhiều edge     │
│                     │                      │                     │ cases)              │
│ Risk                │ Thấp                 │ Loop nếu sai cách   │ Performance nếu     │
│                     │                      │                     │ observe rộng        │
│ Browser Support     │ Modern (IE11+)       │ Modern (IE11+)      │ Modern (IE11+)      │
└─────────────────────┴──────────────────────┴─────────────────────┴─────────────────────┘
```

**🎯 Khi Nào Dùng Observer Nào?**

- **Intersection Observer**: Lazy loading, Infinite scroll, Visibility tracking
- **Resize Observer**: Responsive components, Charts, Dynamic layouts
- **Mutation Observer**: Auto-init elements, Debug DOM, Third-party integration

**✅ Tổng Kết:**

Observer APIs là công cụ mạnh mẽ để theo dõi thay đổi DOM một cách hiệu quả. Key takeaways:

1. **Hiệu năng tốt hơn** event listeners truyền thống
2. **Bất đồng bộ** → không block main thread
3. **Cần cleanup** đúng cách → tránh memory leak
4. **Filter chính xác** → tránh callback fire thừa
5. **Debounce logic nặng** → tránh performance issue

---
</details>