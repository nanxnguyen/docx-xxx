# 📝 Q64: Form Handling & Validation - React Hook Form, Zod, Yup

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (3-4 phút):**

**"Form handling: React Hook Form (uncontrolled, performance) vs Formik (controlled, simple). Validation: Zod (TypeScript-first, schema) vs Yup (runtime, flexible). Best practices: Controller cho custom components, FormProvider tránh prop drilling, validation mode onBlur."**

**🔑 Form Libraries Comparison:**

**1. React Hook Form (Recommended):**

- **Uncontrolled**: Dùng refs, ít re-renders → performance tốt
- **Bundle size**: ~9KB (nhỏ nhất)
- **API**: `useForm()`, `register()`, `Controller`, `FormProvider`
- **Validation**: Built-in + Zod/Yup integration
- **Best for**: Performance-critical forms, large forms

**2. Formik:**

- **Controlled**: Dùng state, nhiều re-renders → đơn giản hơn
- **Bundle size**: ~15KB
- **API**: `useFormik()`, `Field`, `Form`, `ErrorMessage`
- **Validation**: Yup integration
- **Best for**: Simple forms, rapid prototyping

**🔑 Validation Libraries:**

**1. Zod (TypeScript-first):**

- **Type-safe**: Schema → TypeScript types tự động
- **Runtime validation**: Validate data at runtime
- **API**: `z.object()`, `z.string()`, `z.number()`
- **Best for**: TypeScript projects, type safety

**2. Yup:**

- **Flexible**: Schema validation, transformations
- **API**: `yup.object()`, `yup.string()`, `yup.number()`
- **Best for**: JavaScript projects, complex validations

**🔑 Best Practices:**

**1. Performance:**

- **React Hook Form**: Dùng `Controller` cho custom components
- **FormProvider**: Tránh prop drilling, share form context
- **useWatch()**: Watch specific fields thay vì `watch()` toàn form
- **Validation mode**: `onBlur` thay vì `onChange` (nhẹ hơn)

**2. Validation:**

- **Schema validation**: Zod/Yup cho complex rules
- **Field-level validation**: Validate từng field riêng
- **Async validation**: Validate với API calls
- **Custom validators**: Tạo validators riêng cho business logic

**⚠️ Lỗi Thường Gặp:**

- `watch()` toàn form → re-render mỗi keystroke
- Không dùng `Controller` cho custom components → mất validation
- Validation mode `onChange` → quá nặng cho large forms
- Không tách form sections → toàn form re-render

**💡 Kiến Thức Senior:**

- **Form state management**: Controlled vs Uncontrolled trade-offs
- **Multi-step forms**: Wizard pattern với React Hook Form
- **Dynamic fields**: Add/remove fields dynamically
- **File uploads**: Handle file uploads với validation
- **Form performance**: Optimize re-renders với memo, Controller

> **Câu hỏi phỏng vấn Senior Frontend Developer** > **Độ khó:** ⭐⭐⭐⭐ (Advanced)
> **Thời gian trả lời:** 15-20 phút

---

## 📋 **Mục Lục**

