# 📝 Topic 47: Form Handling & Validation - React Hook Form, Zod, Yup

## 1. ⭐ Senior/Staff Summary

Form là một trong những phần dễ tạo bug nhất trong frontend: state phức tạp, validation nhiều tầng, error UX, accessibility, async API, file upload, multi-step flow và performance khi form lớn. Một senior frontend engineer không chỉ biết dùng `register()` hay `z.object()`, mà phải biết **đặt boundary giữa UI form, schema validation, server validation và business rules**.

Tóm tắt lựa chọn:

- ✅ **React Hook Form (RHF)**: phù hợp đa số React forms hiện đại vì dựa nhiều vào uncontrolled inputs, ít re-render, API tốt cho form lớn.
- ✅ **Zod**: TypeScript-first, schema suy ra type tốt, hợp project TS, API explicit, thường là lựa chọn mặc định cho frontend TS.
- ✅ **Yup**: schema runtime validation linh hoạt, mạnh về transform/conditional validation, phổ biến trong codebase cũ/Formik.
- ✅ **Formik**: dễ hiểu, controlled-oriented, vẫn gặp trong legacy app, nhưng không còn là lựa chọn tối ưu cho large/performance-sensitive forms.
- ✅ **Server validation vẫn bắt buộc**: client validation chỉ là UX, không phải security boundary.

> 💡 Mental model: **Form state là UI state tạm thời; schema là contract; server là nguồn sự thật.** Client form giúp user nhập đúng nhanh hơn, nhưng dữ liệu cuối cùng phải được validate ở API/server.

## 2. 🧠 Key Mental Model

### 2.1. Form pipeline trong production

```text
User input
  ↓
Field state: touched, dirty, focused, disabled
  ↓
Client validation: required, format, cross-field rules
  ↓
Submit transform: trim, normalize, parse number/date
  ↓
API request
  ↓
Server validation: auth, permission, uniqueness, business rules
  ↓
Map server errors về field/form
  ↓
Success: reset, redirect, invalidate cache, optimistic update
```

### 2.2. Controlled vs uncontrolled

| Kiểu | Cách hoạt động | Ưu điểm | Nhược điểm | Hợp khi |
|---|---|---|---|---|
| Controlled | React state giữ `value` mỗi field | Dễ debug, sync realtime | Re-render nhiều nếu form lớn | Form nhỏ, custom logic realtime |
| Uncontrolled | DOM giữ value, React đọc qua ref/register | Ít re-render, performance tốt | Cần lib quản lý state/validation | CRUD form lớn, nhiều field |

```tsx
// Controlled: mỗi keystroke setState.
function ControlledEmail() {
  const [email, setEmail] = useState('');

  return (
    <input
      value={email}
      onChange={(event) => setEmail(event.target.value)}
    />
  );
}
```

```tsx
// React Hook Form: register field, DOM giữ value chính.
function UncontrolledEmail() {
  const { register, handleSubmit } = useForm<{ email: string }>();

  return (
    <form onSubmit={handleSubmit(console.log)}>
      <input {...register('email')} />
      <button type="submit">Submit</button>
    </form>
  );
}
```

### 2.3. Client validation vs server validation

| Validation | Mục tiêu | Ví dụ | Có thể tin tuyệt đối không? |
|---|---|---|---|
| Client | UX nhanh, giảm request lỗi | required, email format, min length | ❌ Không |
| Server | Security, business truth | permission, duplicate email, payment limit | ✅ Có |
| Shared schema | Giảm drift giữa client/server | Zod schema dùng chung | ✅ Nếu boundary rõ |

## 3. 📚 Main Concepts

### 3.1. React Hook Form vs Formik

| Tiêu chí | React Hook Form | Formik |
|---|---|---|
| Architecture | Uncontrolled-first, refs/subscription | Controlled form state |
| Re-render | Tối ưu field-level/subscription | Dễ re-render form-level |
| API chính | `useForm`, `register`, `Controller`, `FormProvider`, `useWatch` | `useFormik`, `Formik`, `Field`, `ErrorMessage` |
| Validation | Built-in rules + resolvers | Thường dùng Yup |
| TypeScript | Tốt, đặc biệt với Zod resolver | Dùng được nhưng ít ergonomic hơn |
| Large forms | Rất hợp | Cần tối ưu kỹ |
| Legacy codebase | Có thể cần migrate | Vẫn phổ biến |

