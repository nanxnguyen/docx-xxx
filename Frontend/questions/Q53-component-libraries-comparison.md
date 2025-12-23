# 🎨 Q53: Component Libraries Comparison

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Component Libraries = pre-built UI components để tăng tốc development. MUI = Material Design, enterprise-ready. Ant Design = enterprise admin dashboards. Chakra UI = simple, customizable. Radix UI = headless, accessible. Shadcn/ui = copy-paste components. Chọn library dựa trên: design system, bundle size, customization needs, accessibility requirements."**

**🔑 Top Component Libraries:**

| **Library**    | **Bundle Size**     | **Design System** | **Customization** | **Accessibility** | **Best For**       |
| -------------- | ------------------- | ----------------- | ----------------- | ----------------- | ------------------ |
| **MUI**        | ⚠️ Large (~300KB)   | Material Design   | ✅ Theme-based    | ✅ WCAG 2.1       | Enterprise apps    |
| **Ant Design** | ⚠️ Large (~500KB)   | Ant Design        | ✅ Theme-based    | ✅ Good           | Admin dashboards   |
| **Chakra UI**  | ✅ Medium (~150KB)  | Custom            | ✅ Props-based    | ✅ Excellent      | Modern apps        |
| **Mantine**    | ✅ Medium (~200KB)  | Custom            | ✅ Props-based    | ✅ Excellent      | Full-featured apps |
| **Radix UI**   | ✅ Small (~50KB)    | Headless          | ✅ Full control   | ✅ Excellent      | Custom designs     |
| **Shadcn/ui**  | ✅ Zero (copy code) | Tailwind          | ✅ Full control   | ✅ Excellent      | Tailwind projects  |

**🔑 Key Features:**

**1. Material-UI (MUI):**

- **Material Design 3** - Google's design system
- **Theming** - Powerful theme customization
- **Enterprise-ready** - Production-tested
- **Large ecosystem** - Many components
- **Bundle size** - Large (~300KB gzipped)

**2. Ant Design:**

- **Enterprise focus** - Admin dashboards, data tables
- **Rich components** - Forms, tables, charts
- **Chinese origin** - Popular in Asia
- **Bundle size** - Very large (~500KB)

**3. Chakra UI:**

- **Simple API** - Easy to learn
- **Props-based styling** - No CSS needed
- **Accessibility** - Built-in a11y
- **Bundle size** - Medium (~150KB)

**4. Radix UI:**

- **Headless** - No styles, full control
- **Accessible** - WCAG 2.1 compliant
- **Composable** - Mix and match
- **Bundle size** - Small (~50KB per component)

**5. Shadcn/ui:**

- **Copy-paste** - Own the code
- **Tailwind CSS** - Utility-first
- **Customizable** - Full control
- **Bundle size** - Zero (you copy code)

**⚠️ Lỗi Thường Gặp:**

- Chọn library quá lớn cho simple app → bundle bloat
- Không customize theme → app giống demo
- Ignore accessibility → không pass WCAG
- Mix nhiều libraries → inconsistent design
- Không tree-shake → import toàn bộ library

**💡 Kiến Thức Senior:**

- **Tree-shaking**: Import specific components (not entire library)
- **Theme customization**: Override design tokens, not CSS
- **Accessibility**: Use semantic HTML, ARIA attributes
- **Bundle optimization**: Code splitting, lazy loading
- **Design system**: Consistent spacing, colors, typography

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

// ❌ TỰ CODE TỪ ĐẦU (không dùng library)
const CustomButton = ({ children, onClick }) => {
  return (
    <button
      onClick={onClick}
      style={{
        padding: '8px 16px',
        backgroundColor: '#1976d2',
        color: 'white',
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        // ... 50+ dòng CSS nữa
        // ❌ Thiếu: focus states, disabled states, loading states, accessibility...
      }}
    >
      {children}
    </button>
  );
};
// 💥 Vấn đề:
// - Tốn thời gian code
// - Không consistent với design system
// - Thiếu accessibility (keyboard navigation, screen reader support)
// - Không responsive
// - Phải maintain code

// ✅ DÙNG COMPONENT LIBRARY (MUI)
import { Button } from '@mui/material';

const MyButton = () => {
  return (
    <Button variant="contained" onClick={handleClick}>
      Click me
    </Button>
  );
};
// 🚀 Ưu điểm:
// - Code ngắn gọn (1 dòng)
// - Đã có: styling, accessibility, responsive, keyboard support
// - Consistent với Material Design
// - Production-ready
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

