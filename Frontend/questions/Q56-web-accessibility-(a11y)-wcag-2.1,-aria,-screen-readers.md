# ♿ Q56: Web Accessibility (a11y) - WCAG 2.1, ARIA, Screen Readers

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐ (Advanced)  
> **Thời gian trả lời:** 12-15 phút

---

## 📋 **Mục Lục**

1. [WCAG 2.1 Guidelines](#1-wcag-21-guidelines)
2. [ARIA Attributes](#2-aria-attributes)
3. [Keyboard Navigation](#3-keyboard-navigation)
4. [Screen Reader Support](#4-screen-reader-support)
5. [Color Contrast & Visual Design](#5-color-contrast--visual-design)
6. [Automated Testing](#6-automated-testing)
7. [Focus Management](#7-focus-management)

---

## 1. WCAG 2.1 Guidelines

### **1.1. WCAG Levels**

```typescript
// ===================================================
// 📚 **WCAG 2.1 COMPLIANCE LEVELS**
// ===================================================

const WCAG_LEVELS = {
  // ✅ Level A (Minimum)
  A: [
    '🖼️ All images have alt text',
    '⌨️ All functionality available via keyboard',
    '🎯 Clear focus indicators',
    '📝 Form labels for all inputs',
    '🎨 Color not sole means of conveying info',
  ],
  
  // ✅ Level AA (Recommended - legal requirement in many countries)
  AA: [
    '🎨 Color contrast ratio ≥ 4.5:1 (normal text)',
    '🎨 Color contrast ratio ≥ 3:1 (large text 18pt+)',
    '📏 Text resizable up to 200% without loss of functionality',
    '⌨️ No keyboard trap',
    '🎬 Captions for audio/video',
    '📱 Touch targets ≥ 44×44 CSS pixels',
  ],
  
  // ✅ Level AAA (Enhanced - not required but ideal)
  AAA: [
    '🎨 Color contrast ratio ≥ 7:1 (normal text)',
    '🎨 Color contrast ratio ≥ 4.5:1 (large text)',
    '📖 Reading level ≤ lower secondary education',
    '🎬 Sign language interpretation for audio',
  ],
};

// ===================================================
// 🎯 **4 WCAG PRINCIPLES (POUR)**
// ===================================================

const POUR_PRINCIPLES = {
  Perceivable: 'Information must be presentable to users in ways they can perceive',
  Operable: 'UI components and navigation must be operable',
  Understandable: 'Information and UI operation must be understandable',
  Robust: 'Content must be robust enough for assistive technologies',
};
```

---

## 2. ARIA Attributes

### **2.1. ARIA Roles & Properties**

```tsx
// ===================================================
// 🎭 **ARIA ROLES**
// ===================================================

// ✅ Landmark roles (navigation structure)
function AppLayout() {
  return (
    <div>
      <header role="banner">
        <nav role="navigation" aria-label="Main navigation">
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/about">About</a></li>
          </ul>
        </nav>
      </header>
      
      <main role="main" aria-label="Main content">
        <article role="article">
          <h1>Article Title</h1>
          <p>Article content...</p>
        </article>
        
        <aside role="complementary" aria-label="Related content">
          <h2>Related Articles</h2>
        </aside>
      </main>
      
      <footer role="contentinfo">
        <p>&copy; 2024 Company</p>
      </footer>
    </div>
  );
}

// ===================================================
// 🎛️ **INTERACTIVE ARIA PATTERNS**
// ===================================================

// ✅ Button (custom interactive element)
function CustomButton({ onClick, disabled, children }: ButtonProps) {
  return (
    <div
      role="button"
      tabIndex={disabled ? -1 : 0}
      aria-disabled={disabled}
      onClick={disabled ? undefined : onClick}
      onKeyDown={(e) => {
        if (!disabled && (e.key === 'Enter' || e.key === ' ')) {
          e.preventDefault();
          onClick();
        }
      }}
    >
      {children}
    </div>
  );
}

// ✅ Toggle button (state indication)
function ToggleButton({ pressed, onToggle }: ToggleProps) {
  return (
    <button
      aria-pressed={pressed}
      onClick={onToggle}
    >
      {pressed ? 'ON' : 'OFF'}
    </button>
  );
}

// ✅ Expandable section (accordion)
function Accordion({ title, children }: AccordionProps) {
  const [expanded, setExpanded] = useState(false);
  const contentId = useId();
  
  return (
    <div>
      <button
        aria-expanded={expanded}
        aria-controls={contentId}
        onClick={() => setExpanded(!expanded)}
      >
        {title}
        <span aria-hidden="true">{expanded ? '▲' : '▼'}</span>
      </button>
      
      <div
        id={contentId}
        role="region"
        aria-labelledby={contentId}
        hidden={!expanded}
      >
        {children}
      </div>
    </div>
  );
}

// ===================================================
// 📋 **ARIA LIVE REGIONS** (Dynamic content)
// ===================================================

// ✅ Toast notifications
function ToastNotification({ message, type }: ToastProps) {
  return (
    <div
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      className={`toast toast-${type}`}
    >
      {message}
    </div>
  );
}

// ✅ Status updates (polite, doesn't interrupt)
function StatusMessage({ message }: StatusProps) {
  return (
    <div
      role="status"
      aria-live="polite"
      aria-atomic="true"
    >
      {message}
    </div>
  );
}

// ✅ Loading spinner
function LoadingSpinner({ label = 'Loading' }: LoadingProps) {
  return (
    <div
      role="status"
      aria-live="polite"
      aria-busy="true"
    >
      <span className="spinner" aria-hidden="true"></span>
      <span className="sr-only">{label}...</span>
    </div>
  );
}

// ===================================================
// 🏷️ **ARIA LABELING**
// ===================================================

// ✅ aria-label (invisible label)
function CloseButton({ onClose }: CloseButtonProps) {
  return (
    <button
      aria-label="Close dialog"
      onClick={onClose}
    >
      <span aria-hidden="true">×</span>
    </button>
  );
}

// ✅ aria-labelledby (reference to visible label)
function Modal({ titleId, children }: ModalProps) {
  return (
    <div
      role="dialog"
      aria-labelledby={titleId}
      aria-modal="true"
    >
      <h2 id={titleId}>Modal Title</h2>
      {children}
    </div>
  );
}

// ✅ aria-describedby (additional description)
function PasswordInput() {
  const helpId = useId();
  
  return (
    <div>
      <label htmlFor="password">Password</label>
      <input
        id="password"
        type="password"
        aria-describedby={helpId}
      />
      <p id={helpId}>
        Password must be at least 8 characters with 1 number
      </p>
    </div>
  );
}
```

---

## 3. Keyboard Navigation

### **3.1. Keyboard Support**

```tsx
// ===================================================
// ⌨️ **KEYBOARD NAVIGATION PATTERNS**
// ===================================================

// ✅ Dropdown menu (Arrow keys navigation)
function DropdownMenu({ items }: DropdownProps) {
  const [isOpen, setIsOpen] = useState(false);
  const [focusedIndex, setFocusedIndex] = useState(0);
  const itemRefs = useRef<HTMLButtonElement[]>([]);
  
  const handleKeyDown = (e: KeyboardEvent) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault();
        setFocusedIndex((prev) => Math.min(prev + 1, items.length - 1));
        break;
      
      case 'ArrowUp':
        e.preventDefault();
        setFocusedIndex((prev) => Math.max(prev - 1, 0));
        break;
      
      case 'Home':
        e.preventDefault();
        setFocusedIndex(0);
        break;
      
      case 'End':
        e.preventDefault();
        setFocusedIndex(items.length - 1);
        break;
      
      case 'Escape':
        setIsOpen(false);
        break;
      
      case 'Enter':
      case ' ':
        e.preventDefault();
        items[focusedIndex].onClick();
        setIsOpen(false);
        break;
    }
  };
  
  useEffect(() => {
    if (isOpen) {
      itemRefs.current[focusedIndex]?.focus();
    }
  }, [focusedIndex, isOpen]);
  
  return (
    <div onKeyDown={handleKeyDown}>
      <button
        aria-haspopup="true"
        aria-expanded={isOpen}
        onClick={() => setIsOpen(!isOpen)}
      >
        Menu
      </button>
      
      {isOpen && (
        <ul role="menu">
          {items.map((item, index) => (
            <li key={index} role="none">
              <button
                ref={(el) => el && (itemRefs.current[index] = el)}
                role="menuitem"
                tabIndex={index === focusedIndex ? 0 : -1}
                onClick={item.onClick}
              >
                {item.label}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

// ===================================================
// 📑 **TAB PANEL** (ARIA Tabs pattern)
// ===================================================

function Tabs({ tabs }: TabsProps) {
  const [activeTab, setActiveTab] = useState(0);
  
  const handleKeyDown = (e: KeyboardEvent, index: number) => {
    switch (e.key) {
      case 'ArrowRight':
        e.preventDefault();
        setActiveTab((index + 1) % tabs.length);
        break;
      
      case 'ArrowLeft':
        e.preventDefault();
        setActiveTab((index - 1 + tabs.length) % tabs.length);
        break;
      
      case 'Home':
        e.preventDefault();
        setActiveTab(0);
        break;
      
      case 'End':
        e.preventDefault();
        setActiveTab(tabs.length - 1);
        break;
    }
  };
  
  return (
    <div>
      <div role="tablist" aria-label="Content tabs">
        {tabs.map((tab, index) => (
          <button
            key={index}
            role="tab"
            aria-selected={activeTab === index}
            aria-controls={`tabpanel-${index}`}
            id={`tab-${index}`}
            tabIndex={activeTab === index ? 0 : -1}
            onClick={() => setActiveTab(index)}
            onKeyDown={(e) => handleKeyDown(e, index)}
          >
            {tab.title}
          </button>
        ))}
      </div>
      
      {tabs.map((tab, index) => (
        <div
          key={index}
          role="tabpanel"
          id={`tabpanel-${index}`}
          aria-labelledby={`tab-${index}`}
          hidden={activeTab !== index}
          tabIndex={0}
        >
          {tab.content}
        </div>
      ))}
    </div>
  );
}
```

---

## 4. Screen Reader Support

### **4.1. Screen Reader Optimization**

```tsx
// ===================================================
// 🔊 **SCREEN READER ONLY TEXT**
// ===================================================

// ✅ CSS for screen reader only content
const srOnlyStyles = {
  position: 'absolute',
  width: '1px',
  height: '1px',
  padding: 0,
  margin: '-1px',
  overflow: 'hidden',
  clip: 'rect(0, 0, 0, 0)',
  whiteSpace: 'nowrap',
  border: 0,
} as const;

function ScreenReaderOnly({ children }: { children: React.ReactNode }) {
  return <span style={srOnlyStyles}>{children}</span>;
}

// ===================================================
// 📊 **DATA TABLE** (Complex structure)
// ===================================================

function AccessibleTable({ data }: TableProps) {
  return (
    <table>
      <caption>
        User Statistics
        <ScreenReaderOnly>
          Table showing user count by country and status
        </ScreenReaderOnly>
      </caption>
      
      <thead>
        <tr>
          <th scope="col">Country</th>
          <th scope="col">Active Users</th>
          <th scope="col">Inactive Users</th>
        </tr>
      </thead>
      
      <tbody>
        {data.map((row) => (
          <tr key={row.country}>
            <th scope="row">{row.country}</th>
            <td>{row.activeUsers}</td>
            <td>{row.inactiveUsers}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

// ===================================================
// 🖼️ **IMAGES & ICONS**
// ===================================================

// ✅ Informative image
function ProductImage({ src, alt }: ImageProps) {
  return <img src={src} alt={alt} />;
}

// ✅ Decorative image (empty alt)
function DecorativeImage({ src }: { src: string }) {
  return <img src={src} alt="" role="presentation" />;
}

// ✅ Icon with text label
function SaveButton() {
  return (
    <button>
      <svg aria-hidden="true" focusable="false">
        {/* Icon SVG */}
      </svg>
      <span>Save</span>
    </button>
  );
}

// ✅ Icon-only button
function IconButton({ icon, label, onClick }: IconButtonProps) {
  return (
    <button aria-label={label} onClick={onClick}>
      <span aria-hidden="true">{icon}</span>
    </button>
  );
}
```

---

## 5. Color Contrast & Visual Design

### **5.1. Color Contrast Checker**

```typescript
// ===================================================
// 🎨 **COLOR CONTRAST CALCULATOR**
// ===================================================

function getRelativeLuminance(rgb: [number, number, number]): number {
  const [r, g, b] = rgb.map((val) => {
    const sRGB = val / 255;
    return sRGB <= 0.03928
      ? sRGB / 12.92
      : Math.pow((sRGB + 0.055) / 1.055, 2.4);
  });
  
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function getContrastRatio(color1: string, color2: string): number {
  // Convert hex to RGB (simplified)
  const hexToRgb = (hex: string): [number, number, number] => {
    const result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})$/i.exec(hex);
    return result
      ? [
          parseInt(result[1], 16),
          parseInt(result[2], 16),
          parseInt(result[3], 16),
        ]
      : [0, 0, 0];
  };
  
  const lum1 = getRelativeLuminance(hexToRgb(color1));
  const lum2 = getRelativeLuminance(hexToRgb(color2));
  
  const lighter = Math.max(lum1, lum2);
  const darker = Math.min(lum1, lum2);
  
  return (lighter + 0.05) / (darker + 0.05);
}

function checkWCAGCompliance(ratio: number, fontSize: number) {
  const isLargeText = fontSize >= 18 || (fontSize >= 14 && isBold);
  
  return {
    AA: isLargeText ? ratio >= 3 : ratio >= 4.5,
    AAA: isLargeText ? ratio >= 4.5 : ratio >= 7,
  };
}

// ===================================================
// 🎨 **USAGE EXAMPLE**
// ===================================================

const textColor = '#333333';
const bgColor = '#FFFFFF';
const ratio = getContrastRatio(textColor, bgColor);
// ratio = 12.63 → ✅ Passes AA and AAA

const buttonColor = '#007BFF';
const buttonBg = '#FFFFFF';
const buttonRatio = getContrastRatio(buttonColor, buttonBg);
// buttonRatio = 4.56 → ✅ Passes AA for normal text
```

---

## 6. Automated Testing

### **6.1. axe-core Integration**

```typescript
// ===================================================
// 🔍 **AXE-CORE ACCESSIBILITY TESTING**
// ===================================================

import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility Tests', () => {
  test('should not have any automatically detectable accessibility issues', async ({
    page,
  }) => {
    await page.goto('/');
    
    const accessibilityScanResults = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();
    
    expect(accessibilityScanResults.violations).toEqual([]);
  });
  
  test('should have accessible form', async ({ page }) => {
    await page.goto('/contact');
    
    const results = await new AxeBuilder({ page })
      .include('#contact-form')
      .analyze();
    
    expect(results.violations).toEqual([]);
  });
});

// ===================================================
// 🧪 **JEST + TESTING LIBRARY**
// ===================================================

import { render } from '@testing-library/react';
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

describe('Button Accessibility', () => {
  it('should have no accessibility violations', async () => {
    const { container } = render(<Button>Click me</Button>);
    const results = await axe(container);
    
    expect(results).toHaveNoViolations();
  });
});

// ===================================================
// 📊 **LIGHTHOUSE CI**
// ===================================================

// .lighthouserc.json
{
  "ci": {
    "collect": {
      "numberOfRuns": 3,
      "url": ["http://localhost:3000"]
    },
    "assert": {
      "assertions": {
        "categories:accessibility": ["error", { "minScore": 0.95 }],
        "aria-allowed-attr": "error",
        "aria-required-attr": "error",
        "aria-valid-attr": "error",
        "color-contrast": "error",
        "document-title": "error",
        "html-has-lang": "error",
        "label": "error",
        "meta-viewport": "error"
      }
    }
  }
}
```

---

## 7. Focus Management

### **7.1. Focus Trap & Restoration**

```tsx
// ===================================================
// 🎯 **FOCUS TRAP** (Modal dialogs)
// ===================================================

import { useEffect, useRef } from 'react';

function useFocusTrap(isOpen: boolean) {
  const containerRef = useRef<HTMLDivElement>(null);
  
  useEffect(() => {
    if (!isOpen) return;
    
    const container = containerRef.current;
    if (!container) return;
    
    // Get all focusable elements
    const focusableElements = container.querySelectorAll<HTMLElement>(
      'a[href], button:not([disabled]), textarea:not([disabled]), input:not([disabled]), select:not([disabled]), [tabindex]:not([tabindex="-1"])'
    );
    
    const firstElement = focusableElements[0];
    const lastElement = focusableElements[focusableElements.length - 1];
    
    // Focus first element
    firstElement?.focus();
    
    const handleTab = (e: KeyboardEvent) => {
      if (e.key !== 'Tab') return;
      
      if (e.shiftKey) {
        // Shift + Tab
        if (document.activeElement === firstElement) {
          e.preventDefault();
          lastElement?.focus();
        }
      } else {
        // Tab
        if (document.activeElement === lastElement) {
          e.preventDefault();
          firstElement?.focus();
        }
      }
    };
    
    container.addEventListener('keydown', handleTab);
    
    return () => {
      container.removeEventListener('keydown', handleTab);
    };
  }, [isOpen]);
  
  return containerRef;
}

// ✅ Usage in modal
function Modal({ isOpen, onClose, children }: ModalProps) {
  const containerRef = useFocusTrap(isOpen);
  const previousActiveElement = useRef<HTMLElement | null>(null);
  
  useEffect(() => {
    if (isOpen) {
      previousActiveElement.current = document.activeElement as HTMLElement;
    } else {
      previousActiveElement.current?.focus();
    }
  }, [isOpen]);
  
  if (!isOpen) return null;
  
  return (
    <div
      ref={containerRef}
      role="dialog"
      aria-modal="true"
    >
      <button onClick={onClose} aria-label="Close">×</button>
      {children}
    </div>
  );
}

// ===================================================
// 🔍 **SKIP LINKS** (Jump to main content)
// ===================================================

function SkipLink() {
  return (
    <a
      href="#main-content"
      className="skip-link"
      style={{
        position: 'absolute',
        left: '-9999px',
        ':focus': {
          left: 0,
          top: 0,
          padding: '1rem',
          background: '#000',
          color: '#fff',
          zIndex: 9999,
        },
      }}
    >
      Skip to main content
    </a>
  );
}
```

---

**🎯 Remember:** "Accessibility is not a feature - it's a fundamental requirement. Build inclusively from day one!"