1. [Form Libraries Comparison](#1-form-libraries-comparison)
2. [React Hook Form Deep Dive](#2-react-hook-form-deep-dive)
3. [Validation Libraries (Zod vs Yup)](#3-validation-libraries-zod-vs-yup)
4. [Form Patterns & Best Practices](#4-form-patterns--best-practices)
5. [Complex Form Patterns](#5-complex-form-patterns)
6. [Performance Optimization](#6-performance-optimization)
7. [File Uploads & Advanced Features](#7-file-uploads--advanced-features)
ss
---

## 1. Form Libraries Comparison

### **1.1. React Hook Form vs Formik**

```markdown
# ===================================================

# ⚖️ **REACT HOOK FORM VS FORMIK**

# ===================================================

| Aspect             | React Hook Form          | Formik                  |
| ------------------ | ------------------------ | ----------------------- |
| **Architecture**   | Uncontrolled (refs)      | Controlled (state)      |
| **Re-renders**     | Minimal (field-level)    | Many (form-level)       |
| **Bundle Size**    | ~9KB                     | ~15KB                   |
| **Performance**    | ⚡⚡⚡⚡⚡ Excellent     | ⚡⚡⚡ Good             |
| **Learning Curve** | Medium                   | Easy                    |
| **TypeScript**     | Excellent                | Good                    |
| **Validation**     | Built-in + Zod/Yup       | Yup integration         |
| **Best For**       | Large forms, performance | Simple forms, rapid dev |

# ✅ React Hook Form Advantages:

- Performance: Ít re-renders, field-level updates
- Bundle size: Nhỏ nhất trong các form libraries
- TypeScript: Type-safe với Zod integration
- API: Flexible, nhiều features

# ✅ Formik Advantages:

- Simplicity: API đơn giản, dễ học
- Ecosystem: Nhiều plugins, community lớn
- Controlled: Predictable state management
```

### **1.2. Controlled vs Uncontrolled Forms**

```typescript
// ===================================================
// 🔥 **CONTROLLED COMPONENTS** - React state quản lý
// ===================================================

import { useState } from 'react';

function ControlledForm() {
  // ✅ Tạo state cho mỗi field - React quản lý giá trị
  const [email, setEmail] = useState(''); // State cho email
  const [password, setPassword] = useState(''); // State cho password

  return (
    <form>
      <input
        type="email"
        value={email} // ✅ Giá trị từ React state
        onChange={(e) => setEmail(e.target.value)} // ✅ Mỗi keystroke → setState → re-render
      />
      <input
        type="password"
        value={password} // ✅ Giá trị từ React state
        onChange={(e) => setPassword(e.target.value)} // ✅ Mỗi keystroke → setState → re-render
      />
    </form>
  );
}

// ✅ Ưu điểm (Advantages):
// - Predictable (Dễ đoán): State luôn sync với UI → biết chính xác giá trị
// - Validation (Xác thực): Dễ implement validation vì có state
// - Real-time (Thời gian thực): Updates ngay lập tức khi user gõ

// ❌ Nhược điểm (Disadvantages):
// - Performance (Hiệu năng): Mỗi keystroke → setState → re-render → chậm với form lớn
// - Complexity (Độ phức tạp): Phải quản lý state cho mỗi field → code dài

// ===================================================
// 🎯 **UNCONTROLLED COMPONENTS** - DOM quản lý
// ===================================================

import { useRef } from 'react';
import { useForm } from 'react-hook-form';

function UncontrolledForm() {
  // ✅ useForm() hook - Không cần state cho mỗi field
  const { register, handleSubmit } = useForm();
  // register: Đăng ký field với form (dùng refs)
  // handleSubmit: Xử lý submit form

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* ✅ DOM tự quản lý giá trị - React không re-render mỗi keystroke */}
      <input {...register('email')} /> {/* register trả về ref, name, onChange, onBlur */}
      <input {...register('password')} />
    </form>
  );
}

// ✅ Ưu điểm (Advantages):
// - Performance (Hiệu năng): Ít re-renders → chỉ validate khi cần (onBlur/submit)
// - Simplicity (Đơn giản): Code ngắn gọn hơn, không cần state cho mỗi field
// - Efficiency (Hiệu quả): Chỉ update khi submit/validate → nhanh hơn

// ❌ Nhược điểm (Disadvantages):
// - Less predictable (Ít dễ đoán): State không sync real-time → khó debug
// - Validation (Xác thực): Phải validate manually hoặc dùng library như React Hook Form
```

---

## 2. React Hook Form Deep Dive

### **2.1. Basic React Hook Form**

```typescript
// ===================================================
// 📝 **BASIC REACT HOOK FORM** - Cơ bản
// ===================================================

import { useForm } from 'react-hook-form';

interface FormData {
  email: string;
  password: string;
  age: number;
}

function LoginForm() {
  // ✅ useForm() hook - Quản lý form state và validation
  const {
    register, // ✅ Đăng ký field với form (trả về ref, name, onChange, onBlur)
    handleSubmit, // ✅ Xử lý submit form (tự động validate trước khi submit)
    formState: { errors }, // ✅ Lỗi validation của form (errors.email, errors.password, ...)
    watch, // ✅ Theo dõi giá trị field (subscribe để re-render khi thay đổi)
  } = useForm<FormData>({
    mode: 'onBlur', // ✅ Validation mode: validate khi field mất focus (nhẹ hơn onChange)
    defaultValues: {
      // ✅ Giá trị mặc định cho form
      email: '',
      password: '',
      age: 0,
    },
  });

  // ✅ Hàm xử lý khi submit form (chỉ chạy khi validation pass)
  const onSubmit = (data: FormData) => {
    console.log(data); // ✅ Data đã được validate và type-safe
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* ✅ register('email', {...rules}) - Đăng ký field email với validation rules */}
      <input
        {...register('email', {
          required: 'Email is required', // ✅ Bắt buộc phải nhập
          pattern: {
            value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i, // ✅ Regex kiểm tra format email
            message: 'Invalid email address', // ✅ Thông báo lỗi nếu không đúng format
          },
        })}
      />
      {/* ✅ Hiển thị lỗi nếu có - errors.email?.message */}
      {errors.email && <span>{errors.email.message}</span>}

      <input
        type="password"
        {...register('password', {
          required: 'Password is required',
          minLength: {
            value: 8,
            message: 'Password must be at least 8 characters',
          },
        })}
      />
      {errors.password && <span>{errors.password.message}</span>}

      <input
        type="number"
        {...register('age', {
          required: 'Age is required',
          min: { value: 18, message: 'Must be at least 18' },
          max: { value: 120, message: 'Must be less than 120' },
        })}
      />
      {errors.age && <span>{errors.age.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
}
```

### **2.2. Controller for Custom Components**

```typescript
// ===================================================
// 🎛️ **CONTROLLER** - Cho custom components
// ===================================================

import { Controller, useForm } from 'react-hook-form';
import { Select, DatePicker, Switch } from '@mui/material';

function CustomComponentsForm() {
  // ✅ control: Form control object (cần cho Controller)
  const { control, handleSubmit } = useForm();

  return (
    <form>
      {/* ✅ Controller: Dùng cho custom components (Select, DatePicker, Switch, ...) */}
      {/* ✅ Không thể dùng register() cho custom components → phải dùng Controller */}
      <Controller
        name="country" // ✅ Tên field trong form
        control={control} // ✅ Form control object
        rules={{ required: 'Country is required' }} // ✅ Validation rules
        render={({ field, fieldState }) => (
          // ✅ field: { value, onChange, onBlur, name, ref } - Props cần cho custom component
          // ✅ fieldState: { error, isTouched, isDirty } - State của field
          <Select
            {...field} // ✅ Spread field props (value, onChange, onBlur) vào Select
            error={!!fieldState.error} // ✅ Hiển thị error state
            helperText={fieldState.error?.message} // ✅ Hiển thị message lỗi
          >
            <option value="us">United States</option>
            <option value="vn">Vietnam</option>
          </Select>
        )}
      />

      {/* ✅ Controller cho DatePicker */}
      <Controller
        name="birthDate"
        control={control}
        rules={{ required: 'Birth date is required' }}
        render={({ field }) => (
          <DatePicker
            value={field.value}
            onChange={field.onChange}
            onBlur={field.onBlur}
          />
        )}
      />

      {/* ✅ Controller cho Switch */}
      <Controller
        name="newsletter"
        control={control}
        render={({ field: { value, onChange } }) => (
          <Switch checked={value} onChange={onChange} />
        )}
      />
    </form>
  );
}
```

### **2.3. FormProvider & useFormContext**

```typescript
// ===================================================
// 🌐 **FORMPROVIDER** - Tránh prop drilling
// ===================================================

import { FormProvider, useForm, useFormContext } from 'react-hook-form';

interface FormData {
  firstName: string;
  lastName: string;
  email: string;
}

// ✅ Child component - Không cần nhận props từ parent
// ✅ useFormContext() lấy form methods từ FormProvider (tránh prop drilling)
function PersonalInfoSection() {
  // ✅ useFormContext(): Lấy form methods từ FormProvider context
  const { register, formState: { errors } } = useFormContext<FormData>();
  // register: Đăng ký field
  // errors: Lỗi validation

  return (
    <fieldset>
      <legend>Personal Information</legend>

      {/* ✅ Đăng ký field firstName - Không cần truyền props từ parent */}
      <input {...register('firstName')} />
      {errors.firstName && <span>{errors.firstName.message}</span>}

      {/* ✅ Đăng ký field lastName */}
      <input {...register('lastName')} />
      {errors.lastName && <span>{errors.lastName.message}</span>}
    </fieldset>
  );
}

function ContactInfoSection() {
  const { register, formState: { errors } } = useFormContext<FormData>();

  return (
    <fieldset>
      <legend>Contact Information</legend>

      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}
    </fieldset>
  );
}

// ✅ Parent component - Wrap với FormProvider để share form context
function RegistrationForm() {
  // ✅ Tạo form methods một lần duy nhất
  const methods = useForm<FormData>({
    defaultValues: {
      firstName: '',
      lastName: '',
      email: '',
    },
  });

  const onSubmit = (data: FormData) => {
    console.log(data);
  };

  return (
    {/* ✅ FormProvider: Wrap form để share methods cho child components */}
    {/* ✅ Tránh prop drilling - Không cần truyền register, errors qua props */}
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        {/* ✅ Child components tự lấy methods từ FormProvider context */}
        <PersonalInfoSection />
        <ContactInfoSection />
        <button type="submit">Submit</button>
      </form>
    </FormProvider>
  );
}
```

### **2.4. useWatch vs watch**

```typescript
// ===================================================
// 👀 **USEWATCH VS WATCH** - Watch field values
// ===================================================

import { useForm, useWatch } from 'react-hook-form';

function FormWithWatch() {
  const { register, watch, control } = useForm();

  // ❌ BAD: watch() toàn form → subscribe toàn bộ form
  // ❌ Mỗi khi BẤT KỲ field nào thay đổi → component re-render → performance kém
  const allValues = watch(); // Subscribe toàn bộ form

  // ✅ GOOD: useWatch() cho field cụ thể → chỉ subscribe field đó
  // ✅ Chỉ re-render khi field 'email' thay đổi → performance tốt hơn
  const email = useWatch({ control, name: 'email' });
  const age = useWatch({ control, name: 'age' });

  // ✅ Conditional field: Hiển thị field age chỉ khi email có chứa '@'
  const showAgeField = email?.includes('@');

  return (
    <form>
      <input {...register('email')} />

      {showAgeField && <input {...register('age')} />}
    </form>
  );
}
```

---

## 3. Validation Libraries (Zod vs Yup)

### **3.1. Zod - TypeScript-First Validation**

```typescript
// ===================================================
// 🛡️ **ZOD VALIDATION** - TypeScript-first
// ===================================================

import { z } from 'zod';
import { zodResolver } from '@hookform/resolvers/zod';
import { useForm } from 'react-hook-form';

// ✅ Define schema với Zod - Tự động generate TypeScript types
// ✅ Schema = Validation rules + TypeScript types (2 trong 1)
const formSchema = z
  .object({
    // ✅ Email: string, bắt buộc, phải là email hợp lệ
    email: z
      .string() // ✅ Kiểu string
      .min(1, 'Email is required') // ✅ Tối thiểu 1 ký tự (không được rỗng)
      .email('Invalid email address'), // ✅ Phải đúng format email

    // ✅ Password: string, tối thiểu 8 ký tự, có chữ hoa, chữ thường, số
    password: z
      .string()
      .min(8, 'Password must be at least 8 characters') // ✅ Tối thiểu 8 ký tự
      .regex(/[A-Z]/, 'Password must contain uppercase') // ✅ Phải có chữ hoa
      .regex(/[a-z]/, 'Password must contain lowercase') // ✅ Phải có chữ thường
      .regex(/[0-9]/, 'Password must contain number'), // ✅ Phải có số

    // ✅ Age: number, từ 18 đến 120
    age: z
      .number() // ✅ Kiểu number
      .min(18, 'Must be at least 18') // ✅ Tối thiểu 18
      .max(120, 'Must be less than 120'), // ✅ Tối đa 120

    // ✅ Website: string, optional (có thể không nhập), nếu nhập phải là URL hợp lệ
    website: z
      .string()
      .url('Invalid URL') // ✅ Phải là URL hợp lệ
      .optional() // ✅ Không bắt buộc
      .or(z.literal('')), // ✅ Hoặc cho phép chuỗi rỗng

    confirmPassword: z.string(), // ✅ String, validation ở refine()
  })
  .refine((data) => data.password === data.confirmPassword, {
    // ✅ refine(): Custom validation cho toàn bộ form
    // ✅ Kiểm tra password và confirmPassword có khớp không
    message: "Passwords don't match",
    path: ['confirmPassword'], // ✅ Error hiển thị ở field confirmPassword
  });

// ✅ TypeScript type tự động từ schema - Không cần define type thủ công
// ✅ z.infer<typeof formSchema> = { email: string, password: string, age: number, ... }
type FormData = z.infer<typeof formSchema>;

function ZodForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    resolver: zodResolver(formSchema), // ✅ Zod resolver: Kết nối Zod schema với React Hook Form
    // ✅ zodResolver tự động validate theo schema và set errors
    defaultValues: {
      email: '',
      password: '',
      age: 0,
      website: '',
      confirmPassword: '',
    },
  });

  const onSubmit = (data: FormData) => {
    // ✅ data đã được validate và type-safe (TypeScript biết chính xác kiểu)
    console.log(data); // ✅ Type-safe data: { email: string, password: string, age: number, ... }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}

      <input type="password" {...register('password')} />
      {errors.password && <span>{errors.password.message}</span>}

      <input type="number" {...register('age', { valueAsNumber: true })} />
      {errors.age && <span>{errors.age.message}</span>}

      <input {...register('website')} />
      {errors.website && <span>{errors.website.message}</span>}

      <input type="password" {...register('confirmPassword')} />
      {errors.confirmPassword && <span>{errors.confirmPassword.message}</span>}

      <button type="submit">Submit</button>
    </form>
  );
}
```

### **3.2. Yup - Flexible Validation**

```typescript
// ===================================================
// 🔄 **YUP VALIDATION** - Flexible schema
// ===================================================

import * as yup from 'yup';
import { yupResolver } from '@hookform/resolvers/yup';
import { useForm } from 'react-hook-form';

// ✅ Define schema
const formSchema = yup.object({
  email: yup
    .string()
    .required('Email is required')
    .email('Invalid email address'),

  password: yup
    .string()
    .required('Password is required')
    .min(8, 'Password must be at least 8 characters')
    .matches(/[A-Z]/, 'Password must contain uppercase')
    .matches(/[a-z]/, 'Password must contain lowercase')
    .matches(/[0-9]/, 'Password must contain number'),

  age: yup
    .number()
    .required('Age is required')
    .min(18, 'Must be at least 18')
    .max(120, 'Must be less than 120')
    .typeError('Age must be a number'),

  website: yup
    .string()
    .url('Invalid URL')
    .nullable()
    .transform((value) => value || null), // Transform empty string to null

  confirmPassword: yup
    .string()
    .required('Please confirm password')
    .oneOf([yup.ref('password')], "Passwords don't match"),
});

type FormData = yup.InferType<typeof formSchema>;

function YupForm() {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>({
    resolver: yupResolver(formSchema), // ✅ Yup resolver
    defaultValues: {
      email: '',
      password: '',
      age: 0,
      website: '',
      confirmPassword: '',
    },
  });

  const onSubmit = (data: FormData) => {
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>{/* Same as Zod form */}</form>
  );
}
```

### **3.3. Zod vs Yup Comparison**

```markdown
# ===================================================

# ⚖️ **ZOD VS YUP**

# ===================================================

| Aspect               | Zod                  | Yup                 |
| -------------------- | -------------------- | ------------------- |
| **TypeScript**       | ⭐⭐⭐⭐⭐ Excellent | ⭐⭐⭐ Good         |
| **Type Inference**   | ✅ Automatic         | ⚠️ Manual           |
| **Bundle Size**      | ~10KB                | ~13KB               |
| **Performance**      | ⚡⚡⚡⚡ Fast        | ⚡⚡⚡ Good         |
| **API**              | Modern, clean        | Flexible, verbose   |
| **Transformations**  | ✅ Built-in          | ✅ Advanced         |
| **Async Validation** | ✅ Yes               | ✅ Yes              |
| **Best For**         | TypeScript projects  | JavaScript projects |

# ✅ Zod Advantages:

- TypeScript-first: Type inference tự động
- Modern API: Clean, intuitive
- Performance: Nhanh hơn Yup
- Type safety: Compile-time + runtime

# ✅ Yup Advantages:

- Flexible: Nhiều transformations
- Mature: Ecosystem lớn, nhiều plugins
- JavaScript-friendly: Dễ dùng với JS
```

---

## 4. Form Patterns & Best Practices

### **4.1. Validation Modes**

```typescript
// ===================================================
// ⚙️ **VALIDATION MODES** - Khi nào validate
// ===================================================

import { useForm } from 'react-hook-form';

// ✅ Mode: 'onBlur' (Recommended) - Validate khi field mất focus
// ✅ User gõ → không validate → User click ra ngoài (blur) → validate
const form1 = useForm({
  mode: 'onBlur', // ✅ Nhẹ nhất, validate khi blur → performance tốt
  // ✅ UX: User thấy lỗi sau khi gõ xong → không làm phiền khi đang gõ
});

// ✅ Mode: 'onChange' - Validate mỗi keystroke (nặng)
// ✅ User gõ mỗi ký tự → validate ngay → có thể lag với form lớn
const form2 = useForm({
  mode: 'onChange', // ⚠️ Nặng, validate mỗi keystroke → performance kém
  // ✅ UX: User thấy lỗi ngay khi gõ → feedback nhanh nhưng nặng
});

// ✅ Mode: 'onSubmit' - Validate chỉ khi submit (nhẹ nhất)
// ✅ User gõ → không validate → User click Submit → validate tất cả
const form3 = useForm({
  mode: 'onSubmit', // ✅ Nhẹ nhất, validate khi submit → performance tốt nhất
  // ✅ UX: User chỉ thấy lỗi khi submit → có thể gây khó chịu
});

// ✅ Mode: 'onTouched' - Validate sau khi field được touch (chạm vào)
// ✅ User click vào field → chưa validate → User click ra ngoài → validate
const form4 = useForm({
  mode: 'onTouched', // ✅ Balance giữa UX và performance
  reValidateMode: 'onChange', // ✅ Sau lần validate đầu, re-validate mỗi khi thay đổi
  // ✅ UX: Lần đầu validate khi blur, sau đó validate real-time → tốt nhất
});

// 💡 Best Practice:
// - Large forms: 'onBlur' hoặc 'onSubmit'
// - Simple forms: 'onChange' (nếu cần real-time feedback)
// - Performance-critical: 'onSubmit'
```

### **4.2. Field-Level Re-render Optimization**

```typescript
// ===================================================
// ⚡ **FIELD-LEVEL RE-RENDER** - Tối ưu performance
// ===================================================

import { memo } from 'react';
import { Controller, useFormContext } from 'react-hook-form';

// ✅ GOOD: Tách field component với memo
const EmailField = memo(() => {
  const { control } = useFormContext();

  return (
    <Controller
      name="email"
      control={control}
      rules={{ required: 'Email is required' }}
      render={({ field, fieldState }) => (
        <div>
          <input {...field} />
          {fieldState.error && <span>{fieldState.error.message}</span>}
        </div>
      )}
    />
  );
});

// ❌ BAD: Tất cả fields trong 1 component
function BadForm() {
  const { register } = useForm();

  return (
    <form>
      <input {...register('email')} />{' '}
      {/* Re-render khi bất kỳ field nào thay đổi */}
      <input {...register('password')} />
      <input {...register('age')} />
    </form>
  );
}

// ✅ GOOD: Tách thành sections với memo
const PersonalInfoSection = memo(() => {
  const { register } = useFormContext();

  return (
    <fieldset>
      <input {...register('firstName')} />
      <input {...register('lastName')} />
    </fieldset>
  );
});
```

### **4.3. Batch Updates**

```typescript
// ===================================================
// 📦 **BATCH UPDATES** - Giảm re-renders
// ===================================================

import { useForm } from 'react-hook-form';

function FormWithBatchUpdates() {
  const { setValue, trigger } = useForm();

  // ❌ BAD: Mỗi setValue trigger re-render → 3 lần re-render không cần thiết
  const fillDemoDataBad = () => {
    setValue('firstName', 'John'); // Re-render 1 (không cần thiết)
    setValue('lastName', 'Doe'); // Re-render 2 (không cần thiết)
    setValue('email', 'john@example.com'); // Re-render 3 (không cần thiết)
    // Total: 3 re-renders → Performance kém
  };

  // ✅ GOOD: Batch updates với shouldValidate: false → chỉ 1 lần re-render
  const fillDemoDataGood = () => {
    // ✅ shouldValidate: false → Không validate ngay, không trigger re-render
    setValue('firstName', 'John', { shouldValidate: false });
    setValue('lastName', 'Doe', { shouldValidate: false });
    setValue('email', 'john@example.com', { shouldValidate: false });

    // ✅ Trigger validation 1 lần duy nhất sau khi set tất cả values
    trigger(); // Re-render 1 lần → Performance tốt hơn
    // Total: 1 re-render → Tối ưu performance
  };

  return (
    <form>
      <button type="button" onClick={fillDemoDataGood}>
        Fill Demo Data
      </button>
    </form>
  );
}
```

---

## 5. Complex Form Patterns

### **5.1. Multi-Step Forms (Wizard)**

```typescript
// ===================================================
// 🧙 **MULTI-STEP FORM** - Wizard pattern
// ===================================================

import { useState } from 'react';
import { useForm, FormProvider } from 'react-hook-form';

interface FormData {
  // Step 1: Personal Info
  firstName: string;
  lastName: string;
  email: string;

  // Step 2: Address
  address: string;
  city: string;
  zipCode: string;

  // Step 3: Preferences
  newsletter: boolean;
  terms: boolean;
}

function MultiStepForm() {
  const [step, setStep] = useState(1);
  const methods = useForm<FormData>({
    mode: 'onBlur',
    defaultValues: {
      firstName: '',
      lastName: '',
      email: '',
      address: '',
      city: '',
      zipCode: '',
      newsletter: false,
      terms: false,
    },
  });

  const onSubmit = (data: FormData) => {
    console.log('Final data:', data);
  };

  const nextStep = async () => {
    // ✅ Validate current step trước khi chuyển step tiếp theo
    const fieldsToValidate = getFieldsForStep(step); // ✅ Lấy danh sách fields cần validate ở step hiện tại
    const isValid = await methods.trigger(fieldsToValidate); // ✅ Trigger validation cho các fields đó

    if (isValid) {
      // ✅ Chỉ chuyển step nếu validation pass
      setStep(step + 1);
    }
    // ✅ Nếu validation fail → hiển thị lỗi, không chuyển step
  };

  const prevStep = () => {
    setStep(step - 1);
  };

  const getFieldsForStep = (currentStep: number): (keyof FormData)[] => {
    switch (currentStep) {
      case 1:
        return ['firstName', 'lastName', 'email'];
      case 2:
        return ['address', 'city', 'zipCode'];
      case 3:
        return ['newsletter', 'terms'];
      default:
        return [];
    }
  };

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        {step === 1 && <PersonalInfoStep />}
        {step === 2 && <AddressStep />}
        {step === 3 && <PreferencesStep />}

        <div className="form-actions">
          {step > 1 && (
            <button type="button" onClick={prevStep}>
              Previous
            </button>
          )}
          {step < 3 ? (
            <button type="button" onClick={nextStep}>
              Next
            </button>
          ) : (
            <button type="submit">Submit</button>
          )}
        </div>
      </form>
    </FormProvider>
  );
}
```

### **5.2. Dynamic Fields (Add/Remove)**

```typescript
// ===================================================
// 🔄 **DYNAMIC FIELDS** - Add/remove fields
// ===================================================

import { useFieldArray, useForm } from 'react-hook-form';

interface FormData {
  users: Array<{
    name: string;
    email: string;
  }>;
}

function DynamicFieldsForm() {
  const { control, register } = useForm<FormData>({
    defaultValues: {
      users: [{ name: '', email: '' }],
    },
  });

  // ✅ useFieldArray: Quản lý array fields (add/remove fields động)
  const { fields, append, remove } = useFieldArray({
    control, // ✅ Form control object
    name: 'users', // ✅ Tên field array trong form (users: Array<{name, email}>)
  });
  // ✅ fields: Danh sách fields hiện tại (có id để làm key)
  // ✅ append: Thêm field mới vào cuối array
  // ✅ remove: Xóa field tại index

  return (
    <form>
      {/* ✅ Map qua fields array - field.id làm key (React requirement) */}
      {fields.map((field, index) => (
        <div key={field.id} className="user-row">
          {/* ✅ Register field với path: users.0.name, users.1.name, ... */}
          <input
            {...register(`users.${index}.name`, {
              required: 'Name is required',
            })}
            placeholder="Name"
          />

          {/* ✅ Register field với path: users.0.email, users.1.email, ... */}
          <input
            {...register(`users.${index}.email`, {
              required: 'Email is required',
              pattern: {
                value: /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}$/i,
                message: 'Invalid email',
              },
            })}
            placeholder="Email"
          />

          {/* ✅ Button xóa field tại index */}
          <button
            type="button"
            onClick={() => remove(index)} // ✅ Xóa field tại index
            disabled={fields.length === 1} // ✅ Không cho xóa field cuối (phải có ít nhất 1 field)
          >
            Remove
          </button>
        </div>
      ))}

      {/* ✅ Button thêm field mới vào cuối array */}
      <button
        type="button"
        onClick={() => append({ name: '', email: '' })} // ✅ Thêm object mới {name: '', email: ''} vào cuối array
      >
        Add User
      </button>
    </form>
  );
}
```

### **5.3. Conditional Fields**

```typescript
// ===================================================
// 🔀 **CONDITIONAL FIELDS** - Fields phụ thuộc
// ===================================================

import { useWatch, useForm } from 'react-hook-form';

interface FormData {
  accountType: 'personal' | 'business';
  companyName?: string;
  taxId?: string;
  personalId?: string;
}

function ConditionalFieldsForm() {
  const { register, control } = useForm<FormData>({
    defaultValues: {
      accountType: 'personal',
    },
  });

  // ✅ Watch accountType để hiển thị fields tương ứng
  // ✅ Khi accountType thay đổi → component re-render → hiển thị fields phù hợp
  const accountType = useWatch({ control, name: 'accountType' });

  return (
    <form>
      <select {...register('accountType')}>
        <option value="personal">Personal</option>
        <option value="business">Business</option>
      </select>

      {/* ✅ Conditional rendering: Chỉ hiển thị khi accountType = 'business' */}
      {accountType === 'business' && (
        <>
          {/* ✅ Validation: Chỉ required khi accountType = 'business' */}
          <input
            {...register('companyName', {
              required:
                accountType === 'business' ? 'Company name is required' : false,
              // ✅ Nếu accountType = 'business' → required, ngược lại → không required
            })}
            placeholder="Company Name"
          />

          <input
            {...register('taxId', {
              required:
                accountType === 'business' ? 'Tax ID is required' : false,
            })}
            placeholder="Tax ID"
          />
        </>
      )}

      {/* ✅ Conditional rendering: Chỉ hiển thị khi accountType = 'personal' */}
      {accountType === 'personal' && (
        <input
          {...register('personalId', {
            required:
              accountType === 'personal' ? 'Personal ID is required' : false,
            // ✅ Nếu accountType = 'personal' → required, ngược lại → không required
          })}
          placeholder="Personal ID"
        />
      )}
    </form>
  );
}
```

---

## 6. Performance Optimization

### **6.1. Optimized Form Structure**

```typescript
// ===================================================
// ⚡ **OPTIMIZED FORM** - Best practices
// ===================================================

import { memo, useMemo } from 'react';
import {
  FormProvider,
  useForm,
  useFormContext,
  Controller,
} from 'react-hook-form';

interface FormData {
  firstName: string;
  lastName: string;
  email: string;
}

// ✅ Pattern 1: Memoized field component
const EmailField = memo(() => {
  const { control } = useFormContext<FormData>();

  return (
    <Controller
      name="email"
      control={control}
      rules={{ required: 'Email is required' }}
      render={({ field, fieldState }) => (
        <div>
          <input {...field} />
          {fieldState.error && <span>{fieldState.error.message}</span>}
        </div>
      )}
    />
  );
});

// ✅ Pattern 2: Section component với memo
const PersonalInfoSection = memo(() => {
  const {
    register,
    formState: { errors },
  } = useFormContext<FormData>();

  return (
    <fieldset>
      <input {...register('firstName')} />
      {errors.firstName && <span>{errors.firstName.message}</span>}

      <input {...register('lastName')} />
      {errors.lastName && <span>{errors.lastName.message}</span>}
    </fieldset>
  );
});

// ✅ Pattern 3: Main form với FormProvider
function OptimizedForm() {
  // ✅ useForm() stable - chỉ tạo 1 lần
  const methods = useForm<FormData>({
    mode: 'onBlur', // ✅ Validate on blur (nhẹ hơn onChange)
    reValidateMode: 'onChange', // Re-validate on change sau lần đầu
    defaultValues: {
      firstName: '',
      lastName: '',
      email: '',
    },
  });

  // ✅ useMemo cho static data
  const formSections = useMemo(
    () => [
      { id: 1, label: 'Personal Info', component: PersonalInfoSection },
      { id: 2, label: 'Contact', component: EmailField },
    ],
    []
  );

  const onSubmit = (data: FormData) => {
    console.log(data);
  };

  return (
    <FormProvider {...methods}>
      <form onSubmit={methods.handleSubmit(onSubmit)}>
        <PersonalInfoSection />
        <EmailField />
        <button type="submit">Submit</button>
      </form>
    </FormProvider>
  );
}
```

### **6.2. Common Performance Pitfalls**

```typescript
// ===================================================
// ❌ **COMMON PITFALLS** - Lỗi thường gặp
// ===================================================

// ❌ PITFALL 1: watch() toàn form
function BadForm1() {
  const { register, watch } = useForm();
  const allValues = watch(); // ❌ Subscribe toàn bộ form → re-render mỗi keystroke

  return <form>{/* ... */}</form>;
}

// ✅ FIX: useWatch() cho field cụ thể
function GoodForm1() {
  const { register, control } = useForm();
  const email = useWatch({ control, name: 'email' }); // ✅ Chỉ subscribe field email

  return <form>{/* ... */}</form>;
}

// ❌ PITFALL 2: Validation mode onChange
function BadForm2() {
  const form = useForm({ mode: 'onChange' }); // ❌ Validate mỗi keystroke → nặng

  return <form>{/* ... */}</form>;
}

// ✅ FIX: Validation mode onBlur
function GoodForm2() {
  const form = useForm({ mode: 'onBlur' }); // ✅ Validate khi blur → nhẹ hơn

  return <form>{/* ... */}</form>;
}

// ❌ PITFALL 3: Không dùng Controller cho custom components
function BadForm3() {
  const { register } = useForm();

  return (
    <form>
      <CustomSelect {...register('country')} /> {/* ❌ Mất validation */}
    </form>
  );
}

// ✅ FIX: Dùng Controller
function GoodForm3() {
  const { control } = useForm();

  return (
    <form>
      <Controller
        name="country"
        control={control}
        rules={{ required: 'Country is required' }}
        render={({ field }) => <CustomSelect {...field} />}
      />
    </form>
  );
}

// ❌ PITFALL 4: Tất cả fields trong 1 component
function BadForm4() {
  const { register } = useForm();

  return (
    <form>
      <input {...register('field1')} />
      <input {...register('field2')} />
      <input {...register('field3')} />
      {/* ❌ Toàn form re-render khi bất kỳ field nào thay đổi */}
    </form>
  );
}

// ✅ FIX: Tách thành components với memo
function GoodForm4() {
  return (
    <FormProvider {...useForm()}>
      <form>
        <Field1Section /> {/* ✅ Chỉ section này re-render */}
        <Field2Section />
        <Field3Section />
      </form>
    </FormProvider>
  );
}
```

---

## 7. File Uploads & Advanced Features

### **7.1. File Upload with Validation**

```typescript
// ===================================================
// 📎 **FILE UPLOAD** - Upload files với validation
// ===================================================

import { useForm, Controller } from 'react-hook-form';

interface FormData {
  avatar: FileList;
  documents: FileList;
}

function FileUploadForm() {
  const {
    control,
    handleSubmit,
    formState: { errors },
  } = useForm<FormData>();

  const onSubmit = async (data: FormData) => {
    // ✅ Upload files: Tạo FormData object để gửi files lên server
    const formData = new FormData();
    formData.append('avatar', data.avatar[0]); // ✅ Append file đầu tiên (single file)

    // ✅ Append multiple files
    Array.from(data.documents).forEach((file) => {
      formData.append('documents', file); // ✅ Append từng file vào FormData
    });

    // ✅ Gửi FormData lên server
    await fetch('/api/upload', {
      method: 'POST',
      body: formData, // ✅ FormData tự động set Content-Type: multipart/form-data
    });
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      {/* ✅ Single file upload */}
      <Controller
        name="avatar"
        control={control}
        rules={{
          required: 'Avatar is required', // ✅ Bắt buộc phải chọn file
          validate: (files) => {
            // ✅ Custom validator: Kiểm tra file type và size
            if (files && files[0]) {
              const file = files[0];
              // ✅ Validate file type: Phải là image (image/jpeg, image/png, ...)
              if (!file.type.startsWith('image/')) {
                return 'Avatar must be an image'; // ✅ Return error message nếu không phải image
              }
              // ✅ Validate file size: Tối đa 5MB (5 * 1024 * 1024 bytes)
              if (file.size > 5 * 1024 * 1024) {
                return 'Avatar must be less than 5MB'; // ✅ Return error message nếu quá lớn
              }
            }
            return true; // ✅ Return true nếu validation pass
          },
        }}
        render={({ field: { onChange, value, ...field } }) => (
          // ✅ field: { onChange, value, ...field } - Props từ Controller
          // ✅ onChange: Hàm để update value khi user chọn file
          // ✅ value: FileList object (danh sách files đã chọn)
          <div>
            <input
              {...field} // ✅ Spread field props (name, ref, ...)
              type="file"
              accept="image/*" // ✅ Chỉ cho phép chọn file image
              onChange={(e) => onChange(e.target.files)} // ✅ Update value với FileList mới
            />
            {/* ✅ Hiển thị thông tin file đã chọn */}
            {value && value[0] && (
              <div>
                <p>Selected: {value[0].name}</p> {/* ✅ Tên file */}
                <p>Size: {(value[0].size / 1024 / 1024).toFixed(2)} MB</p> {/* ✅ Kích thước file (MB) */}
              </div>
            )}
          </div>
        )}
      />
      {errors.avatar && <span>{errors.avatar.message}</span>}

      {/* ✅ Multiple files upload */}
      <Controller
        name="documents"
        control={control}
        rules={{
          required: 'At least one document is required',
          validate: (files) => {
            // ✅ Custom validator cho multiple files
            if (files && files.length > 0) {
              // ✅ Validate số lượng files: Tối đa 5 files
              if (files.length > 5) {
                return 'Maximum 5 files allowed'; // ✅ Error nếu quá 5 files
              }
              // ✅ Validate từng file: Kiểm tra size của mỗi file
              Array.from(files).forEach((file) => {
                if (file.size > 10 * 1024 * 1024) {
                  return 'Each file must be less than 10MB'; // ✅ Error nếu file > 10MB
                }
              });
            }
            return true; // ✅ Return true nếu validation pass
          },
        }}
        render={({ field: { onChange, value, ...field } }) => (
          <div>
            <input
              {...field}
              type="file"
              multiple
              onChange={(e) => onChange(e.target.files)}
            />
            {/* ✅ Hiển thị danh sách files đã chọn */}
            {value && value.length > 0 && (
              <ul>
                {Array.from(value).map((file, index) => (
                  // ✅ Map qua từng file và hiển thị tên + size
                  <li key={index}>
                    {file.name} ({(file.size / 1024).toFixed(2)} KB){' '}
                    {/* ✅ Tên file + size (KB) */}
                  </li>
                ))}
              </ul>
            )}
          </div>
        )}
      />
      {errors.documents && <span>{errors.documents.message}</span>}

      <button type="submit">Upload</button>
    </form>
  );
}
```

### **7.2. Async Validation**

```typescript
// ===================================================
// ⏳ **ASYNC VALIDATION** - Validate với API
// ===================================================

import { useForm } from 'react-hook-form';

function FormWithAsyncValidation() {
  const {
    register,
    formState: { errors, isSubmitting },
  } = useForm({
    mode: 'onBlur',
  });

  // ✅ Async validator - Check email exists trên server
  // ✅ Return: true = valid, string = error message
  const checkEmailExists = async (email: string): Promise<boolean | string> => {
    if (!email) return true; // ✅ Skip nếu empty (đã có required validation)

    try {
      // ✅ Gọi API để check email đã tồn tại chưa
      const response = await fetch(`/api/check-email?email=${email}`);
      const data = await response.json();

      if (data.exists) {
        return 'Email already exists'; // ✅ Return error message nếu email đã tồn tại
      }
      return true; // ✅ Return true nếu email chưa tồn tại (valid)
    } catch (error) {
      return 'Error checking email'; // ✅ Return error message nếu API call fail
    }
  };

  // ✅ Async validator - Check username availability với debounce
  const checkUsername = async (username: string): Promise<boolean | string> => {
    if (!username) return true;

    // ✅ Debounce validation: Đợi 500ms trước khi gọi API
    // ✅ Tránh gọi API quá nhiều khi user đang gõ
    await new Promise((resolve) => setTimeout(resolve, 500));

    // ✅ Gọi API để check username có available không
    const response = await fetch(`/api/check-username?username=${username}`);
    const data = await response.json();

    // ✅ Return true nếu available, error message nếu không available
    return data.available || 'Username is already taken';
  };

  return (
    <form>
      <input
        {...register('email', {
          required: 'Email is required',
          validate: checkEmailExists, // ✅ Async validation: Gọi hàm async để validate
          // ✅ validate có thể là function hoặc object với nhiều validators
        })}
      />
      {errors.email && <span>{errors.email.message}</span>}

      <input
        {...register('username', {
          required: 'Username is required',
          minLength: { value: 3, message: 'Min 3 characters' },
          validate: checkUsername, // ✅ Async validation
        })}
      />
      {errors.username && <span>{errors.username.message}</span>}

      <button type="submit" disabled={isSubmitting}>
        {isSubmitting ? 'Submitting...' : 'Submit'}
      </button>
    </form>
  );
}
```

### **7.3. Form State Management**

```typescript
// ===================================================
// 🔄 **FORM STATE MANAGEMENT** - Quản lý state
// ===================================================

import { useForm, useWatch } from 'react-hook-form';

function FormWithStateManagement() {
  const {
    register,
    handleSubmit,
    watch,
    formState: {
      errors, // ✅ Object chứa tất cả lỗi validation (errors.email, errors.password, ...)
      isDirty, // ✅ Form đã thay đổi so với defaultValues (true/false)
      isValid, // ✅ Form hợp lệ (tất cả fields pass validation) (true/false)
      isSubmitting, // ✅ Đang submit form (true khi đang xử lý submit) (true/false)
      isSubmitted, // ✅ Đã submit form ít nhất 1 lần (true/false)
      touchedFields, // ✅ Object chứa fields đã được touch (touchedFields.email = true, ...)
      dirtyFields, // ✅ Object chứa fields đã thay đổi (dirtyFields.email = true, ...)
    },
    reset, // ✅ Reset form về defaultValues hoặc values mới
    setValue, // ✅ Set value cho field programmatically (không cần user input)
    getValues, // ✅ Get current values của form (không trigger re-render)
  } = useForm({
    mode: 'onBlur',
  });

  // ✅ Watch specific field: Subscribe để re-render khi field thay đổi
  const email = useWatch({ name: 'email' });

  // ✅ Reset form: Reset về defaultValues hoặc values mới
  const loadSavedData = () => {
    reset({
      email: 'saved@example.com',
      name: 'Saved Name',
    });
    // ✅ Reset form về values mới → form state reset (isDirty = false, errors = {})
  };

  // ✅ Set value programmatically: Set giá trị cho field (không cần user input)
  const fillDemoData = () => {
    setValue('email', 'demo@example.com', { shouldValidate: true }); // ✅ Set value + validate
    setValue('name', 'Demo User', { shouldValidate: true }); // ✅ Set value + validate
    // ✅ shouldValidate: true → trigger validation sau khi set value
  };

  // ✅ Get all values: Lấy tất cả giá trị hiện tại của form (không trigger re-render)
  const logCurrentValues = () => {
    const values = getValues(); // ✅ Lấy tất cả values: { email: '...', name: '...', ... }
    console.log('Current form values:', values);
    // ✅ getValues() không trigger re-render → dùng khi cần check values mà không muốn re-render
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('email')} />
      <input {...register('name')} />

      <div className="form-actions">
        <button type="button" onClick={loadSavedData}>
          Load Saved
        </button>
        <button type="button" onClick={fillDemoData}>
          Fill Demo
        </button>
        <button type="button" onClick={logCurrentValues}>
          Log Values
        </button>
        <button type="submit" disabled={!isValid || isSubmitting}>
          {isSubmitting ? 'Submitting...' : 'Submit'}
        </button>
      </div>

      {/* ✅ Hiển thị form state để debug */}
      <div className="form-state">
        <p>Dirty: {isDirty ? 'Yes' : 'No'}</p>{' '}
        {/* ✅ Form đã thay đổi so với defaultValues */}
        <p>Valid: {isValid ? 'Yes' : 'No'}</p> {/* ✅ Form hợp lệ (tất cả fields pass validation) */}
        <p>Submitted: {isSubmitted ? 'Yes' : 'No'}</p>{' '}
        {/* ✅ Đã submit form ít nhất 1 lần */}
        <p>Touched fields: {Object.keys(touchedFields).join(', ')}</p> {/* ✅ Danh sách fields đã được touch */}
        <p>Dirty fields: {Object.keys(dirtyFields).join(', ')}</p>{' '}
        {/* ✅ Danh sách fields đã thay đổi */}
      </div>
    </form>
  );
}
```

---

## **🎯 Best Practices Summary**

### **✅ DO:**

1. **Use React Hook Form**: Performance tốt nhất, ít re-renders
2. **Controller for custom components**: Đảm bảo validation hoạt động
3. **FormProvider**: Tránh prop drilling, share form context
4. **useWatch()**: Watch specific fields thay vì `watch()` toàn form
5. **Validation mode onBlur**: Nhẹ hơn onChange
6. **Zod for TypeScript**: Type-safe validation
7. **Memo components**: Tách form sections với memo
8. **Batch updates**: Dùng `shouldValidate: false` khi set nhiều values

### **❌ DON'T:**

1. **watch() toàn form**: Subscribe toàn bộ form → nhiều re-renders
2. **Validation mode onChange**: Quá nặng cho large forms
3. **Không dùng Controller**: Custom components mất validation
4. **Tất cả fields trong 1 component**: Toàn form re-render
5. **Multiple setValue() không batch**: Nhiều re-renders không cần thiết

---

## **💡 Real-World Scenarios**

### **Scenario 1: Registration Form với Multi-step**

```typescript
// Multi-step registration với validation từng step
// Step 1: Personal Info → Step 2: Address → Step 3: Preferences
// Validate từng step trước khi chuyển step tiếp theo
```

### **Scenario 2: Dynamic Product Form**

```typescript
// Form với dynamic fields (add/remove variants)
// useFieldArray để quản lý array fields
// Validation cho từng variant
```

### **Scenario 3: File Upload với Progress**

```typescript
// Upload multiple files với validation
// Show upload progress
// Preview images trước khi upload
```

---

**🎯 Remember:** "React Hook Form + Zod = Type-safe, performant forms. Use Controller for custom components, FormProvider to avoid prop drilling, and validation mode onBlur for better performance!"
