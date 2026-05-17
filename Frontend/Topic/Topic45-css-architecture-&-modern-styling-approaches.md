# 🎨 CSS Architecture & Modern Styling Approaches

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"CSS approaches: BEM (naming convention), CSS Modules (scoped), CSS-in-JS (dynamic, colocated), Tailwind (utility-first). Chọn based on: team size, dynamic needs, performance priority. Critical CSS = above-fold styles inline."**

**🔑 4 Modern Approaches:**

**1. BEM (Block Element Modifier):**

- **Naming**: `.block__element--modifier`
- Ưu: Clear, không conflicts, team-friendly
- Nhược: Verbose (dài), manually maintain
- Use case: Large teams, design systems

**2. CSS Modules:**

- **Scoped**: `import styles from './Button.module.css'`
- Ưu: Auto-scoped, no naming conflicts, works with existing CSS
- Nhược: Không dynamic (can't change based on props easily)
- Use case: Component libraries, gradual migration

**3. CSS-in-JS (Styled Components, Emotion):**

- **Syntax**: `const Button = styled.button\`color: ${props => props.color}\``
- Ưu: **Dynamic**, colocated, scoped, TypeScript support
- Nhược: Runtime overhead (~10-20ms), bundle size
- Use case: Highly dynamic UIs, design tokens

**4. Tailwind CSS:**

- **Utility-first**: `className="bg-blue-500 hover:bg-blue-700 px-4 py-2"`
- Ưu: **Fast development**, small final bundle (PurgeCSS), consistent design
- Nhược: HTML "bloat", learning curve (utility names)
- Use case: Rapid prototyping, startups, landing pages

**🔑 Critical CSS:**

- **Inline above-fold CSS** trong `<head>` để render nhanh
- Defer non-critical CSS (`<link rel="preload" as="style">`)
- Tools: Critters (Next.js), Critical (npm package)
- **FCP improvement**: ~30-50% faster First Contentful Paint

**⚠️ Lỗi Thường Gặp:**

- CSS-in-JS trong SSR không extract styles → FOUC (Flash of Unstyled Content)
- Tailwind không purge → 300KB+ CSS bundle
- BEM không consistent naming → mất ưu điểm
- Global CSS specificity wars → `!important` hell

**💡 Kiến Thức Senior:**

- **Zero-runtime CSS-in-JS**: Linaria, Vanilla Extract - extract CSS build time
- **Atomic CSS**: Tailwind, StyleX (Meta) - share utility classes
- **Design tokens**: CSS variables cho themes, dùng với Tailwind/CSS-in-JS
- **Container queries**: Style based on parent size (không phải viewport)

**❓ Câu Hỏi:**

So sánh các phương pháp styling hiện đại: CSS-in-JS (Styled Components, Emotion), Tailwind CSS, CSS Modules, BEM methodology. Khi nào nên dùng approach nào? Critical CSS là gì?

---

## **📊 CSS ARCHITECTURE LANDSCAPE**

```
┌─────────────────────────────────────────────────────────────┐
│           MODERN CSS APPROACHES (2024)                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  🏗️ TRADITIONAL APPROACHES                                  │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  • BEM (Block Element Modifier)                       │ │
│  │    .block__element--modifier                          │ │
│  │    ✅ Clear naming, ❌ Verbose                         │ │
│  │                                                       │ │
│  │  • SMACSS (Scalable Modular Architecture)            │ │
│  │    Base → Layout → Module → State → Theme            │ │
│  │    ✅ Organized, ❌ Learning curve                    │ │
│  └───────────────────────────────────────────────────────┘ │
│                                                             │
│  🔬 MODERN APPROACHES                                       │
│  ┌───────────────────────────────────────────────────────┐ │
│  │  • CSS Modules                                        │ │
│  │    import styles from './Button.module.css'           │ │
│  │    ✅ Scoped, ✅ No naming conflicts                  │ │
│  │                                                       │ │
│  │  • CSS-in-JS (Styled Components, Emotion)            │ │
│  │    const Button = styled.button`...`                  │ │
│  │    ✅ Dynamic, ✅ Colocated, ❌ Runtime overhead      │ │
│  │                                                       │ │
│  │  • Utility-First (Tailwind CSS)                      │ │
│  │    className="bg-blue-500 hover:bg-blue-700"         │ │
│  │    ✅ Fast dev, ✅ Small bundle, ❌ HTML bloat       │ │
│  └───────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## **1️⃣ BEM METHODOLOGY (Block Element Modifier)**

```css
/* ===================================================
   🎯 BEM NAMING CONVENTION - Quy ước đặt tên
   =================================================== */

/* 📦 Block: Standalone component (thành phần độc lập) */
.card {
}

/* 🧩 Element: Part of a block (phần của block, kết nối với __) */
.card__header {
}
.card__body {
}
.card__footer {
}

/* ⚙️ Modifier: Variant of block or element (biến thể, kết nối với --) */
.card--highlighted {
}
.card__header--large {
}

/* ===================================================
   ✅ GOOD: Proper BEM Structure
   =================================================== */

/* 📦 Component: ProductCard */
.product-card {
  display: flex;
  flex-direction: column; /* 🔽 Layout dọc */
  border: 1px solid #ddd; /* 🔲 Viền xám nhạt */
  border-radius: 8px; /* ➿ Bo góc 8px */
}

.product-card__image {
  width: 100%; /* 🖼️ Chiều rộng 100% */
  height: 200px; /* 📏 Chiều cao cố định */
  object-fit: cover; /* ✏️ Crop image để fit khung */
}

.product-card__title {
  font-size: 1.25rem; /* 🔤 Font size 20px */
  font-weight: 600; /* ⚖️ Font weight semi-bold */
  margin: 16px 0 8px; /* 📏 Khoảng cách trên/dưới */
}

.product-card__price {
  color: #e74c3c; /* 🔴 Màu đỏ (giá) */
  font-size: 1.5rem; /* 🔤 Font size 24px */
  font-weight: 700; /* ⚖️ Font weight bold */
}

.product-card__button {
  padding: 12px 24px; /* 📍 Padding trong/ngoài */
  background: #3498db; /* 🔵 Background xanh */
  color: white; /* ⚪ Chữ trắng */
  border: none; /* 🚫 Không viền */
  border-radius: 4px; /* ➿ Bo góc 4px */
  cursor: pointer; /* 🖌️ Con trỏ pointer khi hover */
}

/* ⚙️ Modifiers for variants (Biến thể) */
.product-card--featured {
  border-color: #f39c12; /* 🟡 Viền vàng (nổi bật) */
  box-shadow: 0 4px 12px rgba(243, 156, 18, 0.3); /* ✨ Bóng vàng */
}

.product-card__button--disabled {
  background: #95a5a6; /* ⚪ Background xám (disabled) */
  cursor: not-allowed; /* 🚫 Con trỏ not-allowed */
  opacity: 0.6; /* 🔅 Mờ 60% */
}

/* ===================================================
   ❌ BAD: BEM Anti-patterns
   =================================================== */

/* ❌ Too deep nesting (avoid .block__elem1__elem2) */
.product-card__header__image {
} /* BAD! */

/* ✅ Flatten structure */
.product-card__header-image {
} /* GOOD */

/* ❌ Using tag selectors (breaks encapsulation) */
.product-card h2 {
} /* BAD! */

/* ✅ Use explicit class names */
.product-card__title {
} /* GOOD */

/* ===================================================
   🎯 BEM HTML Example
   =================================================== */
```

```html
<!-- ✅ GOOD: BEM HTML Structure -->
<div class="product-card product-card--featured">
  <img src="product.jpg" alt="Product" class="product-card__image" />
  <h2 class="product-card__title">Wireless Headphones</h2>
  <span class="product-card__price">$99.99</span>
  <button class="product-card__button">Add to Cart</button>
</div>

<div class="product-card">
  <img src="product2.jpg" alt="Product" class="product-card__image" />
  <h2 class="product-card__title">Gaming Mouse</h2>
  <span class="product-card__price">$49.99</span>
  <button class="product-card__button product-card__button--disabled" disabled>
    Out of Stock
  </button>
</div>
```

**✅ BEM Advantages:**

- Clear component structure (Block → Element → Modifier hierarchy)
- No specificity wars (all classes have same specificity)
- Self-documenting (class names describe purpose)
- No naming conflicts (unique block names)

**❌ BEM Disadvantages:**

- Verbose class names (`.product-card__button--disabled`)
- HTML bloat (long class attributes)
- Manual enforcement (no automatic scoping)
- Learning curve (team must understand methodology)

---

## **2️⃣ CSS MODULES**

```typescript
// ===================================================
// 🎯 CSS MODULES - Scoped Styles (Styles có phạm vi)
// ===================================================

// 📄 Button.module.css
.button {
  padding: 12px 24px;        /* 📍 Padding trong/ngoài */
  background: #3498db;       /* 🔵 Background xanh */
  color: white;              /* ⚪ Chữ trắng */
  border: none;              /* 🚫 Không viền */
  border-radius: 4px;        /* ➿ Bo góc */
  cursor: pointer;           /* 🖌️ Pointer cursor */
  font-size: 1rem;           /* 🔤 Font size 16px */
  transition: background 0.3s ease;  /* ⏱️ Hiệu ứng chuyển đổi */
}

.button:hover {
  background: #2980b9;  /* 🔵 Màu xanh tối hơn khi hover */
}

.button:disabled {
  background: #95a5a6;   /* ⚪ Background xám khi disabled */
  cursor: not-allowed;   /* 🚫 Not-allowed cursor */
  opacity: 0.6;          /* 🔅 Mờ 60% */
}

/* ⚙️ Modifier: Primary variant (Biến thể primary) */
.primary {
  background: #2ecc71;  /* 🟢 Background xanh lá */
}

.primary:hover {
  background: #27ae60;  /* 🟢 Xanh lá tối hơn khi hover */
}

/* ⚙️ Modifier: Danger variant (Biến thể danger) */
.danger {
  background: #e74c3c;  /* 🔴 Background đỏ */
}

.danger:hover {
  background: #c0392b;  /* 🔴 Đỏ tối hơn khi hover */
}

// ===================================================
// ⚛️ Button.tsx (React Component)
// ===================================================

import styles from './Button.module.css';  // 📥 Import CSS module
import classNames from 'classnames'; // 📦 npm install classnames - Thư viện kết hợp className

type ButtonProps = {
  children: React.ReactNode;       // 📝 Nội dung button
  variant?: 'primary' | 'danger';  // ⚙️ Kiểu button
  disabled?: boolean;              // 🚫 Trạng thái disabled
  onClick?: () => void;            // 🖌️ Handler khi click
};

export function Button({ children, variant, disabled, onClick }: ButtonProps) {
  return (
    <button
      className={classNames(styles.button, {  // 🎯 Kết hợp base class + variants
        [styles.primary]: variant === 'primary',  // ✅ Nếu variant = primary
        [styles.danger]: variant === 'danger'     // ✅ Nếu variant = danger
      })}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}

// 📝 Usage
<Button variant="primary">Save</Button>     // 🟢 Button xanh lá
<Button variant="danger">Delete</Button>    // 🔴 Button đỏ
<Button disabled>Loading...</Button>       // ⚪ Button disabled xám

// ===================================================
// 🔍 Generated HTML (CSS Modules output)
// ===================================================

/**
 * CSS Modules automatically generates unique class names:
 *
 * <button class="Button_button__a1b2c Button_primary__d3e4f">
 *   Save
 * </button>
 *
 * .Button_button__a1b2c { ... }  ← Original: .button
 * .Button_primary__d3e4f { ... } ← Original: .primary
 *
 * ✅ No naming conflicts (unique hashes)
 * ✅ Scoped to component
 * ✅ Dead code elimination (unused styles removed)
 */

// ===================================================
// 🎯 COMPOSITION (Reusing Styles - Tái sử dụng styles)
// ===================================================

// 📄 base.module.css
.heading {
  font-family: 'Inter', sans-serif;  // 🔤 Font chữ
  font-weight: 700;                  // ⚖️ Độ dày chữ
  color: #2c3e50;                    // 🎨 Màu chữ
}

// 📄 Article.module.css
.title {
  composes: heading from './base.module.css';  // 🔄 Tái sử dụng heading styles
  font-size: 2rem;                            // 🔤 Thêm font size 32px
  margin-bottom: 16px;                        // 📏 Thêm margin dưới
}

.subtitle {
  composes: heading from './base.module.css';  // 🔄 Tái sử dụng heading styles
  font-size: 1.5rem;                          // 🔤 Font size 24px
  color: #7f8c8d;                             // 🎨 Màu xám nhạt hơn
}

// Article.tsx
import styles from './Article.module.css';

function Article() {
  return (
    <article>
      <h1 className={styles.title}>Main Heading</h1>
      <h2 className={styles.subtitle}>Subheading</h2>
    </article>
  );
}

// ===================================================
// 🔧 GLOBAL STYLES (Escape Scoping)
// ===================================================

// global.module.css
:global(.markdown-content) {
  /* Not scoped - applied globally */
  line-height: 1.6;
}

:global(.markdown-content) h1 {
  font-size: 2.5rem;
}

/* Mix global and local */
.container :global(.user-content) {
  /* .container is scoped, .user-content is global */
  padding: 20px;
}
```

**✅ CSS Modules Advantages:**

- Automatic scoping (no naming conflicts)
- Type-safe (with TypeScript: `styles.button` autocomplete)
- Composition (reuse styles via `composes`)
- Dead code elimination (unused styles removed at build)
- Works with existing CSS (no new syntax)

**❌ CSS Modules Disadvantages:**

- Build step required (webpack, vite, etc.)
- No dynamic styles (need inline styles or CSS variables)
- Verbose in React (`className={styles.button}`)
- Global styles need `:global()` escape hatch

---

## **3️⃣ CSS-IN-JS (Styled Components & Emotion)**

### **3.1. Styled Components**

```typescript
// ===================================================
// 🎨 STYLED COMPONENTS - CSS in JavaScript
// ===================================================

import styled from 'styled-components';  // 📦 npm install styled-components

// ⚙️ Basic styled component (Component cơ bản)
const Button = styled.button`
  padding: 12px 24px;         /* 📍 Padding trong/ngoài */
  background: #3498db;        /* 🔵 Background xanh */
  color: white;               /* ⚪ Chữ trắng */
  border: none;               /* 🚫 Không viền */
  border-radius: 4px;         /* ➿ Bo góc */
  cursor: pointer;            /* 🖌️ Pointer cursor */
  font-size: 1rem;            /* 🔤 Font size 16px */
  transition: background 0.3s ease;  /* ⏱️ Hiệu ứng chuyển đổi */

  &:hover {
    background: #2980b9;  /* 🔵 Màu tối hơn khi hover */
  }

  &:disabled {
    background: #95a5a6;   /* ⚪ Xám khi disabled */
    cursor: not-allowed;   /* 🚫 Not-allowed cursor */
    opacity: 0.6;          /* 🔅 Mờ 60% */
  }
`;

// ===================================================
// 🎯 PROPS-BASED DYNAMIC STYLES (Styles động dựa trên props)
// ===================================================

type ButtonProps = {
  $variant?: 'primary' | 'danger';  // ⚙️ Kiểu button
  $size?: 'small' | 'medium' | 'large';  // 📍 Kích thước button
};

const Button = styled.button<ButtonProps>`
  padding: ${(props) => {  // 📍 Padding dựa trên size
    switch (props.$size) {
      case 'small':
        return '8px 16px';   // 🔹 Small button
      case 'large':
        return '16px 32px';  // 🔷 Large button
      default:
        return '12px 24px';  // 🔸 Medium button (default)
    }
  }};

  background: ${(props) => {  // 🎨 Background dựa trên variant
    switch (props.$variant) {
      case 'primary':
        return '#2ecc71';  // 🟢 Xanh lá (primary)
      case 'danger':
        return '#e74c3c';  // 🔴 Đỏ (danger)
      default:
        return '#3498db';  // 🔵 Xanh (default)
    }
  }};

  color: white;               /* ⚪ Chữ trắng */
  border: none;               /* 🚫 Không viền */
  border-radius: 4px;         /* ➿ Bo góc */
  cursor: pointer;            /* 🖌️ Pointer cursor */
  font-size: 1rem;            /* 🔤 Font size */
  transition: all 0.3s ease;  /* ⏱️ Hiệu ứng chuyển đổi */

  &:hover {
    transform: translateY(-2px);  /* ⬆️ Nâng lên 2px */
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);  /* ✨ Thêm bóng */
  }

  &:disabled {
    background: #95a5a6;   /* ⚪ Xám khi disabled */
    cursor: not-allowed;   /* 🚫 Not-allowed cursor */
    opacity: 0.6;          /* 🔅 Mờ 60% */
    transform: none;       /* 🚫 Không hiệu ứng hover */
  }
`;

// 📝 Usage
<Button $variant="primary" $size="large">Save</Button>  // 🟢 Button xanh lá lớn
<Button $variant="danger">Delete</Button>  // 🔴 Button đỏ medium

// ===================================================
// 🔗 EXTENDING STYLES
// ===================================================

const Button = styled.button`
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
`;

// Extend and add more styles
const PrimaryButton = styled(Button)`
  background: #2ecc71;
  color: white;

  &:hover {
    background: #27ae60;
  }
`;

const OutlineButton = styled(Button)`
  background: transparent;
  border: 2px solid #3498db;
  color: #3498db;

  &:hover {
    background: #3498db;
    color: white;
  }
`;

// ===================================================
// 🎨 THEMING (Global Theme Provider - Theme toàn cục)
// ===================================================

import { ThemeProvider } from 'styled-components';

// 🎨 Define theme (Definition theme)
const theme = {
  colors: {                     // 🎨 Bảng màu
    primary: '#3498db',         // 🔵 Màu chính
    secondary: '#2ecc71',       // 🟢 Màu phụ
    danger: '#e74c3c',          // 🔴 Màu nguy hiểm
    text: '#2c3e50',            // 📝 Màu chữ
    background: '#ecf0f1'       // 🗄️ Màu nền
  },
  spacing: {                    // 📏 Khoảng cách
    small: '8px',               // 🔹 Nhỏ
    medium: '16px',             // 🔸 Trung bình
    large: '24px'               // 🔷 Lớn
  },
  breakpoints: {                // 📱 Responsive breakpoints
    mobile: '480px',            // 📱 Mobile
    tablet: '768px',            // 📱 Tablet
    desktop: '1024px'           // 💻 Desktop
  }
};

// ⚙️ Styled component using theme (Sử dụng theme)
const ThemedButton = styled.button`
  padding: ${(props) => props.theme.spacing.medium};  // 📏 Lấy spacing từ theme
  background: ${(props) => props.theme.colors.primary};  // 🎨 Lấy color từ theme
  color: white;                                       // ⚪ Chữ trắng
  border: none;                                       // 🚫 Không viền
  border-radius: 4px;                                 // ➿ Bo góc

  &:hover {
    background: ${(props) => props.theme.colors.secondary};  // 🟢 Đổi màu khi hover
  }

  @media (max-width: ${(props) => props.theme.breakpoints.mobile}) {  // 📱 Responsive mobile
    padding: ${(props) => props.theme.spacing.small};  // 🔹 Padding nhỏ hơn trên mobile
    font-size: 0.875rem;                              // 🔤 Font nhỏ hơn
  }
`;

// App.tsx
function App() {
  return (
    <ThemeProvider theme={theme}>
      <ThemedButton>Click Me</ThemedButton>
    </ThemeProvider>
  );
}

// ===================================================
// 🌗 DARK MODE TOGGLE
// ===================================================

const lightTheme = {
  background: '#ffffff',
  text: '#2c3e50',
  card: '#ecf0f1'
};

const darkTheme = {
  background: '#2c3e50',
  text: '#ecf0f1',
  card: '#34495e'
};

function App() {
  const [isDark, setIsDark] = useState(false);

  return (
    <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
      <GlobalStyles />
      <button onClick={() => setIsDark(!isDark)}>
        Toggle {isDark ? 'Light' : 'Dark'} Mode
      </button>
      <Content />
    </ThemeProvider>
  );
}

// Global styles with theme
const GlobalStyles = createGlobalStyle`
  body {
    background: ${(props) => props.theme.background};
    color: ${(props) => props.theme.text};
    transition: background 0.3s ease, color 0.3s ease;
  }
`;
```

### **3.2. Emotion**

```typescript
// ===================================================
// 💫 EMOTION - Alternative to Styled Components
// ===================================================

/** @jsxImportSource @emotion/react */  // 🔧 Enable JSX pragma cho Emotion
import { css } from '@emotion/react';  // 📦 Import css function
import styled from '@emotion/styled';  // 📦 Import styled (tương tự styled-components)

// ===================================================
// 🎯 CSS PROP (Inline CSS-in-JS - CSS inline)
// ===================================================

function Button({ variant, children }) {
  return (
    <button
      css={css`  /* 🎨 CSS prop - Viết CSS trực tiếp trong JSX */
        padding: 12px 24px;  /* 📍 Padding */
        background: ${variant === 'primary' ? '#2ecc71' : '#3498db'};  /* 🎨 Màu dựa trên variant */
        color: white;        /* ⚪ Chữ trắng */
        border: none;        /* 🚫 Không viền */
        border-radius: 4px;  /* ➿ Bo góc */
        cursor: pointer;     /* 🖌️ Pointer cursor */

        &:hover {  /* 🖌️ Hiệu ứng hover */
          transform: translateY(-2px);  /* ⬆️ Nâng lên */
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);  /* ✨ Bóng */
        }
      `}
    >
      {children}
    </button>
  );
}

// ===================================================
// 🎨 STYLED COMPONENTS (Emotion syntax)
// ===================================================

const Button = styled.button<{ variant?: 'primary' | 'danger' }>`
  padding: 12px 24px;
  background: ${(props) =>
    props.variant === 'primary'
      ? '#2ecc71'
      : props.variant === 'danger'
      ? '#e74c3c'
      : '#3498db'};
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

// ===================================================
// ⚡ PERFORMANCE: Object Styles (Faster than strings)
// ===================================================

const buttonStyles = {
  padding: '12px 24px',
  background: '#3498db',
  color: 'white',
  border: 'none',
  borderRadius: '4px',
  cursor: 'pointer',

  '&:hover': {
    background: '#2980b9'
  }
};

function Button() {
  return <button css={buttonStyles}>Click Me</button>;
}

// ===================================================
// 🔥 COMPOSITION (Merge Multiple Styles)
// ===================================================

const baseButton = css`
  padding: 12px 24px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
`;

const primaryButton = css`
  ${baseButton}
  background: #2ecc71;
  color: white;
`;

const dangerButton = css`
  ${baseButton}
  background: #e74c3c;
  color: white;
`;

<button css={primaryButton}>Save</button>
<button css={dangerButton}>Delete</button>
```

**✅ CSS-in-JS Advantages:**

- Dynamic styles (props-based, JS logic)
- Scoped by default (no naming conflicts)
- Colocated with components (easier maintenance)
- Theming built-in (ThemeProvider)
- TypeScript support (type-safe props)
- No unused CSS (dead code elimination)

**❌ CSS-in-JS Disadvantages:**

- Runtime overhead (styles computed on render)
- Larger bundle size (library + styles)
- Server rendering complexity (needs extra setup)
- Debugging harder (generated class names)
- Performance concerns (re-rendering re-computes styles)

---

## **4️⃣ TAILWIND CSS (Utility-First Framework)**

```html
<!-- ===================================================
     🎯 TAILWIND CSS - Utility Classes
     =================================================== -->

<!-- Button Examples -->
<button
  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
>
  Primary Button
</button>

<button
  class="bg-green-500 hover:bg-green-700 text-white font-bold py-3 px-6 rounded-lg shadow-lg transition duration-300 ease-in-out transform hover:scale-105"
>
  Large Primary Button with Animation
</button>

<button
  class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded opacity-50 cursor-not-allowed"
  disabled
>
  Disabled Button
</button>

<!-- Card Example -->
<div
  class="max-w-sm rounded overflow-hidden shadow-lg hover:shadow-2xl transition-shadow duration-300"
>
  <img class="w-full h-48 object-cover" src="product.jpg" alt="Product" />
  <div class="px-6 py-4">
    <div class="font-bold text-xl mb-2 text-gray-900">Product Title</div>
    <p class="text-gray-700 text-base">
      Product description goes here. This is a brief overview.
    </p>
  </div>
  <div class="px-6 pt-4 pb-2">
    <span
      class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
    >
      #tag1
    </span>
    <span
      class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
    >
      #tag2
    </span>
  </div>
</div>

<!-- Responsive Grid Layout -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 p-4">
  <div class="bg-white p-6 rounded-lg shadow">Item 1</div>
  <div class="bg-white p-6 rounded-lg shadow">Item 2</div>
  <div class="bg-white p-6 rounded-lg shadow">Item 3</div>
</div>
```

```javascript
// ===================================================
// 🔧 TAILWIND CONFIG (tailwind.config.js)
// ===================================================

module.exports = {
  content: ['./src/**/*.{js,jsx,ts,tsx}'], // Scan these files for classes
  theme: {
    extend: {
      // Custom colors
      colors: {
        brand: {
          50: '#eff6ff',
          100: '#dbeafe',
          500: '#3b82f6',
          900: '#1e3a8a'
        }
      },

      // Custom spacing
      spacing: {
        '128': '32rem',
        '144': '36rem'
      },

      // Custom breakpoints
      screens: {
        '3xl': '1920px'
      },

      // Custom fonts
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['Fira Code', 'monospace']
      },

      // Custom animations
      keyframes: {
        wiggle: {
          '0%, 100%': { transform: 'rotate(-3deg)' },
          '50%': { transform: 'rotate(3deg)' }
        }
      },
      animation: {
        wiggle: 'wiggle 1s ease-in-out infinite'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/aspect-ratio')
  ]
};

// ===================================================
// 🎨 CUSTOM COMPONENTS (Reusable Tailwind Patterns)
// ===================================================

// Button.tsx
type ButtonProps = {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  children: React.ReactNode;
};

export function Button({ variant = 'primary', size = 'md', children }: ButtonProps) {
  const baseClasses = 'font-bold rounded focus:outline-none focus:ring-2 transition duration-150';

  const variantClasses = {
    primary: 'bg-blue-500 hover:bg-blue-700 text-white focus:ring-blue-300',
    secondary: 'bg-gray-200 hover:bg-gray-300 text-gray-800 focus:ring-gray-300',
    danger: 'bg-red-500 hover:bg-red-700 text-white focus:ring-red-300'
  };

  const sizeClasses = {
    sm: 'py-1 px-2 text-sm',
    md: 'py-2 px-4 text-base',
    lg: 'py-3 px-6 text-lg'
  };

  const classes = `${baseClasses} ${variantClasses[variant]} ${sizeClasses[size]}`;

  return <button className={classes}>{children}</button>;
}

// ===================================================
// 📦 @APPLY DIRECTIVE (Extract Repeated Utilities)
// ===================================================

// styles.css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer components {
  .btn-primary {
    @apply bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded;
  }

  .card {
    @apply bg-white rounded-lg shadow-lg p-6;
  }
}

// Usage in HTML
<button class="btn-primary">Click Me</button>
<div class="card">Card Content</div>
```

**✅ Tailwind Advantages:**

- Fast development (no context switching CSS ↔ HTML)
- Small production bundle (PurgeCSS removes unused styles)
- Consistent design system (predefined spacing, colors)
- Responsive by default (`sm:`, `md:`, `lg:`, `xl:` prefixes)
- No naming fatigue (use predefined classes)
- Easy prototyping (compose UI fast)

**❌ Tailwind Disadvantages:**

- HTML bloat (long class strings)
- Learning curve (memorize utility classes)
- Less readable (class soup: `class="flex items-center justify-between px-4 py-2 bg-blue-500..."`)
- Hard to debug (which utility class caused issue?)
- Build step required (PostCSS + PurgeCSS)

---

## **5️⃣ CRITICAL CSS - Performance Optimization**

```typescript
// ===================================================
// ⚡ CRITICAL CSS - Inline Above-the-Fold Styles
// ===================================================

/**
 * Critical CSS = Minimum CSS needed to render above-the-fold content
 *
 * Problem:
 * ┌─────────────────────────────────────────────────┐
 * │  Browser loads HTML                             │
 * │  → Discovers <link rel="stylesheet">            │
 * │  → Fetches CSS file (blocks rendering)          │
 * │  → Parses CSS                                   │
 * │  → Renders page                                 │
 * └─────────────────────────────────────────────────┘
 * Total time: 2-3 seconds (CSS blocks rendering!)
 *
 * Solution: Inline critical CSS
 * ┌─────────────────────────────────────────────────┐
 * │  Browser loads HTML with <style> (inlined CSS)  │
 * │  → Renders page immediately (no blocking!)      │
 * │  → Lazy load full CSS                           │
 * └─────────────────────────────────────────────────┘
 * Total time: 0.5 seconds ✅
 */

// ===================================================
// 🔧 EXTRACT CRITICAL CSS (Webpack Plugin)
// ===================================================

// webpack.config.js
const HtmlWebpackPlugin = require('html-webpack-plugin');
const HtmlCriticalWebpackPlugin = require('html-critical-webpack-plugin');

module.exports = {
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html'
    }),

    new HtmlCriticalWebpackPlugin({
      base: './dist',
      src: 'index.html',
      dest: 'index.html',
      inline: true, // Inline critical CSS
      minify: true,
      extract: true, // Remove inlined CSS from external stylesheet
      width: 1300,
      height: 900,
      penthouse: {
        blockJSRequests: false
      }
    })
  ]
};

// ===================================================
// 📄 OUTPUT: HTML with Inlined Critical CSS
// ===================================================

/**
 * Before:
 * <html>
 *   <head>
 *     <link rel="stylesheet" href="styles.css">  ← Blocks rendering!
 *   </head>
 *   <body>...</body>
 * </html>
 *
 * After:
 * <html>
 *   <head>
 *     <style>
 *       /* Critical CSS (above-the-fold) inlined */
 *       body { margin: 0; font-family: Inter, sans-serif; }
 *       .header { background: #333; color: white; padding: 20px; }
 *       .hero { height: 100vh; background: url(...); }
 *     </style>
 *   </head>
 *   <body>
 *     ...
 *     <link rel="preload" href="styles.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
 *     <noscript><link rel="stylesheet" href="styles.css"></noscript>
 *   </body>
 * </html>
 */

// ===================================================
// ⚡ CRITICAL CSS FOR NEXT.JS
// ===================================================

// _document.tsx
import Document, { Html, Head, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          {/* Inline critical CSS */}
          <style
            dangerouslySetInnerHTML={{
              __html: `
                body { margin: 0; font-family: Inter, sans-serif; }
                .header { background: #333; color: white; }
              `
            }}
          />

          {/* Lazy load full CSS */}
          <link
            rel="preload"
            href="/styles/main.css"
            as="style"
            onLoad="this.onload=null;this.rel='stylesheet'"
          />
          <noscript>
            <link rel="stylesheet" href="/styles/main.css" />
          </noscript>
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;

// ===================================================
// 📊 CRITICAL CSS TOOLS
// ===================================================

/**
 * 1. Critical (npm package)
 *    npm install critical
 *    const critical = require('critical');
 *    critical.generate({ ... });
 *
 * 2. Penthouse (used by Critical)
 *    npm install penthouse
 *
 * 3. UnCSS (Remove unused CSS)
 *    npm install uncss
 *
 * 4. PurgeCSS (Tailwind CSS)
 *    npm install @fullhuman/postcss-purgecss
 *
 * 5. Critters (Webpack Plugin)
 *    npm install critters-webpack-plugin
 */
```

---

## **🎯 COMPARISON TABLE**

| Approach             | **BEM**    | **CSS Modules** | **Styled Comp** | **Tailwind** |
| -------------------- | ---------- | --------------- | --------------- | ------------ |
| **Scoping**          | ❌ Manual  | ✅ Automatic    | ✅ Automatic    | ❌ Global    |
| **Dynamic Styles**   | ❌ No      | ❌ Limited      | ✅ Yes          | ⚠️ Limited   |
| **Learning Curve**   | ⭐⭐       | ⭐⭐⭐⭐        | ⭐⭐⭐          | ⭐⭐⭐       |
| **Bundle Size**      | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐        | ⭐⭐⭐          | ⭐⭐⭐⭐⭐   |
| **Dev Speed**        | ⭐⭐⭐     | ⭐⭐⭐⭐        | ⭐⭐⭐⭐        | ⭐⭐⭐⭐⭐   |
| **Runtime Overhead** | ✅ None    | ✅ None         | ❌ Yes          | ✅ None      |
| **Theming**          | ❌ Manual  | ⚠️ CSS Vars     | ✅ Built-in     | ✅ Config    |
| **TypeScript**       | ❌ No      | ✅ Yes          | ✅ Yes          | ⚠️ Plugins   |

---

## **💡 WHEN TO USE WHAT?**

```typescript
// ===================================================
// 🎯 DECISION MATRIX
// ===================================================

const cssApproachDecision = {
  // New React/Vue app with dynamic theming
  modernApp: "CSS-in-JS (Styled Components or Emotion)",

  // Fast prototyping, landing pages
  prototyping: "Tailwind CSS",

  // Large team, existing CSS codebase
  legacyApp: "BEM or CSS Modules",

  // Component library (npm package)
  library: "CSS Modules or Styled Components",

  // Performance-critical (e-commerce, news)
  performance: "Tailwind CSS + Critical CSS extraction",

  // Server-rendered app (Next.js)
  ssr: "Tailwind CSS or CSS Modules (avoid runtime CSS-in-JS)",

  // Design system with strict guidelines
  designSystem: "Styled Components with ThemeProvider",

  // Simple website (blog, portfolio)
  simpleSite: "Plain CSS or Tailwind CSS",
};

// ===================================================
// ✅ BEST PRACTICES (Universal)
// ===================================================

const cssBestPractices = [
  // 1. Avoid deep nesting (max 3 levels)
  "div > ul > li > a { }  ← OK",
  "div > div > div > div > span { }  ← BAD",

  // 2. Use CSS variables for theming
  ":root { --primary-color: #3498db; }",
  "button { background: var(--primary-color); }",

  // 3. Mobile-first responsive design
  "/* Base styles (mobile) */",
  "@media (min-width: 768px) { /* Tablet */ }",
  "@media (min-width: 1024px) { /* Desktop */ }",

  // 4. Avoid !important (use specificity correctly)
  ".button { background: blue !important; }  ← BAD",
  ".card .button { background: blue; }  ← GOOD",

  // 5. Use semantic class names
  ".btn-primary  ← GOOD",
  ".blue-button  ← BAD (describes style, not purpose)",

  // 6. Critical CSS for above-the-fold content
  "Inline: <style>...</style>",
  'Lazy load: <link rel="preload">',

  // 7. Optimize for production
  "Minify CSS (cssnano)",
  "Remove unused CSS (PurgeCSS)",
  "Compress with Gzip/Brotli",
];
```

---

**🎯 TÓM TẮT Q59 - CSS ARCHITECTURE**

**✅ Traditional Approaches:**

- **BEM**: Clear naming convention, manual scoping, verbose class names
- **SMACSS**: Organized architecture, good for large teams

**✅ Modern Approaches:**

- **CSS Modules**: Automatic scoping, type-safe, no runtime overhead
- **CSS-in-JS**: Dynamic styles, theming, runtime overhead
- **Tailwind CSS**: Fast development, small bundle, utility-first

**✅ Performance:**

- **Critical CSS**: Inline above-the-fold styles, lazy load full CSS
- **PurgeCSS**: Remove unused Tailwind classes (90% size reduction)

**💡 Key Takeaways:**

1. **No silver bullet** - Choose based on project needs
2. **Tailwind dominates** for new projects (2024 trend)
3. **CSS-in-JS declining** (runtime overhead concerns)
4. **CSS Modules stable** (good balance)
5. **Critical CSS essential** for performance
6. **Hybrid approaches work** (Tailwind + CSS Modules)

---
