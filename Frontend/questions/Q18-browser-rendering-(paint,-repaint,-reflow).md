# 🎨 Q18: Browser Rendering (Paint, Repaint, Reflow)




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