// ✅ BASIC USAGE
import { Button, TextField, Box, Stack } from '@mui/material';

function LoginForm() {
  return (
    <Box sx={{ p: 3 }}>
      {' '}
      {/* 📦 Box = div với sx prop (styling) */}
      <Stack spacing={2}>
        {' '}
        {/* 📊 Stack = flex container với spacing */}
        <TextField
          label="Email" // 🏷️ Label hiển thị trên input
          type="email"
          variant="outlined" // 🎨 Variant: outlined, filled, standard
          fullWidth // 📏 Chiếm full width
        />
        <TextField
          label="Password"
          type="password"
          variant="outlined"
          fullWidth
        />
        <Button
          variant="contained" // 🎨 Variant: contained, outlined, text
          color="primary" // 🎨 Color: primary, secondary, error, warning, info, success
          size="large" // 📏 Size: small, medium, large
          fullWidth
        >
          Login
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
import { CssBaseline } from '@mui/material';

// 🎨 CREATE CUSTOM THEME
const theme = createTheme({
  // 🎨 COLOR PALETTE - Định nghĩa màu sắc
  palette: {
    primary: {
      main: '#1976d2', // 🔵 Màu chính (blue)
      light: '#42a5f5', // 🔵 Màu nhạt hơn
      dark: '#1565c0', // 🔵 Màu đậm hơn
      contrastText: '#fff', // ⚪ Màu chữ trên nền primary
    },
    secondary: {
      main: '#dc004e', // 🔴 Màu phụ (pink)
    },
    error: {
      main: '#f44336', // ❌ Màu lỗi (red)
    },
    background: {
      default: '#f5f5f5', // ⚪ Màu nền mặc định
      paper: '#ffffff', // 📄 Màu nền của Paper component
    },
  },

  // 📝 TYPOGRAPHY - Định nghĩa font chữ
  typography: {
    fontFamily: '"Roboto", "Helvetica", "Arial", sans-serif', // 🔤 Font family mặc định
    h1: {
      fontSize: '2.5rem', // 📏 Kích thước heading 1
      fontWeight: 500, // 💪 Độ đậm
    },
    h2: {
      fontSize: '2rem',
      fontWeight: 500,
    },
    body1: {
      fontSize: '1rem', // 📏 Kích thước body text
      lineHeight: 1.5, // 📏 Khoảng cách dòng
    },
  },

  // 📏 SPACING - Định nghĩa khoảng cách
  spacing: 8, // 🔢 Base spacing unit (8px)
  // 💡 sx={{ p: 2 }} = padding: 16px (2 * 8)
  // 💡 sx={{ m: 3 }} = margin: 24px (3 * 8)

  // 📱 BREAKPOINTS - Responsive breakpoints
  breakpoints: {
    values: {
      xs: 0, // 📱 Mobile (0px+)
      sm: 600, // 📱 Tablet (600px+)
      md: 900, // 💻 Desktop (900px+)
      lg: 1200, // 💻 Large desktop (1200px+)
      xl: 1536, // 💻 Extra large (1536px+)
    },
  },

  // 🧩 COMPONENTS - Override default props cho components
  components: {
    MuiButton: {
      defaultProps: {
        variant: 'contained', // 🎨 Mặc định dùng contained variant
        size: 'medium', // 📏 Mặc định size medium
      },
      styleOverrides: {
        root: {
          textTransform: 'none', // 🔤 Không uppercase text
          borderRadius: 8, // 📐 Bo góc 8px
        },
      },
    },
    MuiTextField: {
      defaultProps: {
        variant: 'outlined', // 🎨 Mặc định dùng outlined variant
      },
    },
  },
});

// 🎯 WRAP APP VỚI THEME PROVIDER
function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline /> {/* 🎨 Reset CSS và apply base styles */}
      <LoginForm />
    </ThemeProvider>
  );
}

// 💡 USAGE TRONG COMPONENTS
import { useTheme } from '@mui/material/styles';

