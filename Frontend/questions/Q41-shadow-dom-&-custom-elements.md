# 🎭 Q41: Shadow DOM & Custom Elements

<details>
<summary><span style="font-size:1.25em;font-weight:bold;">🎭 Q41: Shadow DOM & Custom Elements</span></summary>


**Trả lời:**

- Shadow DOM: cô lập DOM/CSS; Custom Elements: định nghĩa thẻ mới

**Code Example:**

```ts
class MyBadge extends HTMLElement {
  shadow = this.attachShadow({ mode: 'open' });
  connectedCallback() {
    this.shadow.innerHTML = `
      <style>:host{display:inline-block;padding:2px 6px;background:#eef;border-radius:12px}</style>
      <slot></slot>
    `;
  }
}
customElements.define('my-badge', MyBadge);
```

**Best Practices:**

- Dùng `:host` và CSS parts/slots; tránh rò rỉ style global

**Mistakes:**

```ts
// ❌ Trông chờ CSS global tác động vào shadow tree
```

</details>