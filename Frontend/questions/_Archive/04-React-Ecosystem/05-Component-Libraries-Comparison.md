# 🎨 Q53: Component Libraries Comparison

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Component Libraries = pre-built UI components để tăng tốc development. MUI = Material Design, enterprise-ready. Ant Design = enterprise admin dashboards. Chakra UI = simple, customizable. Radix UI = headless, accessible. Shadcn/ui = copy-paste components. Chọn library dựa trên: design system, bundle size, customization needs, accessibility requirements."**

**🔑 Top Component Libraries (Thư Viện Component Hàng Đầu):**

| Library (Thư viện) | Bundle Size (Kích thước bundle)         | Design System (Hệ thống thiết kế) | Customization (Tùy chỉnh)             | Accessibility (Khả năng truy cập) | Best For (Tốt nhất cho)                        |
| ------------------ | --------------------------------------- | --------------------------------- | ------------------------------------- | --------------------------------- | ---------------------------------------------- |
| **🏗️ MUI**         | ⚠️ Large (~300KB) (Lớn)                 | Material Design                   | ✅ Theme-based (Dựa trên theme)       | ✅ WCAG 2.1                       | Enterprise apps (Ứng dụng doanh nghiệp)        |
| **📊 Ant Design**  | ⚠️ Large (~500KB) (Rất lớn)             | Ant Design                        | ✅ Theme-based (Dựa trên theme)       | ✅ Good (Tốt)                     | Admin dashboards (Bảng điều khiển quản trị)    |
| **🎨 Chakra UI**   | ✅ Medium (~150KB) (Trung bình)         | Custom (Tùy chỉnh)                | ✅ Props-based (Dựa trên props)       | ✅ Excellent (Xuất sắc)           | Modern apps (Ứng dụng hiện đại)                |
| **⚡ Mantine**     | ✅ Medium (~200KB) (Trung bình)         | Custom (Tùy chỉnh)                | ✅ Props-based (Dựa trên props)       | ✅ Excellent (Xuất sắc)           | Full-featured apps (Ứng dụng đầy đủ tính năng) |
| **🧩 Radix UI**    | ✅ Small (~50KB) (Nhỏ)                  | Headless (Không style)            | ✅ Full control (Kiểm soát hoàn toàn) | ✅ Excellent (Xuất sắc)           | Custom designs (Thiết kế tùy chỉnh)            |
| **📋 Shadcn/ui**   | ✅ Zero (copy code) (Không - copy code) | Tailwind                          | ✅ Full control (Kiểm soát hoàn toàn) | ✅ Excellent (Xuất sắc)           | Tailwind projects (Dự án Tailwind)             |

**🔑 Key Features (Tính Năng Chính):**

**1. 🏗️ Material-UI (MUI):**

- **Material Design 3** - Google's design system (Hệ thống thiết kế của Google)
- **Theming (Giao diện)** - Powerful theme customization (Tùy chỉnh theme mạnh mẽ)
- **Enterprise-ready (Sẵn sàng doanh nghiệp)** - Production-tested (Đã được kiểm thử sản xuất)
- **Large ecosystem (Hệ sinh thái lớn)** - Many components (Nhiều components)
- **Bundle size (Kích thước bundle)** - Large (~300KB gzipped) (Lớn)

**2. 📊 Ant Design:**

- **Enterprise focus (Tập trung doanh nghiệp)** - Admin dashboards, data tables (Bảng điều khiển quản trị, bảng dữ liệu)
- **Rich components (Components phong phú)** - Forms, tables, charts (Form, bảng, biểu đồ)
- **Chinese origin (Nguồn gốc Trung Quốc)** - Popular in Asia (Phổ biến ở Châu Á)
- **Bundle size (Kích thước bundle)** - Very large (~500KB) (Rất lớn)

**3. 🎨 Chakra UI:**

- **Simple API (API đơn giản)** - Easy to learn (Dễ học)
- **Props-based styling (Styling dựa trên props)** - No CSS needed (Không cần CSS)
- **Accessibility (Khả năng truy cập)** - Built-in a11y (Tích hợp sẵn)
- **Bundle size (Kích thước bundle)** - Medium (~150KB) (Trung bình)

**4. 🧩 Radix UI:**

- **Headless (Không style)** - No styles, full control (Không có style, kiểm soát hoàn toàn)
- **Accessible (Có thể truy cập)** - WCAG 2.1 compliant (Tuân thủ WCAG 2.1)
- **Composable (Có thể kết hợp)** - Mix and match (Trộn và kết hợp)
- **Bundle size (Kích thước bundle)** - Small (~50KB per component) (Nhỏ - mỗi component)

**5. 📋 Shadcn/ui:**

- **Copy-paste (Sao chép-dán)** - Own the code (Sở hữu code)
- **Tailwind CSS** - Utility-first (Ưu tiên utility)
- **Customizable (Có thể tùy chỉnh)** - Full control (Kiểm soát hoàn toàn)
- **Bundle size (Kích thước bundle)** - Zero (you copy code) (Không - bạn copy code)

**⚠️ Lỗi Thường Gặp (Common Mistakes):**