**Kết luận thực tế:** Với app React mới, RHF + Zod thường là default tốt. Formik vẫn đáng hiểu vì nhiều dự án cũ dùng, nhưng nếu form lớn và render nhiều, RHF thường dễ tối ưu hơn.

### 3.2. `useForm` - trung tâm của React Hook Form

`useForm` quản lý registration, validation, submit, default values và form state.

```tsx
import { useForm } from 'react-hook-form';

type LoginFormValues = {
  email: string;
  password: string;
};

export function LoginForm() {
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
  } = useForm<LoginFormValues>({
    mode: 'onBlur',
    defaultValues: {
      email: '',
      password: '',
    },
  });

  async function onSubmit(values: LoginFormValues) {
    await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify(values),
    });
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} noValidate>
      <label htmlFor="email">Email</label>
      <input
        id="email"
        type="email"
        autoComplete="email"
        aria-invalid={Boolean(errors.email)}
        {...register('email', {
          required: 'Email là bắt buộc',
          pattern: {
            value: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
            message: 'Email không hợp lệ',
          },
        })}
      />
      {errors.email?.message && <p role="alert">{errors.email.message}</p>}

      <label htmlFor="password">Password</label>
      <input
        id="password"
        type="password"
        autoComplete="current-password"
        aria-invalid={Boolean(errors.password)}
        {...register('password', {
          required: 'Password là bắt buộc',
          minLength: { value: 8, message: 'Tối thiểu 8 ký tự' },
        })}
      />
      {errors.password?.message && <p role="alert">{errors.password.message}</p>}

      <button disabled={isSubmitting} type="submit">
        {isSubmitting ? 'Đang đăng nhập...' : 'Đăng nhập'}
      </button>
    </form>
  );
}
```

### 3.3. Validation modes

| Mode | Khi nào validate | Ưu điểm | Nhược điểm |
|---|---|---|---|
| `onSubmit` | Khi submit | Nhẹ nhất, ít làm phiền user | Lỗi hiện muộn |
| `onBlur` | Khi rời field | UX cân bằng, phổ biến | User phải blur mới thấy lỗi |
| `onChange` | Mỗi lần nhập | Realtime feedback | Nặng với form lớn/async rules |
| `onTouched` | Sau khi field touched | Tránh lỗi hiện quá sớm | Cần hiểu touched state |
| `all` | Blur + change | Feedback nhiều | Dễ noisy và tốn render |

**Khuyến nghị:** dùng `onBlur` hoặc `onSubmit` cho đa số form. Chỉ dùng `onChange` cho field cần feedback realtime như password strength hoặc slug preview.

### 3.4. `Controller` và `useController`

`register()` hợp với native inputs. Với custom controlled component như `Select`, `DatePicker`, `Combobox`, `RichTextEditor`, dùng `Controller` hoặc `useController`.

```tsx
import { Controller, useForm } from 'react-hook-form';
import { Select } from '@radix-ui/themes';

type FormValues = {
  role: 'admin' | 'member';
};

export function RoleForm() {
  const { control, handleSubmit } = useForm<FormValues>({
    defaultValues: { role: 'member' },
  });

  return (
    <form onSubmit={handleSubmit(console.log)}>
      <Controller
        control={control}
        name="role"
        render={({ field, fieldState }) => (
          <div>
            <Select.Root value={field.value} onValueChange={field.onChange}>
              <Select.Trigger aria-label="Role" />
              <Select.Content>
                <Select.Item value="member">Member</Select.Item>
                <Select.Item value="admin">Admin</Select.Item>
              </Select.Content>
            </Select.Root>
            {fieldState.error?.message && (
              <p role="alert">{fieldState.error.message}</p>
            )}
          </div>
        )}
      />
      <button type="submit">Save</button>
    </form>
  );
}
```

**Rule:** nếu component không expose native `ref`, `name`, `onChange`, `onBlur` theo kiểu input chuẩn, dùng `Controller`.

### 3.5. `FormProvider` và `useFormContext`

Khi form có nhiều section/component con, truyền `register`, `control`, `errors` qua props sẽ tạo prop drilling. `FormProvider` giúp chia sẻ form methods qua context.