function ThemedComponent() {
  const theme = useTheme(); // 🎨 Lấy theme object

  return (
    <Box
      sx={{
        // 🎨 Dùng theme values
        color: theme.palette.primary.main, // 🔵 Màu primary
        backgroundColor: theme.palette.background.paper, // 📄 Màu nền paper
        padding: theme.spacing(2), // 📏 Padding 16px (2 * 8)

        // 📱 Responsive với breakpoints
        [theme.breakpoints.down('sm')]: {
          // 📱 Khi màn hình < 600px
          fontSize: '14px',
        },
        [theme.breakpoints.up('md')]: {
          // 💻 Khi màn hình >= 900px
          fontSize: '18px',
        },
      }}
    >
      Responsive Text
    </Box>
  );
}
```

### **2.3. Advanced Patterns**

```typescript
/**
 * 🚀 MUI ADVANCED PATTERNS - Production-ready patterns
 */

// ✅ PATTERN 1: Form với React Hook Form + MUI
import { useForm, Controller } from 'react-hook-form';
import { TextField, Button, Alert } from '@mui/material';

interface FormData {
  email: string;
  password: string;
}

function LoginForm() {
  const {
    control, // 🎮 Controller để control MUI components
    handleSubmit, // 📤 Handle form submission
    formState: { errors }, // ❌ Form errors
  } = useForm<FormData>();

  const onSubmit = (data: FormData) => {
    console.log('Form data:', data); // 📊 Data đã validate
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* 🎮 Controller wrapper cho MUI TextField */}
      <Controller
        name="email" // 🏷️ Field name
        control={control}
        rules={{
          required: 'Email là bắt buộc', // ❌ Validation rule
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
            message: 'Email không hợp lệ',
          },
        }}
        render={(
          { field } // 🎨 Render function
        ) => (
          <TextField
            {...field} // 📤 Spread field props (value, onChange, onBlur...)
            label="Email"
            error={!!errors.email} // ❌ Hiển lỗi nếu có
            helperText={errors.email?.message} // 📝 Hiển message lỗi
            fullWidth
            margin="normal"
          />
        )}
      />

      <Controller
        name="password"
        control={control}
        rules={{
          required: 'Password là bắt buộc',
          minLength: {
            value: 8,
            message: 'Password phải có ít nhất 8 ký tự',
          },
        }}
        render={({ field }) => (
          <TextField
            {...field}
            type="password"
            label="Password"
            error={!!errors.password}
            helperText={errors.password?.message}
            fullWidth
            margin="normal"
          />
        )}
      />

      {errors.root && ( // ❌ Global errors
        <Alert severity="error">{errors.root.message}</Alert>
      )}

      <Button type="submit" variant="contained" fullWidth>
        Login
      </Button>
    </form>
  );
}

// ✅ PATTERN 2: Data Table với MUI Table
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TableSortLabel,
  Paper,
} from '@mui/material';

interface Data {
  id: number;
  name: string;
  email: string;
  role: string;
}

