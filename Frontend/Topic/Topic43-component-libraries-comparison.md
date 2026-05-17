# 🎨 Topic 43: Component Libraries Comparison - MUI, Ant Design, Chakra, Mantine, Radix, Headless UI & shadcn/ui

## 1. ⭐ Senior/Staff Summary

Component library giúp team ship UI nhanh hơn bằng cách cung cấp sẵn `Button`, `Input`, `Modal`, `Select`, `Table`, `DatePicker`, `Toast`, `Tooltip`, keyboard interaction, focus management và accessibility baseline. Nhưng chọn sai library có thể tạo **bundle bloat**, UI khó customize, accessibility giả an toàn, vendor lock-in và design system rời rạc.

Điểm senior cần nhìn:

- ✅ **MUI**: mạnh cho enterprise app cần Material Design, ecosystem lớn, MUI X mạnh cho Data Grid/Date Picker nhưng customization sâu có thể tốn công.
- ✅ **Ant Design**: rất hợp admin dashboard, back-office, data-heavy app; nhiều component enterprise sẵn có nhưng style/opinion khá mạnh.
- ✅ **Chakra UI**: DX tốt, style props dễ học, hợp app cần UI nhanh và accessible defaults; cần kiểm soát design token để tránh inline-style feeling.
- ✅ **Mantine**: full-featured, nhiều hooks/components, hợp product app cần form/date/table-like primitives nhanh; API thực dụng.
- ✅ **Radix UI**: headless primitives, accessibility/focus behavior tốt, hợp custom design system; cần tự styling và tự build layer component.
- ✅ **Headless UI**: unstyled accessible components từ Tailwind Labs, hợp Tailwind app cần primitives đơn giản; coverage ít hơn Radix.
- ✅ **shadcn/ui**: không phải package component library truyền thống; là collection component copy vào codebase, thường dựa trên Radix + Tailwind. Hợp team muốn sở hữu code và customize sâu.

> 💡 Mental model: **Component library không chỉ là “giao diện đẹp”**. Nó là quyết định kiến trúc ảnh hưởng tới design system, accessibility, bundle, SSR/RSC, testing, team velocity và chi phí maintain nhiều năm.

## 2. 🧠 Key Mental Model

### 2.1. Ba nhóm component library

```text
Styled / Opinionated
  MUI, Ant Design, Chakra UI, Mantine
  → Ship nhanh, nhiều component, có design language sẵn.

Headless / Primitive
  Radix UI, Headless UI
  → Có behavior + accessibility, tự quyết định styling.

Copy-owned components
  shadcn/ui
  → Copy code vào repo, team sở hữu và chỉnh sửa như code nội bộ.
```

### 2.2. Tradeoff cốt lõi

| Trục đánh giá | Styled library | Headless library | shadcn/ui |
|---|---|---|---|
| Ship nhanh | ✅ Cao | ⚠️ Trung bình | ✅ Cao nếu dùng Tailwind |
| Custom brand | ⚠️ Tùy library | ✅ Rất tốt | ✅ Rất tốt |
| Accessibility behavior | ✅ Có sẵn nhiều | ✅ Rất mạnh | ✅ Dựa nhiều vào Radix |
| Bundle control | ⚠️ Phải kiểm tra | ✅ Tốt hơn | ✅ Bạn kiểm soát code |
| Maintenance | ✅ Library update hộ | ⚠️ Tự build wrapper | ⚠️ Tự merge update |
| Design consistency | ✅ Nếu dùng theme đúng | ✅ Nếu design token tốt | ✅ Nếu governance tốt |
| Vendor lock-in | ⚠️ Trung bình/cao | ✅ Thấp hơn | ✅ Thấp hơn nhưng code fork nhiều |

### 2.3. Một câu hỏi quyết định

Trước khi chọn library, hỏi:

> Team cần **ship nhanh theo design có sẵn**, hay cần **xây design system riêng có kiểm soát lâu dài**?

Nếu ship nhanh cho admin/internal tool, chọn MUI/Ant/Mantine thường hợp lý. Nếu xây product brand riêng hoặc design system nhiều năm, Radix/shadcn/headless approach thường dễ kiểm soát hơn.

## 3. 📚 Main Concepts

### 3.1. Component library giải quyết gì?

Một component production không chỉ là CSS:

- visual states: default, hover, active, disabled, loading, error
- keyboard interaction: `Tab`, `Enter`, `Escape`, arrow keys
- focus management: focus trap trong modal, restore focus sau khi đóng
- accessibility: semantic HTML, ARIA, screen reader behavior
- responsiveness: layout, touch target, mobile behavior
- theming: color, spacing, typography, radius, shadow, dark mode
- integration: form library, router, SSR, RSC, testing
- maintenance: breaking changes, token migration, browser support

Ví dụ `Select` tốt phải xử lý:

- keyboard navigation
- screen reader announcement
- virtualized long list nếu nhiều option
- search/filter
- controlled/uncontrolled state
- portal positioning
- mobile UX
- validation/error message

### 3.2. MUI - Material UI

MUI là React component library triển khai Material Design. Nó có ecosystem lớn, docs tốt và các package nâng cao như MUI X.

**Hợp khi:**

- Enterprise app cần component ổn định, phổ biến.
- Team chấp nhận Material Design hoặc có thể theme theo brand.
- Cần Data Grid, Date Picker, Charts, Tree View hoặc component nâng cao từ MUI X.
- Dự án cần docs nhiều, cộng đồng lớn, hiring dễ.

**Cẩn thận khi:**

- Brand khác xa Material Design.
- Muốn override style quá sâu ở mọi component.
- Bundle/performance là constraint lớn trên mobile.
- Không muốn phụ thuộc vào CSS-in-JS/theming model của MUI.

```tsx
import { Button, Stack, TextField, ThemeProvider, createTheme } from '@mui/material';

const theme = createTheme({
  palette: {
    primary: { main: '#2563eb' },
  },
  shape: {
    borderRadius: 6,
  },
});

export function LoginForm() {
  return (
    <ThemeProvider theme={theme}>
      <Stack component="form" spacing={2} maxWidth={360}>
        <TextField label="Email" name="email" type="email" />
        <TextField label="Password" name="password" type="password" />
        <Button type="submit" variant="contained">
          Login
        </Button>
      </Stack>
    </ThemeProvider>
  );
}
```

**Senior note:** Với MUI, hãy customize qua theme/design tokens trước. Đừng rải `sx` override khắp app nếu muốn maintain design system lâu dài.

### 3.3. Ant Design

Ant Design là React UI library hướng mạnh vào enterprise web applications: dashboard, admin, CRUD, form lớn, table nhiều cột, filter, pagination.

**Hợp khi:**

- Back-office/admin dashboard.
- Data-heavy app cần `Table`, `Form`, `DatePicker`, `Select`, `Tree`, `Upload`.
- Team không có design system riêng nhưng cần UI nhất quán nhanh.
- Sản phẩm nội bộ ưu tiên tốc độ ship hơn brand uniqueness.

**Cẩn thận khi:**

- Public-facing product cần brand riêng mạnh.
- App cần semantic HTML cực chặt, accessibility audit nghiêm ngặt.
- Muốn design tối giản, nhẹ, ít opinion.
- Muốn mix với Tailwind/custom CSS nhiều mà không có governance.

```tsx
import { Button, Form, Input, Table } from 'antd';

type User = {
  id: string;
  name: string;
  email: string;
};

const columns = [
  { title: 'Name', dataIndex: 'name', key: 'name' },
  { title: 'Email', dataIndex: 'email', key: 'email' },
];

export function UsersAdmin({ users }: { users: User[] }) {
  return (
    <section>
      <Form layout="inline">
        <Form.Item name="keyword">
          <Input.Search placeholder="Search users" />
        </Form.Item>
        <Button type="primary">Create user</Button>
      </Form>

      <Table rowKey="id" columns={columns} dataSource={users} />
    </section>
  );
}
```

**Senior note:** Ant Design rất mạnh cho CRUD productivity, nhưng nên wrap các component quan trọng (`AppTable`, `AppForm`, `AppModal`) để giảm lock-in và áp design convention của team.

### 3.4. Chakra UI

Chakra UI nổi bật với style props, component API dễ đọc và accessible defaults. Chakra v3 đi theo hướng composition/token tốt hơn, nhưng team vẫn cần governance để tránh mỗi màn hình style một kiểu.

**Hợp khi:**

- Team muốn DX nhanh, dễ học.
- Product app vừa và nhỏ cần UI hiện đại, dark mode, responsive props.
- Team thích style props thay vì viết CSS file nhiều.
- Cần build component wrapper nhanh.

**Cẩn thận khi:**