```tsx
import { FormProvider, useForm, useFormContext } from 'react-hook-form';

type CheckoutFormValues = {
  customer: {
    email: string;
  };
  shipping: {
    address: string;
  };
};

function CustomerSection() {
  const {
    register,
    formState: { errors },
  } = useFormContext<CheckoutFormValues>();

  return (
    <section>
      <label htmlFor="email">Email</label>
      <input id="email" {...register('customer.email')} />
      {errors.customer?.email?.message && (
        <p role="alert">{errors.customer.email.message}</p>
      )}
    </section>
  );
}

export function CheckoutForm() {
  const methods = useForm<CheckoutFormValues>({
    defaultValues: {
      customer: { email: '' },
      shipping: { address: '' },
    },
  });

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(console.log)}>
        <CustomerSection />
        <button type="submit">Checkout</button>
      </form>
    </FormProvider>
  );
}
```

### 3.6. `watch` vs `useWatch`

`watch()` tiện nhưng dễ làm component cha re-render khi field thay đổi. `useWatch()` subscribe ở component con, giúp cô lập render tốt hơn.

```tsx
import { useWatch, useFormContext } from 'react-hook-form';

function ShippingPreview() {
  const { control } = useFormContext<CheckoutFormValues>();
  const address = useWatch({
    control,
    name: 'shipping.address',
  });

  return <p>Giao tới: {address || 'Chưa nhập địa chỉ'}</p>;
}
```

**Rule:** dùng `watch()` khi debug hoặc logic nhỏ trong component form. Dùng `useWatch()` khi field thay đổi thường xuyên hoặc form lớn.

### 3.7. Zod - TypeScript-first schema validation

Zod cho phép định nghĩa schema runtime và suy ra TypeScript type từ schema.

```ts
import { z } from 'zod';

export const RegisterSchema = z
  .object({
    email: z.string().email('Email không hợp lệ'),
    password: z.string().min(8, 'Tối thiểu 8 ký tự'),
    confirmPassword: z.string(),
    age: z.coerce.number().int().min(18, 'Phải từ 18 tuổi'),
  })
  .refine((data) => data.password === data.confirmPassword, {
    path: ['confirmPassword'],
    message: 'Password không khớp',
  });

export type RegisterFormValues = z.infer<typeof RegisterSchema>;
```

RHF integration:

```tsx
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';

const form = useForm<RegisterFormValues>({
  resolver: zodResolver(RegisterSchema),
  defaultValues: {
    email: '',
    password: '',
    confirmPassword: '',
    age: 18,
  },
});
```

**Khi dùng Zod:**

- TS project cần type inference tốt.
- Muốn shared schema giữa frontend/backend.
- Cần parse/transform dữ liệu từ API.
- Muốn validation explicit, composable.

### 3.8. Yup - runtime schema linh hoạt

Yup là schema builder cho runtime parsing/validation, phổ biến trong Formik và nhiều codebase cũ. Yup mạnh về chain API, transform, conditional validation.

```ts
import * as yup from 'yup';
import type { InferType } from 'yup';

export const ProfileSchema = yup.object({
  displayName: yup.string().required('Tên hiển thị là bắt buộc'),
  website: yup.string().url('URL không hợp lệ').nullable(),
  role: yup.string().oneOf(['admin', 'member']).required(),
  companyName: yup.string().when('role', {
    is: 'admin',
    then: (schema) => schema.required('Admin cần company name'),
    otherwise: (schema) => schema.optional(),
  }),
});

export type ProfileFormValues = InferType<typeof ProfileSchema>;
```

RHF integration:

```tsx
import { yupResolver } from '@hookform/resolvers/yup';
import { useForm } from 'react-hook-form';

const form = useForm<ProfileFormValues>({
  resolver: yupResolver(ProfileSchema),
});
```

**Khi dùng Yup:**

- Codebase legacy đã dùng Yup/Formik.
- Team quen chain API.
- Conditional validation nhiều và đang ổn.
- Dự án JS không cần type inference quá chặt.

### 3.9. Zod vs Yup

| Tiêu chí | Zod | Yup |
|---|---|---|
| Philosophy | TypeScript-first | Runtime schema builder |
| Type inference | Rất mạnh, `z.infer` | Có `InferType`, nhưng kém ergonomic hơn |
| Transform/coerce | Explicit, rõ ràng | Mạnh, lâu đời |
| Conditional validation | `refine`, `superRefine`, union | `when`, `test`, `lazy` |
| Shared schema FE/BE | Rất hợp | Có thể nhưng ít phổ biến hơn |
| Legacy ecosystem | Mới hơn Yup | Rất phổ biến trong app cũ |
| Default recommendation | TS app mới | Legacy/Formik-heavy app |