function DataTable({ rows }: { rows: Data[] }) {
  const [orderBy, setOrderBy] = useState<keyof Data>('name'); // 📊 Cột đang sort
  const [order, setOrder] = useState<'asc' | 'desc'>('asc'); // 🔄 Hướng sort

  // 🔄 Handle sort click
  const handleSort = (property: keyof Data) => {
    const isAsc = orderBy === property && order === 'asc';
    setOrder(isAsc ? 'desc' : 'asc');
    setOrderBy(property);
  };

  // 📊 Sort rows
  const sortedRows = [...rows].sort((a, b) => {
    if (order === 'asc') {
      return a[orderBy] > b[orderBy] ? 1 : -1;
    }
    return a[orderBy] < b[orderBy] ? 1 : -1;
  });

  return (
    <TableContainer component={Paper}>
      {' '}
      {/* 📄 Paper = card-like container */}
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>
              <TableSortLabel
                active={orderBy === 'name'} // ✅ Highlight nếu đang sort cột này
                direction={orderBy === 'name' ? order : 'asc'} // 🔄 Hiển mũi tên sort
                onClick={() => handleSort('name')} // 🖱️ Click để sort
              >
                Name
              </TableSortLabel>
            </TableCell>
            <TableCell>Email</TableCell>
            <TableCell>Role</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {sortedRows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.email}</TableCell>
              <TableCell>{row.role}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}

// ✅ PATTERN 3: Responsive Layout với MUI Grid
import { Grid, Container } from '@mui/material';

function ResponsiveLayout() {
  return (
    <Container maxWidth="lg">
      {' '}
      {/* 📦 Container với max width */}
      <Grid container spacing={3}>
        {' '}
        {/* 📊 Grid container với spacing */}
        {/* 📱 Mobile: 12 cols (full width) */}
        {/* 💻 Tablet: 6 cols (50% width) */}
        {/* 🖥️ Desktop: 4 cols (33% width) */}
        <Grid item xs={12} sm={6} md={4}>
          <Paper>Card 1</Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper>Card 2</Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
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

// ✅ BASIC USAGE
import { Button, Input, Form, Table, DatePicker } from 'antd';
import 'antd/dist/reset.css'; // 🎨 Import CSS (hoặc dùng CSS-in-JS)

function AdminDashboard() {
  return (
    <div>
      <Form
        layout="vertical" // 📋 Layout: vertical, horizontal, inline
        onFinish={(values) => {
          console.log('Form values:', values);
        }}
      >
        <Form.Item
          label="Username"
          name="username"
          rules={[{ required: true, message: 'Vui lòng nhập username' }]}
        >
          <Input placeholder="Enter username" />
        </Form.Item>

        <Form.Item
          label="Password"
          name="password"
          rules={[{ required: true, message: 'Vui lòng nhập password' }]}
        >
          <Input.Password placeholder="Enter password" />
        </Form.Item>

        <Form.Item>
          <Button type="primary" htmlType="submit">
            Submit
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
import type { ColumnsType } from 'antd/es/table';

interface User {
  id: number;
  name: string;
  email: string;
  status: 'active' | 'inactive';
  createdAt: string;
}

function UserTable() {
  const columns: ColumnsType<User> = [
    {
      title: 'ID',
      dataIndex: 'id', // 🔑 Key trong data object
      key: 'id',
      sorter: (a, b) => a.id - b.id, // 🔄 Sorting function
      width: 80,
    },
    {
      title: 'Name',
      dataIndex: 'name',
      key: 'name',
      sorter: (a, b) => a.name.localeCompare(b.name),
      filterDropdown: ({ setSelectedKeys, selectedKeys, confirm }) => (
        // 🔍 Custom filter dropdown
        <div style={{ padding: 8 }}>
          <Input
            placeholder="Search name"
            value={selectedKeys[0]}
            onChange={(e) =>
              setSelectedKeys(e.target.value ? [e.target.value] : [])
            }
            onPressEnter={() => confirm()}
          />
        </div>
      ),
      onFilter: (value, record) =>
        record.name.toLowerCase().includes(value.toString().toLowerCase()),
    },
    {
      title: 'Email',
      dataIndex: 'email',
      key: 'email',
    },
    {
      title: 'Status',
      dataIndex: 'status',
      key: 'status',
      render: (
        status: string // 🎨 Custom render function
      ) => (
        <Tag color={status === 'active' ? 'green' : 'red'}>
          {status.toUpperCase()}
        </Tag>
      ),
      filters: [
        { text: 'Active', value: 'active' },
        { text: 'Inactive', value: 'inactive' },
      ],
      onFilter: (value, record) => record.status === value,
    },
    {
      title: 'Actions',
      key: 'actions',
      render: (
        _,
        record // 🎨 Render actions column
      ) => (
        <Space>
          <Button size="small" onClick={() => handleEdit(record.id)}>
            Edit
          </Button>
          <Button size="small" danger onClick={() => handleDelete(record.id)}>
            Delete
          </Button>
        </Space>
      ),
    },
  ];

  const data: User[] = [
    {
      id: 1,
      name: 'John Doe',
      email: 'john@example.com',
      status: 'active',
      createdAt: '2024-01-01',
    },
    {
      id: 2,
      name: 'Jane Smith',
      email: 'jane@example.com',
      status: 'inactive',
      createdAt: '2024-01-02',
    },
  ];

  return (
    <Table
      columns={columns}
      dataSource={data}
      rowKey="id" // 🔑 Unique key cho mỗi row
      pagination={{
        pageSize: 10, // 📄 Số rows mỗi trang
        showSizeChanger: true, // ✅ Cho phép đổi page size
        showTotal: (total) => `Total ${total} items`, // 📊 Hiển tổng số
      }}
      scroll={{ x: 800 }} // 📱 Horizontal scroll khi màn hình nhỏ
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

// ✅ SETUP
import { ChakraProvider, extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  colors: {
    brand: {
      50: '#e3f2fd', // 🎨 Color scale (50-900)
      100: '#bbdefb',
      500: '#2196f3', // 🔵 Main color
      900: '#0d47a1',
    },
  },
});

function App() {
  return (
    <ChakraProvider theme={theme}>
      <YourApp />
    </ChakraProvider>
  );
}

// ✅ BASIC USAGE
import {
  Button,
  Input,
  Box,
  Stack,
  FormControl,
  FormLabel,
} from '@chakra-ui/react';

function LoginForm() {
  return (
    <Box p={4}>
      {' '}
      {/* 📦 Box = div, p = padding (4 * 4px = 16px) */}
      <Stack spacing={4}>
        {' '}
        {/* 📊 Stack = flex container với spacing */}
        <FormControl>
          <FormLabel>Email</FormLabel>
          <Input type="email" placeholder="Enter email" />
        </FormControl>
        <FormControl>
          <FormLabel>Password</FormLabel>
          <Input type="password" placeholder="Enter password" />
        </FormControl>
        <Button
          colorScheme="blue" // 🎨 Color scheme (blue, green, red...)
          size="lg" // 📏 Size: sm, md, lg
          width="full" // 📏 Full width
        >
          Login
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
  return (
    <Box
      // 📏 SPACING - Padding, margin qua props
      p={4} // 📱 Padding 16px (4 * 4px)
      m={2} // 📱 Margin 8px (2 * 4px)
      px={6} // 📱 Padding horizontal 24px
      py={8} // 📱 Padding vertical 32px
      // 🎨 COLORS
      bg="blue.500" // 🔵 Background color (từ theme)
      color="white" // ⚪ Text color
      // 📐 BORDERS
      borderWidth="1px" // 📏 Border width
      borderColor="gray.200" // 🎨 Border color
      borderRadius="md" // 📐 Border radius (md = 8px)
      // 📱 RESPONSIVE - Array values [mobile, tablet, desktop]
      width={['100%', '50%', '33%']} // 📱 Mobile: 100%, Tablet: 50%, Desktop: 33%
      fontSize={['14px', '16px', '18px']} // 📱 Responsive font size
      // 🎨 SHADOWS
      boxShadow="md" // 🌑 Shadow (sm, md, lg, xl)
      // 🖱️ HOVER STATES
      _hover={{
        // 🎯 Pseudo-class hover
        bg: 'blue.600', // 🔵 Đổi màu khi hover
        transform: 'scale(1.05)', // 🔄 Phóng to khi hover
      }}
      // 🎯 FOCUS STATES
      _focus={{
        // 🎯 Pseudo-class focus
        outline: '2px solid',
        outlineColor: 'blue.500',
      }}
    >
      Responsive Box
    </Box>
  );
}

// ✅ COMPONENT COMPOSITION
function Card({ children }: { children: React.ReactNode }) {
  return (
    <Box
      p={6}
      bg="white"
      borderRadius="lg"
      boxShadow="lg"
      _hover={{
        boxShadow: 'xl',
        transform: 'translateY(-4px)',
        transition: 'all 0.2s',
      }}
    >
      {children}
    </Box>
  );
}

function ProductCard({ product }: { product: Product }) {
  return (
    <Card>
      <Text fontSize="xl" fontWeight="bold">
        {product.name}
      </Text>
      <Text color="gray.600" mt={2}>
        {product.description}
      </Text>
      <Flex justify="space-between" align="center" mt={4}>
        <Text fontSize="2xl" fontWeight="bold" color="blue.500">
          ${product.price}
        </Text>
        <Button colorScheme="blue">Buy</Button>
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

// ✅ SETUP
import { MantineProvider } from '@mantine/core';
import '@mantine/core/styles.css';

function App() {
  return (
    <MantineProvider>
      <YourApp />
    </MantineProvider>
  );
}

// ✅ BASIC USAGE
import { Button, TextInput, Stack, Paper } from '@mantine/core';

function LoginForm() {
  return (
    <Paper p="md" shadow="sm">
      {' '}
      {/* 📄 Paper = card container */}
      <Stack gap="md">
        {' '}
        {/* 📊 Stack với gap */}
        <TextInput
          label="Email"
          placeholder="Enter email"
          required // ✅ Required field
        />
        <TextInput
          label="Password"
          type="password"
          placeholder="Enter password"
          required
        />
        <Button fullWidth>Login</Button>
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
  const form = useForm<FormValues>({
    initialValues: {
      email: '',
      password: '',
    },
    validate: {
      email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Email không hợp lệ'),
      password: (value) =>
        value.length < 8 ? 'Password phải có ít nhất 8 ký tự' : null,
    },
  });

  const handleSubmit = (values: FormValues) => {
    console.log('Form values:', values);
  };

  return (
    <form onSubmit={form.onSubmit(handleSubmit)}>
      <Stack gap="md">
        <TextInput
          label="Email"
          placeholder="Enter email"
          {...form.getInputProps('email')} // 🎮 Auto bind value, onChange, error
          // 💡 Tương đương:
          // value={form.values.email}
          // onChange={(e) => form.setFieldValue('email', e.target.value)}
          // error={form.errors.email}
        />

        <TextInput
          label="Password"
          type="password"
          placeholder="Enter password"
          {...form.getInputProps('password')}
        />

        {form.errors.root && <Alert color="red">{form.errors.root}</Alert>}

        <Button type="submit">Login</Button>
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

// ✅ BASIC USAGE - Dialog
import * as Dialog from '@radix-ui/react-dialog';

function MyDialog() {
  return (
    <Dialog.Root>
      {' '}
      {/* 🎮 Root component (state management) */}
      <Dialog.Trigger asChild>
        {' '}
        {/* 🖱️ Trigger button */}
        <button>Open Dialog</button>
      </Dialog.Trigger>
      <Dialog.Portal>
        {' '}
        {/* 🌐 Portal (render outside DOM tree) */}
        <Dialog.Overlay className="dialog-overlay" />{' '}
        {/* 🎨 Overlay backdrop */}
        <Dialog.Content className="dialog-content">
          {' '}
          {/* 📄 Dialog content */}
          <Dialog.Title>Dialog Title</Dialog.Title>
          <Dialog.Description>Dialog description text</Dialog.Description>
          <Dialog.Close asChild>
            {' '}
            {/* ❌ Close button */}
            <button>Close</button>
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

function UserMenu() {
  return (
    <DropdownMenu.Root>
      <DropdownMenu.Trigger asChild>
        <button>User Menu</button>
      </DropdownMenu.Trigger>

      <DropdownMenu.Portal>
        <DropdownMenu.Content>
          <DropdownMenu.Item>Profile</DropdownMenu.Item>
          <DropdownMenu.Item>Settings</DropdownMenu.Item>
          <DropdownMenu.Separator />
          <DropdownMenu.Item>Logout</DropdownMenu.Item>
        </DropdownMenu.Content>
      </DropdownMenu.Portal>
    </DropdownMenu.Root>
  );
}

// ✅ ACCESSIBILITY FEATURES (tự động có)
// - Keyboard navigation (Arrow keys, Enter, Escape)
// - Focus management
// - ARIA attributes
// - Screen reader support
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

// ✅ BASIC USAGE - Dialog
import { Dialog } from '@headlessui/react';

function MyDialog({
  isOpen,
  onClose,
}: {
  isOpen: boolean;
  onClose: () => void;
}) {
  return (
    <Dialog open={isOpen} onClose={onClose}>
      <Dialog.Backdrop /> {/* 🎨 Backdrop overlay */}
      <Dialog.Panel>
        {' '}
        {/* 📄 Dialog panel */}
        <Dialog.Title>Dialog Title</Dialog.Title>
        <Dialog.Description>Dialog description</Dialog.Description>
        <button onClick={onClose}>Close</button>
      </Dialog.Panel>
    </Dialog>
  );
}

// ✅ DROPDOWN MENU
import { Menu } from '@headlessui/react';

function UserMenu() {
  return (
    <Menu>
      <Menu.Button>Options</Menu.Button>
      <Menu.Items>
        <Menu.Item>
          {({ active }) => (
            <a className={active ? 'bg-blue-500' : ''}>Profile</a>
          )}
        </Menu.Item>
        <Menu.Item>
          <a>Settings</a>
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

// 📦 SETUP (one-time)
// npx shadcn-ui@latest init

// ✅ USAGE - Copy component code vào project
// Components được copy vào src/components/ui/

import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';

function LoginForm() {
  return (
    <div>
      <Input type="email" placeholder="Email" />
      <Input type="password" placeholder="Password" />
      <Button>Login</Button>
    </div>
  );
}

// 💡 COMPONENT STRUCTURE (sau khi copy)
// src/components/ui/button.tsx
// - Code component với Tailwind classes
// - Bạn có thể sửa trực tiếp
// - Không phụ thuộc vào npm package
```

---

## 9. Comparison Matrix

### **9.1. Detailed Comparison**

```typescript
/**
 * 📊 COMPONENT LIBRARIES COMPARISON MATRIX
 */

const COMPARISON = {
  'Material-UI (MUI)': {
    bundleSize: '~300KB', // ⚠️ Large
    components: '100+', // ✅ Many
    customization: 'Theme-based', // ✅ Good
    accessibility: 'WCAG 2.1', // ✅ Excellent
    typescript: true, // ✅ Full support
    learningCurve: 'Medium', // 📚 Medium
    designSystem: 'Material Design', // 🎨 Google's design
    bestFor: ['Enterprise apps', 'Admin dashboards', 'Material Design apps'],
  },

  'Ant Design': {
    bundleSize: '~500KB', // ⚠️ Very large
    components: '60+', // ✅ Many
    customization: 'Theme-based', // ✅ Good
    accessibility: 'Good', // ✅ Good
    typescript: true, // ✅ Full support
    learningCurve: 'Medium', // 📚 Medium
    designSystem: 'Ant Design', // 🎨 Ant Design system
    bestFor: ['Admin dashboards', 'Data-heavy apps', 'Enterprise tools'],
  },

  'Chakra UI': {
    bundleSize: '~150KB', // ✅ Medium
    components: '50+', // ✅ Good
    customization: 'Props-based', // ✅ Excellent
    accessibility: 'WCAG 2.1', // ✅ Excellent
    typescript: true, // ✅ Full support
    learningCurve: 'Low', // 📚 Easy
    designSystem: 'Custom', // 🎨 Flexible
    bestFor: ['Modern apps', 'MVPs', 'Custom designs'],
  },

  Mantine: {
    bundleSize: '~200KB', // ✅ Medium
    components: '100+', // ✅ Many
    customization: 'Props-based', // ✅ Excellent
    accessibility: 'WCAG 2.1', // ✅ Excellent
    typescript: true, // ✅ Excellent
    learningCurve: 'Medium', // 📚 Medium
    designSystem: 'Custom', // 🎨 Flexible
    bestFor: ['Full-featured apps', 'Form-heavy apps', 'Date picker apps'],
  },

  'Radix UI': {
    bundleSize: '~50KB per component', // ✅ Small
    components: '20+ primitives', // ✅ Primitives
    customization: 'Full control', // ✅ Full control
    accessibility: 'WCAG 2.1', // ✅ Excellent
    typescript: true, // ✅ Excellent
    learningCurve: 'Medium-High', // 📚 Medium-High
    designSystem: 'Headless (no styles)', // 🎨 You style
    bestFor: [
      'Custom design systems',
      'Tailwind projects',
      'Accessibility-critical',
    ],
  },

  'Shadcn/ui': {
    bundleSize: 'Zero (copy code)', // ✅ Zero
    components: '30+', // ✅ Growing
    customization: 'Full control', // ✅ Full control
    accessibility: 'WCAG 2.1', // ✅ Excellent (Radix-based)
    typescript: true, // ✅ Excellent
    learningCurve: 'Medium', // 📚 Medium
    designSystem: 'Tailwind CSS', // 🎨 Tailwind
    bestFor: ['Tailwind projects', 'Custom designs', 'Own the code'],
  },
};
```

### **9.2. Bundle Size Comparison**

```typescript
/**
 * 📦 BUNDLE SIZE COMPARISON (gzipped)
 *
 * ❌ VERY LARGE (>400KB):
 * - Ant Design: ~500KB
 * - Material-UI: ~300KB
 *
 * ⚠️ MEDIUM (100-300KB):
 * - Mantine: ~200KB
 * - Chakra UI: ~150KB
 *
 * ✅ SMALL (<100KB):
 * - Radix UI: ~50KB per component (chỉ import cần)
 * - Headless UI: ~30KB per component
 * - Shadcn/ui: 0KB (copy code, không phải library)
 *
 * 💡 TREE-SHAKING TIPS:
 * - Import specific components: import { Button } from '@mui/material'
 * - Không import entire library: import * from '@mui/material' ❌
 * - Use path imports: import Button from '@mui/material/Button' ✅
 */

// ❌ BAD: Import entire library
import * as MUI from '@mui/material';
// 💥 Import TẤT CẢ components → bundle size lớn

// ✅ GOOD: Import specific components
import { Button, TextField } from '@mui/material';
// 🚀 Chỉ import components cần → tree-shaking hoạt động

// ✅ BETTER: Path imports (smaller bundle)
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
// 🚀 Path imports → bundle size nhỏ hơn
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