- Design system lớn cần token governance chặt.
- Team lạm dụng style props trực tiếp trong feature code.
- App cần SSR/RSC rất nghiêm ngặt, phải kiểm tra provider/client boundary.

```tsx
import { Button, Field, Input, Stack } from '@chakra-ui/react';

export function ProfileForm() {
  return (
    <Stack as="form" gap="4" maxW="sm">
      <Field.Root required>
        <Field.Label>Display name</Field.Label>
        <Input name="displayName" />
        <Field.HelperText>Tên này sẽ hiển thị trong workspace.</Field.HelperText>
      </Field.Root>

      <Button type="submit" colorPalette="blue">
        Save
      </Button>
    </Stack>
  );
}
```

**Senior note:** Với Chakra, nên tạo layer design-system component như `PrimaryButton`, `FormField`, `PageStack` để tránh feature code chứa quá nhiều quyết định visual.

### 3.5. Mantine

Mantine là library thực dụng, nhiều component và hooks, có form utilities, notifications, modals, dates, charts ecosystem. Nó thường hợp product team muốn nhiều building blocks nhưng không muốn Material/Ant look quá rõ.

**Hợp khi:**

- SaaS/product app cần nhiều component nhanh.
- Team cần form/date/notification/hooks tiện.
- Muốn theming tốt nhưng không quá bị ràng buộc bởi Material Design.
- Prototype đến production với API tương đối đầy đủ.

**Cẩn thận khi:**

- Team đã có design system rất riêng.
- Muốn headless hoàn toàn.
- Không kiểm soát import và style provider.

```tsx
import { Button, Group, TextInput } from '@mantine/core';
import { useForm } from '@mantine/form';

export function InviteMemberForm() {
  const form = useForm({
    initialValues: { email: '' },
    validate: {
      email: (value) => (/^\S+@\S+$/.test(value) ? null : 'Email không hợp lệ'),
    },
  });

  return (
    <form onSubmit={form.onSubmit((values) => console.log(values))}>
      <TextInput
        label="Email"
        placeholder="teammate@example.com"
        {...form.getInputProps('email')}
      />
      <Group mt="md">
        <Button type="submit">Invite</Button>
      </Group>
    </form>
  );
}
```

**Senior note:** Mantine có nhiều “batteries included”; hãy chuẩn hóa wrapper và tokens sớm để app không thành tập hợp component dùng tùy hứng.

### 3.6. Radix UI

Radix UI là headless/unstyled primitives tập trung vào accessibility, keyboard interaction và composability. Nó không quyết định visual style.

**Hợp khi:**

- Team có design riêng hoặc design system nội bộ.
- Cần accessible behavior cho Dialog, Dropdown, Popover, Select, Tooltip.
- Muốn kiểm soát CSS/Tailwind/CSS Modules/stitches riêng.
- Cần composition linh hoạt, ví dụ `asChild`.

**Cẩn thận khi:**

- Team muốn UI đẹp ngay mà không có designer/CSS capacity.
- Không có người đủ kinh nghiệm xây design token/component layer.
- Expect Radix là full component library giống MUI/Ant.

```tsx
import * as Dialog from '@radix-ui/react-dialog';

export function ConfirmDeleteDialog() {
  return (
    <Dialog.Root>
      <Dialog.Trigger asChild>
        <button className="btn btn-danger">Delete</button>
      </Dialog.Trigger>

      <Dialog.Portal>
        <Dialog.Overlay className="dialog-overlay" />
        <Dialog.Content className="dialog-content">
          <Dialog.Title>Xóa project?</Dialog.Title>
          <Dialog.Description>
            Hành động này không thể hoàn tác.
          </Dialog.Description>

          <div className="dialog-actions">
            <Dialog.Close asChild>
              <button>Cancel</button>
            </Dialog.Close>
            <button className="btn btn-danger">Confirm</button>
          </div>
        </Dialog.Content>
      </Dialog.Portal>
    </Dialog.Root>
  );
}
```

**Senior note:** Radix thường là nền tốt cho design system, không phải câu trả lời cuối cùng. Team vẫn cần API wrapper, styling convention, testing và docs.

### 3.7. Headless UI

Headless UI là unstyled accessible component library từ Tailwind Labs. Nó phù hợp với Tailwind app cần primitives như Dialog, Menu, Listbox, Combobox, Switch, Tabs.

**Hợp khi:**

- Project dùng Tailwind.
- Cần headless primitives đơn giản.
- Team muốn API ít hơn Radix, dễ tiếp cận.
- UI không cần quá nhiều component enterprise.