### 3.10. Dynamic fields với `useFieldArray`

`useFieldArray` dùng cho list field thêm/xóa/sắp xếp được: product variants, addresses, invoice lines.

```tsx
import { useFieldArray, useForm } from 'react-hook-form';

type ProductFormValues = {
  variants: Array<{
    name: string;
    price: number;
  }>;
};

export function ProductVariantsForm() {
  const { control, register, handleSubmit } = useForm<ProductFormValues>({
    defaultValues: {
      variants: [{ name: '', price: 0 }],
    },
  });

  const { fields, append, remove } = useFieldArray({
    control,
    name: 'variants',
  });

  return (
    <form onSubmit={handleSubmit(console.log)}>
      {fields.map((field, index) => (
        <div key={field.id}>
          <input {...register(`variants.${index}.name`)} placeholder="Variant" />
          <input
            type="number"
            {...register(`variants.${index}.price`, { valueAsNumber: true })}
          />
          <button type="button" onClick={() => remove(index)}>
            Remove
          </button>
        </div>
      ))}

      <button type="button" onClick={() => append({ name: '', price: 0 })}>
        Add variant
      </button>
      <button type="submit">Save</button>
    </form>
  );
}
```

**Pitfall:** dùng `field.id` làm React `key`, không dùng `index`, để tránh lỗi state khi reorder/remove.

### 3.11. Conditional fields

Conditional field cần xử lý cả UI và validation. Nếu field bị ẩn nhưng vẫn registered, data cũ có thể vẫn submit.

```tsx
type PaymentFormValues = {
  method: 'card' | 'bank_transfer';
  cardNumber?: string;
};

function CardFields() {
  const { register } = useFormContext<PaymentFormValues>();

  return (
    <label>
      Card number
      <input {...register('cardNumber')} inputMode="numeric" />
    </label>
  );
}

function PaymentFields() {
  const { control } = useFormContext<PaymentFormValues>();
  const method = useWatch({ control, name: 'method' });

  return method === 'card' ? <CardFields /> : null;
}
```

RHF có option `shouldUnregister`. Dùng khi muốn field unmount thì remove khỏi form values.

### 3.12. File upload

File input là case đặc biệt: `FileList` không serializable, user có thể cancel selection, preview cần cleanup object URL.

```tsx
import { z } from 'zod';

const MAX_FILE_SIZE = 5 * 1024 * 1024;

const UploadSchema = z.object({
  avatar: z
    .instanceof(FileList)
    .refine((files) => files.length === 1, 'Chọn một file')
    .refine((files) => files[0]?.size <= MAX_FILE_SIZE, 'File tối đa 5MB')
    .refine(
      (files) => ['image/png', 'image/jpeg'].includes(files[0]?.type),
      'Chỉ hỗ trợ PNG/JPEG'
    ),
});

type UploadFormValues = z.infer<typeof UploadSchema>;
```

```tsx
export function AvatarUploadForm() {
  const { register, handleSubmit, formState } = useForm<UploadFormValues>({
    resolver: zodResolver(UploadSchema),
  });

  async function onSubmit(values: UploadFormValues) {
    const formData = new FormData();
    formData.append('avatar', values.avatar[0]);

    await fetch('/api/avatar', {
      method: 'POST',
      body: formData,
    });
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input accept="image/png,image/jpeg" type="file" {...register('avatar')} />
      {formState.errors.avatar?.message && (
        <p role="alert">{formState.errors.avatar.message}</p>
      )}
      <button type="submit">Upload</button>
    </form>
  );
}
```

**Security note:** client file validation chỉ để UX. Server vẫn phải validate MIME, size, extension, virus scan nếu cần, quyền user và storage policy.

### 3.13. Async validation

Async validation thường dùng cho username/email uniqueness. Không nên gọi API mỗi keystroke không debounce.

```tsx
function UsernameField() {
  const {
    register,
    formState: { errors },
  } = useFormContext<{ username: string }>();

  return (
    <div>
      <input
        {...register('username', {
          validate: async (value) => {
            if (value.length < 3) return 'Tối thiểu 3 ký tự';

            const response = await fetch(`/api/users/exists?username=${value}`);
            const result: { exists: boolean } = await response.json();

            return result.exists ? 'Username đã tồn tại' : true;
          },
        })}
      />
      {errors.username?.message && (
        <p role="alert">{errors.username.message}</p>
      )}
    </div>
  );
}
```

