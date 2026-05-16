# 🧪 Q50: Testing Strategy - Unit, Integration, E2E Testing

## **⭐ TÓM TẮT CHO PHỎNG VẤN SENIOR/STAFF**

### **🎯 Câu Trả Lời Ngắn Gọn (4-5 phút):**

**"Test Pyramid: 60% Unit (fast, isolated), 30% Integration (component interactions), 10% E2E (critical user flows). Tools: Vitest/Jest (unit), React Testing Library (integration), Playwright (E2E). TDD cho logic, BDD cho features."**

**🔑 Test Pyramid Strategy:**

```
        ╭─────╮
       ╱ E2E  ╲     10% - Chậm, expensive, critical paths only
      ╭───────╮
     ╱ Integr. ╲   30% - Component + API integration
    ╭─────────╮
   ╱   Unit    ╲  60% - Fast, pure functions, business logic
  ╰───────────╯
```

**🔑 3 Loại Tests:**

**1. Unit Tests (Jest/Vitest):**
- **Test**: Pure functions, utilities, hooks (isolated)
- **Fast**: ~1ms/test, chạy thousands trong giây
- **Mock**: External dependencies (APIs, modules)
- **Coverage**: 80-90% cho business logic
- Ví dụ: `formatCurrency(1000)` → "$1,000.00"

**2. Integration Tests (React Testing Library):**
- **Test**: Component interactions, user events, API integration
- **Medium speed**: ~50-200ms/test
- **Real DOM**: jsdom simulation, user-centric queries (`getByRole`)
- **Coverage**: 70-80% cho UI components
- Ví dụ: Click button → API call → show data

**3. E2E Tests (Playwright/Cypress):**
- **Test**: Critical user flows (login, checkout, payment)
- **Slow**: ~5-30s/test, chạy real browser
- **Playwright advantages**: Multi-browser (Chrome, Firefox, Safari), auto-wait, parallel execution
- **Coverage**: Chỉ happy paths + critical errors
- Ví dụ: Full checkout flow (add to cart → payment → confirmation)
- **Best practices**: Reuse auth state, Page Object Model, API mocking

**🔑 Best Practices:**

- **TDD (Test-Driven Development)**: Write test → fail → implement → pass → refactor
- **AAA Pattern**: Arrange (setup) → Act (execute) → Assert (verify)
- **Test behavior, not implementation**: Test user outcomes, not internal state
- **CI/CD Integration**: Run unit/integration on PR, E2E on merge to main

**⚠️ Lỗi Thường Gặp:**
- Test implementation details (`.classList`, internal state) → brittle, dùng user-visible behavior
- 100% coverage cho mọi thứ → waste time, focus critical logic
- E2E tests cho mọi feature → chậm CI, dùng integration tests thay vì
- Không test error cases → production bugs

**💡 Kiến Thức Senior:**
- **Playwright Advanced**: Auto-wait, fixtures, POM pattern, auth state reuse, API mocking
- **Visual Regression**: Chromatic, Percy, Playwright screenshots - detect UI changes
- **Performance Testing**: Lighthouse CI, WebPageTest, Web Vitals (LCP, FCP, CLS)
- **Accessibility Testing**: axe-core, ARIA compliance, keyboard navigation
- **Contract Testing**: Pact - ensure frontend/backend API compatibility
- **Mutation Testing**: Stryker - test your tests (kill mutants)
- **Parallel execution**: Playwright sharding, Jest workers - faster CI
- **Component Testing**: Playwright CT, Storybook - test components in isolation

> **Câu hỏi phỏng vấn Senior Frontend Developer**  
> **Độ khó:** ⭐⭐⭐⭐⭐ (Expert Level)  
> **Thời gian trả lời:** 15-20 phút

---

## 📋 **Mục Lục**