**Cẩn thận khi:**

- Cần coverage component rộng.
- Cần primitives chi tiết như Radix.
- Không dùng Tailwind hoặc không thích class-heavy styling.

```tsx
import { Dialog, DialogPanel, DialogTitle } from '@headlessui/react';

export function SettingsDialog({
  open,
  onClose,
}: {
  open: boolean;
  onClose: () => void;
}) {
  return (
    <Dialog open={open} onClose={onClose} className="relative z-50">
      <div className="fixed inset-0 bg-black/30" />
      <div className="fixed inset-0 flex items-center justify-center p-4">
        <DialogPanel className="w-full max-w-md rounded bg-white p-6">
          <DialogTitle className="text-lg font-semibold">Settings</DialogTitle>
          <p className="mt-2 text-sm text-gray-600">Update workspace settings.</p>
        </DialogPanel>
      </div>
    </Dialog>
  );
}
```

### 3.8. shadcn/ui

shadcn/ui là collection component bạn copy vào project. Nó thường dùng Radix primitives, Tailwind CSS và `class-variance-authority`. Vì code nằm trong repo, team có toàn quyền chỉnh sửa.

**Hợp khi:**

- Project dùng Tailwind.
- Team muốn sở hữu component code.
- Cần UI hiện đại nhanh nhưng vẫn customize sâu.
- Muốn tránh lock-in vào package component runtime.
- Build design system vừa và nhỏ.

**Cẩn thận khi:**

- Team không muốn maintain copied code.
- Không có convention cho update upstream.
- Copy nhiều component nhưng không chuẩn hóa design token.
- Nhiều project cùng dùng nhưng không có shared package/registry nội bộ.

```tsx
import { Button } from '@/components/ui/button';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import { Input } from '@/components/ui/input';

export function BillingCard() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Billing email</CardTitle>
        <CardDescription>Nhận invoice và payment notification.</CardDescription>
      </CardHeader>
      <CardContent className="flex gap-2">
        <Input type="email" placeholder="finance@example.com" />
        <Button>Save</Button>
      </CardContent>
    </Card>
  );
}
```

**Senior note:** Với shadcn/ui, “dependency” không chỉ nằm trong `package.json`; dependency nằm ở code copy về. Cần ownership rõ: ai update, ai review accessibility, ai chuẩn hóa variants.

### 3.9. Comparison Matrix

| Library | Kiểu | Strength | Weakness | Best for |
|---|---|---|---|---|
| MUI | Styled/opinionated | Ecosystem lớn, docs tốt, MUI X mạnh | Material look, customization sâu tốn công | Enterprise app, app cần Material |
| Ant Design | Styled/opinionated | Admin/data components mạnh | Opinionated, brand riêng khó | Internal tools, dashboard |
| Chakra UI | Styled/system props | DX tốt, accessible defaults | Dễ lạm dụng style props | SaaS app, team nhỏ/vừa |
| Mantine | Styled/full-featured | Nhiều component/hooks/form | Cần governance để không tùy hứng | Product app, prototype-to-prod |
| Radix UI | Headless primitives | A11y/focus/composition mạnh | Cần tự style/build wrappers | Custom design system |
| Headless UI | Headless primitives | Hợp Tailwind, API đơn giản | Coverage ít hơn | Tailwind app cần primitives |
| shadcn/ui | Copy-owned | Sở hữu code, đẹp nhanh, customize sâu | Tự maintain/update | Tailwind + custom design |

### 3.10. Bundle size và performance

Không nên tin tuyệt đối các con số bundle size trong blog cũ vì version, bundler, import style và app code khác nhau. Senior approach là đo trong project thật.

```bash
npm run build
npx source-map-explorer 'dist/assets/*.js'
```

Hoặc với Next.js:

```bash
ANALYZE=true npm run build
```

Các yếu tố ảnh hưởng bundle:

- import theo path hay barrel import
- tree-shaking có hoạt động không
- CSS-in-JS runtime hay static CSS
- icon package import sai
- date library dependency
- data grid/date picker/charts thường nặng hơn button/input
- client boundary trong Next.js App Router

### 3.11. Accessibility không phải “library có là xong”

Library tốt giúp baseline, nhưng app vẫn có thể fail WCAG nếu dùng sai:

- Dialog không có title/description.
- Button icon không có accessible name.
- Error message không liên kết với field.
- Color contrast không đạt sau khi customize theme.
- Table thiếu header/scope hoặc dùng table cho layout.
- Dropdown custom không test keyboard.
- Toast chứa thông tin quan trọng nhưng không có persistent fallback.