**Production note:** async validation cần debounce, abort stale request và server vẫn validate lại khi submit.

### 3.14. Multi-step forms / wizard

Multi-step form có hai hướng:

- **Single form instance**: một `useForm`, nhiều step, giữ toàn bộ state. Hợp checkout/onboarding vừa phải.
- **Per-step form**: mỗi step validate riêng, lưu draft vào store/server. Hợp flow dài, có resume.

```tsx
const steps = ['account', 'profile', 'confirm'] as const;
type Step = (typeof steps)[number];

function OnboardingForm() {
  const [step, setStep] = useState<Step>('account');
  const methods = useForm<RegisterFormValues>({
    resolver: zodResolver(RegisterSchema),
    mode: 'onBlur',
  });

  async function goNext() {
    const fieldsByStep: Record<Step, Array<keyof RegisterFormValues>> = {
      account: ['email', 'password'],
      profile: ['age'],
      confirm: [],
    };

    const isValid = await methods.trigger(fieldsByStep[step]);
    if (!isValid) return;

    const currentIndex = steps.indexOf(step);
    setStep(steps[Math.min(currentIndex + 1, steps.length - 1)]);
  }

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(console.log)}>
        {step === 'account' && <AccountStep />}
        {step === 'profile' && <ProfileStep />}
        {step === 'confirm' && <ConfirmStep />}

        <button type="button" onClick={goNext}>
          Next
        </button>
      </form>
    </FormProvider>
  );
}
```

## 4. 💻 Practical TypeScript/JavaScript Examples

### 4.1. Production registration form với RHF + Zod

```tsx
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';
import { z } from 'zod';

const RegistrationSchema = z
  .object({
    email: z.string().email('Email không hợp lệ'),
    password: z.string().min(8, 'Password tối thiểu 8 ký tự'),
    confirmPassword: z.string(),
    termsAccepted: z.literal(true, {
      errorMap: () => ({ message: 'Bạn cần đồng ý điều khoản' }),
    }),
  })
  .refine((data) => data.password === data.confirmPassword, {
    path: ['confirmPassword'],
    message: 'Password không khớp',
  });

type RegistrationFormValues = z.infer<typeof RegistrationSchema>;

type ApiError = {
  fieldErrors?: Partial<Record<keyof RegistrationFormValues, string>>;
  message?: string;
};

export function RegistrationForm() {
  const {
    register,
    handleSubmit,
    setError,
    formState: { errors, isSubmitting },
  } = useForm<RegistrationFormValues>({
    resolver: zodResolver(RegistrationSchema),
    mode: 'onBlur',
    defaultValues: {
      email: '',
      password: '',
      confirmPassword: '',
    },
  });

  async function onSubmit(values: RegistrationFormValues) {
    const response = await fetch('/api/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    });

    if (!response.ok) {
      const error: ApiError = await response.json();

      Object.entries(error.fieldErrors ?? {}).forEach(([field, message]) => {
        setError(field as keyof RegistrationFormValues, { message });
      });

      if (error.message) {
        setError('root', { message: error.message });
      }

      return;
    }

    window.location.assign('/welcome');
  }

  return (
    <form onSubmit={handleSubmit(onSubmit)} noValidate>
      {errors.root?.message && <p role="alert">{errors.root.message}</p>}

      <label htmlFor="email">Email</label>
      <input id="email" {...register('email')} aria-invalid={Boolean(errors.email)} />
      {errors.email?.message && <p role="alert">{errors.email.message}</p>}

      <label htmlFor="password">Password</label>
      <input
        id="password"
        type="password"
        {...register('password')}
        aria-invalid={Boolean(errors.password)}
      />
      {errors.password?.message && <p role="alert">{errors.password.message}</p>}

      <label htmlFor="confirmPassword">Confirm password</label>
      <input
        id="confirmPassword"
        type="password"
        {...register('confirmPassword')}
        aria-invalid={Boolean(errors.confirmPassword)}
      />
      {errors.confirmPassword?.message && (
        <p role="alert">{errors.confirmPassword.message}</p>
      )}

      <label>
        <input type="checkbox" {...register('termsAccepted')} />
        Đồng ý điều khoản
      </label>
      {errors.termsAccepted?.message && (
        <p role="alert">{errors.termsAccepted.message}</p>
      )}

      <button disabled={isSubmitting} type="submit">
        {isSubmitting ? 'Đang tạo tài khoản...' : 'Tạo tài khoản'}
      </button>
    </form>
  );
}
```