1. [Test Pyramid Strategy](#1-test-pyramid-strategy)
2. [Unit Testing - Jest/Vitest](#2-unit-testing---jestvitest)
3. [Integration Testing - React Testing Library](#3-integration-testing---react-testing-library)
4. [E2E Testing - Playwright/Cypress](#4-e2e-testing---playwrightcypress)
5. [Visual Regression Testing](#5-visual-regression-testing)
6. [Performance Testing](#6-performance-testing)
7. [TDD/BDD Methodology](#7-tddbdd-methodology)
8. [CI/CD Integration](#8-cicd-integration)

---

## 1. Test Pyramid Strategy

### **1.1. Testing Pyramid Architecture**

```
                    ╱╲
                   ╱  ╲
                  ╱ E2E╲          ⚠️ 10% - Slow, expensive, brittle
                 ╱──────╲          - Full user flows
                ╱        ╲         - Critical paths only
               ╱──────────╲
              ╱            ╲
             ╱ Integration  ╲     ⚡ 30% - Medium speed
            ╱────────────────╲    - Component integration
           ╱                  ╲   - API integration
          ╱────────────────────╲
         ╱                      ╲
        ╱    Unit Tests          ╲  ✅ 60% - Fast, isolated
       ╱──────────────────────────╲  - Pure functions
      ╱____________________________╲ - Business logic
                                      - Utilities
```

### **1.2. Test Coverage Guidelines**

```typescript
// ===================================================
// 📊 **COVERAGE TARGETS**
// ===================================================

// jest.config.js or vitest.config.ts
export default {
  collectCoverageFrom: [
    'src/**/*.{ts,tsx}',
    '!src/**/*.d.ts',
    '!src/**/*.stories.tsx',
    '!src/main.tsx',
  ],
  coverageThresholds: {
    global: {
      statements: 80,    // ✅ 80% minimum
      branches: 75,      // ✅ 75% minimum
      functions: 80,     // ✅ 80% minimum
      lines: 80,         // ✅ 80% minimum
    },
    // ⭐ Critical modules require higher coverage
    './src/utils/': {
      statements: 95,
      branches: 90,
      functions: 95,
      lines: 95,
    },
    './src/hooks/': {
      statements: 90,
      branches: 85,
      functions: 90,
      lines: 90,
    },
  },
};
```

---

## 2. Unit Testing - Jest/Vitest

### **2.1. Pure Function Testing**

```typescript
// ===================================================
// 🎯 **UTILITY FUNCTIONS** (SUT - System Under Test)
// ===================================================

// src/utils/formatters.ts
export function formatCurrency(amount: number, currency = 'USD'): string {
  if (typeof amount !== 'number' || isNaN(amount)) {
    throw new Error('Amount must be a valid number');
  }

  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency,
  }).format(amount);
}

export function formatDate(date: Date | string): string {
  const dateObj = typeof date === 'string' ? new Date(date) : date;
  
  if (!(dateObj instanceof Date) || isNaN(dateObj.getTime())) {
    throw new Error('Invalid date');
  }

  return new Intl.DateTimeFormat('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  }).format(dateObj);
}

export function calculateDiscount(price: number, discountPercent: number): number {
  if (price < 0 || discountPercent < 0 || discountPercent > 100) {
    throw new Error('Invalid input');
  }

  return price * (1 - discountPercent / 100);
}

// ===================================================
// ✅ **UNIT TESTS** (formatters.test.ts)
// ===================================================

import { describe, it, expect } from 'vitest';
import { formatCurrency, formatDate, calculateDiscount } from './formatters';

describe('formatCurrency', () => {
  // ✅ Happy path
  it('should format positive numbers correctly', () => {
    expect(formatCurrency(1234.56)).toBe('$1,234.56');
    expect(formatCurrency(0)).toBe('$0.00');
  });

  it('should support different currencies', () => {
    expect(formatCurrency(1000, 'EUR')).toBe('€1,000.00');
    expect(formatCurrency(1000, 'GBP')).toBe('£1,000.00');
  });

  // ❌ Error cases
  it('should throw error for invalid input', () => {
    expect(() => formatCurrency(NaN)).toThrow('Amount must be a valid number');
    expect(() => formatCurrency('100' as any)).toThrow();
  });

  // ⚠️ Edge cases
  it('should handle edge cases', () => {
    expect(formatCurrency(0.01)).toBe('$0.01');
    expect(formatCurrency(999999999.99)).toBe('$999,999,999.99');
    expect(formatCurrency(-100)).toBe('-$100.00');
  });
});

describe('calculateDiscount', () => {
  // ✅ Boundary value testing
  it('should calculate discount correctly', () => {
    expect(calculateDiscount(100, 10)).toBe(90);    // 10% off
    expect(calculateDiscount(100, 50)).toBe(50);    // 50% off
    expect(calculateDiscount(100, 0)).toBe(100);    // No discount
    expect(calculateDiscount(100, 100)).toBe(0);    // 100% off
  });

  // ❌ Invalid inputs
  it('should throw for invalid inputs', () => {
    expect(() => calculateDiscount(-100, 10)).toThrow('Invalid input');
    expect(() => calculateDiscount(100, -10)).toThrow('Invalid input');
    expect(() => calculateDiscount(100, 101)).toThrow('Invalid input');
  });

  // 🔢 Precision testing
  it('should handle decimal precision', () => {
    expect(calculateDiscount(99.99, 15)).toBeCloseTo(84.99, 2);
  });
});
```

### **2.2. Custom Hooks Testing**

```typescript
// ===================================================
// 🪝 **CUSTOM HOOK** (useLocalStorage.ts)
// ===================================================

import { useState, useEffect } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T) {
  // ✅ State to store value
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error loading ${key} from localStorage:`, error);
      return initialValue;
    }
  });

  // ✅ Return a wrapped version of useState's setter
  const setValue = (value: T | ((val: T) => T)) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error saving ${key} to localStorage:`, error);
    }
  };

  return [storedValue, setValue] as const;
}

// ===================================================
// ✅ **HOOK TESTING** (useLocalStorage.test.ts)
// ===================================================

import { renderHook, act } from '@testing-library/react';
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { useLocalStorage } from './useLocalStorage';

describe('useLocalStorage', () => {
  beforeEach(() => {
    // ✅ Clear localStorage before each test
    localStorage.clear();
    // ✅ Clear console spies
    vi.clearAllMocks();
  });

  it('should initialize with default value', () => {
    const { result } = renderHook(() => useLocalStorage('test-key', 'default'));
    
    expect(result.current[0]).toBe('default');
  });

  it('should initialize with value from localStorage', () => {
    // ✅ Setup: Pre-populate localStorage
    localStorage.setItem('test-key', JSON.stringify('stored-value'));
    
    const { result } = renderHook(() => useLocalStorage('test-key', 'default'));
    
    expect(result.current[0]).toBe('stored-value');
  });

  it('should update localStorage when value changes', () => {
    const { result } = renderHook(() => useLocalStorage('test-key', 'initial'));
    
    // ✅ Act: Update value
    act(() => {
      result.current[1]('updated');
    });
    
    // ✅ Assert: Check both state and localStorage
    expect(result.current[0]).toBe('updated');
    expect(localStorage.getItem('test-key')).toBe(JSON.stringify('updated'));
  });

  it('should support functional updates', () => {
    const { result } = renderHook(() => useLocalStorage('counter', 0));
    
    // ✅ Functional update: (prev) => prev + 1
    act(() => {
      result.current[1](prev => prev + 1);
    });
    
    expect(result.current[0]).toBe(1);
  });

  it('should handle complex objects', () => {
    const initialUser = { name: 'John', age: 30 };
    const { result } = renderHook(() => useLocalStorage('user', initialUser));
    
    act(() => {
      result.current[1]({ name: 'Jane', age: 25 });
    });
    
    expect(result.current[0]).toEqual({ name: 'Jane', age: 25 });
    expect(JSON.parse(localStorage.getItem('user')!)).toEqual({ name: 'Jane', age: 25 });
  });

  it('should handle localStorage errors gracefully', () => {
    const consoleErrorSpy = vi.spyOn(console, 'error').mockImplementation(() => {});
    
    // ✅ Mock localStorage.setItem to throw error
    vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => {
      throw new Error('QuotaExceededError');
    });
    
    const { result } = renderHook(() => useLocalStorage('test-key', 'initial'));
    
    act(() => {
      result.current[1]('new-value');
    });
    
    // ✅ Assert: Error logged but doesn't crash
    expect(consoleErrorSpy).toHaveBeenCalled();
    expect(result.current[0]).toBe('new-value'); // State still updated
    
    consoleErrorSpy.mockRestore();
  });
});
```

### **2.3. Async Function Testing**

```typescript
// ===================================================
// 🌐 **API CLIENT** (api.ts)
// ===================================================

export interface User {
  id: string;
  name: string;
  email: string;
}

export async function fetchUsers(): Promise<User[]> {
  const response = await fetch('/api/users');
  
  if (!response.ok) {
    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
  }
  
  return response.json();
}

export async function createUser(user: Omit<User, 'id'>): Promise<User> {
  const response = await fetch('/api/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(user),
  });
  
  if (!response.ok) {
    throw new Error('Failed to create user');
  }
  
  return response.json();
}

// ===================================================
// ✅ **ASYNC TESTS** (api.test.ts)
// ===================================================

import { describe, it, expect, beforeEach, vi } from 'vitest';
import { fetchUsers, createUser } from './api';

// ✅ Mock global fetch
global.fetch = vi.fn();

describe('fetchUsers', () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });

  it('should fetch users successfully', async () => {
    const mockUsers = [
      { id: '1', name: 'Alice', email: 'alice@example.com' },
      { id: '2', name: 'Bob', email: 'bob@example.com' },
    ];

    // ✅ Mock successful response
    (global.fetch as any).mockResolvedValueOnce({
      ok: true,
      json: async () => mockUsers,
    });

    const users = await fetchUsers();

    expect(fetch).toHaveBeenCalledWith('/api/users');
    expect(users).toEqual(mockUsers);
  });

  it('should throw error on failed request', async () => {
    // ✅ Mock failed response
    (global.fetch as any).mockResolvedValueOnce({
      ok: false,
      status: 500,
      statusText: 'Internal Server Error',
    });

    await expect(fetchUsers()).rejects.toThrow('HTTP 500: Internal Server Error');
  });

  it('should throw error on network failure', async () => {
    // ✅ Mock network error
    (global.fetch as any).mockRejectedValueOnce(new Error('Network error'));

    await expect(fetchUsers()).rejects.toThrow('Network error');
  });
});

describe('createUser', () => {
  it('should create user with generated ID', async () => {
    const newUser = { name: 'Charlie', email: 'charlie@example.com' };
    const createdUser = { id: '3', ...newUser };

    (global.fetch as any).mockResolvedValueOnce({
      ok: true,
      json: async () => createdUser,
    });

    const result = await createUser(newUser);

    // ✅ Verify fetch called with correct params
    expect(fetch).toHaveBeenCalledWith('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newUser),
    });

    expect(result).toEqual(createdUser);
  });
});
```

---

## 3. Integration Testing - React Testing Library

### **3.1. Component Integration Testing**

```typescript
// ===================================================
// 🧩 **REACT COMPONENT** (UserList.tsx)
// ===================================================

import { useState, useEffect } from 'react';
import { fetchUsers, User } from './api';

export const UserList = () => {
  const [users, setUsers] = useState<User[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchUsers()
      .then(setUsers)
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div role="status">Loading...</div>;
  if (error) return <div role="alert">Error: {error}</div>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id} data-testid={`user-${user.id}`}>
          <h3>{user.name}</h3>
          <p>{user.email}</p>
        </li>
      ))}
    </ul>
  );
};

// ===================================================
// ✅ **INTEGRATION TEST** (UserList.test.tsx)
// ===================================================

import { render, screen, waitFor } from '@testing-library/react';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { UserList } from './UserList';
import * as api from './api';

// ✅ Mock API module
vi.mock('./api');

describe('UserList', () => {
  beforeEach(() => {
    vi.resetAllMocks();
  });

  it('should display loading state initially', () => {
    vi.spyOn(api, 'fetchUsers').mockImplementation(() => new Promise(() => {}));
    
    render(<UserList />);
    
    expect(screen.getByRole('status')).toHaveTextContent('Loading...');
  });

  it('should display users after successful fetch', async () => {
    const mockUsers = [
      { id: '1', name: 'Alice', email: 'alice@example.com' },
      { id: '2', name: 'Bob', email: 'bob@example.com' },
    ];

    vi.spyOn(api, 'fetchUsers').mockResolvedValueOnce(mockUsers);
    
    render(<UserList />);
    
    // ✅ Wait for async operation
    await waitFor(() => {
      expect(screen.getByText('Alice')).toBeInTheDocument();
      expect(screen.getByText('Bob')).toBeInTheDocument();
    });

    // ✅ Verify all users rendered
    expect(screen.getByTestId('user-1')).toBeInTheDocument();
    expect(screen.getByTestId('user-2')).toBeInTheDocument();
  });

  it('should display error message on failed fetch', async () => {
    vi.spyOn(api, 'fetchUsers').mockRejectedValueOnce(new Error('Network error'));
    
    render(<UserList />);
    
    await waitFor(() => {
      expect(screen.getByRole('alert')).toHaveTextContent('Error: Network error');
    });
  });

  it('should not display loading state after data loads', async () => {
    vi.spyOn(api, 'fetchUsers').mockResolvedValueOnce([]);
    
    render(<UserList />);
    
    await waitFor(() => {
      expect(screen.queryByRole('status')).not.toBeInTheDocument();
    });
  });
});
```

### **3.2. Form Testing with User Interactions**

```typescript
// ===================================================
// 📝 **FORM COMPONENT** (LoginForm.tsx)
// ===================================================

import { useState } from 'react';

interface LoginFormProps {
  onSubmit: (credentials: { email: string; password: string }) => Promise<void>;
}

export const LoginForm = ({ onSubmit }: LoginFormProps) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState<Record<string, string>>({});
  const [submitting, setSubmitting] = useState(false);

  const validate = () => {
    const newErrors: Record<string, string> = {};
    
    if (!email) {
      newErrors.email = 'Email is required';
    } else if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Email is invalid';
    }
    
    if (!password) {
      newErrors.password = 'Password is required';
    } else if (password.length < 8) {
      newErrors.password = 'Password must be at least 8 characters';
    }
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validate()) return;
    
    setSubmitting(true);
    try {
      await onSubmit({ email, password });
    } catch (error) {
      setErrors({ submit: (error as Error).message });
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label htmlFor="email">Email</label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          aria-invalid={!!errors.email}
          aria-describedby={errors.email ? 'email-error' : undefined}
        />
        {errors.email && <span id="email-error" role="alert">{errors.email}</span>}
      </div>

      <div>
        <label htmlFor="password">Password</label>
        <input
          id="password"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          aria-invalid={!!errors.password}
          aria-describedby={errors.password ? 'password-error' : undefined}
        />
        {errors.password && <span id="password-error" role="alert">{errors.password}</span>}
      </div>

      {errors.submit && <div role="alert">{errors.submit}</div>}

      <button type="submit" disabled={submitting}>
        {submitting ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
};

// ===================================================
// ✅ **FORM INTEGRATION TEST** (LoginForm.test.tsx)
// ===================================================

import { render, screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';
import { LoginForm } from './LoginForm';

describe('LoginForm', () => {
  it('should render form fields', () => {
    render(<LoginForm onSubmit={vi.fn()} />);
    
    expect(screen.getByLabelText('Email')).toBeInTheDocument();
    expect(screen.getByLabelText('Password')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: 'Login' })).toBeInTheDocument();
  });

  it('should validate email field', async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={vi.fn()} />);
    
    const submitButton = screen.getByRole('button', { name: 'Login' });
    
    // ✅ Submit without email
    await user.click(submitButton);
    
    expect(screen.getByText('Email is required')).toBeInTheDocument();
    
    // ✅ Submit with invalid email
    await user.type(screen.getByLabelText('Email'), 'invalid-email');
    await user.click(submitButton);
    
    expect(screen.getByText('Email is invalid')).toBeInTheDocument();
  });

  it('should validate password field', async () => {
    const user = userEvent.setup();
    render(<LoginForm onSubmit={vi.fn()} />);
    
    const submitButton = screen.getByRole('button', { name: 'Login' });
    
    // ✅ Submit without password
    await user.click(submitButton);
    
    expect(screen.getByText('Password is required')).toBeInTheDocument();
    
    // ✅ Submit with short password
    await user.type(screen.getByLabelText('Password'), 'short');
    await user.click(submitButton);
    
    expect(screen.getByText('Password must be at least 8 characters')).toBeInTheDocument();
  });

  it('should submit form with valid data', async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn().mockResolvedValue(undefined);
    
    render(<LoginForm onSubmit={onSubmit} />);
    
    // ✅ Fill form
    await user.type(screen.getByLabelText('Email'), 'test@example.com');
    await user.type(screen.getByLabelText('Password'), 'password123');
    
    // ✅ Submit
    await user.click(screen.getByRole('button', { name: 'Login' }));
    
    await waitFor(() => {
      expect(onSubmit).toHaveBeenCalledWith({
        email: 'test@example.com',
        password: 'password123',
      });
    });
  });

  it('should display loading state during submission', async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn(() => new Promise(() => {})); // Never resolves
    
    render(<LoginForm onSubmit={onSubmit} />);
    
    await user.type(screen.getByLabelText('Email'), 'test@example.com');
    await user.type(screen.getByLabelText('Password'), 'password123');
    await user.click(screen.getByRole('button', { name: 'Login' }));
    
    await waitFor(() => {
      expect(screen.getByRole('button', { name: 'Logging in...' })).toBeDisabled();
    });
  });

  it('should display error message on submit failure', async () => {
    const user = userEvent.setup();
    const onSubmit = vi.fn().mockRejectedValue(new Error('Invalid credentials'));
    
    render(<LoginForm onSubmit={onSubmit} />);
    
    await user.type(screen.getByLabelText('Email'), 'test@example.com');
    await user.type(screen.getByLabelText('Password'), 'password123');
    await user.click(screen.getByRole('button', { name: 'Login' }));
    
    await waitFor(() => {
      expect(screen.getByText('Invalid credentials')).toBeInTheDocument();
    });
  });
});
```

---

## 4. E2E Testing - Playwright/Cypress

### **4.1. Playwright E2E Tests**

#### **4.1.1. Playwright Overview & Advanced Configuration**

**🎭 Tại Sao Chọn Playwright?**
- ✅ **Multi-browser support**: Chromium, Firefox, WebKit (Safari) - một API cho tất cả
- ✅ **Auto-wait**: Tự động chờ elements sẵn sàng trước khi thao tác
- ✅ **Network interception**: Mock APIs, intercept requests dễ dàng
- ✅ **Parallel execution**: Chạy tests song song, tăng tốc CI/CD
- ✅ **Mobile emulation**: Test responsive với real device profiles
- ✅ **Video & screenshots**: Auto capture khi test fail
- ✅ **Trace viewer**: Debug với timeline UI interactions
- ✅ **Component testing**: Test React/Vue components isolated

```typescript
// ===================================================
// 🎭 **PLAYWRIGHT ADVANCED CONFIG** (playwright.config.ts)
// ===================================================

import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  // ✅ Test directory
  testDir: './e2e',
  
  // ✅ Run tests in parallel (mỗi file là một worker)
  fullyParallel: true,
  
  // ✅ Retry failed tests (CI: 2 lần, local: 0)
  retries: process.env.CI ? 2 : 0,
  
  // ✅ Number of workers (CI: 1, local: số CPU cores)
  workers: process.env.CI ? 1 : undefined,
  
  // ✅ Global timeout cho mỗi test
  timeout: 30000, // 30 seconds
  
  // ✅ Expect timeout cho assertions
  expect: {
    timeout: 5000, // 5 seconds
  },
  
  // ✅ Reporter configuration (nhiều reporters cùng lúc)
  reporter: [
    ['html', { open: 'never' }], // HTML report
    ['json', { outputFile: 'test-results.json' }], // JSON cho CI
    ['junit', { outputFile: 'test-results.xml' }], // JUnit cho Jenkins
    ['list'], // Console output
    ['github'], // GitHub Actions annotations
  ],
  
  // ✅ Shared settings for all projects
  use: {
    // Base URL (dùng relative paths trong tests)
    baseURL: process.env.BASE_URL || 'http://localhost:3000',
    
    // Collect trace on first retry (debug failed tests)
    trace: 'on-first-retry',
    
    // Screenshot on failure
    screenshot: 'only-on-failure',
    
    // Video recording
    video: 'retain-on-failure',
    
    // Emulate timezone
    timezoneId: 'America/New_York',
    
    // Emulate locale & geolocation
    locale: 'en-US',
    geolocation: { longitude: 12.5683, latitude: 55.6761 },
    permissions: ['geolocation'],
    
    // Viewport size
    viewport: { width: 1280, height: 720 },
    
    // Default navigation timeout
    navigationTimeout: 15000,
    
    // Default action timeout
    actionTimeout: 10000,
    
    // Ignore HTTPS errors
    ignoreHTTPSErrors: true,
    
    // Network idle timeout
    // waitUntil: 'networkidle',
  },

  // ✅ Projects for different browsers & devices
  projects: [
    // Desktop browsers
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },
    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },
    
    // Mobile browsers
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
    {
      name: 'iPad',
      use: { ...devices['iPad Pro'] },
    },
    
    // Branded browsers
    {
      name: 'Microsoft Edge',
      use: { ...devices['Desktop Edge'], channel: 'msedge' },
    },
    {
      name: 'Google Chrome',
      use: { ...devices['Desktop Chrome'], channel: 'chrome' },
    },
  ],

  // ✅ Web server configuration (auto-start dev server)
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:3000',
    reuseExistingServer: !process.env.CI, // Reuse trong dev, restart trong CI
    timeout: 120000, // 2 minutes
    stdout: 'ignore', // Không log server output
    stderr: 'pipe', // Log errors
  },
  
  // ✅ Global setup/teardown
  globalSetup: './global-setup.ts',
  globalTeardown: './global-teardown.ts',
});

// ===================================================
// 🌐 **GLOBAL SETUP** (global-setup.ts)
// ===================================================

import { chromium, FullConfig } from '@playwright/test';

async function globalSetup(config: FullConfig) {
  // ✅ Setup: Create admin user, seed database, etc.
  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  // Login and save auth state
  await page.goto('http://localhost:3000/login');
  await page.getByLabel('Email').fill('admin@example.com');
  await page.getByLabel('Password').fill('password123');
  await page.getByRole('button', { name: 'Login' }).click();
  await page.waitForURL('**/dashboard');
  
  // Save authentication state
  await page.context().storageState({ path: 'playwright/.auth/admin.json' });
  
  await browser.close();
}

export default globalSetup;
```

#### **4.1.2. Locator Strategies (Best Practices)**

```typescript
// ===================================================
// 🎯 **PLAYWRIGHT LOCATOR PRIORITIES**
// ===================================================

import { test, expect, Page } from '@playwright/test';

test('Locator strategies from best to worst', async ({ page }) => {
  // ✅ 1. BEST: Role-based (accessibility-friendly)
  await page.getByRole('button', { name: 'Submit' }).click();
  await page.getByRole('textbox', { name: 'Email' }).fill('test@example.com');
  await page.getByRole('link', { name: 'Contact Us' }).click();
  
  // ✅ 2. GOOD: Label text (form inputs)
  await page.getByLabel('Username').fill('admin');
  await page.getByLabel(/password/i).fill('secret'); // Case-insensitive regex
  
  // ✅ 3. GOOD: Placeholder text
  await page.getByPlaceholder('Enter your email').fill('test@example.com');
  
  // ✅ 4. GOOD: Visible text
  await page.getByText('Click here').click();
  await page.getByText(/sign in/i).click(); // Case-insensitive
  
  // ✅ 5. OK: Test ID (fallback khi không có semantic locators)
  await page.getByTestId('submit-button').click();
  
  // ✅ 6. GOOD: Title attribute
  await page.getByTitle('Close dialog').click();
  
  // ✅ 7. OK: Alt text (images)
  await page.getByAltText('Company logo').click();
  
  // ❌ 8. AVOID: CSS selectors (brittle, implementation-dependent)
  await page.locator('.btn-primary').click(); // Bad
  await page.locator('#submit-btn').click(); // Bad
  
  // ❌ 9. AVOID: XPath (hard to read & maintain)
  await page.locator('xpath=//button[@class="submit"]').click(); // Bad
});

// ===================================================
// 🔗 **CHAINING & FILTERING LOCATORS**
// ===================================================

test('Advanced locator chaining', async ({ page }) => {
  await page.goto('/products');
  
  // ✅ Filter by text
  const firstProduct = page.getByRole('listitem').filter({ hasText: 'iPhone' });
  await firstProduct.getByRole('button', { name: 'Add to Cart' }).click();
  
  // ✅ Filter by NOT text
  const nonAppleProducts = page.getByRole('listitem').filter({ hasNotText: 'Apple' });
  
  // ✅ Find child elements
  const productCard = page.getByTestId('product-card').first();
  await productCard.locator('button:text("Add to Cart")').click();
  
  // ✅ Find nth element
  await page.getByRole('button', { name: 'Delete' }).nth(2).click();
  
  // ✅ Get all matching elements
  const allButtons = await page.getByRole('button').all();
  for (const button of allButtons) {
    console.log(await button.textContent());
  }
  
  // ✅ Count elements
  const buttonCount = await page.getByRole('button').count();
  expect(buttonCount).toBeGreaterThan(0);
});
```

#### **4.1.3. API Mocking & Network Interception**

```typescript
// ===================================================
// 🌐 **MOCK API RESPONSES**
// ===================================================

test.describe('API Mocking', () => {
  test('should mock GET request', async ({ page }) => {
    // ✅ Intercept and mock API call
    await page.route('**/api/users', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify([
          { id: 1, name: 'Alice', email: 'alice@example.com' },
          { id: 2, name: 'Bob', email: 'bob@example.com' },
        ]),
      });
    });

    await page.goto('/users');
    
    // ✅ Verify mocked data displayed
    await expect(page.getByText('Alice')).toBeVisible();
    await expect(page.getByText('Bob')).toBeVisible();
  });

  test('should simulate network errors', async ({ page }) => {
    // ✅ Abort request to simulate network error
    await page.route('**/api/users', route => route.abort('failed'));

    await page.goto('/users');
    
    // ✅ Verify error message
    await expect(page.getByText('Failed to load users')).toBeVisible();
  });

  test('should modify request headers', async ({ page }) => {
    await page.route('**/api/users', async route => {
      // ✅ Continue request with modified headers
      await route.continue({
        headers: {
          ...route.request().headers(),
          'Authorization': 'Bearer fake-token',
          'X-Custom-Header': 'test-value',
        },
      });
    });

    await page.goto('/users');
  });
  
  test('should mock based on request method', async ({ page }) => {
    // ✅ Mock POST request
    await page.route('**/api/users', async (route) => {
      if (route.request().method() === 'POST') {
        const postData = route.request().postDataJSON();
        await route.fulfill({
          status: 201,
          body: JSON.stringify({ id: 99, ...postData }),
        });
      } else {
        // Let other methods pass through
        await route.continue();
      }
    });
    
    await page.goto('/users/new');
    await page.getByLabel('Name').fill('Charlie');
    await page.getByRole('button', { name: 'Create' }).click();
  });
  
  test('should delay API responses', async ({ page }) => {
    // ✅ Simulate slow network
    await page.route('**/api/users', async route => {
      await new Promise(resolve => setTimeout(resolve, 3000)); // 3s delay
      await route.continue();
    });
    
    await page.goto('/users');
    // Test loading state during delay
    await expect(page.getByText('Loading...')).toBeVisible();
  });
});
```

#### **4.1.4. Fixtures & Custom Test Context**

```typescript
// ===================================================
// 🎯 **CUSTOM FIXTURES** (test-fixtures.ts)
// ===================================================

import { test as base, expect, Page } from '@playwright/test';

// ✅ Define custom fixture types
type MyFixtures = {
  authenticatedPage: Page;
  testUser: { email: string; password: string; name: string };
  adminPage: Page;
};

// ✅ Extend base test with custom fixtures
export const test = base.extend<MyFixtures>({
  // Custom fixture: authenticated user page
  authenticatedPage: async ({ page }, use) => {
    // Setup: Login before test
    await page.goto('/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('password123');
    await page.getByRole('button', { name: 'Login' }).click();
    await page.waitForURL('**/dashboard');
    
    // Provide page to test
    await use(page);
    
    // Teardown: Logout after test
    await page.getByRole('button', { name: 'Logout' }).click();
  },

  // Custom fixture: admin page
  adminPage: async ({ browser }, use) => {
    const context = await browser.newContext({
      storageState: 'playwright/.auth/admin.json', // Reuse auth state
    });
    const page = await context.newPage();
    await use(page);
    await context.close();
  },

  // Custom fixture: test user data
  testUser: async ({}, use) => {
    const user = {
      email: 'test@example.com',
      password: 'Test123!',
      name: 'Test User',
    };
    // Could create user in database here
    await use(user);
    // Could cleanup user from database here
  },
});

export { expect };

// ===================================================
// 🔧 **USE CUSTOM FIXTURES**
// ===================================================

import { test, expect } from './test-fixtures';

test('should access user dashboard', async ({ authenticatedPage }) => {
  await authenticatedPage.goto('/dashboard');
  await expect(authenticatedPage.getByText('Welcome')).toBeVisible();
});

test('should access admin panel', async ({ adminPage }) => {
  await adminPage.goto('/admin');
  await expect(adminPage.getByText('Admin Panel')).toBeVisible();
});
```

#### **4.1.5. Page Object Model (POM)**

```typescript
// ===================================================
// 📦 **PAGE OBJECT MODEL** (pages/LoginPage.ts)
// ===================================================

import { Page, Locator, expect } from '@playwright/test';

export class LoginPage {
  readonly page: Page;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly loginButton: Locator;
  readonly errorMessage: Locator;
  readonly forgotPasswordLink: Locator;

  constructor(page: Page) {
    this.page = page;
    this.emailInput = page.getByLabel('Email');
    this.passwordInput = page.getByLabel('Password');
    this.loginButton = page.getByRole('button', { name: 'Login' });
    this.errorMessage = page.getByRole('alert');
    this.forgotPasswordLink = page.getByRole('link', { name: 'Forgot Password?' });
  }

  async goto() {
    await this.page.goto('/login');
  }

  async login(email: string, password: string) {
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
    await this.loginButton.click();
  }

  async expectError(message: string) {
    await expect(this.errorMessage).toContainText(message);
  }
  
  async expectToBeOnLoginPage() {
    await expect(this.page).toHaveURL(/.*login/);
  }
}

// pages/DashboardPage.ts
export class DashboardPage {
  readonly page: Page;
  readonly welcomeMessage: Locator;
  readonly logoutButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.welcomeMessage = page.getByTestId('welcome-message');
    this.logoutButton = page.getByRole('button', { name: 'Logout' });
  }

  async expectWelcomeMessage(name: string) {
    await expect(this.welcomeMessage).toContainText(`Welcome, ${name}`);
  }

  async logout() {
    await this.logoutButton.click();
  }
}

// ===================================================
// ✅ **USE PAGE OBJECTS**
// ===================================================

import { test, expect } from '@playwright/test';
import { LoginPage } from './pages/LoginPage';
import { DashboardPage } from './pages/DashboardPage';

test('should login with POM', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const dashboardPage = new DashboardPage(page);
  
  await loginPage.goto();
  await loginPage.login('admin@example.com', 'password123');
  
  await dashboardPage.expectWelcomeMessage('Admin');
});
```

#### **4.1.6. Basic E2E Test Examples**

```typescript
// ===================================================
// 🎭 **PLAYWRIGHT E2E TEST** (login.spec.ts)
// ===================================================

import { test, expect } from '@playwright/test';

test.describe('Login Flow', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('http://localhost:3000/login');
  });

  test('should display login form', async ({ page }) => {
    // ✅ Check form elements exist
    await expect(page.getByLabel('Email')).toBeVisible();
    await expect(page.getByLabel('Password')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Login' })).toBeVisible();
  });

  test('should show validation errors', async ({ page }) => {
    // ✅ Click submit without filling form
    await page.getByRole('button', { name: 'Login' }).click();
    
    // ✅ Assert error messages
    await expect(page.getByText('Email is required')).toBeVisible();
    await expect(page.getByText('Password is required')).toBeVisible();
  });

  test('should login successfully with valid credentials', async ({ page }) => {
    // ✅ Fill form
    await page.getByLabel('Email').fill('admin@example.com');
    await page.getByLabel('Password').fill('password123');
    
    // ✅ Submit form
    await page.getByRole('button', { name: 'Login' }).click();
    
    // ✅ Wait for navigation
    await page.waitForURL('**/dashboard');
    
    // ✅ Verify user is logged in
    await expect(page.getByText('Welcome, Admin')).toBeVisible();
  });

  test('should show error for invalid credentials', async ({ page }) => {
    await page.getByLabel('Email').fill('wrong@example.com');
    await page.getByLabel('Password').fill('wrongpassword');
    await page.getByRole('button', { name: 'Login' }).click();
    
    // ✅ Error message should appear
    await expect(page.getByText('Invalid credentials')).toBeVisible();
    
    // ✅ Should remain on login page
    await expect(page).toHaveURL(/.*login/);
  });

  test('should persist session after page reload', async ({ page }) => {
    // ✅ Login
    await page.getByLabel('Email').fill('admin@example.com');
    await page.getByLabel('Password').fill('password123');
    await page.getByRole('button', { name: 'Login' }).click();
    await page.waitForURL('**/dashboard');
    
    // ✅ Reload page
    await page.reload();
    
    // ✅ Should still be logged in
    await expect(page.getByText('Welcome, Admin')).toBeVisible();
  });
});

// ===================================================
// 🛒 **E2E TEST: Shopping Cart Flow**
// ===================================================

test.describe('Shopping Cart', () => {
  test('should add product to cart and checkout', async ({ page }) => {
    await page.goto('http://localhost:3000');
    
    // ✅ Step 1: Browse products
    await page.getByRole('link', { name: 'Products' }).click();
    await expect(page).toHaveURL(/.*products/);
    
    // ✅ Step 2: Add product to cart
    const firstProduct = page.getByTestId('product-card').first();
    await firstProduct.getByRole('button', { name: 'Add to Cart' }).click();
    
    // ✅ Step 3: Verify cart badge updated
    await expect(page.getByTestId('cart-badge')).toHaveText('1');
    
    // ✅ Step 4: Open cart
    await page.getByTestId('cart-icon').click();
    await expect(page.getByTestId('cart-drawer')).toBeVisible();
    
    // ✅ Step 5: Verify product in cart
    const cartItem = page.getByTestId('cart-item').first();
    await expect(cartItem).toBeVisible();
    
    // ✅ Step 6: Proceed to checkout
    await page.getByRole('button', { name: 'Checkout' }).click();
    await expect(page).toHaveURL(/.*checkout/);
    
    // ✅ Step 7: Fill shipping info
    await page.getByLabel('Full Name').fill('John Doe');
    await page.getByLabel('Address').fill('123 Main St');
    await page.getByLabel('City').fill('New York');
    await page.getByLabel('Zip Code').fill('10001');
    
    // ✅ Step 8: Place order
    await page.getByRole('button', { name: 'Place Order' }).click();
    
    // ✅ Step 9: Verify order confirmation
    await expect(page.getByText('Order Confirmed')).toBeVisible();
    await expect(page.getByTestId('order-number')).toBeVisible();
  });

  test('should update quantity in cart', async ({ page, context }) => {
    // ✅ Setup: Add product to cart first
    await page.goto('http://localhost:3000/products');
    await page.getByTestId('product-card').first().getByRole('button', { name: 'Add to Cart' }).click();
    
    // ✅ Open cart
    await page.getByTestId('cart-icon').click();
    
    // ✅ Increase quantity
    const quantityInput = page.getByTestId('quantity-input').first();
    await expect(quantityInput).toHaveValue('1');
    
    await page.getByTestId('increase-quantity').first().click();
    await expect(quantityInput).toHaveValue('2');
    
    // ✅ Verify total price updated
    const totalPrice = page.getByTestId('cart-total');
    await expect(totalPrice).toContainText('$'); // Price should double
  });
});

// ===================================================
// 📸 **VISUAL REGRESSION TEST** (Playwright)
// ===================================================

test.describe('Visual Regression', () => {
  test('should match homepage screenshot', async ({ page }) => {
    await page.goto('http://localhost:3000');
    
    // ✅ Wait for page to be fully loaded
    await page.waitForLoadState('networkidle');
    
    // ✅ Take screenshot and compare
    await expect(page).toHaveScreenshot('homepage.png', {
      fullPage: true,
      animations: 'disabled', // Disable animations for consistent screenshots
    });
  });

  test('should match mobile viewport', async ({ page }) => {
    // ✅ Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    await page.goto('http://localhost:3000');
    
    await expect(page).toHaveScreenshot('homepage-mobile.png');
  });
  
  test('should match specific element', async ({ page }) => {
    await page.goto('http://localhost:3000/products');
    
    // ✅ Screenshot specific element only
    const productCard = page.getByTestId('product-card').first();
    await expect(productCard).toHaveScreenshot('product-card.png');
  });

  test('should mask dynamic content', async ({ page }) => {
    await page.goto('http://localhost:3000/dashboard');
    
    // ✅ Mask elements with dynamic content (dates, timestamps, IDs)
    await expect(page).toHaveScreenshot('dashboard.png', {
      mask: [
        page.getByTestId('current-time'),
        page.getByTestId('user-id'),
        page.getByTestId('session-id'),
      ],
    });
  });
});

// ===================================================
// 🎬 **ADVANCED INTERACTIONS**
// ===================================================

test.describe('User Interactions', () => {
  test('should handle various user actions', async ({ page }) => {
    await page.goto('/interactions');

    // ✅ Click variations
    await page.getByRole('button', { name: 'Click Me' }).click();
    await page.getByRole('button', { name: 'Right Click' }).click({ button: 'right' });
    await page.getByRole('button', { name: 'Double Click' }).dblclick();
    await page.getByRole('button', { name: 'Shift+Click' }).click({ modifiers: ['Shift'] });
    
    // ✅ Hover & focus
    await page.getByRole('button', { name: 'Hover' }).hover();
    await page.getByLabel('Email').focus();
    
    // ✅ Drag and drop
    await page.getByTestId('draggable').dragTo(page.getByTestId('droppable'));
    
    // ✅ Keyboard input
    await page.keyboard.press('Enter');
    await page.keyboard.type('Hello World');
    await page.keyboard.press('Control+A'); // Select all
    await page.keyboard.press('Control+C'); // Copy
    await page.keyboard.press('Control+V'); // Paste
    
    // ✅ File upload
    await page.getByLabel('Upload File').setInputFiles('path/to/file.pdf');
    // Multiple files
    await page.getByLabel('Upload Files').setInputFiles([
      'file1.jpg',
      'file2.jpg',
    ]);
    // Remove files
    await page.getByLabel('Upload File').setInputFiles([]);
    
    // ✅ Select dropdown
    await page.getByLabel('Country').selectOption('USA');
    await page.getByLabel('Country').selectOption({ label: 'United States' });
    await page.getByLabel('Country').selectOption({ index: 1 });
    
    // ✅ Checkbox & Radio
    await page.getByLabel('Accept Terms').check();
    await expect(page.getByLabel('Accept Terms')).toBeChecked();
    
    await page.getByLabel('Accept Terms').uncheck();
    await expect(page.getByLabel('Accept Terms')).not.toBeChecked();
    
    await page.getByRole('radio', { name: 'Option 1' }).check();
    
    // ✅ Multiple selections
    await page.getByLabel('Multi Select').selectOption(['option1', 'option2', 'option3']);
  });

  test('should handle iframe interactions', async ({ page }) => {
    await page.goto('/iframe-example');
    
    // ✅ Get iframe by URL
    const iframe = page.frameLocator('iframe[src*="payment"]');
    
    // ✅ Interact with elements inside iframe
    await iframe.getByLabel('Card Number').fill('4242424242424242');
    await iframe.getByLabel('Expiry').fill('12/25');
    await iframe.getByLabel('CVV').fill('123');
    await iframe.getByRole('button', { name: 'Pay' }).click();
    
    // ✅ Alternative: Get frame by name
    const namedFrame = page.frame('payment-frame');
    if (namedFrame) {
      await namedFrame.fill('[name="cardNumber"]', '4242424242424242');
    }
  });

  test('should handle new tabs/windows', async ({ context, page }) => {
    await page.goto('/home');
    
    // ✅ Listen for new page (tab/window)
    const [newPage] = await Promise.all([
      context.waitForEvent('page'),
      page.getByRole('link', { name: 'Open in New Tab' }).click(),
    ]);
    
    // ✅ Wait for new page to load
    await newPage.waitForLoadState('networkidle');
    
    // ✅ Interact with new page
    await expect(newPage.getByText('New Tab Content')).toBeVisible();
    await expect(newPage).toHaveTitle('New Page');
    
    // ✅ Close new page
    await newPage.close();
  });

  test('should handle dialogs (alert, confirm, prompt)', async ({ page }) => {
    // ✅ Handle alert
    page.on('dialog', async dialog => {
      expect(dialog.type()).toBe('alert');
      expect(dialog.message()).toBe('This is an alert!');
      await dialog.accept();
    });
    await page.getByRole('button', { name: 'Show Alert' }).click();
    
    // ✅ Handle confirm
    page.on('dialog', async dialog => {
      expect(dialog.type()).toBe('confirm');
      await dialog.accept(); // or dialog.dismiss()
    });
    await page.getByRole('button', { name: 'Confirm Action' }).click();
    
    // ✅ Handle prompt
    page.on('dialog', async dialog => {
      expect(dialog.type()).toBe('prompt');
      await dialog.accept('My answer');
    });
    await page.getByRole('button', { name: 'Enter Name' }).click();
  });
});

// ===================================================
// 🎯 **ACCESSIBILITY TESTING** (Playwright + axe)
// ===================================================

import AxeBuilder from '@axe-core/playwright';

test.describe('Accessibility', () => {
  test('should not have accessibility violations', async ({ page }) => {
    await page.goto('/');
    
    // ✅ Run axe accessibility scan
    const accessibilityScanResults = await new AxeBuilder({ page }).analyze();
    
    // ✅ Assert no violations
    expect(accessibilityScanResults.violations).toEqual([]);
  });

  test('should scan specific regions', async ({ page }) => {
    await page.goto('/');
    
    // ✅ Scan only header
    const results = await new AxeBuilder({ page })
      .include('header')
      .analyze();
    
    expect(results.violations).toEqual([]);
  });

  test('should exclude specific elements', async ({ page }) => {
    await page.goto('/');
    
    // ✅ Exclude third-party widgets from scan
    const results = await new AxeBuilder({ page })
      .exclude('#third-party-widget')
      .analyze();
    
    expect(results.violations).toEqual([]);
  });

  test('should be keyboard navigable', async ({ page }) => {
    await page.goto('/form');
    
    // ✅ Test keyboard navigation
    await page.keyboard.press('Tab');
    await expect(page.getByLabel('Name')).toBeFocused();
    
    await page.keyboard.press('Tab');
    await expect(page.getByLabel('Email')).toBeFocused();
    
    await page.keyboard.press('Tab');
    await expect(page.getByRole('button', { name: 'Submit' })).toBeFocused();
    
    // ✅ Activate with keyboard
    await page.keyboard.press('Enter');
  });

  test('should have proper ARIA labels', async ({ page }) => {
    await page.goto('/');
    
    // ✅ Check ARIA attributes
    await expect(page.getByRole('navigation')).toHaveAttribute('aria-label', 'Main navigation');
    await expect(page.getByRole('main')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Menu' })).toHaveAttribute('aria-expanded', 'false');
  });
});

// ===================================================
// 🔐 **AUTHENTICATION STATE REUSE**
// ===================================================

// auth.setup.ts
import { test as setup, expect } from '@playwright/test';

const authFile = 'playwright/.auth/user.json';

// ✅ Setup authentication state
setup('authenticate', async ({ page }) => {
  await page.goto('/login');
  await page.getByLabel('Email').fill('admin@example.com');
  await page.getByLabel('Password').fill('password123');
  await page.getByRole('button', { name: 'Login' }).click();
  
  // ✅ Wait for successful login
  await page.waitForURL('**/dashboard');
  await expect(page.getByText('Welcome')).toBeVisible();
  
  // ✅ Save authentication state to file
  await page.context().storageState({ path: authFile });
});

// ✅ Configure in playwright.config.ts
export default defineConfig({
  projects: [
    // Setup project
    { name: 'setup', testMatch: /.*\.setup\.ts/ },
    
    // Test project that depends on setup
    {
      name: 'chromium',
      use: {
        ...devices['Desktop Chrome'],
        storageState: authFile, // Reuse auth state
      },
      dependencies: ['setup'], // Run setup first
    },
  ],
});

// ✅ Use in tests (already authenticated)
test('should access protected page', async ({ page }) => {
  // ✅ Already authenticated from storage state
  await page.goto('/admin');
  await expect(page.getByText('Admin Panel')).toBeVisible();
});

// ===================================================
// 📊 **PERFORMANCE METRICS & WEB VITALS**
// ===================================================

test.describe('Performance', () => {
  test('should measure page load time', async ({ page }) => {
    const startTime = Date.now();
    
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    
    const loadTime = Date.now() - startTime;
    
    // ✅ Assert load time under threshold
    expect(loadTime).toBeLessThan(3000); // 3 seconds
    console.log(`Page loaded in ${loadTime}ms`);
  });

  test('should collect Web Vitals (LCP, FCP, CLS)', async ({ page }) => {
    await page.goto('/');
    
    // ✅ Wait for page to fully load
    await page.waitForLoadState('networkidle');
    
    // ✅ Get performance metrics
    const metrics = await page.evaluate(() => {
      return new Promise<any>((resolve) => {
        const vitals: any = {};
        
        // First Contentful Paint
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          vitals.FCP = entries.find((e: any) => e.name === 'first-contentful-paint')?.startTime;
        }).observe({ entryTypes: ['paint'] });
        
        // Largest Contentful Paint
        new PerformanceObserver((list) => {
          const entries = list.getEntries();
          vitals.LCP = entries[entries.length - 1].startTime;
        }).observe({ entryTypes: ['largest-contentful-paint'] });
        
        // Cumulative Layout Shift
        new PerformanceObserver((list) => {
          let cls = 0;
          list.getEntries().forEach((entry: any) => {
            if (!entry.hadRecentInput) {
              cls += entry.value;
            }
          });
          vitals.CLS = cls;
        }).observe({ entryTypes: ['layout-shift'] });
        
        // Resolve after 2 seconds
        setTimeout(() => resolve(vitals), 2000);
      });
    });
    
    console.log('Web Vitals:', metrics);
    
    // ✅ Assert thresholds
    expect(metrics.FCP).toBeLessThan(2000); // 2s
    expect(metrics.LCP).toBeLessThan(2500); // 2.5s
    expect(metrics.CLS).toBeLessThan(0.1); // 0.1
  });

  test('should measure Time to Interactive', async ({ page }) => {
    await page.goto('/');
    
    const tti = await page.evaluate(() => {
      return performance.timing.domInteractive - performance.timing.navigationStart;
    });
    
    expect(tti).toBeLessThan(5000);
    console.log(`Time to Interactive: ${tti}ms`);
  });
});

// ===================================================
// 🔄 **PARALLEL EXECUTION & SHARDING**
// ===================================================

// playwright.config.ts
export default defineConfig({
  // ✅ Run tests in parallel across multiple workers
  workers: process.env.CI ? 2 : 4,
  
  // ✅ Run tests in files in parallel
  fullyParallel: true,
});

// ✅ Run tests with sharding (split across CI machines)
// Machine 1: npx playwright test --shard=1/3
// Machine 2: npx playwright test --shard=2/3
// Machine 3: npx playwright test --shard=3/3

// ✅ Mark tests as serial (run one at a time)
test.describe.serial('Serial tests', () => {
  test('test 1', async ({ page }) => {
    // This will run first
  });
  
  test('test 2', async ({ page }) => {
    // This will run after test 1
  });
});

// ===================================================
// 🐛 **DEBUGGING TECHNIQUES**
// ===================================================

test('debugging example', async ({ page }) => {
  // ✅ 1. Pause test execution (opens Playwright Inspector)
  await page.pause();
  
  // ✅ 2. Slow down execution
  await page.goto('/', { waitUntil: 'networkidle', timeout: 60000 });
  
  // ✅ 3. Screenshot for debugging
  await page.screenshot({ path: 'debug.png', fullPage: true });
  
  // ✅ 4. Get page HTML
  const html = await page.content();
  console.log(html);
  
  // ✅ 5. Console logs from page
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  
  // ✅ 6. Network requests
  page.on('request', request => console.log('>>', request.method(), request.url()));
  page.on('response', response => console.log('<<', response.status(), response.url()));
  
  // ✅ 7. Step-by-step with --debug flag
  // npx playwright test --debug
  
  // ✅ 8. Headed mode (see browser)
  // npx playwright test --headed
  
  // ✅ 9. Trace viewer (timeline of actions)
  // npx playwright show-trace trace.zip
});

// ===================================================
// 🎯 **BEST PRACTICES SUMMARY**
// ===================================================

/*
✅ PLAYWRIGHT BEST PRACTICES:

1. Locator Strategy:
   - Prefer getByRole, getByLabel, getByText (user-facing)
   - Use getByTestId as last resort
   - Avoid CSS selectors & XPath

2. Auto-waiting:
   - Playwright auto-waits for elements to be actionable
   - No need for explicit sleeps/waits in most cases
   - Use waitForLoadState('networkidle') for dynamic content

3. Parallelization:
   - Run tests in parallel for faster execution
   - Use sharding for distributed CI
   - Mark dependent tests as .serial

4. Authentication:
   - Reuse auth state across tests
   - Setup auth once in global setup
   - Save storage state to file

5. API Mocking:
   - Mock APIs for faster, more reliable tests
   - Test error scenarios easily
   - Isolate frontend from backend

6. Page Object Model:
   - Encapsulate page logic in classes
   - Reuse across multiple tests
   - Easier to maintain

7. Visual Regression:
   - Screenshot critical pages
   - Mask dynamic content (timestamps, IDs)
   - Test multiple viewports

8. Accessibility:
   - Run axe scans on all pages
   - Test keyboard navigation
   - Verify ARIA attributes

9. Performance:
   - Measure Web Vitals (LCP, FCP, CLS)
   - Set performance budgets
   - Track over time in CI

10. Debugging:
    - Use --debug flag
    - Enable trace on failure
    - Check screenshots & videos
*/
```

### **4.2. Cypress E2E Tests**

```typescript
// ===================================================
// 🌲 **CYPRESS E2E TEST** (login.cy.ts)
// ===================================================

describe('Login Flow', () => {
  beforeEach(() => {
    cy.visit('/login');
  });

  it('should login successfully', () => {
    // ✅ Intercept API call
    cy.intercept('POST', '/api/auth/login', {
      statusCode: 200,
      body: {
        user: { id: '1', name: 'Admin', email: 'admin@example.com' },
        token: 'fake-jwt-token',
      },
    }).as('loginRequest');

    // ✅ Fill form
    cy.findByLabelText('Email').type('admin@example.com');
    cy.findByLabelText('Password').type('password123');
    
    // ✅ Submit
    cy.findByRole('button', { name: 'Login' }).click();
    
    // ✅ Wait for API call
    cy.wait('@loginRequest');
    
    // ✅ Verify redirect
    cy.url().should('include', '/dashboard');
    cy.findByText('Welcome, Admin').should('be.visible');
  });

  it('should handle login failure', () => {
    // ✅ Mock failed response
    cy.intercept('POST', '/api/auth/login', {
      statusCode: 401,
      body: { error: 'Invalid credentials' },
    }).as('loginRequest');

    cy.findByLabelText('Email').type('wrong@example.com');
    cy.findByLabelText('Password').type('wrongpassword');
    cy.findByRole('button', { name: 'Login' }).click();
    
    cy.wait('@loginRequest');
    
    // ✅ Error should display
    cy.findByText('Invalid credentials').should('be.visible');
  });
});

// ===================================================
// 🔧 **CUSTOM CYPRESS COMMANDS** (commands.ts)
// ===================================================

declare global {
  namespace Cypress {
    interface Chainable {
      login(email: string, password: string): Chainable<void>;
      clearCart(): Chainable<void>;
    }
  }
}

// ✅ Custom login command
Cypress.Commands.add('login', (email: string, password: string) => {
  cy.session([email, password], () => {
    cy.visit('/login');
    cy.findByLabelText('Email').type(email);
    cy.findByLabelText('Password').type(password);
    cy.findByRole('button', { name: 'Login' }).click();
    cy.url().should('include', '/dashboard');
  });
});

// ✅ Custom clear cart command
Cypress.Commands.add('clearCart', () => {
  cy.window().then(win => {
    win.localStorage.removeItem('cart');
  });
});

// ===================================================
// 🎯 **USAGE: Custom Commands**
// ===================================================

describe('Dashboard', () => {
  beforeEach(() => {
    // ✅ Use custom login command
    cy.login('admin@example.com', 'password123');
    cy.visit('/dashboard');
  });

  it('should display user stats', () => {
    cy.findByText('Total Orders').should('be.visible');
    cy.findByTestId('order-count').should('have.text', '42');
  });
});
```

---

## 5. Visual Regression Testing

### **5.1. Chromatic Visual Testing**

```typescript
// ===================================================
// 📸 **STORYBOOK STORIES** (Button.stories.tsx)
// ===================================================

import type { Meta, StoryObj } from '@storybook/react';
import { Button } from './Button';

const meta: Meta<typeof Button> = {
  title: 'Components/Button',
  component: Button,
  parameters: {
    layout: 'centered',
    // ✅ Chromatic configuration
    chromatic: {
      viewports: [320, 768, 1200], // Test multiple viewports
      delay: 300, // Wait for animations
    },
  },
};

export default meta;
type Story = StoryObj<typeof Button>;

// ✅ Stories for visual regression testing
export const Primary: Story = {
  args: {
    variant: 'primary',
    children: 'Primary Button',
  },
};

export const Secondary: Story = {
  args: {
    variant: 'secondary',
    children: 'Secondary Button',
  },
};

export const Disabled: Story = {
  args: {
    variant: 'primary',
    disabled: true,
    children: 'Disabled Button',
  },
};

export const Loading: Story = {
  args: {
    variant: 'primary',
    loading: true,
    children: 'Loading...',
  },
};

// ✅ Interaction test story
export const Hover: Story = {
  args: {
    variant: 'primary',
    children: 'Hover Me',
  },
  play: async ({ canvasElement }) => {
    const canvas = within(canvasElement);
    const button = canvas.getByRole('button');
    await userEvent.hover(button);
  },
};
```

```yaml
# ===================================================
# 🚀 **CHROMATIC CI WORKFLOW** (.github/workflows/chromatic.yml)
# ===================================================

name: Chromatic

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  chromatic:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0 # Full git history for Chromatic

      - uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci

      - name: Publish to Chromatic
        uses: chromaui/action@v1
        with:
          projectToken: ${{ secrets.CHROMATIC_PROJECT_TOKEN }}
          buildScriptName: build-storybook
          exitZeroOnChanges: true # Don't fail on visual changes
          autoAcceptChanges: main # Auto-accept on main branch
```

---

## 6. Performance Testing

### **6.1. Lighthouse CI**

```javascript
// ===================================================
// ⚡ **LIGHTHOUSE CI CONFIG** (lighthouserc.js)
// ===================================================

module.exports = {
  ci: {
    collect: {
      // ✅ URLs to test
      url: [
        'http://localhost:3000',
        'http://localhost:3000/products',
        'http://localhost:3000/dashboard',
      ],
      numberOfRuns: 3, // Run 3 times and average results
      settings: {
        preset: 'desktop',
        // Custom Chrome flags
        chromeFlags: '--no-sandbox --disable-gpu',
      },
    },
    assert: {
      // ✅ Performance budgets
      assertions: {
        'categories:performance': ['error', { minScore: 0.9 }],
        'categories:accessibility': ['error', { minScore: 0.9 }],
        'categories:best-practices': ['error', { minScore: 0.9 }],
        'categories:seo': ['error', { minScore: 0.9 }],

        // ✅ Core Web Vitals
        'first-contentful-paint': ['error', { maxNumericValue: 2000 }],
        'largest-contentful-paint': ['error', { maxNumericValue: 2500 }],
        'cumulative-layout-shift': ['error', { maxNumericValue: 0.1 }],
        'total-blocking-time': ['error', { maxNumericValue: 300 }],

        // ✅ Resource budgets
        'resource-summary:script:size': ['error', { maxNumericValue: 300000 }], // 300KB
        'resource-summary:image:size': ['error', { maxNumericValue: 500000 }],  // 500KB
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
```

---

## 7. TDD/BDD Methodology

### **7.1. Test-Driven Development (TDD)**

```typescript
// ===================================================
// 🔴 **RED PHASE** - Write failing test first
// ===================================================

import { describe, it, expect } from 'vitest';
import { sum } from './calculator';

describe('sum', () => {
  it('should add two numbers', () => {
    expect(sum(2, 3)).toBe(5); // ❌ FAIL: sum is not defined
  });
});

// ===================================================
// 🟢 **GREEN PHASE** - Write minimal code to pass
// ===================================================

export function sum(a: number, b: number): number {
  return a + b; // ✅ PASS
}

// ===================================================
// ♻️ **REFACTOR PHASE** - Improve code quality
// ===================================================

// Add more tests
it('should handle negative numbers', () => {
  expect(sum(-5, 3)).toBe(-2);
});

it('should handle decimals', () => {
  expect(sum(0.1, 0.2)).toBeCloseTo(0.3);
});

// Refactor if needed (e.g., add type safety, error handling)
export function sum(a: number, b: number): number {
  if (typeof a !== 'number' || typeof b !== 'number') {
    throw new TypeError('Both arguments must be numbers');
  }
  return a + b;
}
```

### **7.2. Behavior-Driven Development (BDD)**

```typescript
// ===================================================
// 🥒 **CUCUMBER-STYLE BDD** (login.feature)
// ===================================================

Feature: User Login
  As a user
  I want to log in to the application
  So that I can access my account

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter "admin@example.com" in the email field
    And I enter "password123" in the password field
    And I click the "Login" button
    Then I should be redirected to the dashboard
    And I should see "Welcome, Admin"

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter "wrong@example.com" in the email field
    And I enter "wrongpassword" in the password field
    And I click the "Login" button
    Then I should see an error message "Invalid credentials"
    And I should remain on the login page

// ===================================================
// ✅ **STEP DEFINITIONS** (login.steps.ts)
// ===================================================

import { Given, When, Then } from '@cucumber/cucumber';
import { expect } from '@playwright/test';

Given('I am on the login page', async function () {
  await this.page.goto('http://localhost:3000/login');
});

When('I enter {string} in the email field', async function (email: string) {
  await this.page.getByLabel('Email').fill(email);
});

When('I enter {string} in the password field', async function (password: string) {
  await this.page.getByLabel('Password').fill(password);
});

When('I click the {string} button', async function (buttonName: string) {
  await this.page.getByRole('button', { name: buttonName }).click();
});

Then('I should be redirected to the dashboard', async function () {
  await expect(this.page).toHaveURL(/.*dashboard/);
});

Then('I should see {string}', async function (text: string) {
  await expect(this.page.getByText(text)).toBeVisible();
});
```

---

## 8. CI/CD Integration

### **8.1. GitHub Actions Workflow**

```yaml
# ===================================================
# 🚀 **COMPLETE CI/CD PIPELINE** (.github/workflows/ci.yml)
# ===================================================

name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  # ✅ JOB 1: Unit & Integration Tests
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: 18
          cache: 'npm'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm run test:unit -- --coverage
      
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          files: ./coverage/coverage-final.json
          flags: unittests
          name: codecov-umbrella
      
      - name: Check coverage thresholds
        run: npm run test:coverage

  # ✅ JOB 2: E2E Tests
  e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Install dependencies
        run: npm ci
      
      - name: Install Playwright browsers
        run: npx playwright install --with-deps
      
      - name: Build app
        run: npm run build
      
      - name: Run E2E tests
        run: npm run test:e2e
      
      - name: Upload Playwright report
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: playwright-report
          path: playwright-report/
          retention-days: 30

  # ✅ JOB 3: Lighthouse Performance
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build app
        run: npm run build
      
      - name: Run Lighthouse CI
        run: |
          npm install -g @lhci/cli
          lhci autorun
        env:
          LHCI_GITHUB_APP_TOKEN: ${{ secrets.LHCI_GITHUB_APP_TOKEN }}

  # ✅ JOB 4: Visual Regression
  visual:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - uses: actions/setup-node@v3
        with:
          node-version: 18
      
      - name: Install dependencies
        run: npm ci
      
      - name: Publish to Chromatic
        uses: chromaui/action@v1
        with:
          projectToken: ${{ secrets.CHROMATIC_PROJECT_TOKEN }}
          buildScriptName: build-storybook
```

---

## 📚 **Best Practices Summary**

```typescript
// ===================================================
// ✅ **TESTING BEST PRACTICES CHECKLIST**
// ===================================================

const TESTING_BEST_PRACTICES = {
  general: [
    '✅ Follow AAA pattern: Arrange, Act, Assert',
    '✅ Test behavior, not implementation',
    '✅ Keep tests independent and isolated',
    '✅ Use descriptive test names',
    '✅ One assertion per test (when possible)',
    '✅ Avoid test interdependence',
  ],

  unitTests: [
    '✅ Test pure functions first',
    '✅ Mock external dependencies',
    '✅ Test edge cases and error scenarios',
    '✅ Aim for 80%+ coverage on critical code',
    '✅ Use parameterized tests for similar cases',
  ],

  integrationTests: [
    '✅ Test user interactions, not implementation',
    '✅ Use data-testid sparingly (prefer semantic queries)',
    '✅ Test accessibility (ARIA roles, labels)',
    '✅ Mock API calls at the network level',
    '✅ Clean up after each test',
  ],

  e2eTests: [
    '✅ Test critical user journeys only',
    '✅ Use Page Object Model for maintainability',
    '✅ Run on multiple browsers/viewports',
    '✅ Implement retry logic for flaky tests',
    '✅ Keep E2E tests under 10% of total tests',
  ],

  performance: [
    '✅ Run tests in parallel',
    '✅ Use watch mode during development',
    '✅ Cache dependencies in CI',
    '✅ Skip expensive setup for unit tests',
    '✅ Profile slow tests and optimize',
  ],
};
```

---

## 🎯 **Interview Questions**

```markdown
### **General Testing Strategy**

1. **Giải thích Test Pyramid và tại sao nó quan trọng?**
   → 60% Unit (fast, isolated, test business logic)
   → 30% Integration (medium speed, test component interactions)
   → 10% E2E (slow, expensive, test critical user flows)
   → Unit tests cheap & fast, E2E tests expensive & brittle
   → Focus testing effort where it provides most value

2. **Khi nào dùng shallow vs mount trong React testing?**
   → Không dùng shallow (deprecated in RTL)
   → Dùng render() từ @testing-library/react
   → Test component như user tương tác (behavior, not implementation)
   → Shallow testing violates testing best practices

3. **Làm sao test async code?**
   → async/await trong test functions
   → waitFor() cho React state updates
   → findBy queries (built-in async)
   → Mock timers với vi.useFakeTimers() cho setTimeout/setInterval
   → page.waitForResponse() trong Playwright

4. **Code coverage 100% có đảm bảo code tốt không?**
   → Không! Coverage là metric, không phải mục tiêu
   → Quan trọng là test quality (edge cases, error scenarios)
   → 100% coverage không test business logic correctness
   → Focus on critical paths, 80-90% coverage là đủ
   → Mutation testing để test quality of tests

### **Playwright-Specific Questions**

5. **Playwright vs Cypress - Ưu nhược điểm?**
   
   **Playwright:**
   ✅ Multi-browser: Chromium, Firefox, WebKit (Safari)
   ✅ Faster: Auto-wait, parallel execution, sharding
   ✅ Better API mocking: Route interception built-in
   ✅ Multi-tab/iframe: Better support
   ✅ Mobile testing: Real device emulation
   ❌ Smaller community than Cypress
   ❌ Less intuitive time-travel debugging
   
   **Cypress:**
   ✅ Better DX: Time-travel debugging, great documentation
   ✅ Easier to learn: Simpler API
   ✅ Larger community: More plugins, examples
   ❌ Chromium-based only (Firefox experimental)
   ❌ No multi-tab support
   ❌ Slower execution (runs in browser)
   
   → **Chọn Playwright** cho: Enterprise, multi-browser, performance critical
   → **Chọn Cypress** cho: Simplicity, better DX, Chrome-only OK

6. **Giải thích auto-waiting trong Playwright. Tại sao nó quan trọng?**
   → Playwright tự động chờ elements actionable trước khi interact
   → Actionable = visible + enabled + stable + receives events
   → Không cần explicit waits (page.waitForSelector) trong hầu hết cases
   → Giảm flaky tests do timing issues
   → Ví dụ: await page.click('button') auto-waits cho button visible & enabled

7. **Làm sao handle flaky E2E tests?**
   → Enable retries: `retries: 2` trong playwright.config
   → Use auto-waiting (Playwright built-in)
   → Avoid hard-coded timeouts (use waitForLoadState)
   → Mock APIs to remove external dependencies
   → Use strict locators (getByRole vs CSS selectors)
   → Test isolation: Reset state before each test
   → Run in headed mode to debug: `--headed`
   → Check traces: `trace: 'on-first-retry'`

8. **Locator strategy tốt nhất trong Playwright?**
   → Priority order:
   1. getByRole() - Accessibility-friendly, resilient
   2. getByLabel() - Form inputs
   3. getByPlaceholder() - Alternative for inputs
   4. getByText() - Visible text
   5. getByTestId() - Last resort, requires test IDs
   ❌ Avoid: CSS selectors, XPath (brittle, implementation-dependent)
   
   → Example: `page.getByRole('button', { name: 'Submit' })`

9. **Giải thích Page Object Model (POM). Khi nào dùng?**
   → Design pattern: Encapsulate page logic trong classes
   → Benefits:
     - Reusability: Dùng across multiple tests
     - Maintainability: Update selectors ở một nơi
     - Readability: Test code cleaner
   → Dùng khi: Many tests interact with same page
   → Không dùng khi: Simple tests, overkill for small projects
   
   ```typescript
   class LoginPage {
     constructor(page) { this.page = page; }
     async login(email, password) { ... }
   }
   ```

10. **Làm sao test authentication flows trong Playwright?**
    → Strategy 1: Login in beforeEach (slow, repetitive)
    → Strategy 2: **Reuse auth state** (recommended)
      - Login once in global setup
      - Save storageState to file
      - Reuse across all tests
      - Fast, no repeated logins
    
    ```typescript
    // Save auth
    await context.storageState({ path: 'auth.json' });
    // Reuse auth
    use: { storageState: 'auth.json' }
    ```

11. **Làm sao mock APIs trong Playwright?**
    → Use page.route() to intercept network requests
    → Mock responses with route.fulfill()
    → Simulate errors with route.abort()
    → Modify requests with route.continue()
    
    ```typescript
    await page.route('**/api/users', route => {
      route.fulfill({ status: 200, body: JSON.stringify([...]) });
    });
    ```
    
    → Benefits: Faster tests, test error scenarios, isolate frontend

12. **Parallel testing trong Playwright - Best practices?**
    → Enable `fullyParallel: true` in config
    → Set workers: `workers: 4` (number of parallel processes)
    → Use sharding for CI: `--shard=1/3` (split across machines)
    → Ensure test isolation (no shared state)
    → Use separate browser contexts per test
    → Mark dependent tests as `.serial`
    → Parallel = faster CI, better resource utilization

13. **Làm sao debug failed Playwright tests?**
    → Techniques:
    1. Run with --debug: Opens Playwright Inspector
    2. Run headed: --headed to see browser
    3. Use page.pause(): Pause execution
    4. Screenshots: `screenshot: 'on-failure'`
    5. Videos: `video: 'retain-on-failure'`
    6. Traces: `trace: 'on-first-retry'` → view with `npx playwright show-trace`
    7. Console logs: `page.on('console', msg => console.log(msg))`
    8. Slow mode: `--slowmo=1000` (slow down by 1s per action)

14. **Visual regression testing với Playwright - How it works?**
    → Use `expect(page).toHaveScreenshot('name.png')`
    → First run: Creates baseline screenshot
    → Subsequent runs: Compare against baseline
    → Diff detected: Test fails, shows visual diff
    → Update baselines: `--update-snapshots`
    → Tips:
      - Disable animations: `animations: 'disabled'`
      - Mask dynamic content: timestamps, IDs
      - Test multiple viewports: mobile, tablet, desktop
      - Use in CI to catch visual regressions

15. **Accessibility testing trong Playwright?**
    → Integrate @axe-core/playwright
    → Run automated a11y scans: `new AxeBuilder({ page }).analyze()`
    → Check violations: WCAG compliance
    → Test keyboard navigation: Tab order, focus management
    → Verify ARIA attributes: roles, labels
    → Test screen reader compatibility
    → Benefits: Catch a11y issues early, improve UX for all users

### **Advanced Testing Concepts**

16. **Test-Driven Development (TDD) - Workflow?**
    → 🔴 Red: Write failing test first
    → 🟢 Green: Write minimal code to pass
    → ♻️ Refactor: Improve code quality
    → Repeat cycle
    → Benefits: Better design, higher confidence, living documentation
    → Best for: Business logic, algorithms, pure functions

17. **Contract testing vs E2E testing?**
    → Contract testing: Verify API contracts between services
    → E2E testing: Test entire user flow through UI
    → Contract testing: Faster, isolated, tests API compatibility
    → E2E testing: Slower, tests integration of all components
    → Use both: Contract tests for APIs, E2E for critical flows
    → Tools: Pact (contract), Playwright (E2E)

18. **Mutation testing - What & Why?**
    → Tests your tests! Introduces code mutations (bugs)
    → If tests still pass → tests are weak
    → If tests fail → tests caught the mutation ✅
    → Tools: Stryker
    → Example: Change `>` to `>=`, does test catch it?
    → Benefits: Improve test quality, find missing test cases

19. **Component testing vs Integration testing?**
    → Component testing: Test components in isolation (Playwright CT)
    → Integration testing: Test components with dependencies (RTL)
    → Component testing: Fast, visual testing, no mocks needed
    → Integration testing: Tests real interactions, includes context
    → Use both: Component tests for UI, integration for logic

20. **CI/CD best practices for E2E tests?**
    → Run unit/integration tests on every PR
    → Run E2E tests on merge to main (not every commit)
    → Use sharding to parallelize in CI
    → Retry failed tests (retries: 2)
    → Separate test stages: unit → integration → E2E
    → Cache dependencies: Playwright browsers
    → Upload artifacts: Screenshots, videos, traces
    → Set timeouts: Prevent hanging CI jobs
    → Monitor flakiness: Track & fix flaky tests
```

---

**🎯 Remember:** 

> **"Write tests. Not too many. Mostly integration."** - Kent C. Dodds
> 
> **"Test behavior, not implementation."** - Testing Library
> 
> **"Playwright auto-waits, so you don't have to."** - Playwright Docs