### 3.12. SSR, RSC và Next.js App Router

Khi dùng Next.js App Router hoặc React Server Components:

- Nhiều UI libraries cần provider ở Client Component.
- Component có event handler, state, effect phải nằm trong `"use client"` boundary.
- Headless primitives như Dialog/Popover thường client-side.
- CSS-in-JS cần setup SSR đúng để tránh flash/mismatch.
- shadcn/ui có lợi vì component nằm trong codebase, nhưng nhiều component vẫn dùng Radix client-side.

```tsx
// app/providers.tsx
'use client';

import { ThemeProvider } from '@mui/material/styles';
import { theme } from '@/design/theme';

export function Providers({ children }: { children: React.ReactNode }) {
  return <ThemeProvider theme={theme}>{children}</ThemeProvider>;
}
```

### 3.13. Design tokens và theming

Design token là contract giữa design và code:

- color: `primary`, `danger`, `surface`, `border`
- spacing: `xs`, `sm`, `md`, `lg`
- typography: `body`, `label`, `heading`
- radius: `none`, `sm`, `md`
- shadow/elevation
- motion duration/easing

**Rule tốt:** feature code không nên hardcode màu/spacing tùy tiện. Hãy dùng token hoặc wrapper component.

```tsx
// ❌ Khó maintain nếu rải khắp app
<Button sx={{ backgroundColor: '#1d4ed8', borderRadius: '13px' }}>Save</Button>

// ✅ Tốt hơn: token nằm trong theme hoặc variant
<Button color="primary" variant="contained">Save</Button>
```

### 3.14. Wrapper layer để giảm lock-in

Không cần wrap mọi component ngay từ ngày đầu. Nhưng nên wrap component có business/design rule quan trọng:

- `AppButton`
- `AppModal`
- `AppTable`
- `FormField`
- `DateRangePicker`
- `EmptyState`
- `PageHeader`
- `DataToolbar`

```tsx
import { Button as MuiButton } from '@mui/material';
import type { ButtonProps as MuiButtonProps } from '@mui/material';

type AppButtonProps = MuiButtonProps & {
  trackingId?: string;
};

export function AppButton({ trackingId, onClick, ...props }: AppButtonProps) {
  return (
    <MuiButton
      {...props}
      onClick={(event) => {
        if (trackingId) {
          console.log('track', trackingId);
        }
        onClick?.(event);
      }}
    />
  );
}
```

Wrapper có ích khi:

- cần analytics
- cần consistent loading state
- cần policy accessibility
- cần theme variants
- cần đổi library sau này

Wrapper quá mức gây hại khi:

- chỉ pass-through 100% props mà không thêm rule
- che mất API hữu ích của library
- tạo layer khó debug

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Decision scorecard

```ts
type LibraryScore = {
  velocity: number;
  customization: number;
  accessibility: number;
  bundleControl: number;
  enterpriseComponents: number;
  maintenanceCost: number;
};

const weights = {
  velocity: 2,
  customization: 3,
  accessibility: 3,
  bundleControl: 2,
  enterpriseComponents: 2,
  maintenanceCost: -2,
};

function scoreLibrary(score: LibraryScore) {
  return Object.entries(weights).reduce((total, [key, weight]) => {
    return total + score[key as keyof LibraryScore] * weight;
  }, 0);
}

const radixForDesignSystem = scoreLibrary({
  velocity: 3,
  customization: 5,
  accessibility: 5,
  bundleControl: 5,
  enterpriseComponents: 2,
  maintenanceCost: 4,
});

console.log(radixForDesignSystem);
```

Scorecard không thay quyết định kỹ thuật, nhưng giúp team nói chuyện bằng tiêu chí rõ ràng thay vì “em thích library này”.

### 4.2. App-level component boundary

```tsx
// components/ui/AppTextField.tsx
import { TextField } from '@mui/material';
import type { TextFieldProps } from '@mui/material';

type AppTextFieldProps = TextFieldProps & {
  errorText?: string;
};

export function AppTextField({ errorText, helperText, ...props }: AppTextFieldProps) {
  return (
    <TextField
      {...props}
      error={Boolean(errorText) || props.error}
      helperText={errorText ?? helperText}
      slotProps={{
        htmlInput: {
          'aria-invalid': Boolean(errorText) || props.error || undefined,
          ...props.slotProps?.htmlInput,
        },
      }}
    />
  );
}
```