### 4.2. Form section cô lập render bằng `useWatch`

```tsx
function PricePreview() {
  const { control } = useFormContext<ProductFormValues>();
  const price = useWatch({ control, name: 'price' });
  const discount = useWatch({ control, name: 'discount' });

  const finalPrice = Math.max(0, Number(price || 0) - Number(discount || 0));

  return <p>Giá sau giảm: {finalPrice.toLocaleString('vi-VN')}đ</p>;
}
```

### 4.3. React Query mutation + RHF

```tsx
import { useMutation, useQueryClient } from '@tanstack/react-query';

function EditProfileForm({ profile }: { profile: Profile }) {
  const queryClient = useQueryClient();
  const form = useForm<ProfileFormValues>({
    defaultValues: profile,
    resolver: zodResolver(ProfileSchema),
  });

  const mutation = useMutation({
    mutationFn: updateProfile,
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['profile'] });
      form.reset(form.getValues());
    },
  });

  return (
    <form onSubmit={form.handleSubmit((values) => mutation.mutate(values))}>
      <input {...form.register('displayName')} />
      <button disabled={mutation.isPending} type="submit">
        Save
      </button>
    </form>
  );
}
```

### 4.4. Testing form behavior

```tsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';

test('shows validation error for invalid email', async () => {
  render(<RegistrationForm />);

  await userEvent.type(screen.getByLabelText(/email/i), 'invalid-email');
  await userEvent.click(screen.getByRole('button', { name: /tạo tài khoản/i }));

  expect(await screen.findByRole('alert')).toHaveTextContent('Email không hợp lệ');
});
```

### 4.5. Mapping API errors vào form

```ts
type ServerValidationError = {
  errors: Array<{
    path: string;
    message: string;
  }>;
};

function applyServerErrors<T extends Record<string, unknown>>(
  error: ServerValidationError,
  setError: UseFormSetError<T>
) {
  for (const item of error.errors) {
    setError(item.path as Path<T>, {
      type: 'server',
      message: item.message,
    });
  }
}
```

## 5. 🏗️ Production Notes / React Implications

### 5.1. Performance

RHF tối ưu tốt, nhưng vẫn có thể bị chậm nếu dùng sai:

- Dùng `watch()` toàn form trong parent lớn.
- Render toàn bộ form mỗi khi một field đổi.
- Validate async trên `onChange` không debounce.
- Tạo schema/default values mới trong render liên tục.
- Dùng controlled component nặng cho tất cả field.
- Không virtualize dynamic list dài.

```tsx
// ✅ Schema stable ngoài component nếu không phụ thuộc props.
const SearchSchema = z.object({
  keyword: z.string().max(100),
});

function SearchForm() {
  const form = useForm<z.infer<typeof SearchSchema>>({
    resolver: zodResolver(SearchSchema),
  });

  return <form onSubmit={form.handleSubmit(console.log)}>...</form>;
}
```

### 5.2. Accessibility

Form accessible cần:

- `label` gắn với input qua `htmlFor`/`id`.
- Error message có `role="alert"` hoặc được link bằng `aria-describedby`.
- Input lỗi có `aria-invalid`.
- Submit button có loading text rõ.
- Focus chuyển tới field lỗi đầu tiên hoặc summary lỗi với form dài.
- Không chỉ dùng màu để báo lỗi.

### 5.3. Security

Client validation không bảo vệ API. Server phải validate lại:

- required/type/format
- auth và permission
- rate limit cho async validation
- file size/MIME/content scan
- business constraints
- tránh mass assignment: không tin toàn bộ object client gửi lên

### 5.4. SSR và hydration

Với Next.js/SSR:

- `defaultValues` server và client nên nhất quán.
- Tránh đọc `localStorage` trực tiếp để set default trong render server.
- Date/number formatting có thể lệch locale/timezone.
- File input chỉ client-side.
- Form component có event handler phải là Client Component trong App Router.

### 5.5. API boundary

