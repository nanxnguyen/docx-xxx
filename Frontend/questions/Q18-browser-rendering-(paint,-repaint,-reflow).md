# 🎨 Q18: Browser Rendering (Paint, Repaint, Reflow)

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (1-2 phút):**

**"Reflow (tính toán lại bố cục) tốn kém hơn Repaint (vẽ lại). Tối ưu bằng cách gộp thay đổi DOM, dùng transform/opacity.**

**🎨 Quy Trình Render (Đường Ống Render Quan Trọng):**
1. **Xây Dựng DOM**: Phân tích HTML → cây DOM.
2. **Xây Dựng CSSOM**: Phân tích CSS → cây CSSOM.
3. **Cây Render**: Kết hợp DOM + CSSOM → chỉ các phần tử hiển thị.
4. **Layout (Reflow)**: Tính toán kích thước/vị trí của mỗi phần tử.
5. **Paint (Vẽ)**: Vẽ pixels (màu sắc, hình ảnh, viền, bóng).
6. **Composite (Tổng hợp)**: Kết hợp các lớp → màn hình cuối cùng.

**🔑 Paint vs Repaint vs Reflow:**

| Thao Tác | Kích Hoạt | Chi Phí | Ví Dụ |
|----------|-----------|---------|-------|
| **Paint** | Render lần đầu | Trung bình | Tải trang lần đầu |
| **Repaint** | Thay đổi hình ảnh (không layout) | Thấp | `color`, `background`, `visibility` |
| **Reflow** | Thay đổi bố cục | **Cao** | `width`, `height`, `margin`, `padding`, `display` |

**⚡ Kích Hoạt Reflow (Tốn Kém!):**
- Thao tác DOM: Thêm/xóa phần tử, thay đổi nội dung.
- Thay đổi CSS: `width`, `height`, `margin`, `padding`, `border`, `display`, `position`.
- Đọc thuộc tính layout: `offsetWidth`, `offsetHeight`, `clientWidth`, `scrollTop` → buộc reflow đồng bộ!
- Thay đổi kích thước cửa sổ, thay đổi font, thay đổi class.

**♻️ Kích Hoạt Repaint (Rẻ Hơn):**
- Thuộc tính hình ảnh: `color`, `background-color`, `visibility`, `outline`, `box-shadow`.
- Không thay đổi layout → chỉ vẽ lại pixels.

**🚀 Kỹ Thuật Tối Ưu:**
1. **Gộp Thay Đổi DOM**:
   ```js
   // ❌ Tệ: 3 reflows
   el.style.width = '100px';
   el.style.height = '100px';
   el.style.margin = '10px';
   
   // ✅ Tốt: 1 reflow
   el.style.cssText = 'width: 100px; height: 100px; margin: 10px;';
   // Hoặc dùng class
   el.className = 'new-style';
   ```

2. **Dùng transform/opacity (Chỉ Composite):**
   ```js
   // ❌ Tệ: Reflow + Repaint
   el.style.left = '100px'; // Thay đổi vị trí → reflow
   
   // ✅ Tốt: Chỉ composite (tăng tốc GPU)
   el.style.transform = 'translateX(100px)'; // Không reflow/repaint!
   ```

3. **Tránh Đọc Thuộc Tính Layout Trong Vòng Lặp**:
   ```js
   // ❌ Tệ: Buộc reflow mỗi vòng lặp
   for (let i = 0; i < 100; i++) {
     el.style.width = el.offsetWidth + 10 + 'px'; // Đọc + ghi → reflow!
   }
   
   // ✅ Tốt: Đọc một lần, ghi một lần
   const width = el.offsetWidth;
   el.style.width = width + 1000 + 'px';
   ```

4. **requestAnimationFrame Cho Animation:**
   ```js
   function animate() {
     el.style.transform = `translateX(${x}px)`;
     x += 1;
     requestAnimationFrame(animate); // Sync với browser refresh (60fps)
   }
   ```

5. **Virtualize Long Lists**: Chỉ render visible items (react-window, react-virtualized).

**⚠️ Common Mistakes:**
- Changing styles trong loop → multiple reflows.
- Reading layout properties (offsetWidth) sau write → force synchronous reflow.
- Animating `width/height/top/left` thay vì `transform`.

**💡 Senior Insights:**
- **Composite Layers**: `transform`, `opacity` run on compositor thread (GPU) → không block main thread.
- **will-change**: `will-change: transform` hint browser tạo separate layer → optimize animations.
- **Layout Thrashing**: Read → Write → Read → Write pattern → force multiple reflows. Dùng FastDOM library.
- **DevTools**: Chrome DevTools → Performance tab → see reflow/repaint events.
- **CSS Containment**: `contain: layout` isolate element → reflow không spread to parent.

---

**⚡ Quick Summary:**
> Reflow = recalculate layout (expensive). Repaint = redraw pixels. Paint = first render

**💡 Ghi Nhớ:**
- 🎨 **Paint**: First render lên screen
- 🔄 **Reflow**: Recalculate layout (DOM thay đổi size/position)
- 🖌️ **Repaint**: Redraw pixels (color, visibility change)
- ⚡ **Optimize**: Batch DOM changes, use transform/opacity, requestAnimationFrame

**Trả lời:**

- **Paint**: Vẽ pixels lên screen
- **Repaint**: Vẽ lại elements với same layout
- **Reflow**: Recalculate layout và repaint
- **Hoạt động**: Reflow → Repaint → Composite
- **Ưu điểm**: Optimized rendering, smooth animations
- **Nhược điểm**: Reflow expensive, có thể gây performance issues

**Code Example:**

```typescript
// Reflow triggers
function triggerReflow(): void {
  const element = document.getElementById('myElement');
  if (element) {
    // These trigger reflow
    element.style.width = '200px';
    element.style.height = '100px';
    element.style.margin = '10px';
    element.style.padding = '5px';

    // Reading layout properties also triggers reflow
    const width = element.offsetWidth;
    const height = element.offsetHeight;
  }
}

// Optimized - batch DOM changes
function optimizedReflow(): void {
  const element = document.getElementById('myElement');
  if (element) {
    // Batch all changes
    element.style.cssText =
      'width: 200px; height: 100px; margin: 10px; padding: 5px;';

    // Or use class
    element.className = 'new-style';
  }
}

// Use transform for animations (tránh reflow)
function animateWithTransform(): void {
  const element = document.getElementById('myElement');
  if (element) {
    // Transform doesn't trigger reflow
    element.style.transform = 'translateX(100px)';
    element.style.transition = 'transform 0.3s ease';
  }
}
```

**Best Practices:**

- Tránh reflow khi có thể
- Sử dụng transform cho animations
- Sử dụng requestAnimationFrame
- Batch DOM changes