### 4.3. Avoid mixing libraries trong cùng một form

```tsx
// ❌ UI không nhất quán, validation state khó đồng bộ
import { Button } from '@mui/material';
import { Input } from 'antd';
import { Select } from '@chakra-ui/react';

export function MixedForm() {
  return (
    <form>
      <Input />
      <Select />
      <Button>Save</Button>
    </form>
  );
}
```

```tsx
// ✅ Chọn một visual system cho một surface
import { Button, Form, Input, Select } from 'antd';

export function UserForm() {
  return (
    <Form layout="vertical">
      <Form.Item label="Name" name="name">
        <Input />
      </Form.Item>
      <Form.Item label="Role" name="role">
        <Select options={[{ label: 'Admin', value: 'admin' }]} />
      </Form.Item>
      <Button type="primary">Save</Button>
    </Form>
  );
}
```

### 4.4. Icon import đúng cách

```tsx
// ❌ Có thể kéo nhiều code không cần thiết tùy package/bundler
import * as Icons from '@mui/icons-material';

export function SaveButton() {
  return <Icons.Save />;
}
```

```tsx
// ✅ Import icon cụ thể
import SaveIcon from '@mui/icons-material/Save';

export function SaveButton() {
  return <SaveIcon fontSize="small" />;
}
```

### 4.5. Accessible icon button

```tsx
import { X } from 'lucide-react';

export function CloseButton({ onClick }: { onClick: () => void }) {
  return (
    <button aria-label="Đóng hộp thoại" type="button" onClick={onClick}>
      <X aria-hidden="true" size={16} />
    </button>
  );
}
```

Library có thể cung cấp `IconButton`, nhưng accessible name vẫn là trách nhiệm của app code.

### 4.6. Testing component library usage

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('opens settings dialog', async () => {
  render(<SettingsPage />);

  await userEvent.click(screen.getByRole('button', { name: /settings/i }));

  expect(
    screen.getByRole('dialog', { name: /workspace settings/i })
  ).toBeInTheDocument();
});
```

Test theo role/name giúp bắt lỗi accessibility thật hơn snapshot class name.

## 5. 🏗️ Production Notes / React Implications

### 5.1. React rendering và performance

Component library có thể làm render tree sâu hơn. Điều này không luôn xấu, nhưng cần để ý:

- Table lớn cần virtualization.
- Dropdown/Popover dùng portal cần test z-index/focus.
- Theme object phải stable, tránh tạo theme trong render.
- Wrapper component không nên tạo object/function mới quá nhiều trong hot path.
- CSS-in-JS runtime có thể ảnh hưởng SSR và initial render nếu setup sai.

```tsx
// ❌ Theme được tạo lại mỗi render
function App({ children }: { children: React.ReactNode }) {
  const theme = createTheme({ palette: { mode: 'light' } });
  return <ThemeProvider theme={theme}>{children}</ThemeProvider>;
}

// ✅ Theme stable ngoài render
const theme = createTheme({ palette: { mode: 'light' } });