Đừng để form schema trở thành toàn bộ domain model. Form thường là input DTO:

```ts
type RegisterInput = {
  email: string;
  password: string;
};

type User = {
  id: string;
  email: string;
  role: 'admin' | 'member';
  createdAt: string;
};
```

Form input, API payload và domain entity nên tách rõ để tránh submit nhầm field như `role`, `id`, `createdAt`.

### 5.6. Maintainability

Với form lớn, nên tổ chức:

```text
features/checkout/
  schemas/checkout.schema.ts
  components/CheckoutForm.tsx
  components/CustomerSection.tsx
  components/ShippingSection.tsx
  api/checkout.api.ts
  tests/CheckoutForm.test.tsx
```

Schema, API mapping và UI sections tách ra giúp test và review dễ hơn.

## 6. ⚠️ Common Pitfalls

### 6.1. Dùng `watch()` toàn form cho UI nhỏ

`watch()` toàn form ở parent làm parent re-render thường xuyên. Dùng `useWatch()` ở component con để subscribe đúng field.

### 6.2. Không dùng `Controller` cho custom component

Nếu custom `Select` không forward ref/onChange đúng, `register()` có thể không hoạt động như mong muốn. Dùng `Controller`.

### 6.3. Validate async trên mỗi keystroke

Gọi API uniqueness mỗi ký tự gây load server, race condition và UX giật. Debounce, abort stale request và validate lại khi submit.

### 6.4. Tin client validation là đủ

User có thể bypass JS, sửa request hoặc gọi API trực tiếp. Server validation là bắt buộc.

### 6.5. Không map server errors về field

Nếu API trả `email already exists` nhưng UI chỉ show toast chung, user không biết sửa field nào. Dùng `setError`.

### 6.6. Dùng `index` làm key trong `useFieldArray`

Khi remove/reorder, React có thể giữ nhầm state. Dùng `field.id`.

### 6.7. Hidden field vẫn submit data cũ

Conditional UI cần quyết định field ẩn có được unregister/reset không. Xem `shouldUnregister`, `resetField`, schema conditional.

### 6.8. Default values thay đổi nhưng form không reset

`defaultValues` chỉ dùng để init. Khi data async load xong, gọi `reset(newValues)`.

### 6.9. Schema quá gắn với UI

Một schema dùng cho cả create/edit/search/import có thể trở nên rối. Tách schema theo use case.

### 6.10. File upload preview không cleanup

Nếu dùng `URL.createObjectURL(file)`, cần `URL.revokeObjectURL(url)` khi file đổi/unmount.

## 7. ✅ Decision Guide / Checklist

### 7.1. Chọn stack nào?

| Tình huống | Khuyến nghị |
|---|---|
| React app mới dùng TypeScript | React Hook Form + Zod |
| Legacy app đang dùng Formik/Yup ổn | Giữ, migrate dần khi có lý do |
| Form rất nhỏ 1-2 field | `useState` hoặc native form cũng đủ |
| Form lớn nhiều field/dynamic sections | React Hook Form |
| Shared schema frontend/backend | Zod |
| Conditional validation legacy phức tạp | Yup hoặc Zod `superRefine`, tùy team |
| Server Actions/progressive enhancement | Cân nhắc native form + server validation + RHF nếu cần client UX |

### 7.2. Checklist form production

- [ ] Có `defaultValues` rõ ràng.
- [ ] Schema validation tách khỏi UI component.
- [ ] Server validation được map về field bằng `setError`.
- [ ] Error message accessible.
- [ ] Submit button disable/loading khi submit.
- [ ] Không validate async quá thường xuyên.
- [ ] Conditional fields được unregister/reset đúng.
- [ ] Dynamic fields dùng `field.id` làm key.
- [ ] File upload validate ở cả client và server.
- [ ] Tests cover success, client error, server error.
- [ ] Form reset sau save hoặc khi data mới load.
- [ ] Không submit field ngoài contract API.

### 7.3. Checklist performance

- [ ] Không `watch()` toàn form nếu không cần.
- [ ] Dùng `useWatch()` cho preview/subsection.
- [ ] Dùng `Controller` chỉ khi cần controlled/custom component.
- [ ] Schema/default values không bị tạo lại vô ích.
- [ ] Split form thành section nhỏ.
- [ ] Memoize component nặng nếu có evidence.
- [ ] Debounce async validation.
- [ ] Virtualize list field rất dài.