- ❌ Chọn library quá lớn cho simple app → bundle bloat (Choose library too large for simple app → bundle bloat)
- ❌ Không customize theme → app giống demo (Don't customize theme → app looks like demo)
- ❌ Ignore accessibility → không pass WCAG (Ignore accessibility → doesn't pass WCAG)
- ❌ Mix nhiều libraries → inconsistent design (Mix multiple libraries → inconsistent design)
- ❌ Không tree-shake → import toàn bộ library (Don't tree-shake → import entire library)

**💡 Kiến Thức Senior (Senior Knowledge):**

- **🌳 Tree-shaking**: Import specific components (not entire library) (Import components cụ thể - không phải toàn bộ thư viện)
- **🎨 Theme customization**: Override design tokens, not CSS (Ghi đè design tokens, không phải CSS)
- **♿ Accessibility**: Use semantic HTML, ARIA attributes (Sử dụng HTML ngữ nghĩa, thuộc tính ARIA)
- **📦 Bundle optimization**: Code splitting, lazy loading (Tối ưu bundle - chia code, tải lười)
- **🎨 Design system**: Consistent spacing, colors, typography (Hệ thống thiết kế - khoảng cách, màu sắc, typography nhất quán)

> **Câu hỏi phỏng vấn Senior Frontend Developer** > **Độ khó:** ⭐⭐⭐ (Intermediate-Advanced)
> **Thời gian trả lời:** 10-12 phút

---

## 📋 **Mục Lục**

1. [Component Libraries Overview](#1-component-libraries-overview)
2. [Material-UI (MUI)](#2-material-ui-mui)
3. [Ant Design](#3-ant-design)
4. [Chakra UI](#4-chakra-ui)
5. [Mantine](#5-mantine)
6. [Radix UI](#6-radix-ui)
7. [Headless UI](#7-headless-ui)
8. [Shadcn/ui](#8-shadcnui)
9. [Comparison Matrix](#9-comparison-matrix)
10. [Choosing the Right Library](#10-choosing-the-right-library)
11. [Best Practices](#11-best-practices)

---

## 1. Component Libraries Overview

### **1.1. What are Component Libraries?**

```typescript
/**
 * 🎨 COMPONENT LIBRARIES = Pre-built UI components để tăng tốc development
 *
 * 💡 Thay vì tự code từ đầu:
 * - Button, Input, Modal, Table, Form...
 * - Mỗi component cần: styling, accessibility, keyboard navigation, responsive...
 * - Tốn thời gian: 1-2 tuần chỉ để build basic components
 *
 * ✅ Dùng Component Library:
 * - Import và dùng ngay: <Button>Click me</Button>
 * - Đã có: styling, accessibility, responsive, keyboard support
 * - Tiết kiệm: 80% thời gian development
 * - Consistent: Design system nhất quán
 */

// ❌ TỰ CODE TỪ ĐẦU (không dùng library - without using library)
const CustomButton = ({ children, onClick }) => {
  // 💡 children: Nội dung bên trong button (Content inside button)
  // 💡 onClick: Hàm xử lý khi click (Click handler function)

  return (
    <button
      onClick={onClick} // 🖱️ Xử lý sự kiện click (Handle click event)
      style={{
        padding: '8px 16px', // 📏 Padding trên/dưới 8px, trái/phải 16px
        backgroundColor: '#1976d2', // 🎨 Màu nền xanh dương (Blue background color)
        color: 'white', // ⚪ Màu chữ trắng (White text color)
        border: 'none', // 🚫 Không có viền (No border)
        borderRadius: '4px', // 📐 Bo góc 4px (4px border radius)
        cursor: 'pointer', // 🖱️ Con trỏ chuột thành pointer khi hover (Pointer cursor on hover)
        // ... 50+ dòng CSS nữa (50+ more lines of CSS)
        // ❌ Thiếu: focus states, disabled states, loading states, accessibility...
        // (Missing: focus states, disabled states, loading states, accessibility...)
      }}
    >
      {children} {/* 📝 Hiển thị nội dung button (Display button content) */}
    </button>
  );
};
// 💥 Vấn đề (Problems):
// - Tốn thời gian code (Time-consuming to code)
// - Không consistent với design system (Not consistent with design system)
// - Thiếu accessibility (keyboard navigation, screen reader support)
//   (Missing accessibility - keyboard navigation, screen reader support)
// - Không responsive (Not responsive)
// - Phải maintain code (Must maintain code)

// ✅ DÙNG COMPONENT LIBRARY (MUI) - Using Component Library (MUI)
import { Button } from '@mui/material'; // 📦 Import Button component từ MUI

const MyButton = () => {
  // 💡 Component function không nhận props (Component function doesn't receive props)

  return (
    <Button
      variant="contained" // 🎨 Kiểu button: contained (có nền), outlined (có viền), text (chỉ chữ)
      // (Button style: contained - with background, outlined - with border, text - text only)
      onClick={handleClick} // 🖱️ Hàm xử lý khi click (Click handler function)
    >
      Click me {/* 📝 Nội dung button (Button content) */}
    </Button>
  );
};
// 🚀 Ưu điểm (Advantages):
// - Code ngắn gọn (1 dòng) (Concise code - 1 line)
// - Đã có: styling, accessibility, responsive, keyboard support
//   (Already has: styling, accessibility, responsive, keyboard support)
// - Consistent với Material Design (Consistent with Material Design)
// - Production-ready (Sẵn sàng cho production)
```

### **1.2. When to Use Component Libraries?**

```typescript
/**
 * ✅ NÊN DÙNG COMPONENT LIBRARY KHI:
 *
 * 1️⃣ 🚀 Tăng tốc development
 *    - Deadline gấp, cần ship nhanh
 *    - Team nhỏ, không có designer chuyên nghiệp
 *    - MVP/Prototype cần làm nhanh
 *
 * 2️⃣ 🎨 Cần design system nhất quán
 *    - Enterprise app với nhiều screens
 *    - Team lớn, cần consistency
 *    - Brand guidelines rõ ràng
 *
 * 3️⃣ ♿ Accessibility là requirement
 *    - Government/Healthcare apps (bắt buộc WCAG 2.1)
 *    - Public-facing apps
 *    - Libraries đã test accessibility sẵn
 *
 * 4️⃣ 📦 Cần nhiều components phức tạp
 *    - Data tables với sorting, filtering, pagination
 *    - Date pickers, rich text editors
 *    - Charts, graphs
 *    - Tự code tốn thời gian
 *
 * ❌ KHÔNG NÊN DÙNG KHI:
 *
 * 1️⃣ 🎨 Design độc đáo, không theo standard
 *    - Custom design system riêng
 *    - Brand identity đặc biệt
 *    - Library không match design
 *
 * 2️⃣ 📦 Bundle size là concern chính
 *    - Mobile app, cần tối ưu size
 *    - Library quá lớn (>500KB)
 *    - Chỉ cần 1-2 components đơn giản
 *
 * 3️⃣ 🔧 Cần control hoàn toàn
 *    - Custom behavior phức tạp
 *    - Performance critical
 *    - Library không đáp ứng được
 */
```

---

## 2. Material-UI (MUI)

### **2.1. Overview**

```typescript
/**
 * 🎨 MATERIAL-UI (MUI) = Component library theo Material Design của Google
 *
 * ✅ ƯU ĐIỂM:
 * - Material Design 3: Design system chuẩn của Google
 * - Enterprise-ready: Được dùng bởi nhiều công ty lớn
 * - Rich components: 100+ components (Button, Table, Form, DatePicker...)
 * - Theming: Customize theme dễ dàng
 * - TypeScript: Full TypeScript support
 * - Documentation: Tài liệu rất chi tiết
 * - Community: Large community, nhiều resources
 *
 * ❌ NHƯỢC ĐIỂM:
 * - Bundle size: Lớn (~300KB gzipped)
 * - Learning curve: Cần học Material Design concepts
 * - Customization: Khó customize sâu (phải override nhiều)
 * - Design: Material Design có thể không phù hợp mọi brand
 *
 * 🎯 USE CASES:
 * - Enterprise applications
 * - Admin dashboards
 * - Apps cần Material Design look
 * - Large teams cần consistency
 */

// 📦 INSTALLATION
// npm install @mui/material @emotion/react @emotion/styled
// hoặc
// npm install @mui/material @mui/styled-engine-sc styled-components

// ✅ BASIC USAGE (Cách Sử Dụng Cơ Bản)
import { Button, TextField, Box, Stack } from '@mui/material';
// 📦 Import các components cần thiết từ MUI
// (Import necessary components from MUI)

function LoginForm() {
  // 💡 Component form đăng nhập (Login form component)

  return (
    <Box sx={{ p: 3 }}>
      {/* 📦 Box = div với sx prop (styling)
          (Box = div with sx prop for styling)
          💡 sx={{ p: 3 }} = padding: 24px (3 * 8px base spacing)
          (sx={{ p: 3 }} = padding: 24px - 3 times base spacing of 8px) */}
      <Stack spacing={2}>
        {/* 📊 Stack = flex container với spacing
            (Stack = flex container with spacing)
            💡 spacing={2} = khoảng cách giữa các items: 16px (2 * 8px)
            (spacing={2} = gap between items: 16px - 2 times base spacing) */}

        <TextField
          label="Email" // 🏷️ Label hiển thị trên input (Label displayed on input)
          type="email" // 📧 Kiểu input: email (Input type: email)
          variant="outlined" // 🎨 Variant: outlined (có viền), filled (có nền), standard (chuẩn)
          // (Variant: outlined - with border, filled - with background, standard - default)
          fullWidth // 📏 Chiếm full width của container (Takes full width of container)
        />

        <TextField
          label="Password" // 🏷️ Label: Password (Label: Password)
          type="password" // 🔒 Kiểu input: password (ẩn ký tự) (Input type: password - hides characters)
          variant="outlined" // 🎨 Variant: outlined (Variant: outlined)
          fullWidth // 📏 Chiếm full width (Full width)
        />

        <Button
          variant="contained" // 🎨 Variant: contained (có nền), outlined (có viền), text (chỉ chữ)
          // (Variant: contained - with background, outlined - with border, text - text only)
          color="primary" // 🎨 Color: primary (màu chính), secondary, error, warning, info, success
          // (Color: primary - main color, secondary, error, warning, info, success)
          size="large" // 📏 Size: small (nhỏ), medium (trung bình), large (lớn)
          // (Size: small, medium, large)
          fullWidth // 📏 Chiếm full width (Full width)
        >
          Login {/* 📝 Nội dung button (Button content) */}
        </Button>
      </Stack>
    </Box>
  );
}
```

### **2.2. Theming System**

```typescript
/**
 * 🎨 MUI THEMING - Customize design system toàn bộ app
 *
 * 💡 Theme object chứa:
 * - Colors (primary, secondary, error...)
 * - Typography (font families, sizes...)
 * - Spacing (margins, paddings...)
 * - Breakpoints (responsive breakpoints...)
 * - Components (default props cho components...)
 */

import { createTheme, ThemeProvider } from '@mui/material/styles';
// 📦 createTheme: Tạo theme object tùy chỉnh (Create custom theme object)
// 📦 ThemeProvider: Component cung cấp theme cho toàn bộ app (Component that provides theme to entire app)
import { CssBaseline } from '@mui/material';
// 📦 CssBaseline: Reset CSS và áp dụng base styles (Reset CSS and apply base styles)

// 🎨 CREATE CUSTOM THEME (Tạo Theme Tùy Chỉnh)
const theme = createTheme({
  // 💡 createTheme() nhận object config để tạo theme (createTheme() receives config object to create theme)

  // 🎨 COLOR PALETTE - Định nghĩa màu sắc (Define colors)
  palette: {
    // 💡 palette: Định nghĩa bảng màu cho app (Define color palette for app)
    primary: {
      // 🔵 Màu chính của app (Main color of app)
      main: '#1976d2', // 🔵 Màu chính (blue) - Dùng cho buttons, links chính (Used for main buttons, links)
      light: '#42a5f5', // 🔵 Màu nhạt hơn - Dùng cho hover states (Lighter color - used for hover states)
      dark: '#1565c0', // 🔵 Màu đậm hơn - Dùng cho active/pressed states (Darker color - used for active/pressed states)
      contrastText: '#fff', // ⚪ Màu chữ trên nền primary - Đảm bảo đọc được (Text color on primary background - ensures readability)
    },
    secondary: {
      // 🔴 Màu phụ của app (Secondary color of app)
      main: '#dc004e', // 🔴 Màu phụ (pink) - Dùng cho actions phụ (Secondary color - used for secondary actions)
    },
    error: {
      // ❌ Màu lỗi (Error color)
      main: '#f44336', // ❌ Màu lỗi (red) - Dùng cho error messages, danger buttons (Used for error messages, danger buttons)
    },
    background: {
      // ⚪ Màu nền (Background colors)
      default: '#f5f5f5', // ⚪ Màu nền mặc định của app (Default background color of app)
      paper: '#ffffff', // 📄 Màu nền của Paper component (Background color of Paper component)
    },
  },

  // 📝 TYPOGRAPHY - Định nghĩa font chữ (Define typography)
  typography: {
    // 💡 typography: Định nghĩa font chữ, kích thước, độ đậm cho text (Define fonts, sizes, weights for text)
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif',
    // 🔤 Font family mặc định - Thứ tự ưu tiên: Roboto → Helvetica → Arial → sans-serif
    // (Default font family - Priority order: Roboto → Helvetica → Arial → sans-serif)
    h1: {
      // 📝 Heading 1 style
      fontSize: '2.5rem', // 📏 Kích thước heading 1: 2.5rem = 40px (Heading 1 size: 2.5rem = 40px)
      fontWeight: 500, // 💪 Độ đậm: 500 (medium) (Font weight: 500 - medium)
    },
    h2: {
      // 📝 Heading 2 style
      fontSize: '2rem', // 📏 Kích thước heading 2: 2rem = 32px (Heading 2 size: 2rem = 32px)
      fontWeight: 500, // 💪 Độ đậm: 500 (Font weight: 500)
    },
    body1: {
      // 📝 Body text style (mặc định cho <p>, <span>)
      // (Default style for <p>, <span>)
      fontSize: '1rem', // 📏 Kích thước body text: 1rem = 16px (Body text size: 1rem = 16px)
      lineHeight: 1.5, // 📏 Khoảng cách dòng: 1.5 (Line height: 1.5 - 1.5 times font size)
    },
  },

  // 📏 SPACING - Định nghĩa khoảng cách (Define spacing)
  spacing: 8,
  // 🔢 Base spacing unit: 8px (Base spacing unit: 8px)
  // 💡 Tất cả spacing trong MUI dựa trên giá trị này (All spacing in MUI is based on this value)
  // 💡 sx={{ p: 2 }} = padding: 16px (2 * 8) (sx={{ p: 2 }} = padding: 16px - 2 times base spacing)
  // 💡 sx={{ m: 3 }} = margin: 24px (3 * 8) (sx={{ m: 3 }} = margin: 24px - 3 times base spacing)

  // 📱 BREAKPOINTS - Responsive breakpoints (Điểm ngắt responsive)
  breakpoints: {
    // 💡 breakpoints: Định nghĩa các điểm ngắt cho responsive design (Define breakpoints for responsive design)
    values: {
      xs: 0, // 📱 Mobile: từ 0px trở lên (Mobile: from 0px and up)
      sm: 600, // 📱 Tablet: từ 600px trở lên (Tablet: from 600px and up)
      md: 900, // 💻 Desktop: từ 900px trở lên (Desktop: from 900px and up)
      lg: 1200, // 💻 Large desktop: từ 1200px trở lên (Large desktop: from 1200px and up)
      xl: 1536, // 💻 Extra large: từ 1536px trở lên (Extra large: from 1536px and up)
    },
  },

  // 🧩 COMPONENTS - Override default props cho components (Ghi đè props mặc định cho components)
  components: {
    // 💡 components: Tùy chỉnh default props và styles cho từng component (Customize default props and styles for each component)
    MuiButton: {
      // 🎯 Tùy chỉnh Button component (Customize Button component)
      defaultProps: {
        // 💡 defaultProps: Props mặc định cho tất cả Button (Default props for all Buttons)
        variant: 'contained', // 🎨 Mặc định dùng contained variant (có nền) (Default to contained variant - with background)
        size: 'medium', // 📏 Mặc định size medium (Default size: medium)
      },
      styleOverrides: {
        // 💡 styleOverrides: Ghi đè styles mặc định (Override default styles)
        root: {
          // 🎯 root: Style cho element gốc của Button (Style for Button's root element)
          textTransform: 'none', // 🔤 Không uppercase text - Giữ nguyên chữ hoa/thường (No text transform - keep original case)
          borderRadius: 8, // 📐 Bo góc 8px (Border radius: 8px)
        },
      },
    },
    MuiTextField: {
      // 🎯 Tùy chỉnh TextField component (Customize TextField component)
      defaultProps: {
        variant: 'outlined', // 🎨 Mặc định dùng outlined variant (có viền) (Default to outlined variant - with border)
      },
    },
  },
});

// 🎯 WRAP APP VỚI THEME PROVIDER (Bọc App với Theme Provider)
function App() {
  // 💡 Component gốc của app (Root component of app)

  return (
    <ThemeProvider theme={theme}>
      {/* 🎨 ThemeProvider: Cung cấp theme cho tất cả components bên trong
          (ThemeProvider: Provides theme to all components inside)
          💡 Tất cả components con có thể dùng theme qua useTheme() hook
          (All child components can use theme via useTheme() hook) */}
      <CssBaseline />
      {/* 🎨 Reset CSS và apply base styles
          (Reset CSS and apply base styles)
          💡 Xóa margin/padding mặc định của browser, set font family mặc định
          (Removes default browser margin/padding, sets default font family) */}
      <LoginForm /> {/* 📝 Component form đăng nhập (Login form component) */}
    </ThemeProvider>
  );
}

// 💡 USAGE TRONG COMPONENTS (Cách Sử Dụng Trong Components)
import { useTheme } from '@mui/material/styles';
// 📦 useTheme: Hook để lấy theme object trong component (Hook to get theme object in component)

function ThemedComponent() {
  // 💡 Component sử dụng theme (Component that uses theme)
  const theme = useTheme();
  // 🎨 Lấy theme object - Có thể truy cập palette, typography, spacing, breakpoints
  // (Get theme object - Can access palette, typography, spacing, breakpoints)

  return (
    <Box
      sx={{
        // 🎨 Dùng theme values (Use theme values)
        // 💡 sx prop: Styling prop của MUI, nhận object hoặc function
        // (sx prop: MUI styling prop, accepts object or function)

        color: theme.palette.primary.main,
        // 🔵 Màu primary - Lấy từ theme.palette.primary.main
        // (Primary color - Get from theme.palette.primary.main)

        backgroundColor: theme.palette.background.paper,
        // 📄 Màu nền paper - Lấy từ theme.palette.background.paper
        // (Paper background color - Get from theme.palette.background.paper)

        padding: theme.spacing(2),
        // 📏 Padding 16px (2 * 8) - theme.spacing(2) = 16px
        // (Padding 16px - theme.spacing(2) = 16px)

        // 📱 Responsive với breakpoints (Responsive with breakpoints)
        [theme.breakpoints.down('sm')]: {
          // 📱 Khi màn hình < 600px (When screen < 600px)
          // 💡 theme.breakpoints.down('sm'): Media query cho màn hình nhỏ hơn sm
          // (theme.breakpoints.down('sm'): Media query for screens smaller than sm)
          fontSize: '14px', // 📏 Font size nhỏ hơn cho mobile (Smaller font size for mobile)
        },
        [theme.breakpoints.up('md')]: {
          // 💻 Khi màn hình >= 900px (When screen >= 900px)
          // 💡 theme.breakpoints.up('md'): Media query cho màn hình lớn hơn hoặc bằng md
          // (theme.breakpoints.up('md'): Media query for screens >= md)
          fontSize: '18px', // 📏 Font size lớn hơn cho desktop (Larger font size for desktop)
        },
      }}
    >
      Responsive Text{' '}
      {/* 📝 Text thay đổi theo kích thước màn hình (Text that changes with screen size) */}
    </Box>
  );
}
```

### **2.3. Advanced Patterns**

```typescript
/**
 * 🚀 MUI ADVANCED PATTERNS - Production-ready patterns
 */

// ✅ PATTERN 1: Form với React Hook Form + MUI (Form with React Hook Form + MUI)
import { useForm, Controller } from 'react-hook-form';
// 📦 useForm: Hook quản lý form state và validation (Hook to manage form state and validation)
// 📦 Controller: Component để kết nối MUI components với React Hook Form (Component to connect MUI components with React Hook Form)
import { TextField, Button, Alert } from '@mui/material';
// 📦 Import MUI components (Import MUI components)

interface FormData {
  // 💡 Interface định nghĩa cấu trúc dữ liệu form (Interface defines form data structure)
  email: string; // 📧 Email field (Email field)
  password: string; // 🔒 Password field (Password field)
}

function LoginForm() {
  // 💡 Component form đăng nhập (Login form component)

  const {
    control, // 🎮 Controller để control MUI components - Quản lý state của form fields
    // (Controller to control MUI components - Manages form fields state)
    handleSubmit, // 📤 Handle form submission - Xử lý khi submit form
    // (Handle form submission - Processes form submission)
    formState: { errors }, // ❌ Form errors - Object chứa lỗi validation của từng field
    // (Form errors - Object containing validation errors for each field)
  } = useForm<FormData>();
  // 💡 useForm<FormData>: Khởi tạo form với type FormData (Initialize form with FormData type)

  const onSubmit = (data: FormData) => {
    // 💡 Hàm xử lý khi form submit thành công (Function to handle successful form submission)
    // 💡 data đã được validate, đảm bảo đúng format (data has been validated, ensures correct format)
    console.log('Form data:', data); // 📊 Data đã validate - In ra console (Validated data - Log to console)
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* 📝 HTML form element với handleSubmit wrapper
          (HTML form element with handleSubmit wrapper)
          💡 handleSubmit(onSubmit): Tự động validate trước khi gọi onSubmit
          (handleSubmit(onSubmit): Automatically validates before calling onSubmit) */}

      {/* 🎮 Controller wrapper cho MUI TextField (Controller wrapper for MUI TextField) */}
      <Controller
        name="email" // 🏷️ Field name - Tên field trong form state (Field name in form state)
        control={control} // 🎮 Control object từ useForm (Control object from useForm)
        rules={{
          // 💡 rules: Validation rules cho field này (Validation rules for this field)
          required: 'Email là bắt buộc',
          // ❌ Validation rule: Bắt buộc phải có giá trị (Required - must have value)
          pattern: {
            // 🔍 Pattern validation: Kiểm tra format email (Pattern validation: Check email format)
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            // 💡 Regex pattern: Kiểm tra format email hợp lệ (Regex pattern: Check valid email format)
            message: 'Email không hợp lệ', // ❌ Message lỗi nếu không match pattern (Error message if pattern doesn't match)
          },
        }}
        render={(
          { field } // 🎨 Render function - Nhận field object chứa value, onChange, onBlur...
        ) => (
          // (Render function - Receives field object containing value, onChange, onBlur...)
          <TextField
            {...field}
            // 📤 Spread field props: value, onChange, onBlur, name, ref
            // (Spread field props: value, onChange, onBlur, name, ref)
            // 💡 Tự động bind value và event handlers với React Hook Form
            // (Automatically binds value and event handlers with React Hook Form)
            label="Email" // 🏷️ Label hiển thị trên input (Label displayed on input)
            error={!!errors.email}
            // ❌ Hiển lỗi nếu có - !!errors.email convert thành boolean
            // (Show error if exists - !!errors.email converts to boolean)
            helperText={errors.email?.message}
            // 📝 Hiển message lỗi - Optional chaining để tránh lỗi nếu errors.email = undefined
            // (Display error message - Optional chaining to avoid error if errors.email = undefined)
            fullWidth // 📏 Chiếm full width (Full width)
            margin="normal" // 📏 Margin: normal (có margin), dense (margin nhỏ), none (không margin)
            // (Margin: normal - has margin, dense - small margin, none - no margin)
          />
        )}
      />

      <Controller
        name="password" // 🏷️ Field name: password (Field name: password)
        control={control} // 🎮 Control object (Control object)
        rules={{
          // 💡 Validation rules cho password field (Validation rules for password field)
          required: 'Password là bắt buộc',
          // ❌ Bắt buộc phải có giá trị (Required - must have value)
          minLength: {
            // 📏 Minimum length validation (Minimum length validation)
            value: 8, // 🔢 Độ dài tối thiểu: 8 ký tự (Minimum length: 8 characters)
            message: 'Password phải có ít nhất 8 ký tự',
            // ❌ Message lỗi nếu độ dài < 8 (Error message if length < 8)
          },
        }}
        render={({ field }) => (
          // 💡 Render function nhận field object (Render function receives field object)
          <TextField
            {...field}
            // 📤 Spread field props: value, onChange, onBlur, name, ref
            // (Spread field props: value, onChange, onBlur, name, ref)
            type="password"
            // 🔒 Type: password - Ẩn ký tự khi gõ (Type: password - Hides characters when typing)
            label="Password" // 🏷️ Label: Password (Label: Password)
            error={!!errors.password}
            // ❌ Hiển lỗi nếu có (Show error if exists)
            helperText={errors.password?.message}
            // 📝 Hiển message lỗi (Display error message)
            fullWidth // 📏 Chiếm full width (Full width)
            margin="normal" // 📏 Margin: normal (Margin: normal)
          />
        )}
      />

      {errors.root && (
        // ❌ Global errors - Lỗi toàn cục (không thuộc field cụ thể)
        // (Global errors - Global errors not belonging to specific field)
        // 💡 errors.root: Lỗi từ server hoặc validation custom
        // (errors.root: Errors from server or custom validation)
        <Alert severity="error">
          {/* 🚨 Alert component hiển thị lỗi (Alert component displays error)
              💡 severity="error": Màu đỏ, icon lỗi (severity="error": Red color, error icon) */}
          {errors.root.message}
          {/* 📝 Hiển message lỗi toàn cục (Display global error message) */}
        </Alert>
      )}

      <Button
        type="submit"
        // 📤 Type: submit - Kích hoạt form submission (Type: submit - Triggers form submission)
        variant="contained"
        // 🎨 Variant: contained (có nền) (Variant: contained - with background)
        fullWidth
        // 📏 Chiếm full width (Full width)
      >
        Login {/* 📝 Nội dung button (Button content) */}
      </Button>
    </form>
  );
}

// ✅ PATTERN 2: Data Table với MUI Table (Data Table with MUI Table)
import {
  Table, // 📊 Table component - Container cho table (Table component - Container for table)
  TableBody, // 📋 TableBody - Body của table (chứa data rows) (TableBody - Body of table containing data rows)
  TableCell, // 📄 TableCell - Cell trong table (TableCell - Cell in table)
  TableContainer, // 📦 TableContainer - Container với scroll (TableContainer - Container with scroll)
  TableHead, // 📑 TableHead - Header của table (chứa column headers) (TableHead - Header of table containing column headers)
  TableRow, // 📊 TableRow - Row trong table (TableRow - Row in table)
  TableSortLabel, // 🔄 TableSortLabel - Header với sort functionality (TableSortLabel - Header with sort functionality)
  Paper, // 📄 Paper - Card-like container (Paper - Card-like container)
} from '@mui/material';

interface Data {
  // 💡 Interface định nghĩa cấu trúc dữ liệu (Interface defines data structure)
  id: number; // 🔑 ID duy nhất (Unique ID)
  name: string; // 👤 Tên (Name)
  email: string; // 📧 Email (Email)
  role: string; // 🎭 Vai trò (Role)
}

function DataTable({ rows }: { rows: Data[] }) {
  // 💡 Component hiển thị bảng dữ liệu (Component displays data table)
  // 💡 rows: Props nhận array Data[] (rows: Props receives Data[] array)

  const [orderBy, setOrderBy] = useState<keyof Data>('name');
  // 📊 Cột đang sort - keyof Data đảm bảo chỉ sort theo key hợp lệ
  // (Column being sorted - keyof Data ensures only sorting by valid keys)
  // 💡 'name' là giá trị mặc định (default value)

  const [order, setOrder] = useState<'asc' | 'desc'>('asc');
  // 🔄 Hướng sort: 'asc' (tăng dần) hoặc 'desc' (giảm dần)
  // (Sort direction: 'asc' - ascending or 'desc' - descending)
  // 💡 'asc' là giá trị mặc định (default value)

  // 🔄 Handle sort click (Xử lý khi click sort)
  const handleSort = (property: keyof Data) => {
    // 💡 property: Tên cột muốn sort (property: Column name to sort)
    const isAsc = orderBy === property && order === 'asc';
    // 💡 Kiểm tra: Nếu đang sort cột này và đang tăng dần → đổi thành giảm dần
    // (Check: If sorting this column and ascending → change to descending)
    setOrder(isAsc ? 'desc' : 'asc');
    // 🔄 Đổi hướng sort (Change sort direction)
    setOrderBy(property);
    // 📊 Set cột đang sort (Set column being sorted)
  };

  // 📊 Sort rows (Sắp xếp rows)
  const sortedRows = [...rows].sort((a, b) => {
    // 💡 [...rows]: Tạo copy của array để không mutate original (Create copy to avoid mutating original)
    // 💡 .sort(): Sắp xếp array (Sort array)
    if (order === 'asc') {
      // 📈 Nếu sort tăng dần (If ascending sort)
      return a[orderBy] > b[orderBy] ? 1 : -1;
      // 💡 So sánh: a > b → return 1 (a đứng sau b), ngược lại return -1 (a đứng trước b)
      // (Compare: a > b → return 1 - a after b, otherwise return -1 - a before b)
    }
    // 📉 Nếu sort giảm dần (If descending sort)
    return a[orderBy] < b[orderBy] ? 1 : -1;
    // 💡 So sánh ngược lại: a < b → return 1 (a đứng sau b)
    // (Compare reverse: a < b → return 1 - a after b)
  });

  return (
    <TableContainer component={Paper}>
      {/* 📦 TableContainer: Container với scroll khi table quá lớn
          (TableContainer: Container with scroll when table is too large)
          💡 component={Paper}: Dùng Paper làm container (có shadow, border radius)
          (component={Paper}: Use Paper as container - has shadow, border radius) */}
      <Table>
        {/* 📊 Table: Component table chính (Main table component) */}
        <TableHead>
          {/* 📑 TableHead: Header của table (chứa column headers)
              (TableHead: Header of table containing column headers) */}
          <TableRow>
            {/* 📊 TableRow: Row trong header (Row in header) */}
            <TableCell>
              {/* 📄 TableCell: Cell trong header (Cell in header) */}
              <TableSortLabel
                active={orderBy === 'name'}
                // ✅ Highlight nếu đang sort cột này - active={true} khi orderBy === 'name'
                // (Highlight if sorting this column - active={true} when orderBy === 'name')
                direction={orderBy === 'name' ? order : 'asc'}
                // 🔄 Hiển mũi tên sort - 'asc' (↑) hoặc 'desc' (↓)
                // (Display sort arrow - 'asc' (↑) or 'desc' (↓))
                // 💡 Nếu đang sort cột này → hiển order hiện tại, ngược lại → 'asc'
                // (If sorting this column → show current order, otherwise → 'asc')
                onClick={() => handleSort('name')}
                // 🖱️ Click để sort cột 'name' (Click to sort 'name' column)
              >
                Name {/* 📝 Tên cột (Column name) */}
              </TableSortLabel>
            </TableCell>
            <TableCell>Email</TableCell>
            {/* 📄 Cell: Email - Không có sort (Cell: Email - No sort) */}
            <TableCell>Role</TableCell>
            {/* 📄 Cell: Role - Không có sort (Cell: Role - No sort) */}
          </TableRow>
        </TableHead>
        <TableBody>
          {/* 📋 TableBody: Body của table (chứa data rows)
              (TableBody: Body of table containing data rows) */}
          {sortedRows.map((row) => (
            // 💡 .map(): Render mỗi row trong sortedRows (Render each row in sortedRows)
            <TableRow key={row.id}>
              {/* 📊 TableRow: Row chứa data (Row containing data)
                  💡 key={row.id}: React key để optimize re-render (React key to optimize re-render) */}
              <TableCell>{row.name}</TableCell>
              {/* 📄 Cell: Hiển tên (Cell: Display name) */}
              <TableCell>{row.email}</TableCell>
              {/* 📄 Cell: Hiển email (Cell: Display email) */}
              <TableCell>{row.role}</TableCell>
              {/* 📄 Cell: Hiển role (Cell: Display role) */}
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

// ✅ PATTERN 3: Responsive Layout với MUI Grid (Responsive Layout with MUI Grid)
import { Grid, Container } from '@mui/material';
// 📦 Grid: Component grid system (12 columns) (Grid: Grid system component - 12 columns)
// 📦 Container: Container với max width và padding (Container with max width and padding)

function ResponsiveLayout() {
  // 💡 Component layout responsive (Responsive layout component)

  return (
    <Container maxWidth="lg">
      {/* 📦 Container: Container với max width
          (Container: Container with max width)
          💡 maxWidth="lg": Max width = 1200px (theo MUI breakpoints)
          (maxWidth="lg": Max width = 1200px according to MUI breakpoints)
          💡 Tự động center và có padding (Automatically centered with padding) */}
      <Grid container spacing={3}>
        {/* 📊 Grid container: Container cho grid system
            (Grid container: Container for grid system)
            💡 container: Bật grid layout (Enables grid layout)
            💡 spacing={3}: Khoảng cách giữa các items = 24px (3 * 8px)
            (spacing={3}: Gap between items = 24px - 3 times base spacing) */}

        {/* 📱 Responsive Grid Items:
            (Responsive Grid Items:)
            💡 xs={12}: Mobile (0px+): 12/12 cols = 100% width (full width)
            (xs={12}: Mobile (0px+): 12/12 cols = 100% width)
            💡 sm={6}: Tablet (600px+): 6/12 cols = 50% width
            (sm={6}: Tablet (600px+): 6/12 cols = 50% width)
            💡 md={4}: Desktop (900px+): 4/12 cols = 33.33% width
            (md={4}: Desktop (900px+): 4/12 cols = 33.33% width) */}

        <Grid item xs={12} sm={6} md={4}>
          {/* 📊 Grid item: Item trong grid (Grid item: Item in grid)
              💡 item: Bật grid item (Enables grid item)
              💡 xs={12}: Mobile = full width (Mobile = full width)
              💡 sm={6}: Tablet = 50% width (Tablet = 50% width)
              💡 md={4}: Desktop = 33% width (Desktop = 33% width) */}
          <Paper>Card 1</Paper>
          {/* 📄 Paper: Card component (Card component) */}
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          {/* 📊 Grid item thứ 2 (Second grid item) */}
          <Paper>Card 2</Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          {/* 📊 Grid item thứ 3 (Third grid item) */}
          <Paper>Card 3</Paper>
        </Grid>
      </Grid>
    </Container>
  );
}
```

---

## 3. Ant Design

### **3.1. Overview**

```typescript
/**
 * 🎨 ANT DESIGN = Component library cho enterprise admin dashboards
 *
 * ✅ ƯU ĐIỂM:
 * - Enterprise focus: Components phù hợp admin dashboards
 * - Rich components: Form, Table, DatePicker, Charts...
 * - Chinese origin: Popular ở Trung Quốc, Đông Nam Á
 * - Documentation: Tài liệu chi tiết, nhiều examples
 * - TypeScript: Full TypeScript support
 *
 * ❌ NHƯỢC ĐIỂM:
 * - Bundle size: Rất lớn (~500KB gzipped)
 * - Design: Ant Design style (có thể không phù hợp mọi brand)
 * - Customization: Khó customize sâu
 * - Less popular: Ít popular hơn MUI ở phương Tây
 *
 * 🎯 USE CASES:
 * - Admin dashboards
 * - Data-heavy applications
 * - Enterprise internal tools
 * - Apps cần nhiều form/table components
 */

// 📦 INSTALLATION
// npm install antd

// ✅ BASIC USAGE (Cách Sử Dụng Cơ Bản)
import { Button, Input, Form, Table, DatePicker } from 'antd';
// 📦 Import các components từ Ant Design (Import components from Ant Design)
import 'antd/dist/reset.css';
// 🎨 Import CSS - Reset styles và apply Ant Design styles
// (Import CSS - Reset styles and apply Ant Design styles)
// 💡 Hoặc dùng CSS-in-JS (Or use CSS-in-JS)

function AdminDashboard() {
  // 💡 Component dashboard quản trị (Admin dashboard component)

  return (
    <div>
      <Form
        layout="vertical"
        // 📋 Layout: vertical (label trên input), horizontal (label bên cạnh), inline (cùng dòng)
        // (Layout: vertical - label above input, horizontal - label beside, inline - same line)
        onFinish={(values) => {
          // 📤 Callback khi form submit thành công (Callback when form submits successfully)
          // 💡 values: Object chứa tất cả form values (Object containing all form values)
          console.log('Form values:', values); // 📊 In ra console (Log to console)
        }}
      >
        <Form.Item
          // 📋 Form.Item: Wrapper cho form field (Wrapper for form field)
          label="Username"
          // 🏷️ Label hiển thị cho field (Label displayed for field)
          name="username"
          // 🔑 Tên field trong form state (Field name in form state)
          rules={[{ required: true, message: 'Vui lòng nhập username' }]}
          // ❌ Validation rules: required = bắt buộc, message = message lỗi
          // (Validation rules: required = mandatory, message = error message)
        >
          <Input placeholder="Enter username" />
          {/* 📝 Input component - placeholder hiển thị khi input trống
              (Input component - placeholder displays when input is empty) */}
        </Form.Item>

        <Form.Item
          label="Password" // 🏷️ Label: Password (Label: Password)
          name="password" // 🔑 Field name: password (Field name: password)
          rules={[{ required: true, message: 'Vui lòng nhập password' }]}
          // ❌ Validation: Bắt buộc (Validation: Required)
        >
          <Input.Password placeholder="Enter password" />
          {/* 🔒 Input.Password: Input type password (ẩn ký tự)
              (Input.Password: Password input type - hides characters)
              💡 Có icon eye để show/hide password (Has eye icon to show/hide password) */}
        </Form.Item>

        <Form.Item>
          {/* 📋 Form.Item không có label/name: Container cho button
              (Form.Item without label/name: Container for button) */}
          <Button
            type="primary"
            // 🎨 Type: primary (màu chính), default, dashed, link, text
            // (Type: primary - main color, default, dashed, link, text)
            htmlType="submit"
            // 📤 htmlType: submit - Kích hoạt form submission
            // (htmlType: submit - Triggers form submission)
          >
            Submit {/* 📝 Nội dung button (Button content) */}
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
}
```

### **3.2. Advanced Table Features**

```typescript
/**
 * 📊 ANT DESIGN TABLE - Powerful data table với nhiều features
 */

import { Table, Button, Space, Tag } from 'antd';
// 📦 Import Ant Design components (Import Ant Design components)
import type { ColumnsType } from 'antd/es/table';
// 📦 ColumnsType: Type cho columns definition (Type for columns definition)

interface User {
  // 💡 Interface định nghĩa cấu trúc User (Interface defines User structure)
  id: number; // 🔑 ID duy nhất (Unique ID)
  name: string; // 👤 Tên (Name)
  email: string; // 📧 Email (Email)
  status: 'active' | 'inactive'; // 🎭 Trạng thái: active hoặc inactive (Status: active or inactive)
  createdAt: string; // 📅 Ngày tạo (Created date)
}

function UserTable() {
  // 💡 Component bảng người dùng (User table component)

  const columns: ColumnsType<User> = [
    // 💡 columns: Định nghĩa các cột của table (Defines table columns)
    // 💡 ColumnsType<User>: Type-safe với User interface (Type-safe with User interface)
    {
      title: 'ID', // 📝 Tiêu đề cột (Column title)
      dataIndex: 'id',
      // 🔑 Key trong data object - Lấy giá trị từ row.id
      // (Key in data object - Gets value from row.id)
      key: 'id',
      // 🔑 React key cho column (React key for column)
      sorter: (a, b) => a.id - b.id,
      // 🔄 Sorting function - Sắp xếp theo ID (tăng dần)
      // (Sorting function - Sort by ID ascending)
      // 💡 a.id - b.id: Số dương nếu a > b, số âm nếu a < b
      // (a.id - b.id: Positive if a > b, negative if a < b)
      width: 80,
      // 📏 Độ rộng cột: 80px (Column width: 80px)
    },
    {
      title: 'Name', // 📝 Tiêu đề cột: Name (Column title: Name)
      dataIndex: 'name',
      // 🔑 Key trong data object - Lấy giá trị từ row.name
      // (Key in data object - Gets value from row.name)
      key: 'name', // 🔑 React key (React key)
      sorter: (a, b) => a.name.localeCompare(b.name),
      // 🔄 Sorting function - Sắp xếp theo tên (alphabetical)
      // (Sorting function - Sort by name alphabetically)
      // 💡 localeCompare(): So sánh chuỗi theo locale (locale-aware string comparison)
      filterDropdown: ({ setSelectedKeys, selectedKeys, confirm }) => (
        // 🔍 Custom filter dropdown - Dropdown tùy chỉnh cho filter
        // (Custom filter dropdown - Custom dropdown for filter)
        // 💡 setSelectedKeys: Set giá trị filter (Set filter value)
        // 💡 selectedKeys: Giá trị filter hiện tại (Current filter value)
        // 💡 confirm: Xác nhận filter (Confirm filter)
        <div style={{ padding: 8 }}>
          {/* 📦 Container với padding (Container with padding) */}
          <Input
            placeholder="Search name"
            // 📝 Placeholder: Tìm kiếm tên (Placeholder: Search name)
            value={selectedKeys[0]}
            // 💡 Giá trị input = giá trị filter đầu tiên (Input value = first filter value)
            onChange={
              (e) => setSelectedKeys(e.target.value ? [e.target.value] : [])
              // 💡 Khi thay đổi input → update filter value
              // (When input changes → update filter value)
              // 💡 Nếu có giá trị → set array [value], ngược lại → []
              // (If has value → set array [value], otherwise → [])
            }
            onPressEnter={() => confirm()}
            // ⌨️ Khi nhấn Enter → xác nhận filter (When press Enter → confirm filter)
          />
        </div>
      ),
      onFilter: (value, record) =>
        // 🔍 Filter function - Lọc rows dựa trên giá trị filter
        // (Filter function - Filter rows based on filter value)
        // 💡 value: Giá trị filter (Filter value)
        // 💡 record: Row data (Row data)
        record.name.toLowerCase().includes(value.toString().toLowerCase()),
      // 💡 Kiểm tra: Tên có chứa giá trị filter (không phân biệt hoa/thường)
      // (Check: Name contains filter value - case insensitive)
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
    },
    {
      title: 'Status', // 📝 Tiêu đề cột: Status (Column title: Status)
      dataIndex: 'status',
      // 🔑 Key trong data object - Lấy giá trị từ row.status
      // (Key in data object - Gets value from row.status)
      key: 'status', // 🔑 React key (React key)
      render: (
        status: string // 🎨 Custom render function - Hàm render tùy chỉnh
        // 💡 status: Giá trị của field status (Value of status field)
      ) => (
        <Tag color={status === 'active' ? 'green' : 'red'}>
          {/* 🏷️ Tag component - Hiển thị status với màu
              (Tag component - Display status with color)
              💡 color: green nếu active, red nếu inactive
              (color: green if active, red if inactive) */}
          {status.toUpperCase()}
          {/* 📝 Hiển status dạng chữ hoa (Display status in uppercase) */}
        </Tag>
      ),
      filters: [
        // 🔍 Filter options - Các tùy chọn filter
        // (Filter options - Filter choices)
        { text: 'Active', value: 'active' },
        // 📝 Option 1: Active (text hiển thị, value để filter)
        // (Option 1: Active - display text, value for filtering)
        { text: 'Inactive', value: 'inactive' },
        // 📝 Option 2: Inactive (Option 2: Inactive)
      ],
      onFilter: (value, record) => record.status === value,
      // 🔍 Filter function - Lọc rows có status = value
      // (Filter function - Filter rows with status = value)
    },
    {
      title: 'Actions', // 📝 Tiêu đề cột: Actions (Column title: Actions)
      key: 'actions',
      // 🔑 React key - Không có dataIndex vì không lấy từ data
      // (React key - No dataIndex because not getting from data)
      render: (
        _,
        // 💡 _: Giá trị cell (không dùng vì không có dataIndex)
        // (Cell value - not used because no dataIndex)
        record // 🎨 Render actions column - Record data (toàn bộ row)
        // 💡 record: Toàn bộ row data (Entire row data)
      ) => (
        <Space>
          {/* 📦 Space: Container với spacing giữa các buttons
              (Space: Container with spacing between buttons) */}
          <Button
            size="small"
            // 📏 Size: small (nhỏ), middle (trung bình), large (lớn)
            // (Size: small, middle, large)
            onClick={() => handleEdit(record.id)}
            // 🖱️ Click handler - Gọi hàm edit với record.id
            // (Click handler - Call edit function with record.id)
          >
            Edit {/* 📝 Nội dung button (Button content) */}
          </Button>
          <Button
            size="small"
            danger
            // ⚠️ danger: Màu đỏ (danger color - red)
            onClick={() => handleDelete(record.id)}
            // 🖱️ Click handler - Gọi hàm delete với record.id
            // (Click handler - Call delete function with record.id)
          >
            Delete {/* 📝 Nội dung button (Button content) */}
          </Button>
        </Space>
      ),
    },
  ];

  const data: User[] = [
    // 💡 data: Array chứa dữ liệu hiển thị trong table (Array containing data to display in table)
    {
      id: 1, // 🔑 ID: 1 (ID: 1)
      name: 'John Doe', // 👤 Tên: John Doe (Name: John Doe)
      email: 'john@example.com', // 📧 Email: john@example.com (Email: john@example.com)
      status: 'active', // 🎭 Trạng thái: active (Status: active)
      createdAt: '2024-01-01', // 📅 Ngày tạo: 2024-01-01 (Created date: 2024-01-01)
    },
    {
      id: 2, // 🔑 ID: 2 (ID: 2)
      name: 'Jane Smith', // 👤 Tên: Jane Smith (Name: Jane Smith)
      email: 'jane@example.com', // 📧 Email: jane@example.com (Email: jane@example.com)
      status: 'inactive', // 🎭 Trạng thái: inactive (Status: inactive)
      createdAt: '2024-01-02', // 📅 Ngày tạo: 2024-01-02 (Created date: 2024-01-02)
    },
  ];

  return (
    <Table
      columns={columns}
      // 📋 columns: Định nghĩa các cột (Column definitions)
      dataSource={data}
      // 📊 dataSource: Dữ liệu hiển thị (Data to display)
      rowKey="id"
      // 🔑 Unique key cho mỗi row - Dùng id làm key
      // (Unique key for each row - Use id as key)
      // 💡 React cần key để optimize re-render (React needs key to optimize re-render)
      pagination={{
        // 📄 Pagination: Phân trang (Pagination: Page navigation)
        pageSize: 10,
        // 📄 Số rows mỗi trang: 10 rows (Number of rows per page: 10 rows)
        showSizeChanger: true,
        // ✅ Cho phép đổi page size - Hiển dropdown để chọn số rows/trang
        // (Allow changing page size - Show dropdown to select rows per page)
        showTotal: (total) => `Total ${total} items`,
        // 📊 Hiển tổng số items - Function nhận total và return string
        // (Display total items - Function receives total and returns string)
        // 💡 Ví dụ: "Total 25 items" (Example: "Total 25 items")
      }}
      scroll={{ x: 800 }}
      // 📱 Horizontal scroll khi màn hình nhỏ - x: 800 = min width 800px
      // (Horizontal scroll when screen is small - x: 800 = min width 800px)
      // 💡 Khi table width > viewport → hiển horizontal scrollbar
      // (When table width > viewport → show horizontal scrollbar)
    />
  );
}
```

---

## 4. Chakra UI

### **4.1. Overview**

```typescript
/**
 * 🎨 CHAKRA UI = Simple, modular component library
 *
 * ✅ ƯU ĐIỂM:
 * - Simple API: Dễ học, dễ dùng
 * - Props-based styling: Không cần CSS, style qua props
 * - Accessibility: Built-in a11y support
 * - Bundle size: Medium (~150KB)
 * - Customizable: Dễ customize
 * - Dark mode: Built-in dark mode support
 *
 * ❌ NHƯỢC ĐIỂM:
 * - Less components: Ít components hơn MUI/Ant Design
 * - Design: Không theo design system cụ thể
 * - Community: Nhỏ hơn MUI
 *
 * 🎯 USE CASES:
 * - Modern web apps
 * - Startups/MVPs
 * - Apps cần custom design
 * - Projects dùng Emotion (CSS-in-JS)
 */

// 📦 INSTALLATION
// npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion

// ✅ SETUP (Thiết Lập)
import { ChakraProvider, extendTheme } from '@chakra-ui/react';
// 📦 ChakraProvider: Cung cấp theme cho toàn bộ app (Provides theme to entire app)
// 📦 extendTheme: Mở rộng theme mặc định (Extends default theme)

const theme = extendTheme({
  // 💡 extendTheme(): Mở rộng theme mặc định với custom config (Extends default theme with custom config)
  colors: {
    // 🎨 colors: Định nghĩa màu sắc tùy chỉnh (Define custom colors)
    brand: {
      // 💡 brand: Tên color scheme tùy chỉnh (Custom color scheme name)
      50: '#e3f2fd',
      // 🎨 Color scale (50-900) - Màu nhạt nhất (Lightest color)
      // 💡 50: Màu nhạt nhất, dùng cho hover states (Lightest color, used for hover states)
      100: '#bbdefb',
      // 🎨 Màu nhạt (Light color)
      500: '#2196f3',
      // 🔵 Main color - Màu chính (Main color)
      // 💡 500: Màu chính, dùng cho buttons, links (Main color, used for buttons, links)
      900: '#0d47a1',
      // 🎨 Màu đậm nhất (Darkest color)
      // 💡 900: Màu đậm nhất, dùng cho text trên nền sáng (Darkest color, used for text on light background)
    },
  },
});

function App() {
  // 💡 Component gốc của app (Root component of app)
  return (
    <ChakraProvider theme={theme}>
      {/* 🎨 ChakraProvider: Cung cấp theme cho tất cả components bên trong
          (ChakraProvider: Provides theme to all components inside)
          💡 Tất cả Chakra components có thể dùng theme colors, spacing...
          (All Chakra components can use theme colors, spacing...) */}
      <YourApp /> {/* 📝 Component app của bạn (Your app component) */}
    </ChakraProvider>
  );
}

// ✅ BASIC USAGE (Cách Sử Dụng Cơ Bản)
import {
  Button, // 🔘 Button component (Button component)
  Input, // 📝 Input component (Input component)
  Box, // 📦 Box component (div với styling props) (Box component - div with styling props)
  Stack, // 📊 Stack component (flex container) (Stack component - flex container)
  FormControl, // 📋 FormControl component (wrapper cho form field) (FormControl - wrapper for form field)
  FormLabel, // 🏷️ FormLabel component (label cho form field) (FormLabel - label for form field)
} from '@chakra-ui/react';

function LoginForm() {
  // 💡 Component form đăng nhập (Login form component)

  return (
    <Box p={4}>
      {/* 📦 Box = div với styling props
          (Box = div with styling props)
          💡 p={4}: padding = 16px (4 * 4px base spacing)
          (p={4}: padding = 16px - 4 times base spacing of 4px) */}
      <Stack spacing={4}>
        {/* 📊 Stack = flex container với spacing
            (Stack = flex container with spacing)
            💡 spacing={4}: Khoảng cách giữa các items = 16px (4 * 4px)
            (spacing={4}: Gap between items = 16px - 4 times base spacing) */}

        <FormControl>
          {/* 📋 FormControl: Wrapper cho form field (có label, error handling)
              (FormControl: Wrapper for form field - has label, error handling) */}
          <FormLabel>Email</FormLabel>
          {/* 🏷️ FormLabel: Label cho input (Label for input) */}
          <Input
            type="email"
            // 📧 Type: email - Kiểm tra format email (Type: email - Validates email format)
            placeholder="Enter email"
            // 📝 Placeholder: Hiển khi input trống (Placeholder: Displays when input is empty)
          />
        </FormControl>

        <FormControl>
          {/* 📋 FormControl: Wrapper cho password field (FormControl: Wrapper for password field) */}
          <FormLabel>Password</FormLabel>
          {/* 🏷️ FormLabel: Label cho password (Label for password) */}
          <Input
            type="password"
            // 🔒 Type: password - Ẩn ký tự khi gõ (Type: password - Hides characters when typing)
            placeholder="Enter password"
            // 📝 Placeholder: Hiển khi input trống (Placeholder: Displays when input is empty)
          />
        </FormControl>

        <Button
          colorScheme="blue"
          // 🎨 Color scheme: blue (màu xanh), green, red, purple...
          // (Color scheme: blue, green, red, purple...)
          // 💡 colorScheme tự động tạo các variants: 50, 100, 500, 900
          // (colorScheme automatically creates variants: 50, 100, 500, 900)
          size="lg"
          // 📏 Size: sm (nhỏ), md (trung bình), lg (lớn)
          // (Size: sm - small, md - medium, lg - large)
          width="full"
          // 📏 Full width - Chiếm 100% width của container
          // (Full width - Takes 100% width of container)
        >
          Login {/* 📝 Nội dung button (Button content) */}
        </Button>
      </Stack>
    </Box>
  );
}
```

### **4.2. Props-based Styling**

```typescript
/**
 * 🎨 CHAKRA UI PROPS-BASED STYLING - Style components qua props
 *
 * 💡 Không cần CSS, style trực tiếp qua props
 * 💡 Responsive: Dùng array values [mobile, tablet, desktop]
 */

import { Box, Button, Text, Flex } from '@chakra-ui/react';

function ResponsiveComponent() {
  // 💡 Component responsive với props-based styling (Responsive component with props-based styling)

  return (
    <Box
      // 📦 Box component - div với styling props (Box component - div with styling props)

      // 📏 SPACING - Padding, margin qua props (Spacing - Padding, margin via props)
      p={4}
      // 📱 Padding: 16px (4 * 4px base spacing)
      // (Padding: 16px - 4 times base spacing of 4px)
      // 💡 p = padding all sides (padding tất cả các phía)
      m={2}
      // 📱 Margin: 8px (2 * 4px)
      // (Margin: 8px - 2 times base spacing)
      // 💡 m = margin all sides (margin tất cả các phía)
      px={6}
      // 📱 Padding horizontal: 24px (6 * 4px) - padding left & right
      // (Padding horizontal: 24px - padding left & right)
      // 💡 px = padding x-axis (padding trục x)
      py={8}
      // 📱 Padding vertical: 32px (8 * 4px) - padding top & bottom
      // (Padding vertical: 32px - padding top & bottom)
      // 💡 py = padding y-axis (padding trục y)

      // 🎨 COLORS (Màu sắc)
      bg="blue.500"
      // 🔵 Background color: blue.500 (từ theme)
      // (Background color: blue.500 from theme)
      // 💡 blue.500 = màu chính của blue color scheme (main color of blue color scheme)
      color="white"
      // ⚪ Text color: white (Màu chữ: trắng)
      // (Text color: white)

      // 📐 BORDERS (Viền)
      borderWidth="1px"
      // 📏 Border width: 1px (Độ dày viền: 1px)
      // (Border width: 1px)
      borderColor="gray.200"
      // 🎨 Border color: gray.200 (từ theme) (Màu viền: gray.200 từ theme)
      // (Border color: gray.200 from theme)
      borderRadius="md"
      // 📐 Border radius: md = 8px (Bo góc: md = 8px)
      // (Border radius: md = 8px)
      // 💡 md = medium (trung bình)

      // 📱 RESPONSIVE - Array values [mobile, tablet, desktop]
      // (Responsive - Array values [mobile, tablet, desktop])
      width={['100%', '50%', '33%']}
      // 📱 Mobile (0px+): 100% width, Tablet (768px+): 50% width, Desktop (1024px+): 33% width
      // (Mobile: 100% width, Tablet: 50% width, Desktop: 33% width)
      // 💡 Array index: [0] = mobile, [1] = tablet, [2] = desktop
      fontSize={['14px', '16px', '18px']}
      // 📱 Responsive font size: Mobile 14px, Tablet 16px, Desktop 18px
      // (Responsive font size: Mobile 14px, Tablet 16px, Desktop 18px)

      // 🎨 SHADOWS (Bóng đổ)
      boxShadow="md"
      // 🌑 Shadow: md (medium) - sm (small), md (medium), lg (large), xl (extra large)
      // (Shadow: md - sm, md, lg, xl)

      // 🖱️ HOVER STATES (Trạng thái hover)
      _hover={{
        // 🎯 Pseudo-class hover - Styles khi hover chuột
        // (Pseudo-class hover - Styles when hovering mouse)
        bg: 'blue.600',
        // 🔵 Đổi màu nền khi hover: blue.600 (darker blue)
        // (Change background color on hover: blue.600 - darker blue)
        transform: 'scale(1.05)',
        // 🔄 Phóng to khi hover: scale 1.05 (tăng 5%)
        // (Scale up on hover: scale 1.05 - increase 5%)
      }}
      // 🎯 FOCUS STATES (Trạng thái focus)
      _focus={{
        // 🎯 Pseudo-class focus - Styles khi focus (keyboard navigation)
        // (Pseudo-class focus - Styles when focused - keyboard navigation)
        outline: '2px solid',
        // 📐 Outline: 2px solid (Viền focus: 2px solid)
        // (Outline: 2px solid)
        outlineColor: 'blue.500',
        // 🎨 Màu outline: blue.500 (Màu viền focus: blue.500)
        // (Outline color: blue.500)
      }}
    >
      Responsive Box {/* 📝 Nội dung (Content) */}
    </Box>
  );
}

// ✅ COMPONENT COMPOSITION (Kết Hợp Components)
function Card({ children }: { children: React.ReactNode }) {
  // 💡 Component Card tái sử dụng được (Reusable Card component)
  // 💡 children: Nội dung bên trong Card (Content inside Card)

  return (
    <Box
      p={6}
      // 📏 Padding: 24px (6 * 4px) (Padding: 24px)
      bg="white"
      // ⚪ Background: white (Nền: trắng)
      borderRadius="lg"
      // 📐 Border radius: lg = 16px (Bo góc: lg = 16px)
      boxShadow="lg"
      // 🌑 Shadow: lg (large) - Bóng đổ lớn (Large shadow)
      _hover={{
        // 🖱️ Hover state (Trạng thái hover)
        boxShadow: 'xl',
        // 🌑 Shadow: xl (extra large) - Bóng đổ lớn hơn khi hover
        // (Shadow: xl - larger shadow on hover)
        transform: 'translateY(-4px)',
        // 🔄 Di chuyển lên 4px khi hover (Move up 4px on hover)
        // (Transform: translateY(-4px) - move up 4px)
        transition: 'all 0.2s',
        // ⏱️ Transition: 0.2s cho tất cả properties (Smooth animation)
        // (Transition: 0.2s for all properties - smooth animation)
      }}
    >
      {children}
      {/* 📝 Hiển nội dung children (Display children content) */}
    </Box>
  );
}

function ProductCard({ product }: { product: Product }) {
  // 💡 Component card sản phẩm (Product card component)
  // 💡 product: Props nhận product object (Props receives product object)

  return (
    <Card>
      {/* 📦 Sử dụng Card component (Use Card component) */}
      <Text fontSize="xl" fontWeight="bold">
        {/* 📝 Text component - fontSize: xl (extra large), fontWeight: bold (đậm)
            (Text component - fontSize: xl, fontWeight: bold) */}
        {product.name}
        {/* 📝 Hiển tên sản phẩm (Display product name) */}
      </Text>
      <Text color="gray.600" mt={2}>
        {/* 📝 Text component - color: gray.600, mt={2} = margin-top: 8px
            (Text component - color: gray.600, mt={2} = margin-top: 8px) */}
        {product.description}
        {/* 📝 Hiển mô tả sản phẩm (Display product description) */}
      </Text>
      <Flex justify="space-between" align="center" mt={4}>
        {/* 📦 Flex component - flex container
            (Flex component - flex container)
            💡 justify="space-between": Căn items cách đều (space between items)
            (justify="space-between": Space items evenly)
            💡 align="center": Căn giữa theo trục dọc (align center vertically)
            (align="center": Align center vertically)
            💡 mt={4}: margin-top: 16px (4 * 4px) */}
        <Text fontSize="2xl" fontWeight="bold" color="blue.500">
          {/* 📝 Text component - fontSize: 2xl (rất lớn), fontWeight: bold, color: blue.500
              (Text component - fontSize: 2xl - very large, fontWeight: bold, color: blue.500) */}
          ${product.price}
          {/* 💰 Hiển giá sản phẩm (Display product price) */}
        </Text>
        <Button colorScheme="blue">
          {/* 🔘 Button component - colorScheme: blue
              (Button component - colorScheme: blue) */}
          Buy {/* 📝 Nội dung button (Button content) */}
        </Button>
      </Flex>
    </Card>
  );
}
```

---

## 5. Mantine

### **5.1. Overview**

```typescript
/**
 * 🎨 MANTINE = Full-featured React components library
 *
 * ✅ ƯU ĐIỂM:
 * - Full-featured: Nhiều components, hooks, utilities
 * - TypeScript: Excellent TypeScript support
 * - Accessibility: WCAG 2.1 compliant
 * - Dark mode: Built-in dark mode
 * - Form library: Built-in form library (react-hook-form based)
 * - Date picker: Powerful date picker
 * - Bundle size: Medium (~200KB)
 *
 * ❌ NHƯỢC ĐIỂM:
 * - Learning curve: Cần học API
 * - Less popular: Ít popular hơn MUI/Chakra
 * - Documentation: Tốt nhưng ít examples hơn MUI
 *
 * 🎯 USE CASES:
 * - Full-featured applications
 * - Apps cần form library tích hợp
 * - Projects cần date picker mạnh
 */

// 📦 INSTALLATION
// npm install @mantine/core @mantine/hooks

// ✅ SETUP (Thiết Lập)
import { MantineProvider } from '@mantine/core';
// 📦 MantineProvider: Cung cấp theme và context cho toàn bộ app
// (MantineProvider: Provides theme and context to entire app)
import '@mantine/core/styles.css';
// 🎨 Import CSS styles của Mantine (Import Mantine CSS styles)

function App() {
  // 💡 Component gốc của app (Root component of app)
  return (
    <MantineProvider>
      {/* 🎨 MantineProvider: Wrap app để cung cấp theme và context
          (MantineProvider: Wrap app to provide theme and context)
          💡 Tất cả Mantine components có thể dùng theme, dark mode...
          (All Mantine components can use theme, dark mode...) */}
      <YourApp /> {/* 📝 Component app của bạn (Your app component) */}
    </MantineProvider>
  );
}

// ✅ BASIC USAGE (Cách Sử Dụng Cơ Bản)
import { Button, TextInput, Stack, Paper } from '@mantine/core';
// 📦 Import Mantine components (Import Mantine components)

function LoginForm() {
  // 💡 Component form đăng nhập (Login form component)

  return (
    <Paper p="md" shadow="sm">
      {/* 📄 Paper = card container với padding và shadow
          (Paper = card container with padding and shadow)
          💡 p="md": padding = medium (16px) (padding = medium - 16px)
          💡 shadow="sm": shadow = small (Bóng đổ nhỏ) (shadow = small) */}
      <Stack gap="md">
        {/* 📊 Stack = flex container với gap
            (Stack = flex container with gap)
            💡 gap="md": gap = medium (16px) giữa các items
            (gap="md": gap = medium - 16px between items) */}

        <TextInput
          label="Email"
          // 🏷️ Label hiển thị cho input (Label displayed for input)
          placeholder="Enter email"
          // 📝 Placeholder: Hiển khi input trống (Placeholder: Displays when input is empty)
          required
          // ✅ Required field - Bắt buộc phải có giá trị (Required - must have value)
          // 💡 Tự động hiển dấu * và validation (Automatically shows * and validation)
        />

        <TextInput
          label="Password"
          // 🏷️ Label: Password (Label: Password)
          type="password"
          // 🔒 Type: password - Ẩn ký tự khi gõ (Type: password - Hides characters)
          placeholder="Enter password"
          // 📝 Placeholder: Hiển khi input trống (Placeholder: Displays when input is empty)
          required
          // ✅ Required field (Bắt buộc) (Required field)
        />

        <Button fullWidth>
          {/* 🔘 Button component - fullWidth: Chiếm 100% width
              (Button component - fullWidth: Takes 100% width) */}
          Login {/* 📝 Nội dung button (Button content) */}
        </Button>
      </Stack>
    </Paper>
  );
}
```

### **5.2. Form Library**

```typescript
/**
 * 📋 MANTINE FORM LIBRARY - Built-in form library dựa trên react-hook-form
 */

import { useForm } from '@mantine/form';
import { TextInput, Button, Stack, Alert } from '@mantine/core';

interface FormValues {
  email: string;
  password: string;
}

function LoginForm() {
  // 💡 Component form đăng nhập với Mantine form library
  // (Login form component with Mantine form library)

  const form = useForm<FormValues>({
    // 💡 useForm: Hook quản lý form state và validation (Hook manages form state and validation)
    // 💡 <FormValues>: Type-safe với FormValues interface (Type-safe with FormValues interface)
    initialValues: {
      // 💡 initialValues: Giá trị ban đầu của form fields (Initial values of form fields)
      email: '', // 📧 Email: rỗng (Email: empty)
      password: '', // 🔒 Password: rỗng (Password: empty)
    },
    validate: {
      // 💡 validate: Validation functions cho từng field (Validation functions for each field)
      email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Email không hợp lệ'),
      // 📧 Email validation: Kiểm tra format email
      // (Email validation: Check email format)
      // 💡 Regex: /^\S+@\S+$/ - Kiểm tra format email cơ bản
      // (Regex: /^\S+@\S+$/ - Check basic email format)
      // 💡 Return null nếu hợp lệ, return string nếu không hợp lệ
      // (Return null if valid, return string if invalid)
      password: (value) =>
        value.length < 8 ? 'Password phải có ít nhất 8 ký tự' : null,
      // 🔒 Password validation: Kiểm tra độ dài tối thiểu
      // (Password validation: Check minimum length)
      // 💡 Nếu length < 8 → return error message, ngược lại → null
      // (If length < 8 → return error message, otherwise → null)
    },
  });

  const handleSubmit = (values: FormValues) => {
    // 💡 Hàm xử lý khi form submit thành công (Function handles successful form submission)
    // 💡 values đã được validate, đảm bảo đúng format (values have been validated, ensures correct format)
    console.log('Form values:', values); // 📊 In ra console (Log to console)
  };

  return (
    <form onSubmit={form.onSubmit(handleSubmit)}>
      {/* 📝 HTML form element
          💡 form.onSubmit(handleSubmit): Tự động validate trước khi gọi handleSubmit
          (form.onSubmit(handleSubmit): Automatically validates before calling handleSubmit) */}
      <Stack gap="md">
        {/* 📊 Stack với gap medium (Stack with medium gap) */}

        <TextInput
          label="Email"
          // 🏷️ Label: Email (Label: Email)
          placeholder="Enter email"
          // 📝 Placeholder (Placeholder)
          {...form.getInputProps('email')}
          // 🎮 Auto bind value, onChange, error - Tự động bind với form state
          // (Auto bind value, onChange, error - Automatically binds with form state)
          // 💡 getInputProps('email') trả về: { value, onChange, onBlur, error }
          // (getInputProps('email') returns: { value, onChange, onBlur, error })
          // 💡 Tương đương với:
          // (Equivalent to:)
          // value={form.values.email}
          // onChange={(e) => form.setFieldValue('email', e.target.value)}
          // error={form.errors.email}
        />

        <TextInput
          label="Password"
          // 🏷️ Label: Password (Label: Password)
          type="password"
          // 🔒 Type: password (Type: password)
          placeholder="Enter password"
          // 📝 Placeholder (Placeholder)
          {...form.getInputProps('password')}
          // 🎮 Auto bind với form state (Auto bind with form state)
        />

        {form.errors.root && (
          // ❌ Global errors - Lỗi toàn cục (không thuộc field cụ thể)
          // (Global errors - Global errors not belonging to specific field)
          <Alert color="red">
            {/* 🚨 Alert component - color: red (Alert component - color: red) */}
            {form.errors.root}
            {/* 📝 Hiển message lỗi toàn cục (Display global error message) */}
          </Alert>
        )}

        <Button type="submit">
          {/* 🔘 Button - type: submit (Button - type: submit) */}
          Login {/* 📝 Nội dung button (Button content) */}
        </Button>
      </Stack>
    </form>
  );
}
```

---

## 6. Radix UI

### **6.1. Overview**

```typescript
/**
 * 🎨 RADIX UI = Headless, accessible component primitives
 *
 * ✅ ƯU ĐIỂM:
 * - Headless: Không có styles, bạn tự style
 * - Accessible: WCAG 2.1 compliant, keyboard navigation
 * - Composable: Mix and match components
 * - Small bundle: Chỉ import components cần (~50KB per component)
 * - Unstyled: Full control over styling
 * - TypeScript: Excellent TypeScript support
 *
 * ❌ NHƯỢC ĐIỂM:
 * - No styles: Phải tự style (có thể tốn thời gian)
 * - Learning curve: Cần hiểu accessibility concepts
 * - Composition: Cần hiểu cách compose components
 *
 * 🎯 USE CASES:
 * - Custom design systems
 * - Apps cần full control styling
 * - Projects dùng Tailwind CSS
 * - Accessibility-critical apps
 */

// 📦 INSTALLATION
// npm install @radix-ui/react-dialog @radix-ui/react-dropdown-menu

// ✅ BASIC USAGE - Dialog (Cách Sử Dụng Cơ Bản - Dialog)
import * as Dialog from '@radix-ui/react-dialog';
// 📦 Import Dialog components - * as Dialog để dùng Dialog.Root, Dialog.Trigger...
// (Import Dialog components - * as Dialog to use Dialog.Root, Dialog.Trigger...)

function MyDialog() {
  // 💡 Component Dialog tùy chỉnh (Custom Dialog component)

  return (
    <Dialog.Root>
      {/* 🎮 Root component - Quản lý state (open/close) của Dialog
          (Root component - Manages Dialog state - open/close)
          💡 Không có styles, chỉ quản lý logic (No styles, only manages logic) */}
      <Dialog.Trigger asChild>
        {/* 🖱️ Trigger button - Button để mở Dialog
            (Trigger button - Button to open Dialog)
            💡 asChild: Render children thay vì tạo button mới (Render children instead of creating new button)
            💡 Cho phép dùng button tùy chỉnh (Allows using custom button) */}
        <button>Open Dialog</button>
        {/* 🔘 Button tùy chỉnh - Bạn tự style (Custom button - You style it) */}
      </Dialog.Trigger>
      <Dialog.Portal>
        {/* 🌐 Portal - Render Dialog outside DOM tree (thường là body)
            (Portal - Render Dialog outside DOM tree - usually body)
            💡 Tránh z-index issues, overflow issues (Avoids z-index issues, overflow issues) */}
        <Dialog.Overlay className="dialog-overlay" />
        {/* 🎨 Overlay backdrop - Lớp phủ phía sau Dialog
            (Overlay backdrop - Layer behind Dialog)
            💡 className: Bạn tự style với CSS/Tailwind (You style with CSS/Tailwind)
            💡 Thường dùng: position: fixed, inset: 0, background: rgba(0,0,0,0.5)
            (Usually: position: fixed, inset: 0, background: rgba(0,0,0,0.5)) */}
        <Dialog.Content className="dialog-content">
          {/* 📄 Dialog content - Nội dung Dialog
              (Dialog content - Dialog content)
              💡 className: Bạn tự style (You style it)
              💡 Thường dùng: position: fixed, center, background: white, padding...
              (Usually: position: fixed, center, background: white, padding...) */}
          <Dialog.Title>Dialog Title</Dialog.Title>
          {/* 📝 Title - Tiêu đề Dialog (Title - Dialog title)
              💡 Tự động có ARIA attributes cho accessibility (Automatically has ARIA attributes for accessibility) */}
          <Dialog.Description>Dialog description text</Dialog.Description>
          {/* 📝 Description - Mô tả Dialog (Description - Dialog description)
              💡 Tự động có ARIA attributes (Automatically has ARIA attributes) */}
          <Dialog.Close asChild>
            {/* ❌ Close button - Button để đóng Dialog
                (Close button - Button to close Dialog)
                💡 asChild: Render children thay vì tạo button mới (Render children instead of creating new button) */}
            <button>Close</button>
            {/* 🔘 Button tùy chỉnh (Custom button) */}
          </Dialog.Close>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}

// 💡 STYLING VỚI CSS/Tailwind
// .dialog-overlay {
//   position: fixed;
//   inset: 0;
//   background: rgba(0, 0, 0, 0.5);
// }
//
// .dialog-content {
//   position: fixed;
//   top: 50%;
//   left: 50%;
//   transform: translate(-50%, -50%);
//   background: white;
//   padding: 24px;
//   border-radius: 8px;
// }
```

### **6.2. Composable Pattern**

```typescript
/**
 * 🧩 RADIX UI COMPOSABLE PATTERN - Mix and match components
 */

import * as DropdownMenu from '@radix-ui/react-dropdown-menu';
// 📦 Import DropdownMenu components (Import DropdownMenu components)

function UserMenu() {
  // 💡 Component menu người dùng (User menu component)

  return (
    <DropdownMenu.Root>
      {/* 🎮 Root component - Quản lý state (open/close) của DropdownMenu
          (Root component - Manages DropdownMenu state - open/close) */}
      <DropdownMenu.Trigger asChild>
        {/* 🖱️ Trigger button - Button để mở menu
            (Trigger button - Button to open menu)
            💡 asChild: Render children thay vì tạo button mới (Render children instead of creating new button) */}
        <button>User Menu</button>
        {/* 🔘 Button tùy chỉnh (Custom button) */}
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        {/* 🌐 Portal - Render menu outside DOM tree (Portal - Render menu outside DOM tree) */}
        <DropdownMenu.Content>
          {/* 📄 Menu content - Container cho menu items
              (Menu content - Container for menu items)
              💡 Bạn tự style với CSS/Tailwind (You style with CSS/Tailwind) */}
          <DropdownMenu.Item>Profile</DropdownMenu.Item>
          {/* 📋 Menu item: Profile (Menu item: Profile)
              💡 Tự động có keyboard navigation, focus management
              (Automatically has keyboard navigation, focus management) */}
          <DropdownMenu.Item>Settings</DropdownMenu.Item>
          {/* 📋 Menu item: Settings (Menu item: Settings) */}
          <DropdownMenu.Separator />
          {/* ➖ Separator - Đường phân cách giữa các items
              (Separator - Divider between items) */}
          <DropdownMenu.Item>Logout</DropdownMenu.Item>
          {/* 📋 Menu item: Logout (Menu item: Logout) */}
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
}

// ✅ ACCESSIBILITY FEATURES (tự động có) (Accessibility Features - automatically included)
// - Keyboard navigation (Arrow keys, Enter, Escape)
//   (Điều hướng bàn phím - Phím mũi tên, Enter, Escape)
//   (Keyboard navigation - Arrow keys, Enter, Escape)
// - Focus management (Quản lý focus tự động)
//   (Focus management - Automatic focus management)
// - ARIA attributes (Thuộc tính ARIA tự động)
//   (ARIA attributes - Automatic ARIA attributes)
// - Screen reader support (Hỗ trợ screen reader)
//   (Screen reader support)
```

---

## 7. Headless UI

### **7.1. Overview**

```typescript
/**
 * 🎨 HEADLESS UI = Unstyled, accessible components (by Tailwind team)
 *
 * ✅ ƯU ĐIỂM:
 * - Tailwind CSS: Designed for Tailwind CSS
 * - Accessible: WCAG 2.1 compliant
 * - Simple API: Dễ dùng
 * - Small bundle: Chỉ import cần (~30KB per component)
 *
 * ❌ NHƯỢC ĐIỂM:
 * - Limited components: Ít components hơn Radix UI
 * - Tailwind focus: Tối ưu cho Tailwind (có thể khó dùng với CSS khác)
 *
 * 🎯 USE CASES:
 * - Projects dùng Tailwind CSS
 * - Custom design systems với Tailwind
 */

// 📦 INSTALLATION
// npm install @headlessui/react

// ✅ BASIC USAGE - Dialog (Cách Sử Dụng Cơ Bản - Dialog)
import { Dialog } from '@headlessui/react';
// 📦 Import Dialog component từ Headless UI (Import Dialog component from Headless UI)

function MyDialog({
  isOpen, // 💡 isOpen: Boolean - Dialog đang mở hay đóng (Boolean - Dialog is open or closed)
  onClose, // 💡 onClose: Function - Hàm đóng Dialog (Function - Close Dialog function)
}: {
  isOpen: boolean; // 📝 Type: boolean (Type: boolean)
  onClose: () => void; // 📝 Type: function không return (Type: function that returns void)
}) {
  // 💡 Component Dialog tùy chỉnh (Custom Dialog component)

  return (
    <Dialog open={isOpen} onClose={onClose}>
      {/* 🎮 Dialog component - Quản lý state và accessibility
          (Dialog component - Manages state and accessibility)
          💡 open: Control Dialog mở/đóng (Control Dialog open/close)
          💡 onClose: Callback khi đóng Dialog (Callback when closing Dialog) */}
      <Dialog.Backdrop />
      {/* 🎨 Backdrop overlay - Lớp phủ phía sau Dialog
          (Backdrop overlay - Layer behind Dialog)
          💡 Bạn tự style với Tailwind: className="fixed inset-0 bg-black/50"
          (You style with Tailwind: className="fixed inset-0 bg-black/50") */}
      <Dialog.Panel>
        {/* 📄 Dialog panel - Nội dung Dialog
            (Dialog panel - Dialog content)
            💡 Bạn tự style với Tailwind: className="bg-white p-6 rounded-lg"
            (You style with Tailwind: className="bg-white p-6 rounded-lg") */}
        <Dialog.Title>Dialog Title</Dialog.Title>
        {/* 📝 Title - Tiêu đề Dialog (Title - Dialog title)
            💡 Tự động có ARIA attributes (Automatically has ARIA attributes) */}
        <Dialog.Description>Dialog description</Dialog.Description>
        {/* 📝 Description - Mô tả Dialog (Description - Dialog description)
            💡 Tự động có ARIA attributes (Automatically has ARIA attributes) */}
        <button onClick={onClose}>Close</button>
        {/* 🔘 Button đóng Dialog (Button to close Dialog) */}
      </Dialog.Panel>
    </Dialog>
  );
}

// ✅ DROPDOWN MENU (Menu Thả Xuống)
import { Menu } from '@headlessui/react';
// 📦 Import Menu component (Import Menu component)

function UserMenu() {
  // 💡 Component menu người dùng (User menu component)

  return (
    <Menu>
      {/* 🎮 Menu component - Quản lý state và accessibility
          (Menu component - Manages state and accessibility) */}
      <Menu.Button>Options</Menu.Button>
      {/* 🖱️ Menu button - Button để mở menu
          (Menu button - Button to open menu)
          💡 Tự động có ARIA attributes (Automatically has ARIA attributes) */}
      <Menu.Items>
        {/* 📋 Menu items container - Container cho menu items
            (Menu items container - Container for menu items)
            💡 Bạn tự style với Tailwind: className="bg-white shadow-lg rounded"
            (You style with Tailwind: className="bg-white shadow-lg rounded") */}
        <Menu.Item>
          {/* 📋 Menu item - Item trong menu (Menu item - Item in menu) */}
          {({ active }) => (
            // 💡 Render prop - Nhận { active } object
            // (Render prop - Receives { active } object)
            // 💡 active: Boolean - Item đang được hover/focus (Boolean - Item is hovered/focused)
            <a className={active ? 'bg-blue-500' : ''}>
              {/* 🔗 Link - active ? 'bg-blue-500' : '' (màu nền khi active)
                  (Link - active ? 'bg-blue-500' : '' - background color when active) */}
              Profile {/* 📝 Nội dung item (Item content) */}
            </a>
          )}
        </Menu.Item>
        <Menu.Item>
          {/* 📋 Menu item: Settings (Menu item: Settings) */}
          <a>Settings</a>
          {/* 🔗 Link: Settings (Link: Settings) */}
        </Menu.Item>
      </Menu.Items>
    </Menu>
  );
}
```

---

## 8. Shadcn/ui

### **8.1. Overview**

```typescript
/**
 * 🎨 SHADCN/UI = Copy-paste components (not a library!)
 *
 * ✅ ƯU ĐIỂM:
 * - Copy code: Bạn sở hữu code, tự maintain
 * - Tailwind CSS: Built với Tailwind CSS
 * - Customizable: Dễ customize (vì bạn có code)
 * - Zero bundle: Không tăng bundle size (chỉ code bạn copy)
 * - Radix UI: Built trên Radix UI (accessible)
 * - Modern: Design hiện đại, đẹp
 *
 * ❌ NHƯỢC ĐIỂM:
 * - Manual updates: Phải tự update khi có version mới
 * - Setup: Cần setup Tailwind CSS + Radix UI
 * - Learning curve: Cần hiểu Tailwind + Radix
 *
 * 🎯 USE CASES:
 * - Projects dùng Tailwind CSS
 * - Apps cần custom design
 * - Teams muốn own the code
 */

// 📦 SETUP (one-time) (Thiết Lập - một lần)
// npx shadcn-ui@latest init
// 💡 Lệnh này tạo cấu trúc thư mục và config Tailwind
// (This command creates directory structure and Tailwind config)

// ✅ USAGE - Copy component code vào project (Cách Sử Dụng - Copy component code vào project)
// Components được copy vào src/components/ui/
// (Components are copied to src/components/ui/)
// 💡 Chạy: npx shadcn-ui@latest add button (Run: npx shadcn-ui@latest add button)
// 💡 Component code được copy vào src/components/ui/button.tsx
// (Component code is copied to src/components/ui/button.tsx)

import { Button } from '@/components/ui/button';
// 📦 Import Button từ thư mục components/ui (Import Button from components/ui folder)
// 💡 @/ = alias cho src/ (thường config trong tsconfig.json)
// (@/ = alias for src/ - usually configured in tsconfig.json)
import { Input } from '@/components/ui/input';
// 📦 Import Input từ thư mục components/ui (Import Input from components/ui folder)

function LoginForm() {
  // 💡 Component form đăng nhập (Login form component)

  return (
    <div>
      <Input
        type="email"
        // 📧 Type: email (Type: email)
        placeholder="Email"
        // 📝 Placeholder: Email (Placeholder: Email)
      />
      <Input
        type="password"
        // 🔒 Type: password (Type: password)
        placeholder="Password"
        // 📝 Placeholder: Password (Placeholder: Password)
      />
      <Button>Login</Button>
      {/* 🔘 Button component - Bạn có thể customize code trong button.tsx
          (Button component - You can customize code in button.tsx) */}
    </div>
  );
}

// 💡 COMPONENT STRUCTURE (sau khi copy) (Component Structure - after copying)
// src/components/ui/button.tsx
// 💡 File này chứa code Button component (This file contains Button component code)
// - Code component với Tailwind classes (Component code with Tailwind classes)
//   💡 Ví dụ: className="bg-blue-500 hover:bg-blue-600"
//   (Example: className="bg-blue-500 hover:bg-blue-600")
// - Bạn có thể sửa trực tiếp (You can edit directly)
//   💡 Sửa code trong file này → thay đổi ngay lập tức
//   (Edit code in this file → changes immediately)
// - Không phụ thuộc vào npm package (Not dependent on npm package)
//   💡 Không cần update package, chỉ cần sửa code
//   (No need to update package, just edit code)
```

---

## 📊 9. Comparison Matrix (Ma Trận So Sánh)

### **📋 9.1. Detailed Comparison (So Sánh Chi Tiết)**

**📊 Bảng So Sánh Component Libraries (Component Libraries Comparison Table):**

| Library (Thư viện)       | Bundle Size (Kích thước)    | Components (Số lượng)           | Customization (Tùy chỉnh)             | Accessibility (Khả năng truy cập)       | TypeScript      | Learning Curve (Độ khó học)     | Design System (Hệ thống thiết kế) | Best For (Tốt nhất cho)                  |
| ------------------------ | --------------------------- | ------------------------------- | ------------------------------------- | --------------------------------------- | --------------- | ------------------------------- | --------------------------------- | ---------------------------------------- |
| **🏗️ Material-UI (MUI)** | ⚠️ ~300KB (Lớn)             | ✅ 100+ (Nhiều)                 | ✅ Theme-based (Dựa trên theme)       | ✅ WCAG 2.1 (Xuất sắc)                  | ✅ Full support | 📚 Medium (Trung bình)          | 🎨 Material Design                | Enterprise apps, Admin dashboards        |
| **📊 Ant Design**        | ⚠️ ~500KB (Rất lớn)         | ✅ 60+ (Nhiều)                  | ✅ Theme-based (Dựa trên theme)       | ✅ Good (Tốt)                           | ✅ Full support | 📚 Medium (Trung bình)          | 🎨 Ant Design                     | Admin dashboards, Data-heavy apps        |
| **🎨 Chakra UI**         | ✅ ~150KB (Trung bình)      | ✅ 50+ (Tốt)                    | ✅ Props-based (Dựa trên props)       | ✅ WCAG 2.1 (Xuất sắc)                  | ✅ Full support | 📚 Low (Dễ)                     | 🎨 Custom (Tùy chỉnh)             | Modern apps, MVPs                        |
| **⚡ Mantine**           | ✅ ~200KB (Trung bình)      | ✅ 100+ (Nhiều)                 | ✅ Props-based (Dựa trên props)       | ✅ WCAG 2.1 (Xuất sắc)                  | ✅ Excellent    | 📚 Medium (Trung bình)          | 🎨 Custom (Tùy chỉnh)             | Full-featured apps, Form-heavy apps      |
| **🧩 Radix UI**          | ✅ ~50KB/component (Nhỏ)    | ✅ 20+ primitives (Nguyên thủy) | ✅ Full control (Kiểm soát hoàn toàn) | ✅ WCAG 2.1 (Xuất sắc)                  | ✅ Excellent    | 📚 Medium-High (Trung bình-Cao) | 🎨 Headless (Không style)         | Custom design systems, Tailwind projects |
| **📋 Shadcn/ui**         | ✅ Zero (Không - copy code) | ✅ 30+ (Đang phát triển)        | ✅ Full control (Kiểm soát hoàn toàn) | ✅ WCAG 2.1 (Xuất sắc - dựa trên Radix) | ✅ Excellent    | 📚 Medium (Trung bình)          | 🎨 Tailwind CSS                   | Tailwind projects, Custom designs        |

### **📦 9.2. Bundle Size Comparison (So Sánh Kích Thước Bundle)**

**📊 Bundle Size Comparison (gzipped) (So Sánh Kích Thước Bundle - đã nén):**

**❌ VERY LARGE (>400KB) (Rất Lớn):**

- 📊 Ant Design: ~500KB
- 🏗️ Material-UI: ~300KB

**⚠️ MEDIUM (100-300KB) (Trung Bình):**

- ⚡ Mantine: ~200KB
- 🎨 Chakra UI: ~150KB

**✅ SMALL (<100KB) (Nhỏ):**

- 🧩 Radix UI: ~50KB per component (chỉ import cần - only import needed)
- 🎯 Headless UI: ~30KB per component
- 📋 Shadcn/ui: 0KB (copy code, không phải library - copy code, not a library)

**💡 TREE-SHAKING TIPS (Mẹo Tree-Shaking):**

- ✅ Import specific components: `import { Button } from '@mui/material'` (Import components cụ thể)
- ❌ Không import entire library: `import * from '@mui/material'` (Don't import entire library)
- ✅ Use path imports: `import Button from '@mui/material/Button'` (Sử dụng path imports)

```typescript
// ❌ BAD: Import entire library (TỒI - Import toàn bộ thư viện)
import * as MUI from '@mui/material';
// 💥 Import TẤT CẢ components → bundle size lớn
// (Import ALL components → large bundle size)

// ✅ GOOD: Import specific components (TỐT - Import components cụ thể)
import { Button, TextField } from '@mui/material';
// 🚀 Chỉ import components cần → tree-shaking hoạt động
// (Only import needed → tree-shaking works)

// ✅ BETTER: Path imports (smaller bundle) (TỐT HƠN - Path imports - bundle nhỏ hơn)
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
// 🚀 Path imports → bundle size nhỏ hơn
// (Path imports → smaller bundle size)
```

---

## 10. Choosing the Right Library

### **10.1. Decision Tree**

```typescript
/**
 * 🎯 DECISION TREE - Chọn library phù hợp
 *
 * ┌─────────────────────────────────────────┐
 * │         BẮT ĐẦU CHỌN LIBRARY            │
 * └─────────────────────────────────────────┘
 *                    │
 *                    ▼
 *         ┌──────────────────────┐
 *         │  Cần Material Design?│
 *         └──────────────────────┘
 *              │           │
 *         YES │           │ NO
 *              ▼           ▼
 *         ┌────────┐  ┌──────────────────┐
 *         │  MUI   │  │ Dùng Tailwind CSS?│
 *         └────────┘  └──────────────────┘
 *                          │        │
 *                      YES │        │ NO
 *                          ▼        ▼
 *                   ┌──────────┐  ┌──────────────────┐
 *                   │ Shadcn/ui│  │ Cần full control?│
 *                   └──────────┘  └──────────────────┘
 *                                      │        │
 *                                  YES │        │ NO
 *                                      ▼        ▼
 *                               ┌──────────┐  ┌──────────────────┐
 *                               │ Radix UI │  │ Enterprise app?  │
 *                               └──────────┘  └──────────────────┘
 *                                                  │        │
 *                                              YES │        │ NO
 *                                                  ▼        ▼
 *                                           ┌──────────┐  ┌──────────┐
 *                                           │ Ant Design│ │ Chakra UI│
 *                                           └──────────┘  └──────────┘
 */

// ✅ DECISION CRITERIA

const SELECTION_CRITERIA = {
  // 🎨 DESIGN SYSTEM
  materialDesign: 'MUI',
  antDesign: 'Ant Design',
  customDesign: 'Chakra UI, Mantine, Radix UI, Shadcn/ui',

  // 📦 BUNDLE SIZE
  smallBundle: 'Radix UI, Headless UI, Shadcn/ui',
  mediumBundle: 'Chakra UI, Mantine',
  largeBundle: 'MUI, Ant Design',

  // 🎯 USE CASE
  enterprise: 'MUI, Ant Design',
  adminDashboard: 'Ant Design, MUI',
  mvp: 'Chakra UI, Shadcn/ui',
  customDesign: 'Radix UI, Shadcn/ui',

  // ♿ ACCESSIBILITY
  criticalA11y: 'Radix UI, MUI, Chakra UI, Mantine',

  // 🎨 CUSTOMIZATION
  fullControl: 'Radix UI, Shadcn/ui',
  themeBased: 'MUI, Ant Design, Chakra UI, Mantine',
};
```

### **10.2. Real-World Examples**

```typescript
/**
 * 💼 REAL-WORLD USE CASES
 */

// ✅ CASE 1: Enterprise Admin Dashboard
// Requirements: Data tables, forms, charts, Material Design
// Choice: Material-UI (MUI)
// Reason: Enterprise-ready, rich components, Material Design

// ✅ CASE 2: Startup MVP
// Requirements: Fast development, modern design, small bundle
// Choice: Chakra UI hoặc Shadcn/ui
// Reason: Simple API, quick setup, customizable

// ✅ CASE 3: Custom Design System
// Requirements: Full control, Tailwind CSS, accessible
// Choice: Shadcn/ui + Radix UI
// Reason: Own the code, full control, accessible

// ✅ CASE 4: Government/Healthcare App
// Requirements: WCAG 2.1 AA, keyboard navigation, screen readers
// Choice: Radix UI hoặc MUI
// Reason: Excellent accessibility, tested

// ✅ CASE 5: E-commerce Platform
// Requirements: Forms, date pickers, tables, modern design
// Choice: Mantine hoặc Chakra UI
// Reason: Good form library, modern components
```

---

## 11. Best Practices

### **11.1. Tree-Shaking & Bundle Optimization**

```typescript
/**
 * 📦 TREE-SHAKING BEST PRACTICES
 *
 * 💡 Tree-shaking = Loại bỏ code không dùng trong bundle
 * 💡 Chỉ hoạt động với ES modules (import/export)
 */

// ❌ BAD: Import entire library
import * as MUI from '@mui/material';
// 💥 Import TẤT CẢ → bundle size lớn (~300KB)

// ✅ GOOD: Import specific components
import { Button, TextField, Box } from '@mui/material';
// 🚀 Chỉ import cần → bundle size nhỏ hơn (~50KB)

// ✅ BETTER: Path imports (smallest bundle)
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Box from '@mui/material/Box';
// 🚀 Path imports → bundle size nhỏ nhất (~30KB)

// ✅ BEST: Use babel plugin (MUI)
// babel.config.js
module.exports = {
  plugins: [
    [
      'babel-plugin-import',
      {
        libraryName: '@mui/material',
        libraryDirectory: '',
        camel2DashComponentName: false,
      },
      'core',
    ],
  ],
};
// 🚀 Tự động convert imports → path imports
```

### **11.2. Theme Customization**

```typescript
/**
 * 🎨 THEME CUSTOMIZATION BEST PRACTICES
 */

// ✅ PATTERN 1: Extend default theme (MUI)
import { createTheme } from '@mui/material/styles';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2', // 🔵 Override primary color
    },
  },
  typography: {
    fontFamily: '"Roboto", "Arial", sans-serif',
  },
});

// ✅ PATTERN 2: Use design tokens (Chakra UI)
const theme = extendTheme({
  colors: {
    brand: {
      50: '#e3f2fd',
      500: '#2196f3',
      900: '#0d47a1',
    },
  },
  components: {
    Button: {
      defaultProps: {
        colorScheme: 'brand', // 🎨 Dùng brand color
      },
    },
  },
});

// ✅ PATTERN 3: CSS Variables (Radix UI + Tailwind)
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        primary: 'var(--color-primary)', // 🎨 CSS variable
      },
    },
  },
};

// ✅ PATTERN 4: Design tokens file
// tokens.ts
export const tokens = {
  colors: {
    primary: '#1976d2',
    secondary: '#dc004e',
  },
  spacing: {
    xs: '4px',
    sm: '8px',
    md: '16px',
    lg: '24px',
  },
};
// 💡 Dùng tokens trong theme config
```

### **11.3. Component Composition**

```typescript
/**
 * 🧩 COMPONENT COMPOSITION BEST PRACTICES
 */

// ✅ PATTERN 1: Compose với wrapper components
function Card({ children }: { children: React.ReactNode }) {
  return (
    <Box p={4} bg="white" borderRadius="lg" boxShadow="md">
      {children}
    </Box>
  );
}

function ProductCard({ product }: { product: Product }) {
  return (
    <Card>
      <Text fontSize="xl">{product.name}</Text>
      <Text>{product.description}</Text>
    </Card>
  );
}

// ✅ PATTERN 2: Compound components (Radix UI pattern)
function Dialog({ children }: { children: React.ReactNode }) {
  return <Dialog.Root>{children}</Dialog.Root>;
}

Dialog.Trigger = Dialog.Trigger;
Dialog.Content = Dialog.Content;
Dialog.Title = Dialog.Title;

// Usage
<Dialog>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Content>
    <Dialog.Title>Title</Dialog.Title>
  </Dialog.Content>
</Dialog>;

// ✅ PATTERN 3: Render props (flexible composition)
function DataTable<T>({
  data,
  columns,
  renderRow,
}: {
  data: T[];
  columns: Column[];
  renderRow: (item: T) => React.ReactNode;
}) {
  return (
    <Table>
      {data.map((item) => (
        <TableRow key={item.id}>{renderRow(item)}</TableRow>
      ))}
    </Table>
  );
}
```

### **11.4. Performance Optimization**

```typescript
/**
 * ⚡ PERFORMANCE OPTIMIZATION BEST PRACTICES
 */

// ✅ PATTERN 1: Lazy load components
import { lazy, Suspense } from 'react';

const HeavyDataTable = lazy(() => import('./HeavyDataTable'));

function App() {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <HeavyDataTable />
    </Suspense>
  );
}

// ✅ PATTERN 2: Memoize expensive components
import { memo } from 'react';
import { Table } from '@mui/material';

const ExpensiveTable = memo(({ data }: { data: Data[] }) => {
  // Expensive rendering logic
  return <Table>{/* ... */}</Table>;
});

// ✅ PATTERN 3: Virtual scrolling cho large lists
import { FixedSizeList } from 'react-window';

function LargeList({ items }: { items: Item[] }) {
  return (
    <FixedSizeList height={600} itemCount={items.length} itemSize={50}>
      {({ index, style }) => <div style={style}>{items[index].name}</div>}
    </FixedSizeList>
  );
}

// ✅ PATTERN 4: Code splitting per route
import { lazy } from 'react';
import { Routes, Route } from 'react-router-dom';

const Dashboard = lazy(() => import('./Dashboard'));
const Settings = lazy(() => import('./Settings'));

function App() {
  return (
    <Routes>
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/settings" element={<Settings />} />
    </Routes>
  );
}
```

---

**🎯 Remember:** "Choose component library based on your needs: design system, bundle size, customization, and accessibility requirements. Don't over-engineer - sometimes a simple library is better than a complex one!"