function App({ children }: { children: React.ReactNode }) {
  return <ThemeProvider theme={theme}>{children}</ThemeProvider>;
}
```

### 5.2. Security

UI library không tự giải quyết security:

- Rich text, markdown preview, HTML injection vẫn cần sanitize.
- Upload component vẫn cần server-side validation.
- Table export CSV cần tránh formula injection.
- Link/button external cần `rel="noopener noreferrer"` nếu `target="_blank"`.
- Form validation client chỉ là UX, không phải security boundary.

### 5.3. Observability

Với design system lớn, nên track:

- component usage inventory
- bundle impact theo route
- accessibility violations trong CI
- visual regression
- error rate ở form/modal/checkout flow
- design token drift

### 5.4. Migration strategy nếu muốn đổi library

Đổi component library là migration tốn kém vì ảnh hưởng markup, styling, behavior, tests và design review.

Chiến lược ít rủi ro:

- Không đổi toàn app một lần.
- Bắt đầu từ route ít rủi ro.
- Tạo wrapper cho component core.
- Freeze feature mới trên library cũ nếu cần.
- Dùng visual regression để bắt khác biệt.
- Có guideline rõ: library cũ được dùng ở đâu, library mới dùng ở đâu.

## 6. ⚠️ Common Pitfalls

### 6.1. Chọn library theo popularity thay vì requirement

Star GitHub không nói app của bạn cần gì. Hãy map requirement: admin table, custom brand, a11y audit, mobile performance, SSR, team skill.

### 6.2. Tin “accessible by default” tuyệt đối

Library có thể xử lý keyboard/focus tốt, nhưng app vẫn phải cung cấp label, error text, contrast, DOM structure và flow đúng.

### 6.3. Mix nhiều visual libraries

MUI button + Ant form + Chakra modal thường tạo UX thiếu nhất quán và bundle lớn. Có thể mix headless primitive với styled system, nhưng phải có design rule rõ.

### 6.4. Override CSS bằng selector sâu

```css
/* ❌ Dễ vỡ khi library đổi DOM */
.MuiButton-root > span:nth-child(2) {
  margin-left: 12px;
}
```

Ưu tiên theme token, variant, slot props hoặc wrapper API.

### 6.5. Không đo bundle thực tế

Bundle size trên website không phản ánh route của bạn. Phải đo sau build production.

### 6.6. Không chuẩn hóa form pattern

Mỗi library có form story khác nhau. Nếu app dùng React Hook Form/Zod, cần convention rõ cho integration với field/error/helper text.

### 6.7. Copy shadcn/ui nhưng không maintain

Copy code nghĩa là team chịu trách nhiệm update, security, accessibility, API consistency. Không có `npm update` tự động sửa component đã customize.

### 6.8. Dùng Data Table built-in cho mọi thứ

Table đơn giản khác với data grid enterprise. Sorting/filtering server-side, virtualization, column pinning, row selection, export và permission đều cần thiết kế rõ.

### 6.9. Không test mobile/touch

Popover, Select, DatePicker, Drawer có thể ổn desktop nhưng tệ trên mobile. Touch target, keyboard mobile và viewport resize cần QA thật.

### 6.10. Không có ownership

Design system cần người/chapter ownership. Nếu không, library sẽ bị dùng tùy hứng, token drift và duplicate component tăng dần.

## 7. ✅ Decision Guide / Checklist

### 7.1. Chọn nhanh theo use case

| Use case | Nên cân nhắc |
|---|---|
| Admin dashboard ship nhanh | Ant Design, MUI, Mantine |
| Enterprise app Material Design | MUI |
| Internal CRUD nhiều form/table | Ant Design, Mantine |
| SaaS app cần DX nhanh | Chakra UI, Mantine, shadcn/ui |
| Custom brand/design system | Radix UI, shadcn/ui, Headless UI |
| Tailwind-first app | shadcn/ui, Headless UI, Radix UI |
| Accessibility primitives | Radix UI, Headless UI |
| Data grid nâng cao | MUI X, Ant Design Table, TanStack Table + custom UI |
| Muốn sở hữu component code | shadcn/ui hoặc internal library |

### 7.2. Checklist trước khi chọn library

- [ ] Có đủ component cho 80% screen không?
- [ ] Có support TypeScript tốt không?
- [ ] Có accessibility baseline và docs rõ không?
- [ ] Theming có map được với design tokens không?
- [ ] Bundle impact sau build production ra sao?
- [ ] Có hoạt động tốt với SSR/RSC/framework hiện tại không?
- [ ] Có form integration rõ với React Hook Form/Zod không?
- [ ] Có date picker/table/modal phù hợp requirement không?
- [ ] Team có đủ skill để customize/maintain không?
- [ ] License phù hợp không?
- [ ] Community và release cadence ổn không?
- [ ] Migration/escape hatch nếu đổi library là gì?

### 7.3. Checklist khi đưa vào production

- [ ] Tạo theme/tokens trước khi build nhiều screen.
- [ ] Tạo wrapper cho component core có business rule.
- [ ] Viết docs ngắn: dùng component nào, variant nào, spacing nào.
- [ ] Setup a11y test (`axe`, Testing Library role queries).
- [ ] Setup bundle analyzer.
- [ ] Test modal/select/date picker bằng keyboard.
- [ ] Test mobile/touch.
- [ ] Test dark mode nếu có.
- [ ] Kiểm tra SSR hydration warnings.
- [ ] Định nghĩa ownership cho design system.

### 7.4. Decision tree

```text
Bạn cần admin/data-heavy app nhanh?
  → Ant Design hoặc MUI/Mantine.

Bạn cần custom brand mạnh?
  → Radix UI hoặc shadcn/ui.

Bạn dùng Tailwind và muốn component đẹp nhanh?
  → shadcn/ui.