### 7.4. Checklist accessibility

- [ ] Mỗi input có label.
- [ ] Error liên kết với input.
- [ ] `aria-invalid` set đúng.
- [ ] Error summary cho form dài.
- [ ] Focus tới lỗi đầu tiên khi submit fail.
- [ ] Không chỉ dùng màu để báo lỗi.
- [ ] Keyboard submit hoạt động.
- [ ] File input có mô tả loại/kích thước file.

## 8. 🎤 Short Interview Answer

Theo em, với React form hiện đại thì React Hook Form cộng với Zod là lựa chọn rất tốt cho đa số dự án TypeScript. React Hook Form tối ưu performance vì không bắt React giữ state cho từng keystroke như controlled form truyền thống, còn Zod giúp schema vừa validate runtime vừa suy ra type cho TypeScript.

Điểm em quan tâm trong production là tách rõ các lớp: UI form chỉ quản lý trạng thái nhập liệu, schema xử lý format và cross-field validation, server vẫn validate lại permission và business rules. Khi API trả lỗi, em map lỗi về field bằng `setError` thay vì chỉ show toast chung. Với form lớn, em dùng `FormProvider`, `useWatch`, `Controller` cho custom components và tránh `watch()` toàn form.

Formik/Yup vẫn đáng hiểu vì nhiều codebase cũ dùng. Nhưng nếu làm mới, form nhiều field hoặc cần performance tốt, em thường chọn React Hook Form + Zod, kèm checklist accessibility, testing và server validation đầy đủ.

## 9. 🧾 Ghi nhớ nhanh

- **RHF**: uncontrolled-first, ít re-render, hợp form lớn.
- **Formik**: controlled-oriented, dễ hiểu, phổ biến trong legacy app.
- **Zod**: TypeScript-first, `z.infer`, hợp schema shared.
- **Yup**: runtime schema linh hoạt, mạnh trong legacy/Formik.
- **`register`**: dùng cho native input.
- **`Controller`**: dùng cho custom controlled component.
- **`FormProvider`**: tránh prop drilling.
- **`useWatch`**: subscribe field cụ thể, tối ưu render.
- **`useFieldArray`**: dynamic list fields, dùng `field.id` làm key.
- **Client validation là UX**, server validation mới là security boundary.
- **File upload phải validate server-side**.
- **Server errors nên map về field** bằng `setError`.

## 10. 📖 Giải thích các thuật ngữ trong topic

| Thuật ngữ | Giải thích ngắn |
|---|---|
| Controlled input | Input có `value` đến từ React state |
| Uncontrolled input | Input để DOM giữ value, React đọc qua ref |
| React Hook Form | Library quản lý form state/validation tối ưu re-render |
| `useForm` | Hook chính của RHF để tạo form instance |
| `register` | Đăng ký native input với RHF |
| `Controller` | Adapter cho custom controlled component |
| `FormProvider` | Provider chia sẻ form methods qua context |
| `useFormContext` | Hook đọc form methods từ `FormProvider` |
| `watch` | Theo dõi giá trị field, dễ làm parent re-render |
| `useWatch` | Subscribe field cụ thể ở component con |
| `useFieldArray` | Quản lý list field động |
| Resolver | Adapter nối RHF với Zod/Yup/Ajv/... |
| Zod | TypeScript-first schema validation library |
| Yup | Runtime schema builder cho parsing/validation |
| Schema | Mô tả shape và rule của dữ liệu |
| Cross-field validation | Validation phụ thuộc nhiều field, ví dụ confirm password |
| Async validation | Validation cần gọi API, ví dụ username đã tồn tại |
| Dirty | Field/form đã thay đổi so với default value |
| Touched | Field đã được focus/blur hoặc tương tác |
| `setError` | API set lỗi thủ công, thường dùng cho server errors |
| `reset` | Reset form về values mới hoặc default values |
| `trigger` | Kích hoạt validation thủ công |
| DTO | Data Transfer Object, shape dữ liệu gửi/nhận qua API |

## 11. 📚 Nguồn chính thức đã đối chiếu

- React Hook Form docs: <https://react-hook-form.com/docs/useform>
- React Hook Form Resolvers: <https://github.com/react-hook-form/resolvers>
- Zod docs: <https://zod.dev/>
- Yup docs: <https://github.com/jquense/yup>