Bạn muốn headless primitives ít opinion?
  → Radix UI hoặc Headless UI.

Bạn cần ecosystem enterprise và docs lớn?
  → MUI.

Bạn cần nhiều component thực dụng cho SaaS app?
  → Mantine hoặc Chakra UI.
```

## 8. 🎤 Short Interview Answer

Theo em, chọn component library không nên chỉ nhìn “cái nào đẹp” hoặc “cái nào nhiều star”. Em sẽ bắt đầu từ requirement: app là admin dashboard hay product public-facing, có design system riêng không, accessibility audit có nghiêm không, SSR/RSC dùng framework gì, bundle budget ra sao và team có đủ khả năng maintain customization không.

Nếu cần ship internal dashboard nhanh, em thường cân nhắc Ant Design, MUI hoặc Mantine vì có nhiều component như form, table, date picker. Nếu sản phẩm cần brand riêng và design system lâu dài, em nghiêng về Radix hoặc shadcn/ui vì kiểm soát styling tốt hơn. Chakra UI hợp khi team muốn DX nhanh và API dễ học, nhưng vẫn cần governance về token và wrapper.

Điểm quan trọng là library không thay thế design system. Production app vẫn cần token, accessibility checks, wrapper layer hợp lý, bundle analysis, form convention, SSR setup và ownership rõ. Một library tốt dùng sai vẫn tạo ra UI rời rạc và khó maintain.

## 9. 🧾 Ghi nhớ nhanh

- **MUI**: enterprise + Material Design + ecosystem lớn.
- **Ant Design**: admin dashboard + data-heavy CRUD.
- **Chakra UI**: DX dễ, style props, accessible defaults.
- **Mantine**: full-featured, thực dụng, nhiều hooks/components.
- **Radix UI**: headless primitives, accessibility/focus mạnh.
- **Headless UI**: headless đơn giản, hợp Tailwind.
- **shadcn/ui**: copy code, Tailwind + Radix, sở hữu component.
- **Đừng chọn theo star**: chọn theo requirement, team skill và maintenance cost.
- **A11y không tự xong**: vẫn cần label, focus, contrast, testing.
- **Bundle size phải đo thật**: build production + analyzer.
- **Wrapper vừa đủ**: wrap component có rule, không wrap pass-through vô nghĩa.
- **Design token là contract** giữa design và code.

## 10. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| Component library | Bộ component UI dùng sẵn như Button, Modal, Table |
| Design system | Hệ thống quy tắc UI gồm token, component, pattern, docs |
| Design token | Giá trị chuẩn cho màu, spacing, typography, radius, shadow |
| Headless component | Component có behavior/accessibility nhưng không áp style |
| Primitive | Building block cấp thấp để tạo component phức tạp hơn |
| Styled library | Library có sẵn visual design và theme |
| Opinionated | Có cách làm/design mạnh, ít trung lập |
| Accessibility / a11y | Khả năng sử dụng bởi người dùng keyboard/screen reader/assistive tech |
| WCAG | Bộ tiêu chuẩn accessibility cho web |
| Focus management | Điều khiển focus khi mở/đóng modal, menu, popover |
| Focus trap | Giữ focus trong modal/dialog khi đang mở |
| Portal | Render UI ra vị trí DOM khác, thường dùng cho modal/popover |
| Tree-shaking | Loại bỏ code không dùng khỏi bundle |
| Bundle bloat | Bundle JS/CSS phình to do import/dependency không cần thiết |
| CSS-in-JS | Viết/generate CSS trong JavaScript runtime/build |
| SSR | Server-Side Rendering |
| RSC | React Server Components |
| Hydration | React gắn logic client vào HTML render từ server |
| Vendor lock-in | Bị phụ thuộc vào API/style/behavior của một vendor/library |
| Wrapper component | Component nội bộ bọc library component để áp convention |
| Visual regression | Test so sánh ảnh để phát hiện UI thay đổi ngoài ý muốn |

## 11. 📚 Nguồn chính thức đã đối chiếu

- MUI: <https://mui.com/material-ui/>
- Ant Design: <https://ant.design/docs/react/introduce/>
- Chakra UI: <https://chakra-ui.com/docs/components/concepts/overview>
- Mantine: <https://mantine.dev/>
- Radix UI: <https://www.radix-ui.com/primitives/docs/overview/introduction>
- shadcn/ui: <https://ui.shadcn.com/docs/components>
